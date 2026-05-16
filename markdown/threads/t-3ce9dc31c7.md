[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus COBOL vs. Mainframe COBOL II

_7 messages · 1 participant · 2000-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MicroFocus COBOL vs. Mainframe COBOL II

- **From:** "Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spjbspsvkn9106@corp.supernews.com>`

```
Before I post an example...

Does anyone have an example of  identical COBOL code yielding different
results when compiled and run on a mainframe computer (COBOL II) as opposed
to running on a PC in MicroFocus COBOL ?

LD
```

#### ↳ Re: MicroFocus COBOL vs. Mainframe COBOL II

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ncffo$2c8$1@slb7.atl.mindspring.net>`
- **References:** `<spjbspsvkn9106@corp.supernews.com>`

```
If you are looking for such things, you will need to include a COMPLETE list
of what directives you are using (or "promise" that you are using all the
directives suggested in the MERANT Mainframe Programmer's Guide).  It is
*easy* to show different results if you don't use the directives that MERANT
recommends.  Also, if you are looking for such examples, it will (probably)
depend upon whether or not your are emulating SUPPORTED behavior on the IBM
Mainframe.  There are lots of things that the VS COBOL II compiler
does/allows that are explicitly "unsupported" by IBM.

Having said all of this, if your desire is for the most compatible compiler
(not necessarily run-time results), there is no question that IBM's own
VisualAge COBOL product is "closer" to the mainframe compiler - because it is
the SAME "front-end" as the current/strategic IBM product "IBM COBOL for
OS/390 & VM" (which is a LOT more recent than VS COBOL II).
```

##### ↳ ↳ Re: MicroFocus COBOL vs. Mainframe COBOL II

- **From:** "Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spjnd6ngr5j67@corp.supernews.com>`
- **References:** `<spjbspsvkn9106@corp.supernews.com> <8ncffo$2c8$1@slb7.atl.mindspring.net>`

```
Well, there is much truth to what you say.  No, I am not looking for a
compiler. Yes, I realize that there are many versions/levels of compilers
running in MF shops in the industry.  According to what I've read (and once
tested), the issue had less to do with compiler options (yes, I recognize
that sounds "inexperienced") and more to do with how compilers manage
storage on dissimilar platforms.

So, what exactly was my purpose for the post?  It appears that this forum is
not overly active. So, considering the number of posts that were generated
from my earlier post (yesterday), "Interesting Date Routine", I thought I
would try to generate some more chatter... get a few more ideas (juices)
flowing.

As for the example I made reference to in my original post, I have it in a
paper file somewhere (pre-dates the paper-less office) and I plan to dig it
up soon.  My recollection is that it was from an article in a trade
publication.... and I'll be darned if I can recall which one.... but I will.

Thanks for you thoughtful response....
LD

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8ncffo$2c8$1@slb7.atl.mindspring.net...
> If you are looking for such things, you will need to include a COMPLETE
list
> of what directives you are using (or "promise" that you are using all the
> directives suggested in the MERANT Mainframe Programmer's Guide).  It is
> *easy* to show different results if you don't use the directives that
MERANT
> recommends.  Also, if you are looking for such examples, it will
(probably)
> depend upon whether or not your are emulating SUPPORTED behavior on the
IBM
> Mainframe.  There are lots of things that the VS COBOL II compiler
> does/allows that are explicitly "unsupported" by IBM.
>
> Having said all of this, if your desire is for the most compatible
compiler
> (not necessarily run-time results), there is no question that IBM's own
> VisualAge COBOL product is "closer" to the mainframe compiler - because it
is
> the SAME "front-end" as the current/strategic IBM product "IBM COBOL for
> OS/390 & VM" (which is a LOT more recent than VS COBOL II).
…[9 more quoted lines elided]…
> > results when compiled and run on a mainframe computer (COBOL II) as
opposed
> > to running on a PC in MicroFocus COBOL ?
> >
…[4 more quoted lines elided]…
>
```

#### ↳ Re: MicroFocus COBOL vs. Mainframe COBOL II [Part 1]

- **From:** "Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com>
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spm7k6ssr5j114@corp.supernews.com>`
- **References:** `<spjbspsvkn9106@corp.supernews.com>`

```
The following text was extracted from a publication, "Enterprise Systems
Journal", dated September, 1993, and titled, "COBOL COMPUTE Can Bite You" by
Jim Janossy of DePaul University.  I have reproduced only the first column
of the first page to see if it is of interest to anyone.  I will take the
time to post more if interest exists.

*****     Beginning of Text     ******

A chemistry professor, without a word, entered a lecture hall one Monday
morning, filled a large balloon with hydrogen and let it hover above the
podium on a string. He then held a lighted Bunsen burner under it. The
resulting explosion reverberated throughout the hall and shook loose some
ceiling tiles (and sleeping hulks). It was his way of demonstrating that
some chemical reactions proceed rapidly. Obviously, it caught the audience's
attention, starting the lecture with a bang.

AMOCO Corp. is in the chemicals business and runs one of the larger IS
organizations in the United States. A course was built for its training
division to acclimate programmers to the world of VS COBOL 11 and capture
audience interest with a bang. The [partial] program in Example #1, an
innocent looking routine that divides 248 by 1000 and computes a percentage
accomplished the course's goals.

Example #1:

WORKING-STORAGE SECTION.
01  WS-RECORDS-WITH-ERROR           PIC 9(4)   VALUE 248.
01  WS-TOTAL-RECORDS                       PIC 9(4)   VALUE 1000.
01  WS-HIGH-PRECISION-RESULT        PIC 9(3)V9999.
01  WS-ERROR-PERCENTAGE                PIC  9(3)V9.
01  OUTPUT-LINE.
    05  OL-RECORDS-WITH-ERROR        PIC 9999.
    05  FILLER                                              PIC X(7) VALUE
SPACES.
    05  OL-TOTAL-RECORDS                    PIC 9999.
    05  FILLER                                              PIC X(7) VALUE
SPACES.
    05  OL-ERROR-PERCENTAGE             PIC ZZ9.99.

PROCEDURE DIVISION.
0000-MAINLINE.
         DISPLAY 'PROGRAM G2MATH STARTING'
         DISPLAY 'ERR TOTAL  Err/Total %'
         COMPUTE WS-HIGH-PRECISION-RESULT =
                  (WS-RECORDS-WITH-ERROR / WS-TOTAL-RECORDS) * 100
         COMPUTE ERROR-PERCENTAGE  ROUNDED =
                   WS-HIGH-PRECISION-RESULT
         MOVE WS-RECORDS-WITH-ERROR TO OL-RECORDS-WITH-ERROR
         MOVE WS-TOTAL-RECORDS  TO OL-TOTAL-RECORDS
         MOVE WS-ERROR-PERCENTAGE TO OL-ERROR-PERCENTAGE
         DISPLAY OUTPUT-LINE.
         STOP RUN.

The bang occurs when you run this program under VS COBOL or VS COBOL II as
the following results show. Instead of 24.8 being the answer, it is 20.0.
With adequate unit testing, you could detect this problem and eventually
determine why it occurs: IBM's COBOL compilers are stingy with the size of
intermediate fields.

The result, when compiled and run under VS COBOL II is not accurate:
        PROGRAM G2MATH STARTING
        ERR      TOTAL      Err/Total %
        0248      1000          20.00

The result, when compiled and run under Micro Focus COBOL, gives the correct
result:
        PROGRAM G2MATH STARTING
        ERR      TOTAL      Err/Total %
        0248      1000          24.80

The result, when compiled and run under Ryan McFarland RM/COBOL-85, gives
the correct result:
        PROGRAM G2MATH STARTING
        ERR      TOTAL      Err/Total %
        0248      1000          24.80


*****     End of Text     ******



Lincoln Duncan <NotOnSite*NOSPAM*@Yahoo.com> wrote in message
news:spjbspsvkn9106@corp.supernews.com...
> Before I post an example...
>
> Does anyone have an example of  identical COBOL code yielding different
> results when compiled and run on a mainframe computer (COBOL II) as
opposed
> to running on a PC in MicroFocus COBOL ?
>
> LD
>
```

##### ↳ ↳ Re: MicroFocus COBOL vs. Mainframe COBOL II [Part 1]

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nfbh3$d6q$1@slb0.atl.mindspring.net>`
- **References:** `<spjbspsvkn9106@corp.supernews.com> <spm7k6ssr5j114@corp.supernews.com>`

```
Gee,
  That is EXACTLY why Micro Focus (MERANT) offers the "ARITHMETIC" directive.
The "default" is to provide the more "accurate" answer - however, with
    ARITHMETIC(IBM)
specified, you will get the same results as on the mainframe.

This "issue" is fully discussed in the MERANT "Mainframe Programmer's Guide"

(I know that, because I wrote it - when I still worked for Micro Focus).

The CLASSIC (easier to see) example is:

 05 Num7  Pic 9  Value 7.
 05 Num4  Pic 9  Value 4.
 05 NumResult  Pic 9 Value Zero.
         ...
  Compute NumResult = (Num7 / Num4) * Num4
  Evaluate NumResult
     When Num7
          Display "What you expect and MERANT gives by default"
      When Num4
          Display "You have GOT to be kidding, IBM"
       When Other
          Display "some other vendor's COMPUTE value"
   End-Evaluate

It is NOT true that IBM is "stingy" with intermediate results.  There are
ALSO examples where they give a MORE precise value that MERANT.  However,
their rules are a little "strange" in some cases.
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL vs. Mainframe COBOL II [Part 1]

- **From:** "Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com>
- **Date:** 2000-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spndo2lkr5j117@corp.supernews.com>`
- **References:** `<spjbspsvkn9106@corp.supernews.com> <spm7k6ssr5j114@corp.supernews.com> <8nfbh3$d6q$1@slb0.atl.mindspring.net>`

```
So, I'll take that as a NO....   as in, there is *NO* interest in any
further text from the article.

LD

PS.  How can I get a copy of the MERANT "Mainframe Programmer's Guide"?



William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8nfbh3$d6q$1@slb0.atl.mindspring.net...
> Gee,
>   That is EXACTLY why Micro Focus (MERANT) offers the "ARITHMETIC"
directive.
> The "default" is to provide the more "accurate" answer - however, with
>     ARITHMETIC(IBM)
> specified, you will get the same results as on the mainframe.
>
> This "issue" is fully discussed in the MERANT "Mainframe Programmer's
Guide"
>
> (I know that, because I wrote it - when I still worked for Micro Focus).
…[27 more quoted lines elided]…
> > Journal", dated September, 1993, and titled, "COBOL COMPUTE Can Bite
You"
> by
> > Jim Janossy of DePaul University.  I have reproduced only the first
column
> > of the first page to see if it is of interest to anyone.  I will take
the
> > time to post more if interest exists.
> >
…[5 more quoted lines elided]…
> > resulting explosion reverberated throughout the hall and shook loose
some
> > ceiling tiles (and sleeping hulks). It was his way of demonstrating that
> > some chemical reactions proceed rapidly. Obviously, it caught the
…[5 more quoted lines elided]…
> > division to acclimate programmers to the world of VS COBOL 11 and
capture
> > audience interest with a bang. The [partial] program in Example #1, an
> > innocent looking routine that divides 248 by 1000 and computes a
percentage
> > accomplished the course's goals.
> >
…[9 more quoted lines elided]…
> >     05  FILLER                                              PIC X(7)
VALUE
> > SPACES.
> >     05  OL-TOTAL-RECORDS                    PIC 9999.
> >     05  FILLER                                              PIC X(7)
VALUE
> > SPACES.
> >     05  OL-ERROR-PERCENTAGE             PIC ZZ9.99.
…[15 more quoted lines elided]…
> > The bang occurs when you run this program under VS COBOL or VS COBOL II
as
> > the following results show. Instead of 24.8 being the answer, it is
20.0.
> > With adequate unit testing, you could detect this problem and eventually
> > determine why it occurs: IBM's COBOL compilers are stingy with the size
of
> > intermediate fields.
> >
…[12 more quoted lines elided]…
> > The result, when compiled and run under Ryan McFarland RM/COBOL-85,
gives
> > the correct result:
> >         PROGRAM G2MATH STARTING
…[12 more quoted lines elided]…
> > > Does anyone have an example of  identical COBOL code yielding
different
> > > results when compiled and run on a mainframe computer (COBOL II) as
> > opposed
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL vs. Mainframe COBOL II [Part 1]

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ngmm5$v47$1@slb6.atl.mindspring.net>`
- **References:** `<spjbspsvkn9106@corp.supernews.com> <spm7k6ssr5j114@corp.supernews.com> <8nfbh3$d6q$1@slb0.atl.mindspring.net> <spndo2lkr5j117@corp.supernews.com>`

```
Hum, er, ....
  You can get the manual by checking your current licensed program "manual
set"???

If you don't have a set of MERANT manuals, you can try contacting MERANT to
see if you can purchase this manual "separately".  (It is PROBABLY a part of
the Mainframe Express product these days.)  I know that they have moved more
and more to "online documentation" - so I don't know how easy it will be to
get this specific manual.

FYI,
  There is an entire chapter on things like the "compute example" where you
can get different compile or run-time results - if you don't use the correct
directives and/or run-time switches.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
