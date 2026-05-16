[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-1 conversion

_11 messages · 8 participants · 1999-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: COMP-1 conversion

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1sto$ds5$2@news-1.news.gte.net>`
- **References:** `<36e43e42.0@d2o94.telia.com>`

```
I believe COMP-1 is IEEE single precision and COMP-2 is IEEE double, both of
which are handled as standard "floating piont" types in various compiler
languages.

Micro format? I do not have a clue.

Krister H�ger�s wrote in message <36e43e42.0@d2o94.telia.com>...
>I need program code (basic, C, pascal or xBase) to convert the formats
>
>    fixed binary (=comp-1)
>    micro
>
```

#### ↳ Re: COMP-1 conversion

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990309083436.12463.00000035@ng-fi1.aol.com>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net>`

```
comp-1, or comp, is useage BINARY and is not a floating point storage area
```

##### ↳ ↳ Re: COMP-1 conversion

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c38fp$8rt@netnews1.apci.com>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com>`

```
In IBM mainframe land, there are a number of ways that data can be stored:

DISPLAY -- the default, character mode in EBCDIC
COMP -- binary, length is 2/4/8 bytes depending on number of significant
digits
COMP-1 -- full-word length (4 bytes) floating point
COMP-2 -- double-word length (8 bytes) floating point
COMP-3 -- "packed decimal" with 1/2 byte (a nibble) per digit and a trailing
sign in the final nibble

In 30+ years of programming, I have had the opportunity to use COMP-1/COMP-2
only a few times, although the last one was only two years ago as (believe
it or not) part of our Y2K project.  Nonetheless, it is sometimes a valuable
tool in selected instances.

Alan Russell, PhD, CCP
Work - Russelah@apci.com
Home - AHRussell@computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer

Twymer wrote in message <19990309083436.12463.00000035@ng-fi1.aol.com>...
>comp-1, or comp, is useage BINARY and is not a floating point storage area
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990309102019.06029.00000121@ng-cg1.aol.com>`
- **References:** `<7c38fp$8rt@netnews1.apci.com>`

```
Thank you...I am always getting those two confused.  Generally I use COMP-3 for
any number where computations will be done and DISPLAY for all other numbers.
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

- **From:** "Krister H���ger���s" <krhag@telia.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e54b91.0@d2o94.telia.com>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com>`

```
So, do you know where to find some example program code (in some high level
language like basic) to convert the comp-1 and comp-2 strings to numeric
valules?

It would also help if I could find a detailed description on these formats.

Krister
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c4ghj$nd3$2@news-2.news.gte.net>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com> <36e54b91.0@d2o94.telia.com>`

```
If COMP-1 and COMP-2 are IEEE singles and doubles, using BASIC:

Numericval! = CVS(four-byte-comp-1-string)
NumericVal# = CVD(eight-byte-comp-2-string)

For complete description, I know the format is public domain; you might
inquire at IEEE;
OR;
if you have a friend who uses PowerBASIC/DOS, there are pictures of the bit
patterns, text and and everything in the manual.

MCM
Special Contributor, Basically Speaking magazine


Krister H�ger�s wrote in message <36e54b91.0@d2o94.telia.com>...
>So, do you know where to find some example program code (in some high level
>language like basic) to convert the comp-1 and comp-2 strings to numeric
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

_(reply depth: 5)_

- **From:** "Krister H���ger���s" <krhag@telia.com>
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36eadd6b.0@d2o94.telia.com>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com> <36e54b91.0@d2o94.telia.com> <7c4ghj$nd3$2@news-2.news.gte.net>`

```
Well, the problem is easily solved with the CVS / CVD functions in QB, but
my problem is that i want to convert the strings to numbers without having
those functions, with a program that runs throug the bytes and calculates a
value.

Krister
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ckidt$l20$1@news.igs.net>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com> <36e54b91.0@d2o94.telia.com> <7c4ghj$nd3$2@news-2.news.gte.net> <36eadd6b.0@d2o94.telia.com>`

```
Then write it in Cobol, and it will do exactly what you want.

Krister H�ger�s wrote in message <36eadd6b.0@d2o94.telia.com>...
>Well, the problem is easily solved with the CVS / CVD functions in QB, but
>my problem is that i want to convert the strings to numbers without having
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7clpd7$s78$1@server.cntfl.com>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com> <36e54b91.0@d2o94.telia.com> <7c4ghj$nd3$2@news-2.news.gte.net> <36eadd6b.0@d2o94.telia.com>`

```

Krister H�ger�s wrote in message <36eadd6b.0@d2o94.telia.com>...
>Well, the problem is easily solved with the CVS / CVD functions in QB, but
>my problem is that i want to convert the strings to numbers without having
>those functions, with a program that runs throug the bytes and calculates a
>value.
>
Why not write the functions? (You had mentioned Basic, C, Pacal,
and XBase earlier.)

The equivalent C code should be:
-----------
#include <string.h>

float cvs ( void * s )
{
    float f;
    memcpy ( s, &f, 4 );
    return (f);
}

double cvd ( void *s )
{
    double d;
    memcpy ( s, &d, 8 );
    return (d);
}
-----------
These functions are useful for aligning data on systems that do not
automatically allign data. (Most / All ?) COBOL implementations
will move unaligned data if required.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

_(reply depth: 4)_

- **From:** Nige <znige@zwg.zicl.co.uk>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E565BA.4321F18C@zwg.zicl.co.uk>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com> <36e54b91.0@d2o94.telia.com>`

```
Krister Hï¿½gerï¿½s wrote:
> 
> So, do you know where to find some example program code (in some high level
> language like basic) to convert the comp-1 and comp-2 strings to numeric
> valules?

Unfortunately the way comp-n things are stored depends on your
compiler.  If in doubt, write some COBOL to do it.

   Cheers,
     Nige 
```

###### ↳ ↳ ↳ Re: COMP-1 conversion

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-bn58lG21RUTg@Dwight_Miller.iix.com>`
- **References:** `<7c1sto$ds5$2@news-1.news.gte.net> <19990309083436.12463.00000035@ng-fi1.aol.com> <7c38fp$8rt@netnews1.apci.com> <36e54b91.0@d2o94.telia.com>`

```
On Tue, 9 Mar 1999 16:25:20, "Krister H���ger���s" <krhag@telia.com> 
wrote:

> So, do you know where to find some example program code (in some high level
> language like basic) to convert the comp-1 and comp-2 strings to numeric
> valules?
> 
> It would also help if I could find a detailed description on these formats.

It would help more if they were consistent!  The IEEE version and the 
version used on IBM mainframes is different.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
