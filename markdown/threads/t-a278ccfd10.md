[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Decimal to Comma Conversion?

_12 messages · 10 participants · 2000-06_

---

### Decimal to Comma Conversion?

- **From:** jonsio@my-deja.com
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
Does anybody have an idea on the best way to reformat decimal to commas
for European currency applications?


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Decimal to Comma Conversion?

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394648CE.A0E67E51@yahoo.com>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
Well, for string fields you could try 
INSPECT field-name REPLACING ALL '.' BY ','.

For PICTURE clauses use DECIMAL-POINT IS COMMA in your special-names
paragraph.  This exchanges the functions of the period and the comma in
picture strings and numeric literals.

jonsio@my-deja.com wrote:
> 
> Does anybody have an idea on the best way to reformat decimal to commas
…[3 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Decimal to Comma Conversion?

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uuNbOZU1$GA.283@cpmsnbbsa09>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
INSPECT xxx
                 REPLACING ALL "." BY ",".  Where xxx is the name of the
data element to change.

<jonsio@my-deja.com> wrote in message news:8i5eog$v3u$1@nnrp1.deja.com...
> Does anybody have an idea on the best way to reformat decimal to commas
> for European currency applications?
…[3 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Decimal to Comma Conversion?

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i5ljk$qt3$1@news.igs.net>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
The DECIMAL POINT IS COMMA statement should work for all your output.  If
you are using the "." in actual code (in string and unstring, for example),
and are converting the system to run either/or, then I'd suggest that you do
it with the new CONSTANT function, or put the character into a parameter in
your set-up file. Doing it with the CONSTANT method would require you
compile for a European version, while the other way would make it a setup
parameter.  Avoid hard-coding it like a plaque.  It will come back to haunt
you.

jonsio@my-deja.com wrote in message <8i5eog$v3u$1@nnrp1.deja.com>...
>Does anybody have an idea on the best way to reformat decimal to commas
>for European currency applications?
…[3 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: Decimal to Comma Conversion?

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KXVGORZM=4MUkgOT1jXRUJVhnyrJ@4ax.com>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com> <8i5ljk$qt3$1@news.igs.net>`

```
Although the "Decimal point is comma" works fine, it "can not"
normally be use in a program that has "input".
The reason for this is that up to a short time ago, most terminals
of Unix and others would not allow the "decimal" point on the numeric
keypad to be changed. (someone from the US forgot this "small" detail)

This poses a BIG problem because if developers use the "Decimal point"
ad standard, although this will save some programming time, it will
force the users to use both the normal keyboard (for the "comma") and
the numeric keypad for the numbers.

If one does not use that instruction, all input can be made on the
numeric keypad, and the programmer is responsible for replacing
the variables on output( either display or printer).

As for replacing the variables, I always find the using
inspect variable converting ",." to ".," easy enough to use.

as oposed to use three inspect replacing as someone mentioned before.


FF



On Tue, 13 Jun 2000 11:50:29 -0400, "donald tees"
<donald@willmack.com> wrote:

>The DECIMAL POINT IS COMMA statement should work for all your output.  If
>you are using the "." in actual code (in string and unstring, for example),
…[14 more quoted lines elided]…
>
```

#### ↳ Re: Decimal to Comma Conversion?

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i69q1$ene$1@news.inet.tele.dk>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
It's amazing how we ever got our data displayed correct isn't it??

Looking through all the suggestions I'm confused, and I bet you are too.

This is how we do it far away from the Bermuda Triangle.

Put a DECIMAL POINT IS COMMA in Special-Names.

Move your currency fields to one of folowing display-fields

01 Display-Options.
     05 Less-than-1000    pic zz9,99-
     05 More-than-1000    pic zzz.zzz.zzz.zz9,99-

We fancy the sign after the amount. We fancy one digit in front of the
decimal-point (e.g. 0,37- )

Remember, that some countries in Europe must specify national currency and
EURO for a period of time. You need 6 decimals in calculations to get
satisfactory precission.

Hans Christian Andersen came from Denmark (Europe). Don't listen to other
fairy tales.

Good luck
Ib


jonsio@my-deja.com skrev i meddelelsen <8i5eog$v3u$1@nnrp1.deja.com>...
>Does anybody have an idea on the best way to reformat decimal to commas
>for European currency applications?
…[3 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: Decimal to Comma Conversion?

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mHC15.30070$Gh.286361@typhoon.austin.rr.com>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com> <8i69q1$ene$1@news.inet.tele.dk>`

```

Ib Tanding <ib@tanding.dk> wrote in message
news:8i69q1$ene$1@news.inet.tele.dk...
> Put a DECIMAL POINT IS COMMA in Special-Names.
>
…[4 more quoted lines elided]…
>      05 More-than-1000    pic zzz.zzz.zzz.zz9,99-


Ib,
I'm amazed too. There is a more subtle problem though. I often
have had to make multi-lingual reports, e.g one in US-English
and one in French, etc, all from within the SAME program.
There you can clearly not use the special-names method.

Leif
```

#### ↳ Re: Decimal to Comma Conversion?

- **From:** tscoffey@my-deja.com
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i5i0e$1uv$1@nnrp1.deja.com>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
This might work...(pardon the light-heartedness)


  01  AMERICAN-REAL-MONEY    PIC 9(8)V99 COMP-3.
  01  EURO-SILLY-PLAY-MONEY  PIC 99,999,999.99.

  MOVE AMERICAN-REAL-MONEY TO
       EURO-SILLY-PLAY-MONEY.
  INSPECT EURO-SILLY-PLAY-MONEY REPLACING ALL ',' BY LOW-VALUES.
  INSPECT EURO-SILLY-PLAY-MONEY REPLACING ALL '.' BY ','.
  INSPECT EURO-SILLY-PLAY-MONEY REPLACING ALL LOW-VALUES BY '.'.

Tim Coffey




In article <8i5eog$v3u$1@nnrp1.deja.com>,
  jonsio@my-deja.com wrote:
> Does anybody have an idea on the best way to reformat decimal to
commas
> for European currency applications?
>
> Sent via Deja.com http://www.deja.com/
> Before you buy.
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Decimal to Comma Conversion?

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i68ro$cog$1@news.inet.tele.dk>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com> <8i5i0e$1uv$1@nnrp1.deja.com>`

```
You are not getting paid to make solutions like this, are you?????

Regards
Ib
tscoffey@my-deja.com skrev i meddelelsen <8i5i0e$1uv$1@nnrp1.deja.com>...
>This might work...(pardon the light-heartedness)
>
…[27 more quoted lines elided]…
>Before you buy.
```

###### ↳ ↳ ↳ Re: Decimal to Comma Conversion?

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zDtHOWcOy29S+9Z3y5LJZ4o+C53Z@4ax.com>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com> <8i5i0e$1uv$1@nnrp1.deja.com> <8i68ro$cog$1@news.inet.tele.dk>`

```
As I said in another post, it is either this solution
(if you do not know how to use "inspect ... converting"
or the "inspect ... converting ",." ".,".

And I have to say that from the hundreds of customers
that I have worked with, 90% or more used(1) one or the other
to convert from ",." to ".$" which is the portuguese
monetary separator. like 100$50 which translate as
one hundred ESCUDOS and fifty cents.

FF


(1)- Not anymore because of the EURO.
 "Big time (bucks) converting programs..."




On Tue, 13 Jun 2000 23:30:56 +0200, "Ib Tanding" <ib@tanding.dk>
wrote:

>You are not getting paid to make solutions like this, are you?????
>
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Decimal to Comma Conversion?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i8e0t$ce3$1@slb7.atl.mindspring.net>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com> <8i5i0e$1uv$1@nnrp1.deja.com> <8i68ro$cog$1@news.inet.tele.dk> <zDtHOWcOy29S+9Z3y5LJZ4o+C53Z@4ax.com>`

```
FYI,  the draft of the next Standard "easily" handles multiple methods of
displaying both numeric and monetary amounts in the same program - using
"LOCALE" logic (as defined in POSIX).

Check with your "vendor of choice" on what their plans are for implementing
this particular feature (before any Standard gets approved).  Some (e.g.
COBOL/400) have already done so.
```

#### ↳ Re: Decimal to Comma Conversion?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39464ab9.157202334@207.126.101.100>`
- **References:** `<8i5eog$v3u$1@nnrp1.deja.com>`

```
On Tue, 13 Jun 2000 13:59:56 GMT, jonsio@my-deja.com wrote:

>Does anybody have an idea on the best way to reformat decimal to commas
>for European currency applications?
>

Most compilers support a decimal point is comma directive.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
