[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Are Cobol DLLs possible?

_6 messages · 5 participants · 1998-05 → 1998-06_

---

### Are Cobol DLLs possible?

- **From:** "m.cr..." <ua-author-12785883@usenetarchives.gap>
- **Date:** 1998-05-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kk1fe$dem$1@clyde.open.ac.uk>`

```

Has any one out there created Windows DLLs from Cobol source files?

What products did you use?

We want to use some of our Cobol routines we have developed on
Unix from our Visual Basic applications, and the easiest way to do
this would be by building a DLL.

Any thoughts?

Thanks in advance,

Michael
```

#### ↳ Re: Are Cobol DLLs possible?

- **From:** "simon cordingley" <ua-author-6589258@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea5abf5334-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6kk1fe$dem$1@clyde.open.ac.uk>`
- **References:** `<6kk1fe$dem$1@clyde.open.ac.uk>`

```

Yes, our Casegen COBOL for Windows Professional product gives you the option
of bundling the Windows forms together as an .EXE or using them as .DLLs to
reduce executable size or for use by several applications.

Please see www.casegen.co.uk

Michael Cressey wrote in message <6kk1fe$dem$1.··.@cly··c.uk>...
› Has any one out there created Windows DLLs from Cobol source files?
› 
…[11 more quoted lines elided]…
›
```

#### ↳ Re: Are Cobol DLLs possible?

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea5abf5334-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6kk1fe$dem$1@clyde.open.ac.uk>`
- **References:** `<6kk1fe$dem$1@clyde.open.ac.uk>`

```

Michael,

Mixing Visual Basic and COBOL is very easy. See the White Paper on
Integrating Microsoft Visual Basic with Fujitsu COBOL at:
http://www.adtools.com/support/white.htm

Fujitsu COBOL is the fastest, most reliable COBOL for Windows 95/NT. You
can get the "FREE" unrestricted Fujitsu COBOL Starter Set at:
www.adtools.com

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


Michael Cressey wrote in message <6kk1fe$dem$1.··.@cly··c.uk>...
› Has any one out there created Windows DLLs from Cobol source files?
› 
…[11 more quoted lines elided]…
›
```

#### ↳ Re: Are Cobol DLLs possible?

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-05-31T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea5abf5334-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6kk1fe$dem$1@clyde.open.ac.uk>`
- **References:** `<6kk1fe$dem$1@clyde.open.ac.uk>`

```

Michael Cressey wrote:
› 
› Has any one out there created Windows DLLs from Cobol source files?
…[5 more quoted lines elided]…
› this would be by building a DLL.

Michael,

With Micro Focus COBOL, it can be this simple:

cbllink -D file.cbl

(-D tells the cbllink utility to create a DLL rather than an EXE).

Cheers, Kev.
```

##### ↳ ↳ Re: Are Cobol DLLs possible?

- **From:** "sch..." <ua-author-17074386@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea5abf5334-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ea5abf5334-p4@usenetarchives.gap>`
- **References:** `<6kk1fe$dem$1@clyde.open.ac.uk> <gap-ea5abf5334-p4@usenetarchives.gap>`

```

In <357··.@mfl··o.uk>, Kevin Digweed writes:
› 
›› [Windows DLL from COBOL source stuff snipped]
…[6 more quoted lines elided]…
› 

Do you know if such DLLs are now thread-safe? A couple of years ago
I tried this on OS/2 and got "Runtime error 166" when calling into my
DLLs from a multithreaded C program.
```

###### ↳ ↳ ↳ Re: Are Cobol DLLs possible?

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea5abf5334-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ea5abf5334-p5@usenetarchives.gap>`
- **References:** `<6kk1fe$dem$1@clyde.open.ac.uk> <gap-ea5abf5334-p4@usenetarchives.gap> <gap-ea5abf5334-p5@usenetarchives.gap>`

```

sch··.@no.··m.net wrote:
› 
› In <357··.@mfl··o.uk>, Kevin Digweed  writes:
…[12 more quoted lines elided]…
› DLLs from a multithreaded C program.

Making a COBOL program thread-safe is independant to making it a DLL.
But yes, if the COBOL program is made thread-safe then the DLL it's
built into will also be thread safe provided it's running under the
thread-safe version of the COBOL RTS. This is an absolute requirement
of ISAPI and NSAPI applications, which NetExpress supports.

You got the 166 error because your COBOL program is not reentrant
(this is correct according to the ANSI standard (up to '85, anyway)).
Recursive COBOL programs (re-entrant within a single thread) have been
supported by Micro Focus for some time, and are created by declaring
some data in the "LOCAL-STORAGE SECTION".

In addition, Visual Object COBOL and now NetExpress allow COBOL
programs which are either thread-aware (and coded to be so) or are
thread-safe (compiled with the SERIAL directive, so the COBOL RTS will
ensure that only one thread enters each program at a time).

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
