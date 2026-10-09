Chunk 3; segments 663–990. Start may repeat the previous chunk for context.

# Creator of Scala: Comparing Languages And How AI Will Impact Them | Martin Odersky

Source ID: source-5f7cf6e81e665bd5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Scala_Comparing_Languages_And_How_AI_Will_Impact_Them_Martin_Odersky_en.txt
Video: https://www.youtube.com/watch?v=LdN4sPWM-WY

[L672] [27:23.04] also demand that it would would would
[L673] [27:25.20] generate very efficient code for your
[L674] [27:27.12] program because again the compiler
[L675] [27:29.04] should know that right so there's a lot
[L676] [27:30.88] of demands on that plus there's a demand
[L677] [27:33.52] that it should should be very very fast
[L678] [27:35.76] uh and to square all these demands
[L679] [27:38.88] requires quite a bit of work basically
[L680] [27:42.08] there are also things that make it
[L681] [27:43.60] easier for compilers because they're
[L682] [27:46.00] fundamentally deterministic programs. So
[L683] [27:48.80] essentially you run a compiler on a
[L684] [27:50.56] source and you should you always get the
[L685] [27:52.32] same output. So it means they're easier
[L686] [27:54.48] to debug. You can just replay things and
[L687] [27:56.88] repeat things. Whereas if I would have
[L688] [27:59.28] some cloud service or distributed
[L689] [28:01.04] application that has other nightmares,
[L690] [28:03.52] right? That every run is different and
[L691] [28:05.36] how how do you even figure out what goes
[L692] [28:07.12] wrong?
[L693] [28:07.84] >> So when you wrote that compiler uh I
[L694] [28:10.40] think espresso for Java um how long did
[L695] [28:14.16] it take to write that by hand? uh at the
[L696] [28:17.12] time it took me about 3 months I think
[L697] [28:20.24] not full-time maybe half time three
[L698] [28:22.16] months half time something like that but
[L699] [28:23.92] that was a very simple compiler too so
[L700] [28:26.32] that's the other thing with compilers
[L701] [28:27.68] they typically start simple and when
[L702] [28:30.00] you're at the 10 year mark or 20 year
[L703] [28:31.84] mark then there's lots and lots of
[L704] [28:33.68] essentially other requirements to a
[L705] [28:35.20] compiler that make them more complex.
[L706] [28:37.60] Were there libraries that you could rely
[L707] [28:39.84] on to to kind of piece together
[L708] [28:42.00] components of it or did you have to
[L709] [28:43.44] write you know everything from scratch?
[L710] [28:46.56] I wrote there was a library to uh
[L711] [28:48.88] generate uh bite codes I think uh I
[L712] [28:51.84] think I used that in that version. Yeah
[L713] [28:53.76] I did. Yeah. So there was a a library
[L714] [28:55.84] that essentially a high level library to
[L715] [28:57.92] just assemble by codes and and put them
[L716] [29:00.32] in the to the right format and things
[L717] [29:02.16] like that. Uh but that was essentially
[L718] [29:05.04] it. The rest I wrote by hand. Yeah.
[L719] [29:07.60] That's crazy because well I mean these
[L720] [29:10.40] days a lot of people even more so now
[L721] [29:12.88] we're thinking less using AI more to
[L722] [29:15.36] kind of you know write the code. So
[L723] [29:17.60] that's pretty impressive. I saw one of
[L724] [29:19.92] the big I guess moments for Scola was
[L725] [29:22.16] that Twitter adopted it and I wanted to
[L726] [29:24.72] know the story behind that. How did they
[L727] [29:26.88] choose such a obscure language at that
[L728] [29:29.28] time?
[L729] [29:30.08] >> It was very obscure at the time. That's
[L730] [29:32.16] true. Uh so I believe the story was
[L731] [29:35.28] Twitter originally was written in Ruby
[L732] [29:38.48] and um it wasn't very reliable because I
[L733] [29:42.16] believe it's again a problem with
[L734] [29:43.36] garbage collector and memory management
[L735] [29:45.12] and things like that. So uh the uh and
[L736] [29:49.20] it was a small company at the time. So
[L737] [29:51.20] 25 people uh including the ops people
[L738] [29:54.72] and um the uh essentially the the board
[L739] [29:58.72] and the VC investors said you can't go
[L740] [30:01.44] on like this being unreliable like that.
[L741] [30:04.00] You should do Java because Java was sort
[L742] [30:06.40] of the solid choice at the time. But the
[L743] [30:09.04] the the some some of the engineers at at
[L744] [30:12.08] Twitter they wanted essentially
[L745] [30:13.60] something more fancy as a programming
[L746] [30:15.68] language and there were some people who
[L747] [30:17.92] knew Okamo and liked Okamo but of course
[L748] [30:21.12] Okamel didn't run on the JVM and then
[L749] [30:23.92] they found Scala and said well Scala is
[L750] [30:25.60] actually quite a lot like Okamo and we
[L751] [30:28.24] can tell our investors that we do Java
[L752] [30:30.16] because it's not a lie we do JVM JVM by
[L753] [30:33.04] code that's essentially what it what
[L754] [30:35.20] what where what it comes down to. So
[L755] [30:37.36] that's why why they picked it and they
[L756] [30:39.12] were quite the first but once they
[L757] [30:40.56] picked it sort of the floodgates opened
[L758] [30:42.40] because at that time they were very uh
[L759] [30:45.04] interesting company and a lot of people
[L760] [30:46.88] admired them. So a lot of people
[L761] [30:48.48] followed and did the same thing then uh
[L762] [30:51.04] mostly they came from dynamic languages.
[L763] [30:53.60] So Twitter came from Ruby others came
[L764] [30:55.92] from PHP or uh yeah JavaScript uh things
[L765] [30:59.68] like that. I mentioned a little bit that
[L766] [31:02.24] you know AI is kind of generating a lot
[L767] [31:04.24] of code and I wanted to ask you what you
[L768] [31:07.52] thought maybe the future of programming
[L769] [31:09.76] languages might look like if you kind of
[L770] [31:12.24] speculated or drew out further into the
[L771] [31:15.12] future like if AI is generating more of
[L772] [31:17.12] the code. How do you think that might
[L773] [31:19.20] affect the programming language
[L774] [31:20.96] ecosystem?
[L775] [31:22.32] >> Yeah, I think right now we are sort of
[L776] [31:24.08] in an existential crisis, right? So we
[L777] [31:26.96] have [snorts] AI generating the code but
[L778] [31:29.12] uh uh humans being asked impossible
[L779] [31:32.72] tasks like to review all this these
[L780] [31:35.04] mountains of code and things like that
[L781] [31:36.80] which will never work. Um and uh at the
[L782] [31:40.00] same time a AI is also gotten extremely
[L783] [31:42.96] good at exploiting vulnerabilities in
[L784] [31:45.20] code like we we all heard of Fable and
[L785] [31:47.36] and and things like that that you can't
[L786] [31:49.12] use it anymore because it's too
[L787] [31:51.28] dangerous. It will exploit things. So
[L788] [31:55.44] um we are at a moment where it's
[L789] [31:58.64] essentially very dangerous that we lose
[L790] [32:00.48] control as humans of what what actually
[L791] [32:03.04] happens here and uh that's a challenge
[L792] [32:06.64] that I think programming languages can
[L793] [32:09.28] help meet and probably definitely not
[L794] [32:11.92] only programming languages that's no
[L795] [32:13.76] silver bullet but they definitely can
[L796] [32:16.24] help things. Um so I think one of the
[L797] [32:20.24] things is that the focus if the code is
[L798] [32:24.08] AI generated then the focus has to go
[L799] [32:26.32] elsewhere and I think the co focus will
[L800] [32:28.32] go to the interfaces and to the types.
[L801] [32:31.12] So I expect types will become a lot
[L802] [32:33.76] stronger and more precise than than what
[L803] [32:36.40] we had because types is essentially the
[L804] [32:38.88] handle that we can make a contract
[L805] [32:41.44] between the human and the AI that the
[L806] [32:43.68] that the human can understand and that's
[L807] [32:45.60] concise enough to be reviewed and that
[L808] [32:48.48] essentially the AI can keep to uh we
[L809] [32:51.60] have to level our game quite a lot. Uh
[L810] [32:54.48] because right now I mean let's face it
[L811] [32:57.12] type systems are mostly
[L812] [32:59.92] um uh recommendations. Uh they're mostly
[L813] [33:04.16] uh things that uh mostly hold but not
[L814] [33:07.04] always. There are no guarantees because
[L815] [33:08.56] you can always have a cast or well you
[L816] [33:11.76] you use some dirty memory or I mean
[L817] [33:14.16] there there are number of a lot of
[L818] [33:15.84] techniques to sort of undermine the type
[L819] [33:18.08] systems and we have to close all these
[L820] [33:19.76] holes from the beginning because uh once
[L821] [33:22.56] once there is a hole somebody can
[L822] [33:24.00] exploit it. Uh so I think strong types
[L823] [33:27.04] strong highle types will help. Um and
[L824] [33:31.12] then I think the the other part is
[L825] [33:33.92] generally the programmer has to think
[L826] [33:35.60] much more about what are the
[L827] [33:36.80] requirements and what are the
[L828] [33:40.48] essentially the high level
[L829] [33:41.52] specifications
[L830] [33:43.36] uh and be able to leave the code to be
[L831] [33:47.12] generated by somebody else in confidence
[L832] [33:50.24] and uh I think we're not quite there yet
[L833] [33:53.12] but we we we have some ideas how we
[L834] [33:55.68] could get there. uh so one one uh
[L835] [33:59.84] technique that I believe uh we can use
[L836] [34:02.88] and it has been around for a long time
[L837] [34:04.56] but maybe it's time has come now this
[L838] [34:06.56] capabilities capabilities essent
[L839] [34:09.12] essentially was used in operating
[L840] [34:10.64] systems to give very fine grain
[L841] [34:12.32] permissions to to uh entities users
[L842] [34:16.00] programs and things like that and uh I
[L843] [34:19.44] believe that can be used also for agents
[L844] [34:22.48] and the agentic AI to say well once we
[L845] [34:25.84] have agents We have to give agents very
[L846] [34:28.16] precise and fine grain capabilities what
[L847] [34:30.08] they can do and that lets us essentially
[L848] [34:32.56] be confident about what they will not be
[L849] [34:35.52] able to do like they will not be able to
[L850] [34:37.84] leak my API keys or my email or or do do
[L851] [34:42.08] other things right so I think that's
[L852] [34:44.08] that's an important part uh and the
[L853] [34:48.16] existing languages are uh not there yet
[L854] [34:51.60] uh I think Scala is halfway there at
[L855] [34:54.32] least it's there where in essentially
[L856] [34:56.56] stuff we're working on which we have in
[L857] [34:58.08] the lab and we have released as an
[L858] [34:59.60] experimental feature. So I'm quite
[L859] [35:01.60] excited about that. Um the first thing
[L860] [35:04.08] that you have to do is definitely be
[L861] [35:07.28] memory safe. So a language that
[L862] [35:09.44] essentially is is not safe in memory
[L863] [35:11.52] that lets you essentially uh access
[L864] [35:15.04] undefined memory uh is immediately out
[L865] [35:17.60] because you can't you can't guarantee
[L866] [35:19.28] anything. So that's in that sense it's
[L867] [35:22.16] good that there is a drive to use let's
[L868] [35:23.76] say rust as a memory safe language we're
[L869] [35:25.84] even that that was even promoted by the
[L870] [35:28.80] American government I believe so that's
[L871] [35:30.88] definitely a very useful drive but I
[L872] [35:33.04] think you need a lot more because you
[L873] [35:34.88] need much rest talk folks essentially
[L874] [35:37.60] mostly or only about memory you need to
[L875] [35:40.08] talk about a lot more things than memory
[L876] [35:42.48] you need about essentially read
[L877] [35:43.92] permissions write permissions access to
[L878] [35:46.72] secrets all these things that that are
[L879] [35:49.04] that are uh uh that go beyond that and u
[L880] [35:54.48] you could say okay uh that
[L881] [35:57.68] Martin you're totally unrealistic
[L882] [35:59.52] because uh all our software is written
[L883] [36:01.92] in C and C++ and we will not be able to
[L884] [36:04.48] rewrite that uh but that I believe AIS
[L885] [36:08.64] can help there right so AIs are great to
[L886] [36:10.72] re in rewriting software so if we know
[L887] [36:13.76] what to rewrite too I think we could we
[L888] [36:15.76] might be able to get there
[L889] [36:17.44] >> you mentioned some of those experimental
[L890] [36:19.36] features in Scola that um might have
[L891] [36:22.16] some sort of safety guarantees or signal
[L892] [36:25.12] capabilities. Can you explain what that
[L893] [36:27.60] might look like or maybe give an
[L894] [36:29.12] example?
[L895] [36:30.24] >> So, so a simple example would would be
[L896] [36:32.32] let's say somebody gives me a file and
[L897] [36:34.88] um uh and uh I have access to the file
[L898] [36:39.36] let's say a log file or something like
[L899] [36:41.20] that. I have access for a file for a
[L900] [36:43.04] limited time and then I I need to close
[L901] [36:45.20] it. So typically I have a operation that
[L902] [36:48.32] essentially somebody passes I a file to
[L903] [36:51.36] me to an operation that my program
[L904] [36:54.24] provides and the program does something
[L905] [36:56.56] with the file and then the environment
[L906] [36:58.08] will close it. But how do we make sure
[L907] [37:01.12] that I don't hold on to the file after I
[L908] [37:04.40] get it back to the environment or after
[L909] [37:06.16] I I I pretended I'm finished with it
[L910] [37:08.72] because hey I I have a file. I could
[L911] [37:10.56] have stored it in a variable. I could
[L912] [37:12.32] have stored it on the side. I could have
[L913] [37:14.08] gone g come g come g come g come g come
[L914] [37:14.32] g come g come g come g come g come g
[L915] [37:14.40] come g come g come g come g come g come
[L916] [37:14.40] g come g come g come g come comeone back
[L917] [37:14.72] to it and done something with it. So uh
[L918] [37:17.76] capabilities help me prevent that
[L919] [37:19.76] because essentially I I can say okay so
[L920] [37:21.76] this file is a capability and then I can
[L921] [37:24.08] further say well this capability can be
[L922] [37:26.80] used only in a limited scope and the
[L923] [37:29.28] type system will make sure that the
[L924] [37:31.04] capability doesn't escape and the way we
[L925] [37:33.28] do that is that if a type refers to
[L926] [37:36.48] capabilities so if I have a a thing that
[L927] [37:39.04] I say I give you back a a lambda or a a
[L928] [37:43.44] stream and it holds on to the file. So
[L929] [37:45.76] the stream holds on to the file in
[L930] [37:47.44] secret. In our language that won't be a
[L931] [37:50.32] secret anymore because the type has to
[L932] [37:52.48] declare that the thing I return does
[L933] [37:55.28] hold on to the file. The file is a
[L934] [37:56.88] capability and I can't essentially hide
[L935] [37:59.92] capabilities I have access to in my
[L936] [38:02.16] type. I have to be I have to declare
[L937] [38:04.08] them and that gives me essentially this
[L938] [38:06.80] this control that then I can also
[L939] [38:08.96] enforce to say well at this point you're
[L940] [38:11.04] not allowed to have any capability
[L941] [38:12.48] because the type that I enforced you to
[L942] [38:15.04] have is a type that doesn't hold
[L943] [38:16.80] capabilities and that's that way I
[L944] [38:18.56] enforce with the type system something
[L945] [38:20.56] which uh previously hasn't really been
[L946] [38:23.52] enforcable
[L947] [38:25.04] uh with for memory safety it's
[L948] [38:26.96] essentially the same thing with arenas
[L949] [38:29.04] uh that I I have an area where I
[L950] [38:32.00] allocate memory and then I want want to
[L951] [38:33.84] get rid of it. I have to make sure I
[L952] [38:35.60] don't have pointers pointing into it and
[L953] [38:37.92] that's exactly the same the same
[L954] [38:39.68] situation and and let's say for
[L955] [38:43.12] accessing secrets again. So it's a very
[L956] [38:45.04] common pattern that I say in certain
[L957] [38:47.84] situations I want to make sure that you
[L958] [38:51.12] don't have uh or that you only have a
[L959] [38:53.60] set of defined capabilities that I give
[L960] [38:56.08] you and nothing else. You mentioned uh
[L961] [38:58.80] memory safety is an absolute uh table
[L962] [39:01.68] stakes. What are the programming
[L963] [39:03.60] languages that you think of that are not
[L964] [39:05.44] memory safe? I know there's C, but what
[L965] [39:07.36] are the other ones?
[L966] [39:08.80] >> The big ones is C, C++. Um I I don't
[L967] [39:12.56] know about I think Zik or Nim or other
[L968] [39:14.88] low-level systems languages are not
[L969] [39:16.56] memory safe. So that was sort of in Rust
[L970] [39:19.28] the a big achievement that you say you
[L971] [39:21.36] can be a low-level systems languages and
[L972] [39:23.36] be be memory safe. nobody sort of
[L973] [39:26.00] thought that that was possible before
[L974] [39:27.76] Rust came. Uh so so that's why I would
[L975] [39:31.52] think I don't want to say anything wrong
[L976] [39:33.44] but I would think that essentially most
[L977] [39:36.24] other low-level systems languages would
[L978] [39:38.24] not be memory safe. Um but you really
[L979] [39:41.76] need more than memory safe. You really
[L980] [39:43.28] need capability safes that you say you
[L981] [39:46.08] when I essentially hang on tell you I
[L982] [39:48.80] can't sort of forget capabilities to say
[L983] [39:51.04] I hang on to something and I I just
[L984] [39:52.88] conveniently forget that I have access
[L985] [39:54.80] to that and I can't forge capabilities
[L986] [39:57.36] to say well if I need a capability I
[L987] [39:59.84] just make one up. And so these two
[L988] [40:02.16] things need to be prevented and that
[L989] [40:03.84] goes go that goes beyond memory safety.
[L990] [40:07.12] But memory safety without memory safety
[L991] [40:09.44] essentially you have nothing because you
[L992] [40:10.96] can fake everything.
[L993] [40:12.32] >> A lot of programming language design and
[L994] [40:15.12] how we write code in the past is writing
[L995] [40:18.08] the source code so that it's um it's
[L996] [40:21.52] it's nice for humans to read. But if
[L997] [40:24.48] humans are no longer interacting with
[L998] [40:26.16] the code, what kind of things come to
[L999] [40:28.72] mind that we might not care as much
