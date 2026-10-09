Chunk 5; segments 1608–2007. Start may repeat the previous chunk for context.

# Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones

Source ID: source-3f6b5c7495d2c862
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Co-Creator_of_Haskell_Useless_vs_Useful_Languages,_Rust_vs_C,_Functional_Programming_Simon_Jones_en.txt
Video: https://www.youtube.com/watch?v=xcB_LF3cdqw

[L1617] [55:17.28] Now,
[L1618] [55:18.32] you could write a program that generated
[L1619] [55:20.04] such trees and you could write a program
[L1620] [55:21.76] that consumed such trees knowing that
[L1621] [55:23.64] every 17th
[L1622] [55:25.00] um layer we switch to characters
[L1623] [55:27.12] but most static type systems would make
[L1624] [55:29.40] it pretty hard for you to accept that
[L1625] [55:31.16] program. And yet, it will run.
[L1626] [55:35.96] Now, you might say, "Oh, but I really
[L1627] [55:37.68] want to write that program, guys. You
[L1628] [55:39.04] know, don't get in my way." Well,
[L1629] [55:41.36] then
[L1630] [55:42.44] um
[L1631] [55:43.40] uh then we should provide a way for you
[L1632] [55:45.88] to bail out into dynamic typing.
[L1633] [55:48.72] Right?
[L1634] [55:49.80] What I'd like to do is to say, "Okay, so
[L1635] [55:52.12] if all else fails, then at least you
[L1636] [55:54.24] can, as it were, pair up a value with
[L1637] [55:56.72] its type representation." As one reason
[L1638] [55:58.72] we don't want to interpret an integer as
[L1639] [56:01.08] a double-precision float, for example,
[L1640] [56:03.84] is that, you know, they don't even have
[L1641] [56:05.44] the same representation, which is just
[L1642] [56:06.96] just nonsense. Right?
[L1643] [56:09.04] One possible way, which it untyped
[L1644] [56:10.96] languages let you do, is to tag every
[L1645] [56:12.92] integer and every double-precision float
[L1646] [56:14.88] with the fact, "I'm an integer. I'm a
[L1647] [56:16.36] double-precision float." But that has a
[L1648] [56:17.56] lot of overhead.
[L1649] [56:19.56] So, one merit, and it's not I think it's
[L1650] [56:22.12] not the biggest single merit, is a major
[L1651] [56:23.96] merit of static type systems, is you
[L1652] [56:25.52] have no tags.
[L1653] [56:27.60] You know that if it says it's an
[L1654] [56:29.36] integer, it's going to be an integer.
[L1655] [56:30.68] You know that if it's a double-precision
[L1656] [56:32.44] float, it's going to be double-precision
[L1657] [56:33.48] float. Right?
[L1658] [56:35.12] But if you're not sure, um maybe we
[L1659] [56:37.52] could make a way to make a pair of a
[L1660] [56:40.92] type representation and this value. The
[L1661] [56:43.32] type representation is now like a
[L1662] [56:45.32] runtime tag. It's like a little runtime
[L1663] [56:47.20] data structure that describes the type.
[L1664] [56:49.60] And then in your program, you could say,
[L1665] [56:51.20] "Now I want to say, uh I've got this
[L1666] [56:53.48] type dynamic. We'll call this pair a
[L1667] [56:55.84] value of type dynamic." Now, when I want
[L1668] [56:58.80] to take a value of type dynamic and
[L1669] [57:00.48] treat it as a character, we'll say, "Ah,
[L1670] [57:02.88] look Look at the type dynamic. See if it
[L1671] [57:05.52] says it's character. If it is, return
[L1672] [57:06.84] the character. If not, crash." Right?
[L1673] [57:08.80] Runtime failure.
[L1674] [57:10.40] That's fine. You can do that. So, um
[L1675] [57:12.84] and uh Haskell has good support for
[L1676] [57:15.00] dynamic typing where necessary. So, my
[L1677] [57:17.48] uh my my story would be static typing
[L1678] [57:20.76] should expand as as to carry as much as
[L1679] [57:23.12] possible.
[L1680] [57:24.20] And where you absolutely cannot do it,
[L1681] [57:26.40] sorry, then use dynamic typing, and
[L1682] [57:28.56] we'll provide facilities to support
[L1683] [57:29.84] that.
[L1684] [57:30.92] >> One thing I wanted to to talk with you
[L1685] [57:32.96] about is the compiler. How does the GHC
[L1686] [57:35.68] work on a on a high level?
[L1687] [57:37.48] >> So,
[L1688] [57:38.52] GHC takes a string like like any other
[L1689] [57:40.84] compiler that the source code of the
[L1690] [57:42.40] program, parses it.
[L1691] [57:45.32] Um and then it um
[L1692] [57:48.44] uh type checks it.
[L1693] [57:49.96] Because that is this a type correct
[L1694] [57:51.00] program.
[L1695] [57:52.56] Then it converts it to lambda calculus.
[L1696] [57:58.32] Now,
[L1697] [57:59.28] Haskell the Haskell AST, the original
[L1698] [58:01.80] source tree, has
[L1699] [58:04.04] 50 different data types, 50 different
[L1700] [58:06.12] kinds of nodes, some of which have 30 or
[L1701] [58:08.52] 40 different variants.
[L1702] [58:10.80] So, it's a really big, diverse,
[L1703] [58:13.80] complicated data structure.
[L1704] [58:16.08] The AST.
[L1705] [58:17.92] Lambda calculus has this
[L1706] [58:19.80] variant of the lambda calculus has
[L1707] [58:21.04] eight.
[L1708] [58:24.00] One to data type that maybe two or three
[L1709] [58:25.64] data types with eight constructors.
[L1710] [58:27.80] So, it's like taking a gigantic language
[L1711] [58:31.76] and squeezing it down into a tiny one.
[L1712] [58:36.32] And that tiny one we can then optimize,
[L1713] [58:38.20] right? That's the optimizer works on
[L1714] [58:39.48] that. So, the front end
[L1715] [58:41.72] does parse, rename, type check, desugar
[L1716] [58:44.88] into lambda calculus. That's the front
[L1717] [58:46.68] end.
[L1718] [58:48.80] The lambda calculus, particular
[L1719] [58:50.08] language, is called GHC's core language.
[L1720] [58:52.88] I'm quite proud of it cuz it's been very
[L1721] [58:55.32] very stable.
[L1722] [58:57.76] It's 35 years old and it has barely
[L1723] [59:00.84] changed since birth.
[L1724] [59:02.40] That's amazing, right? Because Haskell
[L1725] [59:04.12] has changed a lot, a lot.
[L1726] [59:07.60] Right? So, almost all of the innovation
[L1727] [59:10.48] in Haskell
[L1728] [59:12.40] has been in the front end.
[L1729] [59:14.64] Very little
[L1730] [59:16.24] in core.
[L1731] [59:18.56] Now, the back end, the core optimizer,
[L1732] [59:20.60] has changed a lot, too.
[L1733] [59:22.24] But all of the changes that were useful
[L1734] [59:23.84] there would have been useful 30 years
[L1735] [59:25.08] ago, right?
[L1736] [59:26.68] Yeah. So, they're two completely
[L1737] [59:28.36] separable things. So, I'm quite proud
[L1738] [59:29.44] about that. Core then we do a lot of
[L1739] [59:31.36] core-to-core passes that simply take
[L1740] [59:33.08] core program core program programs,
[L1741] [59:35.00] right? Lots and lots. Long pipeline.
[L1742] [59:37.92] Then we convert it um
[L1743] [59:40.84] uh to C-- which is a prototypical
[L1744] [59:44.20] imperative language. Think of it as a
[L1745] [59:46.12] portable assembly code.
[L1746] [59:48.28] Right? So, that bit is meant to be
[L1747] [59:50.28] platform independent.
[L1748] [59:52.32] So, it's simply that's the compiler that
[L1749] [59:54.48] take your program I said if you take
[L1750] [59:55.68] lambda calculus and compile it that's
[L1751] [59:57.92] that step, right? I want to compile the
[L1752] [01:00:00.08] lambda calculus into
[L1753] [01:00:02.04] you know, machine instructions really.
[L1754] [01:00:04.32] But I don't really mean machine instruc-
[L1755] [01:00:05.56] I mean portable machine instructions.
[L1756] [01:00:07.68] That's called C--
[L1757] [01:00:09.88] Then I want to convert C-- into actual
[L1758] [01:00:12.12] machine instructions for various
[L1759] [01:00:13.24] platforms. And then we could either do
[L1760] [01:00:15.04] that directly with a native code backend
[L1761] [01:00:16.64] or go via LLVM.
[L1762] [01:00:18.76] >> Interesting. I've never heard of C--
[L1763] [01:00:21.52] What Why not just go directly to I would
[L1764] [01:00:23.80] have thought maybe assembly or something
[L1765] [01:00:25.44] like that?
[L1766] [01:00:26.40] >> what happens in assembly in which for
[L1767] [01:00:28.08] which processor, please?
[L1768] [01:00:30.92] >> Oh, I see.
[L1769] [01:00:32.02] >> [laughter]
[L1770] [01:00:32.44] >> I guess it's the I would have thought
[L1771] [01:00:34.28] the lambda calculus part was already
[L1772] [01:00:35.96] portable. So, you just
[L1773] [01:00:37.08] >> It is, yeah. You could go straight but
[L1774] [01:00:39.88] but but so, there's work to go from
[L1775] [01:00:41.64] lambda calculus you could go all the way
[L1776] [01:00:43.08] to x86.
[L1777] [01:00:44.92] Then throw all that away and now go from
[L1778] [01:00:46.64] lambda calculus to pal PC.
[L1779] [01:00:49.32] Oh dear, I've just duplicated a lot of
[L1780] [01:00:50.96] work.
[L1781] [01:00:53.36] By going from lambda calculus to C-- and
[L1782] [01:00:56.12] then from C-- to x86 C-- We've set We've
[L1783] [01:00:59.60] We've avoided duplicating
[L1784] [01:01:02.24] the work that went from lambda calculus
[L1785] [01:01:04.32] to C-- right?
[L1786] [01:01:06.04] When you see it like that it's pretty
[L1787] [01:01:07.08] obvious, isn't it? Like you got to You
[L1788] [01:01:09.00] want to make the platform specific bit
[L1789] [01:01:11.84] as small as possible.
[L1790] [01:01:14.16] You would like to have as it were like a
[L1791] [01:01:16.16] generic architecture. One that can do
[L1792] [01:01:18.24] addition and has a program counter and a
[L1793] [01:01:19.96] stack and so forth.
[L1794] [01:01:21.72] That's all C-- just a portable assembly
[L1795] [01:01:23.80] language.
[L1796] [01:01:24.84] And then you say, "Oh, the nitty-gritty
[L1797] [01:01:26.32] of, you know, whether you have double
[L1798] [01:01:28.68] precision add and set the floating-point
[L1799] [01:01:30.72] bit here and there." That, well, that's
[L1800] [01:01:32.12] platform specific. The core is itself
[L1801] [01:01:34.16] statically typed. You know, but it's
[L1802] [01:01:36.08] always a surprising because no other
[L1803] [01:01:37.56] compiler does has this property, no
[L1804] [01:01:39.16] other production compiler.
[L1805] [01:01:40.88] By core statically typed, I don't just
[L1806] [01:01:42.56] mean that the initial the initial
[L1807] [01:01:43.80] program was type correct.
[L1808] [01:01:45.84] I mean that a core program, you can run
[L1809] [01:01:48.00] a type checker on that. And I might say,
[L1810] [01:01:49.88] "Why do you need to? Because after all,
[L1811] [01:01:51.44] if GHC is correct, it started with a
[L1812] [01:01:53.76] type correct core program
[L1813] [01:01:55.76] because it came from a type correct
[L1814] [01:01:56.68] Haskell program, assuming the desugaring
[L1815] [01:01:58.40] was right, and all the optimizations, if
[L1816] [01:02:00.60] they're right, will generate a type
[L1817] [01:02:02.48] correct core program. So, why do you
[L1818] [01:02:04.00] need to type check it?"
[L1819] [01:02:05.80] Answer:
[L1820] [01:02:06.92] to discover bugs in GHC.
[L1821] [01:02:09.28] Now, these are serious bugs, right? If
[L1822] [01:02:11.12] you ever take a type correct core
[L1823] [01:02:13.92] program and an optimization pass
[L1824] [01:02:15.32] produces a type incorrect
[L1825] [01:02:17.52] core program,
[L1826] [01:02:19.36] what will happen?
[L1827] [01:02:21.04] If we don't have the type checker for
[L1828] [01:02:22.44] core,
[L1829] [01:02:23.64] we'll generate machine code and we'll
[L1830] [01:02:25.04] run it and we'll get a seg fault.
[L1831] [01:02:28.96] Now, we have to backtrack for any
[L1832] [01:02:30.52] particular test program that now
[L1833] [01:02:31.96] crashes,
[L1834] [01:02:34.20] all the way to back up the pipeline, up
[L1835] [01:02:36.56] the pipeline, up the pipeline, up the
[L1836] [01:02:37.80] pipeline. Oh, it was this pass
[L1837] [01:02:41.08] of GHC that was faulty.
[L1838] [01:02:43.52] That's super hard to do because, you
[L1839] [01:02:45.60] know, you're getting out GDB on some
[L1840] [01:02:47.60] runtime failure
[L1841] [01:02:49.60] that is an indirect and perhaps distant
[L1842] [01:02:51.40] consequence
[L1843] [01:02:52.88] of the fact you just generated a type,
[L1844] [01:02:55.40] you know, you just made a you had a bug
[L1845] [01:02:57.28] in the optimizer.
[L1846] [01:02:59.48] So, it is amazing
[L1847] [01:03:01.76] to have a type checker for core.
[L1848] [01:03:04.36] Now,
[L1849] [01:03:05.20] why does nobody else do this? Well, it's
[L1850] [01:03:07.28] because their intermediate language,
[L1851] [01:03:08.76] typically, and this I really am talking
[L1852] [01:03:10.36] typically because I know of no other
[L1853] [01:03:11.88] compiler that has this property, none,
[L1854] [01:03:14.12] production compiler,
[L1855] [01:03:16.28] typically then they're, you know,
[L1856] [01:03:17.20] complex complex syntax trees decorated
[L1857] [01:03:19.40] with all sorts of pragmatic information
[L1858] [01:03:21.24] and things hanging on it onto it here
[L1859] [01:03:23.20] and there and
[L1860] [01:03:24.76] um
[L1861] [01:03:26.44] um you know, there's no there's no type
[L1862] [01:03:28.80] checker for it at all.
[L1863] [01:03:31.12] And there's no hope of one.
[L1864] [01:03:33.20] So, I'm very proud of the fact that core
[L1865] [01:03:35.20] is statically typed and I'm also also
[L1866] [01:03:38.76] think it's a
[L1867] [01:03:40.72] The most delightful thing is that the
[L1868] [01:03:42.88] way that it is statically typed it is a
[L1869] [01:03:45.00] It's an implementation of something
[L1870] [01:03:46.16] called system F.
[L1871] [01:03:48.44] So, system F when I said lambda calculus
[L1872] [01:03:50.24] lambda calculus as Alonzo Church had it
[L1873] [01:03:52.36] was untyped had no type system at all.
[L1874] [01:03:55.48] But Girard defined defined something
[L1875] [01:03:57.60] called system F which is a statically
[L1876] [01:03:59.80] typed lambda calculus a rather powerful
[L1877] [01:04:01.88] one. And core is essentially system F.
[L1878] [01:04:06.16] So, we literally adopted something from
[L1879] [01:04:08.12] the nerdy theoretical computer science
[L1880] [01:04:10.88] you know, logic community logic and
[L1881] [01:04:13.48] mathematics community and adopted it
[L1882] [01:04:15.24] directly in a in a production
[L1883] [01:04:17.00] implementation.
[L1884] [01:04:18.72] So,
[L1885] [01:04:19.84] I'm very proud of that.
[L1886] [01:04:21.32] Um I think core is
[L1887] [01:04:23.52] and the fact that we can do we have 35
[L1888] [01:04:26.20] years of worth of development that has
[L1889] [01:04:27.48] been not just not impeding but actively
[L1890] [01:04:29.76] aided by statically typed intermediate
[L1891] [01:04:31.20] language is really
[L1892] [01:04:32.68] a big marker in the ground.
[L1893] [01:04:35.00] >> You know, watching all your talks,
[L1894] [01:04:36.24] reading everything. One of the
[L1895] [01:04:38.00] interesting data points that you brought
[L1896] [01:04:39.72] up was that uh Haskell is talked about
[L1897] [01:04:43.60] more than used when you compared Stack
[L1898] [01:04:46.76] Overflow volume and you know, actually
[L1899] [01:04:49.12] GitHub volume. Like who's actually using
[L1900] [01:04:50.96] the programming language? Why do you
[L1901] [01:04:52.76] think that is?
[L1902] [01:04:55.00] >> So,
[L1903] [01:04:56.12] Haskell embodies one
[L1904] [01:04:59.20] key idea.
[L1905] [01:05:01.04] Immutability changes everything. There's
[L1906] [01:05:03.24] a quote from Pat Helland's talk that I
[L1907] [01:05:04.68] think you also paper which I think you
[L1908] [01:05:06.64] also looked at or read. Um So, it says
[L1909] [01:05:08.76] programming with values changes
[L1910] [01:05:10.32] everything about the way you think about
[L1911] [01:05:11.76] programming.
[L1912] [01:05:13.08] It's just
[L1913] [01:05:14.60] mind-changing. It's not necessarily
[L1914] [01:05:16.24] better, but it is different. And so,
[L1915] [01:05:18.96] Haskell takes that idea and runs with
[L1916] [01:05:20.76] it. Everything is driven by that one
[L1917] [01:05:22.60] idea. Everything else is incidental.
[L1918] [01:05:25.24] Uh in the early days, that meant we just
[L1919] [01:05:27.40] said, "Well, guys, suck it up, you know,
[L1920] [01:05:28.96] we'll keep um changing the language, and
[L1921] [01:05:31.24] if it breaks your programs, too bad." Um
[L1922] [01:05:34.20] so, it is, you know, a bit peculiar, and
[L1923] [01:05:35.96] therefore, um oh also, it felt a bit
[L1924] [01:05:37.96] academic, cuz initially, it was really
[L1925] [01:05:39.40] not very powerful. It was taking the key
[L1926] [01:05:41.00] idea, but you couldn't do very much with
[L1927] [01:05:42.60] it. We talked about that, right?
[L1928] [01:05:44.48] So, over time, GHC and on Haskell in in
[L1929] [01:05:47.44] general has become more and more
[L1930] [01:05:48.64] powerful. The type system has become
[L1931] [01:05:49.88] less and less in your way, and more and
[L1932] [01:05:51.84] more useful. The you know, all the
[L1933] [01:05:53.60] obstacles that make functional
[L1934] [01:05:54.84] programming harder become better. The
[L1935] [01:05:56.44] compiler generates faster code, it
[L1936] [01:05:57.96] compiles faster, and so forth. So, um
[L1937] [01:06:01.60] uh
[L1938] [01:06:02.80] So, it has become less, uh if you like,
[L1939] [01:06:05.04] peculiar. Um so, we've become more and
[L1940] [01:06:07.32] more taking into account the the um the
[L1941] [01:06:10.80] uh the needs of our users. But in a way,
[L1942] [01:06:13.08] the sort of cultural heritage is we
[L1943] [01:06:15.12] never give up on the one core principle.
[L1944] [01:06:17.48] We're just not going to give you
[L1945] [01:06:18.80] unrestricted side effects. Sorry.
[L1946] [01:06:20.80] Right?
[L1947] [01:06:21.72] You want to say I'm fully before I am,
[L1948] [01:06:23.32] and put up with the consequences. So,
[L1949] [01:06:25.36] we're going to stick to one core
[L1950] [01:06:26.52] principle, and then we'll we'll do lots
[L1951] [01:06:28.52] of work around the edges to make that
[L1952] [01:06:29.56] better. Right, so, um
[L1953] [01:06:31.96] that does limit our community somewhat,
[L1954] [01:06:33.80] right? It does mean you have to You
[L1955] [01:06:35.52] really have to think in a different way.
[L1956] [01:06:37.12] Immutability changes everything. That
[L1957] [01:06:38.60] means you'd have to think a different
[L1958] [01:06:39.56] way about about programming. Maybe you
[L1959] [01:06:41.28] don't want to think in a different way.
[L1960] [01:06:42.36] That's fine. Then don't use Haskell,
[L1961] [01:06:44.20] right? So, uh so, in a way, we've um we
[L1962] [01:06:47.96] we started from a very small user
[L1963] [01:06:49.44] community, uh very sort of pure and
[L1964] [01:06:51.16] nerdy one, and going going larger and
[L1965] [01:06:52.64] larger, but all slowly, slowly, but all
[L1966] [01:06:54.80] the time main- maintaining uh
[L1967] [01:06:56.40] faithfulness to this core principle.
[L1968] [01:06:58.08] >> I thought that was
[L1969] [01:06:59.64] very unique about Haskell, because I
[L1970] [01:07:02.28] feel a lot of the other programming
[L1971] [01:07:04.36] languages are user-centric. I mean, if
[L1972] [01:07:07.48] if people something, they work on it,
[L1973] [01:07:09.80] they add it. Whereas, Haskell feels more
[L1974] [01:07:13.04] principled or it's it's all starting
[L1975] [01:07:15.32] from these ideas. And if you don't
[L1976] [01:07:19.48] satisfy these ideas as a user, yeah,
[L1977] [01:07:22.16] well, we yeah, that's that's fine.
[L1978] [01:07:24.92] Um for instance, in one of your talks,
[L1979] [01:07:26.60] you mentioned somewhere that there was a
[L1980] [01:07:28.64] release of the compiler where if a file
[L1981] [01:07:32.20] wasn't type correct, then the compiler
[L1982] [01:07:35.36] would delete the file.
[L1983] [01:07:37.52] >> Oh, wait. It would report with the error
[L1984] [01:07:38.60] message first.
[L1985] [01:07:39.88] >> Yeah, it reports there. But, I thought
[L1986] [01:07:41.64] that was that was absurd. I mean, very
[L1987] [01:07:44.68] hostile, I guess, to the I mean, well,
[L1988] [01:07:46.80] it's it's if you're type safe, no
[L1989] [01:07:48.68] problems. But,
[L1990] [01:07:50.08] >> Oh, it was a mistake, right? It was a
[L1991] [01:07:51.80] bug. It wasn't deliberate.
[L1992] [01:07:54.15] >> [laughter]
[L1993] [01:07:55.24] >> And it only happened, you know, how did
[L1994] [01:07:56.72] the bug get, you know, get out? Because,
[L1995] [01:07:58.16] of course, if it always did that, we'd
[L1996] [01:07:59.52] have noticed.
[L1997] [01:08:00.84] Um how did it get into a release? Well,
[L1998] [01:08:02.60] it was because it was only on Windows
[L1999] [01:08:04.04] and only when you compile a module that
[L2000] [01:08:05.48] was not in the current directory.
[L2001] [01:08:07.64] But, at that stage, our um
[L2002] [01:08:09.60] our users were very forgiving. And, you
[L2003] [01:08:11.08] know, somebody wrote to us and said,
[L2004] [01:08:12.24] "Well, by the way, Simon, you might like
[L2005] [01:08:13.56] to know that, you know, GHC does this.
[L2006] [01:08:14.92] But, hey, don't worry about it, you
[L2007] [01:08:16.00] know, I just copy all my files somewhere
[L2008] [01:08:17.68] else before I compile and then I copy
[L2009] [01:08:19.44] them back."
[L2010] [01:08:21.72] So, of course, those days are long gone.
[L2011] [01:08:23.56] We pay a lot more attention to our users
[L2012] [01:08:25.20] and have much more rigorous CI testing
[L2013] [01:08:27.04] than ever we did, right? So, um
[L2014] [01:08:29.44] that's a that's a a story from a long
[L2015] [01:08:31.04] time ago, but it's a good cultural story
[L2016] [01:08:32.80] because it suggests that we've cared
