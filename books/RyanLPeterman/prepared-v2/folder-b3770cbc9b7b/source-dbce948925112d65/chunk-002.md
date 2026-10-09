Chunk 2; segments 368–755. Start may repeat the previous chunk for context.

# Dropbox’s Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling

Source ID: source-dbce948925112d65
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Dropbox’s_Former_Most_Senior_Eng_Building_Great_Systems_and_Advice_for_the_AI_Era_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=3XkmNSuHFmY

[L377] [12:46.16] Our goal was just to solve problems. And
[L378] [12:48.04] I think that's the difference. I mean,
[L379] [12:49.64] in academia, your goal is to advance
[L380] [12:51.96] knowledge. Um in in industry, your goal
[L381] [12:54.96] is to solve problems.
[L382] [12:56.72] Um and
[L383] [12:58.40] I gravitate more towards the solving
[L384] [13:00.68] problems.
[L385] [13:01.68] And I find that a more comfort-
[L386] [13:03.08] comfortable environment within which to
[L387] [13:04.60] work.
[L388] [13:05.72] >> Going to your time in in industry, you
[L389] [13:08.88] know, at Dropbox, you became the most
[L390] [13:10.60] senior engineer at the company. And
[L391] [13:13.04] looking through all the projects that
[L392] [13:14.68] you did, I had a series of just
[L393] [13:18.32] technical curiosities. I saw this idea
[L394] [13:20.76] early in your career about multi-homing,
[L395] [13:22.56] and I wasn't familiar with that concept.
[L396] [13:24.76] What What is multi-homing? What's the
[L397] [13:26.80] problem it
[L398] [13:28.08] >> Yeah, I mean multi-homing is the ability
[L399] [13:30.36] to have data in two locations, two
[L400] [13:32.44] homes. And multi-homing can be valuable
[L401] [13:35.76] for a variety of reasons. Um one is
[L402] [13:39.00] called, you know, primary secondary or,
[L403] [13:41.28] you know,
[L404] [13:42.12] lazily replicated multi-homing whereby
[L405] [13:44.80] all rights commit authoritatively in one
[L406] [13:47.56] region and get replicated to a secondary
[L407] [13:49.96] region. Um and so this is normally used
[L408] [13:53.04] for, you know, business continuity. You
[L409] [13:55.12] know, one thing we did at Dropbox we
[L410] [13:56.64] made sure that if the entire West Coast
[L411] [14:00.04] blew up, you know, which hopefully
[L412] [14:01.52] wouldn't happen, Dropbox would keep
[L413] [14:03.12] running because there would be enough
[L414] [14:04.76] the data would be replicated in other
[L415] [14:05.96] regions. But with a window of
[L416] [14:07.76] vulnerability, with a window of time
[L417] [14:09.32] where there may be some some some data
[L418] [14:11.60] lost.
[L419] [14:12.84] Um so that is, you know, that's kind of
[L420] [14:15.12] primary secondary replication or
[L421] [14:17.00] multi-homing. There's something else
[L422] [14:18.64] called active active multi-homing where
[L423] [14:21.16] there is truly an authoritative copy of
[L424] [14:23.52] the data in multiple locations. So
[L425] [14:25.76] basically when you, for example, write
[L426] [14:27.88] to a system, you don't externalize that
[L427] [14:30.44] right as having succeeded until it has
[L428] [14:32.64] landed in all the regions.
[L429] [14:34.72] Um and so, for example, in the the
[L430] [14:36.68] storage system at Dropbox, the block
[L431] [14:38.16] storage system, we truly had a a
[L432] [14:40.28] multi-region replicated system where we
[L433] [14:42.72] could take down an entire region, say
[L434] [14:44.44] take down the
[L435] [14:45.76] a region in Ashburn, Virginia where
[L436] [14:48.68] everyone's data centers are and there'd
[L437] [14:50.80] be zero downtime for the company and the
[L438] [14:52.56] data was still safe in multiple regions.
[L439] [14:55.12] I think multi-homing
[L440] [14:57.84] is something a lot of engineers aspire
[L441] [14:59.68] to work on cuz it's it seems like
[L442] [15:03.84] the right thing to do.
[L443] [15:05.56] But I think the reality is for most
[L444] [15:07.20] companies it is not.
[L445] [15:09.32] For most companies it's not because
[L446] [15:10.40] there's very high cost there's very high
[L447] [15:12.32] cost latency costs for this. Very high
[L448] [15:14.48] um because the speed of light is just
[L449] [15:16.52] not getting faster. The speed of light
[L450] [15:18.04] is fixed.
[L451] [15:19.24] And if you have to, you know,
[L452] [15:21.12] synchronously write data across multiple
[L453] [15:23.20] regions in the United States, you're
[L454] [15:25.04] going to have, say, 60 milliseconds in
[L455] [15:27.76] the commit path of your protocol, which
[L456] [15:29.72] for most applications is not tenable.
[L457] [15:31.88] Uh, so there is a lot of desire, um, you
[L458] [15:34.44] know,
[L459] [15:35.20] a lot of engineering teams reach out for
[L460] [15:36.80] kind of advice on how to adopt
[L461] [15:38.56] active-active multi-homing for the
[L462] [15:39.96] company. I would normally say, "Don't do
[L463] [15:42.48] it." I would normally say,
[L464] [15:44.76] "Frankly, if US East is down, if Amazon
[L465] [15:47.12] is down that day,
[L466] [15:49.00] that's okay. If Amazon's down that day,
[L467] [15:51.92] your your company will be down. That's a
[L468] [15:54.12] shame, right? But by avoiding that
[L469] [15:57.08] complexity, you're going to be able to
[L470] [15:58.84] move much faster and build a much better
[L471] [16:00.24] product. And so,
[L472] [16:02.04] in my mind, systems is all about
[L473] [16:03.44] trade-offs and making the right ones.
[L474] [16:05.72] I would generally recommend most people
[L475] [16:08.68] do not make the trade-off to have
[L476] [16:10.72] partition tolerance or or or
[L477] [16:12.60] multi-region availability.
[L478] [16:14.48] Even though for a company like Dropbox,
[L479] [16:15.72] yes, that does make sense. When you When
[L480] [16:17.32] you When your When your job is storing
[L481] [16:19.44] data and you have several exabytes of it
[L482] [16:22.00] and and hundreds of millions of
[L483] [16:23.40] customers, I think that's when it's when
[L484] [16:25.20] it starts to make sense.
[L485] [16:26.64] >> So, it's it's just another term for, I
[L486] [16:28.96] guess, data replication and having it
[L487] [16:31.48] available on other regions. Okay. I
[L488] [16:33.88] imagine also, I mean, the cost of
[L489] [16:35.60] storage is a concern. How many replicas
[L490] [16:38.28] would you keep for something? Like,
[L491] [16:40.08] let's just say I stored something in
[L492] [16:41.36] Dropbox. It's my document. Is that
[L493] [16:45.08] on on the order of one or two or is
[L494] [16:47.20] there multiple?
[L495] [16:47.96] >> No, it's on the order of many, many. And
[L496] [16:50.04] so, um,
[L497] [16:51.56] so, if you were to store a file in
[L498] [16:53.84] Dropbox,
[L499] [16:55.92] I modeled the storage to be, as we
[L500] [16:58.08] advertise, at least 12 nines of
[L501] [16:59.68] durability. Internally, the models look
[L502] [17:02.24] around 24 nines of durability. And so,
[L503] [17:04.84] that means the data is secure with
[L504] [17:07.24] 99.99999%
[L505] [17:10.12] where there's 24 nines, right? Which
[L506] [17:12.08] means, at least according to the model,
[L507] [17:15.24] you know, the universe will be extinct
[L508] [17:17.36] before any data is lost. Right. And and
[L509] [17:20.16] the way that is done is by a combination
[L510] [17:22.16] of of what's called erasure coding. So,
[L511] [17:24.52] erasure coding is how you take a
[L512] [17:26.28] several blocks of data and combine them
[L513] [17:27.92] together in it with an encoding scheme
[L514] [17:30.36] and spread them around in in different
[L515] [17:32.12] locations. At that scale, at Dropbox
[L516] [17:34.28] scale, you're you're taking things into
[L517] [17:35.48] consideration like putting data in
[L518] [17:36.80] different racks, different rows of a
[L519] [17:39.60] data center because they're on different
[L520] [17:40.64] power feeds. You're taking into
[L521] [17:42.28] consideration different eras of hard
[L522] [17:45.00] drives and different manufacturers of
[L523] [17:46.64] drives because they can have correlated
[L524] [17:48.04] failure patterns. And then replication
[L525] [17:50.12] across regions.
[L526] [17:51.84] Um so, you know, you you could be
[L527] [17:53.56] looking at
[L528] [17:54.76] 27 fragments, for example. That doesn't
[L529] [17:57.72] mean you're storing 27 times the data.
[L530] [17:59.72] It's it's kind of encoded in in in many
[L531] [18:01.64] regions. But, it's really uh the
[L532] [18:03.60] replication schemes get really quite
[L533] [18:05.24] sophisticated at that point. And we
[L534] [18:06.92] actually had our own
[L535] [18:08.72] custom encoding matrix we had developed.
[L536] [18:10.92] It's called a Vandermonde matrix where
[L537] [18:13.48] you kind of take a bunch of data and you
[L538] [18:15.28] combine it together to produce outputs.
[L539] [18:18.76] And we would plug in some variables like
[L540] [18:21.00] how much do discs cost? How much does
[L541] [18:23.32] network bandwidth cost?
[L542] [18:25.32] Because there's a trade-off. You can
[L543] [18:26.64] either store If you don't want to lose
[L544] [18:27.96] your data, you can store more copies on
[L545] [18:29.84] more discs.
[L546] [18:31.40] Or you can store fewer copies. And
[L547] [18:33.72] anytime a disc fails, you re-replicate
[L548] [18:36.48] it really fast. And re-replicating
[L549] [18:38.52] really fast costs
[L550] [18:40.12] disk band costs network bandwidth.
[L551] [18:42.24] So, these kind of variables go into this
[L552] [18:43.76] equation. Uh it ends up being an
[L553] [18:45.84] extremely complex field of endeavor, but
[L554] [18:48.48] it's kind of abstracted away into a part
[L555] [18:50.36] of the system that doesn't doesn't leak
[L556] [18:51.84] into anywhere else.
[L557] [18:53.28] >> So, with erasure encoding, my my
[L558] [18:55.92] document in Dropbox is fragmented into a
[L559] [18:59.24] bunch of different chunks of data and
[L560] [19:01.12] loaded potentially from many different
[L561] [19:02.64] machines.
[L562] [19:03.48] >> Yes, absolutely.
[L563] [19:04.80] >> It
[L564] [19:05.96] I mean, the the first thought I have is
[L565] [19:08.20] now there's uh I might be waiting there
[L566] [19:10.48] and one of the 27 machines is slow and I
[L567] [19:14.64] can't look at the whole doc. So, how do
[L568] [19:16.44] you prevent against that?
[L569] [19:17.56] >> It's actually faster than not
[L570] [19:19.84] replicated. Because if you imagine I'll
[L571] [19:22.28] I'll pick a
[L572] [19:23.60] uh
[L573] [19:24.36] a simplified example.
[L574] [19:26.04] Imagine this is not the encoding scheme
[L575] [19:28.20] Dropbox uses, but imagine to reconstruct
[L576] [19:30.36] a file, you have to read six out of nine
[L577] [19:33.36] fragments.
[L578] [19:35.08] Right? So, if you read six out of nine
[L579] [19:37.32] fragments, you can just ask all nine
[L580] [19:40.60] and reconstruct and return the data as
[L581] [19:42.28] soon as you've heard from the first six.
[L582] [19:44.64] It's actually
[L583] [19:45.92] faster and you can construct these
[L584] [19:47.68] encoding matrices. So, if it is it's
[L585] [19:49.68] actually faster to have a ratio coded
[L586] [19:51.36] data than than not.
[L587] [19:53.28] >> I see. Okay, so you can
[L588] [19:55.24] like oversubscribe, over request, and
[L589] [19:58.20] then you complete on a portion of them
[L590] [20:01.36] being received.
[L591] [20:02.04] >> Yes. Now,
[L592] [20:03.24] in in practice, it was a bit more
[L593] [20:05.16] complex than that. We'd often have a
[L594] [20:06.52] copy in a single disk to provide fast
[L595] [20:08.64] access. We'd often try to make sure that
[L596] [20:11.04] you could serve your data out of a
[L597] [20:12.64] region close to your home region. So,
[L598] [20:14.88] we'd make sure that your data was mostly
[L599] [20:16.64] served with low latency. But, if that
[L600] [20:19.00] region had failed, you could reconstruct
[L601] [20:20.76] it from the remaining regions. So,
[L602] [20:22.28] there's a lot of um
[L603] [20:24.24] a lot of people, you know, there's a lot
[L604] [20:25.24] of uh talk about building your own
[L605] [20:27.68] infrastructure and and you can save
[L606] [20:29.68] money by moving off the cloud.
[L607] [20:32.08] Um
[L608] [20:32.80] almost definitely you can't. Unless you
[L609] [20:36.24] you unless you either you have very
[L610] [20:37.96] small requirements or very fixed
[L611] [20:40.32] requirements or very very very heavy
[L612] [20:42.96] investment. Cuz if you want to compete
[L613] [20:44.72] with Amazon, if you want to build a more
[L614] [20:46.08] efficient storage system than Amazon,
[L615] [20:48.44] you have to have a supply chain team
[L616] [20:50.12] that's working with you know, Western
[L617] [20:51.96] Digital and Seagate constantly and
[L618] [20:53.96] negotiating on prices of disks and
[L619] [20:55.72] buying shipments at certain time and and
[L620] [20:57.92] capacity teams and and data center
[L621] [21:00.52] teams. Like there's a lot of work that
[L622] [21:02.44] goes into like
[L623] [21:03.88] optimizing this. Because ultimately, our
[L624] [21:06.08] desire was to use the disks to 90-95%
[L625] [21:10.36] of
[L626] [21:11.32] the disk size to to maximize storage
[L627] [21:14.16] efficiency. To put it this way, I mean
[L628] [21:15.92] that was
[L629] [21:16.88] you know, I guess it's a ballpark
[L630] [21:18.20] figure, a billion-dollar project.
[L631] [21:20.32] Right? And was you know, and it I think
[L632] [21:22.76] at the time, as far as I know, was the
[L633] [21:24.44] largest ever data migration in history,
[L634] [21:27.36] I think at the time. And so, extremely
[L635] [21:29.92] large engineering project with very high
[L636] [21:32.92] technical investment. So, yes, if you
[L637] [21:34.84] have that scale and you have the
[L638] [21:36.80] engineering team to do it and you're
[L639] [21:39.88] willing to keep innovating, if you're
[L640] [21:42.12] willing to keep
[L641] [21:43.76] um optimizing and investing effort in
[L642] [21:45.60] it, then yes, you can do it.
[L643] [21:47.64] Um but I think the real I mean, the
[L644] [21:49.40] cloud has been an incredible innovation,
[L645] [21:51.12] right? Most people are not experts at
[L646] [21:52.64] this, and most people should not be
[L647] [21:54.20] experts at this. You know, most people
[L648] [21:55.68] should focus on their applications.
[L649] [21:57.64] >> When you say that most people shouldn't,
[L650] [21:59.76] my immediate thought was but one of the
[L651] [22:02.12] big projects you worked on at Dropbox
[L652] [22:04.40] was my migrating away from S3.
[L653] [22:06.96] >> Yes, yes.
[L654] [22:07.52] >> So,
[L655] [22:08.28] um you know, why why did Dropbox migrate
[L656] [22:10.32] away from S3?
[L657] [22:12.36] >> Yeah, that was a desire of the company
[L658] [22:13.68] for a long time. You know, from even
[L659] [22:15.44] before I was there. So, I started at
[L660] [22:16.88] Dropbox in 20
[L661] [22:18.40] uh 2012. Um and I spoke to to Drew, the
[L662] [22:21.96] Dropbox founder, I think in 2010 about
[L663] [22:24.16] this project. And so, I think there was
[L664] [22:25.92] a desire to
[L665] [22:27.76] um control the destiny of the company
[L666] [22:30.68] from a strategic perspective. I mean, at
[L667] [22:32.12] the time it was before Dropbox kind of
[L668] [22:34.56] reshaped itself as being more about
[L669] [22:36.04] collaboration. You know, at the time it
[L670] [22:37.76] was a file sync and share category. That
[L671] [22:39.64] was that was the that was the that was
[L672] [22:41.24] the market sector, you know? And so, and
[L673] [22:43.80] owning the file system was really
[L674] [22:45.32] valuable to the company.
[L675] [22:47.08] Ultimately, we saved a huge amount of
[L676] [22:48.68] money. I mean, we we And this is before
[L677] [22:51.56] the public company went public. We
[L678] [22:53.28] really drove massive cost efficiencies
[L679] [22:56.20] through the project. Um but it was hard,
[L680] [22:58.48] you know, in a way that I think it'd be
[L681] [22:59.84] very difficult to to emulate without a
[L682] [23:02.00] huge investment.
[L683] [23:03.68] And I do think that there is um
[L684] [23:06.88] there is a benefit to an organization
[L685] [23:09.20] from having hard problems to solve.
[L686] [23:12.32] Because if you have a a company with
[L687] [23:14.04] extremely hard technical challenges, you
[L688] [23:16.48] can attract engineers who like working
[L689] [23:19.00] on those hard technical problems. And
[L690] [23:20.48] when they've solved those problems, they
[L691] [23:23.12] cycle off and work on different parts of
[L692] [23:25.00] the system. So, you know, after we all
[L693] [23:27.04] worked we had a such a great team. It
[L694] [23:28.88] was a very very small engineering team.
[L695] [23:30.72] And after we kind of shipped the the
[L696] [23:33.56] storage system reliably, we all went off
[L697] [23:35.36] and you know, Jamie went and and
[L698] [23:38.04] redesigned the sync protocol, the
[L699] [23:39.72] desktop client, and I worked on the on
[L700] [23:41.88] the file system and the distributed
[L701] [23:43.36] databases. And so, yeah, there's there's
[L702] [23:45.28] value to a business to have
[L703] [23:47.08] um that level of technical investment,
[L704] [23:49.20] but it is uh
[L705] [23:51.04] you know, it's like it's like having a
[L706] [23:52.36] baby and then you have to you've got to
[L707] [23:54.92] raise the baby. You can't just build a
[L708] [23:56.48] system like this and be that's it, we're
[L709] [23:58.16] done.
[L710] [23:59.56] You own it and you have to keep
[L711] [24:01.04] investing in it.
[L712] [24:03.32] >> Did um
[L713] [24:04.72] did S3 do any counter negotiation before
[L714] [24:07.64] you set out to leave them? Did they say
[L715] [24:09.16] like, "Oh, you know, we'll cut you a
[L716] [24:10.36] deal if you
[L717] [24:11.50] >> [laughter]
[L718] [24:12.72] >> I guess I'm allowed to talk about this
[L719] [24:14.00] now. It was a long time ago. Um
[L720] [24:17.04] Yeah, for the longest time they I don't
[L721] [24:18.28] think they were they were particularly
[L722] [24:19.48] aware that this was happening.
[L723] [24:21.40] Um but you know, the the data center
[L724] [24:23.20] folks talk. And uh certainly it was
[L725] [24:26.92] noticed that Dropbox is buying up a lot
[L726] [24:28.68] of data center space. So, yeah, we had
[L727] [24:31.24] we had um obviously at uh at the scales
[L728] [24:34.44] that we were at, I mean, we were
[L729] [24:35.80] negotiating very good rates with Amazon.
[L730] [24:38.52] You know, we weren't paying sticker
[L731] [24:39.60] price, we were paying very very very
[L732] [24:41.36] good discounted rates. Um but yeah, at a
[L733] [24:43.96] certain point they weren't able to meet
[L734] [24:45.36] our cost efficiency. Because it it's it
[L735] [24:47.12] when we launched the system, it really
[L736] [24:48.72] was
[L737] [24:49.96] more efficient than S3.
[L738] [24:51.92] And that's for a variety of reasons. One
[L739] [24:53.68] was that we were using kind of new
[L740] [24:55.32] experimental disks called shingled
[L741] [24:57.24] magnetic recording. We were the first
[L742] [24:59.12] ones, I think, to use these disks at
[L743] [25:00.60] scale.
[L744] [25:01.64] Um and two, we had a very tight
[L745] [25:03.68] understanding of our workloads. So, we
[L746] [25:04.96] were able to design the system
[L747] [25:06.44] specifically optimized for our
[L748] [25:08.20] workloads, whereas S3 has to design the
[L749] [25:10.60] system for everybody. So, you know, it
[L750] [25:13.12] got to the point where, you know, Amazon
[L751] [25:14.76] would not have been able to offer us a
[L752] [25:16.04] more competitive deal because we had a
[L753] [25:18.20] more efficient system.
[L754] [25:20.20] Um
[L755] [25:21.72] I wouldn't recommend another company do
[L756] [25:23.16] this right now.
[L757] [25:24.72] Uh but I think at the time it it
[L758] [25:26.12] certainly made sense for us as a
[L759] [25:27.40] company.
[L760] [25:28.92] >> Can you give an example of uh tight
[L761] [25:31.68] understanding of your workloads leading
[L762] [25:33.52] to like something you could do that S3
[L763] [25:36.24] couldn't?
[L764] [25:36.84] >> Yeah, absolutely. So, for example, I
