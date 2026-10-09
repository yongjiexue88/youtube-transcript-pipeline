Chunk 2; segments 380–769. Start may repeat the previous chunk for context.

# AWS Distinguished Eng: Learning From 3000 Incidents And How Engineering Is Changing | Marc Brooker

Source ID: source-45044ebe79206044
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/AWS_Distinguished_Eng_Learning_From_3000_Incidents_And_How_Engineering_Is_Changing_Marc_Brooker_en.txt
Video: https://www.youtube.com/watch?v=u3GjIXP9N0s

[L389] [13:58.20] this particular line in the software
[L390] [14:00.00] that that caused something, you know,
[L391] [14:01.84] fix the testing processes that that
[L392] [14:03.80] didn't catch that, you know, fix the
[L393] [14:06.96] um you know, maybe social or or team
[L394] [14:09.52] processes that led to those technical
[L395] [14:11.56] processes. Um
[L396] [14:14.48] and you know, and then if you're seeing
[L397] [14:16.36] patterns across multiple postmortems,
[L398] [14:19.72] sort of level those up and say, well,
[L399] [14:21.48] clearly there's a hard underlying
[L400] [14:23.08] problem here. You know, can we build a
[L401] [14:25.92] service around that? Can we build a
[L402] [14:27.92] library around that? Can we build a
[L403] [14:31.56] you know, community of practice around
[L404] [14:33.24] that? You know, are there technical
[L405] [14:35.12] changes we can make uh to to avoid whole
[L406] [14:38.60] classes of things?
[L407] [14:40.44] Um
[L408] [14:42.00] So that's quite a long-winded answer,
[L409] [14:43.56] but I I I do think it is it all flows
[L410] [14:46.92] from
[L411] [14:48.12] understanding and understanding at
[L412] [14:50.12] multiple levels. Like understanding
[L413] [14:51.76] immediately like what happened, but also
[L414] [14:54.12] understanding you know, broadly what
[L415] [14:56.12] happened, you know, technologically and
[L416] [14:58.00] organizationally and and and in context.
[L417] [15:01.44] And then the ability to connect that
[L418] [15:03.20] particular event or or postmortem with
[L419] [15:07.60] other ones, you know, and and and and
[L420] [15:09.76] extract those patterns.
[L421] [15:11.48] You know, one of the things that we we
[L422] [15:13.28] did in D SQL was we spent a lot of time
[L423] [15:15.52] as we were designing that looking
[L424] [15:16.84] around, you know, relational database
[L425] [15:19.00] related postmortems and thinking about
[L426] [15:21.52] both our own and our customers and
[L427] [15:23.44] thinking about, you know, how can we
[L428] [15:24.56] design a database that helps people
[L429] [15:26.32] avoid falling into these traps?
[L430] [15:28.92] Um
[L431] [15:30.48] and, you know, a really common kind of
[L432] [15:33.48] outage pattern folks with relational
[L433] [15:35.72] databases is
[L434] [15:37.92] you have a client
[L435] [15:39.56] on a distributed system, starts a
[L436] [15:41.60] transaction, and then goes out to lunch
[L437] [15:44.40] for whatever reason. And, uh, you know,
[L438] [15:46.80] that could be a GC pause or could be a
[L439] [15:48.72] lossy network or it could be a loss of
[L440] [15:50.24] connectivity and now it's holding locks.
[L441] [15:52.60] Um and so, if you look at, you know,
[L442] [15:55.08] relational databases, they don't tend to
[L443] [15:56.84] be resilient to clients misbehaving in
[L444] [15:59.48] that way. And that's a really common
[L445] [16:01.36] cause of
[L446] [16:03.92] uh, operational issues for systems built
[L447] [16:05.88] on relational databases. And so, as we
[L448] [16:08.16] were designing D SQL, we were thinking,
[L449] [16:10.68] how do we avoid
[L450] [16:12.92] uh, broadly that class of problems? And
[L451] [16:16.08] so, folks can say, "Hey, I'm going to
[L452] [16:18.04] build on D SQL and just not have this
[L453] [16:20.00] whole class of problems."
[L454] [16:21.84] Uh, and, you know, I think that's a
[L455] [16:23.64] really kind of powerful
[L456] [16:25.72] outer loop over the postmortem process
[L457] [16:28.08] is to say, "How do we turn all of these
[L458] [16:30.84] lessons into new services and into
[L459] [16:33.08] service improvements?"
[L460] [16:35.56] How do you prevent misbehaving clients
[L461] [16:38.00] from being a problem for the database?
[L462] [16:41.16] Yeah, so in in D SQL's case, um
[L463] [16:44.28] we have uh, we have no pessimistic
[L464] [16:46.48] locking. And so, it the within the scope
[L465] [16:50.12] of a transaction, uh, everything that
[L466] [16:52.32] happens in that transaction, all of the
[L467] [16:54.68] reads happen using this mechanism called
[L468] [16:56.56] multi-version concurrency control, where
[L469] [16:59.72] every row in the database, we sort of
[L470] [17:01.44] store a history of versions. And so, you
[L471] [17:03.84] can read an old version of a row without
[L472] [17:06.12] blocking writers and saying, "Hey, you
[L473] [17:07.64] can't you can't update this cuz I just
[L474] [17:09.24] read it."
[L475] [17:10.24] Um and then, you know, locally within
[L476] [17:13.32] the query processor that's handling a
[L477] [17:15.36] connection, uh, we spool the rights
[L478] [17:17.80] locally and then you get to commit time
[L479] [17:19.56] and we do this optimistic check of uh,
[L480] [17:22.48] you know, can I commit this transaction
[L481] [17:24.20] at at at the transaction commit time.
[L482] [17:27.36] And so, combining those two mechanisms
[L483] [17:29.20] of having multi-version concurrency
[L484] [17:30.84] control and and the scale-out storage
[L485] [17:33.20] that comes with it
[L486] [17:35.08] and the commit time optimistic checks,
[L487] [17:39.84] we can strongly say that, you know,
[L488] [17:42.68] there is no way that a reader of a piece
[L489] [17:44.68] of data can block other writers and
[L490] [17:46.92] there's a no way that that a writer of
[L491] [17:49.00] data can block readers.
[L492] [17:51.44] Um, writers can block writers, but only
[L493] [17:55.00] um,
[L494] [17:56.04] only by changing data, not just by
[L495] [17:57.96] looking at it. And so, you can, you
[L496] [17:59.92] know, you can say, well, you know, I can
[L497] [18:01.96] cause, um, Sorry, writers can't block
[L498] [18:04.92] writers, but they can prevent other
[L499] [18:06.24] writers
[L500] [18:07.24] uh, transactions from eventually
[L501] [18:08.52] committing by making a bunch of changes.
[L502] [18:10.92] And that is
[L503] [18:12.36] inherent to the definition of the
[L504] [18:15.88] particular database isolation level. Out
[L505] [18:18.52] of curiosity, in practice, what percent
[L506] [18:21.64] overhead would you expect for keeping
[L507] [18:24.24] copies of old rows for the sake of those
[L508] [18:26.88] stale reads? Yeah, it's actually
[L509] [18:28.72] surprisingly small. And it's
[L510] [18:30.84] surprisingly small because if you look
[L511] [18:32.72] at the access patterns for most online
[L512] [18:34.64] databases, even ones that do a lot of
[L513] [18:36.92] write traffic, that write traffic tends
[L514] [18:39.36] to be quite concentrated. Uh, and, you
[L515] [18:42.60] know, it's quite unusual for an online
[L516] [18:44.60] database workload or even an analytics
[L517] [18:46.68] workload
[L518] [18:48.00] to
[L519] [18:49.16] make a second version of every row in
[L520] [18:51.76] the database. Typically, what it's doing
[L521] [18:53.56] is making a,
[L522] [18:55.28] you know, first, second, third,
[L523] [18:56.40] hundredth version of this row and a
[L524] [18:58.08] fiftieth version of that row, but the
[L525] [18:59.64] vast majority of data isn't changing.
[L526] [19:02.40] And so, it's super workload dependent,
[L527] [19:04.36] uh, as as is everything in in in the
[L528] [19:06.52] database world, uh, but the overhead
[L529] [19:09.12] tends to be relatively small.
[L530] [19:11.84] Uh,
[L531] [19:12.52] I would say it's unusual for
[L532] [19:16.80] a online database workload for that
[L533] [19:19.80] overhead on storage to be more than
[L534] [19:21.76] about 10%.
[L535] [19:23.56] From my experience, I've seen an
[L536] [19:25.40] interesting dichotomy between teams
[L537] [19:28.08] where some teams they really understand
[L538] [19:29.92] postmortem culture. They tend to be
[L539] [19:31.40] infrastructure teams. They tend to take
[L540] [19:33.64] it really seriously and everyone in on
[L541] [19:36.04] those teams, the tech leads are asking
[L542] [19:37.68] you, "Hey, why why did that happen?" And
[L543] [19:39.92] you know, really follow up and make sure
[L544] [19:41.88] it's it's not a problem. Then I've also
[L545] [19:44.00] noticed on other teams that is less of a
[L546] [19:46.76] strong muscle. For those teams that
[L547] [19:49.40] don't take it too seriously, what would
[L548] [19:51.40] be your your pitch for why they should
[L549] [19:53.72] take it seriously?
[L550] [19:55.44] Yeah, it all comes down to where you
[L551] [19:56.80] want to spend your time, right? Do you
[L552] [19:58.36] want to spend your time improving your
[L553] [20:00.28] product and and making it better or do
[L554] [20:02.08] you want to spend your time
[L555] [20:04.28] uh fighting the same fire over and over?
[L556] [20:07.04] And uh you know, really the
[L557] [20:10.56] culture of building
[L558] [20:13.00] um
[L559] [20:14.36] you know, building great postmortem
[L560] [20:16.36] cultures to make sure that at the the
[L561] [20:18.24] the
[L562] [20:19.44] pros- at the product level and at the
[L563] [20:21.52] organizational level,
[L564] [20:23.64] um
[L565] [20:24.92] you are
[L566] [20:26.96] fixing known issues
[L567] [20:29.52] and you are avoiding having the same
[L568] [20:31.92] problems multiple times.
[L569] [20:34.68] Um and typically when I see teams that
[L570] [20:38.80] have you know, a poor postmortem
[L571] [20:41.24] culture, I think they're
[L572] [20:43.64] probably one of two failure modes there.
[L573] [20:46.28] You know, one of them is a
[L574] [20:49.08] lack of focus on just the outcomes,
[L575] [20:52.04] right? Like, you know, a lack of of of
[L576] [20:54.12] really
[L577] [20:55.44] um
[L578] [20:56.60] I wouldn't say caring enough. I think
[L579] [20:58.52] that's a little bit too too personal,
[L580] [21:00.44] but being really focused on on, you
[L581] [21:03.04] know, is this
[L582] [21:04.24] is this product performing super well?
[L583] [21:06.28] Are we you know, are we really making
[L584] [21:08.44] our customers happy? And that is
[L585] [21:10.32] fundamentally a cultural and and and
[L586] [21:12.32] leadership cultural problem
[L587] [21:14.72] of of setting the right standards. Oh,
[L588] [21:17.00] and by the way, like I don't think, you
[L589] [21:18.52] know, standards should be
[L590] [21:20.56] uh you know, should be uniform, right?
[L591] [21:22.48] Like there are places where you know,
[L592] [21:25.56] the details really really matter where
[L593] [21:28.08] things like durability are just critical
[L594] [21:30.56] and and and you do need to have super
[L595] [21:32.48] high standards in those places.
[L596] [21:34.60] Um
[L597] [21:35.60] and you know, places where
[L598] [21:37.88] you want to optimize for other things
[L599] [21:39.40] and and and maybe have, you know, have
[L600] [21:41.32] have a a higher production defect rate.
[L601] [21:44.04] And I think that's that's okay.
[L602] [21:46.20] Um as long as that's an intentional
[L603] [21:48.76] decision that's being made. So, that's
[L604] [21:50.92] kind of case one, right? Like
[L605] [21:52.80] insufficient focus on the outcome.
[L606] [21:56.72] I think case two, and and this is a
[L607] [21:58.32] harder one to change,
[L608] [22:00.72] is normalization of kind of operational
[L609] [22:03.96] heroics. Like, we don't need to fix
[L610] [22:06.04] these root causes because our on-calls
[L611] [22:08.68] are super heroic and they're going to
[L612] [22:10.04] stay up all night and they're going to,
[L613] [22:12.24] you know, they're going to hack around
[L614] [22:13.40] things and they don't mind being paged
[L615] [22:14.92] 100 times a week. And
[L616] [22:18.60] they can feel from the inside like it's
[L617] [22:20.56] a good culture, right? Like, oh wow,
[L618] [22:22.56] these people are super strong owners.
[L619] [22:24.24] They're super engaged. They really care.
[L620] [22:26.24] They're really working hard on call.
[L621] [22:28.88] And those are all good signals. But then
[L622] [22:31.24] when you look at it from the outside,
[L623] [22:32.48] it's like, well, we're not actually
[L624] [22:33.72] fixing the causes of things. We're just
[L625] [22:35.64] doing this fantastically expensive
[L626] [22:38.68] investment of taking all of these people
[L627] [22:40.64] and their strong ownership and their
[L628] [22:42.44] expertise and spending them just on on
[L629] [22:44.48] on this break-fix cycle.
[L630] [22:46.84] And that's where you need to kind of
[L631] [22:47.84] look at it from the outside and say,
[L632] [22:49.92] well, let's take this energy of this
[L633] [22:51.80] team, fantastic energy, and focus it on
[L634] [22:56.20] uh on on improving the service, getting
[L635] [22:58.56] getting out of the cycle, finding, you
[L636] [23:01.00] know, finding new things to fix, finding
[L637] [23:03.08] new things to build.
[L638] [23:05.00] And that can be hard because it can be
[L639] [23:07.16] hard for, you know, those folks who've
[L640] [23:10.04] been in that mode to look at it and say,
[L641] [23:13.40] "This feels so good. It feels really
[L642] [23:15.72] like we're we're caring about our
[L643] [23:17.20] customers and caring about our product
[L644] [23:18.92] and caring about our business."
[L645] [23:20.92] Uh, to realize that oh, no, we're
[L646] [23:23.32] actually caring about it at the wrong
[L647] [23:24.72] level and we're not serving our business
[L648] [23:27.48] in the best possible way by being so
[L649] [23:30.40] narrowly and tactically focused on this
[L650] [23:32.68] break-fix cycle. And that's where you
[L651] [23:34.68] sort of need to pop them out and say,
[L652] [23:36.56] "Well,
[L653] [23:37.56] let's spend more time thinking about the
[L654] [23:40.84] postmortem. Let's spend more time
[L655] [23:42.80] thinking about the causes of things.
[L656] [23:45.24] Let's let's spend more time addressing
[L657] [23:47.88] these things in a more uh, strategic
[L658] [23:50.52] way." And wow, okay, now you've got so
[L659] [23:52.80] much more time to do that because you've
[L660] [23:54.44] broken the cycle and you can improve
[L661] [23:56.52] your product in different ways. I mean,
[L662] [23:58.92] since you have worked on AWS for almost
[L663] [24:03.08] two decades, uh,
[L664] [24:04.80] I'm sure you have a lot of experience
[L665] [24:06.28] building distributed systems and I think
[L666] [24:09.12] one of the most common advice that you
[L667] [24:10.84] hear, I guess this is maybe in the
[L668] [24:12.40] context of system design, is I I almost
[L669] [24:16.28] hear almost 100% of the time people will
[L670] [24:18.52] say, "Just throw a cache on it." Or you
[L671] [24:21.44] know, you'll have a system design and
[L672] [24:22.80] say, "How do you make it better? Let's
[L673] [24:24.20] put a cache here. Let's put a cache
[L674] [24:25.52] there." And I saw you had a tweet that
[L675] [24:28.04] said that there are cases where caches
[L676] [24:30.56] are are bad despite people saying it's
[L677] [24:32.76] best practice. I was curious if you
[L678] [24:34.48] could explain that. Yeah, so caching's
[L679] [24:36.84] good, right? Like it's hey, I'm I'm
[L680] [24:38.36] going to uh, take the these core ideas
[L681] [24:40.92] from computer science of of temporal and
[L682] [24:42.84] spatial locality and I am going to
[L683] [24:45.44] exploit those to make my system faster,
[L684] [24:48.84] scale better, et cetera. And so, you
[L685] [24:50.92] know, obviously very attractive. But,
[L686] [24:54.72] the downside of caches, especially in
[L687] [24:56.68] distributed systems, is they have this
[L688] [24:58.36] mode, right? Like they have this um you
[L689] [25:01.08] know the there's a mode where the cache
[L690] [25:02.68] is full, and the cache is full of the
[L691] [25:05.04] right data in time and space to perform
[L692] [25:07.52] very well.
[L693] [25:08.84] And there's a mode where the cache is
[L694] [25:10.16] empty or contains the wrong data.
[L695] [25:13.16] And
[L696] [25:14.52] in the first mode, the system is fast
[L697] [25:17.20] and happy and healthy.
[L698] [25:19.56] In the second mode, the system is slow,
[L699] [25:22.40] often down, because now the back end
[L700] [25:25.04] doesn't scale to deal with
[L701] [25:27.40] all of this under-cache traffic.
[L702] [25:29.56] Customers are very disappointed.
[L703] [25:31.88] Um
[L704] [25:33.32] and often it is down in a stable way.
[L705] [25:36.16] And this is this kind of idea of
[L706] [25:37.40] meta-stable failures, where the system
[L707] [25:39.72] has has um
[L708] [25:41.60] switched from state one to state two,
[L709] [25:44.12] and in state two it's still stable,
[L710] [25:45.76] right? Like it's still it's down, but
[L711] [25:48.16] it's not going to come back up under its
[L712] [25:49.72] own energy, because for example, all of
[L713] [25:52.88] this traffic is causing a huge amount of
[L714] [25:54.60] contention in my database, or it's
[L715] [25:57.00] saturating the network, and so I can't
[L716] [25:58.72] even refill the cache. It's not even
[L717] [26:00.80] getting the right kind of data in.
[L718] [26:03.48] And so, you know, when I talk about the
[L719] [26:05.04] downsides of caches, it's really about,
[L720] [26:07.28] you know, how do we avoid that modality
[L721] [26:11.28] between
[L722] [26:12.84] you know, fast and you know, uh the that
[L723] [26:16.60] that failure of caches, and the you
[L724] [26:19.96] know, how do we avoid the state where
[L725] [26:21.12] we're down?
[L726] [26:22.32] Um
[L727] [26:23.56] And so, if I go back to
[L728] [26:26.00] to DSQL, like our answer there is DSQL,
[L729] [26:29.32] what we call the storage tier, is
[L730] [26:30.72] essentially a cache, but it is a
[L731] [26:32.76] complete cache. It contains every row in
[L732] [26:35.64] the database.
[L733] [26:36.96] Um and so, it doesn't have this mode
[L734] [26:38.80] where how do I recover from it being
[L735] [26:41.04] empty or containing the wrong data? It
[L736] [26:43.36] contains all of the data.
[L737] [26:45.64] Um
[L738] [26:47.68] similarly, if you look at a a more,
[L739] [26:50.24] let's say, classical relational database
[L740] [26:52.12] design like Aurora,
[L741] [26:53.96] the Aurora leader is constantly telling
[L742] [26:56.20] the potential failover targets, "Here's
[L743] [26:57.96] something you should cache. Here's
[L744] [26:59.08] something you should cache. Here's
[L745] [27:00.12] something you should cache."
[L746] [27:01.64] So, when a failover happens, the cache
[L747] [27:03.96] is warm on, you know, on on the failover
[L748] [27:06.80] target. Um and so, those are the kinds
[L749] [27:09.68] of things that you can do to avoid those
[L750] [27:11.60] modalities.
[L751] [27:13.28] But, in general,
[L752] [27:14.92] um
[L753] [27:16.20] you know, and I I I wouldn't extract
[L754] [27:17.92] this as a rule or or or
[L755] [27:19.72] or or say that, you know, this applies
[L756] [27:21.64] 100% of the time,
[L757] [27:23.68] but in general, I prefer to see the
[L758] [27:26.44] teams around me avoiding caching where
[L759] [27:28.60] possible.
[L760] [27:29.88] I prefer patterns where you have a,
[L761] [27:33.36] let's say, complete materialized view of
[L762] [27:35.56] the data if you need very fast access to
[L763] [27:37.80] it, especially if it's slow moving. Just
[L764] [27:39.96] pull it down onto your local machine and
[L765] [27:41.48] work with it in memory.
[L766] [27:43.08] You know, if it's only being updated
[L767] [27:44.32] once a week, who cares? Like, just make
[L768] [27:46.08] lots of copies of it.
[L769] [27:47.72] Um
[L770] [27:49.32] Uh so, that's that's one pattern. Or,
[L771] [27:51.60] you know, use a scalable back end, you
[L772] [27:53.80] know,
[L773] [27:54.72] or Dynamo DB or whatever your favorite
[L774] [27:56.84] scalable database is,
[L775] [27:58.88] and keep your database vendor honest
[L776] [28:01.16] about getting to the the scale and
[L777] [28:03.04] performance you need, rather than
[L778] [28:04.44] putting a cache in front of things.
