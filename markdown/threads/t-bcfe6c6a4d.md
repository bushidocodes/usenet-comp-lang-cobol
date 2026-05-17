[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call pgm no goback/return

_6 messages · 6 participants · 1998-08_

---

### Call pgm no goback/return

- **From:** "a. braet" <ua-author-17074223@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6qvb3i$8i2$1@ins8.netins.net>`

```
Does anyone know what the side effects are of a cobol program calling a
called program which does not contain a "goback" or return command?
```

#### ↳ Re: Call pgm no goback/return

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcfe6c6a4d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6qvb3i$8i2$1@ins8.netins.net>`
- **References:** `<6qvb3i$8i2$1@ins8.netins.net>`

```
› Does anyone know what the side effects are of a cobol program calling a
› called program which does not contain a "goback" or return command?

Sure (It is an EXIT PROGRAM, btw). If the subroutine does not
return, then the effect is that the main program never gets control
back, the same as with any other language.

Oh yes, plus what ever the subroutine does while never returning, the
same as with any other language.
```

#### ↳ Re: Call pgm no goback/return

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcfe6c6a4d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6qvb3i$8i2$1@ins8.netins.net>`
- **References:** `<6qvb3i$8i2$1@ins8.netins.net>`

```

A. Braet wrote in message <6qvb3i$8i2$1.··.@ins··s.net>...
› Does anyone know what the side effects are of a cobol program calling a
› called program which does not contain a "goback" or return command?
›
›

Pre- ANS'85, this was undefined (and if you are using OS/VS COBOL, you may
well get a "fall thru" ABEND). (I am assuming an IBM environment because
you mention the extension "GOBACK".) With any of the newer compilers (using
the NOCMPR2 compiler option - which forces ANS'85 behavior), it should be as
if the program were compiled with a final "EXIT PROGRAM" at the very end of
the source code (physical end - not logical end). This isn't usually what
you really want - but it is "well defined" in the current Standard.
```

#### ↳ Re: Call pgm no goback/return

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcfe6c6a4d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6qvb3i$8i2$1@ins8.netins.net>`
- **References:** `<6qvb3i$8i2$1@ins8.netins.net>`

```

A. Braet wrote in message <6qvb3i$8i2$1.··.@ins··s.net>...
› Does anyone know what the side effects are of a cobol program calling a
› called program which does not contain a "goback" or return command?


yes, but it depends on the compiler and the platform.
Always state these up front, when you post a question to the NG.
```

#### ↳ Re: Call pgm no goback/return

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1998-08-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcfe6c6a4d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6qvb3i$8i2$1@ins8.netins.net>`
- **References:** `<6qvb3i$8i2$1@ins8.netins.net>`

```
On Fri, 14 Aug 1998 01:34:42 GMT "Jeff" wrote:

:>>Does anyone know what the side effects are of a cobol program calling a
:>>called program which does not contain a "goback" or return command?


:>Bad bad things. In an MVS system running an IMS database, depending on how
:>the IMS system is set up, IT COULD BRING DOWN THE ENTIRE DATABASE. From my
:>understanding, all programs accessing IMS online databases are sub-programs
:>of IMS or whatever. When a poorly written ill-conceived piece of s____
:>program written without a GOBACK is executing in this environment, it stops
:>IMS.

:>I was told even a STOP RUN would cause this problem. Ever since, I never
:>code a STOP RUN without a GOBACK immediately before it.

:>I may be wrong. But paranoid programmers live long and fruitful lives.

I believe you misspelled CICS.

In IMS transactions run in a separate address space. Should the transaction
fail to complete in the work unit time, for whatever reason, the message
reason will abend the transaction and the address space would restart. The
transaction would also be stopped and no longer be dispatched.

I would think that a STOP RUN would, at worst, cause a message region restart.

Neither case would hang IMS.
```

#### ↳ Re: Call pgm no goback/return

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-08-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcfe6c6a4d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6qvb3i$8i2$1@ins8.netins.net>`
- **References:** `<6qvb3i$8i2$1@ins8.netins.net>`

```
Jeff wrote:
› 
›› Does anyone know what the side effects are of a cobol program calling a
…[12 more quoted lines elided]…
› I may be wrong. But paranoid programmers live long and fruitful lives.

This is a CICS problem. The STOP RUN command in cobol actually executes
a system services SVC. In this case the SVC says to terminate the
program that I am currently running. Guess what in a cooperative CICS
environment this happened to be CICS itself.

I think that this might have been fixed since, but I agree with be
careful and do not take risks. You may just change to a very old system
one day.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
