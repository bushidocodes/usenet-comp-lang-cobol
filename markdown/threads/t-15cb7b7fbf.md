[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Metaphone

_33 messages · 8 participants · 2011-10_

---

### Metaphone

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-05T15:54:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
Anybody got COBOL code for implementing Metaphone (Soundex on steroids) that 
they'd be willing to share?

I've got it partially coded, but the wet-ware definitions are somewhat 
equivocal. For example:

The letter "G"
1.SILENT if in "-gh-" and not at end
         or before a vowel
         in "-gn" or "-gned"
         in "-dge-" etc., as in above rule
2.J if before "i", or "e", or "y"
         if not double "gg"
3.K      otherwise

I THINK it goes:
xxxGHxxx > xxxHxxx (rule 1)
xxxxxxGH > xxxxxxKH (rule 1 plus rule 3)
xxxGAxxx > xxxKAxxx

In the grand scheme of things, it probably doesn't make much difference as 
long as the result is consistent, but it drives me nuts trying to figure out 
what these civilians are describing.

Of course that's the normal lot of programmers...
```

#### ↳ Re: Metaphone

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-06T13:09:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f49ukF7rbU1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
HeyBub wrote:
> Anybody got COBOL code for implementing Metaphone (Soundex on
> steroids) that they'd be willing to share?
…[12 more quoted lines elided]…
>
I can see your consternation. :-)

Rule 1 is contradictory:

g is NOT  always silent before a vowel (agate), it  may simply change to "j" 
as noted in rule 2. (Last time I looked e is a vowel...)

I would LOVE to see an example of  g sounding like K :-) (I'm sure there 
must be some but I can't think of any offhand.)

I have Soundex in COBOL (and will gladly share it with anyone who wants it) 
but never heard of Metaphone until now.

Looks like fun... :-)

Unfortunately, I'm not able to take on any fun at the moment as I have just 
returned home and have some serious stuff to do. By the time I'm ready for 
fun, You will have solved it :-)



> I THINK it goes:
> xxxGHxxx > xxxHxxx (rule 1)
> xxxxxxGH > xxxxxxKH (rule 1 plus rule 3)
> xxxGAxxx > xxxKAxxx

Not good examples, Jerry. Actual words would be better.

Arrrggghhh! :-)
>
> In the grand scheme of things, it probably doesn't make much
…[3 more quoted lines elided]…
> Of course that's the normal lot of programmers...

Sure. It requires a literal mind and absolutely no sense of humour.

No wonder you are finding it hard :-)

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Metaphone

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-05T22:06:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ivednZzhpLe5hhDTnZ2dnUVZ_oadnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <9f49ukF7rbU1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> Anybody got COBOL code for implementing Metaphone (Soundex on
…[22 more quoted lines elided]…
> there must be some but I can't think of any offhand.)

Oh, it's not meant to generate a WORD. Metaphone makes a CODE. Soundex 
generates a code using numbers, metaphone generates a code using letters.
```

##### ↳ ↳ Re: Metaphone

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-06T05:17:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37643ab5-d61a-4624-937a-80f178bef46b@m37g2000yqc.googlegroups.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <9f49ukF7rbU1@mid.individual.net>`

```
On Oct 6, 1:09 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> HeyBub wrote:
> > Anybody got COBOL code for implementing Metaphone (Soundex on
…[23 more quoted lines elided]…
>

Try GAERDYFF (I think that was the last Welsh spelling of Cardiff that
I encountered when I last left Wales) pronounced as KARDIFF (if you
are English).
```

###### ↳ ↳ ↳ Re: Metaphone

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-10-06T07:44:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53cr8757snb1ku2sr2e42egdt5mmvheb8o@4ax.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <9f49ukF7rbU1@mid.individual.net> <37643ab5-d61a-4624-937a-80f178bef46b@m37g2000yqc.googlegroups.com>`

```
On Thu, 6 Oct 2011 05:17:44 -0700 (PDT), Alistair Maclean
<alistair.j.l.maclean@gmail.com> wrote:

>Try GAERDYFF (I think that was the last Welsh spelling of Cardiff that
>I encountered when I last left Wales) pronounced as KARDIFF (if you
>are English).

I've seen that argument about vowels sometimes including "w".    Welsh
isn't English.    Are we including all languages that use an alphabet
based upon the Latin one?

-- 
"In no part of the constitution is more wisdom to be found,
than in the clause which confides the question of war or peace 
to the legislature, and not to the executive department." 

- James Madison
```

###### ↳ ↳ ↳ Re: Metaphone

_(reply depth: 4)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-07T02:59:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c80be718-8f95-4979-8073-f9249ac21d8d@d28g2000vby.googlegroups.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <9f49ukF7rbU1@mid.individual.net> <37643ab5-d61a-4624-937a-80f178bef46b@m37g2000yqc.googlegroups.com> <53cr8757snb1ku2sr2e42egdt5mmvheb8o@4ax.com>`

```
On Oct 6, 2:44 pm, Howard Brazee <how...@brazee.net> wrote:
> On Thu, 6 Oct 2011 05:17:44 -0700 (PDT), Alistair Maclean
>
…[14 more quoted lines elided]…
> - James Madison

METAPHONE is in at least version 3, with allowances made for non-
English and non-Latin alphabet languages. WELSH is the language
pertaining to the UK before the continent invaders arrived here (pre-
Roman).
```

###### ↳ ↳ ↳ Re: Metaphone

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T11:07:34+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f6n58Fn8aU1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <9f49ukF7rbU1@mid.individual.net> <37643ab5-d61a-4624-937a-80f178bef46b@m37g2000yqc.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 6, 1:09 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[29 more quoted lines elided]…
> are English).

 A brave attempt, Alistair.

However, I believe it is the ENGLISH language that is under discussion... 
:-)

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Metaphone

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2011-10-05T22:59:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udydnaBNY6HjhBDTnZ2dnUVZ_vSdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>`

```

"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com...
> Anybody got COBOL code for implementing Metaphone (Soundex on steroids) 
> that they'd be willing to share?
…[26 more quoted lines elided]…
>

You may have already googled this but if not see: 
http://en.wikipedia.org/wiki/Metaphone
```

#### ↳ Re: Metaphone

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-06T13:34:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6kaop$3n3$1@reader1.panix.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
In article <3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:

[snip]

>The letter "G"
>1.SILENT if in "-gh-" and not at end
>         or before a vowel
>         in "-gn" or "-gned"
>         in "-dge-" etc., as in above rule

'-gh' is a tough one.  With effort one might get through, though, and rest 
'neath a flowering bough.

DD
```

##### ↳ ↳ Re: Metaphone

- **From:** Allodoxaphobia <knock_yourself_out@example.net>
- **Date:** 2011-10-06T22:22:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrnj8sahn.1rdg.knock_yourself_out@shell.config.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <j6kaop$3n3$1@reader1.panix.com>`

```
On Thu, 6 Oct 2011 13:34:17 +0000 (UTC), docdwarf@panix.com () wrote:
> In article <3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[10 more quoted lines elided]…
> 'neath a flowering bough.

Enough!  Enough!		:-)

Jonesy
-- 
  Marvin L Jones    | jonz          | W3DHJ  | linux
   38.24N  104.55W  |  @ config.com | Jonesy |  OS/2
    * Killfiling google & XXXXbanter.com: jonz.net/ng.htm
```

###### ↳ ↳ ↳ Re: Metaphone

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-07T00:11:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6lg39$k4o$1@reader1.panix.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <j6kaop$3n3$1@reader1.panix.com> <slrnj8sahn.1rdg.knock_yourself_out@shell.config.com>`

```
In article <slrnj8sahn.1rdg.knock_yourself_out@shell.config.com>,
Allodoxaphobia  <Reply_to@my.sig.adr> wrote:
>On Thu, 6 Oct 2011 13:34:17 +0000 (UTC), docdwarf@panix.com () wrote:
>> In article <3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>,
…[13 more quoted lines elided]…
>Enough!  Enough!		:-)

One egg is un oeuf.

DD
```

#### ↳ Re: Metaphone (mumble-mumble)

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-06T10:59:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
HeyBub wrote:

Working through the algorithm specified at
http://www.blackbeltcoder.com/Articles/algorithms/phonetic-string-comparison-with-soundex

We see the following rules:

4. 'C' transforms to 'X' if followed by 'IA' or 'H' (unless in latter case, 
it is part of '-SCH-', in which case it transforms to 'K'). 'C' transforms 
to 'S' if followed by 'I', 'E', or 'Y'. Otherwise, 'C' transforms to 'K'.

Which means, if I read it right, the word "CHECK" transforms to "XHEKK"

Beavering on, we reach rule 9:

9. 'CK' transforms to 'K'.

But there is no longer a "CK". Nor can there ever be.

Perhaps someone expert in VB can resolve this conundrum - the source code is 
included at the above link.

Thanks
```

##### ↳ ↳ Re: Metaphone (mumble-mumble)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T11:11:18+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f6nc8Fp2oU1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com>`

```
HeyBub wrote:
> HeyBub wrote:
>
…[20 more quoted lines elided]…
> Thanks

Might I ask why Soundex is inadequate for your purposes?

I've implemented it with database searches and found it extremely useful. 
Especially for people who don't have English as a first language but must do 
searches on things like English names.

What we have seen so far of Metaphone (and I haven't looked at it in detail) 
just looks like a nightmare.

What makes it worth it?

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-06T17:51:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6cs871tfua1hll73u6cfqovirhm1ek16j@4ax.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net>`

```
On Fri, 7 Oct 2011 11:11:18 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>HeyBub wrote:
>> HeyBub wrote:
…[32 more quoted lines elided]…
>What makes it worth it?


Simply that it works a fair bit better than Soundex.  Double Metaphone
is better yet.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T14:44:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f73rcFid0U1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <g6cs871tfua1hll73u6cfqovirhm1ek16j@4ax.com>`

```
Robert Wessel wrote:
> On Fri, 7 Oct 2011 11:11:18 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[39 more quoted lines elided]…
> is better yet.

I have never experienced Soundex "not working". Never had the slightest 
trouble with it. While this doesn't preclude something else working 
"better", it would be necessary to define exactly what criteria "better" was 
based on.

My question was whether the degree of "better" justifies all the hassle...

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-06T18:22:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L7-dnZB3rdSupRPTnZ2dnUVZ_sqdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> HeyBub wrote:
…[23 more quoted lines elided]…
> Might I ask why Soundex is inadequate for your purposes?

Well, Metaphone is newer and, perforce, better. Soundex generates a 
4-character code which seems to me, inexperienced as I am, to be, well, 
limited.

BUT! I am going to abandon this Metaphone quagmire, code up a quickie 
Soundex subroutine and give it a go. If the results seem to me to be too 
equivocal, I'l go back to the (insert curse-word here) project.

>
> I've implemented it with database searches and found it extremely
> useful. Especially for people who don't have English as a first
> language but must do searches on things like English names.

All my users have English as their native language. Except me, of course. I 
grew up hearing my parents speaking what I found out later was Pig Latin 
around me.

>
> What we have seen so far of Metaphone (and I haven't looked at it in
> detail) just looks like a nightmare.

Have a look at the Double-Helix Metaphone.

>
> What makes it worth it?
>

What's art without suffering?
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T15:34:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f76poF6hqU1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <L7-dnZB3rdSupRPTnZ2dnUVZ_sqdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> HeyBub wrote:
…[47 more quoted lines elided]…
> Have a look at the Double-Helix Metaphone.

That would be the Do Not Attempt  version...?

>
>>
…[3 more quoted lines elided]…
> What's art without suffering?

An excellent answer, Jerry. :-) Since you made me smile here's a free 
Soundex routine... :-)

(Maybe others can use it too...)

000010 identification division.
000020 program-id.     SOUNDEX.
000030 installation.   PRIMA Computing.
000040 author.         Peter E. C. Dashwood.
000050 date-written.   Dec 98.
000060* (revised in May,1999).
000070* (reviewed in April 2001.)
000080*
000090*remarks.
000100*
000110* (This module is written to be platform independent and can run
000120*  on ANY platform with an ANSI COBOL compiler - Mainframe,
000130*  mid-range, or PC.)
000140*
000150*             TEXT COMPARISON BY SOUND.
000160*
000170*
000180*    This module takes 2 string inputs and applies the
000190*    SOUNDEX algorithm to them to decide whether or not
000200*    they are homonyms.
000210*
000220*    The module is useful for detecting mis-spelled searches
000230*    (like "too" and "two") or people's names (like
000240*     "Snyder", "Schneider", or "Snider".)
000250*
000260* (All inputs and outputs to this function are via a single
000270* parameter block. See LINKAGE below)
000280*
000290*    INPUTS:
000300* String 1: 20 bytes containing a single word.
000310* String 2: 20 bytes containing a single word.
000320*        (If String 2 is blank, we simply return the Soundex
000330*                 value for string 1 and skip the percentage
000340*                  calculations)
000350*
000360*    OUTPUTS:
000370* A return code: 1 byte. Zero means successful.
000380* The soundex value of string 1 (4 bytes)
000390* The soundex value of string 2 (4 bytes)
000400* The percentage match of the 2 soundexes. (100
000410* indicates a perfect match)
000420* This allows calling applications to implement "fuzzy logic"
000430* by allowing a range of match values (say, "better than 85%")
000440*
000450*
000460*
000470*    *******************************************************
000480 environment division.
000490 configuration section.
000500 source-computer. IBM-PC.
000510 object-computer. IBM-PC.
000520*------------------------  DATA   DIVISION  ---------------------
000530 data division.
000540*file section.
000550
000560 working-storage section.
000570
000580*
000590
000600 01  subscripts usage comp.
000610     12 J                pic s9(4).
000620     12 K                pic s9(4).
000630     12 L                pic s9(4).
000640
000650 01  alphabet-table.
000660     12 filler pic xx value 'A0'.
000670     12 filler pic xx value 'B1'.
000680     12 filler pic xx value 'C2'.
000690     12 filler pic xx value 'D3'.
000700     12 filler pic xx value 'E0'.
000710     12 filler pic xx value 'F1'.
000720     12 filler pic xx value 'G2'.
000730     12 filler pic xx value 'H0'.
000740     12 filler pic xx value 'I0'.
000750     12 filler pic xx value 'J2'.
000760     12 filler pic xx value 'K2'.
000770     12 filler pic xx value 'L4'.
000780     12 filler pic xx value 'M5'.
000790     12 filler pic xx value 'N5'.
000800     12 filler pic xx value 'O0'.
000810     12 filler pic xx value 'P1'.
000820     12 filler pic xx value 'Q2'.
000830     12 filler pic xx value 'R6'.
000840     12 filler pic xx value 'S2'.
000850     12 filler pic xx value 'T3'.
000860     12 filler pic xx value 'U0'.
000870     12 filler pic xx value 'V1'.
000880     12 filler pic xx value 'W0'.
000890     12 filler pic xx value 'X2'.
000900     12 filler pic xx value 'Y0'.
000910     12 filler pic xx value 'Z2'.
000920
000930
000940 01  alpha-chars redefines alphabet-table.
000950     12 sndx-entries occurs 26 indexed by x1.
000960        15 sndx-char      pic x.
000970        15 sndx-val       pic 9.
000980
000990 01  pc1                  pic s9(4) comp.
001000 01  pc2                  pic s9(4) comp.
001010 01  num-work.
001020     12 nw pic 9 occurs 3.
001030
001040 01  three-numbers                pic 999.
001050 01  filler redefines three-numbers.
001060     12 tn pic x occurs 3 indexed by x2.
001070
001080 01  string-work.
001090     12 in-char pic x occurs 20 indexed by x3.
001100
001110 01  last-string-1        pic x(20).
001120 01  last-string-2        pic x(20).
001130 01  last-soundx-1        pic x(4).
001140 01  last-soundx-2        pic x(4).
001150
001160*
001170 01  finish-flag pic x value zero.
001180     88 finished             value '1'.
001190*
001200*
001210*
001220 linkage section.
001230
001240 01  soundx-parms.
001250     12 sp-return-code                pic x.
001260        88 sp-soundx-ok                value '0'.
001270        88 sp-bad-first-chars          value '1'.
001280        88 sp-bad-char                 value '2'.
001290
001300     12 sp-string-1                    pic x(20).
001310     12 sp-string-2                    pic x(20).
001320     12 sp-soundx-1                    pic x(4).
001330     12 sp-soundx-2                    pic x(4).
001340     12 sp-percent                     pic 999.
001350*
001360/
001370 procedure division using soundx-parms.
001380 main section.
001390 main-start.
001400     perform a-initialise
001410     perform b-processing until finished
001420     perform c-close-down
001430     .
001440 return-to-caller.
001450     exit program.
001460*-----------------------------------------------------------------
001470 a-initialise section.
001480 a-0100.
001490     move zero to     three-numbers
001500                      sp-percent
001510                      pc1
001520                      pc2
001530     set sp-soundx-ok to true
001540     move zero to finish-flag
001550*
001560*  The first character in both strings must be
001570*  the same (required by the algorithm)
001580*
001590*
001600     if sp-string-1 (1:1) NOT = sp-string-2 (1:1)
001610                AND NOT
001620        (sp-string-1 (1:1) = space
001630                OR
001640            sp-string-2 (1:1) = space)
001650        set sp-bad-first-chars to true
001660        set finished to true
001670        go to a-9999
001680     else
001690        move sp-string-1 (1:1) to sp-soundx-1
001700        move sp-string-1 (1:1) to sp-soundx-2
001710     end-if
001720
001730*
001740* We can improve efficiency by setting the soundex
001750* value immediately, if either of the last strings was equal to
001760* either of the current strings. (This would be
001770* especially important in cases where the module
001780* is called in Batch...)
001790*
001800     if sp-string-1 NOT = last-string-1
001810        if sp-string-2 NOT = last-string-1
001820           if sp-string-1 NOT = last-string-2
001830              if sp-string-2 NOT = last-string-2
001840                 move zero to sp-soundx-1 (2:3)
001850                              sp-soundx-2 (2:3)
001860              else
001870                 move last-soundx-2 to sp-soundx-2
001880                 move zero to sp-soundx-1 (2:3)
001890           else
001900              move last-soundx-2 to sp-soundx-1
001910              move zero to sp-soundx-2 (2:3)
001920        else
001930           move last-soundx-1 to sp-soundx-2
001940           move zero to sp-soundx-1 (2:3)
001950     else
001960        move last-soundx-1 to sp-soundx-1
001970        move zero to sp-soundx-2 (2:3)
001980     end-if
001990     .
002000 a-9999.
002010     exit.
002020*-----------------------------------------------------------------
002030 b-processing          section.
002040 b000.
002050*
002060*   If the sp-soundx-1 and 2 fields have not been calculated
002070*   calculate them now...
002080*
002090*
002100     if sp-soundx-1 (2:3) = zero
002110        move function UPPER-CASE (sp-string-1)  to string-work
002120        perform s-calc-soundex
002130        move three-numbers to sp-soundx-1 (2:3)
002140     end-if
002150     if sp-string-2 = spaces
002160           set finished to TRUE
002170           go to b999
002180     end-if
002190     if sp-soundx-2 (2:3) = zero
002200        move function UPPER-CASE (sp-string-2) to string-work
002210        perform s-calc-soundex
002220        move three-numbers to sp-soundx-2 (2:3)
002230     end-if
002240*
002250*  Calculate the percentage match...
002260*
002270*
002280     perform s-calc-percentage-match
002290*
002300     set finished to true
002310     .
002320 b999.
002330     exit.
002340*-----------------------------------------------------------------
002350 c-close-down          section.
002360 c000.
002370     move sp-string-1             to last-string-1
002380     move sp-string-2             to last-string-2
002390     move sp-soundx-1             to last-soundx-1
002400     move sp-soundx-2             to last-soundx-2
002410     .
002420 c999.
002430     exit.
002440*-----------------------------------------------------------------
002450 s-calc-soundex        section.
002460 s000.
002470*
002480*   Scan the input string and calculate the Soundex value
002490*
002500* x1 = pointer to the alphabet (soundex value) table
002510* x2 = pointer to the output soundex code string
002520* x3 = pointer to the input text string
002530*
002540     set x2 to 1
002550     perform
002560        varying x3
002570           from 2
002580             by 1
002590          until x3 > 20
002600                  OR
002610                in-char (x3) = space
002620                  OR
002630                x2 > 3
002640                   set x1 to 1
002650                   search sndx-entries
002660                      at end
002670                         set sp-bad-char to true
002680                         set finished to true
002690                         go to return-to-caller
002700                      when
002710                         sndx-char (x1) = in-char (x3)
002720                         if sndx-val (x1) NOT = 0
002730                            move sndx-val (x1) to tn (x2)
002740                            set x2 up by 1
002750                         end-if
002760                   end-search
002770     end-perform
002780     .
002790 s999.
002800     exit.
002810*-----------------------------------------------------------------
002820 s-calc-percentage-match       section.
002830 scp000.
002840*
002850* Weight the numbers in the soundex code (4,2,1) then
002860* calculate them as a percentage of each other
002870*
002880     move sp-soundx-1 (2:3)               to num-work
002890     compute pc1 = nw (1) * 8 +
002900                   nw (2) * 2 +
002910                   nw (3)
002920     move sp-soundx-2 (2:3)               to num-work
002930     compute pc2 = nw (1) * 8 +
002940                   nw (2) * 2 +
002950                   nw (3)
002960
002970     if pc1 = zero OR pc2 = zero
002980        move zero to sp-percent
002990     else
003000        if pc1 < pc2
003010           compute sp-percent rounded = (pc1 * 100) / pc2
003020        else
003030           compute sp-percent rounded = (pc2 * 100) / pc1
003040        end-if
003050     end-if
003060     .
003070 scp999.
003080     exit.
003090*-----------  end of program  ------------------------------------


Cheers,

Pete



-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2011-10-06T21:50:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RamdnXYeKICcxhPTnZ2dnUVZ_jadnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:9f6nc8Fp2oU1@mid.individual.net...
> HeyBub wrote:
>> HeyBub wrote:
…[38 more quoted lines elided]…
>

Soundex can work well if you are dealing with a single language.  We used it 
at Group1 Software mail products and what worked well foe English names did 
not work well for Spanish names like those in Puerto Rico.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T15:41:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f777hF9a3U1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <RamdnXYeKICcxhPTnZ2dnUVZ_jadnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:9f6nc8Fp2oU1@mid.individual.net...
…[45 more quoted lines elided]…
> Puerto Rico.

But it was helpful for Puerto Ricans trying to search English names, right?

I used it in Europe for the same reasons. Temp staff from all over Europe 
were working in England and some of them did not speak or understand English 
very well. They loved it.

I'm wondering if there are different versions for other languages; it should 
just be a matter of adjusting the alphabet strings.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2011-10-10T22:57:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yv2dnY1reuQDLQ7TnZ2dnUVZ_u2dnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <RamdnXYeKICcxhPTnZ2dnUVZ_jadnZ2d@earthlink.com> <9f777hF9a3U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:9f777hF9a3U1@mid.individual.net...
> Charles Hottel wrote:
>> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[61 more quoted lines elided]…
>

I remember geting a magazine about AI and several issues had articles about 
how to tweek Soundex.  I no longer recall the details.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2011-10-11T22:33:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Be6dncTArqbzYQnTnZ2dnUVZ_vWdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <RamdnXYeKICcxhPTnZ2dnUVZ_jadnZ2d@earthlink.com> <9f777hF9a3U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:9f777hF9a3U1@mid.individual.net...
> Charles Hottel wrote:
>> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message


<snip>>>
>> Soundex can work well if you are dealing with a single language.  We
>> used it at Group1 Software mail products and what worked well foe
…[5 more quoted lines elided]…
>

IIRC we were using soundex as part of an address correction process.  The 
U.S. Postal Service sold tapes that contained every valid addreess in the 
U.S. and it's territories.  Using soundex on a misspelled street name might 
lead to the valid street name.  For English street names it was very 
successful but for Spanish street names it was poor.  I believe that a 
soundex designd specifically for Spanish would have been more sucessful.

<snip>
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2011-10-12T13:00:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mamdnSn4HdkrWgjTnZ2dnUVZ_r-dnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <RamdnXYeKICcxhPTnZ2dnUVZ_jadnZ2d@earthlink.com> <9f777hF9a3U1@mid.individual.net> <Be6dncTArqbzYQnTnZ2dnUVZ_vWdnZ2d@earthlink.com>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:Be6dncTArqbzYQnTnZ2dnUVZ_vWdnZ2d@earthlink.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[23 more quoted lines elided]…
>

Sondex reference:

AI Expert, March 1991,  page 15-17, "Pattern Recognition at the Phone 
Company: Soundex" by Mark Minasi

Covers basic ideas of soundex. Contains sample program in Pascal.  Discusses 
tailoring sondexto name groups, e.g. Ukranian and Hispanic and German. 
Contains a table of phonetic classificatio of some English consonants. 
Discusses multiletter combinations including some that soundes handles and 
some that it does not.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-07T16:52:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iImdnaI-SqQ86RLTnZ2dnUVZ_v6dnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> Might I ask why Soundex is inadequate for your purposes?

Well, one reason is that "CLANCY" and "KLANCY" generate different soundex 
codes.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-08T16:54:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f9vreFbs5U1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <iImdnaI-SqQ86RLTnZ2dnUVZ_v6dnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[5 more quoted lines elided]…
> .

OK. Know a lot of  Klancys do you?  :-)

Did you use the Soundex code at all?

I reckon it could be modified to eliminate the clanging Klancy problem...

I was amazed to see that this may actually be the very first time that code 
has been posted here without comment. I guess everyone is so jaded with 
COBOL they can't be bothered... :-) Or maybe it is just perfect code... :-)

Nah, it's too old to be perfect. Perfection is the province of the young.

Pete.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-08T10:23:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xfKdnXQtiLCS9g3TnZ2dnUVZ_jSdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <iImdnaI-SqQ86RLTnZ2dnUVZ_v6dnZ2d@earthlink.com> <9f9vreFbs5U1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> OK. Know a lot of  Klancys do you?  :-)

Er, no I don't know anybody named Klancy.

>
> Did you use the Soundex code at all?

I'm working on it.

>
> I reckon it could be modified to eliminate the clanging Klancy
> problem...

That's what the Metaphone algorithm tries to do.

>
> I was amazed to see that this may actually be the very first time
> that code has been posted here without comment. I guess everyone is
> so jaded with COBOL they can't be bothered... :-) Or maybe it is just
> perfect code... :-)

I'll comment!  I'll comment!  Just give me some time !
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-10T20:42:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bJSdnQ6IsNu5Ag7TnZ2dnUVZ_vOdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <iImdnaI-SqQ86RLTnZ2dnUVZ_v6dnZ2d@earthlink.com> <9f9vreFbs5U1@mid.individual.net> <xfKdnXQtiLCS9g3TnZ2dnUVZ_jSdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[21 more quoted lines elided]…
> I'll comment!  I'll comment!  Just give me some time !

Plodding along, I find the following names generate the same Soundex code:

Ford
Foard
Forte
Firth
Foret
Freed
Faherty
Forwood

Which hardly seems usable in looking for similar names. I mean who would 
mistake "Freed" for "Ford"?

Nevertheless, further experimentation is in progress.
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-12T11:09:02+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fjt3vF11pU1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <iImdnaI-SqQ86RLTnZ2dnUVZ_v6dnZ2d@earthlink.com> <9f9vreFbs5U1@mid.individual.net> <xfKdnXQtiLCS9g3TnZ2dnUVZ_jSdnZ2d@earthlink.com> <bJSdnQ6IsNu5Ag7TnZ2dnUVZ_vOdnZ2d@earthlink.com>`

```
HeyBub wrote:
> HeyBub wrote:
>> Pete Dashwood wrote:
…[36 more quoted lines elided]…
> would mistake "Freed" for "Ford"?

I think the idea is to find anything that is conceivably similar. A dyslexic 
person could easily mistake Freed for Ford :-)

Not sure how you are actually using it, but I used it to find similar names 
by sound, for people who were unfamiliar with English names. The sample ones 
were: Shakespeare, Shakzpeer, Sheikhspeare , and so on...  People could 
enter how the name sounded and be presented with a list of choices. Usually 
these had the first line of address attached so they could be visually 
matched on that as well. I'm sure it could be tweaked to make the hits finer 
if you think it is too broad a brush.

>
> Nevertheless, further experimentation is in progress.

There is no substitute for the empirical approach (well... modelling maybe 
:-))

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Metaphone (mumble-mumble)

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-10-11T16:59:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rei99759gun7v3jhqjm12llvefdkm8pihk@4ax.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com> <9f6nc8Fp2oU1@mid.individual.net> <iImdnaI-SqQ86RLTnZ2dnUVZ_v6dnZ2d@earthlink.com> <9f9vreFbs5U1@mid.individual.net> <xfKdnXQtiLCS9g3TnZ2dnUVZ_jSdnZ2d@earthlink.com> <bJSdnQ6IsNu5Ag7TnZ2dnUVZ_vOdnZ2d@earthlink.com> <9fjt3vF11pU1@mid.individual.net>`

```
On Wed, 12 Oct 2011 11:09:02 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Which hardly seems usable in looking for similar names. I mean who
>> would mistake "Freed" for "Ford"?
>
>I think the idea is to find anything that is conceivably similar. A dyslexic 
>person could easily mistake Freed for Ford :-)

Of course, Soundex also confuses "read" with "read", even though they
are pronounced differently.    Or "Bujold" with "Bujold", even though
one is pronounced in an Anglicized way and the other is still French.

-- 
"In no part of the constitution is more wisdom to be found,
than in the clause which confides the question of war or peace 
to the legislature, and not to the executive department." 

- James Madison
```

##### ↳ ↳ Re: Metaphone (mumble-mumble)

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-06T17:50:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<debs87d194tnkjolrec7rqbqg85hh6fffn@4ax.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <MKOdnTXvvs3KTRDTnZ2dnUVZ_gGdnZ2d@earthlink.com>`

```
On Thu, 6 Oct 2011 10:59:17 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>HeyBub wrote:
>
…[18 more quoted lines elided]…
>included at the above link.


I'm not a VB expert either, but I think the code is correct, assuming
that Peek(-1) does what I think it does.

The (not always clear) Metaphone rules are applied to the original
values of the string, and not the already transformed ones.  Basically
C *and* CK transform to K under rules 4 & 9 (unless C transforms to X
or S under 4).

The original descriptions were clearer - basically reversing the sense
of the rule in that a K following a C (which may have been transformed
under a different rule), is simply dropped (aka "silent").

So assuming that Peek(-1) returns the actual prior character of the
input stream, the VB code appears to be correct for this case (if it
finds a K, and the prior character was a C, it drops the character,
else it outputs a K).
```

#### ↳ UPDATE: Metaphone

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-18T10:35:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ib6dnbP8xs1DAQDTnZ2dnUVZ_vydnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
HeyBub wrote:

I've abandoned Metaphone.

Instead, I took Pete's original code and tweaked it for the letter "C" 
("Kane" and "Caine" generated different Soundex codes). My adjustments were 
taken from the Metaphone algorithm and are:

C ==> X if in "cia" or "ch"
else
  C ==> S if in "ci" "ce" or "cy"
  else
    SILENT if in "sci" or "sce" or "scy"
    else
      C ==>K

The above forces the following alterations:
S ==> X if before "h" or in "sio" or "sia"

T == X if in "tia" or "tio"
else
  T ==> "0" (zero) if before 'h'
  else
   T ==> SILENT if in "tch"

The above adjustments to the name are made before the Soundex code is 
generated.

This resolves the Caine/Kane issue as well as some other rare conditions.

I might employ other Metaphone transformations if some screwball names pop 
up.

Here's the Metaphone algorithm for "G"
C ==> SILENT if
  in "gh" and not at the end or before a vowel,
  in "gn" or "gned",
  in 'dge' 'dgy' or 'dgi'
C ==> J if before 'i' 'e' or 'y' and not part of 'gg'
else
C ==> K

What's art without suffering?
```

##### ↳ ↳ Re: UPDATE: Metaphone

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-19T11:26:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g6couFa8U1@mid.individual.net>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <Ib6dnbP8xs1DAQDTnZ2dnUVZ_vydnZ2d@earthlink.com>`

```
HeyBub wrote:
> HeyBub wrote:
>
…[40 more quoted lines elided]…
> What's art without suffering?

So, the combination of a little pre-processing, together with the posted 
Soundex code, has given you something better than the original. Good result.

Thanks for posting your pre-processes, Jerry.

I'll add them as notes to the original COBOL code.

I have always found the original code to be adequate to my needs but those 
needs have not been critical :-)

From now on I'll use your amendments.

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: UPDATE: Metaphone

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-19T22:56:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<st6v979ae6dg1qp27gi44scubofuhif0pq@4ax.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <Ib6dnbP8xs1DAQDTnZ2dnUVZ_vydnZ2d@earthlink.com>`

```
On Tue, 18 Oct 2011 10:35:57 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>HeyBub wrote:
>
…[40 more quoted lines elided]…
>What's art without suffering? 


I'm curious - why did you abandon Metaphone?
```

###### ↳ ↳ ↳ Re: UPDATE: Metaphone

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-21T09:30:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e-SdnY2ZzLZxHDzTnZ2dnUVZ_vmdnZ2d@earthlink.com>`
- **References:** `<3L2dnXas-7S5WRHTnZ2dnUVZ_uadnZ2d@earthlink.com> <Ib6dnbP8xs1DAQDTnZ2dnUVZ_vydnZ2d@earthlink.com> <st6v979ae6dg1qp27gi44scubofuhif0pq@4ax.com>`

```
Robert Wessel wrote:
> On Tue, 18 Oct 2011 10:35:57 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[47 more quoted lines elided]…
> I'm curious - why did you abandon Metaphone?

Because in most cases it generated a too short code, often just two letters. 
In a 10,000 name database, that meant hundreds of names to wade through.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
