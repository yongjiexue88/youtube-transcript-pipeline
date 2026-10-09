Chunk 2; segments 395–815. Start may repeat the previous chunk for context.

# Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov

Source ID: source-d23f1809e27bec76
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Data_Abstraction,_Dijkstra,_Distributed_Systems_Barbara_Liskov_en.txt
Video: https://www.youtube.com/watch?v=T9CGjbPZeaM

[L404] [14:17.60] >> I also noticed like um when you were
[L405] [14:20.60] uh when you came up with abstract data
[L406] [14:22.32] types
[L407] [14:24.16] maybe I mean maybe it's just cuz there
[L408] [14:25.72] wasn't the internet wasn't as, you know,
[L409] [14:28.68] wasn't there that there was also the
[L410] [14:30.72] object-oriented stuff going on on the
[L411] [14:32.96] West Coast.
[L412] [14:33.96] >> Yes, Alan Kay was developing Smalltalk
[L413] [14:37.28] at the same time that I was working on
[L414] [14:39.20] Clu, and then at Carnegie Mellon uh Bill
[L415] [14:43.00] Wulf and Mary Shaw were working on
[L416] [14:44.48] Alphard, which was another data
[L417] [14:46.04] abstraction language.
[L418] [14:48.80] And you're right, there was no there was
[L419] [14:50.36] no internet, although there was the
[L420] [14:51.68] ARPANET.
[L421] [14:53.20] You know, so we did but it was like
[L422] [14:55.76] there were two independent streams of
[L423] [14:57.64] research going on and we weren't talking
[L424] [14:59.56] to each other.
[L425] [15:01.00] And so, I wasn't paying much attention
[L426] [15:03.24] to Smalltalk and
[L427] [15:05.40] on the West Coast, I don't think they
[L428] [15:06.76] were paying much attention to data
[L429] [15:08.16] abstraction.
[L430] [15:10.00] And this led to the Liskov substitution
[L431] [15:13.20] principle
[L432] [15:14.76] which I mean, the story is a sort of a
[L433] [15:17.16] cute one because
[L434] [15:19.08] in 1986, I think it was, I was asked to
[L435] [15:22.80] give a keynote at OOPSLA.
[L436] [15:25.00] OOPSLA is the object-oriented
[L437] [15:26.68] programming conference, and this was the
[L438] [15:29.80] second year it was happening.
[L439] [15:32.24] And so, I decided I think I'll read all
[L440] [15:35.04] those papers about Smalltalk, and there
[L441] [15:37.08] were other languages being developed
[L442] [15:38.76] that were based on Smalltalk, and see
[L443] [15:40.36] what's going on with them. And I
[L444] [15:42.40] discovered
[L445] [15:44.08] Um so, Smalltalk has this idea of
[L446] [15:46.36] inheritance in it, where you can have a
[L447] [15:48.32] class and a subclass which borrows from
[L448] [15:51.04] the way the class is implemented and
[L449] [15:52.68] changes it a bit.
[L450] [15:54.68] And Clu doesn't have that. Clu just has
[L451] [15:57.20] what we call clusters, and they're all
[L452] [15:58.84] independent.
[L453] [16:00.64] So, I saw that they were talking about
[L454] [16:03.92] this notion of classes and subclasses.
[L455] [16:07.08] And
[L456] [16:08.36] and then I saw that they were also
[L457] [16:09.88] talking about something they called type
[L458] [16:11.56] hierarchy.
[L459] [16:13.28] Where they wanted the type implemented
[L460] [16:15.92] by a class
[L461] [16:17.80] to be related in some way that they
[L462] [16:20.16] didn't understand to the type that was
[L463] [16:22.00] implemented by a subclass.
[L464] [16:24.24] I really thought about modules in terms
[L465] [16:26.20] of their specifications.
[L466] [16:28.92] This partly had to do with a class I
[L467] [16:31.20] developed at MIT
[L468] [16:33.16] that I developed jointly with my
[L469] [16:34.44] colleague John Guttag.
[L470] [16:36.48] And in that class, we taught the
[L471] [16:38.16] students how to do design, about
[L472] [16:39.92] modularity, data types, and so forth,
[L473] [16:42.00] but also how to write specifications,
[L474] [16:44.56] how to reason about correctness.
[L475] [16:46.88] And so, it had a big focus on think
[L476] [16:50.40] about the meaning of things first, and
[L477] [16:53.20] the implementation is something that's
[L478] [16:54.64] kind of hidden inside, and you don't
[L479] [16:55.84] worry about it very much. And so,
[L480] [16:59.28] that was a different way of thinking
[L481] [17:00.60] about things than what was going on in
[L482] [17:02.36] the
[L483] [17:03.92] on the West Coast, where they were
[L484] [17:05.24] really thinking in terms of
[L485] [17:07.44] classes and subclasses. And I even saw
[L486] [17:09.72] papers where they would describe the
[L487] [17:12.28] behavior of a class by explaining how
[L488] [17:14.32] its implementation was different from
[L489] [17:16.12] the implementation of the superclass.
[L490] [17:18.32] So, they were kind of focused on
[L491] [17:19.84] implementations in a way that we
[L492] [17:21.40] weren't. And so,
[L493] [17:24.76] when I read these papers about type
[L494] [17:27.00] hierarchy and I saw they just couldn't
[L495] [17:29.28] figure out what it was supposed to mean,
[L496] [17:32.12] I was thinking about it from the terms
[L497] [17:33.92] of meaning. And so, I was able to say it
[L498] [17:36.84] has to do with the behavior.
[L499] [17:39.16] And this subclass better behave like the
[L500] [17:41.56] superclass if you use it in an
[L501] [17:43.68] environment where the superclass is
[L502] [17:45.56] expected.
[L503] [17:47.56] And that became what ended up being
[L504] [17:49.88] called the Liskov substitution
[L505] [17:51.40] principle.
[L506] [17:52.60] And ultimately, Jeannette Wing and I
[L507] [17:54.28] wrote a paper on behavioral subtyping,
[L508] [17:56.52] which is the formal definition.
[L509] [17:58.84] >> And then, how did it get that name? Cuz
[L510] [18:00.64] you didn't go off on stage and say, "Hey
[L511] [18:02.56] everyone, here's the Liskov substitution
[L512] [18:03.96] principle."
[L513] [18:06.32] >> one day in the
[L514] [18:07.80] in the '90s, after the internet had
[L515] [18:10.00] arrived, I got an email saying, "Can you
[L516] [18:12.80] say if this is the correct
[L517] [18:14.20] interpretation of the Liskov
[L518] [18:15.52] substitution principle?" That's when I
[L519] [18:17.76] discovered
[L520] [18:19.20] that
[L521] [18:19.76] >> [laughter]
[L522] [18:20.44] >> there was such a name.
[L523] [18:22.40] And And I
[L524] [18:24.64] I don't think I had really been aware of
[L525] [18:26.32] how important it was until that point,
[L526] [18:28.48] because I wasn't thinking about this
[L527] [18:29.92] stuff. I was working on other stuff.
[L528] [18:32.20] >> In the academic community, it seems very
[L529] [18:35.04] reasonable to have multiple people have
[L530] [18:37.76] similar ideas. But it seems like some
[L531] [18:40.56] ideas stick
[L532] [18:43.04] more than others. For instance, like the
[L533] [18:46.04] Viewstamped Replication versus Paxos.
[L534] [18:48.92] They're the same thing. I'm wondering,
[L535] [18:51.84] like, in that case for instance, why
[L536] [18:53.68] would Paxos be more known than
[L537] [18:56.76] Viewstamped Replication?
[L538] [18:57.84] >> Yeah. So, what Leslie says is,
[L539] [19:00.80] "I went around giving all the talks, and
[L540] [19:03.20] she implemented it."
[L541] [19:05.61] >> [laughter]
[L542] [19:07.88] >> Really?
[L543] [19:09.76] >> Something up to that.
[L544] [19:11.56] >> Then he
[L545] [19:13.20] got notoriety for speaking about it.
[L546] [19:16.36] >> Yeah, he he he did give lots of talks
[L547] [19:18.44] about it and wrote several papers and so
[L548] [19:20.60] forth and I didn't realize it was the
[L549] [19:23.36] same system. But finally it became clear
[L550] [19:26.24] that they were the same system.
[L551] [19:28.28] >> I also wonder how much the name matters
[L552] [19:31.20] because Paxos is kind of catchy, you
[L553] [19:33.44] know.
[L554] [19:33.52] >> It is a cute name.
[L555] [19:34.48] >> It's a cute name, yeah.
[L556] [19:35.40] >> Yeah, right.
[L557] [19:36.28] >> So, I I could see maybe it has better
[L558] [19:38.60] marketing around the idea, I guess.
[L559] [19:41.48] >> I also think that
[L560] [19:43.64] this approach to solving this problem,
[L561] [19:45.96] which both Leslie and I picked up
[L562] [19:47.44] independently, in my case came from the
[L563] [19:49.84] work I'd been doing with transactions.
[L564] [19:52.44] Because in transactions there's a leader
[L565] [19:55.60] that
[L566] [19:56.64] you know, says now we're going to commit
[L567] [19:58.40] and ask everybody can we commit and if
[L568] [20:00.44] they all say okay, you know, it's
[L569] [20:02.76] but unlike in transactions
[L570] [20:06.00] of in transactions if the leader fails,
[L571] [20:08.28] there's what's called, you know, the
[L572] [20:10.16] this can be a real problem. Here we had
[L573] [20:12.40] to have a way of moving to a new leader
[L574] [20:15.16] if the old leader failed and that's the
[L575] [20:17.28] big step forward that happened in both
[L576] [20:19.88] Viewstamped Replication and and Paxos.
[L577] [20:22.92] Now, there was also Byzantine fault
[L578] [20:25.52] tolerance, which came along later that
[L579] [20:28.72] was developed. So,
[L580] [20:30.28] Viewstamped Replication I developed with
[L581] [20:32.08] my student Brian Oki. It was his PhD
[L582] [20:34.84] thesis.
[L583] [20:36.24] And then Paxos I developed with my
[L584] [20:38.24] student Miguel Castro. It was his PhD
[L585] [20:41.20] student thesis.
[L586] [20:43.20] And
[L587] [20:44.40] Miguel got interested in this problem
[L588] [20:46.40] because
[L589] [20:47.80] uh there was a DARPA request for
[L590] [20:50.04] proposals
[L591] [20:51.68] and there was one about this problem on
[L592] [20:53.96] the internet. By then there were
[L593] [20:55.44] Byzantine attacks and you know,
[L594] [20:57.08] malicious attacks and
[L595] [20:59.40] nodes that would
[L596] [21:01.00] purport to be working correctly, but
[L597] [21:02.80] actually they had been compromised and
[L598] [21:04.76] so forth and so
[L599] [21:06.88] Viewstamped application in Paxos only
[L600] [21:09.04] handled crashes and um
[L601] [21:13.00] if there were messages that were had
[L602] [21:15.20] been played with, you could tell when
[L603] [21:16.88] they arrived that they were bad. And
[L604] [21:18.24] that was about the extent of what we
[L605] [21:19.76] dealt with.
[L606] [21:21.12] But these malicious attacks with nodes
[L607] [21:23.24] that purported to be working when they
[L608] [21:25.52] weren't, that was a big step forward.
[L609] [21:28.68] And Miguel saw this request for
[L610] [21:30.68] proposals and he said to me, "Why don't
[L611] [21:33.00] we see whether we can come up with a
[L612] [21:34.52] protocol that works in the presence of
[L613] [21:36.92] Byzantine attacks?" And
[L614] [21:39.64] and I think by the way, Leslie is the
[L615] [21:41.24] one that invented the word Byzantine to
[L616] [21:43.36] >> I think he did.
[L617] [21:43.96] >> Yeah, right.
[L618] [21:44.92] >> I saw in the in the software crisis
[L619] [21:46.68] stuff. There's the paper with Dijkstra
[L620] [21:48.68] that you had mentioned was one of the
[L621] [21:51.88] papers you you wrote that said, "We need
[L622] [21:54.60] modularity." And that paper was the
[L623] [21:57.12] go-to statements considered harmful.
[L624] [21:59.32] >> Right.
[L625] [22:00.16] >> And I'm curious cuz Dijkstra, I mean,
[L626] [22:02.88] when I was studying computer science,
[L627] [22:04.24] you we all know his name. Did you ever
[L628] [22:07.16] meet him or work with him?
[L629] [22:08.52] >> Oh, yeah, many ti- I did never worked
[L630] [22:10.04] with him, but I did meet him multiple
[L631] [22:12.20] times. And uh you know, he had very
[L632] [22:15.08] interesting ideas. And that
[L633] [22:18.24] paper, uh go-to statement considered
[L634] [22:20.84] harmful, it's not actually a paper. It
[L635] [22:23.56] was a letter to the editor of the
[L636] [22:25.12] Communications of the ACM.
[L637] [22:27.72] But it was very impactful. And
[L638] [22:31.04] what was really important about that
[L639] [22:32.88] paper was that Dijkstra was talking
[L640] [22:35.52] about
[L641] [22:37.20] how difficult it is to reason about the
[L642] [22:39.96] correctness of code.
[L643] [22:42.04] And this was at a time when
[L644] [22:44.92] in the sciences,
[L645] [22:47.20] computer science was kind of dismissed
[L646] [22:49.20] as nothing much.
[L647] [22:51.00] And anybody can write code.
[L648] [22:53.76] And you know, Dijkstra was trying to
[L649] [22:55.68] make a point, which I think was actually
[L650] [22:58.08] important, that it it's not as trivial
[L651] [23:00.76] as you think it is. It's not trivial at
[L652] [23:03.12] all.
[L653] [23:04.32] Um and he was also pointing out that
[L654] [23:06.20] go-tos can be misused.
[L655] [23:08.52] >> And it was controversial at the time.
[L656] [23:11.28] >> It was, yeah.
[L657] [23:12.12] >> But today I I I don't I mean I've
[L658] [23:15.20] written code for yeah, over a decade.
[L659] [23:17.68] >> People don't use go-tos.
[L660] [23:18.52] >> have I have I haven't even seen a go-to
[L661] [23:20.20] in the code.
[L662] [23:21.56] So, what why was it controversial at the
[L663] [23:23.72] time?
[L664] [23:24.76] >> The programming languages were different
[L665] [23:26.36] then.
[L666] [23:27.52] Um first of all, there were people
[L667] [23:29.12] writing programs in assembler.
[L668] [23:31.88] In assembler, you have to use go-tos.
[L669] [23:34.40] Programming languages didn't have
[L670] [23:36.76] some of the constructs in them that we
[L671] [23:38.36] think of today.
[L672] [23:40.20] And uh so some people were using go-tos
[L673] [23:43.40] cuz they had to.
[L674] [23:45.00] And also
[L675] [23:47.24] um compilers didn't do all the kinds of
[L676] [23:49.72] optimizations that they do today. So,
[L677] [23:51.96] there was a concern if you didn't have
[L678] [23:53.60] go-tos, maybe your program wouldn't be
[L679] [23:55.28] efficient enough.
[L680] [23:57.12] And then
[L681] [23:58.72] uh there were people who used go-tos and
[L682] [24:00.64] wrote really good code, and they weren't
[L683] [24:02.40] offended that Dijkstra was saying your
[L684] [24:04.92] code is bad.
[L685] [24:06.64] So, there was a whole but and and
[L686] [24:08.32] Dijkstra was not the most um diplomatic
[L687] [24:11.12] person. So,
[L688] [24:12.81] >> [laughter]
[L689] [24:13.84] >> you know, so he he didn't write it in
[L690] [24:15.72] the you know, nice
[L691] [24:17.32] not you can imagine writing that paper
[L692] [24:18.96] more nicely where you said um
[L693] [24:22.16] So, it that but there were many reasons
[L694] [24:24.72] why it was controversial. You know,
[L695] [24:26.08] people were offended, but then there
[L696] [24:27.96] were also concerns about
[L697] [24:31.16] like programming languages don't have
[L698] [24:32.60] these features I need, what am I
[L699] [24:33.96] supposed to do?
[L700] [24:35.56] And then there were concerns about what
[L701] [24:37.80] the compiler was doing. And so, the
[L702] [24:39.76] world is very different now. But
[L703] [24:41.56] clearly, Dijkstra won the day.
[L704] [24:43.56] >> Yeah, he did.
[L705] [24:44.12] >> Because
[L706] [24:45.20] no go-tos.
[L707] [24:46.87] >> [laughter]
[L708] [24:49.00] >> And is Dijkstra in person
[L709] [24:52.00] also like his writing?
[L710] [24:55.40] >> Uh he was not always as tactful as he
[L711] [24:57.56] might be.
[L712] [24:58.66] >> [laughter]
[L713] [25:00.00] >> Yeah, but you know, he was a a very uh,
[L714] [25:02.56] distinguished researcher.
[L715] [25:04.28] >> Computer science has had such a huge
[L716] [25:06.92] impact on the industry.
[L717] [25:09.24] Why did you choose to stay in academia
[L718] [25:11.56] instead of going into industry?
[L719] [25:14.00] >> So,
[L720] [25:15.60] I like doing research.
[L721] [25:18.52] And I enjoy working with students.
[L722] [25:21.40] And
[L723] [25:23.16] I teaching was never my favorite thing,
[L724] [25:26.04] but I always felt teaching and research
[L725] [25:28.16] were very closely connected.
[L726] [25:30.60] Um, but also it was a different time.
[L727] [25:33.40] So,
[L728] [25:35.60] this business about how professors are
[L729] [25:38.36] all forming companies and so forth,
[L730] [25:40.80] which goes on today, that wasn't
[L731] [25:42.24] happening 20 years ago.
[L732] [25:44.92] Or maybe it was happening 20 years ago,
[L733] [25:47.52] but 30 years ago it wasn't. So, when I
[L734] [25:49.52] was young, it wasn't the thing that you
[L735] [25:51.68] did. It was sort of a
[L736] [25:53.92] either or sort of thing. So, I wasn't
[L737] [25:56.52] even thinking about doing stuff like
[L738] [25:58.24] that.
[L739] [25:59.32] I did work in a startup briefly at the
[L740] [26:01.60] end of the '90s. I didn't like it.
[L741] [26:05.52] I much prefer doing research and as a
[L742] [26:08.60] professor you have this it's it's a gift
[L743] [26:11.56] and a curse.
[L744] [26:13.04] The gift is you can do whatever you
[L745] [26:15.04] want. The curse is you have to figure
[L746] [26:17.12] out what it is that you're doing.
[L747] [26:19.36] But I like that freedom. And the fact
[L748] [26:22.68] that I just could go off in any I mean,
[L749] [26:25.36] my career is full of these interesting
[L750] [26:27.72] zigzags where I would switch to
[L751] [26:29.52] something else. I had the freedom to do
[L752] [26:31.28] that.
[L753] [26:32.28] >> What stops you from going off in a very
[L754] [26:34.72] useless direction?
[L755] [26:36.32] >> Uh, you won't get tenure.
[L756] [26:38.87] >> [laughter]
[L757] [26:40.32] >> Who's the judge?
[L758] [26:41.84] >> The community.
[L759] [26:43.92] Yeah, it's not you know, what what the
[L760] [26:46.52] way that you're viewed at your
[L761] [26:47.96] university
[L762] [26:49.56] has mostly to do with um,
[L763] [26:52.76] one a very important facet of it is how
[L764] [26:55.44] are you viewed in your research
[L765] [26:56.76] community.
[L766] [26:58.92] So,
[L767] [27:00.00] because that's one of the important
[L768] [27:02.40] things they want
[L769] [27:04.40] from their faculty if you're in a
[L770] [27:06.04] research university.
[L771] [27:07.84] >> You mentioned earlier that
[L772] [27:09.68] research and teaching were heavily
[L773] [27:12.20] related in your opinion.
[L774] [27:13.96] Why is that?
[L775] [27:15.04] >> Because when you teach, you have to
[L776] [27:18.04] teach from first principles.
[L777] [27:20.72] And if you're doing good research, you
[L778] [27:22.60] need to understand deeply
[L779] [27:25.12] what's working, what's not working, what
[L780] [27:26.96] assumptions you're making. It's It's
[L781] [27:29.20] really the same thought process.
[L782] [27:31.88] >> It's It sounds like in research
[L783] [27:34.00] I mean, and this is true in every walk
[L784] [27:36.84] of life. There's the I guess the
[L785] [27:38.64] direction that you take
[L786] [27:40.60] and then the work that you do towards
[L787] [27:42.16] that direction. And it sounds like for
[L788] [27:44.20] research the
[L789] [27:45.80] the direction is
[L790] [27:48.36] maybe the most important thing cuz you
[L791] [27:51.08] could have a phenomenal researcher
[L792] [27:54.92] doing an idea that
[L793] [27:56.64] has no you know, even if you did it at
[L794] [27:58.92] 100% it's not going to lead to anything.
[L795] [28:01.52] >> So, you you know, I you tell students
[L796] [28:04.04] graduate students don't do incremental
[L797] [28:05.92] work.
[L798] [28:07.32] Don't you know, you've got you you can't
[L799] [28:09.08] just keep working on the same thing over
[L800] [28:10.76] and over just making little teeny
[L801] [28:12.48] improvements. You need to find You're
[L802] [28:14.44] right, you have to find a good problem,
[L803] [28:16.36] but you also have to find a problem
[L804] [28:18.64] that's amenable to a solution and one
[L805] [28:21.92] that matches your skill set.
[L806] [28:24.80] And
[L807] [28:26.00] you have to recognize when you're going
[L808] [28:28.80] in a good direction versus not going in
[L809] [28:30.68] a good direction.
[L810] [28:32.40] >> Looking back on your career, you say
[L811] [28:34.68] that it was luck and that it seems like
[L812] [28:39.08] things just
[L813] [28:40.80] fit together.
[L814] [28:42.08] >> I feel there was luck involved.
[L815] [28:45.28] There was a lot of hard work involved.
[L816] [28:48.68] There was
[L817] [28:50.60] um not allowing
[L818] [28:54.28] uh something negative to
[L819] [28:57.04] you know, cause you great difficulty.
[L820] [29:00.60] So, for example, when I
[L821] [29:03.88] finished my PhD, I would have liked a
[L822] [29:05.80] faculty position.
[L823] [29:08.04] But, I didn't have any good offers.
[L824] [29:10.88] So, I went back to Mitre, the company I
