[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Input

_3 messages · 3 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Input

- **From:** "robert robbins" <ua-author-2694790@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3506EF70.E87C9754@sunlink.net>`

```

COBOL Gurus,
Screen input in my programs is very annoying
because the
ACCEPT variable statement requires every character to be entered for
a PIC X(30) even if half of the characters are spaces. Is there any way
to
input just the data without having to count spaces as I type?

Robert Robbins
```

#### ↳ Re: Fujitsu Input

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d98f55ac-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3506EF70.E87C9754@sunlink.net>`
- **References:** `<3506EF70.E87C9754@sunlink.net>`

```

Robert Robbins wrote:
› COBOL Gurus,
›                         Screen input in my programs is very annoying
…[4 more quoted lines elided]…
› input just the data without having to count spaces as I type?

Clear the input area to spaces before you ACCEPT.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: Fujitsu Input

- **From:** "dana brasie" <ua-author-17072364@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d98f55ac-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3506EF70.E87C9754@sunlink.net>`
- **References:** `<3506EF70.E87C9754@sunlink.net>`

```

I don't know why there is a difference since "console is the default
device, but If you explicitly state the input device as console you can
enter 'ABC' and and Test-Var will contain 'ABC '. However, if
you don't explicitly state "From Console" the system will wait for you until
you have entered 10 characters.


Program to test behavior of "accept":

IDENTIFICATION DIVISION.
PROGRAM-ID. CONSOLE-TEST.
DATA DIVISION.
WORKING-STORAGE SECTION.

01 TEST-VAR PIC X(10) VALUE SPACES.
01 CHOICE PIC X(01) VALUE SPACE.

PROCEDURE DIVISION.
DISPLAY 'TEST USING "FROM CONSOLE" (Y/N): '
WITH NO ADVANCING.
ACCEPT CHOICE FROM CONSOLE.

DISPLAY 'ENTER CONSOLE TEST VARIABLE: ' WITH NO ADVANCING.
IF FUNCTION UPPER-CASE(CHOICE) = 'Y'
ACCEPT TEST-VAR FROM CONSOLE
ELSE
ACCEPT TEST-VAR
END-IF.

DISPLAY 'YOUR INPUT = <' TEST-VAR '>'.

STOP RUN.


Robert Robbins wrote in message <350··.@sun··k.net>...
› COBOL Gurus,
›                        Screen input in my programs is very annoying
…[8 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
