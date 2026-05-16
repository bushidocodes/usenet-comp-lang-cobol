[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Postal Barcode /MainFrame Cobol

_4 messages · 4 participants · 2003-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Postal Barcode /MainFrame Cobol

- **From:** jdrewf <member40224@dbforums.com>
- **Date:** 2003-11-04T09:03:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3557345.1067954639@dbforums.com>`

```

Is anyone doing postal barcode in cobol ?

and if so, do you have any samples.
```

#### ↳ Re: Postal Barcode /MainFrame Cobol

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 2003-11-04T17:05:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O%Qpb.1558$773.783@newssvr22.news.prodigy.com>`
- **References:** `<3557345.1067954639@dbforums.com>`

```

"jdrewf" <member40224@dbforums.com> wrote in message
news:3557345.1067954639@dbforums.com...
>
> Is anyone doing postal barcode in cobol ?
>
> and if so, do you have any samples.
>

There is an sample program, envelope.cbl, in Liant's RM/COBOL for 32-bit
Windows that will generate POSTNET barcodes.  It uses line drawing features
that are specific to RM/COBOL to print the barcode.

For specifications of postal barcodes see chapter 4, POSTNET Barcodes in:
http://pe.usps.gov/cpim/ftp/pubs/Pub25/pub25.pdf

The basics of it is:

Postnet barcodes can represent five-(ZIP), nine-(ZIP+4), or eleven digit
(ZIP+4+Delivery Point) ZIP code information.  Each code character is made up
of five bars.  Specific combinations of two full bars and three half bars
represent digits 0 thru 9.

                 Numeric   Binary Code
                  Value       Value
                ---------  ------------
                |       |  |   74210  |
                ---------  ------------
                    1          00011        0 - half bar  1 - full bar
                    2          00101
                    3          00110
                    4          01001
                    5          01010
                    6          01100
                    7          10001
                    8          10010
                    9          10100
                    0          11000

The POSTNET bar code always begins and ends with a frame bar (Full or tall
bar).
To ensure POSTNET accuracy a correction character must included immediately
before the rightmost frame bar. The correction character is always the digit
that, when added to the sum of the other digits in the bar code, result in a
total that is a multiple of 10.
The delivery point digits in the delivery point bar code are the last two
digits in the street address.

The width of the bars must be 0.020 +/- 0.005 inches.
The height of the full bars must be 0.125 +/- 0.010 inches.
The height of the half bars must be 0.050 +/- 0.010 inches.
The space between the bars must be between 0.012 and 0.040 inches.

Five-digit   ZIP code (32 Bars)  1.245 >  < 1.625 inches
Nine-digit   ZIP code (52 Bars)  2.075 >  < 2.625 inches
Eleven-digit ZIP code (62 Bars)  2.495 >  < 3.125 inches

-Rob
```

#### ↳ Re: Postal Barcode /MainFrame Cobol

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-04T10:22:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311041022.5aca801c@posting.google.com>`
- **References:** `<3557345.1067954639@dbforums.com>`

```
How are you printing?  Printer environment etc?  I've done this using
PC printers - printing from mainframes - and using Laser printers
(Xerox) connected to mainframes.

Please tell us a little more.


jdrewf <member40224@dbforums.com> wrote in message news:<3557345.1067954639@dbforums.com>...
> Is anyone doing postal barcode in cobol ?
> 
> and if so, do you have any samples.
```

#### ↳ Re: Postal Barcode /MainFrame Cobol

- **From:** Harry Carter <hpcarter@attbi.com>
- **Date:** 2003-11-05T00:11:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6pfgqv4cs9bdptteijc280fu8sk1aquedt@4ax.com>`
- **References:** `<3557345.1067954639@dbforums.com>`

```
On Tue, 04 Nov 2003 09:03:59 -0500, jdrewf <member40224@dbforums.com>
wrote:

>
>Is anyone doing postal barcode in cobol ?
>
>and if so, do you have any samples.

We do it, but not straight from Cobol. We use Custom Statement
Formatter a Metavante product. I would suggest that you investigate
how to invoke AFP printing from Cobol.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
