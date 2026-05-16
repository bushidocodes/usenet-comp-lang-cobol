[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# translate from EBCDIC to ASCII

_4 messages · 4 participants · 2000-02 → 2000-03_

---

### Re: translate from EBCDIC to ASCII

- **From:** Fergus Allan <allanfw@bikebits.bt.co.uk>
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B50854.534429F5@bikebits.bt.co.uk>`
- **References:** `<MPG.1317fe99f30f3e8598986e@news.mersinet.co.uk> <20000219193400.08112.00000694@nso-ce.aol.com>`

```
I am currently processing a file which started as ebcdic and translated on th fly
when transferred from the mainframe.  The file contains signed and COMP-3 fields.
My program converts the fields back to ebcdic.  Are you suggesting that the
mainframe will have changed the representation of the comp-3 fields so that, even
converting the information back to ebcdic is insufficient?

It is true, however that the values I am processing are not correct.  This may be
because of the above problem.  It may be becaues I am not not processing the value

correctly.  The information I have regarding COMP-3 is that it is binary coded
decimal (BCD), thus I am breaking the byte value into
2 nibbles annd, finally, to display this as ascii translating the nibble (0 ->'0',

1 -> '1' ... 15 -> 'F')

Sff5ky wrote:

> In article <MPG.1317fe99f30f3e8598986e@news.mersinet.co.uk>, Charles F Hankel
> <charles@hankel.mersinet.co.uk> writes:
…[22 more quoted lines elided]…
> from EBCDIC to ASCII or ASCII to EBCDIC.
```

#### ↳ Re: translate from EBCDIC to ASCII

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000224073537.19214.00000006@nso-fh.aol.com>`
- **References:** `<38B50854.534429F5@bikebits.bt.co.uk>`

```
Basically, I have never been able to rely on a ASCII-EBCDIC re-translation
of COMP-3 or COMP fields that have been translated EBCDIC-ASCII during
file transfer.   Mainly because of the potential for a COMP-3 or COMP byte
being translated as a communications protocol character and thus changing
the resulting appearance of the file in the PC.
Because of this, I have always moved data files as binary and written file
specific EBCDIC/ASCII conversions to translate only the display formatted 
fields.   Since that time, I have found that the DataConvertor tool that comes
with Fujitsu COBOL does an excellent job of character set translation without
any more programming than setting up a COBOL record layout copylib.
(There are some gotyas regarding the number of fields, occurs clauses
 and that sort of thing, but it works very well).


In article <38B50854.534429F5@bikebits.bt.co.uk>, Fergus Allan
<allanfw@bikebits.bt.co.uk> writes:

>I am currently processing a file which started as ebcdic and translated on th
>fly
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: translate from EBCDIC to ASCII

- **From:** chris_muller@my-deja.com
- **Date:** 2000-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bb3ab$e34$1@nnrp1.deja.com>`
- **References:** `<38B50854.534429F5@bikebits.bt.co.uk> <20000224073537.19214.00000006@nso-fh.aol.com>`

```
Please take a look at the inexpensive and powerful tools in the
download area of our website. Can download as a freeware eval and then
license it for full production.

Chris Muller
www.mullermedia.com

In article <20000224073537.19214.00000006@nso-fh.aol.com>,
sff5ky@aol.comxxx123 (Sff5ky) wrote:
> Basically, I have never been able to rely on a ASCII-EBCDIC re-
translation
> of COMP-3 or COMP fields that have been translated EBCDIC-ASCII during
> file transfer. Mainly because of the potential for a COMP-3 or COMP
byte
> being translated as a communications protocol character and thus
changing
> the resulting appearance of the file in the PC.
> Because of this, I have always moved data files as binary and written
file
> specific EBCDIC/ASCII conversions to translate only the display
formatted
> fields. Since that time, I have found that the DataConvertor tool
that comes
> with Fujitsu COBOL does an excellent job of character set translation
without
> any more programming than setting up a COBOL record layout copylib.
> (There are some gotyas regarding the number of fields, occurs clauses
…[5 more quoted lines elided]…
> >I am currently processing a file which started as ebcdic and
translated on th
> >fly
> >when transferred from the mainframe. The file contains signed and
COMP-3
> >fields.
> >My program converts the fields back to ebcdic. Are you suggesting
that the
> >mainframe will have changed the representation of the comp-3 fields
so that,
> >even
> >converting the information back to ebcdic is insufficient?
> >
> >It is true, however that the values I am processing are not correct.
This
> >may be
> >because of the above problem. It may be becaues I am not not
processing the
> >value
> >
> >correctly. The information I have regarding COMP-3 is that it is
binary
> >coded
> >decimal (BCD), thus I am breaking the byte value into
> >2 nibbles annd, finally, to display this as ascii translating the
nibble (0
> >->'0',
> >
…[4 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: translate from EBCDIC to ASCII

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<893sso$8r8$1@nntp1.atl.mindspring.net>`
- **References:** `<MPG.1317fe99f30f3e8598986e@news.mersinet.co.uk> <20000219193400.08112.00000694@nso-ce.aol.com> <38B50854.534429F5@bikebits.bt.co.uk>`

```
You really, REALLY, should not use the technique that you are trying.  There
is no one-to-one-to definition of EBCDIC -> ASCII -> EBCDIC characters that
you can count on. (In other words, you are not guaranteed to get the same
value after the two conversions.)

If you have COMP-3 (Packed-Decimal) and/or COMP (Binary) data in a file that
also includes EBCDIC character data, then there really are only two "safe"
ways to do the conversion:

1) On the mainframe (where things are EBCDIC) write a program to convert all
the data from COMP or COMP-3 (or any other similar usage) to USAGE DISPLAY
(numeric) with SIGN IS SEPARATE.  Then down-load with EBCDIC/ASCII
conversion. Then write a 2nd program to convert the (relevant) numeric fields
back to their COMP/COMP-3 usages.

2) Download the files withOUT any conversion (i.e. "BINARY") and either write
a conversion routine yourself or use one of the MANY tools provided by
vendors to convert the file based on your record layout.  (As mentioned in
this thread, Micro Focus and Fujitsu have such tools - I think CA does as
well.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
