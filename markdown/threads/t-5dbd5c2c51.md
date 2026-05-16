[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New Jersey's Woes - An Example

_42 messages · 22 participants · 1999-03_

---

### New Jersey's Woes - An Example

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7d91j7$j1s$1@callisto.clark.net>`

```


So I get an email from a buddy o' mine... 'Hey, what's up with this New
Jersey screwup, how did a simple Y2K patch make the checks go out early?'
I sat at the keyboard and I coded up the following which I offer, gratis,
to those who might need such a thing.  Systems-programmers, bare-metal
coders, folks who design compilers and the like may sneer at the quaint
COBOL which follows... but like it or not, this, or something quite like
it, is running on the Jersey Iron.

-- begin quote of myself:

Could be... consider the following two bits of code:

MOVE MFCS-CUST-NO-01 TO WS-CUSTNO.
IF INDEPENDENT-CUSTOMER
    PERFORM A53102-ALLOCATE-LOT THRU A53102-EXIT
    PERFORM C88092-CALC-CUBES   THRU C88092-EXIT
    PERFORM E35702-FIND-SHPWGHT THRU E35702-EXIT
    INSPECT WS-CUSTNO TALLYING WS-PERFORM-SUB FOR ALL 'QZ'
    IF WS-PERFORM-SUB > 0 AND WS-DT-REC-ADDED < WS-CUTOFF
        MOVE 'Y'  TO SPECL-CUST-FLAG
        PERFORM B28095-PROCESS-SPECUST THRU B28095-EXIT
         VARYING SUB1 FROM WS-PERFORM-SUB BY 1
          UNTIL SUB1 > WS-PERFORM-SUB
    END-IF
END-IF.

MOVE MFCS-CUST-NO-01 TO WS-CUSTNO.
IF INDEPENDENT-CUSTOMER
    PERFORM A53102-ALLOCATE-LOT THRU A53102-EXIT
    PERFORM C88092-CALC-CUBES   THRU C88092-EXIT
    PERFORM E35702-FIND-SHPWGHT THRU E35702-EXIT
    INSPECT WS-CUSTNO TALLYING WS-PERFORM-SUB FOR ALL 'QZ'
    IF WS-DT-REC-ADDED-YY < 40
        MOVE 20 TO WS-DT-REC-ADDED-CC
    ELSE
        MOVE 19 TO WS-DT-REC-ADDED-CC
    END-IF
    IF WS-CUTOFF-YY < 40
        MOVE 20 TO WS-CUTOFF-CC
    ELSE
        MOVE 19 TO WS-CUTOFF-CC
    END-IF.
    IF WS-PERFORM-SUB > 0 AND WS-DT-REC-ADDED-CCYYMMDD <
WS-CUTOFF-CCYYMMDD
        MOVE 'Y'  TO SPECL-CUST-FLAG
        PERFORM B28095-PROCESS-SPECUST THRU B28095-EXIT
         VARYING SUB1 FROM WS-PERFORM-SUB BY 1
          UNTIL SUB1 > WS-PERFORM-SUB
    END-IF
END-IF.


(note: I made this up more-or-less on the spot; the syntax is a more
modern dialect of COBOL called 'COBOL '85' or 'COBOL II'... it would have
been *much* more difficult to implement under COBOL '68 or COBOL '74)

This is a very commonly-used technique called 'windowing'.  A 'pivot
date', in this case the year (20)40, is decided-upon... of the year is
less than 40 (00 - 39) then it is considered to be in the 21st century, if
the year is 40 or higher then it is assumed to be in the 20th century.

Stop pissing and whining about how this is an incomplete solution; I
*know* that already... what is important is:

1) Windowing is a solution already decided-upon by many organisations
(and, interestingly enough, will be satisfactory for most of their
applications)

2) the code above, shown 'pre-window' and with window inserted, contains
an introduced logical flaw which will cause it to malfunction.

That's right... the code I inserted to make the program Y2K-compliant has
introduced a bug.  Where is it?

(oh... and while you're looking for the bug remember that your boss, his
boss and *her* boss are all looking over your shoulder and/or pacing
outside of your cubicle, reminding you how Importantit is that this get
fixed Right Now because it is Costing Money because the system is down
*and* they *can't* understand why you didn't get it right the First
Time... just to give you a bit of atmosphere, don'cha know)

(clock's ticking... welfare-moms are spending the money while you're
looking... where's the error, Captain COBOL?)

--end quoted text

Gosh... in the past week I've started threads about sending files via ftp
from NT workstations to mainframes and back again *and* this'un about
remediation difficulties in real live code... I must be slipping,
*everyone* knows that I'm only good for one-liners and demonstrating that
gold isn't money 'cause I don't get no Dime-A-Rands in my pocket-change.

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** scottd@nbnet.nb.ca (Don Scott)
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36f81050.85033633@news.nbnet.nb.ca>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:

>
>
…[4 more quoted lines elided]…
>gold isn't money 'cause I don't get no Dime-A-Rands in my pocket-change.

Nice sample code, and no, I didn't find the bug that you introduced,
but I thought the error was reported as "1999" being entered as "199 "
and the blank got replaced with a zero, making it "1990".

I didn't see that particular piece of logic in your example.

I think the reports are of a *typing* error, not a program logic
error, per se.

Then again, maybe I'm confusing it with some other report.

DS

>
>DD
>
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F84CE1.D71999A1@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36f81050.85033633@news.nbnet.nb.ca>`

```
Don Scott wrote:
> 
> On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:
…[11 more quoted lines elided]…
> and the blank got replaced with a zero, making it "1990".

Oh, I realise that I, in two paragraphs of code, could not hope to
introduce some of the labyrinthine turns of something like the New
Jersey system... i was just trying to demonstrate to my buddy how
remediation introduces bugs.

> 
> I didn't see that particular piece of logic in your example.

See above... I'll wade through a few more replies before springing the
Obvious Error (isn't it interesting how all errors, once pointed out,
become Obvious?)

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** Steve Dover <swd@strata-group.Xcom>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8155F.61D0DE33@strata-group.Xcom>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
docdwarf@clark.net wrote:
> 
[snip the code example]

The windowing logic that was added should be before the
INSPECT TALLYING?  It is not apparent to me as the WS-PERFORM-SUB
value may be dependent upon the dates.  Since you left that code out,
that is probably not it and was just to mislead me.
Of course, I've done no Cobalt in many years so it must be obvious.
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F84E8E.B3592FE2@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F8155F.61D0DE33@strata-group.Xcom>`

```
Steve Dover wrote:
> 
> docdwarf@clark.net wrote:
…[7 more quoted lines elided]…
> Of course, I've done no Cobalt in many years so it must be obvious.

That's right, you're wrong... the solution *is* obvious (aren't they
all?) and not related to the PERFORM based on WS-PERFORM-SUB at all;
that was thrown in as some Miscellaneous Bad Code as that particular
PERFORM will only be done once no matter what.

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** someone@flubnutz.org (Ron Schwarz -- see sig to reply)
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36fd3010.29404631@news3.newscene.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:

>Gosh... in the past week I've started threads about sending files via ftp
>from NT workstations to mainframes and back again *and* this'un about
>remediation difficulties in real live code... I must be slipping,
>*everyone* knows that I'm only good for one-liners and demonstrating that
>gold isn't money 'cause I don't get no Dime-A-Rands in my pocket-change.

Yup.  Imagine that; DD breaks character.  The End *Is* Near!
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F84EC6.BB7B2BAA@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36fd3010.29404631@news3.newscene.com>`

```
Ron Schwarz -- see sig to reply wrote:
> 
> On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:
…[7 more quoted lines elided]…
> Yup.  Imagine that; DD breaks character.  The End *Is* Near!

Maybe so... or maybe there's just more than is dreamed of in *your*
philosophies, neh?

DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** someone@flubnutz.org (Ron Schwarz -- see sig to reply)
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<370477e0.47788255@news3.newscene.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36fd3010.29404631@news3.newscene.com> <36F84EC6.BB7B2BAA@home.com>`

```
On Wed, 24 Mar 1999 02:32:54 GMT, The Goobers <docdwarf@home.com> wrote:

>Ron Schwarz -- see sig to reply wrote:
>> 
…[11 more quoted lines elided]…
>philosophies, neh?

A one-man play?
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

_(reply depth: 4)_

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8D19D.AB50774D@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36fd3010.29404631@news3.newscene.com> <36F84EC6.BB7B2BAA@home.com> <370477e0.47788255@news3.newscene.com>`

```
Ron Schwarz -- see sig to reply wrote:
> 
> On Wed, 24 Mar 1999 02:32:54 GMT, The Goobers <docdwarf@home.com> wrote:
…[16 more quoted lines elided]…
> A one-man play?

Answering a question with a question is no answer at all, Mr Schwarz.

DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7daq3a$2ji$1@news.igs.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36fd3010.29404631@news3.newscene.com> <36F84EC6.BB7B2BAA@home.com> <370477e0.47788255@news3.newscene.com> <36F8D19D.AB50774D@home.com>`

```
The Goobers wrote in message
>> >Maybe so... or maybe there's just more than is dreamed of in *your*
>> >philosophies, neh?
…[3 more quoted lines elided]…
>Answering a question with a question is no answer at all, Mr Schwarz.


Can you pronounce "Mea Culpa" Doc?
<G>
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** Robert Egan <egan263@nospam_allowed.ix.netcom.com>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F83DE0.83335E1F@nospam_allowed.ix.netcom.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
The only explanation I can think of is that your source data exceeds
your window range. In other words, there are some valid records from
1939, etc, still in your database which are now processed incorrectly.

This is, of course, a danger inherent in all windowing solutions.

It would help if you could provide some "dummy" data <g>


Regards
Robert Egan
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F85095.1289C316@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F83DE0.83335E1F@nospam_allowed.ix.netcom.com>`

```
Robert Egan wrote:
> 
> The only explanation I can think of is that your source data exceeds
…[5 more quoted lines elided]…
> It would help if you could provide some "dummy" data <g>

The error, Mr Egan, is data-*in*dependent; it is a 'logic flaw' which
alter the flow of the code after a certain point no matter *which* data
bring it there.

DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** Robert Egan <egan263@nospam_allowed.ix.netcom.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8A856.2B316F85@nospam_allowed.ix.netcom.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F83DE0.83335E1F@nospam_allowed.ix.netcom.com> <36F85095.1289C316@home.com>`

```
Thanks for the tip. I guess the real culprit is the extra period,
prematurely terminating the outermost IF. Like most errors, blindingly
obvious once someone points it out <g>.

I don't understand why the compiler would allow the unmatched END-IF,
but I've been away from COBOL for many years.

Regards
Robert Egan

The Goobers wrote:
> 
> Robert Egan wrote:
…[13 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

_(reply depth: 4)_

- **From:** someone@flubnutz.org (Ron Schwarz -- see sig to reply)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36f8b0ad.62329585@news3.newscene.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F83DE0.83335E1F@nospam_allowed.ix.netcom.com> <36F85095.1289C316@home.com> <36F8A856.2B316F85@nospam_allowed.ix.netcom.com>`

```
On Wed, 24 Mar 1999 03:54:46 -0500, Robert Egan
<egan263@nospam_allowed.ix.netcom.com> wrote:

>Thanks for the tip. I guess the real culprit is the extra period,
>prematurely terminating the outermost IF. Like most errors, blindingly
>obvious once someone points it out <g>.

He did say after a "certain point," didn't he? <g>

>I don't understand why the compiler would allow the unmatched END-IF,
>but I've been away from COBOL for many years.
…[20 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

_(reply depth: 4)_

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8D2F9.648C3937@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F83DE0.83335E1F@nospam_allowed.ix.netcom.com> <36F85095.1289C316@home.com> <36F8A856.2B316F85@nospam_allowed.ix.netcom.com>`

```
Robert Egan wrote:
> 
> Thanks for the tip. I guess the real culprit is the extra period,
> prematurely terminating the outermost IF. Like most errors, blindingly
> obvious once someone points it out <g>.

Well done, Mr Egan... but I see that Mr Sanders' post with this answer
shows, on my screen, the timestamp of 22:47 and you have 22:54.  Nicely
done, though!

DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

_(reply depth: 5)_

- **From:** croaker@barkingmad.org (Frank Ney)
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<3710768f.13593203@news.remarq.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F83DE0.83335E1F@nospam_allowed.ix.netcom.com> <36F85095.1289C316@home.com> <36F8A856.2B316F85@nospam_allowed.ix.netcom.com> <36F8D2F9.648C3937@home.com>`

```
On Wed, 24 Mar 1999 11:56:56 GMT, an orbiting mind control laser caused The
Goobers <docdwarf@home.com> to write:

>> Thanks for the tip. I guess the real culprit is the extra period,
>> prematurely terminating the outermost IF. Like most errors, blindingly
…[4 more quoted lines elided]…
>done, though!

Yes, to both of you.

I recused myself from Doc's little exercise.  It's just not fair for another
COBOL-weenie to deprive others of a learning experience...


Frank Ney  N4ZHG  WV/EMT-B  LPWV  NRA(L) GOA CCRKBA JPFO
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** "Rev Tim Burke" <asciiset@hotmail.com>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<KeXJ2.2309$3C3.5937@news3.ispnews.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```

<docdwarf@clark.net> wrote in message
news:7d91j7$j1s$1@callisto.clark.net...

[snip]

> Gosh... in the past week I've started threads about sending files via ftp
> from NT workstations to mainframes and back again *and* this'un about
> remediation difficulties in real live code... I must be slipping,
> *everyone* knows that I'm only good for one-liners and demonstrating that
> gold isn't money 'cause I don't get no Dime-A-Rands in my pocket-change.

You sicken me, Dwarf. There you go, evolving again. You used to be a nice,
sweet, nude, Cheeto-munching, Stooge-watching, Budgie-loving little
schmuck. NOW LOOK AT CHA'!
_____
Rev Tim Burke

> DD
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8510E.5665B1F5@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <KeXJ2.2309$3C3.5937@news3.ispnews.com>`

```
Rev Tim Burke wrote:
> 
> <docdwarf@clark.net> wrote in message
…[12 more quoted lines elided]…
> schmuck. NOW LOOK AT CHA'!

Mr Burke, whoever said 'Alas, two souls dwell within my breast!' fell
short... by a goodly number of souls, or so ol' Nietzsch' tells us. 
Pray, hold of on your aesthetic judgements... where's the bug?

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** "Greg Condon" <nospam@me.thanks>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7EYJ2.62$y8.562592@news.bctel.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
Um, isn't the "." after the END-IF in the date windowing the bug?
I've been a code reviewer for a while, so I notice these little things.

Do I get a prize?   :^)


 - Greg


docdwarf@clark.net wrote in message <7d91j7$j1s$1@callisto.clark.net>...
>
>
…[41 more quoted lines elided]…
>    END-IF.


^^^^^^  Notice the . after the END-IF.  Watch your system go boom!


>    IF WS-PERFORM-SUB > 0 AND WS-DT-REC-ADDED-CCYYMMDD <
>WS-CUTOFF-CCYYMMDD
…[49 more quoted lines elided]…
>
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F85C2B.C86B8E93@att.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
docdwarf@clark.net wrote:
> 
> So I get an email from a buddy o' mine... 'Hey, what's up with this New
…[5 more quoted lines elided]…
> it, is running on the Jersey Iron.

I was told earlier today that the problem was a result of a person's
keying in 1990 instead of 1999. 

Bill Lynch
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** "Dave Sanders" <davesanders@fuse.net>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<922247327.999.26@news.remarQ.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```

docdwarf@clark.net wrote in message <7d91j7$j1s$1@callisto.clark.net>...
>

>    IF WS-CUTOFF-YY < 40
>        MOVE 20 TO WS-CUTOFF-CC
…[10 more quoted lines elided]…
>END-IF.


It seems to me that the "." at the end of the CUTOFF date windowing would
terminate the "IF INDEPENDENT-CUSTOMER" logic, but it also seems to me it
would create a syntax error because there is then an extraneous "END-IF" at
the end of your example.
```

##### ↳ ↳ Re: New Jersey's Woes - An Example - The Winner!

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8D597.9249E2B4@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <922247327.999.26@news.remarQ.com>`

```
Dave Sanders wrote:
> 
> docdwarf@clark.net wrote in message <7d91j7$j1s$1@callisto.clark.net>...
…[19 more quoted lines elided]…
> the end of your example.

This is correct, both to the logic-error and the syntax-error; the
former was intended, of course, and the latter was the result of a
sloppy cut-n-paste.

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F99E02.4662@netbox.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
docdwarf@clark.net wrote:

> Could be... consider the following two bits of code:
> 
…[29 more quoted lines elided]…
>     END-IF.

I believe you slipped a period in here which changes the logic so the
next section is not executed for the 'independent-customer'

>     IF WS-PERFORM-SUB > 0 AND WS-DT-REC-ADDED-CCYYMMDD <
> WS-CUTOFF-CCYYMMDD
…[5 more quoted lines elided]…
> END-IF.

However, that leaves an extra end-if in the bottom section, and I wonder
how this compiled...oh, this is just an example, not real code, I
forgot.

An easy mistake to make in the coding, but who was responsible for the
testing ??

Bob
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F959A7.69501352@IMN.nl>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
Beside all other things ...

docdwarf@clark.net wrote:
8<

> MOVE MFCS-CUST-NO-01 TO WS-CUSTNO.
> IF INDEPENDENT-CUSTOMER
>     PERFORM A53102-ALLOCATE-LOT THRU A53102-EXIT
>     PERFORM C88092-CALC-CUBES   THRU C88092-EXIT
>     PERFORM E35702-FIND-SHPWGHT THRU E35702-EXIT

MOVE ZERO TO WS-PERFORM-SUB
or add an:
INITIALIZE WS-PERFORM-SUB

>
>     INSPECT WS-CUSTNO TALLYING WS-PERFORM-SUB FOR ALL 'QZ'
…[7 more quoted lines elided]…
>

8<

> Gosh... in the past week I've started threads about sending files via ftp
> from NT workstations to mainframes and back again *and* this'un about
…[4 more quoted lines elided]…
> DD

What's the rate for doing your homework?

Frog
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7ddujn$k4v$1@clarknet.clark.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F959A7.69501352@IMN.nl>`

```
In article <36F959A7.69501352@IMN.nl>,
COBOL Frog (Huib Klink) <H.Klink@IMN.nl> wrote:
>Beside all other things ...

[snippissmus]

>What's the rate for doing your homework?

If one has to ask it then one cannot afford it.

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36faac51.9358576@news3.ibm.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:

>        MOVE 19 TO WS-CUTOFF-CC
>    END-IF.
…[7 more quoted lines elided]…
>END-IF.


Does this compile??  There is a dot behind the END-IF (line 2)  which somehow makes the
final END-IF one too many.
with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: New Jersey's Woes - An Example and My Explicit Apology

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8D687.B1CA6F72@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36faac51.9358576@news3.ibm.net>`

```
Volker Bandke wrote:
> 
> On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:
…[14 more quoted lines elided]…
> with kind regards

That is correct, Mr Bandke... when I formulated the example I cut off
the final END-IFs and placed the period (full stop) after the last
WS-PERFORM-SUB; when I cut-n-pasted the example to the group I did so in
a sloppy manner and I apologise for the syntax error which it
introduced.

I would say, then, that based on my error this example should be
declared null and void and I once again apologise for sullying your eyes
with such laxity.

DD
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example and My Explicit Apology

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36f9f939.921214@news3.ibm.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36faac51.9358576@news3.ibm.net> <36F8D687.B1CA6F72@home.com>`

```
On Wed, 24 Mar 1999 12:12:06 GMT, The Goobers <docdwarf@home.com> wrote:

>Volker Bandke wrote:
>> 
…[27 more quoted lines elided]…
>DD


No need for apologies - your example just sent me on a wild goose chase <g>

Also I will cut and paste it and show it to my students in the next cobol class and let
THEM try to find the error  (I will make things a little bit harder and will remove the
final end-if, but not the final dot)

Again, a fine example for the ODPP rule (one dot per paragraph)

with kind regards

Volker Bandke
(BSP GmbH)
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** GeorgeValentine@usa.net
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7davkv$7ah$1@nnrp1.dejanews.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
Should not the various 19 and 20 be '19' and '20' respectively?

George


In article <7d91j7$j1s$1@callisto.clark.net>,
  docdwarf@clark.net () wrote:
>
>
…[93 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7db0d9$s9$1@clarknet.clark.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <7davkv$7ah$1@nnrp1.dejanews.com>`

```
In article <7davkv$7ah$1@nnrp1.dejanews.com>,  <GeorgeValentine@usa.net> wrote:
>Should not the various 19 and 20 be '19' and '20' respectively?

Not necessarily, Mr Valentine.. granted the definitions of the fields
involved would make this more obvious but if the fields are defined as 99
or 9(02) then the quotes are not needed.

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** kiyoinc@ibm.XOUT.net (cory hamasaki)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7kepWhCNP4qd-pn2-Zm7S5ydDVoO1@localhost>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
On Tue, 23 Mar 1999 21:37:43, docdwarf@clark.net () wrote:

>     IF WS-DT-REC-ADDED-YY < 40
>         MOVE 20 TO WS-DT-REC-ADDED-CC
>     ELSE
>         MOVE 19 TO WS-DT-REC-ADDED-CC
>     END-IF

>     IF WS-CUTOFF-YY < 40
>         MOVE 20 TO WS-CUTOFF-CC
>     ELSE
>         MOVE 19 TO WS-CUTOFF-CC
>     END-IF.

/* it's not above. */

>     IF WS-PERFORM-SUB > 0 AND WS-DT-REC-ADDED-CCYYMMDD <
> WS-CUTOFF-CCYYMMDD

/* Lets see, something about the order of the comparison.  You didn't 
show us the declarations but even the likes of you wouldn't name 
something ccyymmdd and store it as ccyyddmm.  

I'm guessing that this routine authorizes the money if the above test is 
true.  It used to evaluate false.

The data used to be  990321 < 990315  which is false, no funds issued
            if transaction date < cutoff the money date, issue the funds

In the expansion,  19990321 < 19990315 which is still false

*/

>         MOVE 'Y'  TO SPECL-CUST-FLAG
>         PERFORM B28095-PROCESS-SPECUST THRU B28095-EXIT
>          VARYING SUB1 FROM WS-PERFORM-SUB BY 1
>           UNTIL SUB1 > WS-PERFORM-SUB

>     END-IF

 
> That's right... the code I inserted to make the program Y2K-compliant has
> introduced a bug.  Where is it?

//sysudump  dd sysout=a   Give it to me.

> (clock's ticking... welfare-moms are spending the money while you're
> looking... where's the error, Captain COBOL?)
> 
> --end quoted text
 
> Gosh... in the past week I've started threads about sending files via ftp
> from NT workstations to mainframes and back again *and* this'un about
…[4 more quoted lines elided]…
> DD

OK, I give up, you are Caaaaaptain COOOOOBOL.

cory hamasaki 283 Days, 6,796 Hours, http://www.kiyoinc.com/current.html


```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** The Goobers <docdwarf@home.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F8501C.72A2751C@home.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <7kepWhCNP4qd-pn2-Zm7S5ydDVoO1@localhost>`

```
cory hamasaki wrote:
> 
> On Tue, 23 Mar 1999 21:37:43, docdwarf@clark.net () wrote:
…[20 more quoted lines elided]…
> something ccyymmdd and store it as ccyyddmm.

That is correct, Mr Hamasaki; I am not playing any tricks with Bad Data
or Funky Variable Mis-Naming.

> 
> I'm guessing that this routine authorizes the money if the above test is
> true.  It used to evaluate false.

You're taking the example too literally... but that is to be expected
from a bit-burner; paragraph-names like A53102-ALLOCATE-LOT,
C88092-CALC-CUBES and E35702-FIND-SHPWGHT are meant to be generic COBOL
routines, such as those found in a shipping-and-handling system.

> 
> The data used to be  990321 < 990315  which is false, no funds issued
>             if transaction date < cutoff the money date, issue the funds
> 
> In the expansion,  19990321 < 19990315 which is still false

Exactly... you're looking too hard for me to match New Jersey *exactly*,
rather than merely give a general example of how remediation can botch
code.

> 
> */
…[12 more quoted lines elided]…
> //sysudump  dd sysout=a   Give it to me.

It won't show up there.

> 
> > (clock's ticking... welfare-moms are spending the money while you're
…[12 more quoted lines elided]…
> OK, I give up, you are Caaaaaptain COOOOOBOL.

Not yet, Mr Hamasaki... go back and re-examine the specimen without
looking for it to reflect the New Jersey situation so precisely.

I'll even give you a hint... your first assertion is wrong.

DD
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36f86959.88591620@news1.ibm.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:

>
>
…[24 more quoted lines elided]…
>END-IF.

There's been no windowing applied at this point - it occurs later.
What's going to happen is as soon as the cuttoff year is in 2000, this
code will execute (The IF will be true) - where last month it would
not have.    

This could have been remediated years ago, and just now fail.
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36f86a87.88894017@news1.ibm.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
On 23 Mar 1999 21:37:43 GMT, docdwarf@clark.net () wrote:

Late day  - didn't realize it was PRE remediate and POST remediation.
Ugh.  Let me attempt this.


>Could be... consider the following two bits of code:
>
…[29 more quoted lines elided]…
>    END-IF.

** I concur - it's the period above.

>    IF WS-PERFORM-SUB > 0 AND WS-DT-REC-ADDED-CCYYMMDD <
>WS-CUTOFF-CCYYMMDD
…[5 more quoted lines elided]…
>END-IF.
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** burnt out case <burntoutcase@netscape.net>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36F893A1.FF4DF722@netscape.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```


docdwarf@clark.net wrote:
> 
> MOVE MFCS-CUST-NO-01 TO WS-CUSTNO.
…[26 more quoted lines elided]…
> looking... where's the error, Captain COBOL?)

mumble ... mumble  goddamned newfangled end-ifs and
what-nots

but i'll bet they still get in trouble with those damn
periods

did I ever tell you about the guy I ran into who thought it
was a neat trick to put all his periods in col 70 so he knew
where to find them?
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** croaker@barkingmad.org (Frank Ney)
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<371176d2.13660312@news.remarq.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F893A1.FF4DF722@netscape.net>`

```
On Wed, 24 Mar 1999 01:26:25 -0600, an orbiting mind control laser caused
burnt out case <burntoutcase@netscape.net> to write:

>but i'll bet they still get in trouble with those damn
>periods

Of course.

Q:  How is COBOL like a woman?
A:  Miss one period and you're in trouble.

<g, r & dfc>


Frank Ney  N4ZHG  WV/EMT-B  LPWV  NRA(L) GOA CCRKBA JPFO
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** Steve Dover <swd@strata-group.Xcom>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36FAD981.C9226269@strata-group.Xcom>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F893A1.FF4DF722@netscape.net>`

```
burnt out case wrote:
> 
> mumble ... mumble  goddamned newfangled end-ifs and
> what-nots

Still got me confused.  Never saw an end-if in the old days.

> 
> but i'll bet they still get in trouble with those damn
…[4 more quoted lines elided]…
> where to find them?

I remember (many periods ago) the recommendation to
put the periods on a line by themselves. 
He said it improved readability (and I did agree), but I
think he did to improve his SLOC count and impress the boss.
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** Ed Stevens <Ed.Stevens@nmm.nissan-usa.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<7dddum$bq4$1@nnrp1.dejanews.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F893A1.FF4DF722@netscape.net>`

```
In article <36F893A1.FF4DF722@netscape.net>,
  burnt out case <burntoutcase@netscape.net> wrote:
>
>
…[48 more quoted lines elided]…
>

It does nothing for legacy code, but this is the very reason I advocate
adopting statement delimiters (END-IF, END-PERFORM, etc.) which then allows
the elimination of all procedure division periods except to terminate
paragraph names and paragraphs themselves.

A1000-DO-SOME-WORK.
    MOVE A TO B
    IF C = D
        ....
    ELSE
        ....
    END-IF

    EVALUATE PROCESS-FLAG
         ....
    END-EVALUATE
    .       <*---  only period ever needed.

Ed Stevens
(Opinions are not necessarily those of my employer)

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36FA49E4.A8566129@NOSPAMhome.com>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <36F893A1.FF4DF722@netscape.net> <7dddum$bq4$1@nnrp1.dejanews.com>`

```
> It does nothing for legacy code, but this is the very reason I advocate
> adopting statement delimiters (END-IF, END-PERFORM, etc.) which then allows
> the elimination of all procedure division periods except to terminate
> paragraph names and paragraphs themselves.

I usually code periods out of habit, but sometimes I do so deliberately
around pre-compiler statements.  If I am not entirely comfortable with
the way a pre-compiler (in my case IDMS) expands code, I like to have
periods.

IDMS expanded the two commented lines below:
009100*    READY IASAR902-REGION USAGE-MODE RETRIEVAL
009200*        ON ANY-ERROR-STATUS
                 MOVE 2 TO DML-SEQUENCE
                 CALL 'IDMS' USING SUBSCHEMA-CTRL
                         IDBMSCOM (37)
                         IASAR902-REGION
                 IF NOT ANY-ERROR-STATUS PERFORM IDMS-STATUS;
                 ELSE
009300             PERFORM 9000-GENERAL-IDMS-ERROR.

I have seen in the past where it messed up when I have complex
conditions, so I always keep things simple (performing paragraphs,
avoiding NOT, etc).  I think twice and check the expansion when a DML
statement is within an EVALUATE or IF.  And terminate when I can.
```

#### ↳ Re: New Jersey's Woes - An Example

- **From:** "rrcrumb" <zen_108@yahoo.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<5O0K2.2651$Kw1.1379874@news4.mia>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net>`

```
The number 199_  was typed in instead of 1999.
The 199_  was recognized as 1990.

That is the problem according to news reports.


rrc



<docdwarf@clark.net> wrote in message
news:7d91j7$j1s$1@callisto.clark.net...
>
>
…[93 more quoted lines elided]…
>
```

##### ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<36f8e661.1554859@news1.ibm.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <5O0K2.2651$Kw1.1379874@news4.mia>`

```
On Wed, 24 Mar 1999 07:49:21 GMT, "rrcrumb" <zen_108@yahoo.com> wrote:

>The number 199_  was typed in instead of 1999.
>The 199_  was recognized as 1990.
>
>That is the problem according to news reports.

Forgive me for being skeptical --- but I have had DIRECT dealings with
the state of NJ.  After their last fiasco, they are QUICK to get on
the press pulpit and defend themselves.  (Is their assertion true?  I
dunno).

Anyway, It STILL COULD be a byproduct of Y2K remediation.  I bet the
old data entry program would not let you enter 9_, but the new
expanded entry probably does not perform a proper data validation.
```

###### ↳ ↳ ↳ Re: New Jersey's Woes - An Example

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.software.year-2000
- **Message-ID:** `<CA28A7F867E57F3F.C7FD1A4EC6B0C105.B8F616290B1B7C1A@library-proxy.airnews.net>`
- **References:** `<7d91j7$j1s$1@callisto.clark.net> <5O0K2.2651$Kw1.1379874@news4.mia> <36f8e661.1554859@news1.ibm.net>`

```
On Wed, 24 Mar 1999 13:22:15 GMT, redsky@ibm.net (Thane Hubbell)
enlightened us:

>On Wed, 24 Mar 1999 07:49:21 GMT, "rrcrumb" <zen_108@yahoo.com> wrote:
>
…[12 more quoted lines elided]…
>expanded entry probably does not perform a proper data validation.

Hence the old adage garbage in, garbage out still holds true.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

The average woman would rather have beauty than brains because the
average man can see better than he can think.

 Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
