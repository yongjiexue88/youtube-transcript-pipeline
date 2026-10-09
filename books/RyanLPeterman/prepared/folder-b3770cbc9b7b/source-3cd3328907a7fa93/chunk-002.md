Chunk 2; segments 397–787. Start may repeat the previous chunk for context.

# Google DeepMind Distinguished Eng (L9): How To Land a Job at a Frontier Lab | Vlad Feinberg

Source ID: source-3cd3328907a7fa93
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Google_DeepMind_Distinguished_Eng_(L9)_How_To_Land_a_Job_at_a_Frontier_Lab_Vlad_Feinberg_en.txt
Video: https://www.youtube.com/watch?v=cDyi91onoJ8

[L406] [15:27.56] methodology is available because you
[L407] [15:29.56] really won't have
[L408] [15:31.08] a lot of hope of improving upon the
[L409] [15:33.04] methodology if you don't understand
[L410] [15:34.28] what's there already. So, so I think I
[L411] [15:36.80] like mentioned earlier, one of the
[L412] [15:38.60] things that my team works on is is
[L413] [15:41.36] distillation.
[L414] [15:42.76] And in order to
[L415] [15:45.40] advance our
[L416] [15:48.04] understanding in uh distillation for
[L417] [15:50.76] large language models,
[L418] [15:52.92] you have to have a good understanding of
[L419] [15:54.92] like what we're trying to do with LLMs.
[L420] [15:57.92] And uh just to give a cursory overview
[L421] [16:01.12] here, the name of the game for LLM
[L422] [16:04.52] research is
[L423] [16:06.92] especially in pre-training is uh is
[L424] [16:08.88] scaling laws. And so,
[L425] [16:11.24] what are scaling laws? People focus a
[L426] [16:13.12] lot about like, you know, this power law
[L427] [16:15.04] structure and the fact that like you,
[L428] [16:17.96] you know, have this and that exponent,
[L429] [16:19.52] but like what matters is less so the
[L430] [16:21.92] functional form. What matters is
[L431] [16:24.16] for a given recipe of scaling up your
[L432] [16:27.20] LLM, so as you invest more and more
[L433] [16:29.76] flops into the pre-training run of an
[L434] [16:31.48] LLM,
[L435] [16:32.88] you have to be able to predict what the
[L436] [16:35.24] final test loss of this LLM is going to
[L437] [16:39.16] be. And why why do we care about this
[L438] [16:41.72] question? Why do we care about
[L439] [16:42.72] predicting what our uh generalization
[L440] [16:44.88] error is?
[L441] [16:46.08] In the classical machine learning world,
[L442] [16:49.76] like say we're trying to, you know, win
[L443] [16:52.00] ImageNet.
[L444] [16:53.68] We have our test loss, which is our
[L445] [16:55.56] classification uh error for, you know, a
[L446] [16:58.40] thousand different classes and uh you
[L447] [17:00.92] run your VGG or your ResNet proposal to
[L448] [17:04.32] get that uh classification error. That's
[L449] [17:06.80] an estimate of how well that model does
[L450] [17:08.60] at classifying
[L451] [17:10.72] amongst those thousand classes uh
[L452] [17:13.08] various different images.
[L453] [17:15.12] We can estimate how good our method's
[L454] [17:16.76] going to be by taking a validation set
[L455] [17:19.12] and then whenever we have an
[L456] [17:20.20] architecture idea for a neural net, we
[L457] [17:21.88] just train it and then we
[L458] [17:24.32] uh do a bunch of uh validation set runs
[L459] [17:26.76] and we get a cross-validation error that
[L460] [17:28.56] is itself an estimator of our final test
[L461] [17:30.56] error. And so in this way you can just
[L462] [17:32.00] iterate on different ideas
[L463] [17:34.28] uh through this process.
[L464] [17:35.84] But what's different in LLM world is
[L465] [17:38.40] every single time you go up for a
[L466] [17:39.84] pre-training run, you're about to put in
[L467] [17:42.36] more flops into this run than you've
[L468] [17:43.92] ever done before.
[L469] [17:45.72] So, it's in some sense like a one-shot
[L470] [17:48.04] version of this ImageNet problem. You
[L471] [17:49.52] never get to see the full ImageNet
[L472] [17:51.80] training data set. You have to practice
[L473] [17:53.84] on MNIST and then CIFAR and then maybe
[L474] [17:55.92] based off of those, you try to come up
[L475] [17:58.20] with a method that just works right off
[L476] [17:59.76] the bat on ImageNet. And if you were to
[L477] [18:02.96] just do that by itself, as I'm sure many
[L478] [18:05.88] people have tried, uh like certainly
[L479] [18:07.56] when I was learning how to do all of
[L480] [18:08.88] those different things, you get
[L481] [18:10.20] something, it works really great on
[L482] [18:11.60] MNIST, it maybe even works on CIFAR, and
[L483] [18:13.88] then all of a sudden it breaks on
[L484] [18:15.00] ImageNet.
[L485] [18:16.40] You'll find out that like things don't
[L486] [18:18.56] just generalize easily across scale like
[L487] [18:20.40] this. And
[L488] [18:22.52] so much of what we do for LLMs is coming
[L489] [18:25.12] up with recipes, where a recipe is this
[L490] [18:28.40] function that goes from number of flops
[L491] [18:30.60] you'd like to train on to a training
[L492] [18:32.56] routine for this LLM. And if you can
[L493] [18:35.60] couple this recipe with a prediction
[L494] [18:38.08] rule that can predict accurately what
[L495] [18:40.40] your LLM accuracy is going to be, then
[L496] [18:43.24] um you're able to make decisions about
[L497] [18:45.92] how to improve your recipe cuz you can
[L498] [18:47.60] use that prediction.
[L499] [18:49.32] That is all a ton of context on what uh
[L500] [18:52.20] LLM research looks like in general, but
[L501] [18:54.96] that's like a an understanding that we
[L502] [18:57.00] got to, that we even thought was
[L503] [18:59.12] feasible, thanks to so much uh
[L504] [19:02.84] initial LLM scaling work that we've seen
[L505] [19:06.24] across the Kaplan paper, across
[L506] [19:09.00] Chinchilla.
[L507] [19:11.16] Since those two papers, there's been a
[L508] [19:13.72] lot more work in terms of like what
[L509] [19:15.64] other factors are there beyond uh number
[L510] [19:17.92] of params and um
[L511] [19:20.28] number of tokens that you train on that
[L512] [19:22.52] influence your prediction accuracy.
[L513] [19:25.12] Uh like number of unique tokens for
[L514] [19:26.64] instance.
[L515] [19:28.12] But like I would say like those two
[L516] [19:31.08] foundational papers for LLMs, uh those
[L517] [19:33.88] are informed by uh an even even longer
[L518] [19:36.48] line of uh different uh scaling works
[L519] [19:39.64] going back to like say the original uh
[L520] [19:42.20] GPTs and then Google has had a ton of
[L521] [19:44.48] scaling work across its Palm papers.
[L522] [19:47.36] This is just a set of works that have
[L523] [19:51.44] informed that viewpoint that I described
[L524] [19:53.40] earlier that
[L525] [19:55.84] you you kind of just need to build up by
[L526] [19:58.36] having gone through that literature
[L527] [20:00.20] review yourself.
[L528] [20:01.60] >> If you were for instance, if uh
[L529] [20:04.08] you were trying to pick someone that was
[L530] [20:05.76] going on your team and the the way that
[L531] [20:09.12] you would judge their fitness to help
[L532] [20:11.00] you push the frontier is their
[L533] [20:13.80] understanding of the frontier including
[L534] [20:16.12] the existing literature which requires
[L535] [20:18.56] all these prerequisite. I think you
[L536] [20:20.72] called it mathematical maturity in your
[L537] [20:22.76] post.
[L538] [20:23.84] >> Yeah, so I think I I
[L539] [20:26.52] I think it's
[L540] [20:28.52] easy to read and understand those papers
[L541] [20:30.56] once you have mathematical maturity.
[L542] [20:33.24] So I guess the ones I mentioned in
[L543] [20:35.96] particular nowadays they're table
[L544] [20:37.56] stakes. So I I would expect candidates
[L545] [20:39.44] to be familiar with them. Um
[L546] [20:42.84] I think um
[L547] [20:45.20] the the general skill set is being able
[L548] [20:47.80] to dive in to
[L549] [20:49.80] uh a paper of that level and then
[L550] [20:52.16] understanding it.
[L551] [20:54.28] Uh
[L552] [20:55.16] you know being able to take a research
[L553] [20:57.48] idea uh from a paper and implementing it
[L554] [21:01.32] yourself. Like that's that's just a a
[L555] [21:04.04] very important skill set to be able to
[L556] [21:05.52] have. Like we get, you know,
[L557] [21:08.40] all sorts of uh uh different ideas
[L558] [21:10.44] presented, you know,
[L559] [21:12.40] they might not all directly apply to our
[L560] [21:14.80] domain, but if you can deeply understand
[L561] [21:16.64] them, then you can iterate on them, and
[L562] [21:17.80] you can improve them inside of
[L563] [21:19.84] uh inside of our domain. And so, when we
[L564] [21:22.52] assess for people who can work with the
[L565] [21:26.40] mathematical concepts in these machine
[L566] [21:28.00] learning papers, that's that's I guess
[L567] [21:30.04] the the key skill there that would be
[L568] [21:32.24] evidence that you can go pick up this
[L569] [21:34.68] arbitrary paper and see to what extent
[L570] [21:37.96] these ideas carry over uh in the Google
[L571] [21:40.24] setting.
[L572] [21:41.40] >> This probably won't be exhaustive, but
[L573] [21:43.24] I'd be curious to hear other domains
[L574] [21:46.64] that maybe people could dig into to see
[L575] [21:49.80] what kind of matters in frontier AI
[L576] [21:51.68] research. So, you'd mentioned
[L577] [21:53.88] distillation, you also mentioned
[L578] [21:55.32] kernels, it sounds like kernels are
[L579] [21:56.56] helpful everywhere. Um but are there
[L580] [21:59.28] other areas that come to mind if you
[L581] [22:00.72] were just raffle off areas that are not
[L582] [22:02.92] necessarily exhaustive?
[L583] [22:05.12] >> One thing that I think is is quite
[L584] [22:07.56] powerful is uh actually
[L585] [22:10.48] programming language research. So, by
[L586] [22:13.44] looking into how we can create
[L587] [22:15.52] abstractions at the programming language
[L588] [22:17.24] level, we could facilitate kernel
[L589] [22:19.08] development. I think ThunderKittens is a
[L590] [22:21.36] really good example of this. Like,
[L591] [22:23.24] coming up with an
[L592] [22:24.56] an abstraction that allows you to write
[L593] [22:26.36] kernels through four functions instead
[L594] [22:28.40] of arbitrary globs of C++ code uh
[L595] [22:31.96] allows you to move really quickly uh in
[L596] [22:35.24] uh developing algorithms that fully
[L597] [22:37.68] utilize hardware.
[L598] [22:40.08] So, like, it it at that point it it's um
[L599] [22:44.36] it's not about the PL research itself,
[L600] [22:45.88] it's about having a passion for,
[L601] [22:49.36] you know, these kind of programming
[L602] [22:50.36] language abstractions and and working
[L603] [22:52.20] with uh low-level hardware.
[L604] [22:54.48] Um you know, uh people who, you know,
[L605] [22:57.88] are interested in and will
[L606] [23:00.04] try to work with like cute DSL, the this
[L607] [23:02.92] kind of thing where there's a lot of
[L608] [23:05.20] hardware specific domain specific
[L609] [23:07.40] languages. Uh one other thing that comes
[L610] [23:09.60] to mind besides PL and uh scaling law
[L611] [23:13.48] literature would be reinforcement
[L612] [23:15.80] learning literature.
[L613] [23:17.24] Uh so in particular ever since uh RLHF,
[L614] [23:21.28] uh I think we've seen that
[L615] [23:23.36] deep RL algorithms uh like PPO do have a
[L616] [23:27.16] place in production systems and you
[L617] [23:29.48] know, there was a time where
[L618] [23:31.44] that was in question, but uh now it's
[L619] [23:34.16] you know,
[L620] [23:35.24] uh pretty unanimous that we see these
[L621] [23:37.28] kind of algorithms applied to real
[L622] [23:39.36] production systems and
[L623] [23:42.24] the uh theory behind that uh you kind of
[L624] [23:46.40] have to start with the basics for
[L625] [23:48.80] reinforcement learning and work their
[L626] [23:50.80] way up to
[L627] [23:52.84] you know, the myriad uh value-based
[L628] [23:55.20] methods and and uh policy gradient
[L629] [23:57.36] methods that we have today.
[L630] [24:00.32] That's that's another domain that I
[L631] [24:01.92] think is just like a very rich
[L632] [24:03.12] literature tree to crawl. Um and then
[L633] [24:06.60] for more of the back end engineer folks,
[L634] [24:08.64] just beyond just the kernels themselves,
[L635] [24:11.92] there's I think
[L636] [24:13.64] a pretty fun overlap between distributed
[L637] [24:16.16] systems and optimization work where uh
[L638] [24:19.92] figuring out how to design neural net
[L639] [24:23.08] training algorithms that allow for
[L640] [24:26.20] training across
[L641] [24:28.24] many GPUs.
[L642] [24:31.08] There's all sorts of fun challenges
[L643] [24:34.08] between asynchronicity, how up-to-date
[L644] [24:37.04] your gradients are,
[L645] [24:38.88] how
[L646] [24:40.84] pipelining affects the staleness,
[L647] [24:43.44] uh all of these system choices that you
[L648] [24:45.36] could make in your training algorithm
[L649] [24:47.68] design will impact convergence and the
[L650] [24:49.64] final quality of your neural net. And uh
[L651] [24:52.00] those are things that can be analyzed
[L652] [24:53.36] independently of the LLM setting
[L653] [24:55.48] uh and have been for a while. So,
[L654] [24:58.92] uh, you know, especially if you're kind
[L655] [25:00.12] of more infra-inclined, then having a
[L656] [25:02.56] good understanding of like,
[L657] [25:04.68] uh, how those different algorithms works
[L658] [25:06.28] work is a is a really good place to
[L659] [25:07.84] start.
[L660] [25:09.20] >> Do you see any difference between the
[L661] [25:11.68] the demands of the different frontier
[L662] [25:13.60] labs? So, for instance, if someone wants
[L663] [25:15.32] to work at DeepMind, is there like a
[L664] [25:17.64] particular area that you see DeepMind
[L665] [25:20.76] cares about more than Anthropic, for
[L666] [25:22.88] instance?
[L667] [25:24.08] >> I think in terms of the skill set, it's
[L668] [25:25.80] probably pretty similar. Yeah, I think I
[L669] [25:28.20] think there's maybe differences in like
[L670] [25:31.96] business strategy and, uh, you know, the
[L671] [25:36.08] set of offerings that's a function of,
[L672] [25:40.00] uh, the specialties of the labs and,
[L673] [25:43.52] uh, like the kind of different, uh, you
[L674] [25:45.92] know, customers that the labs could
[L675] [25:47.04] have. Uh, but
[L676] [25:49.48] uh, I would say that there's there's
[L677] [25:51.76] quite a lot of overlap between the labs
[L678] [25:53.92] in terms of what people look for. And
[L679] [25:56.04] like, yeah, like when I posted, uh, my
[L680] [25:58.08] post, you would you would see like, you
[L681] [25:59.64] know, people from both OpenAI and
[L682] [26:01.64] Anthropic saying like, yeah, like we
[L683] [26:03.40] agree with this advice. And so, you
[L684] [26:05.04] know, I think, um,
[L685] [26:07.52] that that's just a little bit of
[L686] [26:08.72] evidence towards that.
[L687] [26:09.96] >> I think one reason for the the huge
[L688] [26:12.08] demand for wanting to go closer to AI
[L689] [26:14.56] research is because people are thinking
[L690] [26:17.36] of software engineering is not going to
[L691] [26:18.92] be as important in the future. Is there
[L692] [26:21.08] a similar thought in when it comes to
[L693] [26:23.72] research where LLMs is also going to
[L694] [26:26.28] handle a lot of that work as well, so
[L695] [26:28.68] there's no reason to favor AI research
[L696] [26:31.36] versus software engineering?
[L697] [26:33.04] >> Um,
[L698] [26:34.28] so I think the the research skill set is
[L699] [26:36.84] going to become increasingly important.
[L700] [26:39.92] Uh, so I would say like being able to
[L701] [26:42.84] handle stochastic components in the
[L702] [26:45.80] planning of your work
[L703] [26:47.76] is is just going to be a larger and
[L704] [26:50.96] larger part of how we approach our jobs.
[L705] [26:56.20] Figuring out how to leverage AI in
[L706] [26:58.96] whatever thing you work on, which
[L707] [27:01.28] doesn't even have to be software
[L708] [27:02.40] related, is just an important muscle to
[L709] [27:04.64] start building right away.
[L710] [27:06.76] Um because these components aren't
[L711] [27:08.64] deterministic and thinking about how do
[L712] [27:10.64] I construct systems around these LLMs to
[L713] [27:13.28] do my job more effectively,
[L714] [27:15.24] uh that's that's going to be the thing
[L715] [27:16.68] that sets you apart in the future. And I
[L716] [27:18.60] think that's true no matter what you're
[L717] [27:19.64] going to be doing. Look, I think I think
[L718] [27:21.92] there's there's fud everywhere,
[L719] [27:23.88] especially with with some of the
[L720] [27:25.76] approach to marketing that some people
[L721] [27:28.00] have in terms of AI. It's fud that is
[L722] [27:31.44] being intentionally leveraged. And so, I
[L723] [27:34.12] I feel like
[L724] [27:36.16] people should really just focus on
[L725] [27:37.76] themselves and and trying to uh be more
[L726] [27:40.60] productive themselves.
[L727] [27:42.32] I I don't think that like AI is going to
[L728] [27:45.88] replace all of our roles. And so, the
[L729] [27:48.16] reason for that is that
[L730] [27:51.24] one of the important aspects of what we
[L731] [27:54.32] do as humans in an organization, which
[L732] [27:56.88] is really this web of trust,
[L733] [28:00.76] from like, you know, this organization
[L734] [28:03.92] that is, you know, this pool of
[L735] [28:05.12] resources and this pool of people that
[L736] [28:06.96] manages these resources.
[L737] [28:09.12] One of the important things that we do
[L738] [28:11.16] is we allocate those resources towards
[L739] [28:13.44] cer- certain goals.
[L740] [28:15.04] And um
[L741] [28:17.76] even when
[L742] [28:19.20] we can accelerate
[L743] [28:21.08] our execution,
[L744] [28:23.00] there's an element of making decisions
[L745] [28:25.96] around how we allocate these resources
[L746] [28:28.12] that will always be
[L747] [28:30.48] something that needs to be attributable
[L748] [28:31.84] to a human making that decision.
[L749] [28:34.16] And uh that's simply because
[L750] [28:36.92] you can't hand off blame to AI.
[L751] [28:39.92] So,
[L752] [28:41.12] we at this point have LLMs that really
[L753] [28:44.08] deeply understand law. And they could,
[L754] [28:45.92] you know, review your contract for you
[L755] [28:47.36] or something like that.
[L756] [28:48.92] But, they can't represent you in court
[L757] [28:51.28] because they can't be disbarred.
[L758] [28:53.92] And so, that's that's I think like a
[L759] [28:56.16] really, you know, sharp way that I might
[L760] [28:58.68] describe like, okay, this is why the
[L761] [29:00.76] legal profession will go on even though
[L762] [29:03.88] LLMs are really good at recalling
[L763] [29:06.04] precedent is
[L764] [29:07.88] you want to have someone who is
[L765] [29:10.20] responsible who can validate the output
[L766] [29:12.52] of AI to perform
[L767] [29:16.44] uh
[L768] [29:17.00] legal work more effectively for you
[L769] [29:19.72] rather than
[L770] [29:21.24] hand off
[L771] [29:23.88] your legal defense to an LLM.
[L772] [29:26.00] >> Yeah, I think the FUD, that was actually
[L773] [29:28.60] the original motivation for your post.
[L774] [29:30.76] >> Yeah, I mean, I I really think that the
[L775] [29:33.20] mindset that people should have is is a
[L776] [29:35.52] constructive one. And so, there was a
[L777] [29:38.48] tweet that I saw, I think by Didi, that
[L778] [29:41.00] was like some long-form, you know,
[L779] [29:44.24] fear-mongering about, you know, uh
[L780] [29:47.16] uh
[L781] [29:48.04] AI permanent underclass or something
[L782] [29:50.04] like that. And uh
[L783] [29:51.96] it's easy to get stuck in that loop, but
[L784] [29:54.64] I think the important thing to think
[L785] [29:58.16] about is like we all have agency over
[L786] [30:01.56] our future and we can start investing in
[L787] [30:05.20] uh skills that matter for tomorrow
[L788] [30:08.36] today. And
[L789] [30:10.68] um
[L790] [30:11.40] that's that's really
[L791] [30:13.92] the only thing you should be doing,
[L792] [30:15.24] right? Like, you know, worrying about it
[L793] [30:16.72] is not going to not going to help you.
[L794] [30:18.44] And so, part of why I wanted to write
[L795] [30:20.48] this post is is in response to that.
[L796] [30:23.72] Uh because it it it was something that I
