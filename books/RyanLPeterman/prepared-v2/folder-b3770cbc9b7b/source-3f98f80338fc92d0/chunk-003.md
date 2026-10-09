Chunk 3; segments 656–987. Start may repeat the previous chunk for context.

# Instagram Senior Staff Eng (IC7): What Held Him Back, Redefining Expectations, Promo Stories

Source ID: source-3f98f80338fc92d0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_Senior_Staff_Eng_(IC7)_What_Held_Him_Back,_Redefining_Expectations,_Promo_Stories_en.txt
Video: https://www.youtube.com/watch?v=OXJHfb_lZII

[L665] [23:33.12] name suggests. So it's basically a lot
[L666] [23:35.60] of it is uh when you think about
[L667] [23:36.72] Instagram web basically what is the
[L668] [23:38.40] architecture of the website that we use
[L669] [23:40.56] to structure the code so that everybody
[L670] [23:42.64] who's building on Instagram web can be
[L671] [23:45.28] productive can iterate quickly can
[L672] [23:47.04] iterate with confidence that means
[L673] [23:48.80] there's the right level of safeguards
[L674] [23:51.20] type checking tests right manual and
[L675] [23:54.08] automated what have you uh and this is a
[L676] [23:56.88] space that I have always been interested
[L677] [23:58.88] in because it's a very leveraged area to
[L678] [24:00.96] work in and I also think the more senior
[L679] [24:03.68] you get the more you need to look for
[L680] [24:05.52] these leveraged areas that you can work
[L681] [24:08.56] in because at some point it becomes even
[L682] [24:10.24] if you're a coding machine it becomes
[L683] [24:11.52] quite hard to to deliver strong IC5
[L684] [24:14.48] strong IC6 strong IC7 level product
[L685] [24:17.36] impact because what does that even mean
[L686] [24:19.20] like what is what is an you know an IC7
[L687] [24:21.92] product impact quite high the
[L688] [24:23.84] expectations so I found this product
[L689] [24:25.92] infra to be uh an area that I find super
[L690] [24:28.96] interesting and conversely there's many
[L691] [24:31.36] engineers especially the very product
[L692] [24:32.96] focused ones
[L693] [24:33.92] who don't find it that interesting, who
[L694] [24:35.92] would much rather do the the actual
[L695] [24:38.08] product work, if you will. But yeah,
[L696] [24:39.60] I've spent a lot of time improving our
[L697] [24:42.00] our systems there.
[L698] [24:43.52] >> So, you mentioned leveraged. I think
[L699] [24:46.00] that's a really interesting concept. Can
[L700] [24:47.76] you explain the the idea of what you
[L701] [24:49.84] mean by leveraged?
[L702] [24:51.28] >> Yeah, we talk about this um a lot on our
[L703] [24:54.72] info teams, I think, when we talk about
[L704] [24:56.08] the pit of success. What is the right
[L705] [24:58.32] set of defaults or the right
[L706] [24:59.84] architecture that you can put in place
[L707] [25:02.08] so that somebody who is you know bright
[L708] [25:05.44] and well-intentioned but maybe doesn't
[L709] [25:07.20] have expertise in this area yet or maybe
[L710] [25:09.28] doesn't have a lot of experience working
[L711] [25:10.64] on the surface comes in and hopefully
[L712] [25:12.96] just does the right thing because the
[L713] [25:14.88] framework encourages the right uh way of
[L714] [25:17.44] building product or the right tools are
[L715] [25:19.60] in place to help uh with testing
[L716] [25:21.36] whatnot. One specific thing that that I
[L717] [25:24.00] did early on when I joined the Instagram
[L718] [25:25.84] web team was to test the reliability of
[L719] [25:29.12] the site uh specifically on the front
[L720] [25:30.88] end. So I'm not talking about the back
[L721] [25:31.84] end now. I'm talking specifically about
[L722] [25:33.20] the front end. So in in React we have
[L723] [25:35.68] this concept called error boundaries
[L724] [25:37.84] which you can imagine are like try catch
[L725] [25:40.40] statements about specific pieces of the
[L726] [25:42.64] UI. So you can basically fence a certain
[L727] [25:45.04] area of the UI and you can say if
[L728] [25:46.56] there's any rendering errors happening
[L729] [25:47.84] in this area render this fallback state
[L730] [25:50.72] when that happens. And the way I picture
[L731] [25:53.12] er rendering errors happening right when
[L732] [25:54.88] an error gets thrown it's almost like a
[L733] [25:57.12] little grenade that detonates and now
[L734] [26:00.00] the question is how aggressive is the
[L735] [26:01.84] blast radius how big is the blast radius
[L736] [26:03.68] when there's a little rendering error
[L737] [26:05.52] somewhere on the side in some area that
[L738] [26:07.68] isn't like super important for the page.
[L739] [26:10.08] Are you really happy like blowing up the
[L740] [26:12.32] entire page and just showing like oops
[L741] [26:14.00] something went wrong and taking down
[L742] [26:15.20] Instagram web? Probably not. You
[L743] [26:17.28] probably want to fence that. So I went
[L744] [26:18.80] in and had a lot of fun just opening the
[L745] [26:20.80] developer tools, clicking around
[L746] [26:22.48] different areas. Uh and we can trigger
[L747] [26:24.00] these errors in in any component we like
[L748] [26:25.92] just to feel out like what would happen.
[L749] [26:27.84] Yeah, this is the the reliability
[L750] [26:29.76] effort. You can like argue that this is
[L751] [26:31.92] maybe more like IC4 IC5 level work at
[L752] [26:35.76] this point. But as one of my previous
[L753] [26:37.68] managers said to me, usually there's an
[L754] [26:39.84] IC4, IC5, and IC6. And maybe even higher
[L755] [26:43.76] way to go about almost any problem. And
[L756] [26:46.00] in this case, you can obviously just add
[L757] [26:48.80] one error boundary in one place and call
[L758] [26:51.28] it done. At that point, you're probably
[L759] [26:52.72] doing more IC4 style work, right? Or you
[L760] [26:56.80] can do this work systematically where
[L761] [26:59.44] you audit the entire site. You do this
[L762] [27:01.36] in all places. You solve the problem
[L763] [27:02.80] comprehensively. you dedicate, I don't
[L764] [27:04.80] know, like a day or two or something
[L765] [27:06.00] like that to it. Maybe bring in one or
[L766] [27:07.76] two additional people and you just
[L767] [27:09.52] harden the entire site against these
[L768] [27:11.68] errors, even if they're not happening
[L769] [27:12.96] today, right? That I say I would say is
[L770] [27:15.36] more the the IC5 level expectation. But
[L771] [27:18.08] then you want to push that further
[L772] [27:19.36] because when you're IC6, you can either
[L773] [27:21.68] be a successful IC6 as a coding machine
[L774] [27:23.44] by just doing an ungodly amount of IC5
[L775] [27:25.76] work or you do IC6 level complexity. You
[L776] [27:28.80] take on IC6 level complexity. And um you
[L777] [27:31.84] can probably tell I have a lot of
[L778] [27:33.28] opinions on this topic. I I think this
[L779] [27:34.96] is very important to build reliable user
[L780] [27:36.64] interfaces. I spent some time writing
[L781] [27:39.44] everything down. Everything that I'm
[L782] [27:40.64] telling you right now, I spent some time
[L783] [27:42.00] writing that down in a big note that we
[L784] [27:44.48] can share internally. Teaching people
[L785] [27:46.64] about everything that I just said about
[L786] [27:48.32] like here's how you open the developer
[L787] [27:50.08] tools and here's how you trigger an
[L788] [27:51.60] error in a random place. And then I also
[L789] [27:54.32] took some time to to try and classify
[L790] [27:57.52] these errors and say okay what is what
[L791] [28:00.24] is the primary information on a screen
[L792] [28:02.40] what is secondary and what is tertiary
[L793] [28:04.48] and what do you want to do in each case.
[L794] [28:06.48] So how do you want to handle a primary
[L795] [28:08.56] piece of information missing because of
[L796] [28:10.08] an error? A secondary piece of
[L797] [28:11.28] information missing and a tertiary one
[L798] [28:12.72] missing. And I think that way you can
[L799] [28:14.64] have a lot of impact through setting
[L800] [28:16.80] direction and suddenly me spending this
[L801] [28:19.44] time helps the entire company. Anybody
[L802] [28:22.56] reading this note can now apply this to
[L803] [28:24.08] their own products that have nothing to
[L804] [28:25.28] do at all with with Instagram web. And
[L805] [28:27.20] now you can see how we go from fourle
[L806] [28:29.28] impact to five level impact to six level
[L807] [28:31.60] impact. If I'm understanding correctly,
[L808] [28:33.92] that's where the leverage was in the in
[L809] [28:35.84] the IC6 example was that you empowered
[L810] [28:39.12] others to do useful work on your behalf.
[L811] [28:43.28] Um they can go on and either prevent
[L812] [28:46.64] those issues from coming up in the
[L813] [28:48.16] future or fixing them themselves. And if
[L814] [28:50.80] you did that for 100 engineers, then you
[L815] [28:54.16] know it's just faster than you could
[L816] [28:55.68] have done it yourself,
[L817] [28:56.64] >> right? And it's it's scaled, right? I
[L818] [28:58.48] cannot possibly be expected to know all
[L819] [29:00.24] of the web products in the company and
[L820] [29:01.52] go in myself and and work on a product
[L821] [29:03.52] that, you know, doesn't even fall in my
[L822] [29:05.28] org. But there's there's other things
[L823] [29:06.88] you can do. You know just to complete
[L824] [29:08.16] this example you can think of adding uh
[L825] [29:10.40] lint rules to your codebase so that if
[L826] [29:12.64] you have a specific anti pattern that
[L827] [29:15.36] you can identify you can tell engineers
[L828] [29:17.76] right in their IDE before they even
[L829] [29:19.76] submit their diff tell them right in the
[L830] [29:21.52] editor like hey you're doing something
[L831] [29:23.12] we didn't find an error boundary that
[L832] [29:25.36] protects you from bad breakage you
[L833] [29:28.00] probably might want to add one here I
[L834] [29:29.76] see so and then in this case the tool is
[L835] [29:31.84] doing useful work on your behalf and
[L836] [29:33.44] it's helping you scale and that's
[L837] [29:35.44] expected of IC6 right And then I would
[L838] [29:38.72] say this problem is solved sufficiently
[L839] [29:40.72] well that I don't need to keep
[L840] [29:42.00] dedicating my time to it. I can move on
[L841] [29:43.68] to the next thing and maybe now that
[L842] [29:45.28] we've talked about reliability, right? I
[L843] [29:47.36] can start focusing on what performance
[L844] [29:50.00] next or something like that. Going back
[L845] [29:52.00] to your career story, it sounds like you
[L846] [29:53.44] came on to IG web super great uh like
[L847] [29:57.60] intrinsic motivation fit like you it's
[L848] [29:59.84] exactly the problems you want to solve.
[L849] [30:01.60] Great team, great culture and your
[L850] [30:03.92] performance showed as well. you were
[L851] [30:05.36] greatly exceeding even with the team
[L852] [30:07.36] switch which you know usually causes
[L853] [30:09.28] some thrash and then I saw that you
[L854] [30:11.12] started to work on threads web and you
[L855] [30:13.84] know I'm just so curious about all the
[L856] [30:15.76] stories behind that so yeah how did you
[L857] [30:18.80] start working on threads what's the
[L858] [30:20.32] story there
[L859] [30:21.12] >> threads web has been such an amazing
[L860] [30:24.32] journey honestly uh I'm not paid to say
[L861] [30:26.56] that it's just genuinely been one of the
[L862] [30:28.72] most exciting
[L863] [30:29.20] >> I'm not paid to [laughter]
[L864] [30:30.32] >> well I'm paid to work on it but I'm not
[L865] [30:32.16] paid to sit on the podcast and and tell
[L866] [30:34.16] everybody how how great it was like
[L867] [30:35.52] right
[L868] [30:36.40] >> um
[L869] [30:37.12] >> but seriously it's been a bit of a
[L870] [30:39.20] roller coaster in some way because it
[L871] [30:40.40] was an intense period of time but I look
[L872] [30:42.40] back at uh the time that I spent on
[L873] [30:44.48] threads web with the other engineers
[L874] [30:46.40] working working on threads web and I
[L875] [30:48.64] think collectively this is up until this
[L876] [30:51.04] point at least the best work we have
[L877] [30:52.88] done in in our careers and I again I I
[L878] [30:55.68] don't say this to try and brag about it
[L879] [30:57.60] it's just it's been such a a unique
[L880] [30:59.76] environment to see a zero to one app
[L881] [31:03.04] launch to be there from in my case
[L882] [31:05.44] almost the the very beginning I got
[L883] [31:07.04] involved uh a few weeks after the
[L884] [31:09.84] project had gotten kicked off. So it was
[L885] [31:11.04] all very secretive internally at the
[L886] [31:12.48] time. It's just something that you don't
[L887] [31:14.16] get to do statistically when you join a
[L888] [31:16.32] company like Meta. You know we don't
[L889] [31:18.08] create these new family of apps as we
[L890] [31:20.00] call them apps almost ever. We try
[L891] [31:23.20] different things. We create new products
[L892] [31:24.56] over the years. How'd you get recruited
[L893] [31:26.48] to the threads team? It was my manager
[L894] [31:28.72] reaching out to me and um and suggesting
[L895] [31:30.56] that hey there's this uh kind of hush
[L896] [31:32.80] hush project going on. A small group of
[L897] [31:35.60] people is trying something. I don't know
[L898] [31:37.04] a whole lot about it, but I'm happy to
[L899] [31:38.40] connect you if you're interested. I was
[L900] [31:40.00] interested at least wanted to hear what
[L901] [31:41.52] this is all about. Um got connected to
[L902] [31:43.84] the the hiring manager on threads who
[L903] [31:45.60] ended up being my my manager when you
[L904] [31:47.68] know I fully joined afterwards and we
[L905] [31:51.36] talked about what was required.
[L906] [31:53.84] Initially the scope was quite small that
[L907] [31:55.68] we thought about for web for threads
[L908] [31:57.12] web. Um I later helped grow that into
[L909] [32:01.20] more scope. Um initially it was all all
[L910] [32:04.16] relatively confined, relatively small I
[L911] [32:06.40] would say. But yeah I got involved and
[L912] [32:08.24] um got started working as the the only
[L913] [32:10.40] engineer on it for the first 6 to 8
[L914] [32:12.16] weeks. So the almost the first two
[L915] [32:14.24] months I was by myself working on web.
[L916] [32:16.72] And it's again not something that you
[L917] [32:18.16] usually get to do because it even feels
[L918] [32:20.72] a little bit weird. you know, we we have
[L919] [32:22.32] this big repository um that has most of
[L920] [32:25.60] our web code internally. And I sat down
[L921] [32:28.80] and I thought of a code name for the
[L922] [32:30.96] project because we we have to have these
[L923] [32:32.88] unique file names. So, you have to pick
[L924] [32:34.48] a a code name that's unique. Picked
[L925] [32:36.48] ended up picking the same one that they
[L926] [32:37.92] had picked on the the native apps side.
[L927] [32:40.08] And then I went rightclick new folder
[L928] [32:43.60] and typed in that code name and started
[L929] [32:45.68] from from there. And that's just a very
[L930] [32:48.16] very rare thing to be doing. And I'm I'm
[L931] [32:51.20] honestly I'm very happy and very glad
[L932] [32:52.96] that I got to see it from the very early
[L933] [32:54.80] days and I got to make some of these you
[L934] [32:57.04] know big decisions. Um in hindsight I
[L935] [32:59.84] kind of wish I had picked a different
[L936] [33:01.04] shorter code name. I have typed that
[L937] [33:03.28] name I don't know tens of thousands of
[L938] [33:05.04] times now. [laughter]
[L939] [33:06.88] Wish I had picked one that has slightly
[L940] [33:08.56] fewer characters in it. But here we are.
[L941] [33:10.88] >> You literally started threads from
[L942] [33:13.20] scratch. It's such an unusual project.
[L943] [33:16.32] >> It's very unusual and it's not something
[L944] [33:18.08] that was clear from the very beginning.
[L945] [33:19.76] Again, it is one of those direction
[L946] [33:22.08] setting decisions that you have to make
[L947] [33:23.60] at some point, but you want to make that
[L948] [33:25.28] decision well reasoned. You really want
[L949] [33:27.68] to be sure that this is the way you want
[L950] [33:28.88] to be going. Initially, when we were
[L951] [33:30.56] just uh I say we, at that point, it was
[L952] [33:33.04] just me. Um, initially when I was just
[L953] [33:35.60] starting to render, you know, something
[L954] [33:38.08] just get the first component to show up
[L955] [33:40.16] successfully on screen. I actually
[L956] [33:41.92] started in the Instagram web codebase
[L957] [33:44.72] and I just applied a little bit of CSS
[L958] [33:46.48] to hide everything that was on screen.
[L959] [33:47.92] But it was clear that this wasn't the
[L960] [33:49.28] way to go for threads, right? So at that
[L961] [33:51.44] point I decided, okay, the cleanest
[L962] [33:53.60] separation to prevent any like bleed
[L963] [33:56.24] over any any mix between the two was to
[L964] [33:59.52] just say, okay, let's just create a
[L965] [34:00.80] different folder. Let's create different
[L966] [34:02.00] components. Let's just make it a
[L967] [34:04.00] different surface, if you will. We
[L968] [34:05.60] didn't know the final product name at
[L969] [34:07.28] the time. We didn't know the final
[L970] [34:08.40] domain, but we knew it was going to be
[L971] [34:10.40] different as a surface from Instagram
[L972] [34:11.92] web. So, it's not like we added a tab to
[L973] [34:14.48] Instagram web. You know, at some point
[L974] [34:16.08] when, for example, reals got added, we
[L975] [34:18.24] just added one tab, but that's still on
[L976] [34:20.00] Instagram web. Uh, this was a a
[L977] [34:22.72] different surface entirely. You know, I
[L978] [34:24.72] saw that year you got, which is even the
[L979] [34:27.60] most impressive thing. You got another
[L980] [34:29.44] redefined expectations rating um promo
[L981] [34:32.56] to IC7. I imagine a large part of that
[L982] [34:36.00] was because of how successful Threads
[L983] [34:37.84] was and you know you were an
[L984] [34:39.60] instrumental part of that. Is is that
[L985] [34:42.08] the story behind the IC7 promo there?
[L986] [34:44.64] >> Yeah, ironically you would think that as
[L987] [34:47.68] you get more senior as you get higher up
[L988] [34:49.76] or at least maybe maybe I I thought that
[L989] [34:51.60] beforehand. You'd think that the writing
[L990] [34:54.32] yourself review for the performance
[L991] [34:55.68] cycle, the annual performance cycle
[L992] [34:57.12] would become harder because you have to
[L993] [34:59.76] justify your work in a different way and
[L994] [35:01.92] maybe it is less clearcut. There isn't
[L995] [35:05.20] as much a template of what a successful
[L996] [35:06.72] IC7 looks like versus a successful IC4.
