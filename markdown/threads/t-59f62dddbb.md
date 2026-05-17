[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL2 Debugging

_2 messages · 2 participants · 1995-08_

---

### COBOL2 Debugging

- **From:** "abe..." <ua-author-17087582@usenetarchives.gap>
- **Date:** 1995-08-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vmgjb$bi6@news.ios.com>`

```
Question for all those cobol wizards out there. How does one debug a
cobol2 program w/out abend aid? Does FDUMP really do the job? Does the
interactive debugger clist work? We're just getting started on a very
large cob 2 project and it's not the same as using state and flow in the
options. Anyone?
```

#### ↳ Re: COBOL2 Debugging

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-08-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-59f62dddbb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3vmgjb$bi6@news.ios.com>`
- **References:** `<3vmgjb$bi6@news.ios.com>`

```
For either VS COBOL II or COBOL/370 (renamed last year to "IBM
COBOL for MVS & VM" - there are several "debugging" issues that
you should think about (unfortunately, NONE with "easy" answers).

1) Why start a new project using VS COBOL II? It is a
strategically stabilized product - and you should be looking at
doing new development with COBOL/370 (aka COBOL for MVS & VM) -
which require LE as the run-time system.

2) Are you aware that the OPT/NOOPT compiler options
SIGNIFICANTLY changes the object code created? The last time
that I checked (when working for a former employer) XPEDITER was
the *only* mainframe debugging tool that really (or sort-of)
could handle OPTIMIZED code - everything else required that you
compile with NOOPT to debug your programs - which meant that what
you run in production was different from what you run during
testing. This is always a "scary" option in my opinion.

3) FDUMP isn't real bad and the LE "CEETEST" (or CEE3DMP)
features are OK. They certainly beat getting an ESA system dump.
I think the real question is whether you are talking about the
development/debugging stage - or are you talking about what to do
in the middle of the night/middle of production run. I sure
wouldn't want to face the latter without SOME "production"
debugging support (such as Abend/AID or one of its competitors).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
