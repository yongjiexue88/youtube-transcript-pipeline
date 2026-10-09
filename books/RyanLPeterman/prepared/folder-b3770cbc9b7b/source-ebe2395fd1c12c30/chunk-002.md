Chunk 2; segments 343–686. Start may repeat the previous chunk for context.

# Mozilla Firefox CTO: Chrome vs Firefox and Distinguished Eng Promos

Source ID: source-ebe2395fd1c12c30
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Mozilla_Firefox_CTO_Chrome_vs_Firefox_and_Distinguished_Eng_Promos_en.txt
Video: https://www.youtube.com/watch?v=KhJgI9u47kI

[L352] [12:50.56] something in the address bar, they would
[L353] [12:51.92] end up on Google. And then Google would
[L354] [12:53.60] show these Firefox users an an ad that
[L355] [12:55.68] would say or a big banner directly on
[L356] [12:57.36] google.com, like not even on the search
[L357] [12:58.96] result page saying, "Download Chrome.
[L358] [13:00.72] It's better." And they always claimed
[L359] [13:03.52] that it was unintentional, but these
[L360] [13:05.52] things just kept happening over and
[L361] [13:06.96] over. And I do think that on a sort of
[L362] [13:08.64] organizational strategic level, it was
[L363] [13:10.08] unintentional. But the individual
[L364] [13:11.84] incentives of the people involved and
[L365] [13:14.08] what they got by doing this and then you
[L366] [13:16.00] know maybe fixing it in a in a release a
[L367] [13:18.24] couple weeks later you know they still
[L368] [13:20.56] won as far as their metrics were
[L369] [13:21.92] concerned. So that was one piece, but
[L370] [13:24.88] there was definitely another piece where
[L371] [13:27.28] Firefox
[L372] [13:29.04] had legitimately fallen behind. And part
[L373] [13:33.20] of this was that when Chrome came out,
[L374] [13:35.44] it had a lot of really interesting and
[L375] [13:39.28] new architectural innovations um that
[L376] [13:43.36] created gaps with Firefox. Some of these
[L377] [13:46.48] included having a multipprocess
[L378] [13:48.00] architecture um and they had a plug-in
[L379] [13:51.60] architecture like for things like Adobe
[L380] [13:54.80] Flash that was much more robust against
[L381] [13:57.52] stability issues and they had a very
[L382] [13:59.60] fast JavaScript engine. Firefox also had
[L383] [14:01.20] a fast JavaScript engine and we you know
[L384] [14:03.60] traded back and forth uh you know taking
[L385] [14:07.28] the performance crown but they had some
[L386] [14:09.52] real structural advantages and at the
[L387] [14:11.04] same time Mozilla made a big and
[L388] [14:13.84] ambitious bet in the early 2010s to try
[L389] [14:16.24] to build a mobile phone operating system
[L390] [14:19.20] uh because there was this sense that
[L391] [14:20.48] mobile is coming and both Android and
[L392] [14:22.96] iOS are potentially hostile platforms
[L393] [14:25.44] that are not going to allow Firefox to
[L394] [14:27.92] do what it did on desktop on their
[L395] [14:29.76] platforms.
[L396] [14:30.72] And the belief was that the only
[L397] [14:32.56] possibility was to create a new mobile
[L398] [14:34.48] operating system uh that was based on
[L399] [14:36.48] web technology. And you know there was
[L400] [14:38.96] something to that idea and there was
[L401] [14:40.96] quite a lot of interest from the
[L402] [14:42.16] industry a very surprising amount of
[L403] [14:43.44] interest and we had a lot of partners
[L404] [14:44.88] but ultimately it didn't work and the
[L405] [14:47.20] big bet that Mozilla made on Firefox OS
[L406] [14:50.00] created a lot of resource competition
[L407] [14:52.16] with the work that needed to happen to
[L408] [14:54.64] keep Firefox competitive exactly at the
[L409] [14:57.04] time when it was needed the most. And so
[L410] [14:59.04] Firefox really had a lot of um gaps with
[L411] [15:02.56] respect to Chrome. I think the
[L412] [15:04.00] multipprocess architecture was a big
[L413] [15:05.52] one. The stability issues particularly
[L414] [15:08.32] coming from Adobe Flash which was widely
[L415] [15:10.96] used particularly for streaming video
[L416] [15:12.96] which was becoming a thing. That was
[L417] [15:14.80] another big gap. And Firefox also had
[L418] [15:17.28] some legacy baggage around its uh
[L419] [15:20.40] browser extension API where the way that
[L420] [15:23.52] you would make a browser extension I
[L421] [15:24.64] mean the whole concept of browser
[L422] [15:26.40] extension really arose from the Firefox
[L423] [15:29.36] architecture where you could just inject
[L424] [15:31.28] anything anywhere and the Firefox
[L425] [15:34.24] application was written in JavaScript
[L426] [15:37.12] and markup and you could just modify it
[L427] [15:39.84] with an extension by just adding more
[L428] [15:41.28] JavaScript and more markup and more CSS.
[L429] [15:43.68] And this was really cool and that's
[L430] [15:45.68] where people first got the notion that
[L431] [15:47.04] you could configure and change your
[L432] [15:48.48] browser um and extend it with new
[L433] [15:50.00] functionality. But the problem was that
[L434] [15:52.08] there were no well- definfined
[L435] [15:53.04] interfaces. And so all of these
[L436] [15:56.88] extensions were depending on all of
[L437] [15:58.88] these internal details of how the
[L438] [16:00.32] browser worked. And anytime we change
[L439] [16:02.88] anything we would break an extension and
[L440] [16:04.96] so that was a very real and significant
[L441] [16:07.04] drag with respect to trying to
[L442] [16:09.76] architecturally modernize the browser.
[L443] [16:11.76] You mentioned prior to Google's funding,
[L444] [16:15.28] this was a group of a bunch of people
[L445] [16:17.68] that were working for free in many
[L446] [16:19.52] cases. I kind of curious because I
[L447] [16:22.00] haven't done a lot of open source stuff.
[L448] [16:24.08] What is the incentive structure? Why why
[L449] [16:26.80] would people spend so much time working
[L450] [16:28.56] for free on a project like this?
[L451] [16:32.16] So I think it probably varies but the
[L452] [16:35.68] world was quite different back then and
[L453] [16:38.80] open source there were not first of all
[L454] [16:41.04] a lot of opportunities for people to
[L455] [16:42.72] contribute to something major and
[L456] [16:44.88] meaningful right like these days much of
[L457] [16:47.36] the software stack that everybody uses
[L458] [16:49.52] many projects are open source but there
[L459] [16:51.28] were not so many of those back at the
[L460] [16:52.56] time and so I think that it was an
[L461] [16:54.96] interesting opportunity to have impact
[L462] [16:57.36] and I think for a lot of people like I
[L463] [16:59.52] mentioned Boris he literally got
[L464] [17:01.68] involved in Mozilla because he had no
[L465] [17:03.44] way to browse the internet in his dorm
[L466] [17:04.96] room. One option was he was like at MIT
[L467] [17:07.76] at the time I think and you know he
[L468] [17:09.52] could either VNC into some like Solaris
[L469] [17:11.68] thing with Internet Explorer 5 or he
[L470] [17:13.84] could use this build of Netscape that he
[L471] [17:15.60] downloaded that was just constantly
[L472] [17:16.80] crashing. And so he he got involved just
[L473] [17:19.04] because he wanted to fix something for
[L474] [17:20.96] himself and he had this vision of how he
[L475] [17:22.48] wanted it to be better for him. And then
[L476] [17:24.40] he realized that there were so many
[L477] [17:26.64] other people out there that were also
[L478] [17:28.24] looking for the same things and trying
[L479] [17:29.60] to fix this stuff. And once you dive
[L480] [17:31.84] into a codebase like this, it is just an
[L481] [17:34.08] amazing intellectual challenge because
[L482] [17:35.76] the codebase was just so vast and so
[L483] [17:38.00] complicated. And so he was like a math
[L484] [17:40.16] major, right? But this was in some ways
[L485] [17:42.56] like even harder. And I think that that
[L486] [17:46.56] um challenge was another major aspect.
[L487] [17:49.28] But I think the biggest aspect was the
[L488] [17:51.44] motivation of the Mozilla mission and
[L489] [17:53.52] what we were trying to achieve because
[L490] [17:56.56] the I think a lot of principles that
[L491] [17:58.80] people take for granted about you know
[L492] [18:00.40] how the web should work that it should
[L493] [18:01.76] be open and it should be interoperable
[L494] [18:03.20] that it shouldn't be controlled by one
[L495] [18:05.04] company and even that that about the
[L496] [18:07.44] internet itself right you know the
[L497] [18:09.04] Mozilla mission is about making sure
[L498] [18:12.08] that the internet is a global public
[L499] [18:13.60] resource that is open and accessible to
[L500] [18:15.28] all and I think if you grew up in the
[L501] [18:17.68] 90s when Microsoft oft was eating the
[L502] [18:19.60] world. That was not a given. That was
[L503] [18:23.36] not the dominant way of thinking about
[L504] [18:25.04] how technology platforms should work.
[L505] [18:27.12] And Mozilla had a vision of how it could
[L506] [18:29.12] be different. And it had a means of
[L507] [18:32.00] executing that vision, right? It wasn't
[L508] [18:33.44] just an advocacy organization arguing
[L509] [18:35.60] that tech companies should do something
[L510] [18:37.04] different. It was actually going out and
[L511] [18:39.20] doing something and succeeding and
[L512] [18:41.44] creating a browser that gave users
[L513] [18:44.64] choice to block popups and control over
[L514] [18:47.04] their experience and the ability to
[L515] [18:48.32] block ads and the ability to have tab
[L516] [18:49.76] browsing and all these things that they
[L517] [18:52.40] weren't getting before and creating that
[L518] [18:56.24] reality and making the world better in
[L519] [18:58.72] that way I think was very inspiring to a
[L520] [19:00.80] lot of people.
[L521] [19:02.00] >> Yeah. I'm kind of curious like you know
[L522] [19:03.52] once you got there I want to hear a
[L523] [19:05.60] little bit about the projects that
[L524] [19:07.04] you're working on and the various
[L525] [19:08.88] stories of things that happened in the
[L526] [19:10.80] early days. Are there any projects that
[L527] [19:12.88] you felt were particularly interesting
[L528] [19:15.20] or contributed to your career?
[L529] [19:17.52] >> Yeah, so I got started working on all
[L530] [19:20.48] sorts of things like I think as an
[L531] [19:22.24] intern that I worked on was the uh front
[L532] [19:26.24] end for the new mobile browser but this
[L533] [19:27.92] was before there was Android and iOS. So
[L534] [19:29.84] it was actually for like Nokia Mimo uh
[L535] [19:32.72] and that's what I started on. Then I
[L536] [19:34.96] started working on the graphics engine.
[L537] [19:36.72] I worked on the image rendering library.
[L538] [19:39.28] And there was very much a sense back
[L539] [19:40.56] then just because there was so much code
[L540] [19:42.32] that you know was largely unowned that
[L541] [19:44.80] as soon as you show up and you start
[L542] [19:46.16] working on something and you like fix
[L543] [19:47.36] one thing, you start looking around
[L544] [19:48.72] you're like hey who who owns this? And
[L545] [19:50.24] they're like you do now. And so I really
[L546] [19:52.72] I ended my first internship owning like
[L547] [19:54.72] quite a lot of code in the Firefox
[L548] [19:56.16] browser. And that felt to me like a
[L549] [19:57.84] really big and important responsibility
[L550] [19:59.28] to make sure that um you know this stuff
[L551] [20:01.92] went well. I think I was particularly
[L552] [20:05.44] motivated to work on the really like the
[L553] [20:09.92] hardest and gnarliest parts of the code.
[L554] [20:12.40] um the parts that felt most critical
[L555] [20:15.12] when you know after Chrome came out and
[L556] [20:18.00] then Firefox was coming back with its
[L557] [20:20.16] first counterattack of trying to build a
[L558] [20:23.04] browser that was more performance
[L559] [20:24.64] competitive right particularly around
[L560] [20:25.84] JavaScript. So Chrome launched with this
[L561] [20:28.00] JavaScript engine called V8 that was you
[L562] [20:30.48] know had a just in time compiler and it
[L563] [20:31.92] was very fast and we were intending to
[L564] [20:34.48] ship our own just in time compiler uh
[L565] [20:37.20] for our JavaScript engine but there was
[L566] [20:41.04] a lot of challenge at the end of
[L567] [20:42.64] actually getting this thing shipped
[L568] [20:44.16] particularly around this very
[L569] [20:45.76] complicated area of how the JavaScript
[L570] [20:48.48] engine talks to the rest of the system
[L571] [20:50.72] you know how the the bindings between
[L572] [20:52.08] the JavaScript and the DOM which were
[L573] [20:53.76] referred to as XP connect and so
[L574] [20:55.68] literally There were months of delay of
[L575] [20:57.68] getting Firefox 4 out the door because
[L576] [21:00.40] of all of the tangled web of that
[L577] [21:02.48] architecture and I, you know, also at
[L578] [21:06.16] the advice of Damon at the time decided
[L579] [21:08.24] to dive in and try to help make that
[L580] [21:10.00] stuff better. And so I ended up working
[L581] [21:12.08] on that code and the thing about that
[L582] [21:14.64] code was that it was very
[L583] [21:18.80] uh tied up in a lot of security
[L584] [21:20.40] considerations in the browser. When the
[L585] [21:23.68] browsers and the web were first
[L586] [21:26.00] designed, you know, JavaScript was
[L587] [21:27.60] famously designed in 10 days, people did
[L588] [21:29.76] not fully think through all of the
[L589] [21:31.44] security implications of this
[L590] [21:33.84] architecture. Uh, both in terms of the
[L591] [21:36.00] web platform and the browser itself. So,
[L592] [21:38.88] Firefox as a browser, one of the cool
[L593] [21:40.80] things about it was that all of the
[L594] [21:42.96] application on the front end was also
[L595] [21:44.88] written in markup and JavaScript. But
[L596] [21:47.28] all of that relied from a security
[L597] [21:49.28] perspective on making sure that a
[L598] [21:52.16] website would be properly isolated from
[L599] [21:55.44] touching other websites and from
[L600] [21:57.28] touching the browser replication itself.
[L601] [21:59.44] And this was all a very complicated mess
[L602] [22:01.84] of security enforcement in this
[L603] [22:03.84] DOMbinding code. And it was not perfect.
[L604] [22:07.68] And there was this cat-and- mouse game
[L605] [22:09.52] between people working on Firefox and
[L606] [22:12.40] this external community of security
[L607] [22:14.40] researchers who were constantly finding
[L608] [22:17.28] new ways to poke holes in this, right?
[L609] [22:18.88] And you do some very very clever thing
[L610] [22:20.48] with, you know, function.bind and you
[L611] [22:22.16] end up slithering up the prototype chain
[L612] [22:23.84] and suddenly you're like in the address
[L613] [22:25.92] bar and tab code. And once you do that,
[L614] [22:28.08] you know, the browser and perhaps the
[L615] [22:30.08] computer are compromised. And so there
[L616] [22:32.40] was um there were a number of
[L617] [22:33.76] researchers, there was one, I think
[L618] [22:35.44] their name was Mozbug RA4. We never
[L619] [22:37.60] learned what their actual name was. Uh
[L620] [22:39.92] rumor had it that they worked in they
[L621] [22:42.00] lived in a country where security
[L622] [22:43.44] research was illegal. But there was very
[L623] [22:45.68] much like a weekly back and forth
[L624] [22:47.76] between uh people at Mozilla working on
[L625] [22:50.32] Firefox and Mozbar 4 of new um potential
[L626] [22:54.40] paths of vulnerability. So Firefox 4
[L627] [22:57.84] definitely I think introduced a much
[L628] [23:00.16] more robust architecture and that was
[L629] [23:02.80] when I got involved with some of this
[L630] [23:06.40] stuff. But there started to be other and
[L631] [23:09.76] additional security researchers who
[L632] [23:11.20] showed up who were finding new ways to
[L633] [23:13.92] poke holes in it. And what really
[L634] [23:17.12] started to worry me was that there were
[L635] [23:19.68] certain categories of things that we
[L636] [23:21.84] didn't really have a way to fix in a
[L637] [23:24.72] robust manner. You know, we could put a
[L638] [23:27.04] band-aid over that particular part. We
[L639] [23:28.72] could wallpaper it over, but there were
[L640] [23:30.64] usually ways that you could apply the
[L641] [23:32.72] same attack in another part of the
[L642] [23:34.08] codebase. And
[L643] [23:37.12] I started to get pretty worried about
[L644] [23:38.72] this. And I launched a very large cross
[L645] [23:42.16] functional effort that I spent, you
[L646] [23:43.92] know, at least over a year on which I
[L647] [23:46.80] referred to as slaughterhouse. Um, and
[L648] [23:49.68] that was because, you know, it was a
[L649] [23:51.04] joke because there were these things
[L650] [23:52.00] called Chrome object wrappers that we
[L651] [23:53.52] needed to get rid of. Um, but there was
[L652] [23:55.36] generally a sense um that this could be
[L653] [23:57.36] a really big problem if this these types
[L654] [24:00.40] of exploits were to be weaponized in the
[L655] [24:02.16] wild uh before we did something about
[L656] [24:04.56] it. And there was one particular
[L657] [24:07.20] researcher who I worked with quite a bit
[L658] [24:09.60] um who was really good at identifying
[L659] [24:11.84] and finding these issues. And so what
[L660] [24:13.84] would happen was be these external
[L661] [24:15.04] researchers. They would send us
[L662] [24:16.32] something. They would file it in a
[L663] [24:17.68] confidential bug in Bugzilla and our bug
[L664] [24:19.36] tracker. And then we would look at it
[L665] [24:20.96] and be like, "Yep, this is a real
[L666] [24:22.16] issue." And then we had a bounty
[L667] [24:23.44] program, right, where we would pay them
[L668] [24:24.64] a small amount of money um as as a thank
[L669] [24:27.12] you and an incentive to uh bring it to
[L670] [24:29.20] us and, you know, not sell it on the
[L671] [24:31.84] black market. But the black market
[L672] [24:34.56] certainly paid more and sometimes there
[L673] [24:36.80] would be zero day exploits where you'd
[L674] [24:38.48] have to sort of jump on some new thing
[L675] [24:41.44] and fix it and ship uh a fix within you
[L676] [24:44.96] know 24 hours to make sure that users
[L677] [24:47.44] were protected. And sometimes
[L678] [24:51.20] these attacks got ahead of us. And so
[L679] [24:53.36] there was one situation where
[L680] [24:57.52] uh somebody flagged me that there was a
[L681] [24:59.60] zero day exploit in the wild um that had
[L682] [25:02.16] been discovered. I think it was on like
[L683] [25:04.00] Moscow Times.com and I was disassembling
[L684] [25:07.60] it and then I had this realization that
[L685] [25:09.92] like I knew who had written this exploit
[L686] [25:13.12] um because it was one of the security
[L687] [25:14.24] researchers that we work with and
[L688] [25:16.24] without thinking too hard I fired off an
[L689] [25:18.08] email to this guy being like hey like
[L690] [25:19.92] you're you're double crossing us right
[L691] [25:21.28] like you're not supposed to sell these
[L692] [25:22.80] things if you report them to us and he
[L693] [25:26.48] got back to me and the thing about
[L694] [25:27.44] security researchers is that they're
[L695] [25:28.72] extremely paranoid he's like no no no I
