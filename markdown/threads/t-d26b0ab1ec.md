[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Diff in processing between S/390 and Intel

_4 messages · 2 participants · 2005-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Diff in processing between S/390 and Intel

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-02-02T15:54:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107388455.874579.138360@g14g2000cwa.googlegroups.com>`

```
I am trying to process records that I've pulled over from a VSE system
through to a z/OS system and then downloaded (EBCDIC to ASCII) to my
laptop. I am using an SPF look-a-like under Windows. And I'm using the
FJ COBOL97 on my W/2K system.

The problem that I'm having with these records is that some of them
come through as 80 characters and some come through as 80+n (where n is
1 to 4).

Now I'm using the following SELECT & FD for the input data:

006500     SELECT VSE-INPUT-FILE      ASSIGN TO QSAM-SYSIN
006600*--------------------------------------------------------------*

006700* $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $

006800*  M/S ONLY    M/S ONLY    M/S ONLY    M/S ONLY

006900                                 ORGANIZATION LINE SEQUENTIAL

007000* $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $

007100*--------------------------------------------------------------*

007200                                 FILE STATUS IS SOURCE-STATUS.
~~~~~~
~~~~~~
008800 FD  VSE-INPUT-FILE
008900     BLOCK CONTAINS 0 RECORDS.
009000 01  VSE-BASE-RECORD             PIC X(080).
009100

I just added the LINE SEQUENTIAL clause and things seem to kinda be
better, but I'm still having problems.

I've also put out the input data to a "printer" file and I've added 1
character to the output line of "|" at the expected byte just past the
input data with a MOVE statement. Well, that character is NOT there! It
is not on the output line.

05 VSE-SOURCE-REC  PIC X(80).
05 END-DATA-MARKER PIC X.

MOVE "|" TO END-DATA-MARKER.

Now we know the data is fixed blocked under VSE. And I've had a few
problems with it in using the SPF product until I defined the profile
as variable (and put that into a second file).

What I am thinking is happening is, the CRLF that's embedded at the end
of each record is actually causing SPF a problem when it is told a
profile that is FIXED. And then the COBOL I/O routine also "wraps" the
records (so it appears).

Any one have any idea of what I'm staring at and just not seeing? And I
don't care about the editor, I care about the COBOL program because I
have to fix it to work in three different environments (VSE, z/OS, and
Windoze). Obviously I'm not having this problem under the S/390
environments.

Later
Steve.T
```

#### ↳ Re: Diff in processing between S/390 and Intel

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-02-02T16:17:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107389863.911980.233310@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1107388455.874579.138360@g14g2000cwa.googlegroups.com>`
- **References:** `<1107388455.874579.138360@g14g2000cwa.googlegroups.com>`

```
OK, before the guns start firing, I found the reason why the "|" didn't
show up. I confess, I moved it to follow the perform of the output
paragraph rather than just in front of it. You know, one of those
little tweaks that somebody interrupts you while you're doing it kinda
things just so you look dumb to everyone when the results are all
wrong.

But I'm still getting 1 to 2 blank inputs at times! And I know that all
the records have data in them, because there's only 8 of 'em. But my
quickie validation report is showing 16! Only two records come out back
to back w/o a "blank" record between them.

Later,
Steve.T

[I know I'm gonna feel real dumb when I get to what's wrong. This is
starting to feel like one of those "make me feel stupid" bugs.]
```

##### ↳ ↳ Re: Diff in processing between S/390 and Intel

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-02-02T17:30:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107394237.917791.153630@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1107389863.911980.233310@z14g2000cwz.googlegroups.com>`
- **References:** `<1107388455.874579.138360@g14g2000cwa.googlegroups.com> <1107389863.911980.233310@z14g2000cwz.googlegroups.com>`

```
I told ya.

CTC's SPF editor that I'm using (SPF/SE 3.5) behaves very differently
from the prior versions that supported REXX. And so when it autobuilt
the profile to handle the 80 byte data I was looking at, it
automatically expanded it to 255 characters....

Doncha just love it when the tools are what screw you up?
Later,
Steve.T
```

##### ↳ ↳ Re: Diff in processing between S/390 and Intel

- **From:** epc8@juno.com
- **Date:** 2005-02-02T17:31:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107394305.788706.162270@g14g2000cwa.googlegroups.com>`
- **References:** `<1107388455.874579.138360@g14g2000cwa.googlegroups.com> <1107389863.911980.233310@z14g2000cwz.googlegroups.com>`

```

steve.t wrote:
> OK, before the guns start firing, I found the reason why the "|"
didn't
> show up. I confess, I moved it to follow the perform of the output
> paragraph rather than just in front of it. You know, one of those
> little tweaks that somebody interrupts you while you're doing it
kinda
> things just so you look dumb to everyone when the results are all
> wrong.
>
> But I'm still getting 1 to 2 blank inputs at times! And I know that
all
> the records have data in them, because there's only 8 of 'em. But my
> quickie validation report is showing 16! Only two records come out
back
> to back w/o a "blank" record between them.
>
…[4 more quoted lines elided]…
> starting to feel like one of those "make me feel stupid" bugs.]

This really sounds like an un-intended character translation somewhere.
Either in the EBCDIC to ASCII or perhaps in reading binary (or packed)
data as text. Maybe you have a X'0d', X'0a' or X'00' in there that is
getting gobbled?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
