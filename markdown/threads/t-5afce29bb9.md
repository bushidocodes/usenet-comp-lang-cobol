[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Use after statement in MF-COBOL

_4 messages · 4 participants · 1997-04 → 1997-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Use after statement in MF-COBOL

- **From:** "christo..." <ua-author-17073093@usenetarchives.gap>
- **Date:** 1997-04-28T10:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<862236819.27022@dejanews.com>`

```

How can I handle file errors in MF-COBOL
I tried several structures like the following, but nothing
worked...

procedure division.
declaratives.
ERROR-section.
use after standard error procedure on E11-DATEI
"code"


ERROR-end.

E11-prozedur1
...

stop run.

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Use after statement in MF-COBOL

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5afce29bb9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<862236819.27022@dejanews.com>`
- **References:** `<862236819.27022@dejanews.com>`

```

DECLARATIVES should catch errors, but there are likely cases where they
will not. I have only used them for "I/O Errors", lots of other
possibilities.

You are probably better off (but will use more code) to specifiy STATUS IS
status-variable and then examine the 2 byte status code after EACH AND
EVERY I/O VERB! Especially OPEN, CLOSE, READ, WRITE, REWRITE and START!

Note - MF-COBOL takes a somewhat liberal view of the 2nd byte of the file
status code, seems to me maybe only for values where the first byte is a
9. Unless you insist (via directive) the 2nd byte is not a normal
"character value" but it is a 1 byte binary value that represents the MF
error number. Codes 00 thru 89 are, by definition "standardized".
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

##### ↳ ↳ Re: Use after statement in MF-COBOL

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-05-05T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5afce29bb9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5afce29bb9-p2@usenetarchives.gap>`
- **References:** `<862236819.27022@dejanews.com> <gap-5afce29bb9-p2@usenetarchives.gap>`

```

RWidmer wrote:
›
› You are probably better off (but will use more code) to specifiy STATUS IS
› status-variable and then examine the 2 byte status code after EACH AND
› EVERY I/O VERB! Especially OPEN, CLOSE, READ, WRITE, REWRITE and START!
›
I agree with R. Windmer, using the FILE STATUS convention is a lot more
flexible.
However, depending on what the program is doing, it may or may not be
worth the trouble of trapping an error vs. letting the OS do the dirty
work for you. If, per se, you're doing a critical database update, which
is driven by a sequential file that probably should have been validated
ahead of time but wasn't, then use FILE STATUS and check it after every
sequential operation so you can roll-back your database in case of
problems.
I'd recommend using *one* file status variable for *all* sequential
files, code lot's of 88-levels, and see how it goes :-)
Jim Van Sickle   
Manager, Operations and Tech Support
United Retail Group. Inc.
Rochelle Park, NJ
```

#### ↳ Re: Use after statement in MF-COBOL

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5afce29bb9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<862236819.27022@dejanews.com>`
- **References:** `<862236819.27022@dejanews.com>`

```

Assuming that E11-DATEI is a file with a valid SELECT/ASSIGN and an FD, then,
the following code should work...

.
.
other divisions and sections go up here
.
.
PROCEDURE DIVISION.
DECLARATIVES.
0000-ERROR-TRAP SECTION.
USE AFTER STANDARD ERROR PROCEDURE ON E11-DATEI.
0000-ERROR.
.
.
do whatever you need to do here, but (!), don't try branching out of the
section
.
.
END DECLARATIVES.
0000-MAIN SECTION.
0000-START-PROGRAM.
.
.
program logic goes here
.
.

You've got to be careful how you label the sections and paragraphs in the
declaratives area. It causes a vector to be created, so the program branches to
the appropriate section name when an I/O error is detected. When a new section
name is encountered, the compiler generates a BR instruction to the sentence
immediately following the offending I/O verb.

For example, if you've got this code in your procedure division...

OPEN INPUT E11-DATEI.
MOVE 'HELLO' TO WS-TEXT.

If the file E11-DATEI doesn't exist, or something goes wrong with the OPEN, the
compiler generates all the necessary code to cause an immediate branch to the
0000-ERROR-TRAP section, which falls into the 0000-ERROR paragraph, executing
whatever code you have in there (the USE is a directive, so it never gets
translated into an instruction). At the end of the 0000-ERROR-TRAP section
(i.e., when the compiler finds a new section name, or encounters the END
DECLARATIVES), a BR is generated, causing the logic to branch to the MOVE verb
following the OPEN statement.

Be aware that, although you can't perform or otherwise branch out of the
declaratives area, you >can< issue a GOBACK, EXIT PROGRAM, or STOP RUN.

Hope this helps clarify the situation... :)



The Programmer Has Spoken -- SO THERE!

Chr··.@Do··u.De wrote in article <862··.@dej··s.com>...
> How can I handle file errors in MF-COBOL
> I tried several structures like the following, but nothing
…[18 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
