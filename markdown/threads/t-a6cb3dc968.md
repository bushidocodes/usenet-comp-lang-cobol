[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# microfocus cobol

_5 messages · 5 participants · 1999-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### microfocus cobol

- **From:** bigmanong@aol.com (BIGMANONG)
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990221152637.00963.00001330@ng-fa1.aol.com>`

```
Upon running my program there is an error message qoute  "STOP RUN ENCOUNTERED
WITH RETURN CODE = +00000" . How would you fix the problem. I need help.
```

#### ↳ Re: microfocus cobol

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7apvbq$m99@sjx-ixn6.ix.netcom.com>`
- **References:** `<19990221152637.00963.00001330@ng-fa1.aol.com>`

```
It sounds to be as if you have NO problem.  What makes you think that you
do?  Not every "message" is an "error message".  Is there something that
makes you think that your program has not executed as designed?
```

#### ↳ Re: microfocus cobol

- **From:** "George Zielinski" <georgezielinski@retired.airfoce.net>
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5DC9C12A1F8637AE.E978B0DE802C8E24.824D6384DF149D6A@library-proxy.airnews.net>`
- **References:** `<19990221152637.00963.00001330@ng-fa1.aol.com>`

```
That is not a problem!!  It is telling you that it has reached your STOP RUN
statement in your program.  The return code of 0000 is a successful
completion.
```

#### ↳ Re: microfocus cobol

- **From:** dnikelshpu@aol.com (DNikelshpu)
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990222135253.02874.00001549@ng-fx1.aol.com>`
- **References:** `<19990221152637.00963.00001330@ng-fa1.aol.com>`

```
In case you did not figure it out yet:

Your program ran fine, and did what you told it to...Your problem's in the
logic. Execute your program STEP by step. You should have no problem finding
exactly where your program reaches the stop run statement.
 
If you still can't figure it out let me know and I'll walk you through it.

                              Dmitry
```

#### ↳ Re: microfocus cobol

- **From:** as999@torfree.net (Adrian Boldan)
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F7KLns.AI7.0.bloor@torfree.net>`
- **References:** `<19990221152637.00963.00001330@ng-fa1.aol.com>`

```
BIGMANONG (bigmanong@aol.com) wrote:
: Upon running my program there is an error message qoute  "STOP RUN ENCOUNTERED
: WITH RETURN CODE = +00000" . How would you fix the problem. I need help.

1. Remove the STOP statement from your program.
 or
2. Delete the message :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
