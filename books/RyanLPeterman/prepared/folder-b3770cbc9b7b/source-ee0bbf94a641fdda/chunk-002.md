Chunk 2; segments 330–651. Start may repeat the previous chunk for context.

# Uber Distinguished Eng: Unfair Promos, Influence, Engineering Regrets | Joakim Recht

Source ID: source-ee0bbf94a641fdda
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Uber_Distinguished_Eng_Unfair_Promos,_Influence,_Engineering_Regrets_Joakim_Recht_en.txt
Video: https://www.youtube.com/watch?v=feNh_ubBAMI

[L339] [12:28.24] really hard. Um, and that's of course
[L340] [12:30.72] pretty annoying. Uh, so you so that that
[L341] [12:34.00] that from like a local team perspective
[L342] [12:36.32] can be like quite frustrating if you
[L343] [12:39.36] then have to like you have tooling that
[L344] [12:40.88] kind of works and now you have to
[L345] [12:42.56] rebuild it in in a very different
[L346] [12:44.08] paradigm and it seems like a bit waste
[L347] [12:46.40] of time but it really isn't because you
[L348] [12:47.92] get that you get that large scale
[L349] [12:50.16] benefit uh because you also you get a
[L350] [12:52.96] lot of stuff for free. Like for example,
[L351] [12:54.80] at some point we were like, okay, we
[L352] [12:56.48] built the basic platform.
[L353] [12:58.64] Now let's look at at NUMA. NUMA is the
[L354] [13:01.68] whole like how does memory attach GCPUs?
[L355] [13:04.32] Uh because if you're running databases
[L356] [13:06.56] particular stuff that needs to do a lot
[L357] [13:08.40] of data shuffling, it's nice that the
[L358] [13:10.72] memory is aligned with the CPU that the
[L359] [13:12.56] process is running on. So how do you
[L360] [13:14.40] kind of make that happen uh in a nice
[L361] [13:16.48] way? Also from a scheduling perspective
[L362] [13:18.56] like when you need to do feature
[L363] [13:19.68] optimization, you also need to take that
[L364] [13:21.52] into account. both the actual runtime
[L365] [13:24.48] needs to the kind of schedule that we
[L366] [13:26.56] have the ability to schedule but also
[L367] [13:27.92] the like the actual scheduleuler needs
[L368] [13:29.60] to be able to seem how do we best
[L369] [13:32.24] allocate the CPUs to memory that's a
[L370] [13:34.72] pretty hard thing to do and it's not
[L371] [13:37.12] something you get around to doing
[L372] [13:38.24] yourself but when you have a platform
[L373] [13:39.52] like this you kind of get it for free
[L374] [13:41.20] and I think the more of this stuff we
[L375] [13:43.52] built the more people were like yeah
[L376] [13:45.12] that's pretty nice
[L377] [13:46.56] >> it sounds like this effort was uh kind
[L378] [13:48.72] of a bottoms up kind of effort where you
[L379] [13:52.00] and some engineers realize this is a
[L380] [13:54.16] good idea and then it gained traction
[L381] [13:56.16] gained traction. I'm curious like as the
[L382] [13:58.64] the initiative evolved like did
[L383] [14:00.64] leadership starting get involved at some
[L384] [14:02.32] point and how'd that evolve?
[L385] [14:04.24] >> We could really only get so far uh
[L386] [14:06.48] because especially because uh back then
[L387] [14:08.72] Uber like the stateful part of Uber was
[L388] [14:11.28] basically split into two. One was like
[L389] [14:13.28] the online real online uh databases uh
[L390] [14:17.20] my SQL Postgress uh Cassandra stuff like
[L391] [14:19.68] that and then there was all the data
[L392] [14:21.76] stack uh ACFS Kafka Pino all that stuff
[L393] [14:25.44] and that ran in a completely different
[L394] [14:27.36] orc we had no like like the management
[L395] [14:30.56] chain from that more or less went
[L396] [14:32.08] through the CEO and back down so they
[L397] [14:34.32] were like yeah this thing you're talking
[L398] [14:36.72] about it sounds pretty nice but we
[L399] [14:38.48] really don't care but but then at some
[L400] [14:40.88] point there were there was some a game
[L401] [14:42.64] going on but also
[L402] [14:45.76] we got more and more support up the
[L403] [14:48.08] management chain to like say this by now
[L404] [14:51.36] this is something you have to do at some
[L405] [14:52.80] point there was they just said okay this
[L406] [14:55.52] Odin thing is the future and you will
[L407] [14:59.28] not you will not be allowed to have your
[L408] [15:02.48] own servers any longer you want to run
[L409] [15:04.24] something that's where it runs um and
[L410] [15:07.60] that of course helped a little bit also
[L411] [15:08.96] with like uh adoption because you there
[L412] [15:12.88] will always be like if you have like the
[L413] [15:14.32] full button off thing there will al
[L414] [15:15.68] always be straers or people who are just
[L415] [15:17.52] like ah we don't want to or we have our
[L416] [15:19.28] own thing going it's super hard to like
[L417] [15:21.68] create like full alignments if you if
[L418] [15:24.00] you're just yourself uh no matter how
[L419] [15:26.00] nice the thing you have is there's
[L420] [15:27.76] always going to be somebody out there
[L421] [15:29.12] who's like ah
[L422] [15:30.24] >> yeah I mean it's it's a huge undertaking
[L423] [15:32.08] and I I feel like when you talk about
[L424] [15:34.56] the end state of the entire company the
[L425] [15:37.92] scale of databases all running through
[L426] [15:39.68] this one platform that distinguished
[L427] [15:42.08] scope makes a lot of sense. Um I'm
[L428] [15:44.56] curious for for people who are wanting
[L429] [15:46.96] to know about the career side of things
[L430] [15:48.80] like how did that look at each step when
[L431] [15:51.60] your career was growing through that?
[L432] [15:53.76] >> I think in general
[L433] [15:56.24] I think there many opinions opinions on
[L434] [15:58.72] what how you get promoted what what what
[L435] [16:00.96] triggers a promotion what I have like a
[L436] [16:03.36] somewhat uh maybe naive hope naive
[L437] [16:07.52] perspective on it that it's fairly fair.
[L438] [16:09.76] is not always fair, but it's pretty fair
[L439] [16:11.68] and it's tied to the scope of the work
[L440] [16:13.52] that you're doing, the kind of the
[L441] [16:15.76] amount of people you influence with what
[L442] [16:18.32] you're doing. Uh that's kind of that's
[L443] [16:20.48] how I see it. Um, and so like for
[L444] [16:24.08] something like Odin that had like this
[L445] [16:26.08] natural progression of first you're
[L446] [16:29.12] basically doing it inside your teams,
[L447] [16:30.88] then you're doing it inside your local
[L448] [16:32.48] org, then you're going doing it inside
[L449] [16:34.96] your um like the wider maybe platform or
[L450] [16:39.92] and then it goes even beyond that. And
[L451] [16:41.52] that that kind of reflects the the the
[L452] [16:45.60] like the the job level also like the the
[L453] [16:49.12] the more people you you have under your
[L454] [16:51.52] influence not like it's not like a
[L455] [16:53.68] direct influence but it's like the more
[L456] [16:55.20] people who are like affected by what you
[L457] [16:56.88] do well the the higher you get in the
[L458] [17:00.32] level. Uh so if you're actually able to
[L459] [17:04.16] kind of run a project of that scope to
[L460] [17:08.48] success then I think a promotion will
[L461] [17:11.60] happen or not not a promotion but a
[L462] [17:13.44] number of promotions will happen
[L463] [17:14.48] automatically and not just for you but
[L464] [17:16.00] the like the entire team it kind of
[L465] [17:18.00] drags a lot of people uh along. Uh, of
[L466] [17:21.52] course you can say I was maybe a bit
[L467] [17:24.08] lucky in the sense that I had a single
[L468] [17:26.72] project for a very long time and a lot
[L469] [17:28.80] of people kind of get shuffled around
[L470] [17:30.08] and then do a project or the project get
[L471] [17:32.40] cancelceled or fails and then you have
[L472] [17:33.76] to do something else. Uh, it gets much
[L473] [17:36.96] harder uh to kind of kind of write that
[L474] [17:41.68] expansion. Not impossible. I've seen
[L475] [17:43.52] many things where many is where where
[L476] [17:45.76] where it's definitely possible but but
[L477] [17:47.44] it's just it's much easier when like the
[L478] [17:50.48] project you're working on has that
[L479] [17:51.84] natural scope expansion. Uh so maybe my
[L480] [17:55.52] promotions in to a very large degree
[L481] [17:58.00] followed that work like first
[L482] [18:01.52] first I did some background so I did
[L483] [18:03.92] some other work before we got to to the
[L484] [18:05.52] whole stateful thing and then I did uh
[L485] [18:07.84] the the the first version of it. Uh, I
[L486] [18:11.04] think that got me a promotion and I did
[L487] [18:12.48] then then we did more and we kind of
[L488] [18:13.92] expanded to to standard MySQL and
[L489] [18:16.72] Cassandra and that that got me another
[L490] [18:18.80] promotion to
[L491] [18:21.84] I forget that because the title the
[L492] [18:23.60] title names changed a bit on the way.
[L493] [18:25.68] Um, but that probably got me to to
[L494] [18:28.32] principal engineer and then when we kind
[L495] [18:30.40] of only was more it wasn't done done but
[L496] [18:33.68] it was like sets like it really didn't
[L497] [18:35.76] require me any longer. was basically
[L498] [18:37.84] handed off hand off to to the to the
[L499] [18:40.80] team uh and I could do other things. Um
[L500] [18:44.40] and that basically took me to the to the
[L501] [18:46.24] distinguished uh engineer level. Um but
[L502] [18:49.60] it was a very natural progression. It
[L503] [18:51.68] was not a it was it was not a
[L504] [18:53.60] progression I was like it was not that's
[L505] [18:56.72] that was that was not the reason why we
[L506] [18:58.48] were doing it. Uh it was just it
[L507] [19:00.64] followed the work that we were doing um
[L508] [19:04.08] quite nicely.
[L509] [19:05.20] >> Right. I mean th those are the best
[L510] [19:07.28] kinds of promotions. It sounds like
[L511] [19:08.96] you're saying that the levels obviously
[L512] [19:11.36] they're tied to your impact which is
[L513] [19:13.52] tied to the scope of your influence. And
[L514] [19:16.16] so I guess the natural question then is
[L515] [19:18.64] what are the typical ways to have your
[L516] [19:21.36] work being influencing more and more
[L517] [19:23.68] engineers.
[L518] [19:24.88] >> So I have this personal thing and that
[L519] [19:27.36] is I just I just don't like doing things
[L520] [19:30.64] too many times.
[L521] [19:32.72] I just I really don't like it. Uh, and I
[L522] [19:36.80] think I might have written something
[L523] [19:37.84] about the the lazy engineer at some
[L524] [19:39.60] point which like yeah I I like putting
[L525] [19:42.64] these weird titles on things but the
[L526] [19:45.68] idea that if I've done something like
[L527] [19:48.72] for example I need to do if if I'm
[L528] [19:51.44] operating a database and I need to
[L529] [19:53.28] replace the host and I've done that
[L530] [19:54.80] manually a couple of times I'm like I
[L531] [19:56.48] this I don't want to do any longer. So I
[L532] [19:59.76] that needs to be automated to some
[L533] [20:01.20] degree or abracted away or whatever it
[L534] [20:02.80] might be. Uh and so I think that's it's
[L535] [20:06.72] not the only thing but I think for me
[L536] [20:08.48] that is a major driver because then I'm
[L537] [20:11.12] like why are we why do we have this
[L538] [20:13.04] waste in our systems or in our
[L539] [20:16.08] processes? Uh and I like when when you
[L540] [20:19.52] start thinking about maybe not just your
[L541] [20:21.12] own waste but also the waste of other
[L542] [20:24.24] people. I think that's where you kind of
[L543] [20:26.80] then you get into that scope expansion.
[L544] [20:29.84] Uh so you kind of start thinking about
[L545] [20:31.68] your own stuff then you team and you
[L546] [20:33.20] kind of expand from there. So like that
[L547] [20:35.52] that's that's how I think about it. I
[L548] [20:37.36] don't think about it as like and it's
[L549] [20:38.80] not like oh I need to like get promoted
[L550] [20:40.64] or whatever. It's just I just have this
[L551] [20:43.20] uh I just have this natural thing and it
[L552] [20:46.64] can be pretty annoying sometimes because
[L553] [20:47.92] you all you can kind of tend to rabbit
[L554] [20:49.92] hole a little bit also or it's like a
[L555] [20:52.40] what I what what we kind of call a depth
[L556] [20:54.64] first approach to everything. uh where
[L557] [20:57.20] like oh I'm doing this other thing but
[L558] [20:59.04] suddenly this is annoying me I need to
[L559] [21:00.96] build this tool oh but the tool is also
[L560] [21:02.96] annoying to build so I have to build
[L561] [21:04.08] this I have to build the build system or
[L562] [21:06.16] I have to improve the build system but
[L563] [21:07.36] the build system is also annoying so I
[L564] [21:08.56] have to like whatever and then you take
[L565] [21:09.84] it on a long chain of like [laughter]
[L566] [21:13.20] completely sidetracking what you what
[L567] [21:14.72] you should what you should be doing
[L568] [21:16.16] that's kind of the danger of it but I to
[L569] [21:20.16] me I I think it it just drives a lot of
[L570] [21:24.08] of this like how do you actually improve
[L571] [21:28.64] systematically and systemically like the
[L572] [21:32.88] company and the processes and and in
[L573] [21:35.44] particular your engineering
[L574] [21:36.32] organization. Uh that's why I'm focused
[L575] [21:39.28] but it can also touch other things but
[L576] [21:40.88] mainly engineering. I I see the natural
[L577] [21:43.60] leverage that comes from it because if
[L578] [21:45.28] you build some tooling or something like
[L579] [21:47.68] that that software can then act on your
[L580] [21:51.04] behalf and help others and then that's
[L581] [21:53.92] kind of how you scale yourself.
[L582] [21:55.52] >> Yeah. Yeah. And and yeah. So like we
[L583] [21:57.44] also talk about this whole thing about
[L584] [21:58.64] like yeah how do you scale yourself? How
[L585] [22:00.48] do you how do you come become a force
[L586] [22:02.16] multiplier? Uh and it's something I
[L587] [22:04.24] would like it's always like I don't know
[L588] [22:05.76] then you can mentor people or you can
[L589] [22:07.04] kind of whatever you can step we can
[L590] [22:09.76] start like
[L591] [22:12.24] doing more design so we can push that
[L592] [22:14.40] down. I like the idea of like you become
[L593] [22:17.44] a forceful supplier by allowing other
[L594] [22:19.68] people to work better and faster or
[L595] [22:23.68] maybe not even work at all ideally on
[L596] [22:25.52] the thing that they're working on. like
[L597] [22:27.04] take that problem away like think about
[L598] [22:28.64] how do how do we actually take the
[L599] [22:30.16] problem that you have like out of the
[L600] [22:32.00] equation because I think that's the most
[L601] [22:34.40] fundamental thing you can do like the
[L602] [22:36.24] thing you were doing if you don't have
[L603] [22:37.84] to do that any longer what could you
[L604] [22:39.52] then be doing you one thing you
[L605] [22:41.60] mentioned we're talking about promos is
[L606] [22:43.28] you said they're typically fair and
[L607] [22:46.08] they're based off of the impact of your
[L608] [22:48.00] work but I'm curious it sounds like you
[L609] [22:50.48] have some experience when promos are not
[L610] [22:52.64] fair or what what does it mean when
[L611] [22:54.80] you're saying promos are not fair
[L612] [22:56.24] sometimes times.
[L613] [22:57.20] >> Well, I think it can mean so it can mean
[L614] [22:58.96] a lot of things and like I've been part
[L615] [23:01.12] of promo committees for a very long
[L616] [23:02.72] time. Um, and the promo committee
[L617] [23:06.00] structure has also changed a lot uh from
[L618] [23:11.28] like the first time I was in a promo
[L619] [23:12.96] committee was I think the I wouldn't say
[L620] [23:15.28] one of the scariest experiences of my
[L621] [23:17.20] life. Uh but uh
[L622] [23:22.24] but I
[L623] [23:24.64] like so the first promo commission I was
[L624] [23:26.64] in was basically uh for the entire
[L625] [23:28.56] platform engineering. I forget how many
[L626] [23:30.16] we were but it was like all the managers
[L627] [23:32.56] and VPs and senior directors or whatever
[L628] [23:35.84] and senior engineers in a room for an
[L629] [23:38.48] entire day and then somebody asks okay
[L630] [23:42.88] let's go says let's go through all the
[L631] [23:45.20] candidates or wait let's actually go
[L632] [23:47.92] through all our employees all our
[L633] [23:50.08] engineers just all of them and then the
[L634] [23:53.92] manager talks about like where how good
[L635] [23:56.72] are they and should they get promoted
[L636] [23:58.96] And then we just let it just and there
[L637] [24:00.48] were like I don't know 200 or 5 500
[L638] [24:02.88] engineers like I insane number and we
[L639] [24:05.20] all and there was no preparation there
[L640] [24:06.72] was no material there was just like the
[L641] [24:08.88] manager saying what they thought and
[L642] [24:11.52] obviously they all thought that
[L643] [24:12.40] everybody should be promoted and then it
[L644] [24:14.40] was like okay uh and then we should have
[L645] [24:17.20] some kind of structure let's do some
[L646] [24:18.88] kind of point system or whatever like I
[L647] [24:21.20] is this how it works [laughter]
[L648] [24:24.96] and and and it was back then apparently
[L649] [24:27.12] and of course in in a setup like that it
[L650] [24:29.44] gets super unfair because it all it all
[L651] [24:31.28] depends on how good is your manager at
[L652] [24:33.12] presenting your case and if you have a
[L653] [24:34.88] [ __ ] manager you have a [ __ ] case
[L654] [24:38.16] you might also have a very good manager
[L655] [24:40.00] but your work is [ __ ] so like so in that
[L656] [24:43.52] sense there's a lot of unfairness going
[L657] [24:45.44] on uh which I think also kind of led to
[L658] [24:48.32] some of the early day Uber culture
[L659] [24:50.96] issues not just just that but it was
[L660] [24:53.84] kind of part of it um but anyway things
