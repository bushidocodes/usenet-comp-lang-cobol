[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Freeware tool and code to ponder on...

_107 messages · 15 participants · 2008-09 → 2008-10_

---

### Freeware tool and code to ponder on...

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-23T14:44:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jr3fmF4lc1iU1@mid.individual.net>`

```
A few weeks ago, I asked if anyone had a tool for calculating offsets and 
lengths "on-the-fly" in COBOL record layouts.

There were a number of responses and they were generally helpful, but Robert 
Wagner had a very nice little engine which he kindly agreed to make 
Freeware.

Robert posted his code and you can find it under the "cobdata" thread of 
this forum.

I had offered to wrap any suitable code and put it on .NET so we have been 
working together to get a deliverable product since then.

This exercise has been very interesting. I have never met Robert, just as I 
have never met most of you, but we had no problem working together to sort 
out the problems in bringing our little project to fruition.

There is such a wealth of talent here it would be good to see more joint 
working and sharing of different skill sets.

For myself, I will happily participate in and contribute to any such 
projects, on the understanding that it cannot be a full time effort and time 
may not always be available. (Think "back burner" projects, that really 
don't have a critical deadline).

This project has benefits far and beyond the provision of a simple little 
tool.

We are offering total access to all sources, so people can see how various 
effects were achieved. You can cut and paste our code, change it, re-use it, 
and are encouraged to do so.

I'm always rattling on about expanded skill sets. This project required the 
following (and you have full  download access to all of it...):

For the tool ("COBOL data structure analyser"):

1. Standard procedural COBOL.
2. OO COBOL.
3. C#

For the Deployment and the web site:

1. ASP.NET
2. JavaScript
3. Windows Script Hosting (VBScript)
4. C#
5. XML

The only tools I used were Fujitsu COBOL IDE and Visual Studio 2008 (which 
never stops amazing me as I find new stuff in it :-)), Robert may have used 
some other tools.

Conceptually, the project shows how Legacy COBOL can be quite easily 
leveraged onto a modern platform (.NET) and can play there with Classes and 
Objects written in other languages.

Please visit the Web site (it is intended to support this community) and 
download the tool. Remember when you run it, this is COBOL...:-)

ALL comments and observations should be posted to this forum. :-)

Here's the link: http://primacomputing.co.nz/cobdata

Enjoy!

Pete.
```

#### ↳ Here's one problem

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-24T15:47:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net>`

```
The following code:
...
  10 NSMAST-AUX PIC X.
  10 NSMAST--SO PIC X. *>redundant 8/06
  10 NSMAST-SYSTEM-SPARE PIC X(6).
05 NSMAST-ABOUT.
  10 NSMAST-IMPRINT PIC X(20).
...

Decodes as follows:

  30 10 nsmast-aux                      315   1
  31 10 nsmast--so                      316   1
  32 0* redundant                       317   6
  33 05 nsmast-about                    323 192
  34 10 nsmast-imprint                  323  20

Note the comment ("*>") is not handled correctly. Also the casing of the 
original is not honored.

I suspect that the funny way it handles comments also causes a miscount of 
the record size. In the case here, your program reports a size of 1655 bytes 
when the actual size is 2232.
```

##### ↳ ↳ Re: Here's one problem

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-25T10:48:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jvuedF5em0rU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com...
> The following code:
> ...
…[20 more quoted lines elided]…
> bytes when the actual size is 2232.
Excellent! Thanks for that.

Pretty sure Robert will get back on this.

Both of us tested the code extensively, but we were looking for things that 
would crash it.

I'm wondering if the double hyphen could be the culprit...it shouldn't be of 
course.

I ran your snippet and received the following:

    Lvl Name                            Pos Len Typ Oc
   1 10 nsmast-aux                        1   1
   2 10 nsmast--so                        2   1
   3 0* redundant                         3   6
   4 05 nsmast-about                      9  20
   5 10 nsmast-imprint                    9  20
        Record length                        28

The actual length is correct but it has certainly stumbled on the commented 
line.

The casing problem should be easily fixed.

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-25T11:02:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
> news:76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com...
…[44 more quoted lines elided]…
> commented line.

Okay, try this:

Example #1

Original:
10 NSVARY-NUMBERS.
  15 NSVARY-PRICES.
    20 NSVARY-SRP PIC S9(5)V99. *>1
    20 NSVARY-RETAIL PIC S9(5)V99. *>2
    20 NSVARY-RETAIL2 PIC S9(5)V99. *>3
    20 NSVARY-RETAIL3 PIC S9(5)V99. *>4
    20 NSVARY-LIST PIC S9(5)V99. *>5
    20 NSVARY-NET PIC S9(5)V99. *>6
    20 NSVARY-NET-AVG PIC S9(5)V99. *>7
    20 NSVARY-WHOLESALE PIC S9(5)V99. *>8
    20 NSVARY-SALE PIC S9(5)V99. *>9
    20 NSVARY-PRICE-QUAN1 PIC S9(5)V99. *>10
    20 NSVARY-PRICE-QUAN2 PIC S9(5)V99. *>11
    20 NSVARY-PRICE-SAVE1 PIC S9(5)V99. *>12
    20 NSVARY-PRICE-SPARE5 PIC S9(5)V99. *>13
    20 NSVARY-PRICE-SPARE4 PIC S9(5)V99. *>14
    20 NSVARY-PRICE-SPARE3 PIC S9(5)V99. *>15
    20 NSVARY-PRICE-SPARE2 PIC S9(5)V99. *>16
    20 NSVARY-PRICE-SPARE1 PIC S9(5)V99. *>17

Result:
119 10 nsvary-numbers                 1560   7
 120 15 nsvary-prices                  1560   7
 121 20 nsvary-srp                     1560   7
 122 0* 1                              1567   7
 123 0* 2                              1574   7
 124 0* 3                              1581   7
 125 0* 4                              1588   7
 126 0* 5                              1595   7
 127 0* 6                              1602   7
 128 0* 7                              1609   7
 129 0* 8                              1616   7
 130 0* 9                              1623   7
 131 0* 10                             1630   7
 132 0* 11                             1637   7
 133 0* 12                             1644   7
 134 0* 13                             1651   7
 135 0* 14                             1658   7
 136 0* 15                             1665   7
 137 0* 16                             1672   7
 138 0* 17                             1560  96

Line 119 is clearly not 7 bytes long.

Or this,
Example #2
10 NSVARY-INVOICE-GROUP.
  12 NSVARY-INVOICE OCCURS 6.
    15 NSVARY-INVOICE-NUMBER PIC X(20).
    15 NSVARY-INVOICE-VENDOR PIC X(6).
    15 NSVARY-INVOICE-RCV-DATE PIC X(8).
    15 NSVARY-INVOICE-DISC-X.
      20 NSVARY-INVOICE-DISC PIC 99V99.
    15 NSVARY-INVOICE-QUAN PIC S9(5).

Resulting in:
103 10 nsvary-invoice-group            797 378
 104 12 nsvary-invoice                  797 378      6
 105 15 nsvary-invoice-number           797 120      6
 106 15 nsvary-invoice-vendor           917  36      6
 107 15 nsvary-invoice-rcv-date         953  48      6
 108 15 nsvary-invoice-disc-x          1001 144      6
 109 20 nsvary-invoice-disc            1001 144     36
 110 15 nsvary-invoice-quan            1145  30      6

It seems confusing to decode this. INVOICE-NUMBER (line 105) may start in 
byte 797*, but it certainly does not continue for 120 bytes.

Example #3
Original
05 NSMAST-KEYS.
  10 NSMAST-TC PIC 9(7).
  10 NSMAST-TITLE PIC X(200).
  10 NSMAST-CONTRIB PIC X(75).
  10 NSMAST-AUTHOR REDEFINES NSMAST-CONTRIB PIC X(75).
  10 NSMAST-IDENTS.
    15 NSMAST-ISBN PIC X(20).
    15 NSMAST-ALT-ISBN PIC X(20).
  10 FILLER REDEFINES NSMAST-IDENTS.
    15 NSMAST-IDENT OCCURS 2 PIC X(20).
  10 FILLER REDEFINES NSMAST-IDENTS.
    15 NSMAST-ID1 PIC X(20).
    15 NSMAST-ID2 PIC X(20).
  10 NSMAST-KEY1-5.
    15 NSMAST-KEY1 PIC X(20).
    15 NSMAST-KEY2 PIC X(20).
    15 NSMAST-KEY3 PIC X(20).
    15 NSMAST-KEY4 PIC X(20).
    15 NSMAST-KEY5 PIC X(20).
  10 FILLER REDEFINES NSMAST-KEY1-5.
    15 NSMAST-KEY OCCURS 5 PIC X(20).
  10 NSMAST-ISBN13 PIC X(20).
05 NSMAST-SYSTEM.
  10 NSMAST-BINDING PIC X(3).
[...]

Resulting in:
   3 05 nsmast-keys                       1 442
   4 10 nsmast-tc                         1   7
   5 10 nsmast-title                      8 200
   6 10 nsmast-contrib                  208  75
   7 10 nsmast-author                   208  75
   8 10 nsmast-idents                   283  40
   9 15 nsmast-isbn                     283  20
  10 15 nsmast-alt-isbn                 303  20
  11 10 filler                          283  40
  12 15 nsmast-ident                    283  40      2
  13 10 filler                          283  40
  14 15 nsmast-id1                      283  20
  15 15 nsmast-id2                      303  20
  16 10 nsmast-key1-5                   283 100
  17 15 nsmast-key1                     283  20
  18 15 nsmast-key2                     303  20
  19 15 nsmast-key3                     323  20
  20 15 nsmast-key4                     343  20
  21 15 nsmast-key5                     363  20
  22 10 filler                          283 100
  23 15 nsmast-key                      283 100      5
  24 10 nsmast-isbn13                   283  20
  25 05 nsmast-system                   303  14
  26 10 nsmast-binding                  303   3
  27 10 nsmast-label                    306   3
[...]

If line 3 starts in 1 for a length of 442, line 25 seemingly should begin in 
byte 443, not 303 as reported.

-------
* It actually starts (according to the pencil-and-paper layout sheet) in 
byte 1021, but I'm still trying to deduce why the discrepency.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-25T19:22:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com>`

```
On Thu, 25 Sep 2008 11:02:11 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

>Okay, try this:
>
…[45 more quoted lines elided]…
>Line 119 is clearly not 7 bytes long.

The problem went away when I fixed comments beginning *>

>Or this,
>Example #2
…[20 more quoted lines elided]…
>byte 797*, but it certainly does not continue for 120 bytes.

It has a length of 6 * 20 = 120. Internally, the program propagates OCCURS 6 to each
subordinate element. It propagated it to group name NSVARY-INVOICE-DISC-X, which it then
propagated AGAIN, in error,  to NSVARY-INVOICE-DISC, causing it to occur 36. I fixed that
bug. When I put OCCURS 2 on DISC-X, its subordinate correctly occurred 12. 

Total length is now correct. Changing offsets to the first group would be easy, I added it
to the list of enhancements.

>Example #3
>Original
…[55 more quoted lines elided]…
>byte 443, not 303 as reported.

Good catch. 442 is correct, the offsets were wrong starting from NSMAST-KEY1-5. 
When it encountered that, it had not yet calculated the length of group name
NSMAST-IDENTS, so failed to add 40 to offset 283. 

Here is the result after I fixed the bug:

    Lvl Name                            Pos Len Typ Occ
   2 05 nsmast-keys                       1 442
   3 10 nsmast-tc                         1   7
   4 10 nsmast-title                      8 200
   5 10 nsmast-contrib                  208  75
   6 10 nsmast-author                   208  75
   7 10 nsmast-idents                   283  40
   8 15 nsmast-isbn                     283  20
   9 15 nsmast-alt-isbn                 303  20
  10 10 filler                                 283  40      2
  11 15 nsmast-ident                    283  40      2
  12 10 filler                                 283  40
  13 15 nsmast-id1                      283  20
  14 15 nsmast-id2                      303  20
  15 10 nsmast-key1-5                   323 100
  16 15 nsmast-key1                     323  20
  17 15 nsmast-key2                     343  20
  18 15 nsmast-key3                     363  20
  19 15 nsmast-key4                     383  20
  20 15 nsmast-key5                     403  20
  21 10 filler                                   323 100      5
  22 15 nsmast-key                      323 100      5
  23 10 nsmast-isbn13                   423  20
  24 05 nsmast-system                   443   3
  25 10 nsmast-binding                  443   3
        Record length                       445

Thanks for finding these bugs.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-09-25T22:49:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`

```
I don't think it handles usage pointer correctly, but that may be machine 
dependent.

input:

       01  TCB.
           05  FILLER             PIC X(08).
           05  DEB-ADDR                     USAGE IS POINTER.
           05  TIOT-POINTER                 USAGE IS POINTER.
           05  FILLER             PIC X(164).
           05  JSCB-POINTER                 USAGE IS POINTER.
           05  FILLER             PIC X(128).
           05  STCB-POINTER                 USAGE IS POINTER.

output:

  Lvl Name                            Pos Len Typ Oc
   1 01 tcb                               1 300
   2 05 filler                            1   8
   3 05 deb-addr                          9
   4 05 tiot-pointer                      9
   5 05 filler                            9 164
   6 05 jscb-pointer                    173
   7 05 filler                          173 128
   8 05 stcb-pointer                    301
        Record length                       300
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-25T20:03:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com>`

```
On Sep 26, 2:49 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> I don't think it handles usage pointer correctly, but that may be machine
> dependent.
…[23 more quoted lines elided]…
>         Record length                       300

Let me just think about whether USAGE POINTER is useful in a file
record.  ... ... ...
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-26T16:26:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k36k0F5soprU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com>`

```


"Richard" <riplin@azonic.co.nz> wrote in message 
news:28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com...
> On Sep 26, 2:49 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
>> I don't think it handles usage pointer correctly, but that may be machine
…[28 more quoted lines elided]…
>
Yes, I have never seen it used in a file. However, the stated purpose of the 
tool is to handle COBOL structure blocks (which could be in 
working-storage), so I think Charlie has a point.

Robert has already developed fixes for the items raised by HeyBub and I'll 
be applying them and re-publishing the product in the next hour or so.

I am blown away by the contributions to this, especially HeyBub's...

Thanks to all concerned.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-26T10:59:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Richard" <riplin@azonic.co.nz> wrote in message
> news:28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com...
…[39 more quoted lines elided]…
>

Well, you're welcome. As long as you're soliciting suggestions, how about 
indentation for levels? That is, massage the output so it looks like:

 103 10 nsvary-invoice-group            797 378
 104     12 nsvary-invoice                  797 378      6
 105         15 nsvary-invoice-number           797 120      6
 106         15 nsvary-invoice-vendor           917  36      6
 107         15 nsvary-invoice-rcv-date         953  48      6
 108         15 nsvary-invoice-disc-x          1001 144      6
 109             20 nsvary-invoice-disc            1001 144     36
 110         15 nsvary-invoice-quan            1145  30      6

At first blush, if I were attacking this "feature" I'd tabulate all the 
input level numbers that exist on the first pass, sort them*, and assign 
increasing spaces to each level. Then, when producing the output, I'd imbed 
the correct number of spaces for each level number. You'd have to normalize 
a level '7' and level '07,' but that's pretty easy.

'Course this would break down for 66, 77, and 88 levels, but who uses 66 & 
77 anyway?

----
* Hint: Using an ISAM file for the level numbers would simultaneously sort 
and eliminate duplicates.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-27T04:56:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k4iieF613aaU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net> <sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com...
> Pete Dashwood wrote:
>> "Richard" <riplin@azonic.co.nz> wrote in message
…[66 more quoted lines elided]…
>

Yeah, right... or a database maybe...  :-)

Unfortunately, there was a problem with the amended code and it cannot be 
published just yet. (There's a fairly lengthy process it has to go through 
to end up on the server, and some of these steps are tricky). It failed a QA 
step and we are looking at it.

As soon as the fixes are in and we are happy that it passes QA it will be 
re-released.

As for indentation, that thought struck me too, pretty early on in the 
piece, when I was amending my own code. It really isn't worth the effort, in 
my opinion, although Robert may feel dfferently and decide to do it.

The code is public. (well, actually it isn't until it is finalised and if 
you try and get it you will be introduced to Heisenberg) so there is nothing 
to stop you putting indentation into it if you really want to, Jerry :-)

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-09-26T17:36:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<146dnVVp7NFByEDVnZ2dnUVZ_oTinZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net> <sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com> <6k4iieF613aaU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6k4iieF613aaU1@mid.individual.net...
>
>
…[96 more quoted lines elided]…
>

Hell, while you are at it how about a 2002 standard compatible compiler. 
Robert can probably reel one off in his spare time.  It should corner the 
market!  .
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-27T11:57:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k5b7pF5t5kpU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net> <sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com> <6k4iieF613aaU1@mid.individual.net> <146dnVVp7NFByEDVnZ2dnUVZ_oTinZ2d@earthlink.com>`

```


"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:146dnVVp7NFByEDVnZ2dnUVZ_oTinZ2d@earthlink.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[104 more quoted lines elided]…
> market!  .

Don't encourage him, Charlie :-)

The man's a COBOL coding maniac... :-) I think every delay in this project 
has been down to me and not to Robert. :-) He has done an outstanding job on 
this. I tested that engine for days and couldn't crash it...of course, I 
don't have HeyBub's perspicacity, but to be fair, he didn't crash it, he 
just got a wrong result....hmmm, perhaps that counts as "crashing" :-)...

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T19:45:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sqvqd4hpi3ljvg3586t0tbld91jpo5n7ht@4ax.com>`
- **References:** `<76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net> <sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com> <6k4iieF613aaU1@mid.individual.net> <146dnVVp7NFByEDVnZ2dnUVZ_oTinZ2d@earthlink.com>`

```
On Fri, 26 Sep 2008 17:36:40 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:

>
>Hell, while you are at it how about a 2002 standard compatible compiler. 
>Robert can probably reel one off in his spare time.  It should corner the 
>market!  . 

What is The Market? Amateurs seeking a free compiler? Open COBOL hasn't been a resounding
success. 

What platform should it target -- native, JVM or .NET? Compilers for the latter two
haven't been best sellers. 

I seriously considered, and even started to write, a Cobol compiler a few years ago. Then
decided it's a no-win. I'd love to be convinced otherwise.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 12)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-09-26T23:33:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZJOdnbCxy6ziNEDVnZ2dnUVZ_tHinZ2d@earthlink.com>`
- **References:** `<76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net> <sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com> <6k4iieF613aaU1@mid.individual.net> <146dnVVp7NFByEDVnZ2dnUVZ_oTinZ2d@earthlink.com> <sqvqd4hpi3ljvg3586t0tbld91jpo5n7ht@4ax.com>`

```
Comments below:

"Robert" <no@e.mail> wrote in message 
news:sqvqd4hpi3ljvg3586t0tbld91jpo5n7ht@4ax.com...
> On Fri, 26 Sep 2008 17:36:40 -0400, "Charles Hottel" 
> <chottel@earthlink.net> wrote:
…[8 more quoted lines elided]…
> success.

I don't think there is one.  I once thought of writing one but it seemed the 
cause was already lost, so I never started.

>
> What platform should it target -- native, JVM or .NET? Compilers for the 
> latter two
> haven't been best sellers.

Just write three backends :-)  Think of all you could learn in the process.

>
> I seriously considered, and even started to write, a Cobol compiler a few 
> years ago. Then
> decided it's a no-win. I'd love to be convinced otherwise.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T19:28:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gquqd49ojr03oc9k5tgr0ji12pbb01619u@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <28dd627f-78d6-4ab9-834b-5dd6b72aeab9@z6g2000pre.googlegroups.com> <6k36k0F5soprU1@mid.individual.net> <sc6dnc77ZN15m0DVnZ2dnUVZ_r7inZ2d@earthlink.com>`

```
On Fri, 26 Sep 2008 10:59:31 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

>Pete Dashwood wrote:
>> "Richard" <riplin@azonic.co.nz> wrote in message
…[52 more quoted lines elided]…
> 110         15 nsvary-invoice-quan            1145  30      6

That's a pretty good suggestion.

>At first blush, if I were attacking this "feature" I'd tabulate all the 
>input level numbers that exist on the first pass, sort them*, and assign 
>increasing spaces to each level. Then, when producing the output, I'd imbed 
>the correct number of spaces for each level number. You'd have to normalize 
>a level '7' and level '07,' but that's pretty easy.

The program already normalizes '7' to '07'.

>'Course this would break down for 66, 77, and 88 levels, but who uses 66 & 
>77 anyway?

It wouldn't break down, they'd be one notch in from the highest level used.

>* Hint: Using an ISAM file for the level numbers would simultaneously sort 
>and eliminate duplicates.

This illustrates the difference between applications and systems programmers. If I
seriously considered using such a brute force tool, I'd be senile, just shoot me.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-25T23:29:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qkood4l0p3k15b5v7u61prjkhv9eit0iik@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com>`

```
On Thu, 25 Sep 2008 22:49:38 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:

>I don't think it handles usage pointer correctly, but that may be machine 
>dependent.
…[23 more quoted lines elided]…
>        Record length                       300

It doesn't do pointers because the size of a pointer is controlled with compiler options
that a) might not be available to cobstruct and b) are stored in a different place for
each compiler. 

TYPEDEF would be the best way to define the length of a pointer -- as COMP PIC S9(9) or
S9(18). I might consider adding typedef support.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-26T07:51:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uW4Dk.1051$hc1.884@flpi150.ffdc.sbc.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <qkood4l0p3k15b5v7u61prjkhv9eit0iik@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:qkood4l0p3k15b5v7u61prjkhv9eit0iik@4ax.com...
> On Thu, 25 Sep 2008 22:49:38 -0400, "Charles Hottel" 
> <chottel@earthlink.net> wrote:
>
>>I don't think it handles usage pointer correctly, but that may be machine
>>dependent.

I know,  I know:  I need to download and try it first but...

I would think  both SIZE("USAGE IS POINTER" items) and ALIGNMENT (i.e, byte, 
word) would be 'setup' or 'user preferences'  options, and you could change 
at will for any one 'run' or 'session.'

(Probably more things, too; but POINTER is 'on point' * here and alignment 
leaped into my head).

Since it's likely any one user will almost always be analyzing code created 
for one specific compiler/compiler options/operating system, allowing him to 
set defaults sounds reasonable.

MCM
* inadvertent. I have no plans to give up my day job.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-27T04:58:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k4ilrF63tbfU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2dnZ2d@earthlink.com> <qkood4l0p3k15b5v7u61prjkhv9eit0iik@4ax.com> <uW4Dk.1051$hc1.884@flpi150.ffdc.sbc.com>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:uW4Dk.1051$hc1.884@flpi150.ffdc.sbc.com...
> "Robert" <no@e.mail> wrote in message 
> news:qkood4l0p3k15b5v7u61prjkhv9eit0iik@4ax.com...
…[17 more quoted lines elided]…
> allowing him to set defaults sounds reasonable.

Even more reasonable if he was paying for it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-09-27T14:23:18
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222521798@f1.n250.z2.fidonet.ftn>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`

```
<76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com>
<6jvuedF5em0rU1@mid.individual.net>
<TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com>
<i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <SoOdnRIf_tAk0EHVnZ2dnUVZ_u2
Hello Pete!

26 Sep 08 05:26, Pete Dashwood wrote to All:

 PD> I am blown away by the contributions to this, especially HeyBub's...

 PD> Thanks to all concerned.

I tried to get a copy of the cobol source but your site(web) seems somewhat 
broken and I have tried with both Firefox (v3.0.1) and Konqueror ie, seeing 
the 'download source' tag at top of page (and at bottom) tried to double click 
both and does not respond. Seems to show it as a text field and not a link.

Would the source work with Open Cobol as I would like to link the code into a 
cobol xreference tool (cobxref) I have placed on to sourceforge?


Vince
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-09-27T10:08:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn>`

```

"Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
news:1222521798@f1.n250.z2.fidonet.ftn...
> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com>
> <6jvuedF5em0rU1@mid.individual.net>
…[27 more quoted lines elided]…
>
I had the same problem.  Try viewing the license first.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-09-27T22:17:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kzDDk.24119$e82.19695@newsfe10.iad>`
- **In-Reply-To:** `<xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
> news:1222521798@f1.n250.z2.fidonet.ftn...
…[34 more quoted lines elided]…
> 
Now this one definitely raises an issue and it is design (systems 
analysis), not programming. Problem is as the designer Pete is both 
designer and programmer, and so close to what is intended, and 
sequences can be misinterpreted and god knows what the 'events' do if 
you hit different method sequences from button clicks.

I can't recall, but I think your license is no big deal, just a caveat 
and 'do this first before anything else'. Why not make that button "Read 
License First" and either hide or disable any remaining buttons until 
they do anything else. That's not the complete story but hopefully you 
get the tenure of what I'm saying. (Before I get back to your project I 
definitely had your dialog popping up three times for me to sign in, 
even though I had already entered my name and a password - the name 
showed up on subsequent shots of the dialog but with the password blank).

Now this problem is not poking at what you have done, but let's take 
some experiences I have just had in the last couple of days.

That clean-up tool Trend Micro Housecalls - brought it up first time and 
stated 'Submit' for a scan - oodles of errors. I say 'oodles' because 
unlike so many of the other clean-up tools it didn't do a summary page, 
giving you a count and then expanding on a treeview to look at specific 
details.

I'll digress now to MS Security SP3. Well they have obviously updated it 
since I looked in April because the dialogs have changed. I can assure 
you, back then "Updates not actioned....." and not one single Error 
Code. I don't know about Error Codes in the latest version. I got it 
going, walked the dogs and when I came back it had successfully done its 
update which was supplemented by two items which would be done on 
Restart. Goody, goody - looks like I'm fairly 'clean' apart from my 
Lexmark printer - did it before; I'll uninstall and re-install.

I take another shot at Trend Micro Housecalls, having had success on SP3 
- I now get their launch dialog with two checkboxes; second is 
customized selection. Click to go - now shows their Java Routine "Scan 
All" but no way to do the customization, even if I wanted to. Click to 
continue, pause in their dialog box and then an ErrorMessage Box 
something about "Invalid binding", and no error code or suggested 
remedial action. Yes the precise entry in that messasgebox is contained 
in the e-mail I sent to them for help - but the e-mail was in their 
dialog, so I'm left without a copy. That's about two days ago and no 
reply back from them.

Anyway even with that error message I let the bloody thing run - this 
time I had zero errors, apparently. How the hell am I supposed to know 
whether the run was kosher or not ? (Remember it's not just us computer 
geeks running this type of software).

Try this one - Expedia an on-line airline booking agency - Eileen is 
going to visit our daughter in Ancaster, On., We fly Westjet, currently 
Canada's #2 airline and a cheapie with no frills. My daughter probably 
flies a minimum of once per month whereas yours truly has flown about 5 
times since I first got here in '75. She is used to all this crap and 
recommends we book through Expedia. Not too much complicated, departure 
and arrival points. Latter happens to be Hamilton - hiccups on that 'cos 
there's more than one Hamilton so I can select Hamilton, ON from the 
drop down. Start date, if return, return date, adult or senior (although 
I think it ignored the latter choice). It selected Westjet - they are 
the only ones that fly into Hamilton so initially I get all the flights 
for that departure date with the $price. Choose a late one which is 
cheaper. Same routine prompting for return journey. Select the two 
journeys and it gives itemised pricing. Because of aviation fuel prices 
I read in the paper the same day, Westjet had reduced their 'additional 
charge' slightly. Ok button on original  price, message it is going to 
recalculate which it does reducing the ticket by $60 on the Westjet 
charge. Good for them - they are honest.

I pay on-line from my plastic. Honky Dory - all is OK; here is your ID 
and the route details - but not printed. So although a first time user 
not a bad experience and they subsequently e-mail, two messages, 
confirming the booking and insurance coverage. Now I'm waiting for 
confirmation from Westjet.

Eileen phoned Anna this morning, who asked for the flight details; well 
we weren't sure so let's take a look firstly at Expedia. Absolutely 
bugger-all in their menu bar and no search box. I filled in one box, 
hopefully, although I guessed it was suspect which prompted me for name 
and a password. Didn't like my password - which I am concrete sure of, 
but just in case put in another I use. Result - poof ! New dialog 
telling me I can change the password and then I get an e-mail saying do 
it within 24 hours.

Sod Expedia, let's goggle and try Westjet for confirmation. Search 
phrases like 'confirm reservation' etc., produced nothing. If I put 
departure and return points and dates in I got a schedule of flights 
with prices. Being totally computer literate, (she still asks 'Where's 
the cursor you tell me you are pointing at"), Eileen tries the old 
fashioned way, contacts  Westjet on the phone. It appears human beings 
are incredibly more flexible than computers, we get all the information 
we need - and the good lady immediately e-mailed it to us.

Why the dis-connect between Expedia and Westjet ? Expedia doesn't pass 
your e-mail address on to Westjet who are then not able to contact you 
direct. And why ? If Westjet has your e-mail address they could have 
by-passed Expedia and sold me a ticket direct !!!!!!!

I do love all this fancy stuff now in EDP (Oops let's get with it, it's 
become "IT"). Had I continued in a programming mode I would have needed 
to take a look at the Web. Can you imagine my reaction when I got my 
first blue screen in Firefox, my browser of choice. "What the F *** !!!!!".

Jimmy
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-28T21:19:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k8t0jF6jmogU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:kzDDk.24119$e82.19695@newsfe10.iad...
> Charles Hottel wrote:
>> "Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
…[38 more quoted lines elided]…
> different method sequences from button clicks.

The events are written in C# and run on the server as compiled code. The 
sequence in which they occur has no bearing on anything. You can click 
buttons in any sequence you like; each event is encapsulated.

There are no (intentional) event dependencies on the site.

You cannot enable the menu until you have viewed the Licence. (Actually, it 
probably IS possible but not easy and not intended to be done that way...)

When you click the "OK noted" button it raises a click event which amends 
the Master Page where the menus live. It also sends a signal back to an 
invisible "traffic cop" page, which tells it that you have seen the menu.

>
> I can't recall, but I think your license is no big deal, just a caveat and 
> 'do this first before anything else'. Why not make that button "Read 
> License First" and either hide or disable any remaining buttons until they 
> do anything else.

Because they may not want to download, (in which case there is no need for 
them to ever read the Licence), may have no intention of ever downloading, 
and that would be forcing them to do something there is no necessity for 
them to do. If I hid stuff untill they read the Licence I would be depriving 
them of stuff I am very happy for them to look at. The design criterion 
is:"Only make them do stuff when they have indicated they want to achieve a 
certain result" Note that you don't HAVE to logon. You can still access all 
the diagrams and documents. Only when you decide that you want to download, 
are you required to log on, and at that point, if you HAVEN'T logged on, you 
are taken to a page that lets you do so. If you have already logged on you 
are taken to the download page for whatever you wanted to download.

>That's not the complete story but hopefully you get the tenure of what I'm 
>saying. (Before I get back to your project I definitely had your dialog 
>popping up three times for me to sign in, even though I had already entered 
>my name and a password - the name showed up on subsequent shots of the 
>dialog but with the password blank).

OK, I'd need to know if you used the logon boxes on the home page. If you 
log in once and get acknowledged as being logged in and told to click the 
resume button, you should NOT be reqired to login again. (Clicking the 
download menu should recognise you are logged in and take you directly to 
the download at any time after that.) HOWEVER, if, having successfully 
logged in, you then use the login box on the Home page AGAIN, it will cancel 
your existing login and require you to do it again. The best way to download 
is to do the following:

1. Read the Licence.
2. Click the now enabled "Download executables" menu.
    You will be taken immediately to a logon page. (If you have previously 
logged on from the home page, you SHOULD be taken to the download page 
directly. If you are not, it may be because cookies are not enabled on your 
Browser...or it may be a bug in my code-behind page code.)

3. Do the logon. If you are not registered, you will be given the chance to 
register without having to re-key your email address.

4. If the logon/registration succeeds you will receive a message thanking 
you for your logon. The message causes another button marked "Resume" to 
become visible. Click this button and you are taken to the Download page.

If this process does not succeed, or you back out of it or it fails for any 
other reason, you will need to repeat the process before you can download.

Unless you can tell me the exact sequence of what you did and what it said, 
I can't really do much. As far as I know the process works.

>
> Now this problem is not poking at what you have done, but let's take some 
…[6 more quoted lines elided]…
> details.

Nevertheless, it is an excellent tool in terms of its stated purpose: to 
find and destroy malware on your system.

>
> I'll digress now to MS Security SP3. Well they have obviously updated it 
…[6 more quoted lines elided]…
> it before; I'll uninstall and re-install.

Installing SP3 does NOT "clean" your system in any way. It simply closes 
down existing vulnerabilities.
>
> I take another shot at Trend Micro Housecalls, having had success on SP3 - 
…[13 more quoted lines elided]…
>

The non-computer people have less trouble with software because they take 
the time to read each screen, do not "expect" a certain behaviour, and just 
do what it says. For most of us we don't do that. As a result, we often 
experience frustration with modern software.

> Try this one - Expedia an on-line airline booking agency - Eileen is going 
> to visit our daughter in Ancaster, On.,

I use Expedia all the time and find their site very well laid out.


>We fly Westjet, currently Canada's #2 airline and a cheapie with no frills. 
>My daughter probably flies a minimum of once per month whereas yours truly 
…[16 more quoted lines elided]…
> the route details - but not printed.

It won't print unless you ask it to... You can ask it to easily from the 
menus. You can also mail the page to yourself as "belt and braces" In fact, 
if you simply note the ID, the details and the confirmation number on a 
piece of paper (with a pencil) they will STILL issue your electronic ticket 
at the airport when you check in.


>So although a first time user not a bad experience and they subsequently 
>e-mail, two messages, confirming the booking and insurance coverage. Now 
>I'm waiting for confirmation from Westjet.
>
If you have a confirmed ID from Expedia you need nothing more.

> Eileen phoned Anna this morning, who asked for the flight details; well we 
> weren't sure so let's take a look firstly at Expedia.

Should have printed (or noted) the details on the schedule page. Doesn't 
matter. As long as you have your confirmation you can access the Expedia 
site and recall the details.


> Absolutely bugger-all in their menu bar and no search box. I filled in one 
> box, hopefully, although I guessed it was suspect which prompted me for 
…[13 more quoted lines elided]…
>

So, at least for you and Eileen, dealing with a human is a more comfortable 
experience than dealing with a computer. Fair enough. Such is not the case 
for everyone, though. There is no "right" or "wrong" here, just what works 
for you. Like I said, I use Expedia all the time and find it very useful and 
easy. That is not a criticism of you; just an observation that there is much 
diversity in the world and some of us like different approaches.


> Why the dis-connect between Expedia and Westjet ? Expedia doesn't pass 
> your e-mail address on to Westjet who are then not able to contact you 
> direct. And why ? If Westjet has your e-mail address they could have 
> by-passed Expedia and sold me a ticket direct !!!!!!!

Expedia may have bought blocks of seats from Westjet. Westjet may have 
decided they don't want the hassles of dealing with customers and are happy 
to outsource that to Expedia, we could speculate all day. The fact is that 
both companies are happy with the arrangement (or they wouldn't be in it...)

No comment other than "YMMV" :-) Like I said, I use Expedia (and a couple of 
others) all the time and haven't used a travel agent for around 15 years. 
Online travel booking is brilliant. My housekeeper needed a flight to visit 
her sister the other day. She doesn't have a computer and visited several 
TAs to get quotes. The cheapest she got was $1043.00. I got on the web and 
got the same flights for $600.00. She was chuffed :-)

>
> I do love all this fancy stuff now in EDP (Oops let's get with it, it's 
> become "IT"). Had I continued in a programming mode I would have needed to 
> take a look at the Web. Can you imagine my reaction when I got my first 
> blue screen in Firefox, my browser of choice. "What the F *** !!!!!".

Web programming is a lot more complex than many people realise. 
Nevertheless, it is fun and very rewarding when people actually use what you 
wrote.

I hope you have revisited the site, Jimmy, as it now renders very well in 
Firefox (including the Licence agreement). The documents and diagrams are 
working fine in Firefox too, much to my relief.

It is still interesting to me that Deamweaver (a non-MicroSoft product) can 
create a simple table (6 rows, 2 columns) with very basic HTML. Yet, when 
viewed in Firefox the table is a disaster with columns skewed and requires 
extra tags or CSS to correct it. The same table in IE renders correctly with 
no additional help.

Let me have more details about your logon problem and I'll look at that too.

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-09-28T12:43:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222627008_3050@isp.n>`
- **In-Reply-To:** `<6k8t0jF6jmogU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:kzDDk.24119$e82.19695@newsfe10.iad...
…[52 more quoted lines elided]…
> invisible "traffic cop" page, which tells it that you have seen the menu.


I'm sure you considered this but may I suggest that the "View License"
requirement be part of the "actions" resulting from selecting the
download options rather than being a separate required action of the
main page?

Logically, you only want the user who's intending to download to read
and accept the license terms before proceeding (as you indicate below.)
Additionally, the user must register/logon before downloading. Having
the "View License" function on the main page is fine, but clicking the
"Download ..." items should go down the view/accept/register/logon path
as is required rather than being optionally enabled after license stuff
processing.

IMHO.  8-)


>> I can't recall, but I think your license is no big deal, just a caveat and 
>> 'do this first before anything else'. Why not make that button "Read 
…[207 more quoted lines elided]…
> 

Jeff


----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-29T12:28:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kai88F5cijpU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <1222627008_3050@isp.n>`

```


"Jeff Campbell" <n8wxs@arrl.net> wrote in message 
news:1222627008_3050@isp.n...
> Pete Dashwood wrote:
>> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
…[73 more quoted lines elided]…
>

Yes, on reflection, I think you're right Jeff.

I simply can't afford the time to change it right now, but conceptually you 
are on the button.

I might change it so that once they logon they don't need to view the 
Licence. (It appears as part of the install process anyway.)

Thanks for the comment.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-28T11:52:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net>`

```
On Sep 28, 9:19 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> You cannot enable the menu until you have viewed the Licence. (Actually, it
> probably IS possible but not easy and not intended to be done that way...)
>

The problem that I see is that the menu and splash screen show up on
the page and the 'view licence' is 3 pages down with no link between
the two. A viewer will see that the menu doesn't work and simply think
that the site doesn't work.

IMHO it would be better if the menu worked but did different things.
So clicking 'download' put up a message 'read the licence and agree
first', rather than simply being broken.

> Because they may not want to download, (in which case there is no need for
> them to ever read the Licence),
…[5 more quoted lines elided]…
> certain result"

The implementation is 'I am broken until you work it out for
yourself'.


> Unless you can tell me the exact sequence of what you did and what it said,
> I can't really do much. As far as I know the process works.

That's now sounding like a support call. Asking a user to indicate the
exact sequence of what they did is usually not productive. They
probably can only remember half of what was done, and get the sequence
wrong.

>
> The non-computer people have less trouble with software because they take
> the time to read each screen, do not "expect" a certain behaviour, and just
> do what it says.

They wouldn't be called 'users' if they did that.

> For most of us we don't do that. As a result, we often
> experience frustration with modern software.

I avoid software that does not do what I tell it to do. In particular
"Microsoft knows best" Windows.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-29T12:31:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kaiemF6u5qrU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com>`

```


Richard" <riplin@azonic.co.nz> wrote in message 
news:27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com...
On Sep 28, 9:19 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> You cannot enable the menu until you have viewed the Licence. (Actually, 
> it
> probably IS possible but not easy and not intended to be done that way...)
>

The problem that I see is that the menu and splash screen show up on
the page and the 'view licence' is 3 pages down with no link between
the two. A viewer will see that the menu doesn't work and simply think
that the site doesn't work.

IMHO it would be better if the menu worked but did different things.
So clicking 'download' put up a message 'read the licence and agree
first', rather than simply being broken.

[Pete]

Yep. Jeff made the same point. I agree. I'll fix it as soon as I can spare 
the time.

> Because they may not want to download, (in which case there is no need for
> them to ever read the Licence),
…[7 more quoted lines elided]…
> certain result"

The implementation is 'I am broken until you work it out for
yourself'.


> Unless you can tell me the exact sequence of what you did and what it 
> said,
> I can't really do much. As far as I know the process works.

That's now sounding like a support call. Asking a user to indicate the
exact sequence of what they did is usually not productive. They
probably can only remember half of what was done, and get the sequence
wrong.

[Pete]

Nevertheless, it is as far as I can go at the moment.

>
> The non-computer people have less trouble with software because they take
> the time to read each screen, do not "expect" a certain behaviour, and 
> just
> do what it says.

They wouldn't be called 'users' if they did that.

> For most of us we don't do that. As a result, we often
> experience frustration with modern software.

I avoid software that does not do what I tell it to do. In particular
"Microsoft knows best" Windows.

[Pete]

Yes, Richard... :-)

Thanks for your post.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-09-29T15:55:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oacEk.465$ex3.296@newsfe02.iad>`
- **In-Reply-To:** `<6kaiemF6u5qrU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Richard" <riplin@azonic.co.nz> wrote in message 
> news:27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com...
…[51 more quoted lines elided]…
> 

Richard is right on the button, but I also accept that you can't follow 
it up from the brief sequence I gave you; as an off-chance, thought just 
maybe you 'might'.....   Suggestion - delete me and my password from 
your DB and when you signal that the whole thing is complete - including 
Heidleberg/Hesleberg or whatever his bloody name was, I'll give it a 
shot from point zero, and yes, I'll scribble down each step I take. (Of 
course when we see something on the Web we presume it is working and 
never think of doing an 'audit trail' to confirm cock-ups we may make).

Of course I don't make cock-ups, and as you already know, or should 
know, to while away my dotage, as a hobby I design jet-engines for 
airliners .........yeah.

Now why Heidleberg etc... You once had a cartoon for Gipetto - if I have 
that right I can associate it. I immediately think of Pinocchio doing 
his little dance routine for Stromboli :-

"I-ve........
Got no strings to hold me down,
da, da, da, da
........."

> [Pete]
> 
> Nevertheless, it is as far as I can go at the moment.
> 
>
One thought - "too busy to change it right now". What was the object of 
rushing this project to print, before you both were satisfied it was 
functioning to your satisfaction ? "QA" as a reference sounds really 
grand, until some of us used non-Microsoft browsers. Exclude me but as a 
suggestion, I would have recommended at least four names from CLC to do 
the initial testings for you - Richard, Michael M and Jerry; the fourth 
I'd have to give a little further thought to....  perhaps Jeff or Charlie ?

>>The non-computer people have less trouble with software because they take
>>the time to read each screen, do not "expect" a certain behaviour, and 
>>just do what it says.
> 

Well, I did read your screens and they seemed comprehensive, but perhaps 
they could be paraphrased a bit, and from other suggestions (e.g. 
Jeff's), could further be reduced based on a slightly different sequence 
of button usage. (At the back of the comment - the sheer volumes we have 
to absorb these days from reading newspapers and web sites - I'm washed 
out, I deliberately try to reduce my intake).

I don't even like writing it, but some others must have had the same 
thought; rushing the publication of a project that didn't totally work, 
smoothly, given the environment options, it brings into question your 
credibility - and we KNOW you are both competent programmers.

For Robert :

I haven't yet downloaded your COBOL program to take a look, but....
Remember the furore your 'Best practices' caused. Much of it was like a 
red rag to a bull for Bill K and Chuck Stevens. So given your format, 
what percentage of COBOL programmers do you think actually give a 
picture of data items, WITHOUT a final period/full Stop ?

Bear in mind that Pete suggested this project was a two way street (1) 
an example to COBOLERs of how to integrate to dotNet and, (2) The 
'outside world', Java and the C-family etc., using it as a tool to 
extract a COBOL copyfile and produce input for a DB. Leaving out those 
periods could lead them up the wrong path, if they subsequently thought 
they would like to dabble in COBOL.

Way back - your usage of Net Express Collections - you instantiated an 
Ordered Collection and then added some 5,000 (or was it 50,000) elements 
having done calculations on the data to go into the elements. Next step 
you :-

invoke os-Collection "finalize"

but then proceeded to access the elements by their individual 
identities. I took a deep breath and stopped at that point. What you did 
was OK, because at the end STOP RUN gets rid of the whole shebang of 
objects.

Now to 'Best Practices', any newbie to Net Express, or even a competent 
N/E user gingerly making a move to OO could be terribly misled by what 
you did. Particularly if STOP RUN is some way off in the future in an 
Exit from your Master Menu program. They wont be aware, but you probably 
are - those 5,000/50,000 elements left hanging are what are neatly 
referred to as a Memory Leak.

single objects , fine :- invoke ThisSingleObject "finalize" returning 	
						ThisSingleObject

Collections :- invoke ThisCollectioin "deepfinalize" returning
						 ThisCollection

Collections with 'Levels' :- invoke ThisCollection 	
				"deepFinaliseWithDepth" using n
				rturning ThisCollection

And one you didn't need to mention :-

		invoke thisObject "reallydeepfinalize" returning
					thisObject

(Never used it - but that last one is "if all else fails.....")

Still haven't got NE working, so above is from memory.

The specific point I'm making is whether it is a COBOLer or 'others' 
looking at a COBOL source, they should be led down the path which is 
generally considered to be the 'programmer standard'. For general 
circulation - don't use neat tricks, not unless your source has a Caveat 
covered by comments.

Never used it, but very vaguely aware of nested programs. What was the 
reason to turn yours into a nested set of programs and the advantages. I 
don't, (rather 'didn't') do 'Procedural' but am curious to know.

	
Jimmy

> They wouldn't be called 'users' if they did that.
> 
…[14 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 12)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-29T22:15:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<khu2e4dc7hl67vgcvj07v1esif5a8as1ep@4ax.com>`
- **References:** `<6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net> <oacEk.465$ex3.296@newsfe02.iad>`

```
On Mon, 29 Sep 2008 15:55:52 -0600, "James J. Gavan" <jgavandeletethis@shaw.ca> wrote:


>For Robert :
>
…[4 more quoted lines elided]…
>picture of data items, WITHOUT a final period/full Stop ?

Periods are not omitted, they're on the next line. This is normal practice in other
languages, such as SQL, that require superfluous punctuation. For example

select rowid
  , customer_name
 , address_1
 , address_2 
 , city

The format makes it easy to visually see missing punctuation. Leading periods in the
procedure division simplify copy-and-paste editing. Some traditionalists have gone to
putting the period at a paragraph's end on a line by itself. It's not a great leap to put
it in front of the following paragraph name.

>Bear in mind that Pete suggested this project was a two way street (1) 
>an example to COBOLERs of how to integrate to dotNet and, (2) The 
…[3 more quoted lines elided]…
>they would like to dabble in COBOL.

COBOLERs will think this is a worst case -- if it works with this screwey format, it will
surely work with my conventional code. Outsiders won't notice anything unusual. They might
even think Cobol isn't so bad after all.  :)

The program parses its own source without error.

>Way back - your usage of Net Express Collections - you instantiated an 
>Ordered Collection and then added some 5,000 (or was it 50,000) elements 
…[8 more quoted lines elided]…
>objects.

No, I did NOT access objects after their referencing container was destroyed with
'finalize'.  The code said:

  perform construct-data

   display '16. Dictionary' with no advancing
   perform Timer-on
   perform repeat-factor times
       perform construct-Collection
       perform lookup-entries
       perform destroy-Collection
   end-perform
   perform Timer-off

   perform destory-data
   goback

. destroy-Collection.
            invoke a-Dictionary "finalize"
                returning a-Dictionary
 . destroy-data.
     invoke a-OrderedCollection "finalize"
         returning a-OrderedCollection

>Now to 'Best Practices', any newbie to Net Express, or even a competent 
>N/E user gingerly making a move to OO could be terribly misled by what 
…[7 more quoted lines elided]…
>Collections :- invoke ThisCollectioin "deepfinalize" returning ThisCollection

You are correct about a-OrderedCollection. I orphaned 50,000 strings, but then terminated
the program on the very next line. I should have invoked "deepfinalize".  The collections
I used for the timing tests contained only references to those 50,000 strings. If I had
deepfinalized them, I wouldn't have been able to run more than one iteration.

There would have been no memory leak if a-OrderedCollection was an OrderedCollection
"ofValues", rather than "ofReferences", but then the rest of the program would have been
slower and unconventional. 

>The specific point I'm making is whether it is a COBOLer or 'others' 
>looking at a COBOL source, they should be led down the path which is 
>generally considered to be the 'programmer standard'.

I disagree. A tutorial should demonstrate best practices, not most common practices.

Most COBOLERs learned their craft by mimicing code written by others, who in turn were
mimicing others. They did not learn from tutorials. The style became a paradigm. In The
Structure of Scientific Revolutions, Thomas Kuhn wrote, "Successive transition from one
paradigm to another via revolution is the usual developmental pattern of mature science."
By that dictum, Cobol programming is unscientific. A more pessimistic Max Planck wrote, "a
new scientific truth does not triumph by convincing its opponents and making them see the
light, but rather because its opponents eventually die, and a new generation grows up that
is familiar with it."

> For general 
>circulation - don't use neat tricks, not unless your source has a Caveat 
>covered by comments.

I agree with that. There was one non-obvious usage, which I explained with a comment.

* A Dictionary contains Associations, an object with
* two parts: antecedent (key) and consequent (result). In this
* test, both are the same object -- a String containing a
* random number. Sub-classing Association with nulls tells
* it both parts will be objects rather than intrinsics.

>Never used it, but very vaguely aware of nested programs. What was the 
>reason to turn yours into a nested set of programs and the advantages. I 
>don't, (rather 'didn't') do 'Procedural' but am curious to know.

What is the advantage of a single working-storage containing an ocean of data, with no way
of knowing which structure belongs to which paragraph? 

What is the advantage of PERFORMing a paragraph with no parameters, so the reader has no
way to knowing the paragraph's inputs and outputs?
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 13)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-09-29T22:03:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PyhEk.2014$YN3.1601@newsfe08.iad>`
- **In-Reply-To:** `<khu2e4dc7hl67vgcvj07v1esif5a8as1ep@4ax.com>`
- **References:** `<6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net> <oacEk.465$ex3.296@newsfe02.iad> <khu2e4dc7hl67vgcvj07v1esif5a8as1ep@4ax.com>`

```
Robert wrote:
> On Mon, 29 Sep 2008 15:55:52 -0600, "James J. Gavan" <jgavandeletethis@shaw.ca> wrote:
> 
…[99 more quoted lines elided]…
> 
Thanks for the detailed reply Robert, understand what you are saying and 
why - but don't necessarily agree with it all :-) Yes I hated it in 
Procedural when you had the huge table of entries in Working Storage. Of 
course that problem disappears with OO.

On above sentence not quite sure what your difference is between 
"ofValues" and "ofReferences" they both create the same number of 
elements. As I recall your elements were pic 9(?) so you could jump 
straight into arithmetic functions. As to using CharacterArray to turn 
pic 9(?) or pic x(?) into "ofReferences" resulting in slowness - did you 
confirm that with timings ? Was the percentage significant ?

Jimmy

>>The specific point I'm making is whether it is a COBOLer or 'others' 
>>looking at a COBOL source, they should be led down the path which is 
…[40 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 14)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-30T08:20:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iv74e4ptu80e0u6ke88aiprvp16jma0d5m@4ax.com>`
- **References:** `<i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net> <oacEk.465$ex3.296@newsfe02.iad> <khu2e4dc7hl67vgcvj07v1esif5a8as1ep@4ax.com> <PyhEk.2014$YN3.1601@newsfe08.iad>`

```
On Mon, 29 Sep 2008 22:03:49 -0600, "James J. Gavan" <jgavandeletethis@shaw.ca> wrote:

>Robert wrote:
>> On Mon, 29 Sep 2008 15:55:52 -0600, "James J. Gavan" <jgavandeletethis@shaw.ca> wrote:
…[111 more quoted lines elided]…
>confirm that with timings ? Was the percentage significant ?

Construct-data used CharacterArray to turn 50,000 numbers into object references once, at
the beginning of the program, OUTSIDE timing loops (see above). Thus, timing tests
measured only the speed of collection classes organizing and finding data. They did not
include creation of the test data. 

Other tests I published did the same -- assumed data existed, measured time to find it.
Results showed they were 50 times faster than MF's collection classes. 

Sure, I could have written collection classes using the same algorithms (tree, radix
sort), but that would have negated the idea of using off-the-shelf components.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-09-29T15:59:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5dcEk.467$ex3.260@newsfe02.iad>`
- **In-Reply-To:** `<6kaiemF6u5qrU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Richard" <riplin@azonic.co.nz> wrote in message 
> news:27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com...
…[51 more quoted lines elided]…
> 

Richard is right on the button, but I also accept that you can't follow
it up from the brief sequence I gave you; as an off-chance, thought just
maybe you 'might'.....   Suggestion - delete me and my password from
your DB and when you signal that the whole thing is complete - including
Heidleberg/Hesleberg or whatever his bloody name was, I'll give it a
shot from point zero, and yes, I'll scribble down each step I take. (Of
course when we see something on the Web we presume it is working and
never think of doing an 'audit trail' to confirm cock-ups we may make).

Of course I don't make cock-ups, and as you already know, or should
know, to while away my dotage, as a hobby I design jet-engines for
airliners .........yeah.

Now why Heidleberg etc... You once had a cartoon for Gipetto - if I have
that right I can associate it. I immediately think of Pinocchio doing
his little dance routine for Stromboli :-

"I-ve........
Got no strings to hold me down,
da, da, da, da
........."

> [Pete]
> 
> Nevertheless, it is as far as I can go at the moment.
> 
>
One thought - "too busy to change it right now". What was the object of
rushing this project to print, before you both were satisfied it was
functioning to your satisfaction ? "QA" as a reference sounds really
grand, until some of us used non-Microsoft browsers. Exclude me but as a
suggestion, I would have recommended at least four names from CLC to do
the initial testings for you - Richard, Michael M and Jerry; the fourth
I'd have to give a little further thought to....  perhaps Jeff or Charlie ?

>>The non-computer people have less trouble with software because they take
>>the time to read each screen, do not "expect" a certain behaviour, and 
>>just do what it says.
> 

Well, I did read your screens and they seemed comprehensive, but perhaps
they could be paraphrased a bit, and from other suggestions (e.g.
Jeff's), could further be reduced based on a slightly different sequence
of button usage. (At the back of the comment - the sheer volumes we have
to absorb these days from reading newspapers and web sites - I'm washed
out, I deliberately try to reduce my intake).

I don't even like writing it, but some others must have had the same
thought; rushing the publication of a project that didn't totally work,
smoothly, given the environment options, it brings into question your
credibility - and we KNOW you are both competent programmers.

For Robert :

I haven't yet downloaded your COBOL program to take a look, but....
Remember the furore your 'Best practices' caused. Much of it was like a
red rag to a bull for Bill K and Chuck Stevens. So given your format,
what percentage of COBOL programmers do you think actually give a
picture of data items, WITHOUT a final period/full Stop ?

Bear in mind that Pete suggested this project was a two way street (1)
an example to COBOLERs of how to integrate to dotNet and, (2) The
'outside world', Java and the C-family etc., using it as a tool to
extract a COBOL copyfile and produce input for a DB. Leaving out those
periods could lead them up the wrong path, if they subsequently thought
they would like to dabble in COBOL.

Way back - your usage of Net Express Collections - you instantiated an
Ordered Collection and then added some 5,000 (or was it 50,000) elements
having done calculations on the data to go into the elements. Next step
you :-

invoke os-Collection "finalize"

but then proceeded to access the elements by their individual
identities. I took a deep breath and stopped at that point. What you did
was OK, because at the end STOP RUN gets rid of the whole shebang of
objects.

Now to 'Best Practices', any newbie to Net Express, or even a competent
N/E user gingerly making a move to OO could be terribly misled by what
you did. Particularly if STOP RUN is some way off in the future in an
Exit from your Master Menu program. They wont be aware, but you probably
are - those 5,000/50,000 elements left hanging are what are neatly
referred to as a Memory Leak.

single objects , fine :- invoke ThisSingleObject "finalize" returning 	
						ThisSingleObject

Collections :- invoke ThisCollectioin "deepfinalize" returning
						 ThisCollection

Collections with 'Levels' :- invoke ThisCollection 	
				"deepFinaliseWithDepth" using n
				rturning ThisCollection

And one you didn't need to mention :-

		invoke thisObject "reallydeepfinalize" returning
					thisObject

(Never used it - but that last one is "if all else fails.....")

Still haven't got NE working, so above is from memory.

The specific point I'm making is whether it is a COBOLer or 'others'
looking at a COBOL source, they should be led down the path which is
generally considered to be the 'programmer standard'. For general
circulation - don't use neat tricks, not unless your source has a Caveat
covered by comments.

Never used it, but very vaguely aware of nested programs. What was the
reason to turn yours into a nested set of programs and the advantages. I
don't, (rather 'didn't') do 'Procedural' but am curious to know.

	
Jimmy

> They wouldn't be called 'users' if they did that.
> 
…[14 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-30T13:33:12+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kdae8F7b6qrU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net> <5dcEk.467$ex3.260@newsfe02.iad>`

```


"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:5dcEk.467$ex3.260@newsfe02.iad...
> Pete Dashwood wrote:
>> Richard" <riplin@azonic.co.nz> wrote in message 
…[42 more quoted lines elided]…
>>

Not necessarily. Many people have accessed without problem.
>>
>>
…[6 more quoted lines elided]…
>> exact sequence of what they did is usually not productive.

On the contrary, I find that getting them to retrace their steps helps both 
me and them.

It is hardly reasonable to expect something they think is 'broken' to be 
fixed by clairvoyance...

If the alleged error cannot be reproduced, it can be argued that it doesn't 
exist, and there is therefore no point in wasting time on it.


>They
>> probably can only remember half of what was done, and get the sequence
>> wrong.
>>

Yes, for complex processes that certainly can happen. It is less likely with 
processes that only involve a few steps.
>
> Richard is right on the button, but I also accept that you can't follow
…[4 more quoted lines elided]…
> shot from point zero, and yes, I'll scribble down each step I take.

I cannot delete your entry without knowing your password. Your password is 
encrypted on the DB. I neither know it nor want to know it. I COULD take a 
brute force approach and simply remove your entry from the DB as 
Administrator, but that means downloading the whole DB and I don't want to.

Instead, I have provided a simple procedure so you can remove it yourself. 
Go to the site and press the login button or enable the "Download 
Executables" menu and click on that. Either way, you'll be taken to the 
login page where you will see a button marked "Remove Me" Enter your login 
and password, then click that button. Quick and painless. And no, I don't 
archive your entry. If you remove yourself you are then unknown to the 
site.You would need to register again if you wanted to try it anew.

Heisenberg will be retired some time in the next few days, until he is 
needed again for something else.

I'm sorry he annoyed you. Most people find him amusing, and that was my 
intention in placing him there. If you're not familiar with basic quantum 
physics, the allusion will be lost and you won't see the joke. Heisenberg's 
Uncertainty Principle was formulated by Werner Heisenberg in 1926, while he 
was working with Niels Bohr. It became one of the most important theorems in 
modern physics and describes certain limitations in our observation of 
physical reality. If I had a cat (and I can't at the moment because I travel 
too much) I would call it Schroedinger... I alluded to this the other day in 
a post, which the Doc picked up right away.

The point is that humour comes in many forms and, as Sir Arthur Wing Pinero 
once remarked: "For there is no harm in laughter."


>(Of
> course when we see something on the Web we presume it is working and
…[6 more quoted lines elided]…
> Now why Heidleberg etc...

Explained above. Sadly, when a joke is explained, it is seldom funny...:-)

You once had a cartoon for Gipetto - if I have
> that right I can associate it. I immediately think of Pinocchio doing
> his little dance routine for Stromboli :-
…[5 more quoted lines elided]…
>

There, you see... different people associate different things with the same 
image. Nothing wrong in that, as long as it makes us smile...:-)

>> [Pete]
>>
…[4 more quoted lines elided]…
> functioning to your satisfaction ?

We didn't. We WERE satisfied that it was OK or it would not have been 
published. I think you are being a tad unfair here, Jimmy. It is freeware. 
Neither of us was paid to do it, it just seemed like a good idea. I still 
think it was a good idea and I'm using the tool almost every day. There were 
a number of "spin-offs" from the exercise and they have been there since day 
one.


>"QA" as a reference sounds really
> grand, until some of us used non-Microsoft browsers.

Yes, I agree the Forefox thing could have been done better. However I have 
fixed it and gained valuable experience in the process. I COULD have just 
decided that if people use non-MS software, serve them right... like your 
ISP. I didn't.

I'm not sure what more I could do. It is easy with hindsight to say: "Well, 
you should have tested every possible Browser before you released it". I DID 
do cross Browser checking, but it wasn't good enough. As a result, the next 
site I do will be better, and I learned a lot more about CSS than I ever 
wanted to know... :-)

I could accept this particular criticism more graciously if you had ever 
built a web site. Until you do, you have no idea of the complexity of web 
programming. This is NOT just knocking out some HTML in Notepad (like the 
first site I ever built).

Your comments on the design (along with others) have been taken on board and 
I'll probably do something when I have time. In the meantime, many people 
have accessed the site without problem.



>Exclude me but as a
> suggestion, I would have recommended at least four names from CLC to do
> the initial testings for you - Richard, Michael M and Jerry; the fourth
> I'd have to give a little further thought to....  perhaps Jeff or Charlie 
> ?

It is not my place (or desire) to co-opt or coerce individuals into doing 
anything. HeyBub picked up the tool and found bugs in it. Both Robert and 
myself were amazed and grateful. The bugs have been fixed (and some of it 
was non-trivial), even though it states quite clearly in the Licence 
agreement that we WON'T necessarily support the product or fix bugs in it.

I don't think we can do much more.

>
>
…[10 more quoted lines elided]…
> out, I deliberately try to reduce my intake).

Sure, most of us do that. Nevertheless, I had something to say, so I said 
it. The reward for reading it is getting the menus unlocked :-)

I hope that some of the people who have accessed the site will think about 
keeping their legacy COBOL and moving it to the new environments.

I have clients who are doing just that and I am doing my best to help them.
>
> I don't even like writing it, but some others must have had the same
…[3 more quoted lines elided]…
>

Let it out, Jimmy :-)

My "credibility" is based on my track record. I have no trouble getting 
people to pay me for my advice.

The project was not rushed. In fact I wasn't ABLE to rush it due to other 
pressures.If anything, I was holding Robert back, although I did as much as 
I could, as fast as I could.

Please confine your comments to the project and let's not get personal. It 
isn't about Robert's or my credibility or any other "...ility".

Both of us have been completely open in this, acknkowledging freely where we 
could have done better. It is intended to be a learning exercise, and as 
such has been honestly explored. The things that needed fixing have been 
attended to, some other, less important ones, will be attended to.

Actually, I guess for a software project, that is pretty "incredible"... :-)

I leave Robert to speak for himself should he so choose.

> For Robert :
>
…[53 more quoted lines elided]…
> generally considered to be the 'programmer standard'.

And who formulates that 'programmer standard', Jimmy?  On a development 
site, there will be agreed standards governing style so people can exchange 
work more easily. But there is NO overall, comprehensive, 'programmer 
standard' for COBOL or any other programming language, OTHER than the 
language standard itself. We all like what we like and wish everyone would 
code the way we do. Robert uses a different style than I do; I found it 
strange at first, but I can see benefits in it. If someone wants to call 
themself a 'programmer' then they should be able to pick up ANY style the 
language is written in. It is only COBOL... (or VB, or C#, or JavaScript, or 
whatever...)

I don't think people should be led down any path.

The best you can do is provide some sample code and say:"This works for me 
because..." but they have a perfect right to NOT do it that way.


> For general
> circulation - don't use neat tricks, not unless your source has a Caveat
> covered by comments.
>
One man's "neat tricks" are another man's normal approach.

Almost every time that Rick Smith posts code here, I learn something I 
didn't kow about COBOL. I have often thought:"Wow! that is SO cool... a neat 
trick." But it isn't to Rick... that's my point.

> Never used it, but very vaguely aware of nested programs. What was the
> reason to turn yours into a nested set of programs and the advantages. I
> don't, (rather 'didn't') do 'Procedural' but am curious to know.
>

I'll leave this for Robert... All I would say is that there are a number of 
advantages in nested COBOL programs, Fujitsu supports it very well, and I 
have found it useful. Obviously, so has Robert...

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 13)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-09-29T20:11:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DVfEk.1221$hX5.36@newsfe06.iad>`
- **In-Reply-To:** `<6kdae8F7b6qrU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <27a8a6fa-b635-4a91-9c46-aca2f937e9d6@w1g2000prk.googlegroups.com> <6kaiemF6u5qrU1@mid.individual.net> <5dcEk.467$ex3.260@newsfe02.iad> <6kdae8F7b6qrU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:5dcEk.467$ex3.260@newsfe02.iad...
…[14 more quoted lines elided]…
>>>><snip>

Had a couple of cold days, got down to zero but not minus - but 
sufficient to make the zucchini plants roll over and die. Weather is 
beautiful at the moment with clear, clear blue skies and lots of sun. 
Probably the first dumps of snow in October - so meanwhile I'm zipping 
out to the garden, doing some pruning, which saves me doing it in the 
Spring.

I'll get back later on this.

Jimmy
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-28T18:38:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UrydnYIhcbUMiH3VnZ2dnUVZ_gGdnZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net>`

```
Pete Dashwood wrote:

>>> I had the same problem.  Try viewing the license first.
>> Now this one definitely raises an issue and it is design (systems
…[17 more quoted lines elided]…
> seen the menu.

I, too, got into a confusing loop.

Carefully, I weighed my options,
These three seemed to be the top ones,
Clearly, I must now adopt one,
With my fingers pale and trembling,
Slowly to the keyboard bending,
Longing for a happy ending,
Hoping all would be restored.

Praying for some guarantee,
Finally I pressed a key,
But on the screen what did I see?
I tried to catch the chips off guard,
I pressed again but twice as hard,
I hadn't drawn a lucky card,
I saw what went before.

Ultimately, through various random permutations, I wore down the web page, 
made it weep, and give up the prize.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-29T18:53:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kb8rdF6nql1U1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <UrydnYIhcbUMiH3VnZ2dnUVZ_gGdnZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:UrydnYIhcbUMiH3VnZ2dnUVZ_gGdnZ2d@earthlink.com...
> Pete Dashwood wrote:
>
…[37 more quoted lines elided]…
> I saw what went before.

Good stuff! Edgar Allan Poe would be proud... :-)

OK...

Pondering on midnights dreary
Brain so tired and eyes so bleary
How to give the maximum freedom
Yet be sure we know who's seen 'em
All the treasures that we've hidden
On the site's uncharted shore
Lock the menu
'Til hey've read through
And found the button
That's the key to
Opening the Download door.

Just read the page
And scroll it down
Read the page...
And you'll be shown
It's there in red
So you can see it
All you have to do is read it

Only this
And nothing more...

> Ultimately, through various random permutations, I wore down the web page, 
> made it weep, and give up the prize.

Well done!

Look at the satisfaction you got...

Much better than getting it easy :-)

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-29T09:45:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54mdnUXICLS5d33VnZ2dnUVZ_qninZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn> <xIqdneJWyZzAo0PVnZ2dnUVZ_rTinZ2d@earthlink.com> <kzDDk.24119$e82.19695@newsfe10.iad> <6k8t0jF6jmogU1@mid.individual.net> <UrydnYIhcbUMiH3VnZ2dnUVZ_gGdnZ2d@earthlink.com> <6kb8rdF6nql1U1@mid.individual.net>`

```
Pete Dashwood wrote:
>>
>> I, too, got into a confusing loop.
…[52 more quoted lines elided]…
>

What's art without suffering?
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-28T03:19:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k6togF6db91U1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222521798@f1.n250.z2.fidonet.ftn>`

```


"Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
news:1222521798@f1.n250.z2.fidonet.ftn...
> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com>
> <6jvuedF5em0rU1@mid.individual.net>
…[17 more quoted lines elided]…
> link.

These links are disabled until you read the Licence.

>
> Would the source work with Open Cobol as I would like to link the code 
> into a
> cobol xreference tool (cobxref) I have placed on to sourceforge?

If the compiler supports OO COBOL, yes,it will work. If not you would need 
to download Robert's original source code which is standard COBOL.
>
>
> Vince
>
Thanks for your interest, Vince.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-09-28T10:59:40
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222595980@f1.n250.z2.fidonet.ftn>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`

```
Hello Pete!

27 Sep 08 15:19, Pete Dashwood wrote to All:

 >> I tried to get a copy of the cobol source but your site(web) seems
 >> somewhat
…[3 more quoted lines elided]…
 >> a text field and not a link.

 PD> These links are disabled until you read the Licence.


Yes did that but the license text displays then within a fraction of a second 
get overwritten with a light(ish) blue overlay which makes the licence 
impossible to read.

 >>
 >> Would the source work with Open Cobol as I would like to link the
 >> code into a cobol xreference tool (cobxref) I have placed on to
 >> sourceforge?

 PD> If the compiler supports OO COBOL, yes,it will work. If not you would
 PD> need to download Robert's original source code which is standard
 PD> COBOL.

Where would I find that?

Vince
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-09-28T11:19:13
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222597153@f1.n250.z2.fidonet.ftn>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`

```
Hello Pete!

28 Sep 08 10:59, I wrote to Pete Dashwood:

 VC> Hello Pete!

 VC> 27 Sep 08 15:19, Pete Dashwood wrote to All:

 >>> I tried to get a copy of the cobol source but your site(web) seems
 >>> somewhat
…[3 more quoted lines elided]…
 >>> show it as a text field and not a link.

 PD>> These links are disabled until you read the Licence.


 VC> Yes did that but the license text displays then within a fraction of a
 VC> second get overwritten with a light(ish) blue overlay which makes the
 VC> licence impossible to read.

Tried again using firefox 3.0.3 and saw it as tried to download the source but 
it seems that page is still under development (some mention of Heidelberg or 
similar).

 >>>
 >>> Would the source work with Open Cobol as I would like to link the
 >>> code into a cobol xreference tool (cobxref) I have placed on to
 >>> sourceforge?

 PD>> If the compiler supports OO COBOL, yes,it will work. If not you
 PD>> would need to download Robert's original source code which is
 PD>> standard COBOL.

 VC> Where would I find that?

and it this a copy that has been updated subject to the bug reports?

Vince
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-29T00:59:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k99trF6j82oU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222597153@f1.n250.z2.fidonet.ftn>`

```


"Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
news:1222597153@f1.n250.z2.fidonet.ftn...
> Hello Pete!
>
…[24 more quoted lines elided]…
> similar).

:-) That's Mr. Heisenberg. He is related to the man who formulated the 
famous Uncertainty Principle. Funny how jokes become less funny when you 
explain them... :-)

The plan is to put the full projects up there so they can be easily 
downloaded. As long as we have known bugs in the code, I can't do that, and 
that is why I have placed Mr Heisenberg there.

>
> >>>
…[10 more quoted lines elided]…
> and it this a copy that has been updated subject to the bug reports?

The code has been amended according to the bug reports we have received. 
However, it may contain a couple of bugs which people haven't found yet. 
Robert is looking at it. The ORIGINAL code, which you can browse from the 
artifacts page, as far as I know, has NOT been amended. We needed to amend 
the OO version so the tool would work. When the full source download becomes 
available (and Mr. Heisenberg is retired) you will get the original AND the 
amended code.

Sorry for the inconvenience and glad you can now see it under Firefox.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-28T18:40:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wJidndDTHcx0iH3VnZ2dnUVZ_hGdnZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222597153@f1.n250.z2.fidonet.ftn>`

```
Vince Coen wrote:
>
> Tried again using firefox 3.0.3 and saw it as tried to download the
> source but it seems that page is still under development (some
> mention of Heidelberg or similar).
>

Beware: Firefox will give your cat warts.

If you don't have a cat, you should be okay.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-09-28T18:14:49
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222622089@f1.n250.z2.fidonet.ftn>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`

```
Hello Pete!

28 Sep 08 12:59, Pete Dashwood wrote to All:


 PD> The code has been amended according to the bug reports we have
 PD> received. However, it may contain a couple of bugs which people
 PD> haven't found yet. Robert is looking at it. The ORIGINAL code, which
 PD> you can browse from the artifacts page, as far as I know, has NOT been
 PD> amended. We needed to amend the OO version so the tool would work.
 PD> When the full source download becomes available (and Mr. Heisenberg is
 PD> retired) you will get the original AND the amended code.

Only a couple ?  :)

Right.

I will look forward to when you make it avail.  In the meanwhile I'm trying to 
get the Cobol code to compile under OC as a standalone prior to adding it into 
the cobxref code but seem to have found a problem or two with OC that I have 
passed to the programmer to look at.




Vince
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-29T12:35:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kaimbF6qaffU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222622089@f1.n250.z2.fidonet.ftn>`

```


"Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
news:1222622089@f1.n250.z2.fidonet.ftn...
> Hello Pete!
>
…[11 more quoted lines elided]…
> Only a couple ?  :)

Yes. :-) In fact Robert has sent me NKB (No Known Bugs) code this morning. 
I'll rebuild the product and retest it later today.

I have every confidence he will have fixed it.

>
> Right.
…[10 more quoted lines elided]…
>

Thank you for your positive post Vince.

I'll announce here when we think it is OK.

Pete.
```

###### ↳ ↳ ↳ NKB on version 2.0.0.6 WAS Re: Here's one problem

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-30T03:56:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kc8k3F78r10U1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com> <1222622089@f1.n250.z2.fidonet.ftn> <6kaimbF6qaffU1@mid.individual.net>`

```


"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6kaimbF6qaffU1@mid.individual.net...
>
>
…[22 more quoted lines elided]…
> I have every confidence he will have fixed it.

I have rebuilt it, tested it and it has passed. I was so inspired by 
Robert's good work that I fixed the dependency detection in the 
bootstrapper. This means that it now detects if the COBOL runtime is already 
installed, and doesn't install it again. Same as the other prerequisites. 
The only one you need to re-install is the COBOL component. It will check to 
make sure the COBOL runtime is installed, then install itself, if it is. The 
new version of the tool is quicker (the C# has been optimised, and the COBOL 
has had debug removed), and it now puts the engine version on the analysis 
output.

Most importantly, it no longer gets bamboozled by comments... :-)

If you have already installed the tool, it will check for updates every 7 
days (if your machine is connected to the internet) and automatically update 
itself, if there is a newer version of the tool. If you don't want to wait, 
you can manually download and install from the site. This time will be much 
faster and easier than the first time you did it, as most of the 
prerequisites will not require installing.

The site has taken around 450 hits although, as Richard pointed out, some of 
that is probably robots. I still haven't checked how many people have 
downloaded the product. (The database is fairly large, so I don't normally 
access it unless I need to...)
>
>>
…[8 more quoted lines elided]…
>> passed to the programmer to look at.

I'll be cleaning up the projects and posting them (Full Source) in the next 
week or so. In the meantime, you can browse the COBOL from the site.

Thanks to all for comments and patience.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2008-10-01T00:41:21
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1222818081@f1.n250.z2.fidonet.ftn>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <6jvuedF5em0rU1@mid.individual.net> <TaKdnRItBtSfK0bVnZ2dnUVZ_sudnZ2d@earthlink.com> <i89od4l50d1j7h60q58f1sd4eb127dppd0@4ax.com>`

```
Hello Pete!

29 Sep 08 00:35, Pete Dashwood wrote to All:

 PD> I have every confidence he will have fixed it.

 >> I will look forward to when you make it avail.  In the meanwhile I'm
 >> trying to get the Cobol code to compile under OC as a standalone
 >> prior to adding it into the cobxref code but seem to have found a
 >> problem or two with OC that I have passed to the programmer to look
 >> at.

 PD> Thank you for your positive post Vince.

 PD> I'll announce here when we think it is OK.


Just a quick update, now have it working compiled with OC (small buglet found) 
and adjusted the spacing in the display to allow for larger WS areas.

Later this week I will try and work out what changes are needed so it will go 
through the exture data division/WS div producing correct info without baffing 
on finding another 01 level or other statements. This I will need in order to 
hook into my cobxref utility.

Bye the bye anyone interested in using it for any Cobol compiler that doesn't 
have such a facility can grab it on sourceforge at 
//sourceforge.net/project/cobxref  or search for 'cobxref' Full source code is 
supplied under the GPL v2.0 licence.

Any repoorts of bugs is more than welcome.

Vince
```

##### ↳ ↳ Re: Here's one problem

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-24T22:08:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com>`

```
On Wed, 24 Sep 2008 15:47:01 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

>The following code:
>...
…[15 more quoted lines elided]…
>Note the comment ("*>") is not handled correctly.

You found a bug. Thanks.

Pete: in read-input, change 
 n less than line-length and
to 
 n less than line-limit and

> Also the casing of the original is not honored.

That was deliberate. I translate to lower case for convenience of syntax analysis and
matching REDEFINES to the referenced name. It would be easy to preserve the case of the
data name, if important.

>I suspect that the funny way it handles comments also causes a miscount of 
>the record size. In the case here, your program reports a size of 1655 bytes 
>when the actual size is 2232. 

The snippet doesn't show that. Try again after Pete fixes the bug. The fixed program
should automatically reinstall when you run it.
```

###### ↳ ↳ ↳ Re: Here's one problem

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-25T06:33:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com...
>
> You found a bug. Thanks.

That happens; and I know the 'thank you' is genuine.

In the old (and I mean, OLD) "COBFD" I wrote (and which your offering SHOULD 
replace), I got a bug report nine (9) years after the software was made 
available.

Took me close to, oh, call it six minutes to find and  fix.... once I knew 
about it and had data which could recreate it.

Sometimes it amazes me how a bug can go undetected that long.

MCM
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-26T00:18:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k1dslF5jqe4U1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com...
>
> "Robert" <no@e.mail> wrote in message 
…[15 more quoted lines elided]…
> MCM

Michael, I can't speak for Robert, but I don't see our tool as a replacement 
for yours. They both work in different environments. What we have is closer 
to what I originally requested, designed to be interactive in an environment 
where the mouse is king.But the exercise of producing the tool works at a 
number of levels which really have nothng to do with the tool itself.  The 
bug that HeyBub found is a good one and it will get fixed tomorrow. That in 
no way invalidates your tool (or ours...)

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-25T12:26:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbg02j$be8$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com>`

```
In article <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:

[snip]

>Sometimes it amazes me how a bug can go undetected that long.

I was in a meeting, once - it might be difficult to imagine such a thing, 
true - about a payroll system that was being replaced.  The Olde Tymers 
were, as expected, rather defensive about the entire situation... and a 
discrepancy between test results from the old system and the new was 
causing them to indulge in Great Mirth and Derision...

... until someone from Legal was called... and, sure enough, the Old 
System was giving the wrong results and, under certain conditions, paying 
people for two kinds of hours worked simultaneously.

The Project Director was aghast and shouted 'WHAT DO YOU MEAN?  HOW HAVE 
WE BEEN PAYING PEOPLE WRONG FOR THE PAST TWENTY YEARS AND NOBODY SAID 
ANYTHING ABOUT IT?!?'... and in the silence I said 'It is my experience, 
sir, that very few people will actively or loudly voice complaints over 
financial errors that they see as being in their favor.  Under-pay them 
and you'll hear about it, *fast*... over-pay them and they might not 
appear to be responding with similar diligence.'

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-26T17:08:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k392iF5tekeU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:gbg02j$be8$1@reader1.panix.com...
> In article <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[24 more quoted lines elided]…
>
Ain't that the truth... :-)

I remember a certain hospital board which took two years to DESIGN a payroll 
system, producing a document which served as a doorstop to keep the breeze 
circulating in our office during the Summer.

(To be fair, hospitals have a wide diversity of occupations and professions, 
all subject to different union agreements and even individual contract 
negotiations...)

Anyway, it took another two years to implement and about a year later, it 
was discovered that a certain sector had been overpaid ever since the system 
went live.

It amused me no end to see the 3 month feedback reports from this sector. 
They said the new system was fantastic, best thing since sliced bread, 
couldn't mimagine how they got on without it, etc... :-)

When the problem came to light, the sector concerned were told that the 
overpayment would be deducted over a period of time from their wages. They 
promptly went on strike. When other sectors heard what had happened, they 
went on strike as well (probably because they HADN'T been overpaid :-)) Mind 
you, in those days there was a propensity for people to go on strike at the 
drop of a hat... the famous one was the freezing works where the whole 
workforce went on strike because the chips in the canteen were not hot... 
when the sun is shining and you live near a beach it is really easy to find 
reasons for not being at work... At the hospital chaos ensued unbtil it was 
finally agreed that they would not have to repay the money they had received 
incorrectly.

The last I heard, they had replaced the in-house payroll with a package. 
Probably what they should have done in the first place...

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-26T09:36:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbiafh$n26$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net>`

```
In article <6k392iF5tekeU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[6 more quoted lines elided]…
>>>Sometimes it amazes me how a bug can go undetected that long.

[snip]

>> The Project Director was aghast and shouted 'WHAT DO YOU MEAN?  HOW HAVE
>> WE BEEN PAYING PEOPLE WRONG FOR THE PAST TWENTY YEARS AND NOBODY SAID
…[6 more quoted lines elided]…
>Ain't that the truth... :-)

Well... at least it is what I recall my experience to have been, aye.

>
>I remember a certain hospital board which took two years to DESIGN a payroll 
…[5 more quoted lines elided]…
>negotiations...)

Those complex situations tend to take a while to describe, aye... might 
this have happened sometime around 1985??  Back in such Oldene Dayse I 
noticed a tendency for spec documents to be an attempt to reproduce 
pencil-and-paper systems on computers, completely ignoring such things as 
databases.

The emphasis was on 'how do we do This Job on a computer', not 'how would 
a computer be used to produce (results) to satisfy (condition)'... 
different times, different views.

>
>Anyway, it took another two years to implement and about a year later, it 
…[8 more quoted lines elided]…
>overpayment would be deducted over a period of time from their wages.

Hmmmm... if The Sector was signing its own paychecks then yes, that might 
have been appropriate... leaving aside niggling details about how 
pension-based percentages were to be recalculated and the like.  On the 
other hand... if The Sector did not sign its own paychecks in a vacuum 
then the solution appears inappropriate.

>They 
>promptly went on strike. When other sectors heard what had happened, they 
>went on strike as well (probably because they HADN'T been overpaid :-))

... or because they realised that 'the Workers did not calculate the 
checks, authorise the checks, issue the checks or honor the checks when 
presented for payment yet the Workers are the only ones (from your 
description given) who are asking to take any sort of action to resolve 
the situation.  Are the Managers who were responsible for the resources 
used which resulted in this error being asked to pay the Company the 
interest lost on these sums, the machine-time and equpiment costs for the 
mistake and made to likewise bear the burden?'

>Mind 
>you, in those days there was a propensity for people to go on strike at the 
…[3 more quoted lines elided]…
>reasons for not being at work... 

Ahhhhh, for the Oldene Dayse... when there were almost as many reasons for 
a Strike as there are for Managament Seminars, today!

>At the hospital chaos ensued unbtil it was 
>finally agreed that they would not have to repay the money they had received 
…[3 more quoted lines elided]…
>Probably what they should have done in the first place...

... and when the package is found out to have a bug in it, which overpays 
a Sector under certain conditions... then the Lawyers from the Hospital 
and the Vendor start billing hours in staggering quantities... but hey, at 
least the Workers are no longer getting overpaid!

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-26T08:05:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q0rpd41mdshmrvkso8v6ksovudoaqkls60@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com>`

```
On Fri, 26 Sep 2008 09:36:49 +0000 (UTC), docdwarf@panix.com () wrote:

>Back in such Oldene Dayse I 
>noticed a tendency for spec documents to be an attempt to reproduce 
…[5 more quoted lines elided]…
>different times, different views.

And that didn't go away when switching from one computerized system to
the next.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T20:04:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com>`

```
On Fri, 26 Sep 2008 09:36:49 +0000 (UTC), docdwarf@panix.com () wrote:

>Those complex situations tend to take a while to describe, aye... might 
>this have happened sometime around 1985??  Back in such Oldene Dayse I 
…[6 more quoted lines elided]…
>different times, different views.

The question was cast as 'how do we write a COBOL program running on the mainframe to do
this job?' The platform and language were givens. So were the actors -- our programmers. 

There weren't a lot of options before the IBM PC erupted in 1982. It's been downhill or
uphill, depending on your point of view, ever since.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-26T18:39:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com>`

```
On Sep 27, 1:04 pm, Robert <n...@e.mail> wrote:
> On Fri, 26 Sep 2008 09:36:49 +0000 (UTC), docdw...@panix.com () wrote:
> >Those complex situations tend to take a while to describe, aye... might
…[13 more quoted lines elided]…
> uphill, depending on your point of view, ever since.

There were plenty of options. The IBM PC was just one small step. In
fact the IBM PC was originally designed to compete directly against
the Apple ][, the first to be called a 'PC', and the Commodore Pet,
which had been around since 1978 and was increasingly to be found in
IBMs sites running Visicalc and other software.

I had been using Cobol on micros since 1979 with CIS Cobol on CP/M and
DRS20 8bit networked systems and RM on MP/M and OASYS.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T21:57:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pf7rd4p9pvnlqi8k9d6ghu154r1fu6olkd@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com>`

```
On Fri, 26 Sep 2008 18:39:40 -0700 (PDT), Richard <riplin@azonic.co.nz> wrote:

>On Sep 27, 1:04ï¿½pm, Robert <n...@e.mail> wrote:
>> On Fri, 26 Sep 2008 09:36:49 +0000 (UTC), docdw...@panix.com () wrote:
…[23 more quoted lines elided]…
>DRS20 8bit networked systems and RM on MP/M and OASYS.

I too worked on some of those in 1979-1982. My major interest was the TI-99/4A. I knew
none of them wasThe One. When the IBM PC came out in 1982, I knew it WAS The One. I bought
one with $2,000 of my own money. A year later, half my programming staff was working on
the PC. At first, we used Compiled Basic because it was one of only two compilers
available, the other being Turbo Pascal.  The real breakthru came with Realia Cobol in
1984. 

We were ok for 11 years. The era ended with Win95.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-27T00:30:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4766ec5-f710-4f29-a349-b3bd504b0e55@p31g2000prf.googlegroups.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com> <pf7rd4p9pvnlqi8k9d6ghu154r1fu6olkd@4ax.com>`

```
On Sep 27, 2:57 pm, Robert <n...@e.mail> wrote:
> On Fri, 26 Sep 2008 18:39:40 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
> >On Sep 27, 1:04 pm, Robert <n...@e.mail> wrote:
…[27 more quoted lines elided]…
> none of them wasThe One. When the IBM PC came out in 1982, I knew it WAS The One.

I have an IBM PC model B here now. It is pre-XT. The model A could
only support 256Kb tops no matter how many memory cards were used. The
model B took this to 640Kb but needed many memory cards to get there.

The IBM PC was a toy, it only had 2 diskettes which originally were
160Kb each, then double sided went to 320Kb, and finally with 9
sectored managed 360Kb. I was already running multi-user MP/M systems
with 10Mbyte hard disks and networked multi-cpu (8085) DRS20s.

> I bought
> one with $2,000 of my own money.

That must have been a pretty sparse machine. I still have a price list
here. A box with 48Kb was $US 2235.00. Floppy controller $220, floppy
drive $570 (each), Monitor $345, printer adaptor $150, CGA card $300,
colour monitor $999. Memory board 64K $540...

> A year later, half my programming staff was working on
> the PC. At first, we used Compiled Basic because it was one of only two compilers
> available, the other being Turbo Pascal.

On the day the IBM PC was released there were MS Pascal, Fortran,
Cobol and Basic compilers, so there were always at least 4. Turbo
Pascal was later, it was still Compass Pascal on CP/M when the IBM PC
came out.

>  The real breakthru came with Realia Cobol in
> 1984.
>
> We were ok for 11 years. The era ended with Win95.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-27T13:09:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blrsd4da7anvjikaa4huf1dgj6h8d0rual@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com> <pf7rd4p9pvnlqi8k9d6ghu154r1fu6olkd@4ax.com> <f4766ec5-f710-4f29-a349-b3bd504b0e55@p31g2000prf.googlegroups.com>`

```
On Sat, 27 Sep 2008 00:30:49 -0700 (PDT), Richard <riplin@azonic.co.nz> wrote:

>On Sep 27, 2:57ï¿½pm, Robert <n...@e.mail> wrote:
>> On Fri, 26 Sep 2008 18:39:40 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
…[34 more quoted lines elided]…
>The IBM PC was a toy,

I think it was positioned as a toy, or *personal* computer, to allay fears WITHIN IBM. I
saw the PC as a general purpose computer.

> it only had 2 diskettes which originally were
>160Kb each, then double sided went to 320Kb, and finally with 9
>sectored managed 360Kb. I was already running multi-user MP/M systems
>with 10Mbyte hard disks and networked multi-cpu (8085) DRS20s.

MSDOS version 1 didn't support hard disks well. They had to be partitioned to look like
floppies. Version 2 introduced Unix-style directories. 

>> I bought
>> one with $2,000 of my own money.
…[4 more quoted lines elided]…
>colour monitor $999. Memory board 64K $540...

Those sound like IBM list prices. Third party prices were about half.

>> A year later, half my programming staff was working on
>> the PC. At first, we used Compiled Basic because it was one of only two compilers
…[5 more quoted lines elided]…
>came out.

MS Cobol would have been my first choice. I'm fairly sure it came later, around 1984.

Turbo Pascal (PC version) was published November 20, 1983, selling for $49.99. It became a
best seller NOT because buyers liked the Pascal language but rather because there were few
other compilers available in that price range. In the early '80s, compilers sold for
several hundred dollars. 

I was impressed with Turbo Pascal's integrated workbench, but did not like the Pascal
language. I found BASCOM easier to tolerate. In retrospect, I should have used C. I didn't
because I thought C was The Enemy of Cobol.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 12)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-27T13:08:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9972650e-58cd-4ce9-be7e-c06355bb351f@40g2000prx.googlegroups.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com> <pf7rd4p9pvnlqi8k9d6ghu154r1fu6olkd@4ax.com> <f4766ec5-f710-4f29-a349-b3bd504b0e55@p31g2000prf.googlegroups.com> <blrsd4da7anvjikaa4huf1dgj6h8d0rual@4ax.com>`

```
On Sep 28, 7:09 am, Robert <n...@e.mail> wrote:
> On Sat, 27 Sep 2008 00:30:49 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
> >On Sep 27, 2:57 pm, Robert <n...@e.mail> wrote:
…[38 more quoted lines elided]…
> saw the PC as a general purpose computer.

It was just another arrival amongst dozens of similar machines into a
market that had been growing since the mid-70s. It was only the brand
name and marketing that made stand out, certainly not the technology.

It wasn't even the first 16bit or the first MS-DOS machine. It was
cobbled together from their old System 23 planar, hacked to take an
8088 which only required an 8bit bus and fitted out with parts that
were considered obsolete at the time (eg: 8250 serial ports).

It was aimed at the Apple ][ and in stopping these infiltrating
mainframe sites. It had Visicalc and dBase II and could act as a
terminal. This is why the serial ports were DTE (terminal) while the
machines I used had DCE (computer) serial ports.

> > it only had 2 diskettes which originally were
> >160Kb each, then double sided went to 320Kb, and finally with 9
…[4 more quoted lines elided]…
> floppies. Version 2 introduced Unix-style directories.

PC-DOS 1 didn't support hard disks at all. The IBM PC BIOS didn't
support hard disks until the XT. There were add-ons that gave limited
access to a hard disk where the controller emulated a floppy
controller, but this was slow, and as you say, no directories at all,
nor any division by user area as CP/M had. Like the floppies all files
in 'root directory' and this was limited to 128 files.

> >> I bought
> >> one with $2,000 of my own money.
…[17 more quoted lines elided]…
> MS Cobol would have been my first choice. I'm fairly sure it came later, around 1984.

MS Cobol had been available with CP/M since the late 70s and was
available on the IBM-PC at release. In fact it was version 2.2 by
then.

> Turbo Pascal (PC version) was published November 20, 1983, selling for $49.99.

Previously it had been running on CP/M (as Compass and Turbo). As you
say, this is over two years after the IBM-PC was released (august
1981).

> It became a
> best seller NOT because buyers liked the Pascal language but rather because there were few
> other compilers available in that price range. In the early '80s, compilers sold for
> several hundred dollars.

> I was impressed with Turbo Pascal's integrated workbench, but did not like the Pascal
> language. I found BASCOM easier to tolerate. In retrospect, I should have used C. I didn't
> because I thought C was The Enemy of Cobol.

By November 1983 there were several C compilers for the IBM-PC. Byte
September 1983 had a comparison review of 9 of them. As you say they
ranged in price from $35 to $650.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-27T18:33:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nb7td41bc60ibiurkpqqhtksi42pv24b5l@4ax.com>`
- **References:** `<gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com> <pf7rd4p9pvnlqi8k9d6ghu154r1fu6olkd@4ax.com> <f4766ec5-f710-4f29-a349-b3bd504b0e55@p31g2000prf.googlegroups.com> <blrsd4da7anvjikaa4huf1dgj6h8d0rual@4ax.com> <9972650e-58cd-4ce9-be7e-c06355bb351f@40g2000prx.googlegroups.com>`

```
On Sat, 27 Sep 2008 13:08:43 -0700 (PDT), Richard <riplin@azonic.co.nz> wrote:

>On Sep 28, 7:09ï¿½am, Robert <n...@e.mail> wrote:
>> On Sat, 27 Sep 2008 00:30:49 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
…[43 more quoted lines elided]…
>name and marketing that made stand out, certainly not the technology.

Open Architecture made it stand out. Detailed specs, including a BIOS listing, were
readily available. It was a developer's machine.

>It wasn't even the first 16bit or the first MS-DOS machine. 

It was the first Microsoft DOS. Microsoft licensed DOS version 1 from Seattle Computer
Products, which called it QDOS. It ran on SCP's 8086 board, which plugged into an S-100
bus.  Microsoft quickly rewrote DOS from scratch and released it as MSDOS version 2.

>It was
>cobbled together from their old System 23 planar, hacked to take an
…[6 more quoted lines elided]…
>machines I used had DCE (computer) serial ports.

No, modems had DCE ports. The difference between DTE and DCE was assignment of transmit
and receive lines. To connect two computers, both having DTE, a null modem was used to
exchange the transmit and receive lines. The same null modem could be used to connect a
computer with a DCE port to a modem with a DCE port.


>> >> A year later, half my programming staff was working on
>> >> the PC. At first, we used Compiled Basic because it was one of only two compilers
…[11 more quoted lines elided]…
>then.

My 1983 notes DO show a MS Cobol available, but it was very slow. I ran these benchmarks
personally, so must have had hands-on. 

Language                cost    relative speed
Mainframe COBOL (.5 mip)        1
BASCOM                  300           20
TURBO Pascal           50           30
mbp                         850           30
BASIC interp          free          160
CIS/MicroFocus    1800          160
Ryan McFarland    600e         180
IBM/Microsoft        600          200

These web sites say Microsoft published COBOL-80 on Aprol 11, 1978. 
http://www.thocp.net/companies/microsoft/microsoft_company.htm
http://www.robotwisdom.com/linux/microsoft.html

As previously discussed here, MS COBOL 3 & 4 were rebadged Micro Focus. Who wrote versions
1 & 2? There was an article in Creative Computing, March 1980, which  compared Micro Focus
COBOL to Microsoft COBOL. There is a good chance of finding the answer there, but I cannot
find the article.
http://eric.ed.gov/ERICWebPortal/custom/portlets/recordDetails/detailmini.jsp?_nfpb=true&_&ERICExtSearch_SearchValue_0=EJ218480&ERICExtSearch_SearchType_0=no&accno=EJ218480

Based on relative speeds above, it does not appear that MS Cobol version 1 was MF nor RM.
My guess is Ellis Computing's Nevada Cobol, a major compiler in the CP/M world.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 14)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-27T21:40:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<418f9ea0-770e-4c3b-9cde-e701ab10a668@s20g2000prd.googlegroups.com>`
- **References:** `<gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com> <pf7rd4p9pvnlqi8k9d6ghu154r1fu6olkd@4ax.com> <f4766ec5-f710-4f29-a349-b3bd504b0e55@p31g2000prf.googlegroups.com> <blrsd4da7anvjikaa4huf1dgj6h8d0rual@4ax.com> <9972650e-58cd-4ce9-be7e-c06355bb351f@40g2000prx.googlegroups.com> <nb7td41bc60ibiurkpqqhtksi42pv24b5l@4ax.com>`

```
On Sep 28, 12:33 pm, Robert <n...@e.mail> wrote:
> On Sat, 27 Sep 2008 13:08:43 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
> >On Sep 28, 7:09 am, Robert <n...@e.mail> wrote:
…[47 more quoted lines elided]…
> readily available. It was a developer's machine.

No different from CP/M machines. The BIOS listings were available for
most of those too. S100 was probably even better documented than the
IBM PC.

> >It wasn't even the first 16bit or the first MS-DOS machine.
>
> It was the first Microsoft DOS.

The IBM-PC used PC-DOS which was, admittedly, a version of SCP-/86-/MS-
DOS.

> Microsoft licensed DOS version 1 from Seattle Computer
> Products, which called it QDOS.

QDOS was purportedly only used briefly for prototype versions and is
almost mythology. It was actually released as 86-DOS and SCP-DOS as
seen in Byte ads in 1981 or so (eg Aug 81 p270).

SCP were alleged to have taken a CP/M BDOS 'listing' and put it
through the Intel 8080 -> 8086 translator as the starting point for
'QDOS'. DRI reportedly showed IBM that PC-DOS 1.0 had a DRI copyright
hidden in the code. SCP and MS were both DRI OEMs so had all the tools
and source that DRI made available.

> It ran on SCP's 8086 board, which plugged into an S-100
> bus.  Microsoft quickly rewrote DOS from scratch and released it as MSDOS version 2.
>

I am not sure about the 'quickly' there was two years between 1 and 2.


> >It was
> >cobbled together from their old System 23 planar, hacked to take an
…[11 more quoted lines elided]…
> computer with a DCE port to a modem with a DCE port.

The point is that 'computers' had DCE and _terminals_ (eg Wyse 60) had
DTE. Obviously modems were DCE too so they would connect to the
terminal with a 1:1 cable. The IBM PC was designed to be a terminal,
not a computer.


> >> >> A year later, half my programming staff was working on
> >> >> the PC. At first, we used Compiled Basic because it was one of only two compilers
…[34 more quoted lines elided]…
> My guess is Ellis Computing's Nevada Cobol, a major compiler in the CP/M world.

No. Like MS Pascal it was written by Microsoft. I know that it is
unusual, but MS has written some software.

I used MS Cobol-80 on some Z-80 driven POS terminals back in the late
70s. I also still have a copy of 2.2 here left over from some
conversion I did more than a decade ago.

MS Cobol 1 & 2 were strictly single-user and thus mostly useless.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T23:02:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p1ard41tceiaiq5ajvhq3l1tensav07a9t@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com>`

```
On Fri, 26 Sep 2008 18:39:40 -0700 (PDT), Richard <riplin@azonic.co.nz> wrote:

>I had been using Cobol on micros since 1979 with CIS Cobol on CP/M and
>DRS20 8bit networked systems and RM on MP/M and OASYS.

I worked on CIS Cobol in 1984, running on a PC,  in the course of revewing it for a
magazine. I wasn't sure of its provenance; it seemed to be tied to Micro Focus. 

mbp was more memorable. It generated native code, but the compiler was interpreted p-code
generated from CDL2. It took ten minutes to compile an average program. 

In 1984, CIS sold for $1,800, mbp sold for $850 and RM sold for $600. Realia blew them out
of the water for $1,000. It compiled in milliseconds and generated the most optimized code
in that era. On benchmarks, it beat all the hot C compilers such as Lattice. I can't
imagine a better Cobol compiler. It was written in Cobol and used to compile itself. 

Some of its optimizations still blow me away. For instance SEARCH on a byte array
generated a single machine instruction: REPNE SCASB. 

The reward: Realia was acquired by Computer Associates who proceeded to bury it, for no
reason other than corporate incompetence.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-27T00:45:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4b993c1-abd3-4e0c-bebd-c11d9d355a25@a3g2000prm.googlegroups.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com> <c107142e-f49b-4338-bac1-7f2a2d42e2aa@n33g2000pri.googlegroups.com> <p1ard41tceiaiq5ajvhq3l1tensav07a9t@4ax.com>`

```
On Sep 27, 4:02 pm, Robert <n...@e.mail> wrote:
> On Fri, 26 Sep 2008 18:39:40 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
> >I had been using Cobol on micros since 1979 with CIS Cobol on CP/M and
…[3 more quoted lines elided]…
> magazine. I wasn't sure of its provenance; it seemed to be tied to Micro Focus.

The two guys that started MicroFocus previous worked for a division of
ICL called DataSkill (at ICL Bracknell I was there for some months)
and they developed a limited Cobol for the ex-Singer, ex-Cogar, ICL
1500 series desktop machine that were first made in the early 70s (I
still have a couple laying around here.).

They left ICL and formed Microfocus around 1978 and CIS Cobol was
their first product. Initially on CP/M as single user they developed a
shared filesystem process that gave it multi-user capability on MP/M
and networked systems around 1980 or so.

> mbp was more memorable. It generated native code, but the compiler was interpreted p-code
> generated from CDL2. It took ten minutes to compile an average program.
>
> In 1984, CIS sold for $1,800, mbp sold for $850 and RM sold for $600. Realia blew them out
> of the water for $1,000. It compiled in milliseconds and generated the most optimized code

On the other hand it had no filesharing capability and so was
basically single-user. You had to open and close files so others on a
network could access the files and this was s_l_o_w. I was developing
multi-user systems and a single 8086 with 1 Mbyte ram could handle 4
or 5 users because MF Level II Cobol had shared code for its run-time
(ie one copy of the run-time code was shared by half a dozen
processes).

There was always spare CPU time available - but that was because MP/M
(later CDOS) ran pre-emptive multi-tasking and could use the CPU time
concurrently with disk access.

> in that era. On benchmarks, it beat all the hot C compilers such as Lattice. I can't
> imagine a better Cobol compiler. It was written in Cobol and used to compile itself.
…[5 more quoted lines elided]…
> reason other than corporate incompetence.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-27T01:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbk35h$7on$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <6k392iF5tekeU1@mid.individual.net> <gbiafh$n26$1@reader1.panix.com> <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com>`

```
In article <9k0rd4h6mq02ag1kefe2klqge5mutm9jqf@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 26 Sep 2008 09:36:49 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[13 more quoted lines elided]…
>our programmers. 

Not... quite, Mr Wagner.  I'd agree with 'on a mainframe' because back in 
those days there weren't too many other options... but not necessarily 'a 
COBOL program', as there were systems of related programs... and not 
necessarily COBOL, as scientists held to FORTRAN and folks writing 
control-interfaces might have tended towards machine-languages.

The programmers had a job in doing this... as did the analysts, as did the 
users, as did the managers, as did the executives.  What I try to point 
out is the difference between 'how is this tool used in order to continue 
what we've been doing' versus 'how can using this tool accomplish our 
desired ends in different ways that are better for the company and the 
customers'.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-09-26T17:31:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X7WdnUj3Q_YoyUDVnZ2dnUVZ_qrinZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <gbg02j$be8$1@reader1.panix.com> <6k392iF5tekeU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6k392iF5tekeU1@mid.individual.net...
>
<snip>

> The last I heard, they had replaced the in-house payroll with a package. 
> Probably what they should have done in the first place...
…[4 more quoted lines elided]…
>

I once worked on a payroll system for the U.S. Senate and it was replaced by 
a package, but the package had to be customized and enhanced to do certain 
requirements that most payroll systems do not have.  Things like 
re-employeed annuitants and shared employeees etc.  Of course with every new 
release of the package something broke and changes had to be redone.  I 
hated it and it was the main reason I left.  Of course there was nothing 
wrong with the old system except it was "old technology".
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-25T10:28:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BqOdnWy124ywM0bVnZ2dnUVZ_jidnZ2d@earthlink.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com>`

```
Michael Mattias wrote:
> "Robert" <no@e.mail> wrote in message
> news:1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com...
…[14 more quoted lines elided]…
> MCM

From the book "Systemantics"

"Functional Indeterminacy Theorem (F.I.T)
In complex systems, malfunction and even total nonfunction may not be 
detectable for long periods, if ever. Such systems may, however, persist 
indefinitely or even expand."
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-25T20:31:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <BqOdnWy124ywM0bVnZ2dnUVZ_jidnZ2d@earthlink.com>`

```
On Thu, 25 Sep 2008 10:28:45 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

>Michael Mattias wrote:
>> "Robert" <no@e.mail> wrote in message
…[22 more quoted lines elided]…
>indefinitely or even expand." 

Worse, the system RESISTS correcting errors that are discovered and reported. I often see
errors so obvious, they leap out of source code. 

Me: This is a bug. It's not setting the price plan on a cancellation reversal.
Colleague: The customer is supposed to get the original plan.
Me: If the transaction is New Business and we find the product on file in cancelled
status, we change the New Business to a Cancellation Reversal. The customer may have been
gone five years. He's not entitled to the old price plan, which was probably cancelled
years ago.
Colleague: I never thought of that. Tell the boss.

First line of defense: Denial

Manager: That code has been in production for years. Nobody has complained. It must not
happen  the way you say.
Me: I set up a test case. Here, you can see it happening.
Manager: Sure, you made it happen. Has it ever happened in the real world?

(Two hours research, searching millions of archived transactions.)

Second line of defense: Minimizing

Me: Here are five examples that happened yesterday.
Manager: How much could we have lost, maybe twenty dollars on each, tops. You want to
spend a thousand dollars to recover less than a hundred?
Me: It happened five times yesterday. This year, it's happened 1,623 times. 

Third line of defense: Blame Others

Manager: We did what the customer asked for. It says right here in the High Level Design
that we should convert the New Business to a Cancellation Reversal. 
Me: The customer didn't tell us to ignore the new price plan.
Manager: Well, they didn't tell us to pick it up, either. 
Me: The customer didn't write the High Level Design, we did. 
Manager: The customer signed off on it. And they didn't catch it during UAT. 

Fourth line of defense: Bargaining

Me: Let's call the customer and ask what we should be doing.
Manager: That'll open a can of worms. They'll want us to compute adjustments for the last
year. What would it take to fix it quietly?
Me: One line of code, in a program we're already changing.
Manager: Just do it and don't discuss it with the customer.

Fifth line of defense: Depression = anger turned inward

Manager: Why do you waste time looking for obscure errors? Don't you have enough work to
do?
Me: I was changing that paragraph for project xxxx. The error was obvious.
Manager: We do code reviews to catch errors like this. Who reviewed this code?
Me: (knowing correct answer is You Did) I don't know, I didn't check.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-26T16:30:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k36r9F5r79dU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <76ednR2xbZzbOkfVnZ2dnUVZ_sTinZ2d@earthlink.com> <1fvld45rl4dsaop1u543533jsor4oljvmb@4ax.com> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <BqOdnWy124ywM0bVnZ2dnUVZ_jidnZ2d@earthlink.com> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com...
> On Thu, 25 Sep 2008 10:28:45 -0500, "HeyBub" <heybub@NOSPAMgmail.com> 
> wrote:
…[90 more quoted lines elided]…
> Me: (knowing correct answer is You Did) I don't know, I didn't check.

I really enjoyed the above, Robert. Excellent.

And sadly, accurate in many companies, also.

Pete.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-26T13:22:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbinm8$cet$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <BqOdnWy124ywM0bVnZ2dnUVZ_jidnZ2d@earthlink.com> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>`

```
In article <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 25 Sep 2008 10:28:45 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

[snip]

>>"Functional Indeterminacy Theorem (F.I.T)
>>In complex systems, malfunction and even total nonfunction may not be 
…[5 more quoted lines elided]…
>errors so obvious, they leap out of source code. 

Mr Wagner, leaving aside the fact that 'obvious is in the mind of the 
beholder' and that what you bring to an organisation is a different 
mind... you might do well to remember your Elementary Physics.

Newton's First Law is that 'an object perserveres in its state of rest or 
uniformly straightforward motion except as it is forced to change its 
state by another impressed force'.

(the Latin is lovely; 'Corpus omne perseverare in statu suo' can be 
readily punned into 'Omne preseverare in status quo')

When a change in motion is sought two things must be remembered: the 
original force compelling the motion, by Law cited above, will resist this 
change and force must be applied.  Human beings, at times, do not respond 
well to being subject to force... but that's sociology, not physics.

>
>Me: This is a bug. It's not setting the price plan on a cancellation reversal.

[snip]

>Colleague: I never thought of that. Tell the boss.

Obviously an organisation which does not reward the behavior of 'notice 
what appears to be an error, change the code, notify the boss'.

>
>First line of defense: Denial
…[5 more quoted lines elided]…
>Manager: Sure, you made it happen. Has it ever happened in the real world?

I'll try to avoid the check-list of a psychiatrist, Mr Wagner, and stick 
to the languages of harder sciences.  You present an observation ('the 
code will do (x)') and generate a series of conditions which confirm your 
observation.  The Manager questions whether the series of conditions you 
contrived are representative of Business As She Is Done.

>
>(Two hours research, searching millions of archived transactions.)

This is one reason of many for avoiding the Kubler-Ross model... not only 
was the experiment acceptable as basis for further questioning ('has it 
ever happened in the real world?') but time - both human and machine - 
were allowed to be used in further research.

(I am assuming that you did not do this research on your own free time, of 
course... and if the company did not freely allow you use of its own 
resources (CPU-time and XIOs cost money, you know) then I question the 
rationality of working with an organisation that demands you steal from it 
in order to try to save it money.)

>
>Second line of defense: Minimizing
…[5 more quoted lines elided]…
>Me: It happened five times yesterday. This year, it's happened 1,623 times. 

This, I would say, reflects more on the presentation of the data.  First 
the sample size and timeline, *then* the analyses of frequency, severity 
and cost.  'Five times yesterday'... those who have participated in a 'go 
live' or two, or seen a few divisions/corporations absorbed/spun off, 
might see that all 'yesteredays' are not equal.

'1,623 times' is also another imprecise statement.  'Millions of archived 
transactions'... assuming two million then 1,623 errors is an 
accuracy-rate of over 99%.  What kind of transaction-costs are involved? 
Not all widgets are the same, shoelaces are not steamships.  Stating the 
results as:

'Given an analysis of (n) transactions over (period) there were found to 
be (m) transactions showing the error noted.  Total costs for all errors 
to the company were (US$X), with an average cost of (US$Y) and a median 
cost of (US$Z).'

This is not bargaining with God or playing chess with the Grim Reaper, it 
is supplying data upon which a more financially-sound course of action 
might be based.  Given (what it costs) and (what it will cost to 
repair)... is it worth it?

This isn't rocket surgery... errrrr... brain science... errrrrrr... you 
don't need to be the sharpest knife in the chandelier to play this game.

(note to those unfamiliar with colloquial American English: if the above 
needs explaining please ask)

>
>Third line of defense: Blame Others
…[7 more quoted lines elided]…
>Manager: The customer signed off on it. And they didn't catch it during UAT. 

If it is costing the company sufficient money as to merit correction it 
might, given a statement of costs, be corrected.  

If it is costing the customer money AND IS WITHIN THE LAW... then it 
becomes a question of tangible versus intangible costs.

If it is costing the customer money AND IS ILLEGAL... then a lot of 
possibilities open up.  

(One of these possibilities could be for you, as the one who discovered 
that the company's 'previously undetected' (quotation marks intentional) 
illict actions, to hire someone to start your car in the morning because 
someone from Corporate is going to wire it to explode.)

>
>Fourth line of defense: Bargaining
…[6 more quoted lines elided]…
>Manager: Just do it and don't discuss it with the customer.

Refinement of a process so that it requires the least amount of energy in 
order to accomplish its necessary goal is a way to increase a system's 
chances of survival, Mr Wagner.  'Get the most from the least' is not only 
bargaining, it is pretty sound biology.

>
>Fifth line of defense: Depression = anger turned inward
…[6 more quoted lines elided]…
>Me: (knowing correct answer is You Did) I don't know, I didn't check.

Do not minimise your contribution, Mr Wagner... the error was *not* 
'obvious', it required *your* Special Eyes and Mind to see, understand, 
find experimentally, test for and determine the cost of... all of which 
was then submitted for Appropriate Management Approval, as it should be.  
You might want to consider a different approach of

'I was working on the code and this just seemed kind of... odd, so I 
looked into it while waiting for the compile/test run/lunch break to end.  
Sometimes, unpredictably, I'll give one away, for free, it is just part of 
my Nature... even though my Gran'pappy warned me about the kid at the 
schoolyard who'd say 'Oh, don't worry... the *first* one's *always* for 
free.'

In short... less attention to Kubler-Ross, Mr Wagner, and more attention 
to Newtonian mechanics, basic principles of accounting, a bit of biology 
and the simple economics demonstrated by a schoolyard drug-dealer might 
give the kind of light which shows the process differently.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-26T08:42:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MF5Dk.1098$W06.841@flpi148.ffdc.sbc.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <BqOdnWy124ywM0bVnZ2dnUVZ_jidnZ2d@earthlink.com> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com> <gbinm8$cet$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:gbinm8$cet$1@reader1.panix.com...
> In article <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>,
> Robert  <no@e.mail> wrote:
…[9 more quoted lines elided]…
>>>.....

I'd like a nickel for every time I've been asked to enhance / modify a 
"working" program and while testing  found an as-yet undiscovered bug.

If I did I sure as hell would not be spending my time posting on Usenet. 
Then again, I might just BUY Usenet.

MCM
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-26T13:52:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbipeq$76e$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com> <gbinm8$cet$1@reader1.panix.com> <MF5Dk.1098$W06.841@flpi148.ffdc.sbc.com>`

```
In article <MF5Dk.1098$W06.841@flpi148.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:gbinm8$cet$1@reader1.panix.com...
>> In article <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>,
…[13 more quoted lines elided]…
>"working" program and while testing  found an as-yet undiscovered bug.

I try not to discuss rates too much, Mr Mattias... but I think you might 
want to consider readjusting yours a bit upwards.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T21:34:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <oVKCk.2202$eb4.1240@flpi147.ffdc.sbc.com> <BqOdnWy124ywM0bVnZ2dnUVZ_jidnZ2d@earthlink.com> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com> <gbinm8$cet$1@reader1.panix.com>`

```
On Fri, 26 Sep 2008 13:22:16 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com>,
>Robert  <no@e.mail> wrote:
…[66 more quoted lines elided]…
>in order to try to save it money.)

The concept that CPU and IO cycles cost money is an obsolete one from the days of
mono-processor mainframes. I work on boxes having 64 or 128 CPUs that are idle >95% of the
time. Cycles are fixed overhead. Using them doesn't add any cost.

>>Second line of defense: Minimizing
>>
…[21 more quoted lines elided]…
>cost of (US$Z).'

You talk like an MBA. Did you work for Anderson Consulting?

>This is not bargaining with God or playing chess with the Grim Reaper, it 
>is supplying data upon which a more financially-sound course of action 
>might be based.  Given (what it costs) and (what it will cost to 
>repair)... is it worth it?

Financially Sound has a nice ring to it, but lost its cachet when three out of five
investment banks tanked within a week. It is now public knowledge that Imperial Titans Of
Finance had no clothes. 

>This isn't rocket surgery... errrrr... brain science... errrrrrr... you 
>don't need to be the sharpest knife in the chandelier to play this game.
…[27 more quoted lines elided]…
>someone from Corporate is going to wire it to explode.)

It's nothing more than a program bug, a logic error. 

>>Fourth line of defense: Bargaining
>>
…[10 more quoted lines elided]…
>bargaining, it is pretty sound biology.

The company's necessary goal was not to screw up, to charge the customer wrongly. No one
planned it. It was a MISTAKE. 

>>Fifth line of defense: Depression = anger turned inward
>>
…[23 more quoted lines elided]…
>give the kind of light which shows the process differently.

You're missing the essence of the story: emotional responses are lousy at handling
technical/logic problems. Source code isn't influenced by Denial, Minimizing, Blame,
Bargaining nor Anger. Yet those are the only tools managers have. They're trying to
marshall program logic with a tool designed to marshall people. What we have is a paradigm
clash. 

Programmers often champion "the best tool for the job." The tools available to managers
aren't in the ballpark, aren't even in the same county. 

If managers were rational, they'd fix the problem WITHOUT resorting to Denial, Minimizing,
etc.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-27T15:33:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbljoj$nsn$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com> <gbinm8$cet$1@reader1.panix.com> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com>`

```
In article <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 26 Sep 2008 13:22:16 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[74 more quoted lines elided]…
>time. Cycles are fixed overhead. Using them doesn't add any cost.

That variew from shop to shop, Mr Wagner, and I purposefully chose a 
worst-case scenario.  There are still shops out there which do 
machine-time chargebacks; the concept may be 'obsolete'... but the 
arguments over budgets, numbers with commas in them, are still there.  It 
might be wise to prepare for such possibilities.

>
>>>Second line of defense: Minimizing
…[24 more quoted lines elided]…
>You talk like an MBA. Did you work for Anderson Consulting?

Next, of course, comes questioning my accent... 'Listen to how he drops 
his 'g's and shifts dental fricatives to hard dentals... you couldn't 
believe someone who talked like *that*, could you?'

If one is interested in usefulness, Mr Wagner - as you may, at times, have 
claimed to be - the source is secondary to the value gained.  I was never 
an Anderoid but I have read Frederick Winsolw Taylor's 'The Principles of 
Scientific Management' and written a few laboratory reports for an organic 
chemistry professor.

I also subscribe to The Economist... the language they use, at times, is 
beautiful, they give me ways to see the world I have not had before... and 
it can be used as a sort of Know Your Enemy campaign.

>
>>This is not bargaining with God or playing chess with the Grim Reaper, it 
…[8 more quoted lines elided]…
>Finance had no clothes. 

That, of course, is a *perfect* reason for you to jump off the Brooklyn 
Bridge, as well... and I am the King of England.  The manager is given 
'Here's what it is costing you, here is what it will cost to fix.  You 
control the budget, you have the information, you make the call.'

>
>>This isn't rocket surgery... errrrr... brain science... errrrrrr... you 
…[30 more quoted lines elided]…
>It's nothing more than a program bug, a logic error. 

No, Mr Wagner... in the third instance it is a system function which 
overcharges the customer AND IS ILLEGAL (caps original).  Companies do... 
funny things in order to keep making money on activities.

>
>>>Fourth line of defense: Bargaining
…[15 more quoted lines elided]…
>planned it. It was a MISTAKE. 

Thecompany's necessary goal is to Make Money, Mr Wagner, just as any other 
company's.  Your own small, singular example might be taken out of an 
isolated, atomised status and be seen as the beginning of a Way To Do 
Things Differently.

>
>>>Fifth line of defense: Depression = anger turned inward
…[28 more quoted lines elided]…
>technical/logic problems.

I'd say I was finding that as the exact essence of the story, Mr Wagner... 
but instead of the emotional responses coming only from the client side 
they also came from the side which approached the situation based on the 
Kubler-Ross model, a model based on an emotional experience (remember that 
the book was 'On Death and Dying'? hard to get much more emotional than 
that).

Perhaps approaching a situation using less emotionally-laden models - the 
models of the laboratory, not the models of the funeral-home - might lead 
to different reception, different results and an entirely different 
status.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-27T13:37:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <dabod4pgnntf1ukd1kgthlcslarsf267cb@4ax.com> <gbinm8$cet$1@reader1.panix.com> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com>`

```
On Sat, 27 Sep 2008 15:33:39 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com>,
>Robert  <no@e.mail> wrote:

>>>This is not bargaining with God or playing chess with the Grim Reaper, it 
>>>is supplying data upon which a more financially-sound course of action 
…[12 more quoted lines elided]…
>control the budget, you have the information, you make the call.'

The catch is that there's never a budget for bug fixes. Budgets are allocated for
acquisitions and enhancements. Management refuses to acknowledge there are bugs in
existing code. Fixing bugs comes under Maintenance, which does not follow the development
Process of design, review and testing. As a result, bug fixes often introduce new bugs. 

>>>In short... less attention to Kubler-Ross, Mr Wagner, and more attention 
>>>to Newtonian mechanics, basic principles of accounting, a bit of biology 
…[17 more quoted lines elided]…
>status.

Programmers in the trenches DO follow the laboratory model. They just want the system to
work correctly. Managers apply the emotional model.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-27T23:14:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbmeo1$8hn$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com>`

```
In article <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 27 Sep 2008 15:33:39 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[19 more quoted lines elided]…
>The catch is that there's never a budget for bug fixes.

Of course... so if there's never a budget for bug fixes, and a bug is 
demonstrated to be costing (US$n/period) then the bug will never get fixed 
and the company will continue to lose money.

Did I mention that I am the King of England?

[snip]

>>>>In short... less attention to Kubler-Ross, Mr Wagner, and more attention 
>>>>to Newtonian mechanics, basic principles of accounting, a bit of biology 
…[19 more quoted lines elided]…
>want the system to work correctly. Managers apply the emotional model.

Nothing is true of all groups in all places at all times, including these 
statements:  

If programmers 'just wanted the system to work correctly' then nobody 
would crack a smile at the mention of 'Look, Mom, I'm a Programmer! code', 
showing off - often, badly - a newly-learned technique or subtlety. 

If managers 'applied the emotional model' then there would never be mass 
layoffs or offshoring because of the human devestation that is wrought.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-27T21:55:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com>`

```
On Sat, 27 Sep 2008 23:14:09 +0000 (UTC), docdwarf@panix.com () wrote:


>If managers 'applied the emotional model' then there would never be mass 
>layoffs or offshoring because of the human devestation that is wrought.

Boomers/yuppies are a 'me generation' that doesn't care about others. Fortunately, they're
now shuffling off stage in preparation for the official Passing Of The Baton to the X-Gen
contingent, led by Obama. Good riddence. 

Some of them, in their 50s, will refuse to acknowledge the ouster applies to them. They
will have to be helped to the Acceptance stage. Pointing out they have 401Ks might be all
it takes.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-28T07:19:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbnb6s$1gh$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com>`

```
In article <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 27 Sep 2008 23:14:09 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[4 more quoted lines elided]…
>Boomers/yuppies are a 'me generation' that doesn't care about others.

Then coders who are boomers/yuppies would seem not to care about systems, 
they would care about themselves, violating your previous assertion... but 
hey, that was yesterday, right?

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 12)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-28T08:04:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com...
> On Sat, 27 Sep 2008 23:14:09 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[10 more quoted lines elided]…
> it takes.

Wait until it's your turn.

MCM
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-28T21:39:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbotis$b5$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com>`

```
In article <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>"Robert" <no@e.mail> wrote in message 
>news:1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com...
>> On Sat, 27 Sep 2008 23:14:09 +0000 (UTC), docdwarf@panix.com () wrote:
>>
>> Boomers/yuppies are a 'me generation' that doesn't care about others. 

Mr Mattias, please check your attributions.  I do not recall posting what 
appears to be attributed to me.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 13)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-07T10:40:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcg6th$gqa$2@venn.venn.bc.ca>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com>`

```
Michael Mattias wrote:

> 
> 
…[17 more quoted lines elided]…
> 

Robert (now known as Fumin bin Lyin; see http://fumingmad.com ) cringes in
the fear that the "boomers/yuppies" that he professes to despise will take
away his cigarettes from him. These cigarettes are all he has left.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 14)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-07T20:33:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca>`

```
On Tue, 07 Oct 2008 10:40:01 -0700, Robert Broughton <rbronews2@broug8hton.ca> wrote:

>Michael Mattias wrote:
>
…[23 more quoted lines elided]…
>away his cigarettes from him. These cigarettes are all he has left.

What do boomers have left? Upsidedown mortages on houses they planned to 'flip,' until the
bottom fell out. 401Ks that will soon be worth half what they were a year ago. SUVs. A
president impeached for acting like trailer trash in the Oval Office.  A failed war in
Iraq. "Greed is good." Destruction of the world's banking system.

"And why do you look at the speck in your brother's eye, but do not perceive the plank in
your own eye? "

I'm moving to a prestigous job in Florida; boomers are on the way out. Sayonara.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-08T01:37:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gch2sf$rpd$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com>`

```
In article <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>I'm moving to a prestigous job in Florida; boomers are on the way out.

I thought that boomers were reaching the age when Florida was The Place To 
Be... welcome to the National Low-Sodium Section.

Are you going to FPL in Jacksonville, perchance?

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 16)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-07T22:05:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com> <gch2sf$rpd$1@reader1.panix.com>`

```
On Wed, 8 Oct 2008 01:37:19 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com>,
>Robert  <no@e.mail> wrote:
>
>[snip]

Robert Broughton is a hate monger from alt.smokers who has turned into a cross posting
troll. My apologies for attracting him here.

>>I'm moving to a prestigous job in Florida; boomers are on the way out.
>
>I thought that boomers were reaching the age when Florida was The Place To 
>Be... welcome to the National Low-Sodium Section.

Fittingly, the real estate bubble burst is bad in Florida. Just in time for them to buy
their deam houses for half price. 

>Are you going to FPL in Jacksonville, perchance?

No. I'm moving to central Florida, in the Titusville-Orlando area.
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-08T09:25:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gchuaq$j$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com> <gch2sf$rpd$1@reader1.panix.com> <js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com>`

```
In article <js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com>,
Robert  <no@e.mail> wrote:
>On Wed, 8 Oct 2008 01:37:19 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>troll. My apologies for attracting him here.

I've seen the type before, Mr Wagner, and while I know there's no need for 
the apology - welcome to the UseNet and all that - I can find reasons for 
it... I've run across similar phenomena before.

>
>>>I'm moving to a prestigous job in Florida; boomers are on the way out.
…[10 more quoted lines elided]…
>No. I'm moving to central Florida, in the Titusville-Orlando area.

I hope you find the environs salubrious and the work to be interesting to 
you, of benefit to others and remunerative.

DD
```

###### ↳ ↳ ↳ Re: Here's one problem

_(reply depth: 17)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-09T08:14:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcl75f$pdk$2@venn.venn.bc.ca>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com> <gch2sf$rpd$1@reader1.panix.com> <js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com>`

```
Robert wrote:

> 
> 
…[8 more quoted lines elided]…
> cross posting troll. My apologies for attracting him here.

Wrong again, liar. I wrote my first COBOL program in 1970. You did not
attract me here. And the biggest hate monger in alt.smokers is you.

If you want to apologize for something, apologize for being a serial liar.
(See http://fumingmad.com ) 
```

###### ↳ ↳ ↳ OT: Re: Here's one problem

_(reply depth: 18)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-09T21:35:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdete4h6sgve3r6hleiool5a9j14pd19aq@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com> <gch2sf$rpd$1@reader1.panix.com> <js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com> <gcl75f$pdk$2@venn.venn.bc.ca>`

```
On Thu, 09 Oct 2008 08:14:55 -0700, Robert Broughton <rbronews2@broug8hton.ca> wrote:

>Robert wrote:

>> On Wed, 8 Oct 2008 01:37:19 +0000 (UTC), docdwarf@panix.com () wrote:
>> 
…[8 more quoted lines elided]…
>Wrong again, liar. I wrote my first COBOL program in 1970. 

Good, say something in COBOL.

>You did not attract me here. 

Then why ARE you here?

>And the biggest hate monger in alt.smokers is you.

Try a more appropriate newsgroup, like england.rec.gardening.

>If you want to apologize for something, apologize for being a serial liar.

If I did, no one would believe me. Instead I'll say you're a brilliant logician who does
NOT work in RPG and has a good grasp of netequitte.

Correct me if I'm wrong.
```

###### ↳ ↳ ↳ Re: OT: Re: Here's one problem

_(reply depth: 19)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-10T12:09:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nLNHk.10884$jZ3.6069@newsfe03.iad>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com> <gch2sf$rpd$1@reader1.panix.com> <js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com> <gcl75f$pdk$2@venn.venn.bc.ca> <gdete4h6sgve3r6hleiool5a9j14pd19aq@4ax.com>`

```
Fumin bin Lyin wrote:

>>
>>Wrong again, liar. I wrote my first COBOL program in 1970.
> 
> Good, say something in COBOL.
>

INSPECT SUBJECT-FIELD TALLYING TALLY-FIELD FOR ALL COMMA.
 
>>You did not attract me here.
> 
> Then why ARE you here?

What part of "I wrote my first COBOL program in 1970" did you not
understand?

> 
>>And the biggest hate monger in alt.smokers is you.
…[5 more quoted lines elided]…
> If I did, no one would believe me.

Indeed. See http://fumingmad.com/
```

###### ↳ ↳ ↳ Re: OT: Re: Here's one problem

_(reply depth: 20)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-10T20:40:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n00f4huvakmngn6r4c07qqsvkhnah6ab4@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <i02oe4hio7kfe2v8ad45rugited3v5bk7f@4ax.com> <gch2sf$rpd$1@reader1.panix.com> <js7oe4h91jgp09ov7c9qhc7bbb174ndvne@4ax.com> <gcl75f$pdk$2@venn.venn.bc.ca> <gdete4h6sgve3r6hleiool5a9j14pd19aq@4ax.com> <nLNHk.10884$jZ3.6069@newsfe03.iad>`

```
On Fri, 10 Oct 2008 12:09:06 -0700, Robert Broughton <rbronews2@broug8hton.ca> wrote:

>Fumin bin Lyin wrote:
>
…[6 more quoted lines elided]…
>INSPECT SUBJECT-FIELD TALLYING TALLY-FIELD FOR ALL COMMA.

Bzzt, you fail. COMMA is a reserved word, as in DECIMAL-POINT IS COMMA, but not a
figurative constant. That statement will not compile. 

>>>You did not attract me here.
>> 
…[3 more quoted lines elided]…
>understand?

You haven't said a word about Cobol except the failed attempt above. 

You may find it hard to believe, all Usenet is not a playground for trolls like you. There
ARE newsgroups having legitimite on-topic issues to discuss. This is one of them. If you
have nothing to say about Cobol, say it elsewhere or kiss your ISP goodbye.
```

###### ↳ ↳ ↳ OT: hate mail WAS: Re: Here's one problem

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-08T17:16:03+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6l2qg5Fa5ifnU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca>`

```


"Robert Broughton" <rbronews2@broug8hton.ca> wrote in message 
news:gcg6th$gqa$2@venn.venn.bc.ca...
> Michael Mattias wrote:
>
…[25 more quoted lines elided]…
>

I can't see the point in a site such as this. I had a look at it, then noted 
it is up for sale.

I reckon if you have an axe to grind with someone, slug it out fairly in a 
forum where there is a right of reply, not on a very primitive, 
"after-school", hand made web site, which you then expect people to buy from 
you so they can use it to perpetuate more similar nonsense.

How brave is that? Take a bunch of cheap shots at someone who you dislike, 
without giving them any chance to defend themself? If the site was a blog 
(and, frankly you could set up a blog from a template that would be far 
better than that site, and cost you nothing...) at least other people as 
well as the person being attacked could discuss the issue. You never know, 
rather than just a flame fest the group might come up with some useful 
ideas...)

While this is an unmoderated forum, and that's usually a "Good Thing" you 
have demonstrated the downside of that policy.

The least you could do was prefix your hate mail with OT...

I'd prefix it with OTT, because I see it as over the top.

Pete.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 15)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-09T08:10:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcl6sl$pdk$1@venn.venn.bc.ca>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net>`

```
Pete Dashwood wrote:

> 
> 
…[33 more quoted lines elided]…
> I can't see the point in a site such as this.

Robert/Fumin bin Lyin has the bad habit of calling people liars. For a
while, I was posting the list of his lies in response when he did this.
Adding the list to http://fumingmad.com/ was just a matter of convenience
and brevity. It's easier to just post the URL every time instead of posting
the list.

The story of how the http://fumingmad.com/ site originated is, Fumin bin
Lyin I (Robert is Fumin bin Lyin II) let his domain name lapse.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-10T12:10:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6l7hbqFb4u7fU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca>`

```


"Robert Broughton" <rbronews2@broug8hton.ca> wrote in message 
news:gcl6sl$pdk$1@venn.venn.bc.ca...
> Pete Dashwood wrote:
>
…[37 more quoted lines elided]…
> Robert/Fumin bin Lyin has the bad habit of calling people liars.

Bob, I know this is irritating. There was a time when I used to get very 
unwrapped when someone did this to me, especially when I knew it wasn't the 
case. (I try very hard not to deliberately lie because the results of doing 
so are just too complex for my aging brain to keep up with.)

However, Usenet and the Internet are places where we expose ourselves to all 
kinds of abuse.

It really isn't a place for sensitivity. (I know this, because in real life 
I am quite sensitive and have been hurt by posts here on a number of 
occasions.) But even in negative experiences there is growth. It has been a 
long time since I was actually hurt by posts here, although I do get stung 
occasionally... :-)

The answer is not to respond in kind but to calmly and dispassionately ask 
for the reasoning behind the accusation.

(Considered grown-up response, rather than childish indulgenece of the 
immediate emotional reaction...)

Someone calls you a liar. Did you lie? If you didn't, state that you didn't 
and ask for the reasoning that led them to this conclusion. If you have 
evidence supporting your assertion, produce it. (Unfortunately, on one 
famous occasion here with one particular person who called me a liar, even 
sending him the evidence privately so as not to publicly humiliate him, was 
not enough to get him to withdraw his stupid statement. Sometimes people say 
things in anger that they really can't support and then, having painted 
themselves into a corner it is impossible for them to back down. Eventually, 
you just have to let it go.)

If you did lie, then accept that what is being said is the truth, but point 
out in your own defence that you do not habitually do so and on this 
occasion there was probably stress or some other extenuating circumstance. 
Most of us can relate to people being Human.

I don't know the circumstances under which Robert called you a liar, but I 
can't believe he would do so unprovoked.

Don't take it to heart. Responding by pillorying someone on a public web 
site will not win people to your cause.

> while, I was posting the list of his lies in response when he did this.

While that is a playground response, it is the one that most of us would 
naturally go with... :-)

"You're a liar"
"No, you're a liar"
"No, you're a liar."

As if showing that the other person lies has any bearing on your own 
fabrication :-)

> Adding the list to http://fumingmad.com/ was just a matter of convenience
> and brevity. It's easier to just post the URL every time instead of 
> posting
> the list.

The question I would ask is: "What does such a list achieve?".

OK, it helps you vent your anger, but do you think anyone is actually 
persuaded by it?

In fact, a fair-minded neutral observer (like me... :-)) is more likely to 
consider it a cheap shot than to avidly rush into agreement with the 
sentiments expressed.

The internet is an irritating place sometimes, and there are definitely 
people we would rather not communicate with. You have a perfect right to 
choose who you are OK with and who you are not, but you will win more 
support by being fair and open than you will by sniping from cover.

If you have an issue with Robert (or anyone else...) the best course is to 
state it and see what the response is. You might be surpprised at the 
result.  More importantly, it is good practise for learning to settle 
differences in a way that is acceptable, grown-up, and leaves you with your 
dignity intact.

Flaming is for kids who don't know better; adults resolve differences like 
men... (And that doesn't always require pistols at dawn...)

Whern all is said and done, you don't have to like Robert, or even have any 
truck with him at all.

But your present course actually diminishes you more than it harms him.

Think on it.

Pete.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-09T23:36:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net>`

```
On Fri, 10 Oct 2008 12:10:48 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>"Robert Broughton" <rbronews2@broug8hton.ca> wrote in message 
>news:gcl6sl$pdk$1@venn.venn.bc.ca...
>> Pete Dashwood wrote:
>>> "Robert Broughton" <rbronews2@broug8hton.ca> wrote in message
>>> news:gcg6th$gqa$2@venn.venn.bc.ca...

>>>> Robert (now known as Fumin bin Lyin; see http://fumingmad.com ) cringes
>>>> in the fear that the "boomers/yuppies" that he professes to despise will
…[8 more quoted lines elided]…
>case. 

Unsupported name calling doesn't upset me. It makes the other party look foolish.

>However, Usenet and the Internet are places where we expose ourselves to all 
>kinds of abuse.

Abusers embarrass themselves in public. I don't have to lift a finger. There is no easier
way to win points. 

>Someone calls you a liar. Did you lie? If you didn't, state that you didn't 
>and ask for the reasoning that led them to this conclusion. If you have 
>evidence supporting your assertion, produce it. 

I rebutted with facts BEFORE Broughton wrote his web page. He ignored what I said.
For instance, he said "The number of US uniformed personnel in either Laos or Cambodia was
very small."  I had not made any claims about uniforms nor numbers, but cited Operation
White Star as contrary evidence.

In 1961, however, the United States lent full and open support to the Vientiane government
and the program was renamed "Operation White Star" with U.S. soldiers openly wearing their
uniforms.
http://en.wikipedia.org/wiki/Operation_White_Star

"At its peak on 23 July 1962 when a Declaration of Neutrality was signed, the White Star
strength was 433."
http://www.psywarrior.com/LaosPSYOP.html

What irks him is that I don't just call people liars, I PROVE it with  evidence. He
doesn't know what to do, so he writes a web page callimg me a liar. As you said, it a
schoolyard response, "No, you're a liar." 

>I don't know the circumstances under which Robert called you a liar, but I 
>can't believe he would do so unprovoked.

It was about political issues. I didn't call him personally a liar, I said it about
representatives of the antismoking movement he champions.

>Don't take it to heart. Responding by pillorying someone on a public web 
>site will not win people to your cause.

Don't tell him that. I WANT people to be repelled by his cause. The more he misbehaves,
the more popular support it loses.

>> Adding the list to http://fumingmad.com/ was just a matter of convenience
>> and brevity. It's easier to just post the URL every time instead of 
…[6 more quoted lines elided]…
>persuaded by it?

Yes, they're persuaded AGAINST his movement.

Suppose you are running for office and your opponent shows up for debate wearing a clown
suit. Would you ask him to take it off and debate like an adult, or just let him destroy
his own image?
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-10T20:48:30+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6l8fmgFauu46U1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com...
> On Fri, 10 Oct 2008 12:10:48 +1300, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[26 more quoted lines elided]…
>

Maybe. It is tiresome and unnecessary.

>>However, Usenet and the Internet are places where we expose ourselves to 
>>all
…[4 more quoted lines elided]…
> way to win points.

That rather depends on the point of view of the people witnessing it.

>
>>Someone calls you a liar. Did you lie? If you didn't, state that you 
…[22 more quoted lines elided]…
> http://www.psywarrior.com/LaosPSYOP.html

So, 45 years later, two intelligent men can move each other to extreme anger 
over points that really have very little bearing on their lives now?

(Yeah, I know, we all do it... it's just easier to see when it's other 
people... :-))


>
> What irks him is that I don't just call people liars, I PROVE it with 
> evidence.

Then it is kind of redundant to actually do the namecalling, isn't it? :-)


>He
> doesn't know what to do, so he writes a web page callimg me a liar. As you 
…[8 more quoted lines elided]…
> representatives of the antismoking movement he champions.

Excellent. There is a perfectly reasonable and moderate statement. Actually, 
very little is achieved by anybody calling anybody a liar, when the evidence 
can simply be produced. My point is that people can have differences; how 
they solve them says much about the people... :-)

>
>>Don't take it to heart. Responding by pillorying someone on a public web
…[5 more quoted lines elided]…
>

Most of us are not keen on extreme positions. I know that anti-smokers can 
get very worked up about it, but it really doesn't help the cause. 
Personally, I quit smoking cigarettes about 30 years ago and the idea really 
repels me now. (I don't let people smoke in my house or car, but I'm OK with 
them doing it in the garden... :-)) And yet, I can enjoy a cigar and a 
brandy occasionally (say 3 times a year...) without feeling the need to 
start smoking again. (It is the Buddhist "middle way"... obsessively NOT 
doing something, is just as bad as obsessively doing it... :-))

>>> Adding the list to http://fumingmad.com/ was just a matter of 
>>> convenience
…[10 more quoted lines elided]…
>

His movement is actually fine. People have a right to smoke or not smoke and 
a right to lobby for their position. Most non-smokers undestand the need of 
smokers to smoke. The problem is when it is also inflicted on people who 
DON'T want it.  I have no problem with people smokng if they want to, as 
long as they do it far away from me... Like I said before, it is HOW we 
address differences that defines us as people.

"Do you mind if I smoke...?"
"I'd rather you didn't... Do you mind if I fart?"
(We both understand each other...)

> Suppose you are running for office and your opponent shows up for debate 
> wearing a clown
…[3 more quoted lines elided]…
>

Well, we really shouldn't judge people by how they look so I'd probably 
completely ignore the clown suit and just get to the debate. On the other 
hand if he was using the suit to get support (like, everybody loves 
clowns...:-)) I'd have to comment  and it would be something like: "Thanks 
for taking the time to wear your best outfit tonight, are you free for 
childrens' parties...?"  For the rest of the evening he would be addressed 
as "Bozo"... no malice, just like it was his name. :-)

Sometimes a sense of humour can be a life preserver...:-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 19)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-10T08:29:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0njue49an5jna4sh7cr0teim05o9i12nm1@4ax.com>`
- **References:** `<844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <6l8fmgFauu46U1@mid.individual.net>`

```
On Fri, 10 Oct 2008 20:48:30 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>His movement is actually fine. People have a right to smoke or not smoke and 
>a right to lobby for their position. Most non-smokers undestand the need of 
…[3 more quoted lines elided]…
>address differences that defines us as people.

A troll's objective is sparking an off-topic discussion like this. I'll just say there's a
lot more than 'rights', addiction and dislike of odor going on behind the scenes; it's
really about money. The pharmaceutical industry has secretly led the movement in order to
extend life expectancy through social engineering. Old people are its best customers.
Coercing a 50 year old into quitting today will return $1,000 profit (present value)  in
25 years. Investing $100 to get $1,000 return is simply good business. They quit doing it
last year (did you miss the announcement?) because coercion became too expensive.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 20)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-10T12:02:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LENHk.10751$jZ3.5664@newsfe03.iad>`
- **References:** `<844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <6l8fmgFauu46U1@mid.individual.net> <0njue49an5jna4sh7cr0teim05o9i12nm1@4ax.com>`

```
Fumin bin Lyin wrote:

> The pharmaceutical
> industry has secretly led the movement in order to extend life expectancy
> through social engineering.

Booga booga.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-11T11:32:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6la3gnFbdfnvU1@mid.individual.net>`
- **References:** `<844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <6l8fmgFauu46U1@mid.individual.net> <0njue49an5jna4sh7cr0teim05o9i12nm1@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:0njue49an5jna4sh7cr0teim05o9i12nm1@4ax.com...
> On Fri, 10 Oct 2008 20:48:30 +1300, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[25 more quoted lines elided]…
>
I don't uderstand any of what you wrote, Robert. But it doesn't matter.

From the posts being made here it is pretty obvious that reason will not 
prevail so I won't be responding further on this.

It  is simply sad to see people who should know better behaving like this.

Pete.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 19)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-10T12:00:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bDNHk.10719$jZ3.10509@newsfe03.iad>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <6l8fmgFauu46U1@mid.individual.net>`

```
Pete Dashwood wrote:

> Actually, very little is achieved by anybody calling anybody a liar,

Actually, a lot can be achieved by publicly identifying liars as liars. 

Get copies of _Rush Limbaugh is a Big Fat Liar_ and _Lies and the Lying
Liars who Tell Them_ (both by Senatorial candidate Al Franken) and read
them.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 18)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-10-10T12:02:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6l8uibFbavddU1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com>`

```
In article <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com>,
	Robert <no@e.mail> writes:
> 
> Suppose you are running for office and your opponent shows up for
> debate wearing a clown suit.

I thought they all did.

>                               Would you ask him to take it off and
> debate like an adult, or just let him destroy his own image? 

I have never known or even seen a politiician with an image worth
worrying about.


bill
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 18)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-10T11:55:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UyNHk.10634$jZ3.988@newsfe03.iad>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com>`

```
Fumin bin Lyin wrote:

> 
> Unsupported name calling doesn't upset me.

Supported facts don't seem to influence you much, either.

> 
> It was about political issues.

No, it was about lies that Robert Wagner told about himself, the
addictiveness of tobacco, scientists, the medical profession, illiteracy
and newpapers in Nigeria, Shawn Hinn, and anti-tobacco activists.

Oh yes, he also wrote that the German Nazis "got a few things right and, if
nothing else, didn't disgrace themselves."

Anyone who chooses to do so can read all of this for themselves at
http://fumingmad.com/
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 19)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-10T20:01:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qsve4hciufl8nmpn71ascp374kkr4tkrm@4ax.com>`
- **References:** `<844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <UyNHk.10634$jZ3.988@newsfe03.iad>`

```
On Fri, 10 Oct 2008 11:55:47 -0700, Robert Broughton <rbronews2@broug8hton.ca> wrote:

>> It was about political issues.
>
>No, it was about lies that Robert Wagner told about himself, the
>addictiveness of tobacco, scientists, the medical profession, illiteracy
>and newpapers in Nigeria, Shawn Hinn, and anti-tobacco activists.

Go away, pest. Your postings are unwelcome and totally inappropriate in this newsgroup.

But thanks for showcasing your stupidity by naming the wrong country. The discussion was
about Niger, not Nigeria. The Nigerien (not Nigerian) illiteracy rate is 80%.

>Oh yes, he also wrote that the German Nazis "got a few things right and, if
>nothing else, didn't disgrace themselves.

We're not all tabloid readers limited to black and white judgements.

If you continue posting here, sjrb.ca will be notified that you're violating their AUP.
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 20)_

- **From:** Robert Broughton <rbronews2@broug8hton.ca>
- **Date:** 2008-10-10T19:09:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MVTHk.357$R%4.211@newsfe08.iad>`
- **References:** `<844rd41q4jj3hb1cetmnr8atho22fovlo4@4ax.com> <gbljoj$nsn$1@reader1.panix.com> <7ntsd4lhhgvm2i224f3tsdfl85jjbt6a6c@4ax.com> <gbmeo1$8hn$1@reader1.panix.com> <1crtd4d7jhjphp33jdh6c5do7u58ppkoss@4ax.com> <WGLDk.1968$c45.894@nlpi065.nbdc.sbc.com> <gcg6th$gqa$2@venn.venn.bc.ca> <6l2qg5Fa5ifnU1@mid.individual.net> <gcl6sl$pdk$1@venn.venn.bc.ca> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <UyNHk.10634$jZ3.988@newsfe03.iad> <9qsve4hciufl8nmpn71ascp374kkr4tkrm@4ax.com>`

```
Fumin bin Lyin wrote:

> On Fri, 10 Oct 2008 11:55:47 -0700, Robert Broughton
> <rbronews2@broug8hton.ca> wrote:
…[9 more quoted lines elided]…
>

Gee, I just can't imagine why you would feel this way. :-)
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-11T04:57:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcpbod$1rk$1@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <UyNHk.10634$jZ3.988@newsfe03.iad>`

```
In article <UyNHk.10634$jZ3.988@newsfe03.iad>,
Robert Broughton  <rbronews2@broug8hton.ca> wrote:

[snip]

>No, it was about lies that Robert Wagner told about himself, the
>addictiveness of tobacco, scientists, the medical profession, illiteracy
>and newpapers in Nigeria, Shawn Hinn, and anti-tobacco activists.

... and let's not forget the time he spent in upstate New York, in a town 
near a Great Natural Wonder known the world over... a little town called 
'Niagara Falls'...

NNNNIIIIAAAGGGGAAARRRRAAAA FFFFAAAALLLLLSSSSSS!!!!..... *Slooooooowly* he 
turned, *step* by step, *inch* by inch...

... oh... sorry... did I say that out loud?

DD
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 20)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-10-11T12:40:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tz5Ik.5468$0e6.2449@newsfe09.iad>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <6l7hbqFb4u7fU1@mid.individual.net> <oggte4db6thl7cm1490ravniqvgmdrif5c@4ax.com> <UyNHk.10634$jZ3.988@newsfe03.iad> <gcpbod$1rk$1@reader1.panix.com>`

```
???? Wayne & Schuster ???

<docdwarf@panix.com> wrote in message news:gcpbod$1rk$1@reader1.panix.com...
> In article <UyNHk.10634$jZ3.988@newsfe03.iad>,
> Robert Broughton  <rbronews2@broug8hton.ca> wrote:
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: hate mail WAS: Re: Here's one problem

_(reply depth: 21)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-10-13T15:23:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcvp5i$sj2$2@reader1.panix.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <UyNHk.10634$jZ3.988@newsfe03.iad> <gcpbod$1rk$1@reader1.panix.com> <tz5Ik.5468$0e6.2449@newsfe09.iad>`

```
In article <tz5Ik.5468$0e6.2449@newsfe09.iad>, tlmfru <lacey@mts.net> wrote:

[top-posting prompted by a reference to Niagara Falls and turning 
slooooooowly]

>???? Wayne & Schuster ???

An Olde Standard of uncertain provenanace, I believe... I've seen Abbot & 
Costello do a similar routine about Floogle Street and the Susquehanna Hat 
Company and I'm sure it has shown up other places as well.

DD
```

#### ↳ Re: Freeware tool and code to ponder on...

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-09-26T16:42:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48DD10F0.6F0F.0085.0@efirstbank.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net>`

```
Nice web page!  And interesting project.  I will have to download it some
weekend and take a deeper look before making any more detailed comments.

I did find amusing Robert's posititioning of the period terminators.  I
think he must have them as much as I do.  I'm not sure I'm ready to go that
far, though!  :-)

Frank
```

##### ↳ ↳ Re: Freeware tool and code to ponder on...

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-27T12:03:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k5bj8F66147U1@mid.individual.net>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <48DD10F0.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:48DD10F0.6F0F.0085.0@efirstbank.com...
> Nice web page!  And interesting project.  I will have to download it some
> weekend and take a deeper look before making any more detailed comments.
…[7 more quoted lines elided]…
>
Yes, my eyes widened a bit when I first saw it :-). However, it seems to 
work fine. I have worked on sites where people were programming stored 
procedures in SQL and it seems to be pretty standard practice for that.

I'm not personally ready to make the jump, yet, but since working with 
Robert's code it has become less unfamiliar and I think it could have some 
advantages.

Thanks for the kind words, Frank. I hope you will find time to download and 
try the tool.

Pete.
```

##### ↳ ↳ Re: Freeware tool and code to ponder on...

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-26T19:06:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drsqd49s4ssi7cv10ghp8o94nubeecujs7@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <48DD10F0.6F0F.0085.0@efirstbank.com>`

```
On Fri, 26 Sep 2008 16:42:24 -0600, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
wrote:

>Nice web page!  And interesting project.  I will have to download it some
>weekend and take a deeper look before making any more detailed comments.
…[3 more quoted lines elided]…
>far, though!  :-)

Terminator in front is common in the world of PL/SQL. 

There is an intermediate style I've seen in a lot of Modern Cobol (no snickering)
production code. They put the period on a line by itself at the end of each paragraph.

paragraph-1.
    stuff
    stuff
    .
paragraph-2.

 I think it derives from the C style:

{ stuff.
   stuff
}

The best solution, IMO, would be for the compiler to honor indentation, where an outdent
signals the end of a block. That's how Python works. That's how humans read code. A
language should be designed for the convenience of humans, not parsers.
```

###### ↳ ↳ ↳ Re: Freeware tool and code to ponder on...

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-09-26T20:49:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4bhDk.138$J63.72@newsfe08.iad>`
- **In-Reply-To:** `<drsqd49s4ssi7cv10ghp8o94nubeecujs7@4ax.com>`
- **References:** `<6jr3fmF4lc1iU1@mid.individual.net> <48DD10F0.6F0F.0085.0@efirstbank.com> <drsqd49s4ssi7cv10ghp8o94nubeecujs7@4ax.com>`

```
Robert wrote:
> On Fri, 26 Sep 2008 16:42:24 -0600, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
> wrote:
…[31 more quoted lines elided]…
> 

No I don't think it derives from C style - I think if you look at the 
dummy program I did for John using Easytrieve with a COBOL sub-program, 
I play safe by putting a period on a separate line before the next 
paragraph name. Of course that doesn't apply with OO methods, except for 
those few methods which might use paragraphs for convenience.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
