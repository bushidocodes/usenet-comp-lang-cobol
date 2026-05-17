[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL in Unix -- getting a ksh shell variable: How?

_3 messages · 3 participants · 1996-12 → 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL in Unix -- getting a ksh shell variable: How?

- **From:** "spk..." <ua-author-17071408@usenetarchives.gap>
- **Date:** 1996-12-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5aa5ad$qii@newsfeed.cts.com>`

```

I have RTFM'd til I'm blue in the face... so then I tried coding a bunch of
guesses...

I would certainly appreciate if some kind soul could tell me how to obtain the
value of a ksh shell variable from within MF COBOL? Here's what I have so
far:

=======================================
Script started on Mon Dec 30 15:11:18 1996
$ cat -n get-env.cbl
1 IDENTIFICATION DIVISION.
2 PROGRAM-ID. skel.
3 ENVIRONMENT DIVISION.
4 CONFIGURATION SECTION.
5 SPECIAL-NAMES.
6 ENVIRONMENT-NAME is ENV ENVIRONMENT-VALUE is the-env.
7 INPUT-OUTPUT SECTION.
8 FILE-CONTROL.
9 DATA DIVISION.
10 WORKING-STORAGE SECTION.
11 01 it-x.
12 05 it pic x(10).
13
14 PROCEDURE DIVISION.
15 INIT.
16 accept it from the-env.
17 display "env:" it ":".
18 STOP RUN.
19
20 9999-END. EXIT.
$ export ENV="xxx"
$ echo "ENV is " $ENV
ENV is xxx
$ get-env
env: :
$ ^D
script done on Mon Dec 30 15:11:24 1996

Homepage at http://www.users.cts.com/crash/s/spkemp
```

#### ↳ Re: MF COBOL in Unix -- getting a ksh shell variable: How?

- **From:** "greg lindholm" <ua-author-17072220@usenetarchives.gap>
- **Date:** 1996-12-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1c8c8cf35-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5aa5ad$qii@newsfeed.cts.com>`
- **References:** `<5aa5ad$qii@newsfeed.cts.com>`

```

Steve Kemp wrote:
› 
› I have RTFM'd til I'm blue in the face... so then I tried coding a bunch of
…[37 more quoted lines elided]…
› Homepage at  http://www.users.cts.com/crash/s/spkemp

Nice try but you would never figure it out from the docs.
This is what you need to do:

DISPLAY "ENV" UPON ENVIRONMENT-NAME.
ACCEPT it FROM ENVIRONMENT-VALUE.

and get rid of the SPECIAL-NAMES stuff.
```

#### ↳ Re: MF COBOL in Unix -- getting a ksh shell variable: How?

- **From:** "charles henry" <ua-author-2492697@usenetarchives.gap>
- **Date:** 1997-01-02T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1c8c8cf35-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5aa5ad$qii@newsfeed.cts.com>`
- **References:** `<5aa5ad$qii@newsfeed.cts.com>`

```



Steve Kemp wrote in article
<5aa5ad$q.··.@new··s.com>...
›
› I would certainly appreciate if some kind soul could tell me how to
› obtain the
› value of a ksh shell variable from within MF COBOL?

Steve,

I don't know what version of MF Cobol you are using, but I am using 3.1 and
here is how it works for me: (This will get the value of an environment
variable named "IT")

WORKING-STORAGE SECTION.
77 IT-WS PIC X(10).
PROCEDURE DIVISION.
....
DISPLAY "IT" UPON ENVIRONMENT-NAME.
ACCEPT IT-WS FROM ENVIRONMENT-VALUE.

In an older version, this worked:

WORKING-STORAGE SECTION.
77 PERM-POINTER USAGE POINTER.
01 IT-NAME.
05 FILLER PIC X(2) VALUE "IT".
05 FILLER PIC X VALUE X"00".
05 FILLER PIC X(17) VALUE SPACES.
01 IT-WS PIC X(80).
01 IT-STRING PIC X(80).

PROCEDURE DIVISION.
MAIN-PARA.
CALL "cobgetenv" USING IT-NAME
RETURNING PERM-POINTER.
IF PERM-POINTER NOT = NULL
SET ADDRESS OF IT-STRING TO PERM-POINTER
MOVE SPACES TO IT-WS
UNSTRING IT-STRING DELIMINITED BY LOW-VALUES
INTO IT-WS
DISPLAY "IT=" IT-WS.

I hope this helps

Charles Henry
Programmer/Analyst
Escambia County Tax Collector's Office
Pensacola, Florida
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
