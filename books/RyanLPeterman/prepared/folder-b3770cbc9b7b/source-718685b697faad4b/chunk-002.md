Chunk 2; segments 382–778. Start may repeat the previous chunk for context.

# Turing Award Winner: Disagreeing with Google, Postgres, Future Problems | Mike Stonebraker

Source ID: source-718685b697faad4b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Disagreeing_with_Google,_Postgres,_Future_Problems_Mike_Stonebraker_en.txt
Video: https://www.youtube.com/watch?v=YPObBOwIrHk

[L391] [18:08.08] warehouses that's table stakes so I
[L392] [18:11.44] think it's just as true today as it ever
[L393] [18:13.52] was I think that
[L394] [18:17.28] what is true
[L395] [18:19.52] is that if you want to get going, you
[L396] [18:21.92] have a database problem,
[L397] [18:24.64] you know, the answer is choose Postgress
[L398] [18:27.62] [snorts] and there's a huge programming
[L399] [18:29.84] community, all kinds of all kinds of,
[L400] [18:32.96] you know, data type implementations.
[L401] [18:35.76] it's free uh and you can find Postgress
[L402] [18:41.36] talent easily and get going
[L403] [18:44.72] and and so I think it's it's it's a
[L404] [18:47.68] great choice for lowest common
[L405] [18:49.36] denominator
[L406] [18:51.28] and until you're trying to do [snorts] a
[L407] [18:55.84] million transactions a second it works
[L408] [18:57.84] just fine until you're trying to support
[L409] [19:01.04] a pabyte data warehouse it it I say at
[L410] [19:03.92] the low end it it's absolutely
[L411] [19:05.44] Absolutely the right one sizefits-all at
[L412] [19:07.92] the low end it's Postgress at the high
[L413] [19:10.72] end that's just not true
[L414] [19:13.12] >> GPUs do they make available some new
[L415] [19:16.56] opportunities to optimize databases
[L416] [19:19.44] probably but I think the the big
[L417] [19:22.08] challenge is that GPUs are
[L418] [19:27.20] you know sum simd you know single
[L419] [19:29.92] instruction multi- data and that's
[L420] [19:32.64] that's the anathema of indexing
[L421] [19:36.08] And so whenever indexing is the right
[L422] [19:38.40] answer, they're probably not a good
[L423] [19:41.36] idea.
[L424] [19:43.44] And I think uh also you've got to
[L425] [19:47.76] architect them so that the so that the
[L426] [19:51.52] bandwidth
[L427] [19:53.44] so that the bandwidth from storage is is
[L428] [19:57.76] not not the bottleneck. And so if
[L429] [20:01.52] they're an add-on to the CPU as often as
[L430] [20:04.16] not the bus connecting it to the the GPU
[L431] [20:07.68] to the CPU is a bottleneck.
[L432] [20:10.08] >> Can you explain why indexing would be
[L433] [20:13.52] not as effective when there's SIMD?
[L434] [20:17.84] >> So let's let's say I'm I'm [snorts]
[L435] [20:21.60] looking for Ryan's
[L436] [20:24.40] I'm looking for Ryan's salary and I have
[L437] [20:26.56] a B tree.
[L438] [20:28.64] So you go to the root of the B tree.
[L439] [20:32.24] You find you find the divider that has
[L440] [20:36.16] both sides of Ryan.
[L441] [20:38.48] You follow the pointer.
[L442] [20:41.12] That's a memory access for sure. Then
[L443] [20:44.24] you do it all again and you do this like
[L444] [20:47.04] three or four times.
[L445] [20:49.28] So that doesn't parallelize well. So the
[L446] [20:52.00] answer is indexing doesn't parallelize
[L447] [20:54.24] well. You mentioned B trees. When you
[L448] [20:56.64] first implemented
[L449] [20:58.48] uh that first version of ingress, did
[L450] [21:01.36] you write all of that by hand? Because I
[L451] [21:03.84] imagine there's probably not some
[L452] [21:05.44] existing B tree library or something.
[L453] [21:08.16] >> Yeah, we wrote the original version of
[L454] [21:10.32] ingress was all written from scratch.
[L455] [21:12.96] >> What was the hardest part of that
[L456] [21:14.24] implementation?
[L457] [21:16.56] >> Uh query optimizer.
[L458] [21:18.56] >> And why was that hard?
[L459] [21:20.24] >> It's tough. It's it's just
[L460] [21:24.48] algorithmically difficult. It's still if
[L461] [21:27.68] you ask most any senior database
[L462] [21:30.88] programmer what's the hardest hardest
[L463] [21:33.44] part, they'll still say the optimizer.
[L464] [21:36.80] Map produce came out at some point in
[L465] [21:39.20] the early 2000s and it kind of took the
[L466] [21:41.68] data world by storm. People were really
[L467] [21:44.56] impressed by it. They thought Google
[L468] [21:46.40] really knows what they're doing. this is
[L469] [21:48.56] the best thing since sliced bread. But
[L470] [21:51.28] it seems like when I look at the
[L471] [21:53.92] literature and what you thought at the
[L472] [21:55.44] time, you kind of disagreed heavily. Why
[L473] [21:58.08] did you disagree so much with uh map
[L474] [22:00.80] produce?
[L475] [22:02.32] Well, I think
[L476] [22:04.80] there were a lot of
[L477] [22:07.28] not very enlightened people who said
[L478] [22:09.44] Google Google is really smart. They must
[L479] [22:12.32] know what they're doing and so we'll do
[L480] [22:15.36] whatever they say. And so they would
[L481] [22:18.40] they would uh they would engage in
[L482] [22:22.56] Hadoop or engage with Hadoop. But Hadoop
[L483] [22:26.16] is ridiculously inefficient. And so uh
[L484] [22:30.24] at the time,
[L485] [22:32.64] you know, others, you know, Dave Dwit
[L486] [22:34.64] and others who who were involved in our
[L487] [22:36.88] 2011 paper, we understood distributed
[L488] [22:40.56] databases
[L489] [22:42.72] and understood that you could beat the
[L490] [22:44.80] heck out of Hadoop.
[L491] [22:46.80] uh with a distributed database system,
[L492] [22:49.20] which is basically what that 2011 paper
[L493] [22:52.56] says.
[L494] [22:54.08] And of course, it was it's true. And
[L495] [22:58.24] but that wasn't the only that wasn't the
[L496] [23:01.60] only thing Google was stupid about.
[L497] [23:04.80] So Google also
[L498] [23:08.08] had the opinion that eventual
[L499] [23:11.44] consistency was the right way to do
[L500] [23:14.00] concurrency control.
[L501] [23:16.64] And so that was postulated from on high
[L502] [23:20.64] by Google all during that same period of
[L503] [23:23.68] time.
[L504] [23:25.36] And it it wasn't and all the database
[L505] [23:29.44] people said, you know, you're out of
[L506] [23:31.84] your frigin mind because it doesn't it
[L507] [23:36.24] solves one particular kind of problem
[L508] [23:38.80] but only and that very rarely occurs in
[L509] [23:41.84] practice. Why did they pursue eventual
[L510] [23:44.48] consistency?
[L511] [23:45.68] >> Okay, well the idea is that you have an
[L512] [23:47.76] east coast database and a west coast
[L513] [23:49.44] database and they're replicas. So you
[L514] [23:51.36] want them to be the same. If you say I'm
[L515] [23:56.00] going to do a transaction, I'm going to
[L516] [23:58.16] decrement by one the number of widgets
[L517] [24:01.36] in the west coast warehouse then I'm
[L518] [24:04.16] going to with before I commit that
[L519] [24:06.72] transaction I'm going to update the east
[L520] [24:09.44] coast warehouse pay pay a message over
[L521] [24:11.68] and back to update it and then to make
[L522] [24:15.36] sure everything goes well it takes a it
[L523] [24:17.68] takes another roundtrip a message to
[L524] [24:20.56] make sure that both of them actually do
[L525] [24:23.68] the commit correctly. So it's expensive
[L526] [24:26.56] to do a distributed commit and it still
[L527] [24:30.24] is. And so the idea was well you you do
[L528] [24:35.12] the e you do the west coast update you
[L529] [24:37.68] decrease the widgets by one you just
[L530] [24:39.52] send a message asynchronously and not in
[L531] [24:42.64] a transaction so that eventually the
[L532] [24:45.84] east coast uh warehouse gets decremented
[L533] [24:49.44] by one.
[L534] [24:51.36] So meanwhile,
[L535] [24:53.44] if you're on the east coast, you you
[L536] [24:55.92] decrement, you know, food stuffs by one.
[L537] [24:59.52] You send an asynchronous message.
[L538] [25:01.84] Eventually, the West Coast gets it and
[L539] [25:04.48] eventually everything settles out. So if
[L540] [25:10.16] you're allowed to to go below zero
[L541] [25:14.72] then what will happen is if the east
[L542] [25:16.72] coast guy and the west coast guy
[L543] [25:18.24] simultaneously
[L544] [25:20.24] sell the last widget
[L545] [25:22.64] then then eventually
[L546] [25:25.28] uh the
[L547] [25:27.44] state of the warehouse will be minus one
[L548] [25:32.16] and somebody won't get their widget
[L549] [25:34.32] their widget
[L550] [25:36.80] and So, uh, if if you're allowed like
[L551] [25:41.36] Amazon to say usually ships in 24 hours,
[L552] [25:45.12] then maybe you're can allowed to
[L553] [25:47.68] oversell, but most enterprises can't do
[L554] [25:51.60] that. And so eventual consistency just
[L555] [25:54.88] doesn't work. So, we talked a million
[L556] [25:58.64] hours ago about referential integrity.
[L557] [26:01.92] So referential integrity in a sales
[L558] [26:04.32] system is uh integrity constraint is
[L559] [26:08.40] stock is greater than minus one and that
[L560] [26:12.08] fails
[L561] [26:13.60] with eventual consistency.
[L562] [26:16.32] And so uh Jeff Dean finally of Google
[L563] [26:19.92] finally figured that out
[L564] [26:22.40] and uh when they did Spanner, Spanner
[L565] [26:26.16] had a conventional transactional system
[L566] [26:29.04] and so Google comp uh completely
[L567] [26:31.84] abandoned eventual consistency
[L568] [26:34.72] and completely abandoned map reduce.
[L569] [26:37.84] >> So the trade-offs basically um
[L570] [26:40.64] correctness for performance. So, it's
[L571] [26:43.04] performance versus data integrity. And
[L572] [26:46.00] if you don't care about your data,
[L573] [26:48.80] then you're willing to deal with with
[L574] [26:52.00] bad things happening.
[L575] [26:54.24] So, did you ever talk to the Google team
[L576] [26:56.64] while they were doing those things that
[L577] [26:58.48] you thought were so wrong? We talked to
[L578] [27:01.28] them before the
[L579] [27:05.20] 2011 paper
[L580] [27:08.64] and said, "Why why don't we why don't we
[L581] [27:12.32] partner up and do some stuff?" And they
[L582] [27:15.84] weren't they weren't interested.
[L583] [27:18.24] So, they declined. Have you seen other
[L584] [27:20.72] examples in other big tech companies
[L585] [27:22.64] where their databases or database
[L586] [27:25.20] solutions where you actively disagree
[L587] [27:27.76] with them? like maybe Amazon or or
[L588] [27:30.64] Facebook. Well, I gave a talk at Amazon
[L589] [27:34.08] maybe three years ago
[L590] [27:37.04] and I told them all the things I thought
[L591] [27:38.96] they were doing wrong and I think uh
[L592] [27:44.16] Amazon's problem is that they are
[L593] [27:47.36] supporting you know
[L594] [27:50.72] 15 different database systems
[L595] [27:53.76] and that's about 12 too many. So, so I
[L596] [27:58.16] think they have their own culture and I
[L597] [28:01.04] told I I said you're supporting too many
[L598] [28:03.36] database systems
[L599] [28:05.52] and at this point they haven't chosen to
[L600] [28:07.76] retire any of them.
[L601] [28:09.76] >> Why do you say that the 15 should be
[L602] [28:12.08] three? Well, they're supporting a
[L603] [28:14.56] graph-based database system, and it's
[L604] [28:17.44] well understood that a graph-based
[L605] [28:21.12] database system is almost never the
[L606] [28:25.12] performant option.
[L607] [28:27.92] And so, if you want a graph, if you
[L608] [28:31.20] want, if you like the idea of having a
[L609] [28:34.96] user interface that deals with nodes and
[L610] [28:38.72] edges, that's fine. put put a layer on
[L611] [28:41.52] top of a relational database system that
[L612] [28:44.56] gives you that user model. And so most
[L613] [28:48.88] of their database systems, there's some
[L614] [28:51.52] other of their database systems that
[L615] [28:53.44] better at what it does than
[L616] [28:56.72] than it is.
[L617] [28:59.04] And so so the answer is you should
[L618] [29:01.12] retire
[L619] [29:04.32] you should retire any database system
[L620] [29:06.56] that isn't performant
[L621] [29:10.24] in in a big enough market to justify the
[L622] [29:13.36] maintenance. you've uh influenced
[L623] [29:16.32] industry significantly from academia
[L624] [29:19.92] and my one thought that I had is what
[L625] [29:24.24] why not work directly in industry or why
[L626] [29:28.08] why do you prefer the position of being
[L627] [29:30.56] in academia and having influence in the
[L628] [29:32.88] way that you have versus just uh taking
[L629] [29:36.16] a job at AWS or something like that
[L630] [29:38.72] being a very you know distinguished
[L631] [29:40.64] engineer there
[L632] [29:43.20] uh because that gives you to a boss.
[L633] [29:45.55] [laughter]
[L634] [29:46.64] And that gives you company rules, limits
[L635] [29:49.44] your ability to publish, limits your
[L636] [29:52.16] ability to go talk at conferences,
[L637] [29:55.12] uh limits your abil your ability to
[L638] [30:01.20] go go poke at what what various
[L639] [30:04.64] competitors are doing that they won't
[L640] [30:07.68] tell their competitors.
[L641] [30:10.40] But mostly I really like being in
[L642] [30:12.72] startups and I and I after the
[L643] [30:15.28] commercial version of Postgress got
[L644] [30:17.28] acquired by InformX.
[L645] [30:19.60] You know I was working part-time for
[L646] [30:22.64] InformX
[L647] [30:24.40] which was a 2,000 person company and I
[L648] [30:27.28] didn't feel like I could make a
[L649] [30:28.80] difference because it was bureaucratic
[L650] [30:32.16] and and whatever the president wanted he
[L651] [30:35.76] got.
[L652] [30:38.40] So, I think I'm just not cut out for I'm
[L653] [30:41.92] not cut out for politicking. I don't do
[L654] [30:44.16] that very well
[L655] [30:46.32] and I have a hard time interacting with
[L656] [30:48.80] people I think are dumb and that again.
[L657] [30:51.68] So, I guess I I I have I have some
[L658] [30:54.64] problems with with big companies.
[L659] [30:58.00] >> I I want to talk a little bit about
[L660] [31:00.24] Debboss. I just thought it was a really
[L661] [31:02.80] interesting technical model. Can you
[L662] [31:05.36] explain what the boss is? We started the
[L663] [31:09.12] academic project in
[L664] [31:12.48] 20
[L665] [31:14.96] 19 2020 something like that. And the
[L666] [31:18.40] gist of it was
[L667] [31:20.88] uh at that point Mate Mate Haria who is
[L668] [31:24.88] on the faculty at Stanford was also one
[L669] [31:27.52] of the founders of data bricks was the
[L670] [31:30.16] original creator of Spark.
[L671] [31:33.68] And so he said uh
[L672] [31:38.08] at the time data bricks you know
[L673] [31:40.48] basically was running people's spark
[L674] [31:43.60] jobs on the cloud. And so he said at any
[L675] [31:48.16] given time we might be orchestrating a
[L676] [31:52.08] million Spark jobs.
[L677] [31:54.40] And so we have to write a scheduler
[L678] [31:57.04] that's going to decide who to run next
[L679] [32:00.88] at scale a million.
[L680] [32:03.28] And he said there was no we tried all
[L681] [32:06.40] the all the schedulers written by the OS
[L682] [32:09.28] folks and they they couldn't they didn't
[L683] [32:12.32] scale.
[L684] [32:14.64] So we put all the scheduling data in a
[L685] [32:16.64] Postgress database and basically a
[L686] [32:20.24] Postgress application was doing
[L687] [32:22.16] scheduling and then it sort of clicked
[L688] [32:24.88] that by and large most everything you do
[L689] [32:28.56] in an operating system
[L690] [32:30.96] is managing data at scale
[L691] [32:34.00] and you should do that using database
[L692] [32:36.40] technology.
[L693] [32:38.32] So why don't we just replace at least
[L694] [32:41.28] the upper half of Linux with a database
[L695] [32:44.24] system.
[L696] [32:46.88] So that was the gist of the academic
[L697] [32:49.36] project and we worked on it at Berkeley
[L698] [32:52.64] and Stanford
[L699] [32:54.48] uh in the early early 20s and it was it
[L700] [32:59.12] was very successful. It clearly it
[L701] [33:02.16] clearly worked.
[L702] [33:04.24] And in the process
[L703] [33:07.20] uh the Stanford folks wrote an extension
[L704] [33:12.56] to uh JavaScript so that you could
[L705] [33:15.84] program you need some programming world
[L706] [33:18.32] that can can talk to your
[L707] [33:21.44] implementation.
[L708] [33:23.68] So if you're doing what amounts to a
[L709] [33:27.52] programming language and you're running
[L710] [33:30.08] on top of what amounts to an operating
[L711] [33:32.96] system that is a database,
[L712] [33:35.76] then the obvious thing to do is put all
[L713] [33:37.92] your state in the database. And that's
[L714] [33:40.00] exactly what they did. And so we had an
[L715] [33:42.40] innovative
[L716] [33:44.08] programming language model, an
[L717] [33:46.64] innovative operating system model
[L718] [33:50.40] and and of course then the idea was well
[L719] [33:53.84] can we start a company
[L720] [33:56.24] and so we talked to the VCs
[L721] [34:00.88] who to a person said
[L722] [34:04.88] you're you're dreaming if you think
[L723] [34:06.80] you're going to displace Linux. However,
[L724] [34:10.08] this programming language stuff is
[L725] [34:11.76] really nifty. We had what amounted to
[L726] [34:15.76] extensions to JavaScript
[L727] [34:19.84] that would allow
[L728] [34:21.92] any any program to have all of the nice
[L729] [34:24.88] features of a database system. You know,
[L730] [34:27.76] stuff was durable. You could have
[L731] [34:29.84] transactions.
[L732] [34:31.52] If it failed, you'd fail over. You know,
[L733] [34:34.32] it was all that nifty stuff.
[L734] [34:37.36] So we got funded
[L735] [34:39.60] uh to start a company in 2023
[L736] [34:44.80] and that was Debboss Incorporated and we
[L737] [34:49.12] decided that that was the name of the
[L738] [34:51.04] project since it always been the name of
[L739] [34:53.44] the project
[L740] [34:55.20] but we were ba we were basically in the
[L741] [34:57.84] programming language business and so at
[L742] [35:00.72] the current time uh deboss has a version
[L743] [35:05.20] of Typescript a version of Java, version
[L744] [35:07.76] of Joe, Go,
[L745] [35:10.56] and a version of Python, which which are
[L746] [35:15.60] basically seamless. It runs what looks
[L747] [35:18.40] like vanilla programs. In the world of
[L748] [35:23.44] the cloud, there's every incentive for
[L749] [35:26.80] you to structure your your your
[L750] [35:28.88] application as a workflow.
[L751] [35:31.36] And so we decided that we would support
[L752] [35:34.96] a workflow system period.
[L753] [35:38.48] And so the workflow that that deboss
[L754] [35:43.04] supports in [snorts] those four
[L755] [35:45.12] languages is the steps in in a workflow,
[L756] [35:50.32] the individual
[L757] [35:52.40] micro apps, whatever you want to call
[L758] [35:54.32] them, are transactional.
[L759] [35:57.36] Uh workflows are durable. So that once
[L760] [36:00.80] you do a step it's not forgotten.
[L761] [36:04.48] Uh and it's clear that we can make
[L762] [36:10.00] uh workflows atomic if there was a
[L763] [36:13.44] market for it which means the whole
[L764] [36:16.08] workflow would either finish or look
[L765] [36:19.60] like it never happened. So it has very
[L766] [36:22.32] very nice properties
[L767] [36:24.64] and is
[L768] [36:27.52] a great deal faster and a great deal
[L769] [36:29.36] easier to use than the competition.
[L770] [36:32.48] So
[L771] [36:34.00] the company is selling and innovating in
[L772] [36:37.28] this area.
[L773] [36:39.60] And so so the idea is that you want to
[L774] [36:43.04] make state of your application
[L775] [36:45.52] persistent when you put it in the
[L776] [36:47.84] database. uh and then it and then you
[L777] [36:50.96] figure out how to do it fast.
[L778] [36:53.68] And I [snorts] think their their
[L779] [36:56.80] business model as we were talking
[L780] [36:59.44] earlier is very much get and get leaf
[L781] [37:04.16] level programmers
[L782] [37:06.32] interested.
[L783] [37:07.92] So it's been very much uh you know tell
[L784] [37:11.84] us leaf level programmer tell us what
[L785] [37:14.56] you need that we don't have get it
[L786] [37:17.44] quickly
[L787] [37:19.28] and convince people to try it and
