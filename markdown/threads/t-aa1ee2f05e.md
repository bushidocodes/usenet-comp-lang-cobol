[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting COBOL numerics to ASCII

_7 messages · 7 participants · 1999-09_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Converting COBOL numerics to ASCII

- **From:** ppoggione@my-deja.com
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sofjm$ol0$1@nnrp1.deja.com>`

```
I need to convert COBOL data imported to MS Access that contains
numeric data in the format S9(5)V99. Importing the data is no problem
but I need to run a script that will convert the trailing digit to make
the number useful. ie: 000230{

I'm not a COBOL programmer but I do understand that in this format the
decimal is implied and the last character determines both the last
digit as well as the sign of the number. Can anyone give me the mapping
for the last character? I see a lot of A's, B's, C's, {'s and }'s etc..
If someone would be kind enough to enlighten me I would greatly
appreciate it.

The sad thing is that I've done this once before about 18 months ago
but have lost the code that I used!


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Converting COBOL numerics to ASCII

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7KPH3.674$Xv.88526@news21b.ispnews.com>`
- **References:** `<7sofjm$ol0$1@nnrp1.deja.com>`

```

<ppoggione@my-deja.com> wrote in message news:7sofjm$ol0$1@nnrp1.deja.com...
> I need to convert COBOL data imported to MS Access that contains
> numeric data in the format S9(5)V99. Importing the data is no problem
…[8 more quoted lines elided]…
> appreciate it.

{ = +0     A-I = +1 thru +9
} = -0      J-R = -1 thru -9

The sign and the last digit are combined in the last character.  For
PIC S9(5)V99   and a value of "000230{" represents a value of +23.00

HTH
```

##### ↳ ↳ Re: Converting COBOL numerics to ASCII

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sq5ee$ten$1@nnrp1.deja.com>`
- **References:** `<7sofjm$ol0$1@nnrp1.deja.com> <7KPH3.674$Xv.88526@news21b.ispnews.com>`

```
In article <7KPH3.674$Xv.88526@news21b.ispnews.com>,
  "Warren Porter" <warrenp123@netdoor123.com> wrote:
>
> <ppoggione@my-deja.com> wrote in message news:7sofjm$ol0
$1@nnrp1.deja.com...
> > I need to convert COBOL data imported to MS Access that contains
> > numeric data in the format S9(5)V99. Importing the data is no
problem
> > but I need to run a script that will convert the trailing digit to
make
> > the number useful. ie: 000230{
> >
> > I'm not a COBOL programmer but I do understand that in this format
the
> > decimal is implied and the last character determines both the last
> > digit as well as the sign of the number. Can anyone give me the
mapping
> > for the last character? I see a lot of A's, B's, C's, {'s and }'s
etc..
> > If someone would be kind enough to enlighten me I would greatly
> > appreciate it.
…[9 more quoted lines elided]…
>
Use caution.  It *may* be platform specific. (Although I suspect, in
this case, that the map may be correct).
-trblshtr-
```

#### ↳ Re: Converting COBOL numerics to ASCII

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EFE104.1218@NOSPAMguysoftware.com>`
- **References:** `<7sofjm$ol0$1@nnrp1.deja.com>`

```
ppoggione@my-deja.com wrote:
> 
> I need to convert COBOL data imported to MS Access that contains
…[9 more quoted lines elided]…
> appreciate it.

As I noted in another post, there are utilities that will do this for you. ParseRat 
(http://www.guysoftware.com/parserat.htm) can handle this with its "binary" input 
option (which can handle "zoned" decimals like this as well as "packed") and its ability 
to do a /100 to get to two places of decimals.  It will export as fixed format, 
delimited, mailmerge or, more useful for your need, dBase.
```

#### ↳ Re: Converting COBOL numerics to ASCII

- **From:** "Gumbo" <gumbo@please.eatme.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p2XH3.2263$j4.65186@viper>`
- **References:** `<7sofjm$ol0$1@nnrp1.deja.com>`

```
As indicated by your posting the SIGN IS TRAILING. Assuming this follows
standards, The hig order nibble will be hexadecimal C for positive and
hexadecimal D for negative. The low order value will contain the absolute
value of the numeric value. All other digits will have a hexadecimal F in
the high order nibble and the absolute numeric value in the low order
nibble. ZERO always being stored as a positive number. The } indicates +0.

Using your example:
Display    Hexadecimal
0                    F0
0                    F0
0                    F0
2                    F2
3                    F3
}                    C0

for +0002300Display    Hexadecimal

0                    F0
0                    F0
0                    F0
2                    F2
3                    F3
???               D0

for -002300, not sure of the DISPLAY representation for hex "D0"
```

#### ↳ Re: Converting COBOL numerics to ASCII

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F1343B.B3E863BE@siber.com>`
- **References:** `<7sofjm$ol0$1@nnrp1.deja.com>`

```
ppoggione@my-deja.com wrote:
> 
> I need to convert COBOL data imported to MS Access that contains
…[9 more quoted lines elided]…
> appreciate it.

Then you can use Data2Fkat converter from Siber Systems.
It can read your Cobol data files and convert them
to CVS (comma-separated values) files that can be easily
imported into MS Access.

More info on this at http://www.siber.com/sct/datafile/

Regards,
Vadim Maslov
```

#### ↳ Re: Converting COBOL numerics to ASCII

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F06736.1DB26FFA@att.net>`
- **References:** `<7sofjm$ol0$1@nnrp1.deja.com>`

```
From IBM's "Principles of Operations":

A.1.2 Decimal Integers


Decimal integers consist of one or more decimal digits and a sign. Each
digit and the sign are represented by a 4-bit code. The decimal digits
are in binary-coded decimal (BCD) form, with the values 0-9 encoded as
0000-1001. The sign is usually represented as 1100 (C hex) for plus and
1101 (D hex) for minus. These are the preferred sign codes, which are
generated by the machine for the results of decimal-arithmetic
operations. There are also several alternate sign codes (1010, 1110, and
1111 for plus; 1011 for minus). The alternate sign codes are accepted by
the machine as valid in source operands but are not generated for
results.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
