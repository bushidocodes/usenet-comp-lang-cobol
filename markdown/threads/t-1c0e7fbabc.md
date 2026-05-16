[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Odd" little programming challenge

_5 messages · 3 participants · 2004-05_

---

### "Odd" little programming challenge

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-11T06:34:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xt_nc.15863$V97.9345@newsread1.news.pas.earthlink.net>`

```
to: comp.lang.cobol
        and
     IBM-main
        and
     SHARE LNGC & DVLG projects

IBM has posted a "cross-language" programming challenge that was brought to my
attention in the comp.lang.pli newsgroup.

As someone posted there, this is *NOT* a "real-world" program, but it does allow
one to compare programming "styles" for a "minimalist" program.

I have *just* (today) started working on a COBOL program.  It works with the
"small" input file (using at least one PC COBOL compiler), but I have a logic
bug (that I haven't found so far) when handling the "million record" input file.

The specifications (with test-data) are at:
   http://www2.hursley.ibm.com/decimal/telco.html

My "work-in-progress" COBOL program is available (in "text format") at:
    http://home.netcom.com/~wmklein/dox/TELCO.txt

I have used MOSTLY standard COBOL, so my "starting program" should be relatively
easy to port to almost all '85 Standard (with one intrinsic function) compilers.
I did, however, go over the "traditional" column 72 for the R-margin and have
used "*>" for inline comments (pretty easy to comment out).  (I even used
A-/B-margins for those with compilers still requiring this).

  ****

I would be HAPPY if anyone can tell me where my "logic error is" (why I don't
get the expected totals with the large input file).  My *guess* is that it has
to do with the "odd" (to me) HALF-EVEN rounding rules that are required in the
specifications (i.e round to nearest even decimal point for ".xx5" results).

I really, REALLY, believe there are "tons" of ways to do this program in COBOL -
much less in lots of other languages.  I would be happy to "post" on my
web-space any other COBOL solutions (showing "better" and/or "different" styles
than mine).

I have *not* (yet?) tried to optimize my program for performance (my use of
Packed-Decimal, Display, *and* Binary numeric formats is BOUND to be
inefficient).  Nor have I yet put any comments in the program.  It should be
(medium-) clear to most experienced COBOL programmers.
```

#### ↳ Re: "Odd" little programming challenge

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-05-11T12:37:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hO3oc.74$uL5.6@newssvr33.news.prodigy.com>`
- **References:** `<xt_nc.15863$V97.9345@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:xt_nc.15863$V97.9345@newsread1.news.pas.earthlink.net...
>
> IBM has posted a "cross-language" programming challenge that was brought
to my
> attention in the comp.lang.pli newsgroup.


Bill, since I haven't touched a COBOL program in about three years, I can't
really help you out, but I wanted to thank you for posting this.

My BASIC language on-line Peer Support forum at

http://www.powerbasic.com/support/forums/Ultimate.cgi

has long been besieged by posts of "do-nothing loop" programs which users
have thought are valid performance benchmark programs. I posted this info
there this AM. (I noticed in the language-specific notes provided BASIC was
treated as non-existent).

I think I'll get  good feedback and hopefully this will help some of the
newer BASIC-language programmers both understand what a valid performance
benchmark program is, and learn some interesting ways to approach real world
application challenges.
```

#### ↳ Re: "Odd" little programming challenge

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-05-11T18:46:27+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6142a0p2vochptg22jpms838v4369gvnra@4ax.com>`
- **References:** `<xt_nc.15863$V97.9345@newsread1.news.pas.earthlink.net>`

```
On Tue, 11 May 2004 06:34:05 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>to: comp.lang.cobol
>        and
…[31 more quoted lines elided]…
>specifications (i.e round to nearest even decimal point for ".xx5" results).
Bill,

Without any change to your program I am getting the correct values!!

FJ v7

  Time  Rate |        Price         Btax         Dtax |      Output   
-------------+----------------------------------------+-------------  
.....
.....
    35    D  |         0.31         0.02         0.01 |         0.34  
   193    D  |         1.73         0.11         0.05 |         1.89  
   792    L  |         1.03         0.06              |         1.09  
   661    D  |         5.91         0.39         0.20 |         6.50  
    44    L  |         0.06         0.00              |         0.06  
   262    L  |         0.34         0.02              |         0.36  
-------------+----------------------------------------+-------------  
   Totals:   |   922,067.11    57,628.30    25,042.17 | 1,004,737.58  


And from their web page

 For the 1,000,000-number file, exponential distribution with a mean
of 180 [infile=expon180.1e6 or infile=expon180.1e6b], the sum values
should be:

  sumT = 1004737.58
  sumB = 57628.30
  sumD = 25042.17
  

(In either case, if sumD is unexpectedly 0 then probably the BCD data
file is being used when the testcase expects the binary data file.)




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: "Odd" little programming challenge

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-11T21:13:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2mboc.16566$Hs1.9423@newsread2.news.pas.earthlink.net>`
- **References:** `<xt_nc.15863$V97.9345@newsread1.news.pas.earthlink.net> <6142a0p2vochptg22jpms838v4369gvnra@4ax.com>`

```
I found my problem and fixed it (and posted the corrected version on the web).
I hadn't checked enough decimal points in my original program.

I'll let "everyone know" once I add the "timing" logic.
```

###### ↳ ↳ ↳ Re: "Odd" little programming challenge

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-05-12T00:18:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n3l2a0dh1sb0bnehgpcqc77cmul34kjtg3@4ax.com>`
- **References:** `<xt_nc.15863$V97.9345@newsread1.news.pas.earthlink.net> <6142a0p2vochptg22jpms838v4369gvnra@4ax.com> <2mboc.16566$Hs1.9423@newsread2.news.pas.earthlink.net>`

```
On Tue, 11 May 2004 21:13:34 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>I found my problem and fixed it (and posted the corrected version on the web).
>I hadn't checked enough decimal points in my original program.
>
>I'll let "everyone know" once I add the "timing" logic.

Ah. That explains it.

My timings (3 run's)

Local machine (without timing for compute): 78.03s and 76.34s and
76.73s (rough avg = 77.03)

Local machine:
total time: 79.90s and 80.09s and 78.54s (rough avg = 79.51)
compute time: 21.89s and 21.80s and 21.46s (rough avg = 21.72)

This gives a % of 28.20 if we ignore the "timing impact" or of 27.31
if we count the timing.



Remote machine(without timing for compute): 96.34s and 97.08s and
94.91s (rough avg = 96.11)


Remote machine:
total time: 100.75s and 101.38s and 103.81s (rough avg = 101.98)
compute time: 22.83s and 21.59s and 23.01s (rough avg = 22.48)


This gives a % of 23.38 if we ignore the "timing impact" or of 22.04
if we count the timing.


Now we can't really compare my timings, as machines are not the same
spec, and HD speed is SCSI U160 on the network compared to SCSIU320 on
the local machine.

Enjoy




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
