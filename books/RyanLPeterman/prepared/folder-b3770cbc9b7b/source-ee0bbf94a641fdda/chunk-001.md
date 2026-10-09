Chunk 1; segments 1–337. 

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
