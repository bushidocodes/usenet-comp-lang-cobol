[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comp-3

_10 messages · 6 participants · 2006-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Comp-3

- **From:** "GARY" <gcotterl@co.riverside.ca.us>
- **Date:** 2006-07-16T10:37:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com>`

```
What is the ASCII equivalent of a field with a PIC of "S9(09)v99
Comp-3"?
```

#### ↳ Re: Comp-3

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-16T13:18:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bl0ociah9964a@news.supernews.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com>`

```
GARY wrote:
> What is the ASCII equivalent of a field with a PIC of "S9(09)v99
> Comp-3"?

There isn't one. There's no "ASCII equivalent" of any data definition. 
Perhaps you could rephrase?

I can tell you the above PIC defines (usually) six bytes with a decimal 
digit in each half-byte and the last half-byte contains the algebraic sign 
of the number. i.e., 12 34 56 78 91 2S = 123,456,789.12
```

##### ↳ ↳ Re: Comp-3

- **From:** "GARY" <gcotterl@co.riverside.ca.us>
- **Date:** 2006-07-16T12:12:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153077136.934457.120940@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<12bl0ociah9964a@news.supernews.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com>`

```
How many text (ASCII) characters are contained in each of the following
fields?
In the "COMP-3" fields, how are negative numbers (for example,
-00000048612) shown?

PIC X(01)
PIC 9(09)
PIC 9(04)
PIC 9(02)
PIC 9(07)
PIC 9(02)
PIC 9(02)
PIC 9(04)
PIC 9(01)
PIC 9(06)
PIC 9(07)
PIC S9(09)V99       COMP-3
PIC S9(05)V99       COMP-3
PIC S9(02)V99       COMP-3
PIC S9(05)V99       COMP-3
PIC 9(04)
PIC 9(04)
PIC S9(09)            COMP-3
PIC S9(09)V99      COMP-3
PIC S9(03)V99      COMP-3
PIC S9(03)V99      COMP-3
PIC S9(03)V99      COMP-3
PIC S9(09)V99      COMP-3
PIC 9(08)
PIC X(01)
PIC 9(02)
PIC X(02)
PIC S9(07)V99      COMP-3
PIC X(04)
PIC 9(07)
PIC 9(04)
PIC 9(05)
PIC S9(09)V99      COMP-3
PIC S9(09)V99      COMP-3
PIC S9(03)V99      COMP-3
PIC S9(03)V99      COMP-3
PIC S9(07)V99      COMP-3
PIC X(01)                      
PIC X(02)
```

###### ↳ ↳ ↳ Re: Comp-3

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-16T19:19:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yiwug.211924$YR4.181404@fe10.news.easynews.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com> <1153077136.934457.120940@i42g2000cwa.googlegroups.com>`

```
What operating system? What compiler? What compiler options specified? and what 
do you think the answers are?
```

###### ↳ ↳ ↳ Re: Comp-3

_(reply depth: 4)_

- **From:** "GARY" <gcotterl@co.riverside.ca.us>
- **Date:** 2006-07-16T13:03:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153080213.610225.323410@p79g2000cwp.googlegroups.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com> <1153077136.934457.120940@i42g2000cwa.googlegroups.com> <Yiwug.211924$YR4.181404@fe10.news.easynews.com>`

```
                                          My "guess" is:

PIC X(01)                                   1
PIC 9(09)                                   9
PIC 9(04)                                   4
PIC 9(02)                                   2
PIC 9(07)                                   7
PIC 9(02)                                   2
PIC 9(02)                                   2
PIC 9(04)                                   4
PIC 9(01)                                   1
PIC 9(06)                                   6
PIC 9(07)                                   7
PIC S9(09)V99 COMP-3                      11
PIC S9(05)V99 COMP-3                       7
PIC S9(02)V99 COMP-3                       4
PIC S9(05)V99 COMP-3                       7
PIC 9(04)                                 4
PIC 9(04)                                 4
PIC S9(09) COMP-3                        9
PIC S9(09)V99 COMP-3                     11
PIC S9(03)V99 COMP-3                       5
PIC S9(03)V99 COMP-3                       5
PIC S9(03)V99 COMP-3                       5
PIC S9(09)V99 COMP-3                     11
PIC 9(08)                                   8
PIC X(01)                                   1
PIC 9(02)                                   2
PIC X(02)                                   2
PIC S9(07)V99 COMP-3                       9
PIC X(04)                                   4
PIC 9(07)                                   7
PIC 9(04)                                   4
PIC 9(05)                                   5
PIC S9(09)V99 COMP-3                     11
PIC S9(09)V99 COMP-3                     11
PIC S9(03)V99 COMP-3                       5
PIC S9(03)V99 COMP-3                       5
PIC S9(07)V99 COMP-3                       9
PIC X(01)                                    1
PIC X(02)                                    2



Note: The "Comp-8" LRECL = 160; the LRECL of my "guess" = 214
```

###### ↳ ↳ ↳ Re: Comp-3

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-16T23:42:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B9Aug.277741$cd2.267474@fe06.news.easynews.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com> <1153077136.934457.120940@i42g2000cwa.googlegroups.com> <Yiwug.211924$YR4.181404@fe10.news.easynews.com> <1153080213.610225.323410@p79g2000cwp.googlegroups.com>`

```
(On an IBM mainframe - and many - not all - other platforms)

     PIC S9(09)V99 COMP-3                      11

takes 6 bytes AS DOES

    PIC S9(08)V99 COMP-3

Can you figure out why?

There is NOTHING about any of this that has to do with "ASCII CHARACTERS" - but 
it does have to do with "information contained" (10 or 11 digits and a sign) and 
how many bytes it takes to store it.
```

###### ↳ ↳ ↳ Re: Comp-3

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-16T13:18:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153081095.625535.274670@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1153077136.934457.120940@i42g2000cwa.googlegroups.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com> <1153077136.934457.120940@i42g2000cwa.googlegroups.com>`

```

GARY wrote:
> How many text (ASCII) characters are contained in each of the following
> fields?

It may be 'none' if this is on an EDCIDC machine.  Fields need not be
represented as ASCII characters, for example binary or packed decimal
are bit patterns which need to be examined as bits or hexadecimal
nibbles. COMP-3 may be packed decimal* and thus each digit is a nibble
(4 bits - half byte).

> In the "COMP-3" fields, how are negative numbers (for example,
> -00000048612) shown?

Sign is probably in last in last nibble.



* COMP-3 can be anything the compiler writer wants it to be. You need
to specify the compiler and possibly the system it is used on.  In many
cases COMP-3 is packed decimal with the sign in the last nibble.
```

###### ↳ ↳ ↳ Re: Comp-3

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-17T08:31:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bn49qmup4ld53@news.supernews.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com> <1153077136.934457.120940@i42g2000cwa.googlegroups.com>`

```
GARY wrote:
> How many text (ASCII) characters are contained in each of the
> following fields?

None. ASCII has nothing to do with it.

> In the "COMP-3" fields, how are negative numbers (for example,
> -00000048612) shown?

A hex F, A, C, or E in the last nibble indicates a positive number, D and B 
indicate negative.

>
> PIC X(01)
…[37 more quoted lines elided]…
> PIC X(02)
```

###### ↳ ↳ ↳ Re: Comp-3

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2006-07-17T21:33:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3d1$44bc3a60$4f9c6ce$14474@DIALUPUSA.NET>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com> <12bl0ociah9964a@news.supernews.com> <1153077136.934457.120940@i42g2000cwa.googlegroups.com>`

```

"GARY" <gcotterl@co.riverside.ca.us> wrote in message 
news:1153077136.934457.120940@i42g2000cwa.googlegroups.com...
> How many text (ASCII) characters are contained in each of the following
> fields?
…[42 more quoted lines elided]…
>

How about DISPLAYing LENGTH OF
```

#### ↳ Re: Comp-3

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-07-17T07:17:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd3nb25qb27smk0caauo4tmsgesksousn3@4ax.com>`
- **References:** `<1153071455.248304.311190@75g2000cwc.googlegroups.com>`

```
On 16 Jul 2006 10:37:35 -0700, "GARY" <gcotterl@co.riverside.ca.us>
wrote:

>What is the ASCII equivalent of a field with a PIC of "S9(09)v99
>Comp-3"?

Your question doesn't make any sense.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
