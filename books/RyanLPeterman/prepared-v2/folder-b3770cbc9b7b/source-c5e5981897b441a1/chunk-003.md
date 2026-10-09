Chunk 3; segments 655–986. Start may repeat the previous chunk for context.

# Meta Distinguished Eng (IC9): Influencing Engs, Failures, and Learnings | Adam Ernst

Source ID: source-c5e5981897b441a1
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Distinguished_Eng_(IC9)_Influencing_Engs,_Failures,_and_Learnings_Adam_Ernst_en.txt
Video: https://www.youtube.com/watch?v=YA_OYJF3Mmw

[L664] [22:11.52] could have a component script screen
[L665] [22:12.88] which had a native section. All this
[L666] [22:14.80] stuff, really cool features.
[L667] [22:17.04] And for me, it was a real learning
[L668] [22:19.12] experience because I learned that just
[L669] [22:20.80] because it was technically excellent
[L670] [22:22.72] didn't mean it was going to win. It
[L671] [22:25.68] checked all the boxes we needed in terms
[L672] [22:27.52] of interop and type safety, but it
[L673] [22:31.04] didn't win and didn't come close to
[L674] [22:32.56] winning because there were many other
[L675] [22:34.16] factors that I didn't take into account.
[L676] [22:37.52] So, a great example of writing a lot of
[L677] [22:39.28] code and doing a lot of technical work
[L678] [22:41.12] doesn't mean that it's going to win. I
[L679] [22:43.36] mean, if we were to kind of postmortem
[L680] [22:45.92] why it didn't win, what are the things
[L681] [22:48.40] that you did well and what are the
[L682] [22:50.40] things that maybe could have gone
[L683] [22:51.68] better?
[L684] [22:52.24] >> Um, I mean, doing well, I just mentioned
[L685] [22:54.40] it did check it checked all the
[L686] [22:55.92] technical boxes that we as in like the
[L687] [22:58.32] core product infra group cared about,
[L688] [23:01.12] right? Like it was type safe. It
[L689] [23:04.08] integrated with GraphQL and component
[L690] [23:06.08] kit and WHO, our existing native
[L691] [23:07.52] frameworks. It was birectional. So, you
[L692] [23:09.44] would never be suddenly cut off. There
[L693] [23:11.36] would never be a point where you're
[L694] [23:12.24] like, "Oh, I just need to embed this
[L695] [23:13.60] native component and I can't do it." No,
[L696] [23:15.60] you could always do it. The mistakes
[L697] [23:17.28] were number one, I wasn't really aiming
[L698] [23:20.80] at a particular target engineer, right?
[L699] [23:23.28] So, React Native was focused on like web
[L700] [23:25.44] engineers who wanted to write for
[L701] [23:26.64] mobile. Component kit was focused on,
[L702] [23:29.52] hey, we have iOS engineers that already
[L703] [23:31.44] know how to write iOS code. Let's let
[L704] [23:34.32] them write iOS code, but have excellent
[L705] [23:36.72] performance.
[L706] [23:38.40] Component script is like, hey, you can
[L707] [23:39.76] write JavaScript, but it's not React.
[L708] [23:41.84] So, like iOS engineers were like, I
[L709] [23:43.28] don't want to learn a whole new
[L710] [23:44.16] language. I don't want to learn
[L711] [23:45.12] JavaScript. And JavaScript engineers
[L712] [23:47.28] were like, I'll use React Native. I
[L713] [23:48.88] don't want to touch this like weird not
[L714] [23:50.88] React API. No thank you. So, we were
[L715] [23:53.84] kind of stuck. Number two is that like
[L716] [23:56.00] we on the product infrastructure group
[L717] [23:57.52] really cared about GraphQL. We were
[L718] [23:58.88] like, hey, we want data consistency
[L719] [24:00.64] everywhere. So, this framework needs to
[L720] [24:02.16] be based on GraphQL. But it turns out
[L721] [24:04.32] GraphQL can be kind of a pain sometimes,
[L722] [24:06.96] right? Especially at that time, GraphQL
[L723] [24:10.24] tooling was slow and a lot of uh a lot
[L724] [24:13.04] of hassle. We've fixed it a lot since
[L725] [24:15.20] then, but at the time it was bad. And so
[L726] [24:18.08] trying to build on top of this slow,
[L727] [24:21.60] janky native GraphQL stack really slowed
[L728] [24:23.76] us down. Meanwhile, there was another
[L729] [24:25.76] framework out there that was, you know,
[L730] [24:27.20] coming in with a server-driven sort of
[L731] [24:29.52] UI approach. And their solution was
[L732] [24:32.00] like, don't worry about data
[L733] [24:32.96] consistency.
[L734] [24:34.48] What if we just didn't do it? And we
[L735] [24:36.08] were all horrified. were like, "What?
[L736] [24:37.44] You don't have data consistency?" So, if
[L737] [24:39.36] you like a post on one screen and you go
[L738] [24:41.04] to another screen, it won't show you
[L739] [24:42.56] that the post is liked. And the answer
[L740] [24:45.20] was yes. 60% of the time, 80% of the
[L741] [24:48.72] time, products just don't care. And for
[L742] [24:50.72] the 20% that do care, you could hack
[L743] [24:52.96] something in there that makes it work.
[L744] [24:54.80] So, we were pretty horrified by not
[L745] [24:56.24] using GraphQL, but it that was a huge
[L746] [24:58.40] advantage if you could just skip all
[L747] [25:00.48] that stuff. But, I refused to compromise
[L748] [25:02.40] and that was a problem. And then
[L749] [25:04.00] finally, I went really wide. I was like,
[L750] [25:06.24] "All right, I'm just going to talk to
[L751] [25:07.28] all engineers, all mobile engineers, and
[L752] [25:09.76] be like, you guys should all try out
[L753] [25:10.96] component script." And this meant that I
[L754] [25:12.88] got little pings of interest all over
[L755] [25:14.40] the place. Because there were a few
[L756] [25:16.16] engineers here and there that were like,
[L757] [25:17.28] "Sure, I'll try JavaScript. Sure, I'll
[L758] [25:18.80] try crossplatform." But there wasn't any
[L759] [25:21.36] individual team that was like, "Yes,
[L760] [25:23.36] this is how we want to write products
[L761] [25:25.20] from now on." And so that meant that it
[L762] [25:27.44] never went anywhere, right? Individual
[L763] [25:29.12] engineers would try individual little
[L764] [25:30.64] things here and there, but that was not
[L765] [25:32.16] going to get any momentum. Funny thing
[L766] [25:34.16] was just when I finally pulled the plug
[L767] [25:36.00] on component script the group's team was
[L768] [25:37.68] like oh we just decided we were going to
[L769] [25:39.12] go all in on component script and I was
[L770] [25:40.56] like oh man no [laughter] u but even
[L771] [25:42.88] that would not have been enough momentum
[L772] [25:44.40] right it was too little too late so you
[L773] [25:46.32] wrote about this retrospection it's you
[L774] [25:48.64] know very detailed one of the best you
[L775] [25:50.88] know retrospectives I've I've read why
[L776] [25:53.60] did you publish that so publicly what
[L777] [25:57.28] was the motivation behind it
[L778] [25:59.52] >> I don't recall it might have been
[L779] [26:02.00] encouraged that I write it, but I
[L780] [26:03.76] certainly wanted to write it. It was
[L781] [26:04.96] cathartic to talk about what went wrong.
[L782] [26:07.52] And even at the time, I had a
[L783] [26:09.36] reputation, right? People who knew who I
[L784] [26:11.04] was. So, everyone would always be like,
[L785] [26:12.32] "Hey, how's that component script thing
[L786] [26:13.68] going?" And the postmortem was a
[L787] [26:15.28] convenient way for me to rip the
[L788] [26:16.56] band-aid off and be candid about, "Hey,
[L789] [26:18.40] it didn't work and here's why." And not
[L790] [26:20.08] have to constantly rehash that
[L791] [26:22.00] conversation over and over and over. Um,
[L792] [26:24.32] but also I hope that it would influence
[L793] [26:26.72] the way that people did stuff at the
[L794] [26:28.24] company in the future, right? Like
[L795] [26:29.60] hopefully no one made the same mistake
[L796] [26:31.04] after that if they read my postmortem or
[L797] [26:32.88] at least they were aware of what they
[L798] [26:34.16] were walking into. And you know in this
[L799] [26:36.08] case you drove a very ambitious project
[L800] [26:39.12] and it did fail in the end when it comes
[L801] [26:42.08] to performance reviews in a half where
[L802] [26:44.64] something like this is happening or a
[L803] [26:46.24] year where something like this is
[L804] [26:47.36] happening. How does that play out and
[L805] [26:49.76] should people be worried about you know
[L806] [26:52.08] their projects getting cancelled or
[L807] [26:53.76] things like that?
[L808] [26:54.72] >> The thing that made me realize it needed
[L809] [26:56.24] to be cancelled is that I got a meets
[L810] [26:57.92] most. So performance did its job there.
[L811] [27:00.48] >> My manager at the time did the right
[L812] [27:02.72] thing and was like this is not working.
[L813] [27:04.72] >> He was also a new manager for me. So I
[L814] [27:06.96] think he like
[L815] [27:08.64] >> could see it with fresh eyes and be like
[L816] [27:10.24] this is not going to work. And then when
[L817] [27:13.04] I did cancel it, I like to think I did
[L818] [27:15.28] it in the right way, which is there were
[L819] [27:17.12] products and features written in
[L820] [27:18.80] component script and I helped those
[L821] [27:20.08] teams migrate back to native code or to
[L822] [27:22.16] react native or whatever they wanted and
[L823] [27:24.96] I completely deleted the framework. I
[L824] [27:26.72] didn't weave it as like, you know, oh,
[L825] [27:29.28] this one product is still on component
[L826] [27:30.88] script, so we have to weave it around
[L827] [27:31.84] forever and someone will have to clean
[L828] [27:33.28] it up someday. No, I was like, I'm
[L829] [27:35.36] driving this all the way and I'm
[L830] [27:36.40] deleting the code is going to be gone
[L831] [27:37.68] from the repo, which I think garnered
[L832] [27:39.44] some goodwill because it showed others
[L833] [27:41.60] this is the right way to clean up after
[L834] [27:42.96] your mess. Um, so I feel like I got in
[L835] [27:46.08] if anything a positive bump after the
[L836] [27:48.00] fact, right? Like there was enough
[L837] [27:50.48] relief of like, all right, this showed
[L838] [27:52.00] people how to wind up wind down a
[L839] [27:53.92] project that isn't working out. and he
[L840] [27:55.84] posted publicly about it show talking
[L841] [27:58.24] about the lessons learned and there's no
[L842] [28:00.16] mass left behind. So if anything I feel
[L843] [28:02.40] like it helped in the in the immediate
[L844] [28:04.72] aftermath. So if anyone is like staring
[L845] [28:06.32] down the barrel of like I think my
[L846] [28:07.76] framework's not going well but I'm
[L847] [28:09.36] afraid to kill it. You might get more
[L848] [28:10.64] goodwill from killing it responsibly
[L849] [28:12.72] than just like dragging it out and
[L850] [28:14.56] constantly waiting until it's too late.
[L851] [28:17.60] Were there signs that like looking back
[L852] [28:20.48] you could have maybe avoided some of the
[L853] [28:23.44] pain of I don't know meets most or you
[L854] [28:26.08] know kind of like it going on as long as
[L855] [28:28.08] it did.
[L856] [28:28.96] >> Yeah. I mean look there were there was
[L857] [28:31.36] it was a two-year project and for the
[L858] [28:32.96] last year I knew it wasn't going right
[L859] [28:34.72] and I should have listened to my gut,
[L860] [28:36.16] right? I there were some literally
[L861] [28:37.68] sleepless nights. Not a lot but like
[L862] [28:39.60] some where I was like this is it doesn't
[L863] [28:40.96] feel right. It's not going well. I don't
[L864] [28:42.48] understand what to do. And I'm a coding
[L865] [28:45.60] machine. So my reaction was I just need
[L866] [28:47.12] to write more code. I just need to help
[L867] [28:48.88] more features convert and it'll suddenly
[L868] [28:51.12] take off. And I should have listened
[L869] [28:52.48] instead to that part of my gut that was
[L870] [28:55.12] telling me this is not going to work
[L871] [28:56.32] out. Just go do something you love and
[L872] [28:58.64] find a different way to have impact and
[L873] [29:01.04] uh that would have been much better for
[L874] [29:02.64] me in the short and long run.
[L875] [29:04.80] >> You said before that you know for sure
[L876] [29:07.20] you you never wanted to try management
[L877] [29:09.36] and it was not right for you. Um, for
[L878] [29:11.76] someone who's considering that kind of
[L879] [29:13.20] decision, how did you know that
[L880] [29:15.52] management's not right for you?
[L881] [29:17.36] >> I like writing code. I really like
[L882] [29:18.96] writing code a lot. And as a manager,
[L883] [29:21.20] you can't write codes. So, I mean, for
[L884] [29:22.40] me, it's a no-brainer, right? I'm also
[L885] [29:24.32] just I'm
[L886] [29:26.24] less good at the non-code related parts
[L887] [29:30.56] of the job. So, like driving alignment
[L888] [29:33.52] and writing docs, I'm just not good at
[L889] [29:35.44] that stuff. And so, for me, I'm like,
[L890] [29:37.12] yeah, I don't want to touch that. And
[L891] [29:38.48] finally, I feel like I'm very good at
[L892] [29:39.84] communication with other engineers in a
[L893] [29:41.76] technical role. Like I'm very good at
[L894] [29:43.12] like, hey, we need to solve this
[L895] [29:44.16] technical problem. Let's all get on the
[L896] [29:45.44] same page about how to solve it. I don't
[L897] [29:47.44] think I'm as good at doing that when I'm
[L898] [29:49.04] not quite when I'm more removed from the
[L899] [29:51.28] problem, right? Managers have to lot of
[L900] [29:52.56] do a lot of direction setting and
[L901] [29:56.16] influencing people without directly
[L902] [29:58.08] pointing to like this line of code is
[L903] [29:59.44] the problem and that I think I'm less
[L904] [30:01.28] good at. So for me, I always knew
[L905] [30:04.16] management is not for me. Uh but it
[L906] [30:06.16] depends on the person. Obviously, I'm a
[L907] [30:07.52] pretty extreme case.
[L908] [30:09.04] >> What about um picking the domain that
[L909] [30:11.04] you went with? So, from what I see in
[L910] [30:12.80] your career, it's almost entirely on the
[L911] [30:15.04] iOS side with some crossplatform work.
[L912] [30:18.08] Well, how did you align on iOS? And is
[L913] [30:20.72] that something that you feel strongly
[L914] [30:22.32] about being tied to or is that just
[L915] [30:24.96] where things have taken you?
[L916] [30:26.40] >> That's where things have taken me. I
[L917] [30:28.56] don't change around a lot. I've never
[L918] [30:30.16] really changed teams once at this
[L919] [30:31.84] company, right? like I've like been
[L920] [30:33.60] shifted on to different teams as part of
[L921] [30:35.44] reorgs, but I don't know. I just kind of
[L922] [30:38.24] roll with the punches and I like what
[L923] [30:39.44] I'm doing. I feel like I like the team,
[L924] [30:41.28] so why mess it up? I admire engineers
[L925] [30:44.00] that are like, you know what, I want to
[L926] [30:45.12] go see what this AI thing is about. I'm
[L927] [30:46.48] going to go check it out. Or like, oh
[L928] [30:47.76] man, I really want to go work on ARVR.
[L929] [30:50.00] That's not me. I knew I liked mobile and
[L930] [30:52.88] I felt like I was getting the right
[L931] [30:55.52] opportunities to work on stuff I cared
[L932] [30:57.12] about. So, I just kept rolling with it.
[L933] [30:58.96] And I think it has worked out really
[L934] [31:00.16] well for me because it allowed me to
[L935] [31:01.68] build deep knowledge expertise about how
[L936] [31:06.08] all different parts of our system work.
[L937] [31:07.92] Right? If you want to know the guts of
[L938] [31:09.28] the graphical codegen or value object
[L939] [31:11.84] generation or buck or all these things,
[L940] [31:13.84] I know what's up. And so it's really
[L941] [31:16.24] helped me get really deep in this
[L942] [31:18.16] particular domain. And that means I have
[L943] [31:19.60] a lot of knowledge about it that helps
[L944] [31:21.92] answer questions from others. Very
[L945] [31:23.84] useful. Would I do mobile if I was a
[L946] [31:26.96] brand new engineer today? Maybe not.
[L947] [31:28.64] Maybe I do AI because that seems like
[L948] [31:30.16] the hot stuff, right? Or I don't know
[L949] [31:31.44] what else. Uh but I don't feel too bad
[L950] [31:34.56] about sticking with it. You you talked
[L951] [31:36.56] about the technical depth. Let's say
[L952] [31:38.32] someone's goal was to be like you. They
[L953] [31:40.64] they really wanted to, you know, super
[L954] [31:43.12] aggressively pursue the high IC career
[L955] [31:45.84] path. They want to go IC9 or bust. Do
[L956] [31:48.88] you think that technical depth is better
[L957] [31:51.84] than breath for becoming the highest
[L958] [31:54.32] levels of uh senior IC? I I mean it
[L959] [31:57.04] depends on how you operate. I've seen
[L960] [31:58.64] lots of different engineers that operate
[L961] [32:00.00] in different ways. I will say I have
[L962] [32:01.60] breath and depth, right? As in like not
[L963] [32:03.52] that you know it's perfect. It's not
[L964] [32:05.68] like I only know mobile though, right?
[L965] [32:07.12] Like I know ex a lot about how buck
[L966] [32:08.96] operates. I know a lot about how uh
[L967] [32:11.36] GraphQL
[L968] [32:12.96] schema works. And so for me, the thing
[L969] [32:15.20] that helped me personally worked for me,
[L970] [32:17.68] maybe not for everyone, when I run into
[L971] [32:19.84] a problem, instead of being like, "All
[L972] [32:20.96] right, got to go talk to the GraphQL
[L973] [32:22.32] team." I'm like, "Screw it. I'm just
[L974] [32:23.92] going to figure out what the problem is.
[L975] [32:25.52] I'm going to dive eight levels deep into
[L976] [32:27.28] their codegen guts until I find the
[L977] [32:29.76] problem and then I'll either fix it
[L978] [32:31.60] myself and now I know GraphQL codegen or
[L979] [32:34.08] I will show up to the GraphQL team and
[L980] [32:35.60] I'll be like hey ran into this problem
[L981] [32:37.60] debugged it eight levels deep here's the
[L982] [32:39.36] problem how do I fix it which impresses
[L983] [32:42.16] the GraphQL team means that I'm not
[L984] [32:44.24] taking up all their time and I've
[L985] [32:45.84] learned something new about a new system
[L986] [32:47.52] and if you keep doing that enough then
[L987] [32:50.00] you will discover a lot about a lot of
[L988] [32:52.16] different systems and you'll understand
[L989] [32:53.36] them and that'll give you so much
[L990] [32:55.60] knowledge and so much it's like a
[L991] [32:57.28] superpower to be able to dive into all
[L992] [32:58.96] these systems that you now know. It's
[L993] [33:01.36] also organic, right? We talked before
[L994] [33:02.96] about code review and how if you just
[L995] [33:04.48] review code that organically gives you
