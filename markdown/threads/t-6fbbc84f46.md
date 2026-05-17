[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL AND ANONYMOUS PIPES

_3 messages · 3 participants · 1996-08_

---

### COBOL AND ANONYMOUS PIPES

- **From:** "jerome" <ua-author-9909@usenetarchives.gap>
- **Date:** 1996-08-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bb8db3$7f697260$1bcd75c2@photon.club-internet.fr>`

```

I am a C++ programmer and i made a Win95 app that needs to communicate
informations to a DOS COBOL app.
I have dÃ©cided to use Win95 anonymous pipes. So i want to lunch the cobol
dos app and pass the pipe's handle.
The cobol app is a child process of the Win95 app and inherites all the
files handles of the parent.

cmd line: cobolapp.exe 7 8 (7 is the handle of read pipe and 8 is the
handle of write pipe)

HOW CAN THE COBOL APP READ AND WRITE ON A FILE THAT HAS NO NAME BUT A
HANDLE?
----------------------------------------------------------------------------
----
PIQUOT JÃ©rÃ´me
FRANCE
(pho··.@clu··t.fr)
----------------------------------------------------------------------------
----
```

#### ↳ Re: COBOL AND ANONYMOUS PIPES

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-08-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6fbbc84f46-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bb8db3$7f697260$1bcd75c2@photon.club-internet.fr>`
- **References:** `<01bb8db3$7f697260$1bcd75c2@photon.club-internet.fr>`

```

In message <<01bb8db3$7f697260$1bc··.@pho··t.fr>> "JEROME" writes:
› informations to a DOS COBOL app.
› I have d cided to use Win95 anonymous pipes. So i want to lunch the cobol
…[8 more quoted lines elided]…
› HANDLE?

The same way as any other language: by calling DOS functions. Now
some languages (such as C) have library functions that wrap these
DOS calls, but Cobol doesn't. It is often possible to call C
functions from Cobol if appropriate 'startups' are available and
the C library is linked.

It may be that you could do a CALL "__putc" USING Char-X, StdOut.

I would suggest a simple C program to test talking on the pipes and
a simple Cobol program to test accessing the handles before going
to the production environment.
```

#### ↳ Re: COBOL AND ANONYMOUS PIPES

- **From:** "r..." <ua-author-12494308@usenetarchives.gap>
- **Date:** 1996-08-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6fbbc84f46-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bb8db3$7f697260$1bcd75c2@photon.club-internet.fr>`
- **References:** `<01bb8db3$7f697260$1bcd75c2@photon.club-internet.fr>`

```

"JEROME" writes:

› I am a C++ programmer and i made a Win95 app that needs to communicate
› informations to a DOS COBOL app.
…[3 more quoted lines elided]…
› files handles of the parent.
 
› cmd line: cobolapp.exe 7 8     (7 is the handle of read pipe and 8 is the
› handle of write pipe)
 
› HOW CAN THE COBOL APP READ AND WRITE ON A FILE THAT HAS NO NAME BUT A
› HANDLE?
As far as I know this is impossible, cause the filehandling of a Win95-
application differs from the filehandling within the dos-app.
The easiest way to work around this is to use the filename (which has to
be a short 8+3 one for the most compilers ...).

CU, Ralf.

--------------------------------------------------------------------------------
Ralf Draeger          Megacom EDV-Loesungen GmbH        Microsoft:
r.··.@meg··m.de        Zur Heupresse 4                       Where do you want to
r.··.@tn··t.de           82140 Olching                         find a bug today?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
