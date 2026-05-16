[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ansi-74 and Ansi-85

_9 messages · 8 participants · 1998-11_

---

### Ansi-74 and Ansi-85

- **From:** "murkesm" <murkesm@convertis.nl>
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<729r30$opo@news3.euro.net>`

```
Hiya,
does somebody has a comprehensive listing of the differences between ANSI-74
and ANSI-85 Cobol?
Mark
```

#### ↳ Re: Ansi-74 and Ansi-85

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3648806F.31AC@compaq.com>`
- **References:** `<729r30$opo@news3.euro.net>`

```
murkesm wrote:
> 
> Hiya,
> does somebody has a comprehensive listing of the differences between ANSI-74
> and ANSI-85 Cobol?
> Mark

The last chapter of my book, COBOL 85 for Programmers (available from 
me for ten bucks), has such a list.  In fact, that is what the whole 
book is about.  There is also a list in the standard, but from other 
posts it is obviously difficult to obtain.
```

##### ↳ ↳ Re: Ansi-74 and Ansi-85

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-WKdoC0LxqBxW@Dwight_Miller.iix.com>`
- **References:** `<729r30$opo@news3.euro.net> <3648806F.31AC@compaq.com>`

```
On Tue, 10 Nov 1998 17:57:14, Don Nelson <don.nelson@compaq.com> 
wrote:

> murkesm wrote:
> > 
…[8 more quoted lines elided]…
> posts it is obviously difficult to obtain.


Send Don the ten bucks.  One of the best investments I ever made.
```

###### ↳ ↳ ↳ Re: Ansi-74 and Ansi-85

- **From:** kownby@humboldt1.com (Kindrick Ownby)
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3648cc63.19437573@news2.humboldt1.com>`
- **References:** `<729r30$opo@news3.euro.net> <3648806F.31AC@compaq.com> <Jl0PnHJ5PvPd-pn2-WKdoC0LxqBxW@Dwight_Miller.iix.com>`

```
On 10 Nov 98 22:40:36 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>On Tue, 10 Nov 1998 17:57:14, Don Nelson <don.nelson@compaq.com> 
>wrote:
…[15 more quoted lines elided]…
>

Ditto!
```

#### ↳ Re: Ansi-74 and Ansi-85

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3649ad8a.11526321@news.teo-computer.com>`
- **References:** `<729r30$opo@news3.euro.net>`

```
"murkesm" <murkesm@convertis.nl> wrote:

>Hiya,
>does somebody has a comprehensive listing of the differences between ANSI-74
…[4 more quoted lines elided]…
>
I have a list of difference between IBM COBOL '74 and COBOL II, if
that's what you're looking for:

Heres the list of dropped verbs:

Identification Division
        Remarks (use * or / in column 7)

Environment Division
        Processing mode clause

Procedure Division
        READY TRACE
        NOTE
        EXHIBIT (use DISPLAY)
        EXAMINE (use INSPECT)
        CURRENT-DATE (use ACCEPT WS-DATE FROM DATE)
        TIME-OF-DAY (use ACCEPT WS-TIME FROM TIME)
        TRANSFORM (use INSPECT)
        ON statement (use IF...ELSE or EVALUATE)
        Write after/before positioning (use just 'WRITE' , drop
positioning.



Additions in Cobol II

Scope terminators for verbs:
        END-ADD, END-CALL, END-COMPUTE, END-DIVIDE, END-EVALUATE,
END-IF, END-MULTIPLY, END-PERFORM, END-READ, END-SEARCH

CONTINUE verb use instead of NEXT SENTENCE
        NEXT SENTENCE means go to next period
        CONTINUE means go to the next scope terminator

INITIALIZE
        Will whole copybooks and fields with cascading levels to
spaces or numerics depending on PIC value.

EVALUATE
        Uses case structure to replace the use of massive
IF...ELSE...IF....ELSE statements.

There is more, and variations of the above additions and deletions,
along with a few feature changes, and a few inconsistencies between
Cobol and Cobol II, but this will get you going.



Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

##### ↳ ↳ Re: Ansi-74 and Ansi-85

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3649BD81.EE85F58A@home.com>`
- **References:** `<729r30$opo@news3.euro.net> <3649ad8a.11526321@news.teo-computer.com>`

```
>         EXAMINE (use INSPECT)
>         TRANSFORM (use INSPECT)

EXAMINE went away between ANSI 68 and ANSI 72.  At the time, I worked in
a shop which had both types of programs, so I replaced EXAMINE, where
possible, with TRANSFORM so that it would always work.  Of course, now
somebody is replacing my TRANSFORM which no longer works!!
```

###### ↳ ↳ ↳ Re: Ansi-74 and Ansi-85

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1998-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364b3a8c.21317066@news.teo-computer.com>`
- **References:** `<729r30$opo@news3.euro.net> <3649ad8a.11526321@news.teo-computer.com> <3649BD81.EE85F58A@home.com>`

```
Howard Brazee <NOSPAMbrazee@home.com> wrote:

>>         EXAMINE (use INSPECT)
>>         TRANSFORM (use INSPECT)
…[4 more quoted lines elided]…
>somebody is replacing my TRANSFORM which no longer works!!

I don't think that is true with the IBM version of COBOL.  I still
remember running into EXAMINE at a shop a few years ago, running IBM
COBOL 74.

Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

###### ↳ ↳ ↳ Re: Ansi-74 and Ansi-85

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981112174115.24584.00000711@ng150.aol.com>`
- **References:** `<364b3a8c.21317066@news.teo-computer.com>`

```
tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
Date: 12 Nov 1998 11:45:48 PST

quotes
>>>

 Howard Brazee <NOSPAMbrazee@home.com> wrote:

>>         EXAMINE (use INSPECT)
>>         TRANSFORM (use INSPECT)
…[4 more quoted lines elided]…
>somebody is replacing my TRANSFORM which no longer works!!
<<<

tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
then comments 
>>>
I don't think that is true with the IBM version of COBOL.  I still
remember running into EXAMINE at a shop a few years ago, running IBM
COBOL 74.
<<<

This involves an expensive subtlety.  When moving to COBOL for MVS (or COBOL
for OS/390), shops not only need to convert COBOL 74 syntax to COBOL 85, but
they loose any further support for a list of IBM extensions that were covered
in earlier compilers (COBOL II) but are gone now.

That is a gotcha.  INSPECT is the only viable verb for the text manipulations
contemplated.

IBM is not to be faulted, they actually stretched old syntax really far over
time. But for some things, time's up. The check list of things to do for COBOL
for OS/390 involves more than the COBOL 74 / COBOL 85 differences. It is best
to discover this surprise in the early resource planning phase.

Both posters are right. In a certain sense it may have been better to drop
EXAMINE syntax earlier, considering current skyrocketting labor costs.  But
should we really complain if folks are just a little short-sighted?!

It's like windowing instead of expanding; you can pay me now, or you can pay me
now and later. 

Be happy! Soon we will be examining source modules to find opportunities to
transform all text manipulations to COBOL FUNCTION invocations of super-duper
Language Environment C string processing routines. And we know that that will
standardize the heck out it all.





Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Ansi-74 and Ansi-85

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72cg7e$dj2@sjx-ixn9.ix.netcom.com>`
- **References:** `<729r30$opo@news3.euro.net>`

```

murkesm wrote in message <729r30$opo@news3.euro.net>...
>Hiya,
>does somebody has a comprehensive listing of the differences between
ANSI-74
>and ANSI-85 Cobol?
>Mark
>
>


Do you really want to know the differences in the Standard - or do you want
to know the differences between two implementations or options?  One person
responded with some information about IBM's products - but (as may or may
not be clear from that list) the Standard differences are only a VERY MINOR
part of the differences between OS/VS COBOL with LANGLVL(2) and VS COBOL II
(or COBOL for this-and-that) with NOCMPR2.

Don's book is great for the Standard differences, but if you want to know
about any "implementation" differences, you will need to let us know what
products (and compiler options) you are actually trying to compare.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
