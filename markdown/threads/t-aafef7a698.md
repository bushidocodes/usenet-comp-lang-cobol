[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS 4.1 HELP PLEASE

_9 messages · 7 participants · 1998-06 → 1998-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS 4.1 HELP PLEASE

- **From:** "don bailey" <ua-author-88128@usenetarchives.gap>
- **Date:** 1998-06-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3587C98D.E666AAC7@cslp.org>`

```

Hi People!
I running into problems with some of our CICS programs which ran fine
under CICS 2.1.2 but don't run correctly under CICS 4.1.0. 1st case:
CICS program sends map to the screen and parts of the program such as
working storage begins here displays on the screen instead of what is
supposed to show on the screen. Get various results of changing maps as
you continue to clear screen and type the transaction. When I run it
under CEDF and CECI, everything works correctly. But when it is run by
itself, I get weird stuff on the screen. Does anyone have some ideas
that would make this work correctly????

2nd Case, getting ASRD failure on another program. When we look at the
offset, it is a simple MOVE instruction. Something like Move Message-13
to Msgarea. I don't see any macro code or Address of CSA in the
program. This program was compiled using COBOL 1 (I know rather old)
but it still works correctly under CICS 2.1.2. Any Suggestions????

3rd Case. Once in a while I see the following messages:
+DFHSM0134 CICSTNEW CICS is no longer short on storage above 16MB.
+DFHSM0133 CICSTNEW CICS is under stress (short on storage above 16MB).
This then wipes out the WTO queue which is a problem because these
messages (approx 90 messages) happened at 14.03.26 not to mention all
the other ones that occured 14 seconds later and so on.
Is there any way to reduce the number of messages sent to the WTO?????
I 'm still trying to figure out what caused the shortage.

Thanks

Don Bailey
Extremely Frustrated over the above items :(
```

#### ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-06-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafef7a698-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3587C98D.E666AAC7@cslp.org>`
- **References:** `<3587C98D.E666AAC7@cslp.org>`

```

Is all of this OS/VS COBOL only? Is there any chance that you have changed
your run-time (not compiler) to LE or even VS COBOL II? The problems SOUND
like they have to do with compiler and run-time options of WSCLEAR (VS COBOL
II) or STORAGE(LE) - and NUMPROC. If you don't have any of the new stuff
running, then these can't be the issue, but it sure sounds like it. If you
DO have the new stuff running (compiler OR run-time), then let us know and
we can make specific suggestions related to these options and how they might
fit your problems.



Don Bailey wrote in message <358··.@cs··p.org>...
› Hi People!
›  I running into problems with some of our CICS programs which ran fine
…[28 more quoted lines elided]…
›
```

#### ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "rrp..." <ua-author-13513217@usenetarchives.gap>
- **Date:** 1998-06-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafef7a698-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3587C98D.E666AAC7@cslp.org>`
- **References:** `<3587C98D.E666AAC7@cslp.org>`

```

Just an FYI, but your problem might not be in the CICS product after
all; check your cobol compile options (for cobol/2 to cobol/le and
higher) and make sure you have the runtime option WSCLEAR set on.
```

#### ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "am" <ua-author-33177@usenetarchives.gap>
- **Date:** 1998-07-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafef7a698-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3587C98D.E666AAC7@cslp.org>`
- **References:** `<3587C98D.E666AAC7@cslp.org>`

```

Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
statement
to OS/VS Cobol. This has caused the short on storage above 16MB problem on
a
previous project I was involved.

AM
```

##### ↳ ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-07-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafef7a698-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aafef7a698-p4@usenetarchives.gap>`
- **References:** `<3587C98D.E666AAC7@cslp.org> <gap-aafef7a698-p4@usenetarchives.gap>`

```

AM wrote:
› 
› Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
…[5 more quoted lines elided]…
› AM

Short on storage *above* the line? I doubt it. OS/VS Cobol runs only
below the line.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net      mailto:Bar··.@att··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  MSMSMSMSMSMS 6/32/113
e    |\ Can you solve the BBA-CAB-DBB series?
Y    |/                 http://members.aol.com/PanicYr00/Sequence.html
o    |\ The Zeros Are Coming!         http://members.aol.com/PanicYr00
u    |/ The Zeros Are Coming!         http://members.aol.com/PanicYr00
```

###### ↳ ↳ ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "am" <ua-author-33177@usenetarchives.gap>
- **Date:** 1998-07-06T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafef7a698-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aafef7a698-p5@usenetarchives.gap>`
- **References:** `<3587C98D.E666AAC7@cslp.org> <gap-aafef7a698-p4@usenetarchives.gap> <gap-aafef7a698-p5@usenetarchives.gap>`

```
Yes OS/VS COBOL is below the line. and passing the working storages to an
above the line
program such as COBOL II was (one of) the cause(s) of the problem we had.
You cannot use a CALL
statement between OS/VS COBOL and higher COBOL versions (COBOL II / MVS
COBOL) in
a CICS environment.

RandallBart wrote in article
<6ns5l5$n.··.@bgt··t.net>...
| AM wrote:
| >
| > Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
| > statement
| > to OS/VS Cobol. This has caused the short on storage above 16MB problem
on
| > a
| > previous project I was involved.
…[15 more quoted lines elided]…
|
```

#### ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bda916$fb6fe170$c58c3398@us0071826>`
- **References:** `<3587C98D.E666AAC7@cslp.org>`

```

Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
statement 
to OS/VS Cobol. This has caused the short on storage above 16MB problem on
a
previous project I was involved. 

AM
```

##### ↳ ↳ Re: CICS 4.1 HELP PLEASE

- **From:** RandallBart <Barticus@att.spam.net>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ns5l5$nsh@bgtnsc03.worldnet.att.net>`
- **References:** `<3587C98D.E666AAC7@cslp.org> <01bda916$fb6fe170$c58c3398@us0071826>`

```

AM wrote:
> 
> Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
…[5 more quoted lines elided]…
> AM

Short on storage *above* the line?  I doubt it.  OS/VS Cobol runs only
below the line. 
```

###### ↳ ↳ ↳ Re: CICS 4.1 HELP PLEASE

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bda9b3$c1bfe220$c58c3398@us0071826>`
- **References:** `<3587C98D.E666AAC7@cslp.org> <01bda916$fb6fe170$c58c3398@us0071826> <6ns5l5$nsh@bgtnsc03.worldnet.att.net>`

```
Yes OS/VS COBOL is below the line. and passing the working storages to an
above the line
program such as COBOL II was (one of) the cause(s) of the problem we had.
You cannot use a CALL
statement between OS/VS COBOL and higher COBOL versions (COBOL II / MVS
COBOL) in
a CICS environment.

RandallBart <Barticus@att.spam.net> wrote in article
<6ns5l5$nsh@bgtnsc03.worldnet.att.net>...
| AM wrote:
| > 
| > Are you using any COBOL II/CICS? COBOL II/CICS cannot use the CALL
| > statement
| > to OS/VS Cobol. This has caused the short on storage above 16MB problem
on
| > a
| > previous project I was involved.
…[15 more quoted lines elided]…
|
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
