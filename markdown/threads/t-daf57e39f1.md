[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# C calling MF-COBOL

_1 message · 1 participant · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### C calling MF-COBOL

- **From:** "wolfgang grossbauer" <ua-author-12437406@usenetarchives.gap>
- **Date:** 1998-03-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f3hvh$pte$1@news.Austria.EU.net>`

```

Hi there,
I have the following problem: have linked the MicroFocus COBOL runtime to a
new runtime , using cob -xe "" and so on. This is on a UNIX SVR4.
The main-C-program does a
cobcall("CBL_ERROR_PROC"...); and cobcall ("CBL_END_PROC"...); to provide
own error and end routines (clean up RDBMS interface, etc).
Later in the coding a
cobcall("batchprogram",...);
executes a batchprogram.
So far so good, everything works as it should, BUT
sometimes, in the CBL_EXIT_PROC-function, AFTER , I receive .
I need to the CBL_END_PROC-function, as otherwise the exit-code
of would not be set to the return code possibly set in the
executed batch program (STOP RUN RETURNING nnn.).
The C-runtime also traps Sig11, and I do perform some informational messages
and exit the process with . This should terminate the entire
process - but big surprise - it appears that another process is
involved, as the exit-code of is 11, apparently from the Sig 11.
This problen occurs definitely AFTER of the batch program, and
occurs also very seldom, so the correct execution of the program is granted,
but I am curious if somebody has an idea.
Thanks, Wolfgang Grossbauer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
