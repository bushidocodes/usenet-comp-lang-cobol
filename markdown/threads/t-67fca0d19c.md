[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What do these cobol types look like?

_5 messages · 5 participants · 2001-10_

---

### What do these cobol types look like?

- **From:** Steve <sfang88@yahoo.com>
- **Date:** 2001-10-08T14:00:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC1E9B1.4EB9F8E7@yahoo.com>`

```
Can anyone give some example for each of those cobol types?
COBOLAlphaNumericEditedType
COBOLNumericEditedType
COBOLDBCSType
COBOLInternalFloatType
COBOLExternalFloatType

Thanks!

Steve
```

#### ↳ Re: What do these cobol types look like?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-10-09T00:04:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Iarw7.439$ZJ.601064@paloalto-snr2.gtei.net>`
- **References:** `<3BC1E9B1.4EB9F8E7@yahoo.com>`

```

http://www.flexus.com/downloads.html

Get file cobdata.zip, a freeware tutorial on COBOL data types.

Also, ANY "Welcome to COBOL" or "COBOL 101" book will explain all types
except maybe DBCS, which is not actually a COBOL thing, its an O/S thing.
(But then so is external float, sorta).
```

##### ↳ ↳ Re: What do these cobol types look like?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-09T02:44:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC26612.A77CDAA3@home.com>`
- **References:** `<3BC1E9B1.4EB9F8E7@yahoo.com> <Iarw7.439$ZJ.601064@paloalto-snr2.gtei.net>`

```


Michael Mattias wrote:

> http://www.flexus.com/downloads.html
>
…[4 more quoted lines elided]…
> (But then so is external float, sorta).

Just a follow-up on Michael's message re DBCS :-

"Makes the Compiler accept characters of the Double-byte Character Set (DBCS)
for use in ideographic languages such as Japanese, Chinese and Korean " -
straight from my on-line help.

Jimmy, Calgary AB
```

#### ↳ Re: What do these cobol types look like?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-09T00:39:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pu2p9$e87$1@slb5.atl.mindspring.net>`
- **References:** `<3BC1E9B1.4EB9F8E7@yahoo.com>`

```
You don't tell us your platform, compiler, or more importantly WHY you are
asking this question.  If this is a "homework" assignment, then I suggest
that you check the references that you are using for your class.  If this is
to "inter-act" with a program in another programming language, then your
question probably won't get you the information that you need/want.
Definitely some of the forms (DBCS and internal/external floating point) are
VERY compiler dependent today.

HOWEVER, just to give you the "absolutely" correct answer (for the NEXT
COBOL Standard),  I thought I would give you the full answer - that probably
won't answer your question at all:

To define an item as alphanumeric-edited, character-string-1 shall include
- at least one symbol 'A' or one symbol 'X', and
- at least one of the symbols from the set 'B', '0', '/'.

To define an item as numeric-edited, one of the following options shall be
specified:
a) To produce a fixed-point edited result, character-string-1 shall include:
- at least one symbol 'Z'; or
- at least one symbol '*'; or
- at least two identical symbols from the set '+', '-', currency symbol; or
- at least one symbol '9' and at least one of the symbols from the set 'B',
'CR', 'DB', '0', '/', ',',
'.', '+', '-', the currency symbol.
b) To produce a floating-point edited result <external floating point>,
characters-string-1 shall consist of two parts, separated without any
spaces, by the symbol 'E'. The first part represents the significand; the
second part represents the exponent.
The significand shall be a valid character-string for either a numeric item
or a numeric-edited item for a
fixed-point result.
The exponent shall be '+9', '+99', '+999', or '+9(n)' where n = 1, 2, or 3.

To define an item as national <DBCS>, character-string-1 shall contain only
one or more occurrences of the symbol 'N'.

The usages float-short, float-long and float-extended define signed numeric
data items that are held in a floating-point format suitable for the machine
on which the runtime module is to run <internal floating point>. The size
and permitted range of values for these fields is defined by the
implementor. Any value that may be held in a data item of usage float-short
shall also be expressible in a data item of usage float-long. Any value that
may be held in a data item of usage float-long shall also be expressible in
a data item of usage float-extended.

  ***

From the terminology used ("internal/external floating point" and "DBCS") it
wouldn't surprise me if this question has to do with an IBM or
IBM-compatible environment.  If  so, you can find their definitions of such
terms at:

http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igylr205/5.3.11.3
    and
http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igylr205/5.3.16.1
```

#### ↳ Re: What do these cobol types look like?

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-15T16:52:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VuEy7.29836$ev2.36524@www.newsranger.com>`
- **References:** `<3BC1E9B1.4EB9F8E7@yahoo.com>`

```
On Mon, 08 Oct 2001 14:00:18 -0400, in article <3BC1E9B1.4EB9F8E7@yahoo.com>,
Steve stated 
>
>Can anyone give some example for each of those cobol types?

Hope this helps a little Steve.....

>COBOLAlphaNumericEditedType pic xxxbxxbxxxx 
(adds blanks for ssn convert to '-' later with inspect verb)

>COBOLNumericEditedType      pic zz9          (shows one digit for 009)

>COBOLDBCSType               Never used and am clueless what it is used for.
(Double Byte Character Data)

99v99 is a fixed decimal point these below are not fixed and will not line up
necessarily.  I have never used them and do not know what they look when
displayed.

>COBOLExternalFloatType (I have not used)  
>
This may be referring to the floating dollar sign $$$$$9.99
>Thanks!
>
Technical manuals and school books are introducing new terms.
In my manual, External Floating-Point refers to not being in a fixed format.
05  Result   pic -9v9(9)E-99.  (no value clause allowed)
I am guessing this means the decimal point can be anywhere, but there is a
decimal point and it has 9 digits.  


>COBOLInternalFloatType     ( I have never used this)

Internal floating point is for comp-1 or comp-2

A picture clause is not allowed.

05 Result            Usage Comp-1 Value 06.23E-24

This is like 06.23 X 10^-24
or something like:
".00000000000000000000000623";
that is a mouth full.

As a Note, COMP is defined by the compiler, and many compilers treat how it is
applied differently.  I use the IBM Mainframe COBOL LE for VSE/ESA compiler.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
