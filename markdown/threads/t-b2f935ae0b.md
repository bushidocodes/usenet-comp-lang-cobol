[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP : how to read packed comp-3 fields in my pc ???

_3 messages · 3 participants · 1998-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### HELP : how to read packed comp-3 fields in my pc ???

- **From:** "News Server" <rimon@hotmail.com>
- **Date:** 1998-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o2pvh$j42$1@lnews.actcom.co.il>`

```
Hi,
Im doing some data warehouse project that includes lots of data migration
from
IBM MF to NT, Im getting Flat files from the MF and they are in EBCDIC and
comp-3.
I know the structure if the records, and I know how to translate the EBCDIC,
my only problem is how to read the comp-3 fields.
if any one can please tell me how the format works...


thank you.

Rimon.

Applicom Software Ltd.

rimon@applicom.co.il
```

#### ↳ Re: HELP : how to read packed comp-3 fields in my pc ???

- **From:** "Dave Johnson" <systemad@globalnet.co.uk>
- **Date:** 1998-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o391t$hba$4@heliodor.xara.net>`
- **References:** `<6o2pvh$j42$1@lnews.actcom.co.il>`

```
News Server wrote in message <6o2pvh$j42$1@lnews.actcom.co.il>...
>Hi,
>Im doing some data warehouse project that includes lots of data migration
…[3 more quoted lines elided]…
>I know the structure if the records, and I know how to translate the
EBCDIC,
>my only problem is how to read the comp-3 fields.
>if any one can please tell me how the format works...
…[5 more quoted lines elided]…
>


IBM Mainframe COMP-3 also known as packed data (PD) because,
amazingly, the data is (or are) packed! Works like this........

Each digit occupies 1/2 byte (4 bits) and the last 4 bits are used for the
sign. A PD field can only be a full number of bytes, so if you specify an
even number of digits, the compiler assumes a leading zero.

The IBM normally uses 'C' for a positive sign, 'D' for a negative (there
are some packages which use 'F' for positive, but this is treated as a
'C' for arithmetic compares. If you don't declare the field as signed, I
believe a 'C' is assumed (I would stand correction on that, may be 'F').

Examples:

Assuming a field defined as PIC S9(7) COMP-3   (4 bytes)......

+123456   would be held as  x'0123456C'
-123456    would be held as  x'0123456D'

For a larger field PIC S9(11) COMP-3  (6 bytes)

+123456  would be held as  x'00000123456C'
-123456  would be held as   x'00000123456D'

(hope I counted them correctly).

One thing to note - a PD field does not hold the decimal place - this
is defined as a 'V' in the picture (eg PIC S9(5)V99 which will hold 7
digits, and will perform the alignment on arithmetic operations and
decimal moves). So if the first example was S9(5)V99 instead of
S9(7), the actual value would be +/- 1234.56.

Hope that helps,
DaveJ.
```

#### ↳ Re: HELP : how to read packed comp-3 fields in my pc ???

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35A8DC4E.CE7B4C5@zip.com.au>`
- **References:** `<6o2pvh$j42$1@lnews.actcom.co.il>`

```
Rimon,

I know that you said that you know how to convert from EBCDIC but just
in case:  If you translate using FTP or whatever the COMP-3 fields will
be lost forever.  The translation from EBCDIC to ASCII will make the
data very unreadable.

I hope that you are doing a binary transfer and reading it internally in
your conversion program, in this case Dave's infomation will work for
you.n

Good luck
Ken


News Server wrote:
> 
> Hi,
…[14 more quoted lines elided]…
> rimon@applicom.co.il
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
