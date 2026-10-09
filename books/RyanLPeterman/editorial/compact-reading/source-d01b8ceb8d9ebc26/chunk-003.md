# MIT Professor: Leetcode, P vs NP, SAT Solvers | Ryan Williams
Source: source-d01b8ceb8d9ebc26 | Chunk 3 of 5
Video: https://www.youtube.com/watch?v=AaK1SL2i_4Y
All caption text retained; paragraphs merge caption fragments without changing words.

[29:46.16–30:44.04; L793–L820] wrong, it's going to be false. Okay, so we have to avoid one of those assignments, okay? Well, that means that there are seven out of the eight possible assignments, so there's like three variables, two to the three, eight possible assignments, seven of them could be a satisfying assignment. They uh they could be part of a satisfying assignment, we don't know. But one of them is definitely not. So the one easy way to see that 2-SAT can be solved in less than 2 to the n time is just take any clause, try one of the seven possible assignments, and plug them in, and then recurse on the remaining formula. Now, let's think about what we did. If we were just trying all the possible 2 to the n assignments, and we we would like plug in, you know, uh one of eight possible assignments for each of those three variables. And so we'd have eight recursive calls.

[30:47.28–31:29.44; L821–L841] Well, we instead, because we're clever and we looked at the clauses, we have seven recursive calls. And that that's the difference. So so we reduced by three variables at the cost of seven recursive calls as opposed to eight. And this gets you a slight improvement. This gets you about uh 1.9 two to the end. Something slightly better than than uh two to the end. Okay, but you can do better than this. Um But this is this is sort of like the idea. You try to look at ways to plug in variables that will force constraints so you can rule out a large portion of the possible assignments.

[31:30.84–31:59.64; L842–L853] >> When I was thinking about circuits, it and you know, the different widths and depths, I I don't know if this is uh unusual question, but it it reminds me of neural nets, but the operators are different and the space of the uh the literals is different. So instead of booleans, it's maybe floating points. And so it just made me wonder about uh the algorithms that you might apply on a neural net. Is there, you know, analogs in between these two spaces?

[32:01.16–33:06.88; L854–L880] >> Yes. Yes. So um Yeah, if we look at say I want to model a neural network on So I want to compute say it's still a boolean function, but I want to do it with like a neural network. So like I want to use, let's say uh relus or um sign activation functions or or what what have you. Um There is a slightly more general like gate that we can use instead of ors and ands. That turns out to basically be equivalent. So, if instead of using ORs and ANDs, we use a so-called majority gate, which outputs one if and only if at least half of its inputs are one. Using this and negations, we can actually simulate uh neural nets, like the usual types of neural nets that you think of with the usual types of activation functions. So, if they have a constant number of layers of neurons, we can get a constant number

[33:09.16–33:23.12; L881–L887] of layers of majority gates and and negations. So, once you go So, this is so-called TC circuits for threshold circuits. Uh yeah, so once you allow threshold circuits, you can start to model uh neural networks.

[33:24.40–33:24.40; L888–L888] >> Still using booleans. It's just

[33:26.04–34:02.64; L889–L907] >> We're still looking at boolean inputs though, yes. So, once you allow your input space to to be larger and like have floating points, then um you can you can prove a lot uh more in terms of lower bounds. You can find like things that take like depth three in a neural net that's, you know, can't be done in depth two and so on. Um So, yeah, once you go past that and you start looking at just arbitrary real domain, it it becomes a a a totally different picture than from a discrete domain.

[34:04.84–34:53.76; L908–L930] >> OpenAI, Anthropic, Cursor, and Vercel all use this product to make their lives better. And the problem it solves is when you're building SaaS or an ad product and you want to sell to other companies, there's all these requirements you need to meet. There's SSO, there's SCIM, there's RBAC, there's audit logs. These are all things that take time to integrate, but aren't the main focus of your app. WorkOS is an API layer that lets you meet all of these requirements in just a few lines of code. So, let's say you have a new SaaS product and you want to sell to other companies, WorkOS will solve all of these critical feature gaps for you. You can check them out at workos.com to learn more and get started. And I appreciate them for supporting my work and sponsoring this podcast. One topic I thought might be fun to go over is you you wrote this paper about the

[34:55.76–35:09.36; L931–L936] likelihoods of these various conjectures in complexity theory and I I pulled a few of these that were kind of a minority opinions or maybe, you know, less less common takes. So, I'm curious to hear your rationale. So,

[35:11.74–35:11.74; L937–L937] >> [laughter]

[35:12.28–35:31.32; L938–L947] >> uh one of them the well-known one, you P P not equal to NP or, you know, P versus NP. Um you assigned an 80% confidence that they're not the same. And I think most people say much higher confidence. So, why do you why would you assign such a low confidence that they're not the same?

[35:32.68–35:44.92; L948–L954] >> It's interesting because I think I originally had something like 75% but then uh my college classmate Scott Aaronson was like, "How dare you?" kind of you know, he was

[35:45.15–35:45.15; L955–L955] >> [laughter]

[35:45.52–36:55.72; L956–L986] >> he was he he sort of called me out and I'm like, "Okay, fine. For you 80% fine." I guess that my point is that we really don't understand polynomial time computation as deeply as we think we do. And there are surprises like all the time in the power of algorithms. There are very few surprises in terms of lower bounds. Like, when we are able to prove a lower bound, typically it's something we very much expected to be true but it was hard to prove. It was hard to prove. Somehow we pulled it off, we got what we expected to be true. But all the time in algorithms people are finding algorithms where it's just like surprising. Just Wait. What? How How do you get something that fast? You're right. So uh this just happens over and over. When I was younger um when I was first thinking about P versus NP I like I had an intuition for what should

[36:57.92–38:08.36; L987–L1018] be. And what I've understood over the years is that my intuition for what should be is often just wrong. And I'm I'm having to revise my intuitions uh all the time. So when something like this happens often enough you start asking yourself, "What do I really understand? Uh do I really understand P versus NP?" Like I mean, I understand the the the statement, right? Like it's just one of those problems where somehow it is not so difficult to to make formal, to write down mathematically. But to actually know what the answer is is just orders of magnitude more difficult than it is to phrase the problem. And complexity theory in particular is littered with statements like this where um the the space of algorithms is just that vast. Um so if you just if you're just keep getting surprised over time, you're just like, "Well, what what do I understand?" Maybe it was just misplaced confidence.

[38:10.36–38:15.88; L1019–L1021] >> Okay, what about this one? So EXP not equal to NEXP or would you say NEXP?

[38:16.80–38:22.12; L1022–L1024] >> Oh, NEXP. Yeah. EXP versus NEXP. So this is like the exponential time of P versus NP.

[38:24.40–38:29.40; L1025–L1026] >> For X not equal to NX or NEXP, you gave it a 45% chance. And if this is

[38:32.18–38:32.18; L1027–L1027] >> [laughter]

[38:32.40–38:36.84; L1028–L1030] >> the P not equal to NP equivalent, but for exponential time, why is your

[38:37.68–38:37.68; L1031–L1031] >> Yeah.

[38:38.16–38:38.16; L1032–L1032] >> Why is it so low?

[38:39.40–38:43.64; L1033–L1035] >> Oh, because exponential time algorithms are even more powerful. Did I really say 45%? I mean,

[38:45.96–38:45.96; L1036–L1036] >> You did.

[38:47.28–38:47.28; L1037–L1037] >> versus X or NX versus co-NX.

[38:50.16–38:50.16; L1038–L1038] >> Yeah, NX not equal to X 45%.

[38:53.14–38:53.14; L1039–L1039] >> [laughter]

[38:53.16–38:53.92; L1040–L1041] >> I have it. It's in this table.

[38:55.20–40:05.44; L1042–L1073] >> So, so in other words, I believe NX equals X more than I believe they're different, right? So, um yeah, let me try to explain why. So, you can think of the NX versus X question as um some special case of P versus NP, where instead of looking at the arbitrary SAT problem, I'm looking at a SAT problem which is extremely compressible. So, there's like a really small little computer that is exponentially smaller than the length of the instance, and it just outputs the character uh on the line number and the column number for the for the DIMACS CNF, like the the CNF file, okay? So, it's like a extreme compression of like some file. So, it's like you zipped it down to like something like exponentially smaller than its original length, okay? So, it's like some super compressed, extremely highly regular SAT instance. So, I give you that, and I ask you, uh when you unpack this thing,

[40:07.76–41:19.88; L1074–L1107] decompress it, is the result going to be satisfiable or not? And I want you to solve this in time polynomial in the decompressed representation. Okay. Okay. So, the point is that like this is SAT, but in the some very special case where the thing is extremely structured. So, the idea um one conjecture for why SAT solvers work um in practice. Like one I mean this is I mean conjecture maybe overkill because I mean this is just this is not even a well-formed mathematical statement. So, one hypothesis for why SAT solvers work in practice is because um the real world is highly structured. The real world is governed by physical laws that are not random. They're not arbitrary. Like from a very small number of rules, we can recreate so much of science. So, what arises in practice from designs of hardware and things like this are often extremely compressible. They have to be extremely compressible.

[41:22.56–41:49.44; L1108–L1120] And so maybe it's true that you know, every uh SAT which has uh a highly compact representation can just be solved uh efficiently. This is This is the idea of whether, you know, NEXP equals EXP. Um that it when it's really really structured like that and super compressible, there is some advantage. It's not like a completely random and since it's not like something arbitrary, it's No, it's in fact very very special.

[41:51.92–42:02.68; L1121–L1125] >> The other one is 80% likelihood on NEXP equal to coNEXP, and you wrote why would a self-respecting complexity theory do that?

[42:03.74–42:03.74; L1126–L1126] >> [laughter]

[42:04.68–42:06.60; L1127–L1128] >> Yeah, I was curious why that's such a contentious statement.

[42:08.36–43:10.44; L1129–L1159] >> So, NEXP versus coNEXP. Let's Let's first talk about NP versus co-NP. So, co-NP um is like the class of sort of complements of NP-complete problems like like UNSAT, like checking whether something's UNSAT. Now, from the time complexity point of view there's no difference between checking SAT and UNSAT. You can always flip the answer. But from the complexity point of view, if I if I ask you does co-NP equal NP? What I'm asking you is, could you prove to me that a formula is unsatisfiable with a short proof? When it's satisfiable I can give you a short proof. I can just give you the satisfying assignment. You plug it in, check that it works. But if it's unsatisfiable, if there no assignment works we're saying for all assignments the formula is not true. Can you flip that to an existential statement and say, "Oh, there exists this little proof makes it work." So people don't believe that NP is equal to

[43:13.88–44:24.52; L1160–L1193] co-NP and in fact like NP different from co-NP implies P different from NP. Um But so this is the exponential time version of NP versus co-NP. So it's co-NEX uh versus NEX. The reason why I think these are likely to be equal is that if a little birdie sat on an NEX machine's shoulder and gave it a little bit of advice about what the co-NEX thing is doing then the an NEX uh algorithm can actually solve co-NEX problems. And so let let me explain uh let me explain why Yeah, what's the little birdie What the heck is the little birdie saying? So because NEX problems can run in 2 to the end time and two to the N squared time and things like that. Running an exhaustive search over all possible inputs of length N is no problem for NX. So, what a little birdie can do is say, "Okay, suppose um like I want to verify that

[44:27.88–45:31.12; L1194–L1223] this particular um instance like let's say let we can talk about like an unsat but like the you know some compressible unsat problem or something. Suppose I want to prove that this compressible unsat instance um is a yes. Okay? How am I going to do that uh with NX? The little birdie will tell me the total number of inputs of length N which are a yes. Okay? So, it it will it will just tell me some string which says, "Here's the total number of inputs of length N. You gave me a length N input. Here's the total number of inputs of length N uh that are a yes. Okay? Okay? So, um this this advice this little you know birdie's advice doesn't take very much like to encode a count. It's like order N bits to encode a count uh of things. So, um so, what does the NX thing do to prove a co-NX thing? What it does is it

[45:33.88–45:54.44; L1224–L1234] guesses the things which are a no. So, I'm trying to prove unsat. So, unsat means yes, sat means no. So, the NX thing guesses those things which are no. The no things it can answer, right? If it's a sat thing, it can just guess the answer to each of the nos. Okay? So, it guesses the answer to each of the
