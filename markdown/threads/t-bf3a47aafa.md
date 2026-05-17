[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Determining who CALLed me

_9 messages · 7 participants · 1997-11 → 1997-12_

---

### Determining who CALLed me

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65vree$43s@bgtnsc03.worldnet.att.net>`

```

Can anyone suggest a way for a batch Cobol II pgm, MVS/ESA environment,
to determine the name of the CALLing program?

TIA,
Bill Lynch
```

#### ↳ Re: Determining who CALLed me

- **From:** "sco..." <ua-author-6589162@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<65vree$43s@bgtnsc03.worldnet.att.net>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net>`

```

Either pass the name from the CALL'ing program or CALL an Assembler
subroutine to pass it back to you.

I've run into this situation before where I had to know the CALL'ing
program name, but I'll be damned if I can remember why. Probably I
was making the CALL'ed program work differently based on its CALL'ing
program. Is this your case?

Don


On Mon, 01 Dec 1997 21:22:59 -0500, Bill Lynch
wrote:

› Can anyone suggest a way for a batch Cobol II pgm, MVS/ESA environment,
› to determine the name of the CALLing program?
› 
› TIA,
› Bill Lynch
```

##### ↳ ↳ Re: Determining who CALLed me

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf3a47aafa-p2@usenetarchives.gap>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net> <gap-bf3a47aafa-p2@usenetarchives.gap>`

```

Don Scott wrote:
› 
› Either pass the name from the CALL'ing program or CALL an Assembler
…[7 more quoted lines elided]…
› Don

Not exactly. I'm implementing my new, and improved, date routine, and
I'd like to tailor any error messages with the name of the CALLing pgm
so we know exactly where to look. CICS makes this *much* easier and I've
already solved the problem there. We're definitely *not* going to change
all the existing batch pgms to pass their names, so I expect I'll have
to rely on good ol' ASM. It's not all that easy there, either, because
the CALLs are all dynamic. I know it's solvable - Abend-Aid & Xpediter
do it.

Thanks for responding,
Bill Lynch

› 
› On Mon, 01 Dec 1997 21:22:59 -0500, Bill Lynch
…[6 more quoted lines elided]…
›› Bill Lynch
```

###### ↳ ↳ ↳ Re: Determining who CALLed me

- **From:** "richard frankel" <ua-author-6589082@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf3a47aafa-p3@usenetarchives.gap>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net> <gap-bf3a47aafa-p2@usenetarchives.gap> <gap-bf3a47aafa-p3@usenetarchives.gap>`

```

Bill Lynch wrote:
› 
 
›› 
›› On Mon, 01 Dec 1997 21:22:59 -0500, Bill Lynch
…[6 more quoted lines elided]…
››› Bill Lynch

This solution does require a little work, but is easy to implement.
Why not define a common variable, say WC-CALLING-PROGRAM-ID as usage
EXTERNAL, in all your calling programs, and also in the common called
routine. Have each calling program set the variable to a suitable
value, call the called-routine, where you will be able to access
WC-CALLING-PROGRAM-ID.

This variable is then available
```

###### ↳ ↳ ↳ Re: Determining who CALLed me

_(reply depth: 4)_

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf3a47aafa-p4@usenetarchives.gap>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net> <gap-bf3a47aafa-p2@usenetarchives.gap> <gap-bf3a47aafa-p3@usenetarchives.gap> <gap-bf3a47aafa-p4@usenetarchives.gap>`

```

snips
›››› Can anyone suggest a way for a batch Cobol II pgm, MVS/ESA environment,
›››› to determine the name of the CALLing program?
…[4 more quoted lines elided]…
› routine. 

In a similar vein - how about a SYSIN in the JCL with the calling
program's name? Then the CALLed program could ACCEPT CALLER-PROGRAM-NAME
FROM SYSIN. The CALLers would not have to acknowledge SYSIN, so there
would be no change to them. The chore is to change all the JCL steps
where a CALL might happen. If SYSIN is already used by the CALLer
program, a file name such as //CALLER DD * could suffice, with approp
OPEN, READ, and CLOSE statements in the CALLed program. It's still
unacknowledged by the CALLers, so they have no changes in them.
Of course this would not suffice if a JCL step runs 'master program'
which calls a number of 'subprograms' any of which could call the lowest
program, and the lowest program is the one who cares about the caller.

It also implies that the CALLed program must always find SYSIN (or the
FILE), so it would be a little more tricky to have the CALLed program
available from online as well as batch.

You could phase in the JCL implementation to contain the new statements.
Then when all JCL's are ready, move in the new CALLed program. Once the
CALLed program is there, of course, all the JCLs better be ready.

I haven't tried this but I am pretty sure it would work. (I think this
strategy was used in a Walker A/P project I did many lifetimes ago.) If
not correct, someone please respond - so bad info doesn't get out there
(particularly with my name on it:)).

John
```

#### ↳ Re: Determining who CALLed me

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p6@usenetarchives.gap>`
- **In-Reply-To:** `<65vree$43s@bgtnsc03.worldnet.att.net>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net>`

```



Bill Lynch wrote in article
<65vree$4.··.@bgt··t.net>...
› Can anyone suggest a way for a batch Cobol II pgm, MVS/ESA environment,
› to determine the name of the CALLing program?

All I know to do is to pass the calling program's id as one of the call
parameters.
```

#### ↳ Re: Determining who CALLed me

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-12-04T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p7@usenetarchives.gap>`
- **In-Reply-To:** `<65vree$43s@bgtnsc03.worldnet.att.net>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net>`

```

Bill Lynch wrote:
› 
› Can anyone suggest a way for a batch Cobol II pgm, MVS/ESA environment,
…[3 more quoted lines elided]…
› Bill Lynch

Bill,
I'll bet this info is available in an MVS control block, which you could
probably get at from your program. Personally I don't know how to get at the
info, but I'll cross-post this reply to the IBM-MAIN group in case someone has
an example they'd like to share.

***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: Determining who CALLed me

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-12-05T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p8@usenetarchives.gap>`
- **In-Reply-To:** `<65vree$43s@bgtnsc03.worldnet.att.net>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net>`

```

On Mon, 01 Dec 1997 21:22:59 -0500, Bill Lynch
wrote:

› Can anyone suggest a way for a batch Cobol II pgm, MVS/ESA environment,
› to determine the name of the CALLing program?
Can't you get Caller-ID on that computer?

George Trudeau
```

##### ↳ ↳ Re: Determining who CALLed me

- **From:** "sco..." <ua-author-6589162@usenetarchives.gap>
- **Date:** 1997-12-05T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf3a47aafa-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bf3a47aafa-p8@usenetarchives.gap>`
- **References:** `<65vree$43s@bgtnsc03.worldnet.att.net> <gap-bf3a47aafa-p8@usenetarchives.gap>`

```

On Sat, 06 Dec 1997 16:16:59 GMT, don··.@roc··l.com (George
Trudeau) wrote:

› On Mon, 01 Dec 1997 21:22:59 -0500, Bill Lynch
› wrote:
…[5 more quoted lines elided]…
› George Trudeau

Caller-ID would work, wouldn't it????...... Except wouldn't some
programs want to have non-published numbers and therefore they
wouldn't show up on Caller-ID????..... But, other than that very
slight obstacle, I think Caller-ID is definitely the way to go....and
maybe we can make it an ANSI standard that all programs must have a
visible phone number..... no non-pubs.. Yeah, that's the ticket.....

Don
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
