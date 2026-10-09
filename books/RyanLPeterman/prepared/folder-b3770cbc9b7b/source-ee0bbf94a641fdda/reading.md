# Uber Distinguished Eng: Unfair Promos, Influence, Engineering Regrets | Joakim Recht

Source ID: source-ee0bbf94a641fdda
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Uber_Distinguished_Eng_Unfair_Promos,_Influence,_Engineering_Regrets_Joakim_Recht_en.txt
Video: https://www.youtube.com/watch?v=feNh_ubBAMI

[L10] [00:00.00] A software engineer needs to write code.
[L11] [00:01.84] If you're not writing code, you're not a
[L12] [00:03.84] software engineer.
[L13] [00:04.88] >> This is Yo-kim [music] Rect. He grew to
[L14] [00:07.28] be one of the few distinguished
[L15] [00:08.72] engineers among thousands at Uber. And I
[L16] [00:11.20] asked him about how he did it. What are
[L17] [00:13.28] the typical ways to have your work being
[L18] [00:15.92] influencing [music] more and more
[L19] [00:17.44] engineers?
[L20] [00:18.24] >> I like the idea of like you become a
[L21] [00:19.84] forceful multiplier by allowing other
[L22] [00:21.84] people to work better and faster.
[L23] [00:23.58] [music]
[L24] [00:24.00] >> He was also on a ton of promo
[L25] [00:25.52] committees. So I asked him about what
[L26] [00:27.12] most engineers never get to see. What
[L27] [00:29.76] does it mean when you're saying promos
[L28] [00:31.60] are not fair? Sometimes
[L29] [00:32.96] >> it gets super unfair because it all
[L30] [00:34.48] depends on how good is your manager at
[L31] [00:36.32] presenting your case. And if you have a
[L32] [00:38.08] [ __ ] manager, you have a [ __ ] case.
[L33] [00:40.40] >> Is there an engineering mistake that you
[L34] [00:42.88] saw happen at Uber that was only obvious
[L35] [00:45.68] in hindsight?
[L36] [00:46.64] >> And I maybe somebody's going to be super
[L37] [00:48.48] angry about this. I don't know. But uh
[L38] [00:51.04] >> here's the full episode.
[L39] [00:56.72] What was the initial problem that you
[L40] [00:58.48] were solving and the story behind the
[L41] [01:00.40] project that eventually got you promoted
[L42] [01:02.00] to distinguished?
[L43] [01:03.20] >> Not that long after I started at Uber,
[L44] [01:05.52] we were at the local office in Denmark,
[L45] [01:07.52] we had been tasked with building a new
[L46] [01:10.80] data store for Uber. like previously ran
[L47] [01:13.76] on just Postgress single instance like
[L48] [01:16.32] just a big ass machine and lot of like a
[L49] [01:18.80] lot of replicas and stuff like that but
[L50] [01:20.08] like a single database and that was kind
[L51] [01:22.16] projected to run out at a certain point
[L52] [01:23.76] in time so before that point in time we
[L53] [01:25.92] had to like have a new data store in
[L54] [01:27.60] place uh so in the office we were
[L55] [01:30.24] building a new have object store that's
[L56] [01:33.60] called schemalist there's also a lot of
[L57] [01:34.96] stuff about that out there u schema is
[L58] [01:37.36] bas based on shed my sql my job was
[L59] [01:42.08] primar primarily handling all those my
[L60] [01:43.84] SQL shots, managing and operating them,
[L61] [01:47.84] monitoring, scaling, all that stuff. And
[L62] [01:51.28] in the early setup, it was basically
[L63] [01:52.80] just like bare metal puppets and my SQL.
[L64] [01:57.28] And so every time you had to like do a
[L65] [01:59.44] promote a a master promotion or any kind
[L66] [02:02.72] of maintenance or replacement, you had
[L67] [02:05.20] to do some puppet mangling. You had
[L68] [02:07.76] login mangled puppet, hope for the best.
[L69] [02:10.40] And that was kind of it was pretty hard
[L70] [02:12.48] and it got harder and harder because the
[L71] [02:14.48] system kind of scaled more and more uh
[L72] [02:17.36] or grew more and more and so at around
[L73] [02:19.92] that time also like it's not that dugger
[L74] [02:21.84] was super new at that point in time but
[L75] [02:23.60] containerization was fairly fairly new
[L76] [02:26.08] concept still uh some people were using
[L77] [02:28.40] it some people weren't kubernetus I
[L78] [02:30.56] think was out in like it just got
[L79] [02:32.40] released in the like the first alpha
[L80] [02:33.92] version um just around that time so I
[L81] [02:37.92] had the like I at some point we kind
[L82] [02:40.00] start talking about I like why don't we
[L83] [02:41.84] actually just run the databases in DA so
[L84] [02:44.32] that we can both run different MySQL
[L85] [02:46.96] versions more easily we don't have to
[L86] [02:49.20] like have the entire host we can
[L87] [02:51.28] actually run multiple databases on a
[L88] [02:53.36] single host because when you run the
[L89] [02:54.72] sharded my SQL things it's a bit
[L90] [02:56.80] expensive if you want your own database
[L91] [02:59.20] and that then requires probably at least
[L92] [03:02.24] nine physical servers to run a database
[L93] [03:05.04] that it gets pretty expensive especially
[L94] [03:07.20] because you're not going to utilize it
[L95] [03:09.20] So why don't we why don't we virtualize
[L96] [03:11.60] and containerize some of that so that we
[L97] [03:13.36] can improve so we can improve
[L98] [03:15.60] utilization but also it becomes much
[L99] [03:17.60] more easy to manage if we then also get
[L100] [03:20.08] take that idea that's become very common
[L101] [03:22.48] now but was very uncommon back then
[L102] [03:25.04] which is let's define what we want to
[L103] [03:27.44] have like a goal state or an intent uh
[L104] [03:30.56] and then have a system that can kind of
[L105] [03:32.00] take you there so you don't have this
[L106] [03:33.36] procedural
[L107] [03:34.96] uh promote us promote a new master or
[L108] [03:37.28] replace something you just say we want
[L109] [03:38.80] cluster it needs to have nine uh we want
[L110] [03:42.24] a database we have nine nine individual
[L111] [03:45.04] clusters three nodes each and then make
[L112] [03:46.80] that work and don't care about the
[L113] [03:48.40] details. So that was basically the idea
[L114] [03:50.64] uh like roughly we built that for
[L115] [03:52.32] schemas first and that worked out pretty
[L116] [03:54.16] well. Uh there was like a whole
[L117] [03:56.64] ecosystem around that was also
[L118] [03:58.16] monitoring and management and version
[L119] [04:00.64] control. It was like it was like all
[L120] [04:03.60] back then a was not githubs. Uh I have
[L121] [04:06.24] like a somewhat of a version to GitHubs
[L122] [04:08.64] because GitHub is like a oneway thing.
[L123] [04:10.32] Uh you push something, you hope for the
[L124] [04:12.80] best. There's not really any there's no
[L125] [04:14.88] feedback involved. Uh so you don't
[L126] [04:16.80] really know if stuff is going to work or
[L127] [04:18.16] not uh or how far it is and there's no
[L128] [04:20.24] orchestration. So we built a whole
[L129] [04:21.76] orchestration layer and monitoring on
[L130] [04:23.84] top of like a traditional GitHubs uh
[L131] [04:25.76] GitHubs uh strategy and that kind of
[L132] [04:28.56] took off and it made us
[L133] [04:31.68] much better at scaling and much better
[L134] [04:33.60] at monitoring and much better at
[L135] [04:35.04] operating and so over time we were like
[L136] [04:37.60] okay so we did that for that part uh and
[L137] [04:40.08] then the next idea was basically why
[L138] [04:41.60] don't we why don't we do that for all
[L139] [04:43.60] the different databases that we run and
[L140] [04:47.52] was basically that what became the Odin
[L141] [04:49.68] effort
[L142] [04:50.64] uh which was basically just can we build
[L143] [04:52.40] something similar that can
[L144] [04:56.40] run work for any kind of stakehold
[L145] [05:00.48] so that ideally we have a single team
[L146] [05:02.24] that can operate an entire fleet doing
[L147] [05:04.56] host maintenance doing database
[L148] [05:06.00] management doing scaling all that stuff
[L149] [05:08.24] which was previously every single back
[L150] [05:10.80] then every database technology had its
[L151] [05:13.28] own team attached to it and they did
[L152] [05:16.00] bare metal they did host management the
[L153] [05:18.64] host monitoring provisioning,
[L154] [05:20.32] decommissioning, database management,
[L155] [05:22.32] all that stuff. And it was just a lot of
[L156] [05:24.16] like everybody had their own tool chain.
[L157] [05:25.68] It was super wasteful. So basically the
[L158] [05:27.28] idea was can can we actually can we can
[L159] [05:29.44] we make a single platform that can
[L160] [05:30.88] handle all that uh and that that
[L161] [05:33.44] basically then became yeah Odin uh and
[L162] [05:35.76] that took a while let [laughter] me say
[L163] [05:37.92] that uh for many reasons like there's
[L164] [05:41.36] there's organizational like or like
[L165] [05:43.68] there's just people because they already
[L166] [05:46.00] built many many teams built their own
[L167] [05:47.68] tool chain like why do we why do we use
[L168] [05:49.68] something else but from a local point of
[L169] [05:51.52] view it's like doesn't make any sense.
[L170] [05:53.60] Um, so it just took a while a while is
[L171] [05:56.88] like yes and yes to convince everybody
[L172] [05:59.44] that was actually a good idea and then
[L173] [06:00.64] actually get it rolled out and also
[L174] [06:02.64] getting it to work with like
[L175] [06:04.96] technologies that are not that were in
[L176] [06:06.80] that are inherently
[L177] [06:08.88] not like cloud ready or like contain
[L178] [06:12.96] container ready like HDFS for example or
[L179] [06:15.68] or Kafka used to also be notoriously bad
[L180] [06:18.56] at like moving stuff around dynamically.
[L181] [06:21.92] It's like just not a thing. Uh because
[L182] [06:24.08] like host names are encoded everywhere
[L183] [06:26.16] and pod numbers and like you need to
[L184] [06:28.32] shuffle data and there's no good way of
[L185] [06:30.24] shuffling data really. So getting all
[L186] [06:32.48] that to work uh it just took a lot of
[L187] [06:35.04] time uh and effort. Uh but basically the
[L188] [06:38.48] scope but basically the that that
[L189] [06:40.08] project just grew and grew and grew in
[L190] [06:42.08] scope from like a very like uh single
[L191] [06:45.28] thing where we just need we need just
[L192] [06:46.88] need to manage our own team stuff to
[L193] [06:49.12] actually managing the entire company on
[L194] [06:51.76] the stateful side and when I when I left
[L195] [06:54.48] it was actually running all the like all
[L196] [06:56.24] the stateful workloads at uh which is
[L197] [06:59.12] like [sighs]
[L198] [07:00.80] I don't remember the exact numbers by
[L199] [07:02.40] now but like when I left I think we had
[L200] [07:04.00] like around 120,000 physical servers
[L201] [07:06.56] under our control. H and like around
[L202] [07:09.20] half a million like databases. Uh so
[L203] [07:12.16] like all collocated and whatever and
[L204] [07:14.80] running on
[L205] [07:16.56] being being kind of operated by a team
[L206] [07:18.48] of 20ish people which to me is like
[L207] [07:22.00] pretty insane. There was still like
[L208] [07:23.44] database teams that did the actual
[L209] [07:24.72] database like Cassandra, MySQL like
[L210] [07:27.12] expertise, but just the fleet management
[L211] [07:29.12] part of it um like the ability to be
[L212] [07:31.92] able to upgrade a kernel with a single
[L213] [07:34.96] click uh or rotate like decommission
[L214] [07:38.96] data centers or commission new data all
[L215] [07:41.20] that stuff which usually takes a whole
[L216] [07:42.96] lot of manual effort.
[L217] [07:45.20] That's that kind of over time got got
[L218] [07:47.68] pretty advanced. In my understanding the
[L219] [07:50.16] initial motivation was two main things.
[L220] [07:53.76] One is the the fragmentation of the
[L221] [07:55.84] machines. So not everyone needed a full
[L222] [07:57.68] instance. So you could save a lot of
[L223] [07:59.76] capacity. And then the other one it
[L224] [08:02.16] sounds like maybe even the bigger one is
[L225] [08:03.76] the dev velocity or the engineering time
[L226] [08:06.40] savings cuz you don't need as many
[L227] [08:08.80] production engineers to manage all these
[L228] [08:11.84] instances. And also just the consistency
[L229] [08:14.48] of of that part like you want the kind
[L230] [08:17.36] of the same availability all over the
[L231] [08:19.36] place. You don't want to have everybody
[L232] [08:20.64] invent
[L233] [08:22.40] ways of making sure that servers are
[L234] [08:25.28] working and when do you discover
[L235] [08:26.88] something is broken? Uh when how do you
[L236] [08:29.20] discover that a disc doesn't work any
[L237] [08:30.88] long or whatever it might be. Like you
[L238] [08:32.64] don't want everybody to go around do
[L239] [08:34.08] that doing that by themselves. You kind
[L240] [08:35.68] of want that to just be done once.
[L241] [08:37.84] Sounds like you didn't have a grand plan
[L242] [08:39.76] for it to eventually be all of managing
[L243] [08:42.80] all of Uber's uh stateful workloads. So
[L244] [08:45.92] what is it that you saw at the beginning
[L245] [08:47.68] and how did you convince people that you
[L246] [08:50.00] should start using um Docker for
[L247] [08:52.80] databases?
[L248] [08:53.84] >> Well, so one of the good things about
[L249] [08:55.12] Uber especially in the early days was
[L250] [08:57.60] just a lot of freedom. That freedom also
[L251] [08:59.92] came with a lot of cost. I think at some
[L252] [09:01.92] point somebody counted that we were
[L253] [09:03.84] using Adubo there were like something
[L254] [09:05.92] like 52 maybe different database
[L255] [09:09.52] technologies in use in the company which
[L256] [09:12.24] is like that's a lot. Uh uh but on the
[L257] [09:16.64] other hand we also had the freedom to
[L258] [09:18.88] basically pick what we wanted. Um so the
[L259] [09:22.72] decision was was a fairly easy one
[L260] [09:25.44] because we didn't have to like there
[L261] [09:27.92] were not a lot of people who had to be
[L262] [09:29.28] involved in it. there was some people
[L263] [09:30.32] but it was not a lot of people who had
[L264] [09:32.08] to be involved in it. Um so in that
[L265] [09:35.36] sense it was fairly it was fairly easy
[L266] [09:37.92] on the on like the first thing because
[L267] [09:39.44] we just did it for our team by ourselves
[L268] [09:41.68] and that was like how Uber operated for
[L269] [09:44.24] better for worse. Um
[L270] [09:47.44] so that part was pretty easy. I think
[L271] [09:48.88] the the harder part was when we kind of
[L272] [09:50.88] realized we should really be doing this
[L273] [09:52.72] for everything. uh there it became a a
[L274] [09:56.00] bigger project to kind of convince
[L275] [09:58.56] people that it's the right thing and and
[L276] [10:00.96] and we also did not con try to convince
[L277] [10:03.60] everybody at the same time. We said
[L278] [10:05.68] we're going to build this thing. The
[L279] [10:08.08] long-term idea is to make to do it for
[L280] [10:10.48] everything, but we're going to start
[L281] [10:12.72] like it would be a very incremental
[L282] [10:14.16] effort going to start with with the
[L283] [10:16.16] stuff that we own in our office. Then
[L284] [10:18.64] we're going to do the things that are
[L285] [10:20.48] owned by
[L286] [10:23.12] our our friends uh in other departments
[L287] [10:27.04] and then we're go going to broader and
[L288] [10:28.72] broader to people who who are more more
[L289] [10:30.96] resistant to to stuff like this. Uh that
[L290] [10:33.84] we kind of that we knew up front. Uh we
[L291] [10:37.36] also knew that we like we're not going
[L292] [10:39.44] to have like a ready platform like from
[L293] [10:41.36] day one anyway. So we don't want to have
[L294] [10:43.60] everybody on on day one. Um, but baby
[L295] [10:47.68] was like a like I always have like a I
[L296] [10:50.88] don't want to force anything down
[L297] [10:53.04] anybody's throat. Uh, so I just want
[L298] [10:56.72] like I want to build I prefer to build
[L299] [10:58.64] something and ensure that it actually
[L300] [10:59.84] works and then people can kind of say
[L301] [11:01.84] okay that maybe isn't that bad than if
[L302] [11:03.68] they actually see it work somewhere. So
[L303] [11:06.40] a more incremental approach to to the
[L304] [11:08.48] whole thing. And I think that that
[L305] [11:09.76] helped a lot. It also took a very long
[L306] [11:12.80] time.
[L307] [11:13.76] >> When you said there were challenges when
[L308] [11:15.84] you were influencing the other teams uh
[L309] [11:18.48] to adopt this, what was the main push
[L310] [11:20.96] back that you'd hear and how did you
[L311] [11:22.40] convince people?
[L312] [11:23.92] >> Well, I think one push back is just that
[L313] [11:26.72] we already have something and it works.
[L314] [11:29.20] So, it's a waste to do something else.
[L315] [11:32.00] Um I and I I can see where I see that
[L316] [11:36.08] argument, but it's also a kind of local
[L317] [11:38.08] perspective. It's not a global
[L318] [11:40.32] perspective. Like when we built this, it
[L319] [11:42.00] was more of like from like a companywide
[L320] [11:44.16] perspective of like we want to improve
[L321] [11:46.64] the general state of stateful workloads.
[L322] [11:50.40] We don't just want to improve your
[L323] [11:52.00] thing. Uh so it does also come with a
[L324] [11:54.16] little bit of like yeah so some things
[L325] [11:55.84] will be much nicer but some things will
[L326] [11:58.48] also be
[L327] [12:00.24] kind of annoying.
[L328] [12:02.16] uh like for example uh because Uber
[L329] [12:05.28] didn't and still doesn't have a full uh
[L330] [12:09.92] uh software defined network where you
[L331] [12:12.00] can just like
[L332] [12:13.92] virtually move IP addresses around and
[L333] [12:16.56] host names. You like if you get a new
[L334] [12:18.40] host you get a new host name you get a
[L335] [12:20.40] random port number and that's it. So you
[L336] [12:22.40] can you can't like do a logical move of
[L337] [12:24.32] something and that that just for some
[L338] [12:26.48] storage technologies it makes it really
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
[L661] [24:56.72] did get more structured Uh but it is
[L662] [25:00.08] just super hard because it you cannot
[L663] [25:02.24] there's just no way you can objectively
[L664] [25:04.24] judge
[L665] [25:07.52] how a person is doing because there's so
[L666] [25:10.24] many dimensions. There's so many things
[L667] [25:12.88] you're not operating in isolation. Maybe
[L668] [25:15.20] you depend on like maybe the thing you
[L669] [25:16.72] were doing actually depended on another
[L670] [25:17.92] team and that team didn't do what they
[L671] [25:20.16] said they would do. They just like
[L672] [25:22.96] ghosted you or whatever. like
[L673] [25:25.84] they didn't do it and it's like so what
[L674] [25:28.00] that's not your fault or maybe you had
[L675] [25:30.32] the project it was running it was almost
[L676] [25:32.56] in production then it gets canceled by
[L677] [25:34.24] management just for various reasons not
[L678] [25:36.80] your fault but like then what like are
[L679] [25:39.92] you then not getting promoted or are you
[L680] [25:42.48] getting promoted and if if you're
[L681] [25:44.00] getting promoted then on what basis like
[L682] [25:46.56] is it just like oh because you wrote a
[L683] [25:48.00] lot of code but the code was like never
[L684] [25:49.44] used and nobody ever saw it again and so
[L685] [25:51.92] like it's is hard because sometimes you
[L686] [25:55.28] also like yeah you did a really good
[L687] [25:57.44] effort and we don't want to demotivate
[L688] [25:59.12] you completely by saying because it
[L689] [26:00.40] didn't go to production it was not your
[L690] [26:02.48] fault you're not getting a promotion. Uh
[L691] [26:05.60] other times it's like you just also have
[L692] [26:07.76] to make the thing where like you really
[L693] [26:09.52] haven't proven anything yet.
[L694] [26:12.00] You did a lot of good work but it's just
[L695] [26:14.96] like was not your fault but you're not
[L696] [26:16.88] getting promoted. Um, so yeah, ideally
[L697] [26:20.80] there's just fairness all around, but I
[L698] [26:22.88] think there's there is just inherently
[L699] [26:24.80] in a in because it's a human process.
[L700] [26:26.56] There's just a a fair amount of
[L701] [26:27.92] unfairness. Um, and then I think there's
[L702] [26:31.68] there's a lot of people who don't really
[L703] [26:33.76] understand what it means. like they
[L704] [26:35.92] think it's super unfair because they
[L705] [26:39.12] think they did really well and compared
[L706] [26:41.92] to maybe the team they did super well
[L707] [26:44.56] but it's just also because the team is
[L708] [26:46.00] not very well very good or you live you
[L709] [26:49.20] lived on an island and you hadn't
[L710] [26:51.12] realized that there's another world out
[L711] [26:54.00] there that's actually very different and
[L712] [26:55.84] more whatever um which I think just in
[L713] [27:00.48] the early days of like Uber used to be a
[L714] [27:02.56] Python shop well first like a JavaScript
[L715] [27:04.72] Python shop. Then it went into a Go kind
[L716] [27:07.44] of shop and like nobody knew Go. So
[L717] [27:10.88] there was a lot of like a lot of people
[L718] [27:13.12] just trying [ __ ] out and so you would
[L719] [27:15.36] kind of encounter these these kind of
[L720] [27:17.36] groups of people who kind of had been in
[L721] [27:19.28] under their own influence
[L722] [27:21.60] and like and you just look at the what
[L723] [27:23.76] they have produced and like this is not
[L724] [27:26.88] this is no good. [laughter] Like this is
[L725] [27:29.04] just no good. uh even though you you
[L726] [27:31.36] kind of uh maybe yeah sure there's one
[L727] [27:33.12] of you who's better than the other
[L728] [27:34.16] whatever like but it's just like as a as
[L729] [27:36.32] a whole it's just no good. Uh so we
[L730] [27:38.16] cannot we just cannot promote you
[L731] [27:40.64] because you need to look at what's going
[L732] [27:42.48] on over here. Um and that can that can
[L733] [27:45.12] just feel super super unfair to those
[L734] [27:48.40] people. Uh because if they were not
[L735] [27:51.04] prepared for what they actually went
[L736] [27:53.44] into, I think that's also why I try I I
[L737] [27:57.36] kind of made this effort of like trying
[L738] [27:59.52] to describe how can you actually get
[L739] [28:01.04] promoted like what does it mean? And
[L740] [28:03.28] it's not about like I know like I I
[L741] [28:04.88] think I call it something like beating
[L742] [28:06.40] the promo committee or whatever uh which
[L743] [28:08.72] can just like a a a catchy title but it
[L744] [28:12.64] was really more about like what does it
[L745] [28:14.64] actually mean to be a software engineer
[L746] [28:16.72] at Uber?
[L747] [28:18.48] uh because you have kind of all sort of
[L748] [28:19.52] the ideas what that means but but
[L749] [28:21.36] actually there is something there is a
[L750] [28:22.88] way to be a software engineer at Uber
[L751] [28:25.20] like there's there's and that way is
[L752] [28:27.04] most likely different than meta or
[L753] [28:29.36] Google or whatever and I think it's
[L754] [28:31.52] pretty pretty important to be aware of
[L755] [28:32.96] that because otherwise you kind of
[L756] [28:35.12] worked towards something and that was
[L757] [28:38.00] not the thing that it should have been
[L758] [28:40.48] um and that that that can that can
[L759] [28:42.88] create a lot of frustration and a lot of
[L760] [28:44.40] disappointment uh yeah uh which uh and
[L761] [28:49.12] it's and it's too bad uh that that
[L762] [28:50.80] people can't get into that state and
[L763] [28:52.72] don't get the correction uh along the
[L764] [28:55.36] way that they go all the way to promo
[L765] [28:57.68] have prepared a package written a lot of
[L766] [28:59.52] stuff gotten feedback getting peer
[L767] [29:01.84] feedbacks or whatever and then the the
[L768] [29:04.64] promo committee is like nah it's no
[L769] [29:06.80] good.
[L770] [29:08.32] >> Yeah. you you said you wrote that piece
[L771] [29:10.96] that was how to beat the promo committee
[L772] [29:13.52] and it's basically you know the the way
[L773] [29:16.08] that you grow as an engineer at Uber and
[L774] [29:18.80] it's it's not focused on actually the
[L775] [29:21.28] specifics of like the promo packets it's
[L776] [29:24.16] actually focused on how do you become a
[L777] [29:25.76] stronger engineer what was in there
[L778] [29:28.72] >> mainly just to say like good engineering
[L779] [29:31.60] practices and something that I found
[L780] [29:33.92] surprising and like I actually found
[L781] [29:35.36] surprising during all my years at Uber
[L782] [29:38.00] which is well I don't it also met our
[L783] [29:40.72] philosophy but I'm like a software
[L784] [29:42.32] engineer needs to write code if you're
[L785] [29:43.92] not writing code you're not a software
[L786] [29:45.92] engineer I know that's some people find
[L787] [29:47.76] that pretty controversial for some I
[L788] [29:49.20] don't know why but like apparently it is
[L789] [29:51.04] to me that and that applies to any level
[L790] [29:53.84] like if your level if your title
[L791] [29:56.16] includes engineer
[L792] [29:58.24] you should be writing code and there's a
[L793] [30:01.04] it might be different how much code you
[L794] [30:02.48] write but you should be writing code on
[L795] [30:04.16] a regular basis
[L796] [30:06.24] um and to me regular basis means every
[L797] [30:09.20] day. I know for some people might just
[L798] [30:11.84] means once a week or whatever but like I
[L799] [30:14.64] to me it's like every day uh ideally. So
[L800] [30:17.84] like I think the main advice in that
[L801] [30:20.24] thing was really just write code
[L802] [30:25.04] don't don't mess around [laughter]
[L803] [30:28.00] and and don't like don't overthink it
[L804] [30:30.08] either like don't like oh I need to
[L805] [30:32.56] write like advanced uh at my level code
[L806] [30:35.20] or whatever like the the higher my level
[L807] [30:37.36] the more advanced my code has to be like
[L808] [30:39.36] don't no it just like just write code
[L809] [30:41.76] because the more like if you have that
[L810] [30:44.96] if you do that uh I have just never seen
[L811] [30:47.60] anybody who will not grow along with
[L812] [30:49.84] that and just keep writing the same code
[L813] [30:52.16] like doesn't make any sense. Um so I
[L814] [30:55.76] think that was the main advice was
[L815] [30:57.12] actually just that just write code also
[L816] [31:00.32] write good code like the secondary
[L817] [31:02.08] advice and make make good good uh commit
[L818] [31:04.40] messages and make sure to review code
[L819] [31:06.16] and make your code nice to review and
[L820] [31:08.00] all just like standard
[L821] [31:11.28] software [snorts] practice which people
[L822] [31:13.92] kind of I don't know forget a bit about
[L823] [31:16.80] many people also like might not have
[L824] [31:18.88] learned it because like normally you
[L825] [31:20.48] don't actually learn like real life
[L826] [31:21.92] software engineering out of college or
[L827] [31:23.76] wherever you are, it's all theory. But
[L828] [31:26.08] like in real life, there's just there
[L829] [31:27.92] there's also there's also a
[L830] [31:29.76] craftsmanship to it that you have to
[L831] [31:31.76] learn and you don't learn learn that in
[L832] [31:34.48] isolation. It's almost impossible to
[L833] [31:35.84] learn it by yourself. Well, these days
[L834] [31:37.28] you can get a lot of help uh from from
[L835] [31:39.84] AI and whatever, but like you you have
[L836] [31:42.64] to like see somebody doing it in order
[L837] [31:44.64] to improve. Um, yeah. So, I think those
[L838] [31:48.48] were really the that was really the main
[L839] [31:50.48] thing and and there's a lot of other
[L840] [31:52.56] things, smaller things about it because
[L841] [31:54.32] you also need to be able to actually
[L842] [31:56.00] articulate what you're doing like design
[L843] [31:57.68] documents. You also need to like be out
[L844] [32:00.56] there like you like having like my my
[L845] [32:05.44] other one of my other philosophies is
[L846] [32:07.44] like running code beats perfect code
[L847] [32:10.72] anything.
[L848] [32:12.40] I know you can always come up with like
[L849] [32:13.92] weird S cases but in in the big picture
[L850] [32:18.48] running code will always beat working
[L851] [32:20.80] like perfect code or beautiful code or
[L852] [32:22.96] whatever. Uh and that could be as as a
[L853] [32:26.24] software engineer pretty hard to like
[L854] [32:27.68] like some people because some people are
[L855] [32:29.12] really oh no no like like it needs to
[L856] [32:31.36] handle the cases and whatever. Um I I I
[L857] [32:35.92] I I'm I'm just much more of like yeah
[L858] [32:39.20] just do something because if you do the
[L859] [32:41.44] perfect thing you get tied up in this oh
[L860] [32:44.24] in order to kind of submit code I have
[L861] [32:46.64] to have all the I have to do the entire
[L862] [32:48.80] thing and it must handle all cases and
[L863] [32:51.68] then you kind of work on some that's
[L864] [32:53.36] where you kind of start working on
[L865] [32:54.48] something and then you refactor and you
[L866] [32:56.80] do some more and then event like after a
[L867] [32:58.72] month you do a commit and
[L868] [33:03.68] That's just not useful because you did
[L869] [33:05.36] not get any feedback. You never saw it.
[L870] [33:07.84] You might be on a completely wrong track
[L871] [33:09.36] like god knows what.
[L872] [33:10.64] >> One common advice I hear when people are
[L873] [33:13.84] thinking about growing in their career
[L874] [33:16.08] is that they have to scale themselves
[L875] [33:18.32] and that often points them towards being
[L876] [33:21.60] more and more of a delegator and more
[L877] [33:24.88] and more of a tech lead. and they start
[L878] [33:27.28] getting into this zone where they're in
[L879] [33:29.60] these highle discussions in the design
[L880] [33:31.92] docs but not actually writing any code.
[L881] [33:35.36] What's your thought on that? Because
[L882] [33:36.96] that's like a very common thing that
[L883] [33:38.96] people will push on higher level
[L884] [33:40.56] engineers say stop writing code go and
[L885] [33:42.72] delegate.
[L886] [33:43.60] >> Yeah. And like as like personally I like
[L887] [33:45.52] I I don't subscribe to that idea at all.
[L888] [33:47.68] I see that a lot. Uh this is also like
[L889] [33:51.04] some it's also just about like to some
[L890] [33:54.64] degree it's also what you about what you
[L891] [33:56.72] find interesting and I I just like
[L892] [33:58.88] writing code. I just do I have always
[L893] [34:01.28] liked it. It's just like what I like to
[L894] [34:02.64] do. I would probably like if I had if I
[L895] [34:04.40] didn't have anything else to do what I
[L896] [34:06.08] do but I would do if I didn't have a job
[L897] [34:07.84] I would probably also do it. Uh so like
[L898] [34:10.32] I just like it. Um, but I think there's
[L899] [34:13.52] also just a very big overlap
[L900] [34:16.16] between like just the between the
[L901] [34:19.12] writing of code and the ability to like
[L902] [34:22.40] um perform [clears throat]
[L903] [34:24.32] uh at any level. Uh, and to me it's it's
[L904] [34:27.20] like it's there are many facets to it.
[L905] [34:29.68] Uh, I think one thing is if you're not
[L906] [34:32.48] writing code, you lose touch with like
[L907] [34:35.28] the system.
[L908] [34:37.60] uh not on day one of course because like
[L909] [34:39.44] on day one if you stop writing code on
[L910] [34:41.28] day one and one month one it's fine
[L911] [34:44.08] because you you kind of remember what
[L912] [34:45.60] was going on but the system evolves all
[L913] [34:47.12] the time and you forget how it is and
[L914] [34:48.56] you kind of probably get a more more and
[L915] [34:50.24] more high level like view of what's
[L916] [34:52.48] actually going on inside the machine.
[L917] [34:55.12] Um, so and that just means it gets
[L918] [34:58.00] harder and harder for you to kind of um
[L919] [35:02.32] design for the f future like the designs
[L920] [35:04.96] you come up with will be more and more
[L921] [35:09.28] uh decoupled from reality and be more
[L922] [35:12.40] and more it might be idealistic. Uh
[L923] [35:15.60] whereas like and then when it gets to
[L924] [35:17.36] actually implementing it's handed off to
[L925] [35:18.72] somebody else and they're like what is
[L926] [35:20.00] this [ __ ] Uh and who came up with this?
[L927] [35:22.72] Oh, that's that that's that guy with the
[L928] [35:25.52] with the whiteboard and like what and
[L929] [35:27.28] and the documents like what who's that
[L930] [35:30.32] to like say what we should should be
[L931] [35:33.04] doing because we the actual problems we
[L932] [35:35.28] have are like this. Um so I think that's
[L933] [35:40.24] I think that's one main that's one major
[L934] [35:43.28] thing. Um and tied to that is the is the
[L935] [35:47.20] kind of how do you actually build a team
[L936] [35:50.40] because as you say you need to scale
[L937] [35:52.08] yourself that's for sure. Um or I think
[L938] [35:55.92] another way of of saying you need to
[L939] [35:57.60] scale yourself is you need to enable as
[L940] [35:59.92] many people to work as efficiently as
[L941] [36:03.52] possible. Um which I think is a bit
[L942] [36:06.88] different than just scaling yourself.
[L943] [36:08.56] It's getting the sounds that you're kind
[L944] [36:10.08] of cloning yourself which is like
[L945] [36:12.40] usually doesn't quite work. Uh
[L946] [36:15.60] but if you need to kind of make your
[L947] [36:18.00] team
[L948] [36:20.00] the when I say your team like the people
[L949] [36:22.64] around you the people you're supposed to
[L950] [36:24.32] influence if you're kind of supposed to
[L951] [36:26.80] kind of affect change whatever the
[L952] [36:29.20] change might be it just is much easier
[L953] [36:31.36] to do if they trust you. They know what
[L954] [36:34.56] they know that you know that what their
[L955] [36:37.52] pain points are and they that you that
[L956] [36:40.32] they know that if you say something it
[L957] [36:42.72] usually works out
[L958] [36:45.12] or if they say something then you listen
[L959] [36:47.20] to them.
[L960] [36:49.04] Um and so that that decoupling kind of
[L961] [36:52.00] it hurts in that sense because you get
[L962] [36:55.20] new people in like of course the people
[L963] [36:57.28] you work with before they will know you
[L964] [36:59.68] so they're kind of okay but like people
[L965] [37:01.52] start rotating in and out so you lose
[L966] [37:04.40] more and more touch with both the people
[L967] [37:05.76] and the system and that over time gets
[L968] [37:08.40] you to it might be a pretty bad state
[L969] [37:10.72] where yeah you're doing a lot of designs
[L970] [37:12.64] and you're doing a lot of documents and
[L971] [37:14.00] you're doing a lot of talking and
[L972] [37:15.84] reviewing and whatnot but you lose more
[L973] [37:18.08] and more touch with what is actually
[L974] [37:19.52] going on and then um and this might be
[L975] [37:23.12] just be an Uber thing uh but you get
[L976] [37:25.44] more more hostility also and people
[L977] [37:27.44] won't tell you to your face like but you
[L978] [37:30.00] will be everybody will think who's that
[L979] [37:32.72] [ __ ] or who's that kind of guy to
[L980] [37:35.52] like come and say whatever. So, you're
[L981] [37:37.68] saying if if you're not hands-on, you
[L982] [37:40.56] lose trust. And then people won't tell
[L983] [37:43.52] you that you've lost trust. And then if
[L984] [37:45.44] you try to influence them or or convince
[L985] [37:48.16] them, they're going to, you know, not go
[L986] [37:51.44] your way.
[L987] [37:52.32] >> Yeah. I think I think at least I've seen
[L988] [37:54.48] that a lot. Uh, and the the the the
[L989] [37:58.08] other thing is if you're not like in
[L990] [38:00.88] there, uh, then at least personally, um,
[L991] [38:05.36] I I don't want anybody to tell me what
[L992] [38:07.52] I'm supposed to do. Uh, [laughter]
[L993] [38:10.96] it's not it's not that I'm not open for
[L994] [38:12.88] input. Really like to talk about it, but
[L995] [38:16.96] if you don't have skin in the game, I I
[L996] [38:20.00] think you should stay out of my things.
[L997] [38:22.80] Uh and then I will also promise to stay
[L998] [38:25.36] out of new things. Uh uh if you ask for
[L999] [38:28.72] help, more than willing to help. If I
[L1000] [38:30.64] ask for help, I hope that somebody will
[L1001] [38:32.00] help. But and so so that whole thing
[L1002] [38:34.48] about like if you kind of do this top
[L1003] [38:36.72] down, oh by the way, now we're supposed
[L1004] [38:38.48] to do this. People don't really know
[L1005] [38:39.84] you, don't know where you're coming
[L1006] [38:40.88] from, don't know why why you're saying
[L1007] [38:42.16] what you're saying. That just it just
[L1008] [38:43.68] creates a lot of mistrust and and in and
[L1009] [38:46.00] in some cases just plain hostility. Um
[L1010] [38:49.52] and and I maybe in the worst case people
[L1011] [38:52.00] will kind of say, "Yeah, that's a pretty
[L1012] [38:53.12] good idea." And then they will just
[L1013] [38:55.76] completely gaslight you and just like go
[L1014] [38:57.84] go back and not not do any of the stuff
[L1015] [39:00.56] that you talked about. Uh
[L1016] [39:03.92] probably the most annoying outcome that
[L1017] [39:05.84] you can get. Uh you said something in my
[L1018] [39:09.20] research, you said something somewhere.
[L1019] [39:10.48] said if a VP says the exact same thing
[L1020] [39:14.16] an engineer does, engineers will still
[L1021] [39:17.20] not fully trust the VP. And so yeah,
[L1022] [39:20.32] that my question is why don't engineers
[L1023] [39:22.56] trust management? Yeah, but I think it's
[L1024] [39:25.12] back to that um that if you don't really
[L1025] [39:28.56] like if you have somebody who you feel
[L1026] [39:31.44] don't really know what they're talking
[L1027] [39:33.04] about to some degree. Uh like they might
[L1028] [39:36.48] have an idea but they don't really like
[L1029] [39:38.40] and that but that idea might be
[L1030] [39:40.08] completely off because they haven't
[L1031] [39:41.92] really spent the time to kind of
[L1032] [39:44.16] understand what is actually going on.
[L1033] [39:46.64] Um, it might be that they're completely
[L1034] [39:48.72] right,
[L1035] [39:50.72] but but it's just it's just I don't
[L1036] [39:54.08] know. I don't know if it's just human
[L1037] [39:56.00] whatever nature or if it's just like if
[L1038] [39:57.84] it's just me. Uh, but [laughter]
[L1039] [40:00.32] but I I just I just know from myself and
[L1040] [40:03.36] from other people I've seen is like
[L1041] [40:05.52] somebody says something and if you don't
[L1042] [40:07.92] like if you don't have a connection to
[L1043] [40:09.60] them,
[L1044] [40:11.20] then it's just hard to like take at face
[L1045] [40:13.52] value. And if face value is all that is
[L1046] [40:16.16] or or force like authority uh like if
[L1047] [40:21.12] authority is the only thing
[L1048] [40:24.16] it just at least in
[L1049] [40:26.88] so this might also be a super local
[L1050] [40:29.04] thing here like in like a Danish thing
[L1051] [40:31.04] like because it's like there's basically
[L1052] [40:32.88] no structure anywhere. Uh but it's also
[L1053] [40:37.28] a thing in Bay Area where like authority
[L1054] [40:41.76] in itself
[L1055] [40:43.60] doesn't really get you all the way. Uh
[L1056] [40:48.08] it it and again people might like say
[L1057] [40:50.08] yeah not a smile and yeah that's that's
[L1058] [40:52.24] nice but if they don't truly believe it
[L1059] [40:56.08] and I have I have just seen so many
[L1060] [40:57.60] times where people yeah that's nice and
[L1061] [40:59.36] they just they they don't mean it.
[L1062] [41:02.17] [laughter]
[L1063] [41:02.72] And if you don't mean it, then how are
[L1064] [41:04.48] you supposed to successfully implement a
[L1065] [41:06.16] project? It would just it will always be
[L1066] [41:08.80] maybe it gets done, but it will be a bit
[L1067] [41:10.72] like it won't like if you if people
[L1068] [41:12.56] don't think it's a good idea, they don't
[L1069] [41:14.16] take ownership. It's just not going to
[L1070] [41:15.92] be really nice. Uh so and so I think
[L1071] [41:19.20] that just takes effort and it takes much
[L1072] [41:21.12] more effort than you normally like that
[L1073] [41:22.88] than you would like it to be. Yeah.
[L1074] [41:25.84] >> You had to influence a ton of people in
[L1075] [41:28.24] getting your project to scale across
[L1076] [41:30.08] Uber. So if Yeah. How do you influence
[L1077] [41:34.16] other engineers then and avoid that
[L1078] [41:36.16] situation you're talking about?
[L1079] [41:37.52] >> Yeah. And again like as I said before
[L1080] [41:40.48] like there's probably always going to be
[L1081] [41:42.24] be somebody somewhere who's like they're
[L1082] [41:46.00] never going to be convinced. Just never
[L1083] [41:49.36] go for 100%. Like that's one thing at
[L1084] [41:52.08] least. Um but but but to me it's really
[L1085] [41:55.04] like I I just believe a lot in leading
[L1086] [41:57.12] by example. like if you say this is what
[L1087] [42:00.72] you're going this is what we're going to
[L1088] [42:02.08] build then you help building and you
[L1089] [42:05.60] also take a lot of the pain and I think
[L1090] [42:09.52] in particular and there's also the thing
[L1091] [42:11.68] about like another thing that that can
[L1092] [42:14.32] very quickly happen is that the the the
[L1093] [42:16.48] the higher level you get uh the more you
[L1094] [42:19.52] can concentrate on the like the hard
[L1095] [42:20.96] stuff the stuff that you there that is
[L1096] [42:24.24] only you who can do um but but That's
[L1097] [42:28.48] really not a lot that only you can do.
[L1098] [42:30.96] Uh there might be a couple of things but
[L1099] [42:32.40] it's really not a lot. So all the other
[L1100] [42:35.04] stuff there there's some tendencies for
[L1101] [42:37.44] people to like say oh because I came up
[L1102] [42:40.24] with the idea I should also implement
[L1103] [42:42.00] the most interesting stuff or what are
[L1104] [42:43.92] new algorithms or whatever or like I
[L1105] [42:46.48] should play with the fun stuff. Um, and
[L1106] [42:49.60] sometimes you do that, but but I think
[L1107] [42:51.92] most of the time you should really
[L1108] [42:53.04] delegate that down. Like you should
[L1109] [42:55.28] delegate the hard stuff down, not and
[L1110] [42:57.36] just keep the easy not the easy stuff,
[L1111] [42:59.36] but um but the stuff that is kind of
[L1112] [43:02.48] boring and you should just do that
[L1113] [43:04.64] yourself because again, you don't have
[L1114] [43:06.24] to prove anything any longer. Once you
[L1115] [43:08.32] once you have reached a certain level,
[L1116] [43:09.84] you don't have to prove anything. You
[L1117] [43:11.60] can do what you want. And so at that
[L1118] [43:13.92] point it's much better to in in my view
[L1119] [43:15.68] at least push down the hard stuff to the
[L1120] [43:18.48] people who can like barely manage it and
[L1121] [43:20.40] then help them uh make sure that they do
[L1122] [43:23.20] that kind they're kind of in the right
[L1123] [43:24.72] direction and then let them kind of work
[L1124] [43:27.20] with that rather that take that yourself
[L1125] [43:29.68] and then delegate all the [ __ ] work
[L1126] [43:32.00] that's that that doesn't help anybody.
[L1127] [43:34.32] Um and we have like we had like this
[L1128] [43:37.12] expression of like shoveling [ __ ] It's
[L1129] [43:39.04] not a nice expression but it is what it
[L1130] [43:40.64] is. Uh there sometimes there's just like
[L1131] [43:42.88] in order to do something there's just
[L1132] [43:45.44] some some really [ __ ] work in there. Uh
[L1133] [43:49.28] and if you take that work uh and like
[L1134] [43:52.72] the the other people do the do the the
[L1135] [43:54.56] fun work that will also it will give you
[L1136] [43:57.04] a lot of credit uh but it will also
[L1137] [43:59.68] allow them to grow much faster because
[L1138] [44:01.92] if they get challenged the rest of the
[L1139] [44:04.24] team they work much faster they they
[L1140] [44:06.96] grow much faster and that's just to to
[L1141] [44:08.48] everybody's benefit. Um so like that
[L1142] [44:11.36] whole thing that's also yeah the coding
[L1143] [44:13.92] leading by example and to me leading by
[L1144] [44:15.60] example just means writing code to a
[L1145] [44:19.04] very large degree. Uh and then taking
[L1146] [44:21.12] all this taking some of that stuff that
[L1147] [44:23.92] other people
[L1148] [44:25.76] that you don't really want to do might
[L1149] [44:28.08] also be improving documentation or
[L1150] [44:30.72] fixing weirdo bugs whatever it is. And
[L1151] [44:33.28] there's not a lot of like there doesn't
[L1152] [44:35.04] have to be a lot of like glory to it.
[L1153] [44:38.24] there's usually not a lot of glory to
[L1154] [44:39.68] it. Um, but I Yeah, I I'm a very strong
[L1155] [44:43.84] believer in in stuff like that.
[L1156] [44:46.56] >> Interesting. Yeah, that's the opposite
[L1157] [44:48.32] advice I I usually hear usually like as
[L1158] [44:50.72] you go up people say you got to do the
[L1159] [44:53.36] hardest parts, the most impressive ones
[L1160] [44:55.28] as well, complex ones to kind of warrant
[L1161] [44:58.24] it being worth your time and you push
[L1162] [45:00.64] out all the easy stuff to anyone that
[L1163] [45:02.64] can handle it that's not you. What's the
[L1164] [45:04.72] downsides of doing it that way? Yeah,
[L1165] [45:06.72] but it's also because it usually turns
[L1166] [45:08.96] out that the easy stuff has it's easy
[L1167] [45:12.88] because it's like it might be easy to
[L1168] [45:14.80] do, but then you're like, oh, this this
[L1169] [45:16.96] thing
[L1170] [45:18.48] why like why are we doing this?
[L1171] [45:21.84] And then you start thinking, oh, how can
[L1172] [45:23.60] we avoid doing that? So you kind of take
[L1173] [45:26.08] some of the easy stuff and it usually
[L1174] [45:27.44] turns it turns out to give that you can
[L1175] [45:29.20] kind of expand that to something that is
[L1176] [45:31.84] not trivial in any longer that actually
[L1177] [45:35.76] that actually did require you to come
[L1178] [45:38.00] in. It was not it was just the intention
[L1179] [45:40.32] or purpose. But when you come in and
[L1180] [45:42.32] look at like why are we why do we have
[L1181] [45:45.20] this many bucks like what is this? And
[L1182] [45:48.56] then you start thinking about is that
[L1183] [45:49.68] the because we have bad reviews because
[L1184] [45:51.44] we have bad testing because something
[L1185] [45:53.12] else and then you can kind of start like
[L1186] [45:55.28] how do we how do we kind of make that
[L1187] [45:57.44] better?
[L1188] [45:58.96] Um, so I think and I and I have I've
[L1189] [46:02.56] heard that the same advice a lot of
[L1190] [46:04.24] times and I had a lot of people come
[L1191] [46:07.12] before after promo committees or
[L1192] [46:09.68] mentoring or whatever saying oh how do I
[L1193] [46:12.80] how do I get the right project so that I
[L1194] [46:14.88] can get promoted or how do I like how do
[L1195] [46:17.92] I grow my scope or like and my advice
[L1196] [46:20.64] has always been the same
[L1197] [46:23.04] more or less forget about that part and
[L1198] [46:25.44] just start writing some code uh focus on
[L1199] [46:28.56] that just do something that works.
[L1200] [46:30.16] Doesn't have to be big. Doesn't have to
[L1201] [46:31.44] be anything. Focus on something that
[L1202] [46:32.96] works. And then every time you do
[L1203] [46:34.32] something, think about are we doing the
[L1204] [46:37.12] right thing here? Like are we
[L1205] [46:38.64] introducing because in a lot of cases
[L1206] [46:41.36] actually um when you build something you
[L1207] [46:43.60] actually introduce more work to other
[L1208] [46:45.84] people. You kind of build a system and
[L1209] [46:48.24] then you like oh this is nice for us but
[L1210] [46:50.08] then it actually turns out that for
[L1211] [46:51.28] other people now they have more work uh
[L1212] [46:54.72] because they have more systems to manage
[L1213] [46:56.24] or they need to configure some other
[L1214] [46:57.68] something else and have more stuff in
[L1215] [46:58.96] their head like how do you think about
[L1216] [47:01.12] how what what is the net overall result
[L1217] [47:04.24] of what you're doing and how can you
[L1218] [47:06.40] make that better?
[L1219] [47:08.32] uh and it just doesn't have to be big
[L1220] [47:10.48] things. Uh but if you like if you're
[L1221] [47:12.64] always working with that in mind, my
[L1222] [47:15.68] philosophy is that then the other thing
[L1223] [47:17.68] will come. Uh you don't have to like you
[L1224] [47:20.56] don't have to be like oh I I must find
[L1225] [47:22.72] something. Uh it will come. And I have
[L1226] [47:25.04] seen it not many times because there are
[L1227] [47:27.68] not many but I have seen a lot of times
[L1228] [47:30.48] where people like oh I need to do like I
[L1229] [47:33.36] need to be promoted and I need to find
[L1230] [47:35.12] the right scope. like just like relax
[L1231] [47:37.52] about that part and just focus on
[L1232] [47:40.00] providing value because once you do that
[L1233] [47:42.88] the other thing will come uh in most
[L1234] [47:45.28] cases again back to the fairness part
[L1235] [47:47.12] that cases where it doesn't come and
[L1236] [47:48.32] then too bad but like in most cases it
[L1237] [47:51.84] it does and I think it's to me it's the
[L1238] [47:54.80] by far the most successful way uh of
[L1239] [47:57.20] getting there. I'm curious as you
[L1240] [47:59.44] advance in your career because I think
[L1241] [48:01.20] this is a common thing some people
[L1242] [48:02.56] experience is did your role become more
[L1243] [48:05.44] political?
[L1244] [48:07.52] >> I'm always like what does political mean
[L1245] [48:09.84] exactly? Um
[L1246] [48:12.32] so I think there a couple things to it.
[L1247] [48:14.48] Um of course you have to talk to more
[L1248] [48:16.64] people so there's more talking and
[L1249] [48:19.28] there's more fighting because you have
[L1250] [48:22.56] to like promote your ideas. H well you
[L1251] [48:26.00] have to promote your ideas but not
[L1252] [48:27.44] probably worse you have to listen to
[L1253] [48:28.80] other people's ideas all the time uh and
[L1254] [48:31.52] because they also want something and
[L1255] [48:32.88] like I think maybe I maybe don't have I
[L1256] [48:35.68] have an opinion or you think that is not
[L1257] [48:38.00] that nice um so in that sense there's
[L1258] [48:41.76] there's a lot of like fighting going on
[L1259] [48:44.08] um I think you also get you get much
[L1260] [48:47.28] more exposed to
[L1261] [48:49.68] to like the realities
[L1262] [48:52.08] like when you're a junior engineer you
[L1263] [48:53.92] kind Oh, we're doing we're kind of doing
[L1264] [48:56.80] engineering and then somebody else has a
[L1265] [48:59.44] grand has a grand plan. They all know
[L1266] [49:01.52] what's going on. It's all under control.
[L1267] [49:04.00] Then you're like you realize at some
[L1268] [49:06.24] point [laughter]
[L1269] [49:08.16] nobody's in control. Like there's an
[L1270] [49:11.12] illusion of control,
[L1271] [49:13.36] but there's just like people randomly
[L1272] [49:17.04] getting ideas and pushing them out. Uh
[L1273] [49:20.88] and that that I think that part is
[L1274] [49:22.32] pretty scary. [laughter]
[L1275] [49:24.24] uh to to to like as a rational engineer
[L1276] [49:28.24] to get to the point where like okay so
[L1277] [49:30.96] we're making decisions just based on
[L1278] [49:33.36] nothing or because you had like a vision
[L1279] [49:37.60] while you were in the shower I don't
[L1280] [49:39.44] know
[L1281] [49:40.96] or like you talked to some other guy who
[L1282] [49:43.68] also don't know what they're talking
[L1283] [49:44.88] about and now that's the strategy um is
[L1284] [49:48.56] that politics maybe it is uh but you get
[L1285] [49:51.12] more and more like you get you get more
[L1286] [49:52.88] and more subject ed to that part and I
[L1287] [49:54.48] think that's that's pretty scary and
[L1288] [49:56.32] it's also definitely not for everybody.
[L1289] [49:58.80] Uh I didn't like it at all. I didn't
[L1290] [50:01.04] particularly like it. I can abstract
[L1291] [50:02.56] from it. I can just do my own thing. But
[L1292] [50:04.40] if you get sucked into that then it then
[L1293] [50:07.76] and a lot of people get sucked into that
[L1294] [50:10.08] because there's so much like oh we could
[L1295] [50:11.44] also do this and let's do a big plan for
[L1296] [50:13.36] whatever and then that takes like weeks
[L1297] [50:15.20] and weeks to do a plan and like
[L1298] [50:18.00] with inbox like okay now we did that
[L1299] [50:20.72] hooray. Um
[L1300] [50:23.68] and so and then there's the whole like
[L1301] [50:25.60] that that idea of like that thing about
[L1302] [50:27.28] like somebody somebody came up with an
[L1303] [50:28.80] idea and now that needs to get
[L1304] [50:30.40] implemented and there's a lot of push
[L1305] [50:31.92] back and all this stuff. Um and of
[L1306] [50:34.72] course everybody has ideas who gets
[L1307] [50:38.08] heard how do we get your how do you get
[L1308] [50:40.40] your idea in? So there's a lot of that.
[L1309] [50:43.12] Um,
[L1310] [50:44.80] my personal approach to all that was
[L1311] [50:47.44] really back to the whole thing about
[L1312] [50:49.28] like I don't need anybody to tell me how
[L1313] [50:51.68] I need to do my things. So I don't also
[L1314] [50:53.92] don't want to tell other people how how
[L1315] [50:55.28] to do their things. Uh and I also don't
[L1316] [50:59.04] like I I have never been like a like
[L1317] [51:02.48] career planner as such like I have not I
[L1318] [51:04.40] oh this is how like I get to this but I
[L1319] [51:07.76] also have a very strong aversion to
[L1320] [51:09.60] projects that I can just see are just
[L1321] [51:13.28] stupid or dead ends or whatever you call
[L1322] [51:15.84] them and just stay away from them and
[L1323] [51:18.24] let somebody else do that. And that's
[L1324] [51:20.32] might be a little bit unfair to those
[L1325] [51:21.68] other people sometimes. Uh but that's
[L1326] [51:24.16] kind of how how I kind of kept my sanity
[L1327] [51:27.28] was basically say, well, okay, this
[L1328] [51:29.28] thing I think you should like it's fine.
[L1329] [51:32.72] You're already enough people. Like you
[L1330] [51:35.20] have plenty of people. I don't need to
[L1331] [51:36.56] be involved. I I have I have my own
[L1332] [51:38.80] thing over here that I can do. I don't
[L1333] [51:40.40] need all that stuff. Uh and of course,
[L1334] [51:42.56] as long as my thing is significant
[L1335] [51:45.20] enough, because if you don't have
[L1336] [51:46.48] anything to do, you're kind of a little
[L1337] [51:47.60] bit then you need to engage with
[L1338] [51:49.20] something. But like as so as as long as
[L1339] [51:51.60] you have something going on yourself
[L1340] [51:53.76] that can kind of fill out your scope
[L1341] [51:56.96] then I like I just say no um a lot uh
[L1342] [52:02.56] and some people might also say too much.
[L1343] [52:05.12] Um, but that's kind of my way of staying
[L1344] [52:08.16] kind of staying a bit away from all that
[L1345] [52:10.16] because there is just there is a lot uh
[L1346] [52:12.56] of noise and I don't know
[L1347] [52:16.48] I just like to be blunt about it just
[L1348] [52:18.00] like plain stupidity in my view but like
[L1349] [52:21.12] I think some people probably call it
[L1350] [52:22.88] politics. I don't think I don't know.
[L1351] [52:24.80] Um, but I also have very low patience
[L1352] [52:26.72] for it uh for stuff like I think if
[L1353] [52:29.68] you're doing something let's talk about
[L1354] [52:31.04] it and do it. I don't want to talk about
[L1355] [52:32.88] we should do something and we talk about
[L1356] [52:34.72] that for hours or days or whatever and
[L1357] [52:37.36] then at the end of it we was like yeah
[L1358] [52:40.80] we could do it next year and like okay
[L1359] [52:42.32] that that was just a pure waste of time.
[L1360] [52:44.48] >> One thing that I hear some from some
[L1361] [52:46.32] friends is they want to avoid all that
[L1362] [52:48.32] stuff so they don't want to get promoted
[L1363] [52:51.12] because then the expectations get higher
[L1364] [52:53.52] of more of that other stuff. So I'm
[L1365] [52:56.24] curious, did is any part of you regret
[L1366] [52:58.32] getting promoted to such a high level
[L1367] [53:00.48] and having to deal with politics?
[L1368] [53:02.64] >> Well, there were okay there were times
[L1369] [53:04.16] when like this is like this just
[L1370] [53:08.40] if only. But I heard but again it really
[L1371] [53:12.32] also depends on how good you are at
[L1372] [53:15.44] resisting pressure
[L1373] [53:17.52] and just like being like being yourself
[L1374] [53:20.48] like resting in yourself. I know it's
[L1375] [53:23.52] like I don't know some kind of voodoo
[L1376] [53:24.88] stuff, but like how confident are you in
[L1377] [53:28.32] just yourself? And do you care how much
[L1378] [53:31.20] do you care about other people's
[L1379] [53:33.12] opinions? And if you care a lot, it's
[L1380] [53:35.92] it's hard. If you don't care too much,
[L1381] [53:40.80] uh it's it's okay. And I like and I I I
[L1382] [53:44.16] like because I had like the good thing
[L1383] [53:45.60] about by by the way, we were remote uh
[L1384] [53:48.88] office in Denmark, small office in
[L1385] [53:50.24] Denmark. And we worked a lot a lot with
[L1386] [53:53.36] the teams in in um in San Francisco.
[L1387] [53:57.04] And the good thing about that is that
[L1388] [53:59.36] our daytime was uninterrupted. So we
[L1389] [54:01.76] basically do whatever we wanted. The bad
[L1390] [54:04.16] thing is we didn't have meetings in the
[L1391] [54:05.68] evening. But it's like but you actually
[L1392] [54:07.68] had a day work like normal work. You
[L1393] [54:11.28] could just do whatever you want and then
[L1394] [54:13.12] you have meetings in the evening. And
[L1395] [54:15.12] that creates this nice like you you kind
[L1396] [54:18.16] of get fully sucked into it. you only
[L1397] [54:20.32] get kind of a couple of hours every day
[L1398] [54:21.92] get sucked into it which I think helps a
[L1399] [54:24.64] lot. Just having having the physical
[L1400] [54:26.32] distance and the time zone distance
[L1401] [54:28.48] actually helped a lot in that because
[L1402] [54:30.88] there was like a lot of other people
[L1403] [54:32.32] were like oh then you pass some BP on uh
[L1404] [54:35.60] in the hallway that oh could you please
[L1405] [54:37.28] come along and we just like talk about
[L1406] [54:38.96] something. Yeah. But we we couldn't do
[L1407] [54:41.12] that. Uh so I think that also helped a
[L1408] [54:43.92] lot.
[L1409] [54:44.56] >> We talked a little bit about influence
[L1410] [54:46.16] and just last question on this. I found
[L1411] [54:48.88] somewhere that you said the best outcome
[L1412] [54:51.52] is when the other person thinks the idea
[L1413] [54:53.60] is theirs. Can you elaborate on what you
[L1414] [54:56.32] mean by that?
[L1415] [54:58.32] >> Yeah. Um, and it's not it's not like it
[L1416] [55:02.00] doesn't happen very often, but I'm I'm
[L1417] [55:03.52] just always when it happens, I am is
[L1418] [55:05.84] those are the best days when I hear
[L1419] [55:08.40] somebody
[L1420] [55:10.48] talking to somebody else like when I
[L1421] [55:12.08] overhear a conversation maybe in the
[L1422] [55:13.60] office, somebody talking to somebody
[L1423] [55:15.44] else about an idea I had originally that
[L1424] [55:19.04] they didn't like.
[L1425] [55:21.04] Um, and then maybe a couple months later
[L1426] [55:23.60] or whatever, it's like they're saying it
[L1427] [55:25.60] and they're not saying that I said it.
[L1428] [55:27.28] they're saying it with conviction.
[L1429] [55:29.68] Um, and it can be it can just be small
[L1430] [55:31.84] stuff, but it can also be a bit lar some
[L1431] [55:34.00] some larger things like I don't like
[L1432] [55:36.64] let's let's just say like you have
[L1433] [55:38.64] resistance on like Odin where you need
[L1434] [55:40.64] to rebuild something because you already
[L1435] [55:42.08] had the tooling but now if you were
[L1436] [55:43.92] actually using you actually had the
[L1437] [55:45.12] benefits but you initially you were not
[L1438] [55:47.84] like able to kind of see through see see
[L1439] [55:50.16] through that and like go go kind of
[L1440] [55:52.80] beyond what you had yourself and see the
[L1441] [55:54.80] benefits of the other thing because you
[L1442] [55:56.48] were looking only at the cost. But after
[L1443] [55:58.80] a while you might have realized that
[L1444] [56:01.28] this actually a good thing. Um without
[L1445] [56:04.24] having been like forced into that you
[L1446] [56:06.24] just like a seed was planted uh and then
[L1447] [56:09.36] that kind of grew into something and
[L1448] [56:11.84] then suddenly that person is actually
[L1449] [56:15.20] aligned and you didn't do a lot. Maybe
[L1450] [56:17.84] you notched a couple of times or there
[L1451] [56:20.00] was like a team kind of not a conscious
[L1452] [56:22.16] team effort but like you get into an
[L1453] [56:24.00] environment and it kind of changes you a
[L1454] [56:26.40] little bit. Um, and like it's just a
[L1455] [56:29.04] couple I' I've seen it not many many
[L1456] [56:31.44] times, but I've seen it a couple times.
[L1457] [56:33.04] It's just like it's just the best
[L1458] [56:34.64] feeling. And it's not the best feeling
[L1459] [56:36.80] of like, oh, you were right kind of
[L1460] [56:38.24] thing. It's just um to some degree a
[L1461] [56:40.80] proud feeling of like those guys, they
[L1462] [56:44.80] learned they they're on the right track
[L1463] [56:46.40] now. And it was without force. Like
[L1464] [56:49.84] there was no force involved. It was not
[L1465] [56:51.84] just because you kind of forced it into
[L1466] [56:54.88] them. You we just need to do this. They
[L1467] [56:57.20] were like actually actually like oh yeah
[L1468] [56:59.28] this actually good idea that's truth.
[L1469] [57:01.60] >> I saw somewhere that you had some
[L1470] [57:04.16] unconventional advice for picking
[L1471] [57:05.92] mentees or just something that I hadn't
[L1472] [57:07.52] heard before where you pick mentees
[L1473] [57:11.28] specifically outside of your org and you
[L1474] [57:13.60] try to disperse them to increase your
[L1475] [57:15.68] influence. I'm curious to hear more
[L1476] [57:17.84] about how do you pick mentees?
[L1477] [57:20.64] >> Yeah. So men like Okay. So mentoring in
[L1478] [57:23.12] general is like it's a very like um
[L1479] [57:27.36] I don't know it sounds so nice and
[L1480] [57:30.16] appealing but it's also when you look at
[L1481] [57:32.48] like the whole thing about scaling
[L1482] [57:33.68] yourself it's like super inefficient
[L1483] [57:36.32] like because
[L1484] [57:38.48] you kind of paralyze it. You're like
[L1485] [57:40.72] you're you're one person you're talking
[L1486] [57:42.08] to one other person. Uh and there's only
[L1487] [57:44.96] so much time in you only have so much
[L1488] [57:46.88] time. Um, so like the it's just super
[L1489] [57:50.88] hard to get high value out of that. Uh,
[L1490] [57:53.28] so to me it was it was really always
[L1491] [57:56.64] mainly just about having a network
[L1492] [58:00.88] uh and having conversations that are
[L1493] [58:02.56] like two-way conversations. It's not
[L1494] [58:04.24] just me providing whatever. It's just
[L1495] [58:06.24] also them talking about something. And
[L1496] [58:08.48] that's where like if you go if you're
[L1497] [58:10.40] all mentoring inside your own like team
[L1498] [58:12.56] or or is like like who's who's actually
[L1499] [58:15.84] learning what now? uh and like the the
[L1500] [58:20.48] that close range mentoring I think you
[L1501] [58:23.04] can that is much easier to do at like
[L1502] [58:25.12] not at scale but you can kind of talk to
[L1503] [58:28.08] people in a group setting more easily
[L1504] [58:31.36] about like career advice or whatever you
[L1505] [58:34.56] can do a bit of like
[L1506] [58:36.96] informal like oh what about that and
[L1507] [58:39.20] what about but it doesn't have to be
[L1508] [58:40.48] like scheduled or structured in that
[L1509] [58:42.88] sense where if you go to people you
[L1510] [58:45.12] don't really know or they're further
[L1511] [58:46.40] away from you there's more work in it
[L1512] [58:48.32] and you also have to like there's also
[L1513] [58:49.84] more benefit for you because you could
[L1514] [58:51.68] learn something about what they're doing
[L1515] [58:53.28] you can give them more input on what
[L1516] [58:54.64] they could be doing or why they're doing
[L1517] [58:56.16] what and so like so that's I think it's
[L1518] [58:59.44] nice it's nice if you actually have to
[L1519] [59:01.44] like spend the time to to actually do it
[L1520] [59:03.20] so that you also get some kind of
[L1521] [59:04.80] benefits but also so that you can kind
[L1522] [59:06.88] of plant plant seeds elsewhere
[L1523] [59:11.20] um because I've also seen
[L1524] [59:14.64] a number of times actually that people
[L1525] [59:17.20] come in and say, "Oh, I just how do I
[L1526] [59:19.92] get promoted? I'm I'm I only get [ __ ]
[L1527] [59:22.40] projects and like whatever." Um, but
[L1528] [59:25.68] then you kind of once they start
[L1529] [59:27.12] thinking about, oh, maybe there's
[L1530] [59:28.80] another way of thinking about the whole
[L1531] [59:30.16] thing, another way of working that will
[L1532] [59:32.64] kind of rub off inside their teams. Uh
[L1533] [59:36.24] so you're kind of planting a small seed
[L1534] [59:37.84] there that again will take a while but
[L1535] [59:40.72] might actually do positive change not
[L1536] [59:42.88] only to the mentee but also the rest of
[L1537] [59:45.60] the team and eventually the rest of the
[L1538] [59:47.36] orc. Um so that's why like
[L1539] [59:51.28] I I I prefer to like have people who are
[L1540] [59:54.56] not super close.
[L1541] [59:55.76] >> Do you have advice for mentees on how to
[L1542] [59:59.04] signal their potential to mentors? So I
[L1543] [01:00:02.16] imagine at some point you had probably
[L1544] [01:00:04.64] more asks for people to you know be
[L1545] [01:00:07.20] mentored by you or spend time with you
[L1546] [01:00:09.44] than you had time for. Um but let's say
[L1547] [01:00:12.08] someone's you really promising and they
[L1548] [01:00:13.92] really want to mentor from some person.
[L1549] [01:00:16.96] What would be your advice? How can they
[L1550] [01:00:19.04] you know set that up in a very natural
[L1551] [01:00:20.64] way? But I would I would probably start
[L1552] [01:00:23.04] like not just by asking oh can you do
[L1553] [01:00:25.04] mentoring because also because mentoring
[L1554] [01:00:26.96] can be kind of a mental load kind well
[L1555] [01:00:29.36] not a mental load because that's
[L1556] [01:00:30.40] something else but like it could be kind
[L1557] [01:00:32.08] of it could be kind of it can feel like
[L1558] [01:00:34.80] a big thing and a responsibility that
[L1559] [01:00:37.04] you might not actually want. Um, so it
[L1560] [01:00:40.48] might more be like, "Oh, can you help
[L1561] [01:00:42.08] with can you do can you help with
[L1562] [01:00:43.52] something specific or can we just talk
[L1563] [01:00:45.20] about like
[L1564] [01:00:47.04] something a design or a product we're
[L1565] [01:00:49.20] building or whatever?" Like just have a
[L1566] [01:00:50.80] conversation and then you take it from
[L1567] [01:00:52.64] there. I think that's that's one thing
[L1568] [01:00:54.88] you can do. Um, if if it's about like
[L1569] [01:00:58.08] how do you actually approach in the
[L1570] [01:00:59.44] first place, of course, always like cold
[L1571] [01:01:02.80] call and it works most of the time. Um,
[L1572] [01:01:05.92] I I usually didn't have that many
[L1573] [01:01:07.52] people. um reach out but there were a
[L1574] [01:01:09.84] couple of times but but um
[L1575] [01:01:13.44] but then also like just show up ask
[L1576] [01:01:16.56] questions like if you I had a lot of
[L1577] [01:01:18.88] presentations like in different offices
[L1578] [01:01:23.12] um and I always like when people like
[L1579] [01:01:25.36] come up and talk and ask uh so if you
[L1580] [01:01:27.68] kind of ask good questions uh I don't
[L1581] [01:01:30.80] know what question good quick good
[L1582] [01:01:31.60] questions are but like if you ask if you
[L1583] [01:01:33.76] just come up and ask and signal like
[L1584] [01:01:36.08] that I think that's that is a good
[L1585] [01:01:37.44] signal of interest. Uh and then just
[L1586] [01:01:42.24] because I I think it's also on the on
[L1587] [01:01:46.00] the mentor to kind of say, well, okay,
[L1588] [01:01:49.68] what you what you come and say is is
[L1589] [01:01:53.36] really not what you should be saying.
[L1590] [01:01:55.44] And I I don't think that should
[L1591] [01:01:56.88] disqualify because that's the whole
[L1592] [01:01:58.96] point. They need mentor. They need
[L1593] [01:02:01.44] mentoring. They might not actually know
[L1594] [01:02:02.80] what to say. Um, so, so I I I don't
[L1595] [01:02:06.72] think that if you if you want to do
[L1596] [01:02:08.24] mentoring, don't don't disqualify just
[L1597] [01:02:10.56] because they don't didn't send the right
[L1598] [01:02:12.00] resume or whatever. Um,
[L1599] [01:02:14.96] but they do have to have some
[L1600] [01:02:16.00] willingness to learn. And I think you
[L1601] [01:02:18.16] get you can kind of gr you can kind of
[L1602] [01:02:20.16] gauge that from just a like a short
[L1603] [01:02:23.68] discussion of like what are they doing,
[L1604] [01:02:26.64] what are the outlooks, what they have to
[L1605] [01:02:28.24] be doing, what are they thinking and see
[L1606] [01:02:30.00] how they do, how do they react to your
[L1607] [01:02:31.52] thing. Um and that might take a while
[L1608] [01:02:34.48] take just a bit of time like 10 15
[L1609] [01:02:36.32] minutes. Um and that's I think the other
[L1610] [01:02:39.36] thing is like to me mentoring is much
[L1611] [01:02:42.08] better if it's just pretty informal.
[L1612] [01:02:44.88] Like I I have like Uber has had have
[L1613] [01:02:48.48] been through different like a number of
[L1614] [01:02:50.48] different like mentoring systems or
[L1615] [01:02:52.24] platforms or [snorts] projects or
[L1616] [01:02:53.84] programs or whatever. And I'm like I
[L1617] [01:02:56.64] don't want a plan uh and I don't want a
[L1618] [01:02:59.68] schedule. that don't want anything
[L1619] [01:03:01.12] because like it's all individual what
[L1620] [01:03:03.44] people want or need. Uh so so also don't
[L1621] [01:03:07.60] just don't make it more than has to be
[L1622] [01:03:11.28] and also don't don't be afraid to say
[L1623] [01:03:13.20] okay I don't think we like kind of we're
[L1624] [01:03:16.96] done like or like I don't think we're
[L1625] [01:03:19.04] getting going to like you're not going
[L1626] [01:03:20.40] to going to get more out of it I'm not
[L1627] [01:03:22.08] going to get more of it. So this like
[L1628] [01:03:23.60] yeah it was nice
[L1629] [01:03:25.12] >> coming to the end of your career story.
[L1630] [01:03:27.04] I know eventually you left Uber and I'm
[L1631] [01:03:29.68] curious what's the story behind you
[L1632] [01:03:31.20] leaving Uber.
[L1633] [01:03:32.72] >> It's not a nice story unfortunately. Uh
[L1634] [01:03:35.68] I like I don't think so it is because I
[L1635] [01:03:38.32] was actually pretty happy on Uber. Uh
[L1636] [01:03:40.72] and um surprisingly so uh because when I
[L1637] [01:03:44.88] joined Uber I was like this like a crazy
[L1638] [01:03:47.68] like a crazy high pace place. When I
[L1639] [01:03:50.96] joined in 14,
[L1640] [01:03:53.12] it was also a very hot place to be and
[L1641] [01:03:56.32] people were coming from Google, Netflix,
[L1642] [01:03:59.28] Amazon like it like Uber was kind of the
[L1643] [01:04:01.68] place people were going to. Uh and then
[L1644] [01:04:04.24] you get a bit of like imposter syndrome
[L1645] [01:04:05.84] because like I didn't come from like big
[L1646] [01:04:07.60] tech is going I came from small tech. Um
[L1647] [01:04:12.08] so so I like all these people kind of
[L1648] [01:04:14.24] are much better than me. So like what
[L1649] [01:04:17.28] can I do? Uh and like I was talking so I
[L1650] [01:04:19.92] better like
[L1651] [01:04:22.00] I kind of hit the ground running uh uh
[L1652] [01:04:24.56] and never stop and that that that's can
[L1653] [01:04:28.08] also that that you can only do that for
[L1654] [01:04:30.00] so long. I'm like okay like I saw when I
[L1655] [01:04:33.20] joined and again I didn't have a plan
[L1656] [01:04:34.88] but like I wouldn't be surprised if I'm
[L1657] [01:04:36.88] out of there after like three or four
[L1658] [01:04:38.16] years because it's like it's like a
[L1659] [01:04:39.68] pretty intense environment. Um but it
[L1660] [01:04:43.84] turns out it was yeah it was intense.
[L1661] [01:04:45.52] also turned out that all those people
[L1662] [01:04:46.96] who came from the other places
[L1663] [01:04:49.76] well I don't want to like they were not
[L1664] [01:04:52.64] that much better than me after all
[L1665] [01:04:55.33] [laughter] uh it turned out they were
[L1666] [01:04:57.12] they were also just human um
[L1667] [01:05:00.80] and maybe more importantly they change
[L1668] [01:05:04.00] jobs much more frequently which means
[L1669] [01:05:06.80] it's really hard to keep a long project
[L1670] [01:05:08.48] running uh and kind of get the long-term
[L1671] [01:05:11.04] benefit of that but but even with the
[L1672] [01:05:14.16] high pace environment and the
[L1673] [01:05:15.76] performance uh performance management
[L1674] [01:05:18.00] and the
[L1675] [01:05:20.32] promos and all that stuff that is like
[L1676] [01:05:22.72] not natural to a like a Danish work
[L1677] [01:05:25.20] environment. Uh it was also just a whole
[L1678] [01:05:27.68] lot of fun. Uh and we had an office
[L1679] [01:05:31.44] with a very outsized
[L1680] [01:05:33.92] um um uh influence.
[L1681] [01:05:38.40] Uh we had a lot of senior engineers
[L1682] [01:05:41.44] uh compared to like we were a small
[L1683] [01:05:42.96] office but like we had very senior
[L1684] [01:05:45.52] engineers more or less from the get-go
[L1685] [01:05:47.28] and we just kept on getting more because
[L1686] [01:05:49.84] and we grew most of them internally a
[L1687] [01:05:51.76] lot of people grew to high levels. Um so
[L1688] [01:05:55.68] like in our office we grew two distin
[L1689] [01:05:57.52] distinct Indians which is like out of at
[L1690] [01:06:00.00] that point like 70 people it's like out
[L1691] [01:06:03.60] of 4 and a half thousand years that's
[L1692] [01:06:06.48] that's pretty insane. Um, so it was a
[L1693] [01:06:11.68] lot of fun and and we had these very in
[L1694] [01:06:14.64] like these these projects that we're
[L1695] [01:06:16.32] working on were very like challenging
[L1696] [01:06:19.36] and satisfying to work on and it was all
[L1697] [01:06:21.12] the stuff that if you're just like in a
[L1698] [01:06:23.04] normal company somewhere you go to
[L1699] [01:06:24.88] conference or whatever or you read about
[L1700] [01:06:26.56] blog posts and you reading about these
[L1701] [01:06:28.24] people who get to like do these
[L1702] [01:06:29.60] optimizations automations like ah if
[L1703] [01:06:32.24] only if only we had that like if only we
[L1704] [01:06:35.28] could do that and but we had that um so
[L1705] [01:06:38.16] like a lot of good stuff. Unfortunately,
[L1706] [01:06:40.72] it just happened that management
[L1707] [01:06:42.96] changed. Um, and that just
[L1708] [01:06:47.36] created this
[L1709] [01:06:49.92] uh change in engineering culture that
[L1710] [01:06:53.84] just meant that more and more people did
[L1711] [01:06:56.08] not like it. Uh uh and my managers
[L1712] [01:07:01.12] decided to leave at some point. He was
[L1713] [01:07:03.28] like my local manager who was also the
[L1714] [01:07:05.68] site lead. He decided to leave. Then the
[L1715] [01:07:08.48] the first distinguishing engineer in our
[L1716] [01:07:10.56] office decided to leave at around the
[L1717] [01:07:12.08] same point. Other people started to
[L1718] [01:07:13.84] leave. A lot of people left in the US
[L1719] [01:07:16.00] also and that just meant that it got
[L1720] [01:07:19.68] less and less fun and there was more and
[L1721] [01:07:22.80] more top top down kind of management
[L1722] [01:07:26.00] going on because initially in the old
[L1723] [01:07:27.92] days it was very engineering
[L1724] [01:07:30.32] oriented especially in platform
[L1725] [01:07:31.60] engineering where where I was. Uh so
[L1726] [01:07:33.68] very much uh very much not necessarily
[L1727] [01:07:36.40] only driven by engineers but engineers
[L1728] [01:07:38.00] were kind of part of the process when
[L1729] [01:07:40.48] you're designing something you were you
[L1730] [01:07:42.64] were there uh you were not always like
[L1731] [01:07:46.48] it was not always the thing you wanted
[L1732] [01:07:48.32] to do that actually was decided to do
[L1733] [01:07:49.84] but at least you were there you
[L1734] [01:07:52.00] understood the reasoning you kind of
[L1735] [01:07:53.84] stand behind it no almost no matter what
[L1736] [01:07:55.84] but it turn it kind of went to a place
[L1737] [01:07:58.48] where it was just like oh now we now we
[L1738] [01:08:00.80] need to do this and you're like that
[L1739] [01:08:02.40] seems stupid. Um and like there was this
[L1740] [01:08:06.32] decision of going to cl to to cloud.
[L1741] [01:08:08.56] Google had on-prem uh was operating
[L1742] [01:08:10.88] onrem had benefits and had downsides. Uh
[L1743] [01:08:14.64] and there was a decision that we should
[L1744] [01:08:16.40] move to cloud. Uh and the decision was
[L1745] [01:08:18.80] based on price that it was going to be
[L1746] [01:08:21.60] cheaper to run on cloud and no engineer
[L1747] [01:08:25.52] believed that also turned out not to be
[L1748] [01:08:27.60] true. It only turned out to be true
[L1749] [01:08:29.84] because then we had to cut cost of
[L1750] [01:08:32.56] platform by almost 50%. Then
[L1751] [01:08:36.40] it was cheaper but we we could also have
[L1752] [01:08:39.44] done that on prim and have have it like
[L1753] [01:08:41.20] then we just have even cheaper but so
[L1754] [01:08:44.24] that whole like top down management uh
[L1755] [01:08:47.92] just led to a full-on drain of uh
[L1756] [01:08:51.60] especially senior engineers because they
[L1757] [01:08:54.08] nobody really want to be part of it any
[L1758] [01:08:55.76] longer.
[L1759] [01:08:57.44] Nobody wants to be left out any longer
[L1760] [01:08:59.20] to some degree also. Um so at some point
[L1761] [01:09:01.76] I was also like I could stay but staying
[L1762] [01:09:04.72] would basically mean
[L1763] [01:09:06.96] that I would have to like um work in an
[L1764] [01:09:11.12] environment where a lot of a lot I
[L1765] [01:09:14.08] wouldn't be able to kind of uh stand
[L1766] [01:09:16.88] behind the decisions that were made. And
[L1767] [01:09:19.68] as a as a senior engineer,
[L1768] [01:09:23.04] if you're not behind the decisions that
[L1769] [01:09:25.20] are made, it's really hard.
[L1770] [01:09:28.32] Uh then you can just choose
[L1771] [01:09:31.60] my one of my peers or one of the
[L1772] [01:09:35.44] managers managers actually said when I
[L1773] [01:09:37.52] was like, I'm I think I'm going to
[L1774] [01:09:38.72] leave. He was like, yeah, but don't why
[L1775] [01:09:40.56] not just stick around and you just do
[L1776] [01:09:41.92] your own thing and just take the money
[L1777] [01:09:45.04] more or less. I'm like, yeah, sure. the
[L1778] [01:09:47.04] money the money is pretty nice but I
[L1779] [01:09:49.28] just I don't think I can do it. I don't
[L1780] [01:09:51.04] think I can witness
[L1781] [01:09:53.52] what other people are going through and
[L1782] [01:09:54.96] just like do my own thing. I just don't
[L1783] [01:09:57.20] think I can do it. Uh so at that point I
[L1784] [01:09:59.44] was like I then I was like then I have
[L1785] [01:10:01.28] to leave because I have tried enough to
[L1786] [01:10:03.84] change uh how things are done no effect
[L1787] [01:10:07.20] and that just means in my view that Uber
[L1788] [01:10:10.00] does not have the need for interviewers
[L1789] [01:10:13.92] at that level. as simple as that. Um,
[L1790] [01:10:17.92] and then I was like, then didn't then
[L1791] [01:10:20.00] yeah, at that point I had to leave. Uh,
[L1792] [01:10:22.24] but so to me it's a pretty sad thing
[L1793] [01:10:25.12] because it's like a self-inflicted thing
[L1794] [01:10:28.80] that Uber did uh for no for no good
[L1795] [01:10:32.16] reason in my view, but it just lost so
[L1796] [01:10:34.96] many really really good people. Mostly
[L1797] [01:10:37.44] two data bricks by now by the way, but
[L1798] [01:10:39.04] whatever. [laughter]
[L1799] [01:10:40.48] There's like a parallel world going on
[L1800] [01:10:41.84] there.
[L1801] [01:10:42.96] what made you want to go to a startup
[L1802] [01:10:44.64] instead of maybe data bricks or like a
[L1803] [01:10:46.80] big company again?
[L1804] [01:10:48.08] >> Yeah, so I think there are two parts to
[L1805] [01:10:50.16] it. Uh so data bricks pretty pretty nice
[L1806] [01:10:53.76] because they had also a local office of
[L1807] [01:10:55.92] open the local office. A lot of people
[L1808] [01:10:58.32] moved there a lot of people are new but
[L1809] [01:11:00.56] also just to build this to to build more
[L1810] [01:11:02.88] infrastructure and more or less to build
[L1811] [01:11:05.52] the same thing we have built once in a
[L1812] [01:11:06.88] while and I like we already built it. It
[L1813] [01:11:10.24] wasn't that [ __ ] Uh, so like I don't
[L1814] [01:11:12.96] know if I want to do it again. Like
[L1815] [01:11:14.80] yeah, it was a lot of fun, but like I
[L1816] [01:11:17.12] don't know, maybe it's like like if I'm
[L1817] [01:11:19.92] if I'm moving somewhere, there should be
[L1818] [01:11:21.28] some kind of change. And it's nice to
[L1819] [01:11:23.04] have it like a an like a like what's
[L1820] [01:11:25.52] called a like a cultural change. It's
[L1821] [01:11:27.44] nice, but it would also just be nice to
[L1822] [01:11:29.20] like do something else. Uh, the other
[L1823] [01:11:32.88] thing is uh as as it's nice to be a
[L1824] [01:11:35.84] senior engineer, but it's also scary.
[L1825] [01:11:38.80] Scary when you change jobs.
[L1826] [01:11:41.36] uh because suddenly you get into an
[L1827] [01:11:44.56] environment where you don't know
[L1828] [01:11:45.92] anybody. They don't know you. You have
[L1829] [01:11:48.24] no reputation. Well, you have some
[L1830] [01:11:50.08] reputation from the outside but you have
[L1831] [01:11:51.92] no personal reputation. Uh and what I
[L1832] [01:11:56.56] have seen a lot of times is like people
[L1833] [01:11:58.16] come in super like senior years come in
[L1834] [01:12:00.80] they have like and they come in to fix
[L1835] [01:12:02.80] something usually they're like oh they
[L1836] [01:12:05.12] fix this thing over here they will come
[L1837] [01:12:07.04] in and they will fix it for us also. And
[L1838] [01:12:09.68] it's just never that simple. It's just
[L1839] [01:12:11.76] never that simple. There's almost no
[L1840] [01:12:15.60] chance that you can take whatever you
[L1841] [01:12:17.04] did over there and apply again with
[L1842] [01:12:18.64] success. Just it just doesn't happen. Uh
[L1843] [01:12:21.68] so and those people are just in for a
[L1844] [01:12:23.60] very rough ride because they will face
[L1845] [01:12:25.92] resistance from everybody. Not everybody
[L1846] [01:12:27.76] but they face a lot of resistance.
[L1847] [01:12:29.60] Everybody say yeah what told you
[L1848] [01:12:33.18] [laughter]
[L1849] [01:12:33.84] and will more or less cheer when they
[L1850] [01:12:35.92] when they fail. It's like I don't know
[L1851] [01:12:38.32] it's not super attractive to be a senior
[L1852] [01:12:40.64] engineer like that because like the
[L1853] [01:12:42.88] expectations when you when you come in
[L1854] [01:12:44.48] are so high. Um like some companies do
[L1855] [01:12:48.08] quite well because you kind of just they
[L1856] [01:12:50.32] say well we could like start slow and
[L1857] [01:12:52.32] you embed you into the team or whatever
[L1858] [01:12:54.08] not you're not from on day one kind of
[L1859] [01:12:56.56] but still there's just a lot of like
[L1860] [01:12:58.56] catching up to do and you have to like
[L1861] [01:13:00.00] prove yourself. Um, so it's not that
[L1862] [01:13:03.04] it's cannot be done and I'm not saying
[L1863] [01:13:04.40] that I I didn't want to do it at all,
[L1864] [01:13:05.92] but like I just didn't want to do this
[L1865] [01:13:08.08] like a natural move to another company
[L1866] [01:13:11.36] where to just do the same. I just like I
[L1867] [01:13:13.28] was like if you're doing something, we
[L1868] [01:13:14.48] might as well doing do something real
[L1869] [01:13:16.48] like drastic and the drastic thing is
[L1870] [01:13:19.04] just like the the complete opposite of 4
[L1871] [01:13:22.96] and a half thousand years is like
[L1872] [01:13:26.16] two million years or whatever it is. Um,
[L1873] [01:13:29.60] yeah. Yeah. So that that was basically
[L1874] [01:13:30.72] my my reasoning around it. It's just
[L1875] [01:13:32.56] like okay but like let's just and we can
[L1876] [01:13:35.28] because the other thing we can always do
[L1877] [01:13:36.56] the other thing always like can always
[L1878] [01:13:38.72] just go to data bricks or one of the
[L1879] [01:13:40.64] other places. I can even go back to Uber
[L1880] [01:13:43.12] if I wanted to. I don't want to but like
[L1881] [01:13:46.00] there's always there always the other
[L1882] [01:13:48.32] options. H so doing the startup thing is
[L1883] [01:13:51.60] like if you're doing it then yeah why
[L1884] [01:13:54.08] not why not just go all in on that. So
[L1885] [01:13:57.12] that was my kind of thinking around it.
[L1886] [01:13:59.52] Right. And since you've joined the
[L1887] [01:14:01.60] startup, how how has it been compared to
[L1888] [01:14:03.92] your expectations?
[L1889] [01:14:05.76] >> It has been very interesting. I would
[L1890] [01:14:07.92] say it has been a lot of fun. Like we do
[L1891] [01:14:12.08] we have like an AI enterprise automation
[L1892] [01:14:15.44] startup going. It's super interesting
[L1893] [01:14:18.00] and we we build so much stuff
[L1894] [01:14:21.84] um every day. Uh and we're kind of
[L1895] [01:14:24.88] navigating a space that nobody has ever
[L1896] [01:14:26.80] been in before. So it's like and so you
[L1897] [01:14:29.44] have to really be on on the edge always
[L1898] [01:14:32.80] which is like and I like it and I like
[L1899] [01:14:34.48] and I like also being and we're building
[L1900] [01:14:36.08] a product. We're not just building
[L1901] [01:14:37.60] infrastructure. I love building
[L1902] [01:14:39.36] infrastructure but it also gets you very
[L1903] [01:14:41.60] disconnected from like the reality. Uh
[L1904] [01:14:45.20] where here we're like building the
[L1905] [01:14:46.80] entire thing and I just like that a lot.
[L1906] [01:14:49.36] I don't like a lot the ah the
[L1907] [01:14:52.32] fundraising and oh we're about to run
[L1908] [01:14:54.24] out of money and then what and like that
[L1909] [01:14:56.08] whole thing. it can be a bit stressful.
[L1910] [01:14:58.16] Uh [laughter]
[L1911] [01:14:59.52] uh and yeah, so it's it's been good. Uh
[L1912] [01:15:04.88] uh it's been harder than I thought it
[L1913] [01:15:07.28] would be. Uh for for now, I would say
[L1914] [01:15:11.12] still still worth it. Uh not in not in
[L1915] [01:15:15.44] money. Yes, I hope it will eventually.
[L1916] [01:15:18.40] >> Coming to the end of the conversation, I
[L1917] [01:15:20.80] wanted to ask you some career
[L1918] [01:15:22.32] reflection. So, is there an engineering
[L1919] [01:15:25.60] mistake or the the biggest engineering
[L1920] [01:15:27.36] mistake that you saw happen at Uber that
[L1921] [01:15:30.88] was only obvious in hindsight?
[L1922] [01:15:33.60] >> I think it's hard because there were a
[L1923] [01:15:35.20] lot of choices that did not scale,
[L1924] [01:15:39.84] but at the point where they were made,
[L1925] [01:15:42.96] it was kind of the right choice. It's
[L1926] [01:15:45.68] just it got so painful later. Uh, does
[L1927] [01:15:49.04] that mean that you'd have done it
[L1928] [01:15:50.32] differently? I don't necessarily think
[L1929] [01:15:52.56] so. Um like for example I said like at
[L1930] [01:15:57.68] some point we were operating like 50
[L1931] [01:15:59.52] different databases or whatever. Was
[L1932] [01:16:02.08] that wrong as such? Well maybe that
[L1933] [01:16:04.32] maybe somehat that was wrong but but it
[L1934] [01:16:06.96] came out of the idea of like let
[L1935] [01:16:09.04] builders build like just like if you
[L1936] [01:16:11.12] need to do something go nuts. Let not
[L1937] [01:16:13.68] let nobody block you. Which once you're
[L1938] [01:16:17.68] 10 years into it is an insane strategy
[L1939] [01:16:21.28] that's going to like kill you. Uh but in
[L1940] [01:16:25.36] the early days like you don't want a lot
[L1941] [01:16:27.68] of structure. You just because you don't
[L1942] [01:16:29.60] know what you're doing. You don't know
[L1943] [01:16:30.88] if you're going to be successful. You
[L1944] [01:16:32.64] have no idea what's going to happen. So
[L1945] [01:16:34.24] they go nuts. Um I think the hard part
[L1946] [01:16:37.92] is like when do you like when do you
[L1947] [01:16:40.48] expand? When do you contract? like how
[L1948] [01:16:42.88] how do how do you kind of manage that in
[L1949] [01:16:44.96] a good way and that's super hard uh and
[L1950] [01:16:47.28] I think I think some of the things is
[L1951] [01:16:51.20] that I think Uber really should have and
[L1952] [01:16:53.52] I don't really I have not really
[L1953] [01:16:55.20] reflected much on how how we should have
[L1954] [01:16:57.44] done it but that's definitely something
[L1955] [01:16:59.04] where like we should have better at
[L1956] [01:17:01.44] doing those transition from like full
[L1957] [01:17:04.08] freedom to more structure
[L1958] [01:17:06.88] um like one of our prime examples is uh
[L1959] [01:17:10.40] at some point we start doing tracing uh
[L1960] [01:17:12.72] back when Jerger was uh was built uh for
[L1961] [01:17:15.44] for distributed tracing pretty nice and
[L1962] [01:17:18.88] everybody thought this is pretty nice uh
[L1963] [01:17:20.96] and then there was like a mandate to say
[L1964] [01:17:23.28] okay we need to we need to enable
[L1965] [01:17:24.96] tracing all on all all our service
[L1966] [01:17:26.48] because we have a microser we have like
[L1967] [01:17:27.76] a thousands of microservices nobody
[L1968] [01:17:29.12] knows what's going on let's do tracing
[L1969] [01:17:30.80] because that will give us a lot of
[L1970] [01:17:32.00] benefit and then there was an email
[L1971] [01:17:33.92] going out
[L1972] [01:17:35.92] and I don't remember the exact dates I'm
[L1973] [01:17:37.92] guessing the first email was in 15
[L1974] [01:17:39.76] saying oh okay we're doing tracing. All
[L1975] [01:17:42.40] teams must implement tracing.
[L1976] [01:17:45.20] And there probably was a deadline 3
[L1977] [01:17:47.52] months later. And then 3 months later,
[L1978] [01:17:49.60] it's like the same because it had not
[L1979] [01:17:51.84] happened surprisingly. And then it there
[L1980] [01:17:54.64] was just like maybe until maybe 17, 18,
[L1981] [01:17:57.60] they was like, "Okay, this now we're
[L1982] [01:17:59.36] doing it. Now we're doing it." And but
[L1983] [01:18:01.76] it never got done. And somehow the
[L1984] [01:18:03.76] emails just stopped coming, but it never
[L1985] [01:18:05.12] got done. Like for real.
[L1986] [01:18:09.12] So [snorts]
[L1987] [01:18:10.72] that's inability to kind of affect like
[L1988] [01:18:16.00] global change
[L1989] [01:18:18.24] just made so many projects so hard. Um
[L1990] [01:18:22.80] and it's really to a very large degree a
[L1991] [01:18:25.12] cultural problem. But I think it's not
[L1992] [01:18:27.20] just an engineering problem but it's an
[L1993] [01:18:29.12] engineering culture problem. And I think
[L1994] [01:18:30.80] that I think to me that is probably the
[L1995] [01:18:32.56] one of the biggest things that
[L1996] [01:18:36.16] that to some degree hurt the company
[L1997] [01:18:38.24] because there was there's a lot of waste
[L1998] [01:18:40.24] a lot of waste going on. um that was not
[L1999] [01:18:43.28] necessary later on was necessary in the
[L2000] [01:18:45.36] beginning but they don't not um so I
[L2001] [01:18:49.12] don't think I don't have like a concrete
[L2002] [01:18:50.64] like oh then we did this and then it was
[L2003] [01:18:52.40] kind of stupid and we should have done
[L2004] [01:18:53.68] that where where it was like super
[L2005] [01:18:55.92] obvious well okay I'll just mention one
[L2006] [01:18:58.88] thing and that is uh at some point and
[L2007] [01:19:03.76] maybe somebody's going to be super angry
[L2008] [01:19:05.52] about this I don't know but uh at some
[L2009] [01:19:08.08] point we tried to implement uh a a kind
[L2010] [01:19:12.56] of software networking stack. Um and the
[L2011] [01:19:16.40] the team building it was like, "Yeah, so
[L2012] [01:19:18.40] we're going to do this uh thing where
[L2013] [01:19:20.16] you like we're going to build a software
[L2014] [01:19:22.56] network uh uh where like if you are when
[L2015] [01:19:26.72] when when services need to communicate,
[L2016] [01:19:28.64] it goes into an ingress uh and then it
[L2017] [01:19:31.12] gets routed through a network and to a
[L2018] [01:19:32.56] to to to the right service." And that
[L2019] [01:19:34.48] whole thing we implement in node
[L2020] [01:19:38.40] and I like I just distinctly remember
[L2021] [01:19:41.84] there was like a platform tech talk or
[L2022] [01:19:44.08] about like this is like insane but it
[L2023] [01:19:48.24] was back in 16 or whatever and I was
[L2024] [01:19:49.84] like not that senior yet. So I okay but
[L2025] [01:19:52.56] those people are pretty senior they must
[L2026] [01:19:53.84] know what they're talking about. turned
[L2027] [01:19:56.24] out they did not know what they were
[L2028] [01:19:58.48] talking about and that that caused a lot
[L2029] [01:20:00.96] of pain [laughter]
[L2030] [01:20:02.64] and many years of untangling uh and
[L2031] [01:20:06.08] whatever. Um so I think that that was a
[L2032] [01:20:08.72] pretty bad decision.
[L2033] [01:20:11.44] Sorry to anybody who who don't think
[L2034] [01:20:13.12] there was but I think it was
[L2035] [01:20:15.52] >> about Uber's culture. Um earlier you
[L2036] [01:20:19.44] mentioned that especially with the promo
[L2037] [01:20:21.84] committees that there's a bit of a
[L2038] [01:20:24.00] unusual culture of you know everyone
[L2039] [01:20:27.12] needs to sell their managers just
[L2040] [01:20:29.60] present their reports and you just sell
[L2041] [01:20:31.36] it in a big group and you alluded to
[L2042] [01:20:33.84] that at that time there was also some
[L2043] [01:20:35.92] other cultural backlash and I vaguely
[L2044] [01:20:38.32] remember that too like around maybe it
[L2045] [01:20:40.32] was 2017 or something like that where
[L2046] [01:20:42.96] there was a lot of stuff going on at at
[L2047] [01:20:44.88] Uber. What was it like for you
[L2048] [01:20:47.68] experiencing that at the time?
[L2049] [01:20:49.68] >> There's a fairly big cultural difference
[L2050] [01:20:51.28] between Denmark and Silicon Valley. It's
[L2051] [01:20:55.28] very interesting like and in many ways
[L2052] [01:20:58.16] quite entertaining. Um
[L2053] [01:21:01.44] uh so like so it was a bit weird to
[L2054] [01:21:05.04] experience because like many of those
[L2055] [01:21:07.36] problems we just was we just were like
[L2056] [01:21:10.24] are these like is this how people
[L2057] [01:21:12.80] behave? I thought we were just like
[L2058] [01:21:14.64] coding and having fun. [laughter]
[L2059] [01:21:17.36] Like what are you doing over there? Like
[L2060] [01:21:19.60] you're apparently doing something very
[L2061] [01:21:20.96] different. Uh so it was like it was very
[L2062] [01:21:24.96] well first of all quite disconnected
[L2063] [01:21:26.64] because like we were not like we were
[L2064] [01:21:30.08] quite far from that whole thing. Um or
[L2065] [01:21:33.44] maybe it's just me. I was like maybe I
[L2066] [01:21:36.40] was just very naive. I don't know. Um
[L2067] [01:21:39.20] but first of all it was it was good to
[L2068] [01:21:40.56] be at a distance because we like there
[L2069] [01:21:42.32] was a lot of stuff going on. We could
[L2070] [01:21:44.08] just keep on like executing and doing
[L2071] [01:21:45.92] our thing. So in that sense it was nice
[L2072] [01:21:48.16] but it was also it was also insane like
[L2073] [01:21:50.16] so that much stuff that was happening
[L2074] [01:21:51.68] and people leaving getting fired, board
[L2075] [01:21:55.20] members getting kicked out, Travis
[L2076] [01:21:56.96] getting kicked out. A lot of stuff going
[L2077] [01:21:59.28] on was like every day you like what's
[L2078] [01:22:01.36] going to happen now?
[L2079] [01:22:03.60] Um but again daytime quiet here because
[L2080] [01:22:08.72] 9 9 hours time difference we can just do
[L2081] [01:22:11.28] our thing and then whatever happens
[L2082] [01:22:12.88] happens and there's not really anything
[L2083] [01:22:14.40] we can do about it. It's not like not
[L2084] [01:22:16.80] our fault. Uh there's some of it that of
[L2085] [01:22:19.28] course we also have to adapt to. Um but
[L2086] [01:22:23.36] there was very much like when I joined
[L2087] [01:22:25.92] there was very much like every
[L2088] [01:22:28.16] everything was very much about you like
[L2089] [01:22:30.80] performance reviews you promo you
[L2090] [01:22:33.60] conversation you like when you get hired
[L2091] [01:22:36.48] or and you negotiate your salary it's
[L2092] [01:22:38.32] just about how good you are at
[L2093] [01:22:39.60] negotiating. So it's all about you. It's
[L2094] [01:22:41.20] not about the team. The team doesn't
[L2095] [01:22:42.56] matter at all. It doesn't play into
[L2096] [01:22:43.92] anything more or less. uh which is
[L2097] [01:22:46.56] insane to me [laughter] like I don't get
[L2098] [01:22:50.32] it. So even though that was kind of how
[L2099] [01:22:52.80] how Uber works, we had never like gone
[L2100] [01:22:56.00] fully into that mindset. Uh so for for
[L2101] [01:22:59.84] us there wasn't that big of a of a
[L2102] [01:23:01.92] difference. Um it was more like okay now
[L2103] [01:23:04.56] like because I always thought like I
[L2104] [01:23:06.56] just thought that was how it was in the
[L2105] [01:23:08.08] US. Uh, so I was like, "Okay, so Oh,
[L2106] [01:23:10.88] it's not actually like you actually
[L2107] [01:23:13.20] wanted to be different." Like I thought
[L2108] [01:23:15.12] I thought you liked it like that,
[L2109] [01:23:17.05] [laughter] but but you don't I don't I
[L2110] [01:23:19.04] don't know why why you did it like that
[L2111] [01:23:20.40] then. But anyway, but it was very
[L2112] [01:23:22.96] interesting times and there was just a
[L2113] [01:23:24.48] lot of scandals also where we were like
[L2114] [01:23:27.60] why why did you do that? like why did
[L2115] [01:23:31.44] you decide to go to a strip bar or like
[L2116] [01:23:33.44] why did you decide to to kind of uh open
[L2117] [01:23:36.96] up somebody's private data and see where
[L2118] [01:23:39.12] they went? Like what what motivated you
[L2119] [01:23:41.20] to do that? I don't know. [laughter]
[L2120] [01:23:43.60] But like [snorts] what motivates a board
[L2121] [01:23:45.36] member to like on a live stream to the
[L2122] [01:23:48.08] entire company after a sec sexual
[L2123] [01:23:50.48] harassment scandal to say something
[L2124] [01:23:52.40] like, "Yeah, it's going to be nice to
[L2125] [01:23:54.16] get the women on the board because they
[L2126] [01:23:55.76] talk more." [laughter]
[L2127] [01:23:57.04] >> Oh, no. No. What's
[L2128] [01:23:59.44] >> that's so bad? Like what? Like what are
[L2129] [01:24:02.56] you thinking about? Like what is this
[L2130] [01:24:05.20] insanity? I have mixed feelings about
[L2131] [01:24:07.36] it. It was just I was just happy to be
[L2132] [01:24:09.12] at a distance and but sometimes you
[L2133] [01:24:11.04] could also just feel like okay bring out
[L2134] [01:24:12.96] the popcorn and like see what's
[L2135] [01:24:14.16] happening here because like it was just
[L2136] [01:24:16.24] it was very interesting times when I
[L2137] [01:24:18.32] went to the US to visit before 17. You
[L2138] [01:24:21.44] go to some of the offices people like
[L2139] [01:24:23.60] fist bump and then do you want a
[L2140] [01:24:25.84] whiskey? I don't know. It's like Tuesday
[L2141] [01:24:28.64] at 2:00 p.m. I don't know. Do I want
[L2142] [01:24:30.80] whiskey? I don't think so. Like I I
[L2143] [01:24:33.03] [laughter] don't know. Is that a thing?
[L2144] [01:24:35.92] >> If you look back on your career so far
[L2145] [01:24:38.64] and you knowing everything you know now,
[L2146] [01:24:41.04] if if you were to give yourself advice
[L2147] [01:24:43.12] when you just started in your career,
[L2148] [01:24:45.28] what would you say? Just try stuff and
[L2149] [01:24:48.64] don't don't be afraid just because it
[L2150] [01:24:51.12] looks hard or because those other people
[L2151] [01:24:52.72] look much better than you because they
[L2152] [01:24:55.68] might be better than you. Sure, but but
[L2153] [01:24:58.64] you can also get there. It's not it's
[L2154] [01:25:00.56] not it's not rocket science. Uh it it is
[L2155] [01:25:05.28] just computers. Uh and if if you like
[L2156] [01:25:07.52] computers, uh you're pretty well off uh
[L2157] [01:25:10.00] if you just keep going with that. Um, so
[L2158] [01:25:13.52] I think that's probably the main thing
[L2159] [01:25:15.28] in my view. It's like just let let the
[L2160] [01:25:18.56] let your curiosity take you where
[L2161] [01:25:20.48] wherever and don't just don't assume
[L2162] [01:25:23.84] that what you're doing right now is the
[L2163] [01:25:26.08] best thing you can be doing
[L2164] [01:25:28.64] because there's probably something
[L2165] [01:25:30.00] that's even better out there or or or
[L2166] [01:25:32.16] will will be soon. And then
[L2167] [01:25:35.28] don't don't just discard that just
[L2168] [01:25:37.28] because you're kind of having fun kind
[L2169] [01:25:39.68] of having fun now or whatever. Um, of
[L2170] [01:25:42.56] course it might be hard to like tell
[L2171] [01:25:44.80] which what what is better than what you
[L2172] [01:25:46.40] have now. Like you also just have to
[L2173] [01:25:48.32] take a chance sometime.
[L2174] [01:25:49.84] >> Awesome. Well, yeah, thanks so much for
[L2175] [01:25:52.48] your time. I really uh appreciated it
[L2176] [01:25:55.52] for the guests. I'll I'll link to your
[L2177] [01:25:58.08] socials in the show notes. Is there
[L2178] [01:26:00.32] anything else though you want to, you
[L2179] [01:26:02.08] know, point people to? Maybe something
[L2180] [01:26:03.76] you're working on or anything like that?
[L2181] [01:26:06.24] >> I think my LinkedIn profile is probably
[L2182] [01:26:08.00] the the most relevant place because like
[L2183] [01:26:10.16] that's where all the stuff I write. Uh,
[L2184] [01:26:11.92] it goes.
[L2185] [01:26:13.12] >> Okay, cool. Well, thanks so much. I
[L2186] [01:26:14.72] really appreciate it.
[L2187] [01:26:16.00] >> Awesome.
[L2188] [01:26:17.36] >> Thanks for listening to the podcast. I
[L2189] [01:26:19.92] don't sell anything or do sponsorships,
[L2190] [01:26:22.48] but if you want to help out with the
[L2191] [01:26:24.40] podcast, you can support by engaging
[L2192] [01:26:27.44] with the content on YouTube or on
[L2193] [01:26:29.84] Spotify. If you want to drop a review,
[L2194] [01:26:31.52] that'll be super helpful. And if there's
[L2195] [01:26:33.84] any guests that you want to bring on to,
[L2196] [01:26:35.84] please let me know. I feel like sourcing
[L2197] [01:26:38.16] very senior IC's, there's no wellstudied
[L2198] [01:26:42.00] list out there on Google that I can just
[L2199] [01:26:43.76] search this up. So, if there's someone
[L2200] [01:26:45.52] in your org or at your company who you
[L2201] [01:26:47.44] really look up to and you want to hear
[L2202] [01:26:48.80] their career story, let me know and I'll
[L2203] [01:26:51.36] reach out to
