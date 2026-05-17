[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using the printer in dos

_3 messages · 3 participants · 1996-09_

---

### Using the printer in dos

- **From:** "jl..." <ua-author-17072453@usenetarchives.gap>
- **Date:** 1996-09-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0_0/0_0_24271778@fidonet.org>`

```

Hello !

A relative; taking pity on me, donated her books and
RM/COBOL-85 (dos- student version) compiler to me to
help me with my COBOLII course. It is really nice,
and I have already written McFarland to find out more
about their products.

However, I am having a problem, and haven't been able
to find the answer in any of the books that she gave me.
The following is a simple program we used in class
to get used to using xedit and compiling a COBOLII
program at school. It works well at home also, but does not
print the results, it creates a file called
LISTING on the drive instead. Is this a problem with
the code, or a limitation of the student version
of compiler I am using?



IDENTIFICATION DIVISION.

PROGRAM-ID. PROGRAM1.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.

INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT LISTING ASSIGN TO PRINTER.

DATA DIVISION.
FILE SECTION.
FD LISTING LABEL RECORDS ARE OMITTED.
01 PRINT-REC.
02 LINE-OUT PIC x(80).

PROCEDURE DIVISION.
100-MAIN-MODULE.
OPEN OUTPUT LISTING.
MOVE SPACES TO PRINT-REC.

MOVE " IT WORKS!! " TO PRINT-REC.
WRITE PRINT-REC.
CLOSE LISTING.
STOP RUN.



Thanks in advance!


Joe
---
* Origin: (0:0/0)
```

#### ↳ Re: Using the printer in dos

- **From:** "uwe baemayr" <ua-author-6588910@usenetarchives.gap>
- **Date:** 1996-09-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f242bc03ae-p2@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_24271778@fidonet.org>`
- **References:** `<0_0/0_0_24271778@fidonet.org>`

```

jl··.@pro··g.net wrote:

> Hello !
>
…[14 more quoted lines elided]…
> of compiler I am using?

Use this:

SELECT LISTING ASSIGN TO PRINT, "PRINTER".

------------------------------------------------------------------------
| Uwe Baemayr | E-mail: u.··.@li··t.com |
| Ryan McFarland Corporation | or: jea··.@ccw··s.edu |
| -- a division of Liant Software | Compuserve: 74774,47 / GO LIANT |
------------------------------------------------------------------------
```

#### ↳ Re: Using the printer in dos

- **From:** "lo..." <ua-author-1109403@usenetarchives.gap>
- **Date:** 1996-09-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f242bc03ae-p3@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_24271778@fidonet.org>`
- **References:** `<0_0/0_0_24271778@fidonet.org>`

```

jl··.@pro··g.net wrote:

› Hello !
 
› A relative; taking pity on me, donated her books and
› RM/COBOL-85 (dos- student version) compiler to me to
› help me with my COBOLII course. It is really nice,
› and I have already written McFarland to find out more
› about their products.
 
› However, I am having a problem, and haven't been able
› to find the answer in any of the books that she gave me.
…[6 more quoted lines elided]…
› of compiler I am using?



›       IDENTIFICATION DIVISION.
 
›       PROGRAM-ID. PROGRAM1.
 
›       ENVIRONMENT DIVISION.
›       CONFIGURATION SECTION.
 
›       INPUT-OUTPUT SECTION.
›       FILE-CONTROL.
›              SELECT LISTING ASSIGN TO PRINTER.
 
›       DATA DIVISION.
›       FILE SECTION.
›       FD LISTING       LABEL RECORDS ARE OMITTED.
›       01 PRINT-REC.
›          02 LINE-OUT                    PIC x(80).
 
›       PROCEDURE DIVISION.
›       100-MAIN-MODULE.
›           OPEN OUTPUT LISTING.
›           MOVE SPACES TO PRINT-REC.
 
›           MOVE   "        IT WORKS!!           "  TO PRINT-REC.
›           WRITE PRINT-REC.
›           CLOSE LISTING.
›           STOP RUN.



› Thanks in advance!
 
 
›           Joe
› ---
› * Origin:  (0:0/0)

Hi there. You might want to try using:

SELECT LISTING ASSIGN TO "LPT1:"

in place of what you currently have. Also, you might want to make
sure LISTING isn't being used by your compiler for something else.

Good Luck.
Ego.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
