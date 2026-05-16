[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What does this statement mean.

_5 messages · 5 participants · 1999-03_

---

### What does this statement mean.

- **From:** thomas@vdb.de
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bosf2$p0e$1@nnrp1.dejanews.com>`

```
Hello

Did anyone knows what this statment means.

pic f 999 comp -3

Thanks

Thomas

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: What does this statement mean.

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36DFFD17.772DA25@ASPMnetdoor.com>`
- **References:** `<7bosf2$p0e$1@nnrp1.dejanews.com>`

```
thomas@vdb.de wrote:

> Did anyone knows what this statment means.
>
> pic f 999 comp -3

The short answer is "NO" <g>, but you might not have copied the statement
correctly.
  f pic 999 comp-3     would have defined a three digit numeric field
contained in 2 bytes
                                named "f".  This is only part of a
statement.
    pic s999 comp-3    is part of a statement defining a three digit SIGNED
field contained
                                in two bytes.  The level number, field
name, and any value clause
                                were not shown.  HTH
```

##### ↳ ↳ Re: What does this statement mean.

- **From:** steve casey <stevencasey@ustrustboston.com>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E052D2.5C503DA@ustrustboston.com>`
- **References:** `<7bosf2$p0e$1@nnrp1.dejanews.com> <36DFFD17.772DA25@ASPMnetdoor.com>`

```
It probably can be interpreted as

05(or whatever the level number) filler pic x(02).

Warren Porter wrote:

> thomas@vdb.de wrote:
>
…[18 more quoted lines elided]…
> Rainy Days OR Mondays Always Get Me Down.
```

#### ↳ Re: What does this statement mean.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bpb1t$3ua@dfw-ixnews6.ix.netcom.com>`
- **References:** `<7bosf2$p0e$1@nnrp1.dejanews.com>`

```
thomas@vdb.de wrote in message <7bosf2$p0e$1@nnrp1.dejanews.com>...
>Hello
>
…[6 more quoted lines elided]…
>

I actually think I *might* know what this means (although the lower-case
letters AND a reasonability check both make it pretty unlikely).  With the
OLD IBM mainframe compilers (documented in ANS COBOL Vn - and still
supported but not documented with OS/VS COBOL) there was native language
support for the "olde" British monetary system (pre-decimal) with pounds,
shillings, and pence.  Most often you would see this with USAGE DISPLAY-ST,
but I think (and this is really racking my brain) you could use it with
other numeric usages.  As I recall (and again this is pretty foggy), the
PICTURE symbols did include an "f" (as well as "d" and "l" - maybe?) and
even though the rest of your source code had to be upper case, I do remember
that "D" and "d" represented different values/uses.  Again, this is all
QUITE vague and probably NOT what you are running into - but it should be an
interesting diversion if nothing else.
```

#### ↳ Re: What does this statement mean.

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E435B4.9FDEA41E@IMN.nl>`
- **References:** `<7bosf2$p0e$1@nnrp1.dejanews.com>`

```
I suppose you put the space between the "f" and the "999" by accident as
you did betweren "comp" and "-3".
Than I read: ... pic F999 comp-3

This could be part of a complete field definition like:

01  variable picture is f999, usage is computational-3.

I first thought about an alternative edit character F i.s.o $, which is
possible by stating CURRENCY SIGN IS "F" in the special-names paragraph.
but that conflicts with the usage. May be you should post more code.

The COBOL Frog

thomas@vdb.de wrote:

> Hello
>
…[9 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
