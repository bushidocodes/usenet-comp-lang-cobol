[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Wanted

_7 messages · 6 participants · 1996-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help Wanted

- **From:** "arnd heymann" <ua-author-17086548@usenetarchives.gap>
- **Date:** 1996-11-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`

```

Hello,

Im a Cobol beginner and I魹ｽm looking for help.

I want to define a table with undefined (Occurs)

f.Ex. 05 ABESCHREI PIC X(10) OCCURS ==>N Times

How can I solve this Problem ?

Ciao Arnd Heymann
```

#### ↳ Re: Help Wanted

- **From:** "spam.f..." <ua-author-17086140@usenetarchives.gap>
- **Date:** 1996-11-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3a1db6c64e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`
- **References:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`

```

"Arnd Heymann" wrote:
› Hello,
› 
…[8 more quoted lines elided]…
› Ciao Arnd Heymann

05 abeschrei PIC X(10) OCCURS 1 TO 20 TIMES DEPENDING ON n.
..
77 n PIC 9(4) COMP VALUE 17.

The number of occurrences of the table is defined by the value
stored in n.

Doug Miller
dlm··.@ine··t.net ('from' field rigged to foil e-mail spammers)
views expressed are mine and not those of
Hospital Health Plan Corp. "all health care is local"
```

#### ↳ Re: Help Wanted

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1996-11-04T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3a1db6c64e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`
- **References:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`

```

"Arnd Heymann" wrote:

› Hello,
 
› Im a Cobol beginner and I魹ｽm looking for help.
 
› I want to define a table with undefined (Occurs)
 
› f.Ex. 	05 ABESCHREI PIC X(10) OCCURS ==>N Times
 
› How can I solve this Problem ?


Hope this is on your own and not for a class....since your teacher
will probably hate you doing this....

If you define a table, you can set it up varying against another
variable. As an example:

05 TEMPS PIC 99.
05 TEMP-TABLE PIC X(10) OCCURS 1 TO 31 TIMES DEPENDING ON TEMPS.

The table defined can have a minimum of 1 unit, and a maximum of 31
units, but actually has the number of units as described in TEMPS.
```

#### ↳ Re: Help Wanted

- **From:** "r..." <ua-author-2587243@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3a1db6c64e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`
- **References:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`

```

In article <01bbcb03$3ec10c40$7d4··.@Ope··e.de>
A.··.@Eur··e.de "Arnd Heymann" writes:
› Im a Cobol beginner and I魹ｽm looking for help.
›    I want to define a table with undefined (Occurs)
› f.Ex.   05 ABESCHREI PIC X(10) OCCURS ==>N Times
› How can I solve this Problem ?

Use a file. What was the _original_ problem?

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

#### ↳ Re: Help Wanted

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3a1db6c64e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`
- **References:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`

```

In message <<01bbcb03$3ec10c40$7d4··.@Ope··e.de>> "Arnd Heymann" writes:
› 
› Im a Cobol beginner and I m looking for help.
…[5 more quoted lines elided]…
› How can I solve this Problem ?

Cobol is a business language. In real business problems there is
usually some sensible or actual limit to the number of occurances
that are required. These are usually defined within the problem:
an invoice page is only so many lines long, there can only be a
particular number of price categories.

Where there are unlimited items: number of customers, transactions
for a customer; then this tends to be _shared_ data, several
programs will want to access it at the same time. This leads to
the data being held on an ISAM file where it can be read and
processed as required while catering for the needs of other programs.

Building and processing tables in memory tends to restrict the
ability of others to access this. This may well be appropriate
in certain cases, but it is not usually unrestricted.

Also there is a finite limit to how big an array can be due to
limits of actual memory, hardware accesibility or compiler
limitations. Given that there is some actual upper limit why
would you want to have a variable limit ?

At what point would you actually want to set 'N' ? What is the
range that may occur in practice ? What effects are you looking
by have an OCCURS less than the maximum possible ? Will the
change in 'N' attempt to move other items around (ie will you have
other 05 level items following this ?

Have you looked at OCCURS DEPENDING ON ?
```

#### ↳ Re: Help Wanted

- **From:** "zuffardi eduardo" <ua-author-17086202@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3a1db6c64e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`
- **References:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de>`

```

Arnd Heymann wrote:
› 
› Hello,
…[9 more quoted lines elided]…
› Ciao Arnd Heymann

Hello I'm Eduardo from Argentina... I'm using VAX Cobol in a VMS
environment.

Check your Cobol version and try typing this

05 ABESCHREI PIC X(10) OCCURS 2 to 4 times depending on numtimes

literally "Build a table that can contain at least 2 rows and no more
than four depending of the value of numtimes.

Bye!

e-mail: zuf··.@ffi··u.ar
```

##### ↳ ↳ Re: Help Wanted

- **From:** "zuffardi eduardo" <ua-author-17086202@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3a1db6c64e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3a1db6c64e-p6@usenetarchives.gap>`
- **References:** `<01bbcb03$3ec10c40$7d46e7c2@Operator.europe.de> <gap-3a1db6c64e-p6@usenetarchives.gap>`

```
Zuffardi Eduardo wrote:
› 
› Arnd Heymann wrote:
…[25 more quoted lines elided]…
› e-mail: zuf··.@ffi··u.ar

you can visit my



Eduardo Zuffardi's HomePage
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
