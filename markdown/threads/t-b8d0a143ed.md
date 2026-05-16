[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Old Mainframe program

_3 messages · 3 participants · 1998-09 → 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Old Mainframe program

- **From:** "William R. Fink" <bfink@apci.net>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uqqdo$ate@mhstl1.monsanto.com>`

```
About 15 years ago, someone printed out a picture of the Moon and the Mona
Lisa using an IBM mainframe printer.  I have long since lost these printouts
and wish to recover them.  Has anyone ever heard of these?  If so, could you
reproduce the output ( or send me the program) ?

These picture were text-based and could only be recognized from about 5 feet
from the listing; otherwise, it looked like a bunch of letters and numbers
printed on the green-bar paper.


Bill
```

#### ↳ Re: Old Mainframe program

- **From:** bwspoor@fridaycs.win-uk.net (B W Spoor)
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<21@fridaycs.win-uk.net>`
- **References:** `<6uqqdo$ate@mhstl1.monsanto.com>`

```
 
In article <6uqqdo$ate@mhstl1.monsanto.com>, "William R. Fink" (bfink@apci.net) writes:
>About 15 years ago, someone printed out a picture of the Moon and the Mona
>Lisa using an IBM mainframe printer.  I have long since lost these printouts
…[7 more quoted lines elided]…
>
I remember them from when I worked on ICL mainframes - they were
'engineer test programs' supposedly for testing the printers.

There were several, including (if I remember correctly) one that
printed a calender.

Unfortunately, I never managed to aquire copies and even if I had, I
doubt that the 1900 series binaries would run on anything available
today - pity I liked the machine. We only saw them as binaries -
AFAIK sources weren't issued to the field engineers.

Brian
 

-----------------------------------------------------------
Brian W Spoor MBCS
Chartered Information Systems Practitioner
Friday Computer Services          Phone: +44-(0)1803 852625
bwspoor@fridaycs.co.uk            Fax:   +44-(0)1803 854926
-----------------------------------------------------------
```

#### ↳ Re: Old Mainframe program

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdece0$253fa780$6ad0ba89@tims>`
- **References:** `<6uqqdo$ate@mhstl1.monsanto.com>`

```
At the place where I once work, these pictures were each a member in a
directory file with a record length of 133 chars.  The first character of
each line was the carriage control.  For each printed line of Mona it may
have taken 4 lines from the data file.  We used iebgener to print it.  To
recreate it, you need a printer that uses the carriage control otherwise
you are out of luck.  Oh yeah, the 4 lines would be printed on top of each
other, before advancing one paper print line.

Tim............................. 

William R. Fink <bfink@apci.net> wrote in article
<6uqqdo$ate@mhstl1.monsanto.com>...
> About 15 years ago, someone printed out a picture of the Moon and the
Mona
> Lisa using an IBM mainframe printer.  I have long since lost these
printouts
> and wish to recover them.  Has anyone ever heard of these?  If so, could
you
> reproduce the output ( or send me the program) ?
> 
> These picture were text-based and could only be recognized from about 5
feet
> from the listing; otherwise, it looked like a bunch of letters and
numbers
> printed on the green-bar paper.
> 
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
