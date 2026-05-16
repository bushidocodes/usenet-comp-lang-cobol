[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Perform...Until question

_13 messages · 11 participants · 1999-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Perform...Until question

- **From:** rwaltei1@nycap.rr.ocm (Rich)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369e8eff.4900536@news.nycap.rr.com>`

```

When using a perform until, does it perform first, then check the
condition? like a Do..while construct. Or does it check first.

I looked in two books and found they contradicted themselves.

I know that there is a 'with test before' and a 'with test after' but
what is the default when these clauses arent used.

Thanks.
```

#### ↳ Re: Perform...Until question

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77m6c7$k4k$1@juliana.sprynet.com>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
Using the default of 'test before' it's really a DO WHILE, similar to the DO
WHILE construct in PL/I. This means that it's tested at the top and may not
execute at all. However, using the 'test after' guarantees that it will be
executed at least once, which may or may not be desirable.

HTH....

Cheers,

WOB

Rich wrote in message <369e8eff.4900536@news.nycap.rr.com>...
>
>When using a perform until, does it perform first, then check the
>condition? like a Do..while construct. Or does it check first.


<Rest Snipped>
```

#### ↳ Re: Perform...Until question

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77mbku$bap$1@news.igs.net>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
Cobol checks before. It is possible that the
perform never gets done.

Rich wrote in message <369e8eff.4900536@news.nycap.rr.com>...
>
>When using a perform until, does it perform first, then check the
…[7 more quoted lines elided]…
>Thanks.
```

#### ↳ Re: Perform...Until question

- **From:** "Gary Roush" <support@adtools.com>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77ov1c$np2$1@remarQ.com>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
'test before' is the default in all cases. There may be some that do a run
through any way the first time, but that's a baddie.  In all cases, the
Until clause is what determines whether to execute the perform or not and
when it is to end.  The 'test after' always ensures the perform runs at
least once before it is checked.

Gary
```

#### ↳ Re: Perform...Until question

- **From:** "Rob Annandale" <rob_aNOSPAM@unipharm.com>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369f6655$0$26980@fountain.mindlink.net>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
You can stipulate when you want the perform to check the condition.
e.g.

perform test after varying xx from 1 by 1 until...

or

perform test before varying xx from 1 by 1 until...

AcuCobol-85.

Rob Annandale


Rich wrote in message <369e8eff.4900536@news.nycap.rr.com>...
>
>When using a perform until, does it perform first, then check the
…[7 more quoted lines elided]…
>Thanks.
```

#### ↳ Re: Perform...Until question

- **From:** jraben19@mail.idt.net (Jeff Raben)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369fc89c.2281139@news.idt.net>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
rwaltei1@nycap.rr.ocm (Rich) wrote:

>
>When using a perform until, does it perform first, then check the
…[7 more quoted lines elided]…
>Thanks.
Most cobols default to test before except.... often they do the first
iteration regardless.  NUTS.

JR
and stir with a Runcible spoon...
```

#### ↳ Re: Perform...Until question

- **From:** bbello5778@aol.com (BBello5778)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990114195712.00905.00000247@ng27.aol.com>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
you wrote....

H>When using a perform until, does it perform first, then check the
>condition? like a Do..while construct. Or does it check first.
>
…[4 more quoted lines elided]…
>

Hi, the default is' with test before'. i.e. it does the check first. 

good luck

Bosun

BBello5778@aol.com 
http://members.aol.com/bbello5778/bosun.htm
Programmer/Analyst. Bloomington, IL
```

#### ↳ Re: Perform...Until question

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990114212703.00908.00000321@ng26.aol.com>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```


When using a perform until, does it perform first, then check the
condition? It is absolutely true..
```

#### ↳ Re: Perform...Until question

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369ec41b.7224583@news1.ibm.net>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
On Fri, 15 Jan 1999 00:44:47 GMT, rwaltei1@nycap.rr.ocm (Rich) wrote:

>
>When using a perform until, does it perform first, then check the
…[5 more quoted lines elided]…
>what is the default when these clauses arent used.

I'm a bit froggy tonight after staying at work a few extra hours
optimizing some VSAM stuff....

But I cover this in my book!  Pp 171-172 <G>.

(Sams Teach Yourself COBOL in 24 Hours)
```

##### ↳ ↳ Re: Perform...Until question

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A4DC12.ED33490@IMN.nl>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com> <369ec41b.7224583@news1.ibm.net>`

```
Thane Hubbell wrote:
8<

> I'm a bit froggy tonight ...

Join the club of Frogs!

> ... after staying at work a few extra hours
> optimizing some VSAM stuff....

Bweh

> But I cover this in my book!  Pp 171-172 <G>.

VSAM? :)

> (Sams Teach Yourself COBOL in 24 Hours)

That Frog
```

#### ↳ Re: Perform...Until question

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rzAn2.3275$hE2.20710465@storm.twcol.com>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
>When using a perform until, does it perform first, then check the
>condition? like a Do..while construct. Or does it check first.


When in doubt run a test. Books only tell syntax and what the author is
thinking about at the time. I always find it better to run a test, if time
allows.


       MOVE 'NOT FINISHED' TO WS-INDICATOR
       DISPLAY 'INDICATOR SAYS : ' WS-INDICATOR
       IF WS-INDICATOR = 'FINISHED    ' THEN
          DISPLAY 'LOOP SHOULD NOT BE EXECUTED.'
       END-IF
******* THIS LOOP WILL BE EXECUTED
       PERFORM UNTIL WS-INDICATOR = 'FINISHED    '
          ADD 1 TO WS-COUNTER
          DISPLAY 'LOOP COUNT ' WS-INDICATOR
          IF WS-COUNTER > 5 THEN
             MOVE 'FINISHED    ' TO WS-INDICATOR
          END-IF
       END-PERFORMOVE 'NOT FINISHED' TO WS-INDICATOR

       DISPLAY 'INDICATOR SAYS : ' WS-INDICATOR
       IF WS-INDICATOR = 'FINISHED    ' THEN
          DISPLAY 'LOOP SHOULD NOT BE EXECUTED.'
       END-IF
******* THIS LOOP WILL NOT BE EXECUTED
       PERFORM UNTIL WS-INDICATOR = 'FINISHED    '
          ADD 1 TO WS-COUNTER
          DISPLAY 'LOOP COUNT ' WS-INDICATOR
          IF WS-COUNTER > 5 THEN
             MOVE 'FINISHED    ' TO WS-INDICATOR
          END-IF
       END-PERFORMM
```

##### ↳ ↳ Re: Perform...Until question

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A4DCE1.10EA04@IMN.nl>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com> <rzAn2.3275$hE2.20710465@storm.twcol.com>`

```
Jeff wrote:

> >When using a perform until, does it perform first, then check the
> >condition? like a Do..while construct. Or does it check first.
…[3 more quoted lines elided]…
> allows. (8< Example)

Thus revealing what syntax and semantics the author of the particular compiler
is thinking about at the time. But when it is the compiler it is to be used,
such a test gives indeed useful information.

TTBSF









Trying To Be Smart Frog
```

#### ↳ Re: Perform...Until question

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A4E1A6.A2A5D670@IMN.nl>`
- **References:** `<369e8eff.4900536@news.nycap.rr.com>`

```
Rich wrote:

> When using a perform until, does it perform first, then check the
> condition? like a Do..while construct. Or does it check first.

1) As others pointed out, it checks first, in COBOL.
2) This is to ensure compatibility with earlier COBOL standards (COBOL
'74, '68 etbackera). There was no option "AFTER/BEFORE", but an explicit
definition of being tested "before" in the LRM.
3) But "perform first, then check" is not always "like a Do..while
construct"! The exact behaviour of a "while construct" or "until
construct" is language dependent:
In PL/1: while tests before (terminating when false), until tests after
(terminating when true)
In COBOL: while does not exist, until test before or after depending on
these words (both terminating when true)
In C/C++: while tests before or after, depending on statement, i.e.
while-statement or do..while-statement (both terminating when false).
In Pascal it is like in PL/1. (N. Wirth called PL/1 the second best
constructed comp.lang)!

I think you meant a do-while-construct from C(C++), but as a former PL/1
and C++ programmer I know this to be notoriously misunderstood / mixed
up.

> I looked in two books and found they contradicted themselves.

Then one of them is at fault. Which were they, which one said "after"?

> I know that there is a 'with test before' and a 'with test after' but
> what is the default when these clauses arent used.

I like it as good habit to always specify BEFORE of AFTER in new programs
(don't touch old code when it works).

> Thanks.

You're welcome

The Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
