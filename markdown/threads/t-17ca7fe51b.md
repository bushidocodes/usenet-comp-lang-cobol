[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Duplex printing

_5 messages · 3 participants · 1997-01_

---

### Duplex printing

- **From:** "ron peterson" <ua-author-14911@usenetarchives.gap>
- **Date:** 1997-01-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32E67494.2583@mail.state.wi.us>`

```

The current laser printers have the capability
of printing duplex (IBM AFP and XEROX).

Unfortunately, COBOL has no feature to control
duplex printing to skip to a new sheet of paper.

Are there any enhancements planned to COBOL to
allow for control of a duplex printer?

I currently use AFP Page Definitions to control
duplex printing, but would like to move control
to the application program.
```

#### ↳ Re: Duplex printing

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1997-01-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17ca7fe51b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32E67494.2583@mail.state.wi.us>`
- **References:** `<32E67494.2583@mail.state.wi.us>`

```

Ron,

Fujitsu COBOL fully support Duplex Printing.

PRT-FORM
Specify a print format. The following values can be specified:
Â· P (portrait mode)
Â· L (landscape mode)
Â· LP (line printer mode)
SIZE
Specify a forms size. The following sizes can be specified:
A3, A4, A5, B4, B5, and LTR.
HOPPER
Specify a hopper to be used to feed forms. The following values can be
specified:
Â· P1 (hopper 1)
Â· P2 (hopper 2)
Â· S (sub-hopper)
Â· P (arbitrary hopper)
SIDE
Specify a print side. The following values can be specified:
Â· F (single-sided printing)
Â· B (double-sided printing)
Single-sided printing is output, however, even when B is specified.
BIND
Specify the binding direction when multiple pages are outputted
sequentially
WIDTH
Specify the binding width from 0 through 9999 (unit: 1/1440 inch).
OFFSET
Specify the offset from 0 through 9999 (unit: 1/1440 inch).

For more information see http://www.adtools.com

Fujitsu Software Corporation
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com


Ron Peterson wrote in article
<32E··.@mai··i.us>...
› The current laser printers have the capability
› of printing duplex (IBM AFP and XEROX). 
…[10 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Duplex printing

- **From:** "ron peterson" <ua-author-14911@usenetarchives.gap>
- **Date:** 1997-01-22T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17ca7fe51b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17ca7fe51b-p2@usenetarchives.gap>`
- **References:** `<32E67494.2583@mail.state.wi.us> <gap-17ca7fe51b-p2@usenetarchives.gap>`

```

Fujitsu Software Corporation wrote:
› 
› Ron,
…[32 more quoted lines elided]…
› 

This doesn't say how the write statement is modified to eject to
a new sheet of paper as compared to top-of-page.

Ron
```

#### ↳ Re: Duplex printing

- **From:** "stephen d. poe" <ua-author-8442884@usenetarchives.gap>
- **Date:** 1997-01-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17ca7fe51b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32E67494.2583@mail.state.wi.us>`
- **References:** `<32E67494.2583@mail.state.wi.us>`

```

Ron Peterson wrote:
› 
› The current laser printers have the capability
…[10 more quoted lines elided]…
› to the application program.

Ron -

Are you trying to drive the printers using:

* straight line mode data
* mixed mode (i.e., mostly line mode with IBM AFP '5a' records or Xerox
'DJDE' records mixed in)
* true IBM AFPDS or Xerox Metacode?

How to do it depends alot on which of these three environments you are
in.

If you're using AFP printers, take a look at IBM's AFP API, callable
from COBOL. See: "http://www.can.ibm.com/ibmprinters/fsafpapi.html" for
more info.

You might also want to look at
"HTTP://www.mcs.net/~raj/HTML/afpuser/afpuser.htm" and
"http://www.xplor.org/expert.html" for more info on AFP in general.

Stephen
=====================================================================
Stephen D. Poe, EDPP
Director of Research & Applied Technology
The Xenos Group
ste··.@xen··p.com
sd··.@a··.org
=====================================================================
```

##### ↳ ↳ Re: Duplex printing

- **From:** "ron peterson" <ua-author-14911@usenetarchives.gap>
- **Date:** 1997-01-27T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17ca7fe51b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17ca7fe51b-p4@usenetarchives.gap>`
- **References:** `<32E67494.2583@mail.state.wi.us> <gap-17ca7fe51b-p4@usenetarchives.gap>`

```

Stephen D. Poe wrote:
› 
› Ron Peterson wrote:
…[22 more quoted lines elided]…
› 

I want the following COBOL statements to work correctly with duplex
printers:
WRITE PRINT-LINE AFTER ADVANCING TOP-OF-NEW-PAGE.
WRITE PRINT-LINE AFTER ADVANCING TOP-OF-PAGE.
where the second statement will print on the back of a sheet of
paper.

The other requirement is that if a simplex printer is used that
there will not be any blank pages generated.

Ron
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
