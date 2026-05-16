[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LE, COBOL, CICS, Y2K and related topics

_2 messages · 2 participants · 1999-01_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### LE, COBOL, CICS, Y2K and related topics

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000.tech
- **Message-ID:** `<76uhv6$2ga@sjx-ixn5.ix.netcom.com>`

```
FYI, (aimed particularly at IBM mainframers)
  I just put out the following in the IBM-MAIN newsgroup(list-server)

    *****

At the end of last year (1998) there was a thread that started out
concerning LE 40xx ABEND codes.  It got a lot of "recommendations" - some of
which I agree with and some I don't.  I just thought that I would put out MY
(not IBM's) recommendations - and see how much attacking I get. (Most of
this is common sense, already well known, or familiar to many readers of
IBM-MAIN - but given some of the comments that I read last month, I thought
I would put out this summary anyway.)

1) If you have lots of OS/VS COBOL programs running in production and
haven't moved to LE (or OS/390) yet (probably don't even have a Y2K plan in
effect yet), please do NOT try to "jump" to IBM COBOL for OS/390 & VM (with
or without MLE) and LE quickly.  Especially, do NOT recompile (or even
re-link) existing COBOL programs that are running just fine in production
now. (unless you know they need specific Y2K remediation). DO plan on
upgrading your run-time environment long (or as long as you have now) before
you upgrade your compilers.

2) If you have existing OS/VS COBOL or VS COBOL II *nores* applications
running in production now and they (and their subprograms) do not have
specific Y2K problems, don't change, recompile, or re-link them either.

3) If you are using the VS COBOL II *MIXRES* option, plan on a lot of
research to move to a reliable environment (whether or not your programs are
Y2K compliant).  If you are running with RES, then with a lot of prayer and
as much testing as possible, your applications SHOULD move to LE with
minimal difficulty (and need not be recompiled - unless you have specific
Y2K changes required).

4) If you can (i.e. you have already done some LEARNING, planning, and
testing) do try and get to an LE run-time environment.  This means LE (and
*NO* other libraries - no concatenation) in your Linklist.  Clearly this is
what OS/390 (all releases) thinks is "optimal" and this will be the "nicest"
(cleanest?) environment for everything else.

5) You can run with LE in the Linklist and Steplib to VS COBOL II or run
with VS COBOL II in the Linklist and (for most - but not all applications)
run with LE steplibed.  This works OK, you only get in trouble when try
concatenating the two libraries either in a steplib or a Linklist.  (P.S.
Do understand the order for CICS run-time libraries as they related to the
"common" run-time libraries.  This is true for both LE and VS COBOL II
run-times)

6) If you have one release of LE and are looking at (particularly for
OS/390 - especially TCP/IP -reasons) needing another release of LE
available, do look at RTLS (documented in the current LE manuals).  It isn't
perfect but it is better than nothing (which - by the way is what you have
under CICS - where RTLS isn't working).

7) Whether you are looking at in-house or contracted services, don't let
ANYONE tell you that you must recompile ALL *cobol* programs (no matter how
down-level they are).

8) Do look at the Edge Portfolio product if you are just now beginning (or
even in the middle) of working on Y2K remediation.  You may well be
surprised at what you have (and don't have) running in production.
(Normally, I would say "Edge or any other comparable product" - but I don't
know of any that are comparable.)

9) If you haven't started moving all your Y2K applications into production
yet, please, PLEASE, at least check out the lists of Y2K compliant "vendor"
products.  You have got to be on the right levels of CICS, DB2, IMS,
DFSort/SyncSort, Abend-Aid, etc, ETC - or it won't matter how much
"application remediation" you have done.  By the way, did I mention a Y2K
compliant OS running on hardware that works for Y2K?

10) Get as much training as you need and/or get contracted support in house
(AND training to take over when they leave).  LE is NOT easy.  Newer
releases of COBOL, CICS, and DB2 are NOT easy.  Just because the
installation IVP works, doesn't mean that your production will run (possibly
not even walk).

  *****

Bottom-Line: (IMHO)

If you still have OS/VS COBOL production programs and are not well along on
your Y2K remediation, there are two equally reliable solutions available to
you:

A) Pray a WHOLE lot

B) Concentrate on inventing a time-machine so you can go back 5 to 10
years - so your company will start working on these when they should have!
```

#### ↳ Re: LE, COBOL, CICS, Y2K and related topics

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1999-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000.tech
- **Message-ID:** `<3693a26d.16173876@news.teo-computer.com>`
- **References:** `<76uhv6$2ga@sjx-ixn5.ix.netcom.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>FYI, (aimed particularly at IBM mainframers)
>  I just put out the following in the IBM-MAIN newsgroup(list-server)
…[88 more quoted lines elided]…
>


Arnold Trembley has an excellent set of pages devoted to Y2k "Time
Machine" testing for LE, CICS, MVS, COBOL and Assembler at:

http://home.att.net/~arnold.trembley/tmr.htm




Tim Oxler
TEO Computer Technologies Inc.
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
