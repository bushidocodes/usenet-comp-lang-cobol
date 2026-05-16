[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# START KEY EQUAL TO

_13 messages · 6 participants · 2005-06_

---

### START KEY EQUAL TO

- **From:** cblkid@yahoo.com
- **Date:** 2005-06-28T08:43:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com>`

```
I am working with a client who is using a START ...KEY IS EQUAL TO. We
are migrating the code from an MVS system to Windows. The FD for the
file is similar to:

FD Filename
 01  KEY-REC.
     05  PRIME-KEY.
         10  PK-VAR1  PIC 99.
         10  PK-VAR2  PIC X(10).
         10  PK-VAR3  PIC X(3).
         10  PK-VAR4  PIC X(2).
         10  PK-VAR5.
             15  PK-VAR5A    PIC X(2).
             15  PK-VAR5B    PIC X(4).
             15  FILLER      PIC X(10).
         10  PK-VAR6  PIC 9(4).
     05 PK-KEY1 REDEFINES PRIME-KEY PIC X(17).

They supply values for PK-KEY1 and do a START on it (START filename KEY
IS EQUAL TO PF-KEY1). They say this works on the mainframe. In the PC
environment we are receiving an error (file status '23': Record not
found). We agree with the PC version and have asked for a mainframe
output to show this working.

The logic being this is a partial key. When an EQUAL TO is used
'partial keys' can not be used. Is this correct? Can partial keys be
used when a START EQUAL TO is?

Thank you for all your insight and assistance!

Long Live COBOL!!!
```

#### ↳ Re: START KEY EQUAL TO

- **From:** docdwarf@panix.com
- **Date:** 2005-06-28T12:15:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9rt3v$sph$1@panix5.panix.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com>`

```
In article <1119973385.735390.239950@z14g2000cwz.googlegroups.com>,
 <cblkid@yahoo.com> wrote:

[snip]

>They supply values for PK-KEY1 and do a START on it (START filename KEY
>IS EQUAL TO PF-KEY1). They say this works on the mainframe. In the PC
>environment we are receiving an error (file status '23': Record not
>found). We agree with the PC version and have asked for a mainframe
>output to show this working.

Is the record in question actually there?  Can you step through a debugger 
to verify it?

DD
```

##### ↳ ↳ Re: START KEY EQUAL TO

- **From:** cblkid@yahoo.com
- **Date:** 2005-06-28T11:02:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119981727.326090.83230@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d9rt3v$sph$1@panix5.panix.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <d9rt3v$sph$1@panix5.panix.com>`

```


docdwarf@panix.com wrote:
> In article <1119973385.735390.239950@z14g2000cwz.googlegroups.com>,
>  <cblkid@yahoo.com> wrote:
…[12 more quoted lines elided]…
> DD

I tried it both ways in the debugger, with a valid partial key and an
invalid partial key. In both instances the result is status '23' which
implies to me  this is a partial key and since this is an EQUAL TO will
not be found. But then I feel I'm tainted. Would this be your
interpretation of the same status code?
```

###### ↳ ↳ ↳ Re: START KEY EQUAL TO

- **From:** docdwarf@panix.com
- **Date:** 2005-06-28T14:18:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9s49n$mv6$1@panix5.panix.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <d9rt3v$sph$1@panix5.panix.com> <1119981727.326090.83230@g44g2000cwa.googlegroups.com>`

```
In article <1119981727.326090.83230@g44g2000cwa.googlegroups.com>,
 <cblkid@yahoo.com> wrote:
>
>
…[20 more quoted lines elided]…
>interpretation of the same status code?

According to 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/6.1.8.9.1?SHELF=&DT=20020920180651&CASE=&FS=TRUE> 
a File Status of 23 indicates 'An attempt was made to randomly access a 
record that does not exist in the file, or a START or random READ 
statement was attempted on an optional input file that was not present.'

Unless the key on which you are STARTing EQUAL TO exists on the file the 
START will fail.  If you have:

01  FILEREC.
    05  PRIMARY-KEY.
        10  FIRST-HALF PIC X(05).
        10  OTHER-HALF PIC X(05).
...
01  A-FIELD PIC X(05) VALUE 'ABCDE'.
... and you code:

MOVE SPACES  TO  PRIMARY-KEY.
MOVE A-FIELD TO  FIRST-HALF.
START filnam KEY = PRIMARY-KEY
    INVALID KEY PERFORM INVALID-KEY-RITUAL.

... then unless you have a record on the file with the key of 'ABCDE     ' 
(five trailing spaces) my experience tells me that you will get a 23.

Once again: on the file which you are attempting to access is there a 
record which contains the full key on which you are STARTing?

DD
```

###### ↳ ↳ ↳ Re: START KEY EQUAL TO

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-06-28T11:34:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9s568$22n1$1@si05.rsvl.unisys.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <d9rt3v$sph$1@panix5.panix.com> <1119981727.326090.83230@g44g2000cwa.googlegroups.com> <d9s49n$mv6$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:d9s49n$mv6$1@panix5.panix.com...

> ... then unless you have a record on the file with the key of 'ABCDE     '
> (five trailing spaces) my experience tells me that you will get a 23.

That may be what actually does happen, but unless I misread the wording in
the COBOL standards, I don't think that's supposed to be what happens.

'74/'85 both say that if the operands are unequal size, comparison proceeds
as though the longer one was truncated on the right such that its length is
equal to that of the shorter (START general rule 4).

'02 says the data for comparison is moved from the FD record area into a
temporary (START general rule 17a and 17b), the information from the
associated record key in the record of the file is moved into a second
temporary (general rule 17c), and the second temporary is truncated to the
same length as the first (also gemeral rule 17c).

The comparison is always between "equal length" items, and that comparison
length is that of the comparand, not of the record key.

Have I misread something?  Have I missed something entirely?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: START KEY EQUAL TO

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-28T14:49:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9s648$9gu$1@panix5.panix.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <1119981727.326090.83230@g44g2000cwa.googlegroups.com> <d9s49n$mv6$1@panix5.panix.com> <d9s568$22n1$1@si05.rsvl.unisys.com>`

```
In article <d9s568$22n1$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message news:d9s49n$mv6$1@panix5.panix.com...
…[9 more quoted lines elided]…
>equal to that of the shorter (START general rule 4).

The operand was equal to itsself, no? KEY = PRIMARY-KEY was what I coded.

[snip]

>Have I misread something?  Have I missed something entirely?

Perhaps I should have included a SELECT specifying KEY IS PRIMARY-KEY.

DD
```

###### ↳ ↳ ↳ Re: START KEY EQUAL TO

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-06-28T11:55:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9s6e3$23d5$1@si05.rsvl.unisys.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <1119981727.326090.83230@g44g2000cwa.googlegroups.com> <d9s49n$mv6$1@panix5.panix.com> <d9s568$22n1$1@si05.rsvl.unisys.com> <d9s648$9gu$1@panix5.panix.com>`

```
Ah.  You're right.  The comparison I was talking about (which, ISTM, is what
the original poster was asking) was as if you had coded "START filnam KEY IS
EQUAL TO FIRST-HALF ... ".
In that case, the comparison would be for "ABCDE", and the remaining five
characters of PRIMARY-KEY would NOT matter, according to the various
standards.

    -Chuck Stevens

<docdwarf@panix.com> wrote in message news:d9s648$9gu$1@panix5.panix.com...
> In article <d9s568$22n1$1@si05.rsvl.unisys.com>,
> Chuck Stevens <charles.stevens@unisys.com> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:d9s49n$mv6$1@panix5.panix.com...
> >
> >> ... then unless you have a record on the file with the key of 'ABCDE
'
> >> (five trailing spaces) my experience tells me that you will get a 23.
> >
> >That may be what actually does happen, but unless I misread the wording
in
> >the COBOL standards, I don't think that's supposed to be what happens.
> >
> >'74/'85 both say that if the operands are unequal size, comparison
proceeds
> >as though the longer one was truncated on the right such that its length
is
> >equal to that of the shorter (START general rule 4).
>
…[9 more quoted lines elided]…
>
```

#### ↳ Re: START KEY EQUAL TO

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-06-28T11:17:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9s46u$221q$1@si05.rsvl.unisys.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com>`

```
I'm going to go way out on a limb here, and assume that the SELECT statement
for Filename includes ORGANIZATION INDEXED ACCESS DYNAMIC RECORD KEY IS
PRIME-KEY, and that there are no alternate keys decleared.   I'm also going
to presume that there actually exists a record in the file in which PK-VAR1,
PK-VAR2, PK-VAR3 and PK-VAR4 all match EXACTLY what you've put into the
record description of Filename immediately before the START.

The declaration of "PF-KEY1" falls in the cracks of the '74 standard syntax
rule 5:  "... data-name-1 may reference a data item specified as a record
key ... , or it may reference any data item of category alphanumeric
subrdinate to the data-name of a data item specified as a record key ...
whose leftmost character position corresponds to the leftmost character
position of that record key data item."   PF-KEY1 is NOT subordinate to
PF-KEY.  This is clarifed in the '85 standard to eliminate this ambiguity
(by eliminating the "subordinate to ..." qualification); thus, PF-KEY1
*does* produce meaningful results in '85-and-later COBOL dialects.

Presuming that the current "key of reference" is PRIME-KEY, or that the
START is attempting to establish that field as the "key of reference", I
would expect the comparison on any implementation conforming to the '85
standard to be between the first 17 characters of PRIME-KEY and the
corresponding information in the file.  If there are records satisfying that
criterion, I would not expect an error on the START.   Note that the
standards explicitly state that when the data items involved in the
comparison are of unequal length, comparison is for the length of the
*shorter* (START statement, General Rule 4 in both the '74 and '85
standards; various rules conspire to produce the same result in the '02
standard).

If all of these criteria are met and demonstrable -- PRIME-KEY is the record
key, you've valid information in PK-VAR1 through PK-VAR4, you know that at
least one record exists in the file that matches all four of these values, a
nd you still get a "23" on the START ... KEY IS EQUAL TO --  I'd have a talk
with your vendor's support folk.

ISTM that the most likely compiler bug, if compiler bug there be, is that
the code generated is doing a "normal" comparison between unequal-length
alphanumeric items, which requires *space fill* of the shorter and
comparison for the size of the longer.  That convention is expressly
COUNTERMANDED for the KEY comparisons for START in conforming COBOL
implementations by the aforementioned General Rule 4.

    -Chuck Stevens

<cblkid@yahoo.com> wrote in message
news:1119973385.735390.239950@z14g2000cwz.googlegroups.com...
> I am working with a client who is using a START ...KEY IS EQUAL TO. We
> are migrating the code from an MVS system to Windows. The FD for the
…[29 more quoted lines elided]…
>
```

##### ↳ ↳ Re: START KEY EQUAL TO

- **From:** cblkid@yahoo.com
- **Date:** 2005-06-28T12:20:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1119986444.820310.316990@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d9s46u$221q$1@si05.rsvl.unisys.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <d9s46u$221q$1@si05.rsvl.unisys.com>`

```
Chuck,

Thank you! You hit it right on the head.

My apologies for not clarifying the actual values entered as docdw
asked for. Yes the 17 characters entered were present on the file. The
START command is apparently the issue as it appears to be doing a
comparison on the full key and not the first 17 characters, not
following the '85 standard. If I supply a complete and valid key the
record is found and status is '00'.

So, based on the reply from Chuck it appears to be an issue with the
compiler and runtime. 

Thank you to all who replied!
```

###### ↳ ↳ ↳ Re: START KEY EQUAL TO

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-06-28T13:26:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9sbp4$26ku$1@si05.rsvl.unisys.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <d9s46u$221q$1@si05.rsvl.unisys.com> <1119986444.820310.316990@g44g2000cwa.googlegroups.com>`

```
And, going back to the original message, which said in part "We agree with
the PC version [which gave the I/O status value of "23"] and have asked for
a mainframe output to show this working [giving an I/O status value of
"00"]":   I think it's the PC version (compiler and runtime) whose behavior
is in question here (presuming both claim compliance with ANSI X3.23-1985 or
later), not the "mainframe" compiler and runtime.

    -Chuck Stevens

<cblkid@yahoo.com> wrote in message
news:1119986444.820310.316990@g44g2000cwa.googlegroups.com...
> Chuck,
>
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: START KEY EQUAL TO

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-06-29T02:22:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yBnwe.273051$JA.138335@fe01.news.easynews.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com> <d9s46u$221q$1@si05.rsvl.unisys.com> <1119986444.820310.316990@g44g2000cwa.googlegroups.com> <d9sbp4$26ku$1@si05.rsvl.unisys.com>`

```
I don't think we ever heard what the original PC compiler was - or if that 
compiler had "selectable" file status values.  I *know* that Micro Focus allows 
one to "choose" between '74 and '85 (possibly now '02) values.  It is POSSIBLE 
that the PC compiler is set to use non-'85 Standard values.
```

#### ↳ Re: START KEY EQUAL TO

- **From:** "John Simpson" <jasimp@earthlink.net>
- **Date:** 2005-06-28T17:26:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dgjwe.33955$%Z2.30002@lakeread08>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com>`

```

<cblkid@yahoo.com> wrote in message
news:1119973385.735390.239950@z14g2000cwz.googlegroups.com...
> I am working with a client who is using a START ...KEY IS EQUAL TO. We
> are migrating the code from an MVS system to Windows. The FD for the
…[29 more quoted lines elided]…
>

I've had problems using 'start equal'. Try 'not less than'.

John
```

#### ↳ Re: START KEY EQUAL TO

- **From:** Ubiquitous <weberm@polaris.net>
- **Date:** 2005-06-29T21:22:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i9ydnRj1CtAp1F7fRVn-hg@giganews.com>`
- **References:** `<1119973385.735390.239950@z14g2000cwz.googlegroups.com>`

```
In article <1119973385.735390.239950@z14g2000cwz.googlegroups.com>, 
cblkid@yahoo.com wrote:

>I am working with a client who is using a START ...KEY IS EQUAL TO. We
>are migrating the code from an MVS system to Windows. The FD for the
>file is similar to:

Shouldn't you use GREATER THAN OR EQUAL TO (whatever the equivalent is),
in case the key doesn't match exactly? I had a program with EQUAL that
used to mysteriously bomb out until I realized what had happened...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
