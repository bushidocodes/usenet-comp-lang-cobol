[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# convert ascii file to ebcdid on mainframe

_4 messages · 4 participants · 2005-03_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### convert ascii file to ebcdid on mainframe

- **From:** mark.ludlow@gmail.com
- **Date:** 2005-03-01T07:50:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109692229.694658.261450@o13g2000cwo.googlegroups.com>`

```
My shop is having trouble converting a ascii file to ebcdic using
simple JCL.

We have explored using the OPTCD=Q option in a IEBGENER step but we
can't get anything but tape with standard labels on it.

Anyone have a trick up their sleeve?
```

#### ↳ Re: convert ascii file to ebcdid on mainframe

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-03-01T20:17:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-182462.20171801032005@ispnews.usenetserver.com>`
- **References:** `<1109692229.694658.261450@o13g2000cwo.googlegroups.com>`

```
In article <1109692229.694658.261450@o13g2000cwo.googlegroups.com>,
 mark.ludlow@gmail.com wrote:

> My shop is having trouble converting a ascii file to ebcdic using
> simple JCL.
…[4 more quoted lines elided]…
> Anyone have a trick up their sleeve?


You could try the TCP/IP programs EZATCP04 and EXATCP05 that convert 
between ASCII and EBCDIC.  

I think IBM packages a few others as well in other products, but you are 
guaranteed to have TCP/IP at the current OS level.

Failing that, you might copy the ASCII dataset to a tape (or virtual 
tape) and the copy it back to DAST with OPTCD=Q.

Is that the same as TRTCH=Q?
```

#### ↳ Re: convert ascii file to ebcdid on mainframe

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-02T04:09:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H%aVd.3789541$f47.674287@news.easynews.com>`
- **References:** `<1109692229.694658.261450@o13g2000cwo.googlegroups.com>`

```
Does the source code ONLY include "text" data (i.e. numbers with "+" and "-" and 
"." as separate readable characters) or does it include any "COBOL-type" binary 
or packed-decimal data.  If it does include non-display numeric data conversion 
is NOT easy.  If all the stuff is text-like, then it should be medium easy. 
(Current Enterprise COBOL provides a facility for doing this via the NATIONAL-OF 
and DISPLAY-OF intrinsic functions.  Utilities probably exist as well)
```

##### ↳ ↳ Re: convert ascii file to ebcdid on mainframe

- **From:** Lawrence Greenwald <lgreenwa@cts.com>
- **Date:** 2005-03-02T07:11:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lgreenwa-E2E130.23100401032005@chiapp18.algx.net>`
- **References:** `<1109692229.694658.261450@o13g2000cwo.googlegroups.com> <H%aVd.3789541$f47.674287@news.easynews.com>`

```
In article <H%aVd.3789541$f47.674287@news.easynews.com>,
 "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> Does the source code ONLY include "text" data (i.e. numbers with "+" and "-" 
> and 
…[7 more quoted lines elided]…
> and DISPLAY-OF intrinsic functions.  Utilities probably exist as well)

OPTCD=Q only works on non-labelled tapes - "LABEL=(x,NL)" in JCL 
parlance where 'x' is the file number. It cannot be on a standard 
labelled tape because the label info will be written in EBCDIC (vs ASCII 
the data is in). You can't mix modes - EBCDIC or ASCII on a tape, not 
both and you can't write ASCII to a disk file.

I know, I'm still a mainframer and I deal with this on a regular basis.

--LG
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
