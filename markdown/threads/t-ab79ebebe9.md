[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with GOBACK in COBOL CICS

_8 messages · 8 participants · 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Problem with GOBACK in COBOL CICS

- **From:** peterkr@ms.com
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<78q2ar$dlo$1@nnrp1.dejanews.com>`
- **References:** `<78mlle$ehf$1@news.mclink.it>`

```


I've found a case where the execution of a GOBACK command in a CICS
COBOL program apparantly keeps the program (actually a COBOL sub-program)
active in CICS. Another call to the sub-program causes it to pick up
execution where it left off the last time instead of beginning execution
with a "fresh" version of the sub-program.

There is even a statement in the V2 compiler manual that says this
can happen, but I was wonfering if anyone else has encountered it.

Tia
Pjk

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** Philip Morten <pmorten@transarc.com>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<36B0B40F.4DFAFE33@transarc.com>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
peterkr@ms.com wrote:
> 
> I've found a case where the execution of a GOBACK command in a CICS
…[9 more quoted lines elided]…
> Pjk

What release of which CICS product? What Operating System ?  Whose COBOL ?

Philip Morten
TXSeries Development
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<78qd8p$mte@sjx-ixn10.ix.netcom.com>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
Execution of a GOBACK (IBM extension) in a CICS environment OR ANYWHERE ELSE
from a subprogram *guarantees* that the next time the program is executed it
is re-entered in "last used state".   Given EXEC CICS HANDLE statements,
this may well mean that the execution will appear to "start in the middle".

Bottom-Line:
  I can't remember any case (well almost any) where you really want to reach
a GoBack (or EXIT PROGRAM - and certainly never Stop Run) in a CICS program.
Normally, you use some EXEC CICS statement to transfer control out of  CICS
program.  (You aren't by any chance doing a "real" conversational program
instead of pseudo-conversational - are you?)

You mention the "V2 compiler manual" but don't tell which compiler.  If this
is COBOL for this-and-that, then do look at the CBLPSHPOP (sp?) compiler
option which might be your problem.
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<78qi3g$9ju$1@news.igs.net>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
Is that not the way it is *supposed* to work?  Unless one
uses the "INITIAL" option that is?

peterkr@ms.com wrote in message <78q2ar$dlo$1@nnrp1.dejanews.com>...
>
>
…[13 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** Alan Levenson <aleven@web2000.net>
- **Date:** 1999-01-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<36B12DCF.3BC689B7@web2000.net>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
I haven't written CICS code in quite some time (7+ years), but I recall that
we used to initialize storage when invoking a program for the first time.
That may be your problem.

Alan

peterkr@ms.com wrote:

> I've found a case where the execution of a GOBACK command in a CICS
> COBOL program apparantly keeps the program (actually a COBOL sub-program)
…[11 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** WOB@my-dejanews.com
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<78r90b$gjk$1@nnrp1.dejanews.com>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
Actually, this is the proper behavior of a Sub-Program in CICS that is Called,
either Statically or 'Dynamically' (with a PPT entry, so really not Dynamic).
If the Sub-Program was a CICS Program and that program issued a CICS RETURN as
opposed to a GOBACK, this would terminate the Run-Unit or Task, whichever the
case may be. Otherwise, non-CICS Sub-Program's must always issue a GOBACK.
Another thing to watch out for in Sub-Program's (CICS or non-CICS) is residual
or non-initialized storage. There is NO guarantee of initialized storage after
the first call and execution (just like Batch), even with a VALUE clause. So
all bets are off. This is why it's good practice to initialize Working-Storage
manually at the start of the Procedure Division in a Sub-Program. Note that
NONE of this applies to programs accessed via the LINK API. Although a CALL
'identifier' CANCEL will refresh your storage, the overhead involved is
substantial. But, having never used a CALL CANCEL in CICS, I'm not even sure
it's advisable.

To gain a re-entrancy factor, pass the Sub-Program's workarea as a parameter
from the caller. By doing so, you won't raise any residual storage problems.
The caller is normally COBOL and his storage is serially-reusable. It's also
good practice for the Sub-Program (Load Module) to be no more than 4-5 MVS
Pages (16384-20480) in length.

You might want to try posting your question to bit.listserv.cics-l for some
further opinions and/or explanations.

HTH....

WOB,
Atlanta

In article <78q2ar$dlo$1@nnrp1.dejanews.com>,
  peterkr@ms.com wrote:
>
>
…[14 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<78rp7f$t8f$1@nnrp1.dejanews.com>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
In article <78q2ar$dlo$1@nnrp1.dejanews.com>,
  peterkr@ms.com wrote:
>
>
…[5 more quoted lines elided]…
>
<snip the rest>

Peter,

I am quite sure that it depends whether you CALLed or EXEC CICS LINKed the
subprogram. In the manuals it written that you should code an EXEC CICS
RETURN instead of a GOBACK if the module has been LINKed, but I know that
GOBACK works, too. That may be the difference: LINK gets a new copy, CALL the
last state of the working storage.

Cheers

Daniel

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Problem with GOBACK in COBOL CICS

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<36b96907.90670537@news3.ibm.net>`
- **References:** `<78mlle$ehf$1@news.mclink.it> <78q2ar$dlo$1@nnrp1.dejanews.com>`

```
On Thu, 28 Jan 1999 16:13:24 GMT, peterkr@ms.com wrote:

>
>
…[5 more quoted lines elided]…
>
A Short question:  Did you, by any means, mix COBOL and CICS calling environments?  That
is, if the main program is called A, and the sub program is called B, try any of

A:   EXEC CICS LINK PROGRAM('B') and
B:  GOBACK


or

A: MOVE 'B' TO PGM-NAME
    CALL pgm-name

B: EXEC CICS RETURN



If you did, this spells disaster..........

if EXEC CICS LINK, then EXEC CICS RETURN

if CALL, then GOBACK


with kind regards

Volker Bandke
(BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
