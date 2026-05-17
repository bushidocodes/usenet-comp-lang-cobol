[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help: VSE COBOL dynamic call?

_6 messages · 5 participants · 1995-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help: VSE COBOL dynamic call?

- **From:** "c440..." <ua-author-10776686@usenetarchives.gap>
- **Date:** 1995-09-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42p8mh$10jg@ctsc.hkbc.hk>`

```
Hi

I have a problem in using COBOL dynamic call under VSE/ESA

My scenario is:

dyn. call
(program A) ---------> (program B)

and B is going to
a. open a VSAM file
b. update record
c. close file.

the problem is: if B is called several hundred times
the program will be abended with insuff. virtual storage
to open file ?

Can u tell me why? Any relevant documentation about dyn. call?
Thanks in advance!

W.F Ng
```

#### ↳ Re: Help: VSE COBOL dynamic call?

- **From:** "marty..." <ua-author-17073867@usenetarchives.gap>
- **Date:** 1995-09-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-923efbd28b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<42p8mh$10jg@ctsc.hkbc.hk>`
- **References:** `<42p8mh$10jg@ctsc.hkbc.hk>`

```

NWF> Message-ID: <42p8mh$10··.@cts··c.hk>

NWF> I have a problem in using COBOL dynamic call under VSE/ESA
NWF> My scenario is:

NWF> dyn. call
NWF> (program A) ---------> (program B)

NWF> and B is going to
NWF> a. open a VSAM file
NWF> b. update record
NWF> c. close file.

NWF> the problem is: if B is called several hundred times
NWF> the program will be abended with insuff. virtual storage
NWF> to open file ?

PATIENT: "Doctor, it hurts when I do this."
DOCTOR: "Then don't do that!"

Pass a control parm list.

As part of the initialization of the CALLING program,
Call the subroutine to open the file.

As part of the termination of the CALLING program,
Call the subroutine to close the file.

Your module will also run MUCH faster, as file open/closes
are resource hogs.
---
* SLMR 2.1a * Nothing outlasts Data! He keeps going, and going, and...
```

#### ↳ Re: Help: VSE COBOL dynamic call?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1995-09-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-923efbd28b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<42p8mh$10jg@ctsc.hkbc.hk>`
- **References:** `<42p8mh$10jg@ctsc.hkbc.hk>`

```
The scenario which you describe should work, so long as those are the only
programs involved. Where this usually fails is when an assembler
component is involved in the CALL chain.

Other causes of trouble tend to relate to the compiler option RES, both
main and sub should have the same setting for the RES option. The
presence of a dynamic call in the mainline implies that it must use RES,
thus the subroutine must also be compiled with the RES option. If your
default is NORES, then the main will be forced RES by the dynamic call,
the sub would be left NORES, and the symptoms which you describe would not
be unexpected.

One suggestion to try to see what is going on would be to place a small
code fragment in the subroutine to see if a single copy of the subroutine
remains in storage.

77 TELL-TALE PIC X VALUE 'N'.

PROCEDURE DIVISION USING ...

IF TELL-TALE = 'N' THEN DISPLAY 'FIRST TIME THRU'
ELSE MOVE 'Y' TO TELL-TALE.

If you see "FIRST TIME THRU" more than once, the subroutine is being
loaded multiple times. In your code frag this should not occur since you
are not issuing a CANCEL subname.

The efficiency is probably terrible, opening the file each time, none the
less, it should work.

Probably one to send to compiler / run-time vendor for bug fix.
```

#### ↳ Re: Help: VSE COBOL dynamic call?

- **From:** "mark walsham" <ua-author-15609224@usenetarchives.gap>
- **Date:** 1995-09-08T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-923efbd28b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<42p8mh$10jg@ctsc.hkbc.hk>`
- **References:** `<42p8mh$10jg@ctsc.hkbc.hk>`

```
In article <42p8mh$10··.@cts··c.hk> c44··.@sci··c.hk "NG WAH FUNG" writes:

› Hi
› 
…[20 more quoted lines elided]…
›   
Hi,

Just a quick thing, are you using CANCEL to cancel program b
after the call, ie:-

Program A
.
.
CALL "PROGB" USING PARAMS.
CANCEL "PROGB".

If you do not cancel, this can cuse these sort of problems.

Hang Loose,

Dudeman.
------------------------------------------------------------
FROM:- Ma··.@dud··o.uk [London, United Kingdom, 95]
_-----------------------------------------------------------
```

#### ↳ Re: Help: VSE COBOL dynamic call?

- **From:** "gl..." <ua-author-3965476@usenetarchives.gap>
- **Date:** 1995-09-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-923efbd28b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<42p8mh$10jg@ctsc.hkbc.hk>`
- **References:** `<42p8mh$10jg@ctsc.hkbc.hk>`

```
NG WAH FUNG (c44··.@sci··c.hk) wrote:
: Hi

: I have a problem in using COBOL dynamic call under VSE/ESA

: My scenario is:

: dyn. call
: (program A) ---------> (program B)

: and B is going to
: a. open a VSAM file
: b. update record
: c. close file.

: the problem is: if B is called several hundred times
: the program will be abended with insuff. virtual storage
: to open file ?
:
: Can u tell me why? Any relevant documentation about dyn. call?
: Thanks in advance!

: W.F Ng
:
:

I have not been in VSE for awhile, but my recollection is that that type
of error occurs there under similar conditions to MVS. In general, your
program is getmaining storage every time you enter it, and not releasing
when you leave. You should probably use a
CANCEL program-name
statement after you return from the called subprogram.

gl··.@mil··m.com
```

#### ↳ Re: Help: VSE COBOL dynamic call?

- **From:** "c440..." <ua-author-10776686@usenetarchives.gap>
- **Date:** 1995-09-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-923efbd28b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<42p8mh$10jg@ctsc.hkbc.hk>`
- **References:** `<42p8mh$10jg@ctsc.hkbc.hk>`

```
NG WAH FUNG (c44··.@sci··c.hk) wrote:
: Hi

: I have a problem in using COBOL dynamic call under VSE/ESA

: My scenario is:

: dyn. call
: (program A) ---------> (program B)

: and B is going to
: a. open a VSAM file
: b. update record
: c. close file.

: the problem is: if B is called several hundred times
: the program will be abended with insuff. virtual storage
: to open file ?
:
: Can u tell me why? Any relevant documentation about dyn. call?
: Thanks in advance!

: W.F Ng
:
:
Hi
Thanks for all responses!
But i miss some infomation:
after each call, i do issue CANCEL program B,
but it still don't work.
I think, there should be certain storage that not free by
OS or Cobol run-time stuff! How many & Why?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
