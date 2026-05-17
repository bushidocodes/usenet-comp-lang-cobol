[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comp3 Numbers

_6 messages · 6 participants · 1996-06 → 1996-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Comp3 Numbers

- **From:** "tad..." <ua-author-15664034@usenetarchives.gap>
- **Date:** 1996-06-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31d821f5.11873593@news.earthlink.net>`

```

I currently am involved in a project where I must translate
information from a Btrieve file into a text file for use in a
mainframe system using COBOL. I'm a C++ programmer and haven't the
foggiest idea on how to impliment _SIGNED_ packed-decimal numbers.

Can anybody offer any help? I currently am able to reproduce the
unsigned numbers, but can't figure out where the sign or sign bit
goes.

Thanks in advance!

Tim Adamec.
---------------------------------------------
PGP AVAILABLE UPON REQUEST
---------------------------------------------
I don't care what you say about Clinton,
but his friends have convictions!!!
---------------------------------------------
http://home.earthlink.net/free/tadamec/
```

#### ↳ Re: Comp3 Numbers

- **From:** "the vaxman!" <ua-author-17087128@usenetarchives.gap>
- **Date:** 1996-06-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdde699b12-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31d821f5.11873593@news.earthlink.net>`
- **References:** `<31d821f5.11873593@news.earthlink.net>`

```

Tim Adamec wrote:
› 
› I currently am involved in a project where I must translate
…[17 more quoted lines elided]…
›    http://home.earthlink.net/free/tadamec/

comp-3, or packed numbers, store the sign in the least significant
position. So, +813 will take up two bytes and be stored as X'813C',
while -7145 is stored as X'07145D', occupying three bytes.
```

#### ↳ Re: Comp3 Numbers

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdde699b12-p3@usenetarchives.gap>`
- **In-Reply-To:** `<31d821f5.11873593@news.earthlink.net>`
- **References:** `<31d821f5.11873593@news.earthlink.net>`

```

tad··.@ear··k.net (Tim Adamec) wrote:

› I currently am involved in a project where I must translate
› information from a Btrieve file into a text file for use in a
› mainframe system using COBOL.  I'm a C++ programmer and haven't the
› foggiest idea on how to impliment _SIGNED_ packed-decimal numbers.
 
› Can anybody offer any help? I currently am able to reproduce the
› unsigned numbers, but can't figure out where the sign or sign bit
› goes.
 
› Thanks in advance!
 
› Tim Adamec.
› ---------------------------------------------
…[5 more quoted lines elided]…
›   http://home.earthlink.net/free/tadamec/

Sure; in the dark days of limited memory and storage capacities for
IBM mainframes (yes - at one time this was indead true ;-), tricks
evolved to make as much use of that limited capacity as possible. One
of which is compressing numbers since the first nibble of any EBCDIC
numeric byte is 1111. So packed-decimal numerics were born.

To code a packed-decimal field you code one of the following:

01 WS-NUMBER PIC S9(5)V99 COMP-3 VALUE +0.
(OS/VS COBOL style)

-or-

01 WS-NUMBER PIC S9(5)V99 PACKED-DECIMAL VALUE +0.
(optional ANSI COBOL 2 and beyond style)

But there is a subtle "got-ya" with this in calculating your record
length. The PIC's represent what the number size in it's UNPACKED
form, not what is actually in the record image. You use a
rule-of-thumb to calculate the packed-decimal field's true size for
determining the record length. The rule is:

COMPUTE PACKED-NUMBER-SIZE = PIC-NUMBER-SIZE / 2 + 1.
(Sorry, couldn't resist seeing you are a native C programmer)

All math is in integer form so drop the decimals. Do not include
signs in the field length.

examples:

PIC S9(04) COMP-3 VALUE +1234 gives hex "01 23 4C", and filling three
bytes in the record image. It would be hex "F1 F2 F3 C4" and filling
four bytes if it were in display form.

PIC S9(04) COMP-3 VALUE -1234 gives hex "01 23 4D", filling three
bytes in the record image.

PIC S9(05)V99 COMP-3 VALUE +98765.43 gives hex "98 76 54 3C" and
filling four bytes in the record image. It would be hex "F9 F8 F7 F6
F5 F4 C3" and filling seven bytes if it were in display form.

PIC 9(04) PACKED-DECIMAL VALUE 1234 gives hex "01 23 4F" and filling
four bytes.

BTW, if your PIC is even numbered, add one to it. As you can see the
compiler computes the number in nibbles of two. So PIC S9(05) COMP-3
VALUE +1234 gives hex "01 23 4C" just as well.
Hope this helps
Boyce Williams
```

#### ↳ Re: Comp3 Numbers

- **From:** "bele" <ua-author-13442324@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdde699b12-p4@usenetarchives.gap>`
- **In-Reply-To:** `<31d821f5.11873593@news.earthlink.net>`
- **References:** `<31d821f5.11873593@news.earthlink.net>`

```

tad··.@ear··k.net (Tim Adamec) wrote:
› I currently am involved in a project where I must translate
› information from a Btrieve file into a text file for use in a
› mainframe system using COBOL.  I'm a C++ programmer and haven't the
› foggiest idea on how to impliment _SIGNED_ packed-decimal numbers.
› 

The sign is held in a separate trailing digit (half-character)
position; that is, at the right-hand or least significant end
of the data item.

Sign of data item value: + --> sign half-character x"0C"
Sign of data item value: - --> sign half-character x"0D"

Greetings, Bert Leest
```

#### ↳ Re: Comp3 Numbers

- **From:** "neil duffee" <ua-author-5508101@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdde699b12-p5@usenetarchives.gap>`
- **In-Reply-To:** `<31d821f5.11873593@news.earthlink.net>`
- **References:** `<31d821f5.11873593@news.earthlink.net>`

```

Tim Adamec wrote:
›  ----->  text deleted  <-----
› foggiest idea on how to impliment _SIGNED_ packed-decimal numbers.
…[3 more quoted lines elided]…
› goes.

If you can produce unsigned, packed-decimal numbers then you have
solved 98% of the problem. IBM's packed decimal uses a hexadecimal
'F' in the sign location to indicate the number is to be interpreted
as unsigned ie. '123F'H. A signed, packed-decimal field carries a
'C' for positive and a 'D' for negative numbers in the same location
ie. '123C'H and '123D'H.
---------------> signature = 3 lines follows <-------------------
Neil Duffee, Joe Code Grinder, U d'Ottawa, Ottawa, Ontario, Canada
mailto:nj··.@uot··a.ca or http://www.uottawa.ca/~njd2e
"How *do* you plan for something like that?" Guardian Bob, Reboot
```

#### ↳ Re: Comp3 Numbers

- **From:** "pm..." <ua-author-8578979@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdde699b12-p6@usenetarchives.gap>`
- **In-Reply-To:** `<31d821f5.11873593@news.earthlink.net>`
- **References:** `<31d821f5.11873593@news.earthlink.net>`

```

Greetings Tim:

tad··.@ear··k.net (Tim Adamec) wrote:

› I currently am involved in a project where I must translate
› information from a Btrieve file into a text file for use in a
› mainframe system using COBOL.  I'm a C++ programmer and haven't the
› foggiest idea on how to impliment _SIGNED_ packed-decimal numbers.
 
› Can anybody offer any help? I currently am able to reproduce the
› unsigned numbers, but can't figure out where the sign or sign bit
› goes.

Unless the source code specified the sign to be separate, then the sign
is a part of the last digit as an "overpunch". That last letter needs
to be translated into both the last digit and the sign of the entire
number.

To make matters more interesting, different compilers will use different
overpunch symbols (I know from doing conversion from Ryan McFarland
COBOL to AccuCOBOL that the overpunches for each are different).

Do you know which compiler that was used to create the data files? I
have manuals for both RM and Accu.
===============================================================
Peter Perchansky
PMP Computer Solutions
http://ourworld.compuserve.com/homepages/pmp_computer_solutions
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
