Chunk 1; segments 1–375. 

# AWS to Dropbox: The Largest Ever Data Migration In History | James Cowling

Source ID: source-1f8e66c58d2a4c8b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/AWS_to_Dropbox_The_Largest_Ever_Data_Migration_In_History_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=Ar84Ow4l2XE

[L10] [00:00.00] one of the big projects you worked on at
[L11] [00:01.88] Dropbox was my migrating away from S3.
[L12] [00:04.96] >> Yes. Yes.
[L13] [00:05.68] >> So, um you know, why why did Dropbox
[L14] [00:08.20] migrate away from S3?
[L15] [00:10.60] >> Yeah, that was a desire of the company
[L16] [00:11.96] for a long time. You know, from even
[L17] [00:13.72] before I was there. So, I started at
[L18] [00:15.20] Dropbox in 20 uh 2012.
[L19] [00:18.32] Um and I spoke to to Drew, the Dropbox
[L20] [00:20.64] founder, I think in 2010 about this
[L21] [00:22.64] project. And so, I think there was a
[L22] [00:24.28] desire to um control the destiny of the
[L23] [00:28.60] company from a strategic perspective. at
[L24] [00:30.44] the time, it was before Dropbox kind of
[L25] [00:32.92] reshaped itself as being more about
[L26] [00:34.32] collaboration, you know, but at the time
[L27] [00:36.00] it was a file sync and share category.
[L28] [00:37.76] That was that was the that was the that
[L29] [00:39.44] was the market sector, you know? And so,
[L30] [00:41.68] and owning the file system was really
[L31] [00:43.60] valuable to the company.
[L32] [00:45.28] Ultimately, we saved a huge amount of
[L33] [00:46.92] money. I mean, we we And this is before
[L34] [00:49.84] the public company went public. We
[L35] [00:51.60] really drove massive cost efficiencies
[L36] [00:54.48] through the project. Um but it was hard,
[L37] [00:56.80] you know, in a way that I think it'd be
[L38] [00:58.16] very difficult to to emulate without a
[L39] [01:00.32] huge investment.
[L40] [01:01.88] And I do think that there is um
[L41] [01:05.08] there is a benefit to an organization
[L42] [01:07.52] from having hard problems to solve.
[L43] [01:10.52] Because if you have a a company with
[L44] [01:12.32] extremely hard technical challenges, you
[L45] [01:14.80] can
[L46] [01:15.44] attract engineers who like working on
[L47] [01:17.40] those hard technical problems. And when
[L48] [01:19.00] they've solved those problems, they
[L49] [01:21.40] cycle off and work on different parts of
[L50] [01:23.28] the system. So, you know, after we all
[L51] [01:25.32] worked we had a such a great team. It
[L52] [01:27.16] was a very very small engineering team.
[L53] [01:29.00] And after we kind of shipped the the
[L54] [01:31.84] storage system reliably, we all went off
[L55] [01:33.68] and, you know, Jamie went and and
[L56] [01:36.36] redesigned the sync protocol, the
[L57] [01:38.00] desktop client, and I worked on the on
[L58] [01:40.16] the file system and the distributed
[L59] [01:41.64] databases. And so, yeah, there's there's
[L60] [01:43.56] value to a business to have um that
[L61] [01:46.12] level of technical investment, but it is
[L62] [01:48.28] a
[L63] [01:49.24] you know, it's like it's like having a
[L64] [01:50.64] baby and then you have to you've got to
[L65] [01:53.20] raise the baby. You can't just build a
[L66] [01:54.80] system like this and be that's it, we're
[L67] [01:56.44] done.
[L68] [01:57.84] You own it and you have to keep
[L69] [01:59.32] investing in it.
[L70] [02:01.64] >> Did um
[L71] [02:03.00] did S3 do any counter negotiation before
[L72] [02:05.92] you set out to leave them? Did they say
[L73] [02:07.40] like, "Oh, you know, we'll cut you a
[L74] [02:08.64] deal if you stay."
[L75] [02:09.69] >> [laughter]
[L76] [02:11.00] >> I guess I'm allowed to talk about this
[L77] [02:12.28] now. It was a long time ago. Um
[L78] [02:15.36] yeah, for the longest time there I don't
[L79] [02:16.60] think they were they were particularly
[L80] [02:17.80] aware that this was happening.
[L81] [02:19.68] Um but you know, the the data center
[L82] [02:21.48] folks talk and uh certainly it was
[L83] [02:25.24] noticed that Dropbox was buying up a lot
[L84] [02:27.00] of data center space. So, yeah, we had
[L85] [02:29.48] we had um obviously at at the scales
[L86] [02:32.76] that we were at, I mean, we were
[L87] [02:34.08] negotiating very good rates with Amazon.
[L88] [02:36.80] You know, we weren't paying sticker
[L89] [02:37.88] price, we're paying very very very good
[L90] [02:39.96] discounted rates. Um but yeah, at a
[L91] [02:42.28] certain point they weren't able to meet
[L92] [02:43.64] our cost efficiency because it it's when
[L93] [02:45.68] we launched the system, it really was
[L94] [02:48.24] more efficient than S3.
[L95] [02:50.16] And that's for a variety of reasons. One
[L96] [02:51.96] was that we were using kind of new
[L97] [02:53.60] experimental disks called shingled
[L98] [02:55.56] magnetic recording. We were the first
[L99] [02:57.40] ones I think to use these disks at
[L100] [02:58.84] scale.
[L101] [02:59.92] Um and two, we had a very tight
[L102] [03:01.92] understanding of our workloads. So, we
[L103] [03:03.24] were able to design the system
[L104] [03:04.72] specifically optimized for our
[L105] [03:06.48] workloads, whereas S3 has to design the
[L106] [03:08.84] system for everybody. So, you know,
[L107] [03:11.08] it's it got to the point where, you
[L108] [03:12.36] know, Amazon would not have been able to
[L109] [03:13.80] offer us a more competitive deal because
[L110] [03:16.08] we had a more efficient system.
[L111] [03:18.48] Um
[L112] [03:20.00] I wouldn't recommend another company do
[L113] [03:21.44] this right now.
[L114] [03:23.00] Uh but I think at the time it it
[L115] [03:24.48] certainly made sense for us as a
[L116] [03:25.68] company.
[L117] [03:27.20] >> Can you give an example of a tight
[L118] [03:29.96] understanding of your workloads leading
[L119] [03:31.80] to like something you could do that S3
[L120] [03:34.48] couldn't?
[L121] [03:35.08] >> Yeah, absolutely. So, for example, I
[L122] [03:36.88] know
[L123] [03:38.16] that um well, I'll try not to leak any
[L124] [03:40.36] confidential data, right? But when you
[L125] [03:42.84] when you upload a file to Dropbox, there
[L126] [03:44.96] is a pattern of access, right? Um so,
[L127] [03:48.00] typically people um access the file very
[L128] [03:50.76] quickly shortly afterwards um because
[L129] [03:53.64] you're sharing it with someone, or maybe
[L130] [03:55.72] your Dropbox is processing that file to
[L131] [03:58.12] generate an image preview, and then it
[L132] [03:59.92] decays at a certain rate. And so we
[L133] [04:02.08] understand in general the average block
[L134] [04:04.88] size, and we understand also the access
[L135] [04:08.40] pattern. So we could do things like at a
[L136] [04:10.84] certain point we had these two clusters.
[L137] [04:14.12] One was One was
[L138] [04:15.88] designed for kind of temporary storage.
[L139] [04:19.36] That was kind of storage inefficient,
[L140] [04:21.68] but access efficient. So it was very
[L141] [04:24.24] cheap to read and write to, but it was
[L142] [04:26.32] inefficient to store. And data would get
[L143] [04:28.28] written to there first, and then in the
[L144] [04:30.44] background it would get moved in bulk to
[L145] [04:33.80] this colder storage system.
[L146] [04:36.00] And this colder storage system was far
[L147] [04:37.48] more static.
[L148] [04:39.12] And so it was able to have kind of more
[L149] [04:40.68] efficient algorithms and and and be
[L150] [04:43.08] written to in bulk. And if it went down
[L151] [04:45.92] for rights, that was no problems because
[L152] [04:47.92] it wasn't in the live path. And so we're
[L153] [04:49.92] able to trade off again, like systems is
[L154] [04:51.52] all about trade-offs. So we're able to
[L155] [04:53.36] trade off the the live data write path
[L156] [04:55.64] from the long-term read path.
[L157] [04:57.88] That's one of many examples where
[L158] [05:00.28] knowing the size of your data, where
[L159] [05:02.08] it's accessed from, how frequently it
[L160] [05:03.76] gets accessed, how how long it takes to
[L161] [05:05.84] delete that data, you can really tune a
[L162] [05:08.44] system
[L163] [05:09.72] to your workload. If you know, stuff
[L164] [05:11.96] like looking at
[L165] [05:13.64] um
[L166] [05:14.88] even things down to knowing how much
[L167] [05:16.84] power to put in a rack. You know, you
[L168] [05:18.72] have a rack of hardware there's a power
[L169] [05:21.36] distribution unit, a PDU, at the top of
[L170] [05:23.00] that rack. It has a circuit breaker
[L171] [05:24.92] which can handle a certain number of
[L172] [05:26.36] amps.
[L173] [05:27.84] We would have to figure out, you know,
[L174] [05:29.88] how many amps are required for that rack
[L175] [05:32.24] based on access patterns. And there were
[L176] [05:34.00] times where we got it slightly wrong.
[L177] [05:35.64] There was times where
[L178] [05:37.16] we got to maybe a bad batch of hardware,
[L179] [05:39.48] and disks were failing too frequently.
[L180] [05:41.52] And as a result we were re-replicating
[L181] [05:42.96] the data
[L182] [05:44.16] more regularly, and I was getting you
[L183] [05:45.40] know, messages from the data center team
[L184] [05:46.84] saying, "Hey,
[L185] [05:48.08] we're running the racks really hot right
[L186] [05:49.56] now, you know?" [laughter] So, that's
[L187] [05:51.40] the level of optimizations you can make
[L188] [05:53.28] when you get to that scale. Um but
[L189] [05:55.84] again, that's multi-exabyte scale, you
[L190] [05:58.48] know,
[L191] [05:59.40] million hard drive scale.
[L192] [06:01.56] >> Yeah, when I was reading about this
[L193] [06:02.76] migration, I saw somewhere in the
[L194] [06:04.48] migration
[L195] [06:05.88] you initially started with Go, and then
[L196] [06:09.12] the racks or something that you're
[L197] [06:10.80] running on the hardware itself was
[L198] [06:12.68] ooming too much or
[L199] [06:14.08] >> Yeah.
[L200] [06:14.32] >> requesting too much memory, and then you
[L201] [06:16.68] migrated to Rust.
[L202] [06:18.44] >> So, initially, the prototype was in
[L203] [06:20.44] Python, if you can believe that.
[L204] [06:22.44] And to be fair, Python is actually
[L205] [06:23.88] pretty efficient for IO. I think people
[L206] [06:25.56] give Python a a bad rap for IO-bound
[L207] [06:28.48] workloads. It's pretty good at IO. Um
[L208] [06:31.36] but obviously, um not great for
[L209] [06:33.32] concurrency, not great for memory
[L210] [06:34.56] management, and um very hard to
[L211] [06:36.68] refactor.
[L212] [06:38.04] And it was critical the system was
[L213] [06:39.48] correct. And so, we migrated everything
[L214] [06:42.64] to Go, and we built most of the storage
[L215] [06:44.44] system in Go. This was before Go was in
[L216] [06:47.20] general availability. I think this is
[L217] [06:48.36] before Go was GA. Um
[L218] [06:50.72] and we built the system in Go. Go is a
[L219] [06:52.92] great language for concurrency, a great
[L220] [06:54.80] language for proxies. You know, it's a
[L221] [06:56.80] really well designed for like servers
[L222] [06:58.84] that moved out of one place to another
[L223] [07:00.52] place.
[L224] [07:01.52] At a certain point though,
[L225] [07:03.28] we would have, you know, let's just pick
[L226] [07:05.36] a number. Let's say a million. Let's say
[L227] [07:06.48] we have a million nodes in the system.
[L228] [07:08.80] And every node has um
[L229] [07:12.20] some amount of memory, some amount of
[L230] [07:13.96] disk, some amount of sheet metal in the
[L231] [07:16.24] chassis, right? And we would itemize all
[L232] [07:18.68] these things. You'd have a pie chart of
[L233] [07:21.00] of how much money is spent on all the
[L234] [07:23.12] things. And it would still have stuff
[L235] [07:24.56] like, yeah, sheet metal and screws and
[L236] [07:26.12] stuff. And so, you're trying to optimize
[L237] [07:28.60] the storage, and a big problem for us
[L238] [07:32.00] was the amount of memory um
[L239] [07:34.80] these nodes were using. Not just the
[L240] [07:36.52] memory they were using, but the
[L241] [07:37.88] unpredictability of it. Uh with, you
[L242] [07:40.72] know, with Go having a runtime and and
[L243] [07:44.12] you know, in a storage system an out of
[L244] [07:46.00] memory error is pretty bad.
[L245] [07:48.28] Because if a node runs out of memory and
[L246] [07:49.76] restarts, that looks like a disk
[L247] [07:51.44] failure.
[L248] [07:52.92] So that looks a lot like a disk has
[L249] [07:54.36] failed and has to be re-replicated. And
[L250] [07:56.00] so a batch of nodes OOMing
[L251] [07:59.44] can lead to cascading failures
[L252] [08:01.08] throughout the system.
[L253] [08:02.60] Because maybe
[L254] [08:04.28] um
[L255] [08:05.00] I remember a time it was a band, it
[L256] [08:07.20] might have been De La Soul. I can't
[L257] [08:08.40] remember there was a band released an
[L258] [08:09.92] album on Dropbox.
[L259] [08:11.76] So there was a big spike in load
[L260] [08:14.16] um to a to a
[L261] [08:16.12] a few files. So it was very, very high
[L262] [08:19.08] um bandwidth and it caused them the
[L263] [08:21.48] machines to OOM. So that those machines
[L264] [08:23.96] uh OOMed, those disks OOMed. Um and so
[L265] [08:26.72] as a result, no problems. The system
[L266] [08:28.68] went to try to recover that data from a
[L267] [08:30.76] whole bunch of other replicas, right?
[L268] [08:33.16] Now all of a sudden you've taken one
[L269] [08:35.40] amount one fire hose worth of load
[L270] [08:37.72] coming in and you've turned this into
[L271] [08:39.32] seven fire hoses worth of load coming
[L272] [08:41.04] cuz now you have to do a more expensive
[L273] [08:42.56] reconstruction operation, right? So now
[L274] [08:44.64] you've seven Xed the load. And these are
[L275] [08:46.48] the kind of um cyclical kind of
[L276] [08:48.96] behaviors that can lead to something
[L277] [08:50.12] called congestion collapse. Congestion
[L278] [08:51.76] collapse is when
[L279] [08:53.36] workload to a system crosses a threshold
[L280] [08:55.56] where it all kind of collapses.
[L281] [08:58.04] So can you design against congestion
[L282] [09:00.36] collapse is really the hardest part or
[L283] [09:02.48] one of the hardest parts of Magic
[L284] [09:03.64] Pocket, which is the name of the storage
[L285] [09:04.92] system.
[L286] [09:05.84] Um so ultimately we switched to Rust for
[L287] [09:10.00] the storage nodes themselves. And this
[L288] [09:12.24] again, this is before Rust was in GA, so
[L289] [09:14.68] that was a bit of a risky move. Uh
[L290] [09:16.88] but we rewrote um
[L291] [09:18.96] the switch to Rust coincided with
[L292] [09:20.92] getting rid of the file system entirely
[L293] [09:22.64] on the disks and directly addressing the
[L294] [09:25.36] the disk disk heads. So there was a
[L295] [09:27.60] there's an instruction set, I think it's
[L296] [09:28.80] called ZBC, zone based block control,
[L297] [09:31.88] something like that. There's there's a
[L298] [09:32.80] there's an instruction set for accessing
[L299] [09:34.40] disks that we were using.
[L300] [09:36.44] The disk manufacturers gave us the draft
[L301] [09:38.20] specs of these new disks and we were
[L302] [09:40.20] operating off the draft specs and
[L303] [09:42.16] directly controlling the the disks. And
[L304] [09:44.16] so,
[L305] [09:45.00] all that product was tied up um together
[L306] [09:47.88] um
[L307] [09:49.04] into a product called DiscoTech.
[L308] [09:50.96] It was the disk technology project. Um
[L309] [09:53.76] and ultimately, if you look at that pie
[L310] [09:55.56] chart, one congestion collapse stopped
[L311] [09:57.64] and reliability improved. But if you
[L312] [09:59.40] looked at the pie chart of where all the
[L313] [10:00.84] money was going, it really shifted to be
[L314] [10:03.28] almost all disks. And what we wanted to
[L315] [10:05.48] do is get that pie chart to be
[L316] [10:08.40] almost all the money spent on disks and
[L317] [10:10.80] as little money spent on RAM, on
[L318] [10:12.52] compute, on network, on power, on sheet
[L319] [10:14.88] metal, etc.
[L320] [10:16.20] >> The cascading failure you mentioned, was
[L321] [10:18.28] there So, that that happened and then
[L322] [10:20.72] there was a postmortem.
[L323] [10:21.92] >> I don't think we needed a postmortem. I
[L324] [10:23.28] think we we knew as it was happening.
[L325] [10:25.53] >> [laughter]
[L326] [10:26.52] >> I think when I was getting paged in the
[L327] [10:28.16] middle of the night on these things, I
[L328] [10:29.64] would you know you'd be pretty pretty
[L329] [10:31.20] evident. And so, look, this is the
[L330] [10:33.44] Again, this is an argument in favor of
[L331] [10:35.12] the cloud. All right. Imagine you've
[L332] [10:37.16] spent
[L333] [10:38.48] hundreds of millions of dollars on a on
[L334] [10:40.88] a storage system and it's out in
[L335] [10:42.24] production and it's on physical
[L336] [10:44.28] hardware.
[L337] [10:45.72] You can't just go and put new memory
[L338] [10:48.52] chips in every one of them. I mean, you
[L339] [10:50.00] can, but you have to pay people to come
[L340] [10:52.12] in and swap them out, you know? And so,
[L341] [10:54.56] that's a tricky place. And so, as a And
[L342] [10:57.32] this is what This is what I love about
[L343] [10:58.92] industry. You know, cuz in like some of
[L344] [11:01.84] the more um
[L345] [11:03.40] challenging moments on magic pocket were
[L346] [11:05.92] stuff like In one week,
[L347] [11:08.16] just a weird coincidence, two trucks
[L348] [11:10.48] crashed that were delivering servers.
[L349] [11:12.00] So, there's two trucks showing up to
[L350] [11:13.68] deliver racks and they both crashed. I
[L351] [11:15.60] don't know, you know, the drivers were
[L352] [11:16.72] okay. So, we lost capacity for 2 weeks.
[L353] [11:19.80] Uh so So, we lost capacity for for more
[L354] [11:22.16] than 2 weeks for for for probably 6
[L355] [11:24.00] weeks.
[L356] [11:25.28] Um
[L357] [11:26.44] How What do you do?
[L358] [11:28.16] What happens, you know, is is the
[L359] [11:29.68] equivalent of your disk filling up on
[L360] [11:31.00] your laptop, except it's you know, it's
[L361] [11:32.96] it's a million disks.
[L362] [11:34.88] And you can't tell the customers to go
[L363] [11:36.80] away. You can't delete their files. So,
[L364] [11:38.72] a lot of a lot of tricky
[L365] [11:41.56] a lot of tricky capacity work.
[L366] [11:44.12] And ultimately what that what that led
[L367] [11:45.80] to was trying to build in
[L368] [11:49.36] all these protections against the
[L369] [11:50.96] unknowns. You know, making sure we had
[L370] [11:53.80] the right amount of buffer planned out
[L371] [11:55.76] for anything bad that could happen.
[L372] [11:57.28] Making sure we we design the system so
[L373] [11:59.64] they couldn't be congestion collapsed so
[L374] [12:01.28] they wouldn't be memory spikes.
[L375] [12:03.44] Um and
[L376] [12:05.32] you know, at one point there's a there's
[L377] [12:06.72] a process called I think it's called
[L378] [12:07.88] FMEA,
[L379] [12:09.44] which is like a threat modeling process
[L380] [12:11.08] where you had a big spreadsheet and you
[L381] [12:12.68] kind of write down every bad thing that
[L382] [12:15.04] could possibly happen and then, you
[L383] [12:16.76] know, all the how bad it would be if it
[L384] [12:18.92] happened.
