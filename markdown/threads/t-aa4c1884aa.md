[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus CALL X"91" fn 35 fails in Win95

_3 messages · 3 participants · 1996-05 → 1996-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus CALL X"91" fn 35 fails in Win95

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1996-05-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<833579381snz@minfo.demon.co.uk>`

```

This test program represents part of a friend's large suite of
programs that has to run without alteration on any PC, from a 386
upwards, using DOS or Windows. It works under DOS and Windows
3.11 but fails under Windows 95 (with Animate or run as native
GNT) on the *second* use of the MicroFocus system call.

Any ideas, anyone? (MF COBOL version 3.1.31 L2.4 rev 004)

******************************************************************
* DOSCMD.CBL (modified sample program from MicroFocus) *
* Shows how to execute DOS commands from a COBOL program. *
* Copyright Micro Focus Limited 1985-93. All Rights Reserved. *
******************************************************************
IDENTIFICATION DIVISION.
PROGRAM-ID. DOSCMD.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 res-ult pic 99 comp.
01 function-35 pic 99 comp value 35.
01 null-parameter pic 99 comp value 0.
01 comm-and pic x(80).
PROCEDURE DIVISION.
* do something simple in DOS
move "dir Â¥ " to comm-and
perform until comm-and = spaces
display comm-and upon command-line
CALL X"91" USING RES-ULT, FUNCTION-35, NULL-PARAMETER
* check that free memory stays the same each time
move "mem " to comm-and
display comm-and upon command-line
* *** fails on next line in Win 95 but not in DOS or Win 3.11
CALL X"91" USING RES-ULT, FUNCTION-35, NULL-PARAMETER
* try another command
move spaces to comm-and
display "Please enter DOS command (or Enter to finish) "
accept comm-and
end-perform
stop run.

Richard Ross-Langley   +44 1727 852 801
Mine of Information Ltd,  PO BOX 1000,  St Albans AL3 5NY,  GB
=== Independent Computer Consultancy * Established in 1977 ===
```

#### ↳ Re: MicroFocus CALL X"91" fn 35 fails in Win95

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4c1884aa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<833579381snz@minfo.demon.co.uk>`
- **References:** `<833579381snz@minfo.demon.co.uk>`

```

In article <833··.@min··o.uk>, r.··.@min··o.uk says...
›
› Any ideas, anyone? (MF COBOL version 3.1.31 L2.4 rev 004)

It's working ok on the latest 16 and 32bit products as I just tried it. As
Windows 95 wasn't around when 3.1 came out maybe there is something peculier
about the way 3.1 did the DOS exec that we've now fixed.

Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

#### ↳ Re: MicroFocus CALL X"91" fn 35 fails in Win95

- **From:** "gerhard weinberger" <ua-author-5491649@usenetarchives.gap>
- **Date:** 1996-06-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4c1884aa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<833579381snz@minfo.demon.co.uk>`
- **References:** `<833579381snz@minfo.demon.co.uk>`

```

R Ross-Langley wrote:
› 
› This test program represents part of a friend's large suite of
…[9 more quoted lines elided]…
› === Independent Computer Consultancy * Established in 1977 ===

There are somw programs which causes this error: pcAnywhere32, Norton Antivirus,
... . All these programs use a driver called "SYMEVNT.386" which causes this
error.

Check your system.ini for this file. If you updated your Win31 or WFW to Win95
this driver may be left in your system.ini.

Don't call MicroFocus. They will tell you it's a Microsoft problem.
Don't call Microsoft. They will tell you it's a MicroFocus problem.

----------------------------------------
Gerhard Weinberger
Austria
Voice: ++43-7252-883
Fax: ++43-7242-883 66
EMAIL: ger··.@pr-··c.at
CIS: 100101,3515
----------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
