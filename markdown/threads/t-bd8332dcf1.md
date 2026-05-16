[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXEC=..,PARM=.. It works but I don't understand why

_19 messages · 9 participants · 1998-09_

---

### EXEC=..,PARM=.. It works but I don't understand why

- **From:** "Simon Ward" <tubby@toasts.force9.co.uk>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t3lg3$jau@news3.force9.net>`

```
    I would be gratefull if someone could explain the the difference between
the 2 situations below. I am passing information using the PARM part of the
EXEC statement in JCL to pass information from the JCL into a COBOL
subroutine.

    If I pass a string, the first 4 bytes of the passed data contains the
length of the string in oacked decimal.

    If I pass a hex value (eg comp-3) the first 4 bytes also contain the
length but the data starts at the 6 byte! not the 5th! I don't understand
why this is so. Is the 5th byte used to store something?
```

#### ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R1zK1.122$4E6.1569153@storm.twcol.com>`
- **References:** `<6t3lg3$jau@news3.force9.net>`

```
>length but the data starts at the 6 byte! not the 5th! I don't understand
>why this is so. Is the 5th byte used to store something?


One possible reason is that COBOL cannot use numbers of length 1. I do mean
numbers, not pic X. I assume the first byte you are looking at is '00'x
which simply means the hex value you passed was converted from 1 byte to 2
bytes.

It would be nice to see the exact hex value which is being passed to your
COBOL program.
```

##### ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tetl9$8c8$1@news.igs.net>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com>`

```
Huh?  what about PICTURE 9?

>One possible reason is that COBOL cannot use numbers of length 1. I do mean
>numbers, not pic X. I assume the first byte you are looking at is '00'x
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nvFK1.142$4E6.1829838@storm.twcol.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com> <6tetl9$8c8$1@news.igs.net>`

```
>Huh?  what about PICTURE 9?


Look at a compile listing. You can make the variable any length you want.
COBOL has a minimum requirement of 2 bytes. You have to do some finagelling
to get at a one byte number when passed to a COBOL program. With maybe the
exception of a PIC X field. All numerics are a minimum of 2 bytes in COBOL.
The PIC 9 you refer to only affects the run of the program in so far as the
range of the number is checked. As in compiler directive SSRANGE and
NOSSRANGE. The same kind of thing happens with a PIC 9999 USAGE
PACKED-DECIMAL. Where the actual storage area of the variable is 3 bytes,
normally defining a 5 digit packed-decimal number.

I know it looks incorrect, but look at the cross reference information in a
COBOL listing with a PIC 9 field. There will be 2 bytes assigned to that
number. The cross reference information I am referring to is to the right of
the code. On a normal 80 column screen you have to scroll to the right to
see this information in the WORKING-STORAGE section.

In the end this may have been fixed with the newer versions of COBOL.
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tfb2v$k2b$1@news.igs.net>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com> <6tetl9$8c8$1@news.igs.net> <nvFK1.142$4E6.1829838@storm.twcol.com>`

```

Jeff wrote in message ...
>>Huh?  what about PICTURE 9?
>
…[3 more quoted lines elided]…
>exception of a PIC X field. All numerics are a minimum of 2 bytes in COBOL.


Nonsense.  You probably have your compiler set to use Japanese
characters (16 bit) or something.  I can assure you that Cobol is quite
capable of byte level manipulation. What computer/compiler are you
using?
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tfel0$hvp@dfw-ixnews4.ix.netcom.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com> <6tetl9$8c8$1@news.igs.net> <nvFK1.142$4E6.1829838@storm.twcol.com>`

```
There is not now, nor has there ever been ANY IBM mainframe COBOL compiler
that allocated 2 bytes for a
    PIC 9  (USAGE DISPLAY - implied or stated)
field.  The only time you MIGHT have gotten two bytes for this - is if the
NEXT field required a "slack" byte because it needed to be on a half-word
(or whole- or double- word) boundary.  Please "snip" and show us YOUR XREF
if you compile a data division with.

    01  GROUP-ITEM.
           05   ONE-NUM   PIC 9.
           05   ANOTHER-NUM   PIC 9.
           05   MORE-STUFF  PIC X(10).

(All caps used so it will compile with the OLDEST IBM mainframe compilers.)
If you show an XREF with more than one byte for each numeric field, I will
be very VERY surprised.

(The rules for COMP, COMP-4, BINARY, fields are different - but even a
     PIC S9 COMP-3
item will fit in one byte.)


Jeff wrote in message ...
>>Huh?  what about PICTURE 9?
>
…[13 more quoted lines elided]…
>number. The cross reference information I am referring to is to the right
of
>the code. On a normal 80 column screen you have to scroll to the right to
>see this information in the WORKING-STORAGE section.
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't

_(reply depth: 4)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298255.68763.25458@kcbbs.gen.nz>`
- **References:** `<nvFK1.142$4E6.1829838@storm.twcol.com>`

```
In message <<nvFK1.142$4E6.1829838@storm.twcol.com>> "Jeff" <a@a.com> writes:
> 
> 
…[3 more quoted lines elided]…
> exception of a PIC X field. All numerics are a minimum of 2 bytes in COBOL.

This of course is not a constraint of 'COBOL', but of that one
specific implementation on the machine you are using.  Different
implementations may have different criteria in this area.
```

##### ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tehjd$5l1@dfw-ixnews5.ix.netcom.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com>`

```
Please see the Application Programming Guide for information on how to get a
"PARM" value into the Linkage Section of an IBM (MVS - OS/390) program.  The
brief summary is that it does NOT matter what type of data is passed
(numeric or alphanumeric) but that your linkage section should look like the
following:


         LINKAGE SECTION.
        01  PARMDATA.
             05  STRINGLEN             PIC 999  USAGE COMP.
             05  STRINGPARM          PIC X(6).

(This example is taken directly from the VS COBOL II application programming
guide - but the same technique can be used with any MVS-type COBOL)

Note: You can also use USAGE BINARY instead of COMP.  It would also be
possible to change the PIC 999 to PIC S9(04) (and I think most people do
this) HOWEVER, there is an MVS restriction of only 255 (I think) characters
in a PARM, so you will never need more than 3 "valid" digits.
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KIFK1.144$4E6.1838670@storm.twcol.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com> <6tehjd$5l1@dfw-ixnews5.ix.netcom.com>`

```
>brief summary is that it does NOT matter what type of data is passed
>(numeric or alphanumeric) but that your linkage section should look like
the
>following:
>         LINKAGE SECTION.
…[7 more quoted lines elided]…
>in a PARM, so you will never need more than 3 "valid" digits.



Not sure exactly what you mean here, but my comment didn't refer to the
STRINGLEN size or value. I was referring to the size of the actual field
being passed. And to that I say the smallest numeric variable available to
COBOL is 2 bytes in length. It may be PIC 9, but COBOL uses 2 bytes for the
storage of said number. Thus if you passed a HEX value 1 byte in length to
COBOL from a PARM field in JCL, I assumed the passed value would be
converted to a 2 byte numeric field for COBOL to use.

As to the STRINGLEN field length all binary fields have a storage area with
an even number of bytes, regardless of how they are defined. Such as 2,4, or
8. Look at the compile listing and check the byte size of the field usually
listed off to the right of the field in the listing, beyond column 80
somewhere. I have never seen a parm defined as PIC 999. I have always seen
it defined as PIC S9(04) USAGE COMP [or more acurately USAGE BINARY]. Never
sure why, but I assumed it was because binary fields are defined on an even
word boundary in COBOL.

This all may have been fixed with the newer versions of COBOL.
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tfel1$hvp@dfw-ixnews4.ix.netcom.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <R1zK1.122$4E6.1569153@storm.twcol.com> <6tehjd$5l1@dfw-ixnews5.ix.netcom.com> <KIFK1.144$4E6.1838670@storm.twcol.com>`

```

Jeff wrote in message ...
>>brief summary is that it does NOT matter what type of data is passed
>>(numeric or alphanumeric) but that your linkage section should look like
…[9 more quoted lines elided]…
>>this) HOWEVER, there is an MVS restriction of only 255 (I think)
characters
>>in a PARM, so you will never need more than 3 "valid" digits.
>
…[4 more quoted lines elided]…
>being passed.

The technique listed above WILL get you the exact length of the data passed
in the PARM= statement of your JCL - honest!  It will ALWAYS come in as a
two-byte binary field which can be defined - in COBOL - as

      Pic 9 Comp.
      Pic S9 Comp.
      pic  99 Comp.  Pic 999 COMP, Pic 9999 Comp
      Pic S99 Comp. Pic S99 Comp.  Pic S9999 Comp.
        or any of the above with "BINARY" instead of COMP.

That is the way it will come into your linkage section and that is what you
should use.
```

##### ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998091220075900.QAA04772@ladder03.news.aol.com>`
- **References:** `<R1zK1.122$4E6.1569153@storm.twcol.com>`

```
In article <R1zK1.122$4E6.1569153@storm.twcol.com>, "Jeff" <a@a.com> writes:

>
>One possible reason is that COBOL cannot use numbers of length 1. I do mean
…[6 more quoted lines elided]…
>

Making a major assumption here.  In passing a hex value that you have
identified as representing only 1-byte, the system has expanded this to fit
within the smallest possible binary/hex field of 2-bytes.  Most binary fields
are 2,4,or 8-bytes in size.
```

#### ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FD90B3.B2FDFF99@IMN.nl>`
- **References:** `<6t3lg3$jau@news3.force9.net>`

```


Simon,

When passing data from JCL to COBOL, the following convention is used:

1) Only ONE parameter is passed to the COBOL program
2) That ONE parameter consists of two portions: length and content.
3) The length will be binary encoded in TWO bytes
4) 255 is the maximum amount of data you'll get

So code the following in your
LINKAGE SECTION.
01  ParmFromJCL.
    03  LengthOfParm  pic S9999 usage binary.
    03  Contents  pic X(255).

Of course 255 may be lessened.
Defining Contents as a group is also allowed.

No manual at hand, one thing I do not recall: is the length INCLUDING itself or
EXCLUDING?
So if JCL sais EXEC PGM=YourProg,PARM='ABACADABRA'
I don't know if length is 10 or 12.

The Frog
```

##### ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fe14dc.951017@news2.ibm.net>`
- **References:** `<6t3lg3$jau@news3.force9.net> <35FD90B3.B2FDFF99@IMN.nl>`

```
On Mon, 14 Sep 1998 23:54:59 +0200, "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl> wrote:

>When passing data from JCL to COBOL, the following convention is used:
>
…[3 more quoted lines elided]…
>4) 255 is the maximum amount of data you'll get
Not quite.  According to my JCL Reference, the maximum length of the parameter is 100, not
255

>
>So code the following in your
…[3 more quoted lines elided]…
>    03  Contents  pic X(255).

>No manual at hand, one thing I do not recall: is the length INCLUDING itself or
>EXCLUDING?
>So if JCL sais EXEC PGM=YourProg,PARM='ABACADABRA'
>I don't know if length is 10 or 12.

The length is the actual length of the parameter passed, excluding the enclosing
apostropies or brackets

HTH

with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** WOB@my-dejanews.com
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tkgm4$fem$1@nnrp1.dejanews.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <35FD90B3.B2FDFF99@IMN.nl>`

```
In article <35FD90B3.B2FDFF99@IMN.nl>,
  "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl> wrote:
>
>
…[18 more quoted lines elided]…
> No manual at hand, one thing I do not recall: is the length INCLUDING itself
or
> EXCLUDING?
> So if JCL sais EXEC PGM=YourProg,PARM='ABACADABRA'
…[15 more quoted lines elided]…
>

Huib,

The halfword length would be 10 (11 if it was ABRACADABRA). Just kidding.
Anyway, verify the halfword is greater than zero and less than 256 and use
REFERENCE MODIFICATION to extract the parameter in a single MVC. MOVE CONTENTS
(1:LENGTHOFPARM) to WS-PARAMETER.

Cheers,

WOB


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tki71$6@dfw-ixnews8.ix.netcom.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <35FD90B3.B2FDFF99@IMN.nl> <6tkgm4$fem$1@nnrp1.dejanews.com>`

```

WOB@my-dejanews.com wrote in message <6tkgm4$fem$1@nnrp1.dejanews.com>...
>In article <35FD90B3.B2FDFF99@IMN.nl>,
>  "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl> wrote:
  <snips>
>>
>> So code the following in your
…[4 more quoted lines elided]…
>>

>
>Huib,
…[3 more quoted lines elided]…
>REFERENCE MODIFICATION to extract the parameter in a single MVC. MOVE
CONTENTS
>(1:LENGTHOFPARM) to WS-PARAMETER.
>
…[4 more quoted lines elided]…
>
I don't know WHY (maybe I am one of the "old-thinkers" who still numbers
paragraphs), but I would prefer the following to using reference
modification.

   LINKAGE SECTION.
   01  ParmFromJCL.
       03  LengthOfParm  pic S9(03) usage binary.
       03  Contents.
              05  All-Chars occurs 0 to 255 times
                        depending on LengthOFParm.
                    10  Each-Char    Pic X.

P.S. I haven't checked the manual either, but I am 90% certain that the
value of the length field does NOT count the half-word length field itself.
(and as a reminder the data that comes into "Contents" is everything on the
"correct" side of a "/" - things on the "wrong" side are passed to the
IBM/COBOL run-time system itself, e.g. UPSI, SSRANGE, etc)

P.P.S.  Anyone using this technique with LE, Please look up (and understand
the following)
     CBLOPTS - run-time option
     CEE3PRM - callable routine
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

_(reply depth: 4)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FF8633.64DF4C29@IMN.nl>`
- **References:** `<6t3lg3$jau@news3.force9.net> <35FD90B3.B2FDFF99@IMN.nl> <6tkgm4$fem$1@nnrp1.dejanews.com> <6tki71$6@dfw-ixnews8.ix.netcom.com>`

```
William M. Klein wrote:

8<

> I don't know WHY (maybe I am one of the "old-thinkers" who still numbers
> paragraphs), but I would prefer the following to using reference
…[8 more quoted lines elided]…
>                     10  Each-Char    Pic X.

8<
Maybe because you like non-standard COBOL? (occurs 0 to ... i.s.o. occurs 1 to
... ) :-)
The Frog
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298258.71603.27067@kcbbs.gen.nz>`
- **References:** `<35FF8633.64DF4C29@IMN.nl>`

```
In message <<35FF8633.64DF4C29@IMN.nl>> "COBOL Frog  writes:
> 
> >
…[11 more quoted lines elided]…
> The Frog

          OCCURS 0 TO 255 TIMES DEPENDING ON ...

Is perfectly valid standard Cobol with ANSI-85.

Do try and keep up   ;-)
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tpem7$23q@dfw-ixnews10.ix.netcom.com>`
- **References:** `<6t3lg3$jau@news3.force9.net> <35FD90B3.B2FDFF99@IMN.nl> <6tkgm4$fem$1@nnrp1.dejanews.com> <6tki71$6@dfw-ixnews8.ix.netcom.com> <35FF8633.64DF4C29@IMN.nl>`

```
I don't have my '85 Standard with me, but I *know* that it allows 0 (as a
change from '74).  This is how the entire problem with "zero-length group
items" came into the Standard.  If you want a detailed explanation of the
problems that caused, let me know.

COBOL Frog (Huib Klink) wrote in message <35FF8633.64DF4C29@IMN.nl>...
>William M. Klein wrote:
>
…[15 more quoted lines elided]…
>Maybe because you like non-standard COBOL? (occurs 0 to ... i.s.o. occurs 1
to
>... ) :-)
>The Frog
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXEC=..,PARM=.. It works but I don't understand why

_(reply depth: 6)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360171E2.17A7E192@IMN.nl>`
- **References:** `<6t3lg3$jau@news3.force9.net> <35FD90B3.B2FDFF99@IMN.nl> <6tkgm4$fem$1@nnrp1.dejanews.com> <6tki71$6@dfw-ixnews8.ix.netcom.com> <35FF8633.64DF4C29@IMN.nl> <6tpem7$23q@dfw-ixnews10.ix.netcom.com>`

```
Bill, good day!

You wrote:

> I don't have my '85 Standard with me, but I *know* that it allows 0 (as a
> change from '74).

I based myself on my (sometimes correct) own memory and on the (mostly correct)
Micro Focus Docs/help, which state for the format
   OCCURS [ integer-1 TO ] integer-2 TIMES DEPENDING ON data-name-1
the following:
   Where both integer-1 and integer-2 are used, integer-1 must be greater than
zero and integer-2 must be greater than integer-1.

Are you sure zero is allowed? Perhaps in the next standard?

>  This is how the entire problem with "zero-length group
> items" came into the Standard.  If you want a detailed explanation of the
> problems that caused, let me know.

I'm interested! If you don't need to type the story but have it at hand, please
email me!

CU
Huib

snipped highlight:

> COBOL Frog (Huib Klink) wrote in message <35FF8633.64DF4C29@IMN.nl>...
> >William M. Klein wrote:
> >>               05  All-Chars occurs 0 to 255 times
> > non-standard COBOL? (occurs 0 to ... i.s.o. occurs 1 to ...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
