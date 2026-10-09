Chunk 2; segments 350–697. Start may repeat the previous chunk for context.

# Turing Award Winner: Thinking Clearly, Paxos vs Raft, Working With Dijkstra | Leslie Lamport

Source ID: source-4005a50ded85af4c
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Thinking_Clearly,_Paxos_vs_Raft,_Working_With_Dijkstra_Leslie_Lamport_en.txt
Video: https://www.youtube.com/watch?v=U719vQz-WFs

[L359] [16:47.44] but the communication could not travel
[L360] [16:49.76] faster than the speed of light because
[L361] [16:51.44] nothing can travel faster than the speed
[L362] [16:52.96] of light. Well, I realized there was an
[L363] [16:55.84] obvious analogy.
[L364] [16:58.56] Uh the notion of happens before is
[L365] [17:02.32] exactly the same as in relativity except
[L366] [17:06.00] instead of being whether something one
[L367] [17:09.28] event can influence another by things
[L368] [17:12.96] traveling at the speed of light, it's
[L369] [17:15.36] whether the first event could have
[L370] [17:18.00] affected the other by information sent
[L371] [17:21.12] over messages that were actually sent in
[L372] [17:23.68] the system. The thing that you know blew
[L373] [17:27.20] people away was this this definition of
[L374] [17:29.92] of happens before in a distributed
[L375] [17:32.08] system with also this was the first
[L376] [17:35.12] paper I would call like you know had a
[L377] [17:38.40] scientific result about distributed
[L378] [17:41.12] systems. I made perhaps you know mistake
[L379] [17:45.12] that I was warned against at some point
[L380] [17:47.28] of having two ideas in in one paper. The
[L381] [17:52.00] other thing that I realized was that
[L382] [17:55.52] there was an an algorithm that would
[L383] [17:57.60] show whether one event that it would
[L384] [18:00.72] produce an ordering that satisfied this
[L385] [18:04.32] that condition that if some if one event
[L386] [18:06.88] happened the other before the other then
[L387] [18:08.96] that first event would be ordered before
[L388] [18:10.80] the other. And I realized that if you
[L389] [18:14.08] had an algorithm to do that, you could
[L390] [18:17.20] use it to basically provide the the
[L391] [18:21.04] synchronization you needed for any
[L392] [18:22.80] distributed system
[L393] [18:25.04] because you could describe that system
[L394] [18:27.04] in terms of a state machine. And a state
[L395] [18:30.80] machine as as I described it then is
[L396] [18:32.80] something that has a state and process
[L397] [18:36.80] executes you know uh commands that need
[L398] [18:40.72] to be executed in order and the command
[L399] [18:43.76] simply is something that makes a change
[L400] [18:47.36] of the state and and produces a value.
[L401] [18:50.56] And so you can just describe this state
[L402] [18:53.04] machine as just you know how event how
[L403] [18:56.16] commands affect the state and and how
[L404] [18:58.80] they produce and what you know what the
[L405] [19:00.88] new state is as a function of the
[L406] [19:02.40] original state and what the value is as
[L407] [19:04.64] a function of the original state. It it
[L408] [19:07.44] turned out that this was very obvious to
[L409] [19:10.00] me, but that's really in practice
[L410] [19:13.52] the important idea in that paper
[L411] [19:17.60] because it showed that this method of
[L412] [19:21.44] building distributed systems by thinking
[L413] [19:23.84] in terms of state machine and and can
[L414] [19:27.20] thinking about concurrent systems in
[L415] [19:30.00] terms of state machines.
[L416] [19:32.24] Um but that part was completely ignored.
[L417] [19:37.20] As a matter of fact, twice I talked to
[L418] [19:39.92] people about that paper and they said
[L419] [19:43.84] there was nothing in that paper about
[L420] [19:45.76] state machines and I had to go back and
[L421] [19:48.72] reread and reread the paper to be sure I
[L422] [19:51.28] wasn't going crazy and it really did
[L423] [19:53.20] talk about state machines. It's
[L424] [19:55.92] important uh for another reason. uh if
[L425] [19:59.28] you're trying to understand a concurrent
[L426] [20:01.44] program you concurrent programs are
[L427] [20:04.00] written the bakery algorithm is really
[L428] [20:06.08] an exception uh concurrent programs are
[L429] [20:08.96] written assuming atomic actions so that
[L430] [20:12.88] you assume that the execution behaves
[L431] [20:15.12] like a a sequence you you can assume
[L432] [20:19.12] that the execution proceeds as a
[L433] [20:21.12] sequence of events. It turns out that
[L434] [20:24.64] the way to understand, you know, why why
[L435] [20:28.00] does a program produce the right answer?
[L436] [20:30.72] Well, the answer is well, you it you
[L437] [20:32.56] give it the uh the you know the right
[L438] [20:34.72] input. You give it the input and then it
[L439] [20:37.20] produces the right answer. Well, but by
[L440] [20:40.40] the time you're in the middle of
[L441] [20:41.60] execution,
[L442] [20:43.28] what it was given at the beginning is
[L443] [20:45.68] ancient history. The only thing that
[L444] [20:48.88] that tells the program what to do next
[L445] [20:51.28] is its current state.
[L446] [20:53.68] And the way to understand
[L447] [20:56.72] uh a program, you know, a simple program
[L448] [20:59.12] that just, you know, takes input and
[L449] [21:01.04] produces an answer is to say what is the
[L450] [21:04.80] property of the state at each point that
[L451] [21:09.04] ensures that the answer it produces is
[L452] [21:12.40] correct is going to be correct. And that
[L453] [21:15.20] property which is mathematically a fun a
[L454] [21:20.00] boolean valued function of the state is
[L455] [21:23.20] called an invariant.
[L456] [21:25.12] And understanding the invariant
[L457] [21:28.08] is the way to understand the system. You
[L458] [21:30.96] know the the program and I realized that
[L459] [21:34.40] the same thing is true of concurrent
[L460] [21:36.16] systems and concurrent programs. People
[L461] [21:38.40] like to write proof you know behavioral
[L462] [21:40.32] proofs reasoning about sequences.
[L463] [21:43.04] And the problem with that is that the
[L464] [21:46.64] number of sequences possible sequences
[L465] [21:50.40] you know is exponential in the length of
[L466] [21:52.40] the sequence
[L467] [21:54.16] while the com so your complexity of your
[L468] [21:57.76] reasoning gets to be very complicated.
[L469] [22:00.16] It's very easy to to miss cases. Um but
[L470] [22:03.76] the complexity of an invariance proof
[L471] [22:06.16] the complexity of the invariant
[L472] [22:08.24] basically
[L473] [22:09.92] is well oh god it's the number of
[L474] [22:13.52] possible executions is exponential in
[L475] [22:16.48] the number of processes
[L476] [22:19.12] but the
[L477] [22:22.32] uh
[L478] [22:23.84] the behavior of the proof of a an
[L479] [22:26.72] invariance proof is quadratic in the
[L480] [22:29.76] number of processes. you know that's
[L481] [22:32.00] basically why invariance proofs are
[L482] [22:34.24] better but you know there's still for a
[L483] [22:37.28] long time that you know people you know
[L484] [22:40.88] doing uh distributed systems theory are
[L485] [22:44.16] trying to do it uh you know develop you
[L486] [22:47.36] know methods and formalism something
[L487] [22:49.60] that are based on partial orderings and
[L488] [22:51.76] that they've you know published a lot of
[L489] [22:54.00] papers but it's just you know not the
[L490] [22:56.88] way if you want to do it in practice
[L491] [22:58.40] that's that's not the way to do it and I
[L492] [23:00.72] shouldn't say you know it's not the way
[L493] [23:03.12] uh you know there are algorithms like
[L494] [23:05.36] the bakery algorithm that you know you
[L495] [23:10.08] know thinking in partial orderings is in
[L496] [23:12.24] fact a very good way of doing it but
[L497] [23:14.88] those are the exceptions the the work
[L498] [23:17.60] the method that works you know that you
[L499] [23:20.64] can be sure will will will work is the
[L500] [23:24.48] use of invariance
[L501] [23:26.16] >> I want to talk about the I guess the
[L502] [23:27.92] next paper which uh is the Byzantines
[L503] [23:31.60] general's problem. I think that's
[L504] [23:32.96] something that we hear about and we
[L505] [23:34.88] learn about when you're going through
[L506] [23:37.04] college and computer science and the
[L507] [23:39.60] name is great and I want to know the the
[L508] [23:41.84] story behind that problem. After I wrote
[L509] [23:45.36] that time clocks paper that was a tells
[L510] [23:48.88] you how to build a distributed system
[L511] [23:51.20] but assuming no failures and it was
[L512] [23:54.40] obvious that um
[L513] [23:57.92] you know distributed one reason for a
[L514] [23:59.60] distributed systems is you have multiple
[L515] [24:01.60] computers so if one fails you can you
[L516] [24:03.52] know keep going. in particular
[L517] [24:06.88] uh that was the problem that
[L518] [24:11.04] it was being solved at SRRI when I uh
[L519] [24:15.04] when I joined it but before I got to
[L520] [24:17.84] SRRI and I started working on that
[L521] [24:20.16] problem and I uh there's no notion of
[L522] [24:25.36] idea of you know what I should think
[L523] [24:27.12] about is you know what what can a
[L524] [24:28.80] failure do so I assume that you know the
[L525] [24:32.32] worst possible case that a failed
[L526] [24:34.00] process might do absolutely anything.
[L527] [24:37.04] And I came up with an algorithm that
[L528] [24:41.04] basically would uh implement a state
[L529] [24:44.16] machine uh
[L530] [24:47.84] under that assumption and that the
[L531] [24:50.56] algorithm I came out with used digital
[L532] [24:52.80] signatures. Yeah. So that it used the
[L533] [24:55.20] fact that a faulty process might do
[L534] [24:57.92] anything but it could not forge the
[L535] [25:00.00] signature of another process
[L536] [25:02.16] >> which just means that the message can be
[L537] [25:05.60] trusted that it came from a private
[L538] [25:07.68] >> right so that you can relay messages and
[L539] [25:10.56] the people know can check that the
[L540] [25:12.80] relayed message is actually the one that
[L541] [25:14.96] was originally sent uh and so that a
[L542] [25:18.72] solution using that when I got to SRRI I
[L543] [25:22.88] realized that the people were were
[L544] [25:26.00] trying to solve the same problem. Uh but
[L545] [25:29.76] there are two differences. First of all,
[L546] [25:32.24] at the time I did this was you know
[L547] [25:34.24] 1975.
[L548] [25:36.48] very few people know knew about digital
[L549] [25:38.24] signatures and in fact I don't remember
[L550] [25:40.16] when the Diffy Helman paper was
[L551] [25:42.40] published but it was around 1975
[L552] [25:46.08] and I happen to know about digital
[L553] [25:48.24] signatures because Whit Diffy who was
[L554] [25:51.44] one of the author two authors of that
[L555] [25:53.12] paper uh was a friend of mine and in
[L556] [25:58.16] fact at one point we were at a coffee
[L557] [26:00.88] house uh and he was describing these
[L558] [26:03.28] things that he said we have this problem
[L559] [26:05.12] of building digital signatures uh you
[L560] [26:08.40] know we haven't solved and I said oh
[L561] [26:10.32] that seems easy enough and uh and I sat
[L562] [26:13.20] down and literally on a napkin I wrote
[L563] [26:15.68] out a a you know the first digital
[L564] [26:18.80] signature algorithm. It was not
[L565] [26:20.80] practical at the time because it it
[L566] [26:23.84] required basically something like uh
[L567] [26:27.84] you know 128 bits to sign one bit of the
[L568] [26:32.88] you know of of the thing you they're
[L569] [26:34.88] signing. It's not quite that bad because
[L570] [26:37.44] you know as you might think because you
[L571] [26:39.04] could use sign not a
[L572] [26:42.88] the entire dent document but a hash of
[L573] [26:45.68] that document which you assume you know
[L574] [26:48.80] people cannot forge uh
[L575] [26:52.72] >> the hash they can't reverse
[L576] [26:54.72] >> yeah you can't reverse you go take a
[L577] [26:57.04] hash and and you know you find some
[L578] [26:59.36] other hash that you know or some other
[L579] [27:02.00] document that satisfies that hash. But
[L580] [27:04.72] anyway, that's why I had, you know,
[L581] [27:06.80] digital signatures were part of my
[L582] [27:08.88] toolkit. Uh, so the people at SRRI
[L583] [27:12.16] didn't have that, but they also had a
[L584] [27:15.60] nicer abstraction
[L585] [27:17.76] of it. Instead of getting agreement on a
[L586] [27:20.88] sequence among the processes on a
[L587] [27:23.04] sequence of commands,
[L588] [27:25.92] uh they would agree have an algorithm
[L589] [27:30.40] for agreement on a single command and
[L590] [27:34.00] then that algorithm would be uh executed
[L591] [27:38.08] multiple times to and you know that was
[L592] [27:41.04] a nicer way of of describing
[L593] [27:44.64] uh you know what you're doing than than
[L594] [27:47.52] the than than my method. So the first
[L595] [27:50.80] paper that was published uh use gave
[L596] [27:53.60] both the their original oh so but since
[L597] [27:58.32] they didn't have digital
[L598] [28:00.48] signatures they used a different
[L599] [28:02.40] algorithm uh and they had the property
[L600] [28:05.52] that to tolerate one faulty process uh
[L601] [28:10.00] you needed four processes whereas if you
[L602] [28:13.44] used digital signatures you only needed
[L603] [28:15.76] three processes. So the original paper
[L604] [28:18.96] contained both algorithms and so I was
[L605] [28:22.24] one of the authors. The other algorithm
[L606] [28:25.60] without digital signatures is is more
[L607] [28:28.40] complicated and the general one for end
[L608] [28:32.00] processes was really a work of genius.
[L609] [28:37.04] Uh it was almost incomprehensible. You
[L610] [28:39.84] just had to read in this complicated
[L611] [28:42.08] proof that uh you know for the arbitrary
[L612] [28:45.60] case of an arbitrary number of processes
[L613] [28:47.84] you need n pro for to tolerate n faults
[L614] [28:50.64] you needed four n processes whereas with
[L615] [28:53.68] digital signatures you need three n
[L616] [28:55.68] processes and the the algorithm for
[L617] [28:58.40] single fault wasn't hard but the one for
[L618] [29:01.12] multiple four parts was uh Marshall Peas
[L619] [29:04.88] was the one who did it and just
[L620] [29:07.20] brilliant uh Later in a in a later paper
[L621] [29:11.36] I uh I discovered uh a simpler proof one
[L622] [29:16.00] that was an inductive proofly proof that
[L623] [29:19.36] if it works for n minus one you know you
[L624] [29:23.28] it worked for n with 3 n if it works for
[L625] [29:27.04] 3 n * n minus one the original paper was
[L626] [29:30.72] uh you know the original one was just
[L627] [29:32.72] brilliant uh who would have discovered
[L628] [29:35.52] it anyway um so we published that paper
[L629] [29:40.24] and I realized that this was this the
[L630] [29:44.00] whole idea of Byzantine fault. So the
[L631] [29:46.16] thing is that Byzantine well Byzantine
[L632] [29:48.00] fault is one that where process assume a
[L633] [29:50.96] process can do anything. Now I was
[L634] [29:54.40] assuming that you know processing can do
[L635] [29:56.32] anything because you know I didn't know
[L636] [29:57.68] what to assume but the people at SRRI
[L637] [30:01.28] had the contract for building a
[L638] [30:03.52] multipprocess multi- computer system for
[L639] [30:06.64] flying airplanes and so they were the
[L640] [30:10.16] ones who appreciated the need for
[L641] [30:13.36] solving processes that can do malicious
[L642] [30:15.92] things because they they really couldn't
[L643] [30:18.08] assume what it would do. And every time
[L644] [30:21.84] you would get an algorithm and you you'd
[L645] [30:24.48] see, oh, uh, well, this algorithm, you
[L646] [30:28.48] know, try to get an algorithm with three
[L647] [30:30.08] processes, you know, for one fault, you
[L648] [30:32.40] know, you'd find that, you know, oh, you
[L649] [30:35.44] know, this this works and it must be,
[L650] [30:37.84] you know, really couldn't happen in
[L651] [30:39.28] practice. And then you'd be able to find
[L652] [30:41.76] some sequence of plausible failures that
[L653] [30:45.12] would lead the algorithm to be defeated
[L654] [30:48.16] if there were a faulty process. So you
[L655] [30:51.20] needed four uh and for some reason you
[L656] [30:55.20] know I thought that digital signatures
[L657] [30:59.28] was almost a metaphor in the algorithm
[L658] [31:02.24] that it should be possible
[L659] [31:04.80] you know since we weren't worried about
[L660] [31:07.20] malicious failures but but you know just
[L661] [31:10.96] things that happen randomly that there
[L662] [31:13.76] should be some way of of writing a
[L663] [31:17.12] digital signature algorithm that uh you
[L664] [31:22.00] know would have a sufficiently low
[L665] [31:23.60] probability of of failing but
[L666] [31:28.40] I never worked on that and nobody else
[L667] [31:30.64] ever did. So that those that algorithm
[L668] [31:33.04] was was pretty much ignored because
[L669] [31:36.00] digital signatures were very expensive
[L670] [31:37.84] in those days. I don't know what's being
[L671] [31:40.16] done now because you know computers are
[L672] [31:43.60] digital signatures are just computing
[L673] [31:45.60] and computing is you know is cheap. Uh
[L674] [31:49.68] but uh I remember at some point I
[L675] [31:53.04] happened to be communicating with
[L676] [31:55.20] someone who was an engineer at Boeing
[L677] [31:58.08] and I asked whether they knew about
[L678] [32:00.16] those results and he said yes when that
[L679] [32:04.64] he in fact uh was the one at Boeing who
[L680] [32:08.48] would read that paper and his reaction
[L681] [32:11.60] was oh we need four
[L682] [32:16.64] four computers.
[L683] [32:18.24] Uh but at any rate I realized that this
[L684] [32:21.04] was an important result and it should be
[L685] [32:24.48] well known and I had learned one thing
[L686] [32:27.92] from Dystra.
[L687] [32:29.76] uh Dy, you know, one of the things I
[L688] [32:31.52] learned from Dystra, he wrote this paper
[L689] [32:33.76] called the the dining philosophers
[L690] [32:35.92] problem. And that paper got a lot of
[L691] [32:39.04] attention, but the dining philosophers
[L692] [32:42.16] problem, I won't go into what it is, but
[L693] [32:43.92] I think the basic problem uh was not
[L694] [32:47.28] particularly interesting, but it had a
[L695] [32:49.52] cute story to it. It involved a bunch of
[L696] [32:52.56] philosophers sitting around a table with
[L697] [32:55.12] uh some funny kind of spaghetti that it
[L698] [32:57.28] required two forks and there was one
[L699] [32:59.12] fork between you know each fork would be
[L700] [33:01.68] shared with two people and uh but and I
[L701] [33:04.64] think realized it was because of that
[L702] [33:06.80] cute story that that problem was was
[L703] [33:09.76] popular. And so I decided that you know
[L704] [33:13.60] this this our work needed a cute story
[L705] [33:17.36] you know a nice story and I in invented
[L706] [33:19.52] Byzantine generals with the idea being
