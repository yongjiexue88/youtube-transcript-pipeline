Chunk 2; segments 326–656. Start may repeat the previous chunk for context.

# Robinhood SWE Turned $1B+ Founder: Non-Linear Careers, Being Jaded About Promos, Startup Learnings

Source ID: source-5f8b9d8fe5f8ba39
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Robinhood_SWE_Turned_$1B+_Founder_Non-Linear_Careers,_Being_Jaded_About_Promos,_Startup_Learnings_en.txt
Video: https://www.youtube.com/watch?v=f4eeoetb8t4

[L335] [10:11.28] otherwise would and that could be like a
[L336] [10:13.04] pretty good heristic people use when
[L337] [10:14.24] they're deciding where to go.
[L338] [10:15.76] Definitely. And so you said you you
[L339] [10:18.40] started working at Robin Hood. You were
[L340] [10:20.48] expecting a lot of growth and it sounds
[L341] [10:22.88] like it was not what you expected. I
[L342] [10:25.44] went in thinking that I'd be able to
[L343] [10:26.96] have pretty fast career growth. And for
[L344] [10:29.20] context over there, um I think I
[L345] [10:31.20] honestly just joined a bit too late.
[L346] [10:32.72] Like by the time I started it was series
[L347] [10:34.32] D. the people that had joined around
[L348] [10:36.64] series A, series B time frame, I think
[L349] [10:39.04] they did end up having the kind of
[L350] [10:40.48] growth that I was hoping for, which is
[L351] [10:42.16] like moving up the ladder really
[L352] [10:43.68] quickly, becoming engineering managers
[L353] [10:45.28] or like even higher than that in like a
[L354] [10:47.28] 2 three year time horizon. Um, in my
[L355] [10:49.52] case, I joined and I think at that point
[L356] [10:52.72] it was already starting to manifest into
[L357] [10:54.80] more of like a big company type of
[L358] [10:56.88] progression. So, at my three-month mark,
[L359] [11:00.24] they were having performance reviews,
[L360] [11:01.52] but I couldn't participate in them
[L361] [11:02.80] because I joined like one or two weeks
[L362] [11:04.48] too late. So, I had to participate in
[L363] [11:06.32] the one six months after that. So, at my
[L364] [11:08.24] 9month mark, I like went through the
[L365] [11:10.24] entire perview process. And I've been
[L366] [11:11.76] like busting my ass for the 9 months
[L367] [11:13.36] before then. There were several days
[L368] [11:15.12] where I was working till like 2 a.m.
[L369] [11:16.64] just actually working. Um, and our on
[L370] [11:19.52] call rotation back then was also
[L371] [11:20.96] horrendous because there's this thing
[L372] [11:22.32] called overnight batch where after
[L373] [11:24.40] market closes each day, you need to do a
[L374] [11:26.40] bunch of stuff before market opens the
[L375] [11:28.08] next day. In our case, there was a lot
[L376] [11:30.48] of manual intervention that was
[L377] [11:31.76] required. Hopefully now it's fixed. So,
[L378] [11:34.08] if there's any Robin Node engineers
[L379] [11:35.44] listening, hopefully it's better for you
[L380] [11:37.20] now. Um, but back in our day, it was
[L381] [11:39.12] just horrendous. So, I mean, honestly,
[L382] [11:40.88] there were several times that it went to
[L383] [11:43.36] like 4:00 or 5:00 a.m. and it was like
[L384] [11:44.96] actually dangerously close to causing
[L385] [11:46.80] like a business issue for Al because if
[L386] [11:48.48] you're not done with the batch process
[L387] [11:49.68] by the time market opens the next day,
[L388] [11:51.28] there's like Yeah, definitely a lot of
[L389] [11:52.96] downside there.
[L390] [11:54.16] >> What is the batch pro like what do you
[L391] [11:55.60] need to actually do?
[L392] [11:56.48] >> So, there's things like uh trade
[L393] [11:59.36] settlement that needs to happen. And so
[L394] [12:00.48] you need to be working with a lot of
[L395] [12:01.52] different counterparties externally just
[L396] [12:03.20] to make sure that like everything like
[L397] [12:04.88] all the different parties have accounted
[L398] [12:06.40] for everything uh to be the same across
[L399] [12:09.60] all their systems. It's basically just a
[L400] [12:11.60] bunch of batch jobs need to run one
[L401] [12:13.04] after the other. But if any of them
[L402] [12:14.56] fail, you need to figure out why it
[L403] [12:16.00] failed and then fix it if there's like
[L404] [12:18.00] some kind of like issue from like the
[L405] [12:19.44] actual codebase side. Get it out and
[L406] [12:21.84] then move on to the rest of the process.
[L407] [12:23.68] So imagine that there's like some
[L408] [12:25.04] deployment that happen and there's like
[L409] [12:27.04] hundreds of different bad jobs. So there
[L410] [12:28.32] could be like a three four different
[L411] [12:29.68] deployments that happened that day.
[L412] [12:31.12] There might be two issues that got uh
[L413] [12:33.44] that got deployed and then these batch
[L414] [12:35.12] jobs failed at let's say 11 p.m. at
[L415] [12:36.88] night. You need to page the person who
[L416] [12:38.40] wrote that. They need to fix it. They
[L417] [12:40.00] need to like deploy the new code. Then
[L418] [12:41.60] you have to go through that process
[L419] [12:42.64] again and kind of just like go through
[L420] [12:44.80] with it. So I I do think that Robin
[L421] [12:46.88] Hood's code base has not been
[L422] [12:48.40] architected in the most kind of stable
[L423] [12:51.20] way possible and they did end up having
[L424] [12:53.20] a bunch of tech debt as a result of
[L425] [12:54.56] that. But yeah, I guess the core point
[L426] [12:56.80] was that I felt like I'd been working
[L427] [12:58.80] really hard and then I got like the
[L428] [13:00.96] performance rating which was the
[L429] [13:02.16] performance rating itself was like five
[L430] [13:03.44] out of five. So I'm like okay that's
[L431] [13:05.36] pretty atypical for people to get so I'm
[L432] [13:06.96] happy about that. But then there was
[L433] [13:08.64] like nothing else tied to that. There
[L434] [13:10.48] was like no promotion, no compensation
[L435] [13:13.04] change tied to that. And I was just like
[L436] [13:15.36] why why did I do this? Cuz when you're
[L437] [13:17.52] like 22 there's a lot of things you
[L438] [13:18.80] could be investing your time into. And I
[L439] [13:20.56] felt like if I had just been not
[L440] [13:22.48] investing so much time into work, I
[L441] [13:24.32] would have had a lot more happiness. Um,
[L442] [13:27.36] I don't know if that actually would have
[L443] [13:28.88] materialized in the same way if I hadn't
[L444] [13:30.88] been, but they it did feel like the
[L445] [13:32.96] amount of time I was putting in was not
[L446] [13:34.40] commensurate with the reward I was
[L447] [13:35.60] getting. And I was just like, okay, so
[L448] [13:38.40] then I should just kind of be a little
[L449] [13:39.68] more checked out and just like trying to
[L450] [13:42.40] go through the motions of like playing
[L451] [13:44.96] the game in a way. And that just made me
[L452] [13:47.52] super jaded about like this kind of big
[L453] [13:49.36] tech kind of environment cuz it does
[L454] [13:51.92] feel like a lot of people are just going
[L455] [13:53.60] through the motions playing the game and
[L456] [13:56.08] I felt like there could be something
[L457] [13:57.44] bigger to work towards than that
[L458] [13:59.60] >> and that happened 9 months in but you
[L459] [14:02.48] were there for 3 and 1/2 years.
[L460] [14:04.00] >> Yeah. [laughter]
[L461] [14:05.28] So my situation was a little complex of
[L462] [14:07.84] a couple of reasons. There was like a
[L463] [14:09.12] death in the family which made it harder
[L464] [14:10.56] for me to leave. Um, on top of that,
[L465] [14:12.40] they also gave us options that were
[L466] [14:15.20] expensive to exercise. So, it would have
[L467] [14:17.36] cost me $400,000 to exercise my options,
[L468] [14:19.92] which I didn't have 400k lying around. I
[L469] [14:22.08] would have like needed to take out a
[L470] [14:23.04] loan or something. So, my game plan at
[L471] [14:25.68] the time was to just stick around until
[L472] [14:27.28] there was some way to get out of that,
[L473] [14:29.28] which would have either been um the way
[L474] [14:31.12] that they set it up was if you stayed
[L475] [14:32.72] long enough, then you wouldn't need to
[L476] [14:34.56] exercise the options before leaving.
[L477] [14:36.24] They give you 7 years afterwards. That
[L478] [14:38.08] was like one strategy. The other
[L479] [14:39.20] strategy was to just wait for the IPO to
[L480] [14:41.12] happen.
[L481] [14:41.76] >> And the IPO ended up happening in July
[L482] [14:43.36] of 2021. And that's when I kind of had
[L483] [14:45.28] like my handcuffs removed in a way. I
[L484] [14:48.00] could like do whatever I wanted to at
[L485] [14:49.20] that time. Um, that's when I started
[L486] [14:50.80] like just going a lot more deep, a lot
[L487] [14:52.56] deeper into crypto and kind of exploring
[L488] [14:54.48] like what we could be building over
[L489] [14:56.16] there.
[L490] [14:56.72] >> When you look back, you mentioned like,
[L491] [14:58.72] you know, compensation
[L492] [15:00.56] starting at a pre-IPO startup compared
[L493] [15:03.12] to like as if you had worked in big
[L494] [15:04.80] tech. Um, did it did it net out to be
[L495] [15:08.16] higher pay?
[L496] [15:09.68] >> Yeah, I mean it's like an order of
[L497] [15:11.28] magnitude higher than it would have been
[L498] [15:12.48] at like uh spending three and a half
[L499] [15:14.00] years at like a Google or Facebook type
[L500] [15:15.92] of company,
[L501] [15:16.48] >> right?
[L502] [15:16.72] >> I mean, yeah. So, I think financially
[L503] [15:18.24] that was like a fantastic decision in
[L504] [15:19.68] hindsight, but at the time I kind of
[L505] [15:21.60] felt like I was locked in without really
[L506] [15:24.40] having too much flexibility. So, I think
[L507] [15:26.16] that also detracted from my happiness.
[L508] [15:28.00] >> And I think we definitely got lucky over
[L509] [15:29.52] there as well. Like most of my friends
[L510] [15:31.28] that joined preo companies, some of them
[L511] [15:33.76] ended up IPOing. And so they were like
[L512] [15:35.44] pretty happy about that. Um but a lot of
[L513] [15:37.20] them just still haven't IPOed. So
[L514] [15:38.80] they're kind of um they felt like
[L515] [15:40.40] they've invested all this time and then
[L516] [15:41.92] their stock options didn't really end up
[L517] [15:43.68] being worth anything. And I think we got
[L518] [15:45.44] pretty lucky too cuz I graduated in
[L519] [15:46.88] 2018. There are a lot of tech IPOs that
[L520] [15:48.96] happened in 2021. So like my graduating
[L521] [15:51.92] class, your graduating class, we were
[L522] [15:53.20] pretty fortunate with that timing. I
[L523] [15:54.64] think after that the IPO market cooled
[L524] [15:56.24] down and there's been less and less
[L525] [15:57.36] IPOs. like someone that graduated in
[L526] [15:59.28] like 2020 for example, I don't think
[L527] [16:01.28] they would have had that same kind of
[L528] [16:02.96] liquidation opportunity
[L529] [16:04.32] >> when it comes to your career growth. I
[L530] [16:06.40] mean, sounds like you were a little bit
[L531] [16:08.72] checked out. Was there were you going
[L532] [16:11.28] for promotions or getting them or you
[L533] [16:13.68] were kind of coasting?
[L534] [16:15.52] >> I was I mean I I still got promoted the
[L535] [16:18.40] second performance cycle and then
[L536] [16:19.60] afterwards before leaving I was
[L537] [16:20.88] technically up for promotion. Um, so at
[L538] [16:23.52] that point I was playing the game still,
[L539] [16:25.76] but I wasn't really investing too much
[L540] [16:27.28] mental energy into it or like too much
[L541] [16:29.20] time into it. One way of thinking about
[L542] [16:30.88] it is I was putting in the bare minimum
[L543] [16:32.40] to make sure that I was like close to
[L544] [16:34.32] average. Um, and yeah, then I was
[L545] [16:37.36] spending my time elsewhere.
[L546] [16:38.72] >> When you think about I guess is you were
[L547] [16:41.44] playing the game doing the minimum but
[L548] [16:43.36] still getting promoted like what how'd
[L549] [16:46.08] you do that? Yeah, I think at Rob Node
[L550] [16:48.16] it was probably easier than it would
[L551] [16:49.20] have been at like a Meta or like one of
[L552] [16:50.88] these other bigger companies because I
[L553] [16:52.88] joined and the company just grew 10x
[L554] [16:55.52] after that. So I like became a domain
[L555] [16:57.92] expert pretty like just just because of
[L556] [17:00.40] that in a way cuz like we were hiring a
[L557] [17:02.16] lot of people were starting to build a
[L558] [17:03.36] lot of new services. So just by the fact
[L559] [17:05.20] that I existed and I was in the seat at
[L560] [17:06.72] that time I was the only person that
[L561] [17:08.16] knew how to do like 10 different things.
[L562] [17:10.00] And once you're given that much kind of
[L563] [17:11.60] responsibility, then it's pretty easy to
[L564] [17:13.60] become someone that's viewed as like an
[L565] [17:15.44] expert and can be relied upon to like
[L566] [17:17.84] solve different problems. So I think I
[L567] [17:19.68] was a competent engineer that just knew
[L568] [17:21.76] a lot of stuff and that made it very
[L569] [17:23.20] easy for me to get promoted the second
[L570] [17:24.64] time. And I I think that's what was
[L571] [17:26.40] happening as well for my uh second
[L572] [17:29.36] promotion if that had ended up
[L573] [17:30.64] happening. Like I was already an
[L574] [17:32.16] engineering lead because I was like
[L575] [17:33.52] doing stuff for like a few different
[L576] [17:35.20] systems. So I think I was just kind of
[L577] [17:36.64] given that responsibility.
[L578] [17:38.16] >> I see. So it sounds like just by default
[L579] [17:41.28] in a high growth environment if you are
[L580] [17:44.56] competent you become loadbearing.
[L581] [17:46.96] >> Yeah, I I definitely think that if it's
[L582] [17:49.12] like a high growth environment where
[L583] [17:50.32] both the team grows and like the work to
[L584] [17:53.28] do also grows then 100%.
[L585] [17:56.00] >> And because of that there were also a
[L586] [17:57.76] lot of opportunities I got that I
[L587] [17:59.28] probably wouldn't have gotten at a
[L588] [18:00.48] bigger company. Like I mentored three
[L589] [18:03.28] different people. Like my first person
[L590] [18:04.96] that I mentored was like a year and a
[L591] [18:07.76] half in roughly um to the start of my
[L592] [18:10.64] job over there and I feel like a lot of
[L593] [18:12.56] bigger companies that might be less
[L594] [18:13.84] common like you don't get your first
[L595] [18:15.84] mentee or like your first intern until
[L596] [18:17.52] you're like much more senior.
[L597] [18:19.20] >> Right. Right. So it sounds like I mean
[L598] [18:21.52] you know a lot of career trajectories
[L599] [18:23.44] and things are opportunity luck you know
[L600] [18:26.32] things outside of our control but it
[L601] [18:28.64] sounds like two things that were you
[L602] [18:31.92] know a throughine here was that you you
[L603] [18:34.56] sought out talented people or like you
[L604] [18:36.32] went where talented people were and you
[L605] [18:38.64] went towards like a high growth
[L606] [18:39.92] environment. Yeah.
[L607] [18:41.04] >> And those things just kind of
[L608] [18:43.12] >> you know working together led to
[L609] [18:45.52] promotions even though you weren't
[L610] [18:46.88] really even trying for them.
[L611] [18:49.60] And also your conversation was uh also
[L612] [18:52.72] good as well. Um I understand that you
[L613] [18:55.84] worked at Robin Hood during the whole
[L614] [18:58.48] GameStop saga.
[L615] [19:00.24] >> What was that like from the inside?
[L616] [19:02.32] >> Yeah, I mean so for anyone that doesn't
[L617] [19:04.96] have context into it like
[L618] [19:06.80] >> uh when the GameStop saga happened,
[L619] [19:08.72] there were like 12 stocks. It was like
[L620] [19:10.08] GameStop, AMC, and like 10 other ones
[L621] [19:11.92] that I don't remember right now. Um all
[L622] [19:13.84] of them were just like straight ripping
[L623] [19:15.84] because this is like when COVID was
[L624] [19:18.48] happening so people had gotten their
[L625] [19:19.76] like steamy checks as well if I recall
[L626] [19:21.84] and yeah I mean people were just like
[L627] [19:24.16] gambling a lot in a way. Um and these
[L628] [19:27.44] stocks started going up in value so like
[L629] [19:28.88] hedge funds and a lot of institutional
[L630] [19:30.16] traders were like okay we think that
[L631] [19:32.48] this based on a fundamental analysis
[L632] [19:34.32] like this valuation no longer makes
[L633] [19:35.68] sense so we're going to short it because
[L634] [19:37.28] we think it'll eventually return to
[L635] [19:38.64] normal. Uh the issue with shorting a
[L636] [19:40.48] stock though is that you have to borrow
[L637] [19:42.48] the stock then you sell it and then when
[L638] [19:44.56] you want to close that position you have
[L639] [19:46.56] to buy that stock back and then return
[L640] [19:48.88] it. So when you buy that stock back it
[L641] [19:51.44] leads to the price of that stock going
[L642] [19:52.80] up. So when the price is going up and
[L643] [19:54.88] people have to start closing their short
[L644] [19:56.32] positions that leads to more buy
[L645] [19:58.40] pressure from those shorts being closed
[L646] [19:59.92] which causes a short squeeze. So all
[L647] [20:01.84] these stocks had short squeezes
[L648] [20:03.12] happening on them. Um, and in a way it
[L649] [20:05.44] was like the little guy was beating the
[L650] [20:06.80] big guy because these institutions were
[L651] [20:08.72] leading. Robin Hood was the place where
[L652] [20:10.56] everyone was going to trade. And then I
[L653] [20:12.80] think it was like January 28th of 2021.
[L654] [20:15.28] Uh, Robin Hood just turned off buys on
[L655] [20:18.08] all these meme stocks. And it was insane
[L656] [20:21.04] because I found out about it when I woke
[L657] [20:22.88] up and I was like, damn, this is crazy.
[L658] [20:24.64] And then that day there were so many
[L659] [20:26.00] people that just reached out to me like,
[L660] [20:27.44] yo, man, what the hell is going on? Cuz
[L661] [20:28.96] a lot of them, I think, were actually
[L662] [20:30.08] financially invested in this as well.
[L663] [20:31.92] And when Robin Nonoff is the price of
[L664] [20:33.92] GameStop started to go down, so they're
[L665] [20:35.28] like understandably like quite pissed
