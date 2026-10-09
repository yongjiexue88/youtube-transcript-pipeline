# MIT Professor: Leetcode, P vs NP, SAT Solvers | Ryan Williams
Source: source-d01b8ceb8d9ebc26 | Chunk 1 of 5
Video: https://www.youtube.com/watch?v=AaK1SL2i_4Y
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.00–00:01.88; L10–L11] Hypotheses which are at the edge of our understanding can be enlightening.

[00:04.88–00:17.92; L12–L18] >> This is Ryan Williams. He's a professor at MIT who won the Gödel Prize for theoretical computer science, and I started by asking him a LeetCode question. So, the question is three-sum. Can you do better than n squared for this?

[00:18.36–00:22.44; L19–L21] >> Yeah, you actually can do better than n squared, and this is um not at all obvious.

[00:23.56–00:25.96; L22–L23] >> He also had contrarian takes on popular hypotheses.

[00:26.92–00:34.16; L24–L27] >> I think I'm on the record as not believing this hypothesis. We really don't understand polynomial time computation as deeply as we think we do.

[00:42.08–00:57.20; L28–L33] >> All right, I want to start by asking you the most popular LeetCode question. So, the question is three-sum. Given a list of numbers, and we want to find three numbers such that they sum to zero.

[00:57.76–00:57.76; L34–L34] >> Yes.

[00:58.64–01:03.36; L35–L37] >> And so, what are your thoughts on the brute-force solution for this? We can start there.

[01:04.64–02:06.32; L38–L64] >> So, the obvious brute-force solution takes if you you've got n numbers n cubed time. Just try all the triples of numbers, sum them up, see if they sum to zero. There is a faster uh solution. So, one way to get an order n squared time algorithm for three-sum is to first start by sorting the numbers. And then, you go through the numbers one by one. Say like, you're looking at a number A. And you want to know, is there a B and a C in the rest of the list um whose sum with A is going to be zero? Okay, so, the way this works is after you sort the numbers, you you do what's called a finger search. So, you put um the finger from your left hand on the minimum element and finger from your right hand on the maximum element. So you start there. And you check like, okay, are these my B and C?

[02:08.76–03:04.60; L65–L88] Right? So you you add them min and max and check if adding that with A gets you zero. Okay? And um if you're lucky, okay, then you're done, but typically you're not lucky. And so this sum of the min and the max is either um larger than your target value minus A or it's smaller. Okay? If it's larger, then you need to decrease the larger number. So you take your right finger, which is sitting on the maximum element, and you move it to the left one slot. Okay? So you decrease the larger one. All right? If the sum is smaller than your target, you need to take the smaller number and make it a little bit bigger. So you move the you move your left finger sitting on the minimum over one slot. Okay? And you you keep doing this. You keep checking whether, you know, your left finger and right finger are pointing at a solution.

[03:06.84–03:48.36; L89–L106] And if they aren't, then you adjust it. If they do, they ever do sum up to exactly what you want, you're done. And so after each comparison like this, right? One of your fingers moved. Okay? If the fingers ever cross, then you don't have a solution. Like there's just there just can't be a solution. And so the number of times you move, you know, your fingers in total is like N. So so you have a order N solution for finding that extra pair. And you do this for each of the numbers A. Okay? So then you get a order N squared uh solution overall. You do it N times. Each finger search uh takes order N time.

[03:50.32–03:50.32; L107–L107] >> And that is the popular solution. think.

[03:53.80–03:53.80; L108–L108] >> solution, yes.

[03:54.56–04:08.40; L109–L115] >> of people know when we're in these algorithmic LeetCode interviews. And I know a lot of your research is kind of about pushing lower bounds, so maybe we can start that conversation off by can you do better than n squared for this?

[04:10.48–05:05.28; L116–L140] >> Yeah, you actually can do better than n squared. And this is um uh not at all obvious. In in fact, it it stems from um taking this finger search idea and pushing it in a different direction. So, what you do is you take your sorted list, okay, and you break uh the sorted list up into little groups of contiguous elements. So, let's say your little group is like log n size or square root log n. It's like a really small little group, okay? So, you've got either n over log n groups total or n over square root log n groups total depending on how you break up your groups. And then the idea is you're going to perform the same kind of finger search, but you're going to set things up so that you're comparing two pairs of groups. Your finger's always pointing at an entire group. So, like the left hand and right hand

[05:07.16–05:59.92; L141–L167] are pointing at two groups and you want to know if there's a three sum solution in that group. And you can set up a kind of fast data structure to check a small group, okay? And this data structure will take much less than um the number of elements in the two groups squared. So, you set up some kind of fancy data structure. And because you set your group size so small, it's like a pre-processing that you do over all the possible inputs you could send from a pair of groups. And so, you have some data structure and it will, you know, let's say it takes you n to the 1.5 time to prepare this data structure, this fancy data structure. But now, when you're looking at a pair of groups, you can look at the answer much faster than what finger search would have taken. I guess finger search through like a group of length G and another

[06:01.20–06:43.88; L168–L188] group of length G would take about order G time, and you can do actually do faster by by this kind of look up. This kind of table look up. I think it is kind of like you you take uh this list of length N and you uh kind of shrink it into like N over num uh N over N over group size uh number of things. And these are more complicated objects. And then you do And now like you you're trying to you're trying to speed up like the check over these like small uh complicated objects. For like, should I move my finger to the right? Like, is there nothing in this group? Would finger search just just go straight through this group or not? Is basically what you're asking.

[06:45.08–06:49.08; L189–L191] >> So, the unit that you're operating on is not a single integer, it's a a group.

[06:49.88–07:23.28; L192–L210] >> Yeah, it's like a group of them. So, you use some kind of table look up. Uh And so, well, it's it's it's much fancier than a table look up, actually. It's It goes through some other model called the linear decision tree model. Like, so it's like in some weird model where you can actually get a faster three some solution. You can get a N to the 1.5 solution. And there's It's a really interesting and sophisticated solution, but what I want to emphasize is it starts from the finger search solution. And sort of like figuring out how to like process finger moves faster. Uh sort of do pre-processing so that finger moves can can go faster.

[07:26.52–07:39.20; L211–L216] >> Yeah, I saw the the time complexity this. It's N squared divided by log N divided by log log N all raised to the 2/3. What Is there any intuition behind I mean, that's just crazy.

[07:40.24–08:26.04; L217–L239] >> So, there are several algorithms of this kind, and they all work by doing some modification on what I was talking about because you can sort of reduce to a different model. Like a like a a different kind of look up table, a different kind of set of tricks. And you know, maybe there is some savings you can do here and there by sort of compressing things a little differently. Um so, that yeah, there are several algorithms that beat the n squared running time bound, and they all, to my knowledge, kind of work in a similar type of of way. Like they they're they're taking this n squared time algorithm and finding little ways to like pre-process and then optimize like based on the pre-processing. Like make finger searches faster and things like that. Sort of yeah.

[08:27.88–08:37.16; L240–L244] >> A lot of your research is on this this topic of fine-grained complexity or kind of lowering lower bounds. So, um maybe you can explain what is fine-grained

[08:37.80–08:37.80; L245–L245] >> Lowering lower bounds, I like that.

[08:38.96–08:38.96; L246–L246] >> Yeah, lowering

[08:39.42–08:39.42; L247–L247] >> [laughter]

[08:40.16–09:48.08; L248–L274] >> Um the idea behind fine-grained complexity is we have a variety of problems, canonical problems that we teach to undergrads. Um we have canonical algorithms for these problems. These algorithms have resisted any major improvements in decades, and so, we wonder, are these algorithms optimal? And what does a theory of optimality look like in terms of time complexity? So, what if we just focus solely on the time complexity of a problem? Like the fastest algorithm that will solve that problem. What does complexity look like then? Because like P versus NP is not about time I mean, it's about time complexity but on a coarse grained level where P is just polynomial time. But that polynomial could be n to the 10 into the billion whatever and so like showing that something's not in P is is showing that it needs some super polynomial amount of time. Whereas here we we are concerned with there's a canonical problem it

[09:50.88–10:49.68; L275–L302] takes n cubed time with some very elegant canonical algorithm. We want to know could you do any better? Could you improve that exponent to n to the 3 minus epsilon for some epsilon? And then you ask, well suppose I have a problem over here and it has a quadratic time algorithm. And I want to know if I can improve that quadratic time algorithm by a little bit. Then you start asking questions like, well, suppose I improve this algorithm by a little bit. Can I improve this algorithm over here by a little bit? And this is naturally a notion of reduction like saying that like I want to have some reduction from problem A to problem B so that if I can improve the algorithm for problem B just a little bit then I can also improve the algorithm for for problem A by just a little bit. This actually leads to a different notion of complexity. You can even take

[10:52.04–11:57.84; L303–L334] an NP-complete problem and a P problem and reduce the NP problem to the P problem and the question still makes sense. So for example, uh you could talk about the subset sum uh problem, okay? So the subset sum problem you've uh got n numbers and a target value. And you want to know if there's a subset of those numbers that sum to a particular target value, okay? Now you got n numbers, there's two to the n possible subsets. The obvious algorithm takes two to the n time. Okay? But you can actually do better than this. And the way you do better than this is to reduce to a polynomial time solvable problem. So, you can get a algorithm which runs in square root of 2 to the n time for the subset sum problem. You can avoid enumerating over all the possible subsets in a substantial way. And this is in fact known um commonly in cryptanalysis by

[12:00.08–12:57.76; L335–L359] um I guess a like a meet in the middle uh type approach. Like So, people do this sort of thing all the time. The idea is you partition the set of all the numbers into two halves, n over two, n over two. You enumerate all the subset sums on the two halves. So, you have 2 to the n over two possible sums for like the first half, 2 to the n over two possible sums for the second half. Then you want to know, is there a number from the first half, you know, from this huge list, plus another number from the second half, this huge list, that sums to the target. Now, this is the two sum problem. This is really nothing more than the two sum problem, which you can solve by sorting and binary search. And this is a reduction. We have shown how to solve a subset sum problem like which would normally take 2 to the

[12:59.44–13:50.88; L360–L384] n time in square root of 2 to the n time. An NP-complete problem by reducing it to a problem like two sum. The obvious algorithm there takes n squared time trying all the pairs of numbers to see if they sum to a target, and using an n log n time algorithm for that. So, so fine-grained complexity can can relate problems that would not be relatable at all in the traditional P versus NP theory. Like one problem is NP complete, the other problem is not, so they they should not have a polynomial time reduction between them, like in general, right? But so but if you just look at the time complexity and you focus on okay, I have an algorithm, 2 to the n algorithm, is it the best possible? Then um and then I have a n squared algorithm, is it the best possible? And you then you can relate the two problems. And this is a general phenomenon that

[13:52.72–13:57.28; L385–L387] you can relate problems that look like they should have nothing to do with each other.

[13:58.52–14:10.68; L388–L393] >> So you talked about you talked about reducing subset sum to two sum and but subset sum is n arbitrary integers that sum to the target sum, right?

[14:11.92–14:27.84; L394–L400] >> Yeah, so the idea is um nobody said I had to use a polynomial time reduction or something like that to reduce one problem to another. So so what's what happened what happened the trick was I took this subset sum problem that had n numbers
