[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fijutsu Cobol V3 and the Dollar Sign

_4 messages · 4 participants · 1999-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Fijutsu Cobol V3 and the Dollar Sign

- **From:** binco@t-online.de (patty)
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dl4bk$av3$1@news02.btx.dtag.de>`

```
Could someone please help me!!
I have Fujitsu Cobol V3 installed on my computer running the German version
of Windows 98. and therefore in the currency setting it is the German Symbol
set, and that is the "DM" for Deutsch Mark. So when I try to compile a cobol
file with dollar symbols for example:

01  D-EXAPLES    PIC  $$$.$$

the compiler stops compiling with the message, Invalid characters in string
at the named line.  Is there  a way to correct that, without changing in the
Currency Setup of my Windows 98?. As you know every system depends on the
local currency symbols to display the correct local cuurency of that
particular country. Iam sure the americans will not be please that there
systems prints DM instead of the $ in all there money dealings!


Please reply to  binco@t-online.de

dna.
Pat.
```

#### ↳ Re: Fijutsu Cobol V3 and the Dollar Sign

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36fe4276.223019272@news1.ibm.net>`
- **References:** `<7dl4bk$av3$1@news02.btx.dtag.de>`

```
On Sun, 28 Mar 1999 13:38:08 +0200, binco@t-online.de (patty) wrote:

>Could someone please help me!!
>I have Fujitsu Cobol V3 installed on my computer running the German version
…[5 more quoted lines elided]…
>

As is surely yet another coincidence in comp.lang.cobol (or maybe it's
magic?) we just recently discussed this issue in depth!  You can set
your compiler directive to say: CURRENCY($) and it will override the
Windows regional settings.  The easiest place to put this is at the
top of your program, starting in column 8.  @OPTIONS MAIN,CURRENCY($)

This is for a MAIN (not called) program.
```

#### ↳ Re: Fijutsu Cobol V3 and the Dollar Sign

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7do3hk$hmt$1@client2.news.psi.net>`
- **References:** `<7dl4bk$av3$1@news02.btx.dtag.de>`

```
patty wrote in message <7dl4bk$av3$1@news02.btx.dtag.de>...
>I am sure the americans will not be please that there
>systems prints DM instead of the $ in all there money dealings!


Pat:

As Fujitsu COBOL is implemented almost entirely in Japan, perhaps you should
limit your "blame assignment."  It is my understanding that Fujitsu
(America) is almost exclusively a productization/marketing operation when it
pertains to Fujitsu COBOL.  I am sure that the Fujitsu implementation was a
well-intentioned, but flawed, effort to reduce the burden of currency symbol
issues on the programmer.  Fujitsu will no doubt get it right in a future
release.

Furthermore, COBOL is subject to an international (ISO) standard, which
allows only one character for the currency symbol substitution.  It has been
this way for decades.  If Windows is providing two characters 'DM' as the
currency symbol, then your National Standards organization (DIN?) should
help the current committee drafting the next COBOL standard to resolve this
issue.

Tom Morrison
```

##### ↳ ↳ Re: Fijutsu Cobol V3 and the Dollar Sign

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dojpu$duk@dfw-ixnews5.ix.netcom.com>`
- **References:** `<7dl4bk$av3$1@news02.btx.dtag.de> <7do3hk$hmt$1@client2.news.psi.net>`

```

Tom Morrison wrote in message <7do3hk$hmt$1@client2.news.psi.net>...
  <snip>
>
>Furthermore, COBOL is subject to an international (ISO) standard, which
>allows only one character for the currency symbol substitution.  It has
been
>this way for decades.  If Windows is providing two characters 'DM' as the
>currency symbol, then your National Standards organization (DIN?) should
…[5 more quoted lines elided]…
>

The next Standard already includes syntax for supporting multi-character
currency symbols.  It also has a method for distinguishing between currency
symbols and currency signs.  This is a little obscure (and I don't have all
the details handy) but it does provide a method whereby you can use one
symbol in your PICTURE clause but have another symbol (or symbols) in your
input/output.  This would "handle" the case that was recently discussed in
C.L.C. where you wanted the currency sign to be an "S" but to still be able
to use an "S" in the PICTURE clause for a numeric (not edited) item.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
