[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

_7 messages · 3 participants · 2004-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** Vincent Danion <vdaNOniSPAMon@scort.com>
- **Date:** 2004-11-16T14:47:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vuenqF2p8il6U1@uni-berlin.de>`

```
Hello,

I have a question about internal sign encoding.

"IBM Enterprise COBOL for z/OS - Language Reference - V3R3" says (p.217):

"PACKED-DECIMAL [...] The sign representation uses the same bit 
configuration as the 4-bit sign representation in zoned decimal fields."

But "IBM Websphere Studio COBOL for Windows V5.11" gives examples (p.37) 
which shows that the 4-bit sign representation depends on usage mode:

My understanding is that:

- For (not separate) DISPLAY usage, it depends on the code:
   EBCDIC: + is C, - is D and unsigned is F
   ASCII: + and unsigned is 3, and - is 7.

- For PACKED-DECIMAL usage, it is fixed: + is C, - is D and unsigned is F.

Am I right ?

Thanks
```

#### ↳ Re: Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-16T20:05:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C4tmd.5194925$6p.840234@news.easynews.com>`
- **References:** `<2vuenqF2p8il6U1@uni-berlin.de>`

```
Vincent,
   You have mixed "apples and oranges" - although you may well be correct that 
there is an error in the documentation.

What the Enterprise COBOL LRM states *is* true for the Enterprise COBOL 
compiler.

It is *NOT* (always) true for IBM's COBOL for Windows.  The sign-nibble on the 
PC (with the IBM compiler - and several others) is the same between 
Packed-Decimal and Zoned Decimal when the compiler is in "EBCDIC" mode but IS 
not the same when in ASCII mode.

Some compilers (for example Micro Focus) has an option for working in ASCII 
mode - but using EBCDIC sign-nibbles (or vice versa - I can't remember off the 
top of my head).  However, this is NOT true for the IBM Windows compiler.

I don't see a separate web page for the "IBM Websphere Studio COBOL for Windows 
V5.11" manuals, but the VisualAge COBOL (predecessor product) is at:
   http://www-306.ibm.com/software/awdtools/cobol/va/library/

and that seems to indicate that it uses the same LRM as the "mainframe"  (older 
version IBM COBOL for OS/390 & VM) LRM.  If that is still the case with the 
current Windows compiler, then what you have found is a "bug".
```

##### ↳ ↳ Re: Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** Vincent Danion <vdaNOniSPAMon@scort.com>
- **Date:** 2004-11-17T10:47:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<300l0vF2q72joU1@uni-berlin.de>`
- **In-Reply-To:** `<C4tmd.5194925$6p.840234@news.easynews.com>`
- **References:** `<2vuenqF2p8il6U1@uni-berlin.de> <C4tmd.5194925$6p.840234@news.easynews.com>`

```
William,

Thank you for your answer and congratulation for your Faq: it is very 
documented and interesting.

William M. Klein wrote:

>    You have mixed "apples and oranges" - although you may well be correct that 
> there is an error in the documentation.
…[7 more quoted lines elided]…
> not the same when in ASCII mode.

OK, I understand that. It is like in ASCII mode the DISPLAY sign 
representation should be compatible with ASCII 7 bits (therefore lower 
than 7F), while the PACKED sign representation need not to be 
"printable" (ie it can be the same Ci, Di or Fi than in EBCDIC), isn't it ?

> Some compilers (for example Micro Focus) has an option for working in ASCII 
> mode - but using EBCDIC sign-nibbles (or vice versa - I can't remember off the 
…[4 more quoted lines elided]…
>    http://www-306.ibm.com/software/awdtools/cobol/va/library/

In fact, there is here:

http://www-306.ibm.com/software/awdtools/cobol/library/

You can find on this page two links regarding "COBOL for Windows", one 
for Language Reference and the other for Programming Guide.

> and that seems to indicate that it uses the same LRM as the "mainframe"  (older 
> version IBM COBOL for OS/390 & VM) LRM.  If that is still the case with the 
> current Windows compiler, then what you have found is a "bug".

Indeed there is now a separate LRM for Windows but it says exactly the 
same thing regarding 4-bit sign representation (p.213). IMHO, this is at 
least confusing...

I have another question about the sign position. I was thinking that the 
default was TRAILING, but the IBM Websphere Studio COBOL PGM for Windows 
V5.11 shows (p. 37 again) the following example:

For "PIC S9999 DISPLAY", the value -1234 is encoded like this (NATIVE):
71 32 33 34

For "PIC S9999 DISPLAY", the value -1234 is encoded like this (EBCDIC):
F1 F2 F3 D4

Therefore, in the first case, the sign seems to be held by the first 
byte (71)... but I found no mention of this particularity. Do you have 
an idea about that ?

Best Regards,
```

###### ↳ ↳ ↳ Re: Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-18T04:18:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<doVmd.4692231$ic1.447539@news.easynews.com>`
- **References:** `<2vuenqF2p8il6U1@uni-berlin.de> <C4tmd.5194925$6p.840234@news.easynews.com> <300l0vF2q72joU1@uni-berlin.de>`

```
The LRM seems to contradict the examples in the PG.  I have sent a query to one 
of my "usually reliable sources" in IBM.

My *guess* is that it is the LRM that is wrong and that for some reason 
WebSphere COBOL for Windows defaults to "leading" rather than trailing signs. 
If this is true, it would cause a medium serious "migration inhibitor" for 
people trying to migrate existing IBM mainframe COBOL applications to that 
environment  (as redefines that assume trailing are fairly common).

However, as I don't have the product myself, I'll wait to see what response (if 
any) I receive.
```

#### ↳ Re: Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** alistair@ld50macca.demon.co.uk (Alistair Maclean)
- **Date:** 2004-11-18T14:56:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d487f04c.0411181456.52e39679@posting.google.com>`
- **References:** `<2vuenqF2p8il6U1@uni-berlin.de>`

```
Vincent Danion <vdaNOniSPAMon@scort.com> wrote in message news:<2vuenqF2p8il6U1@uni-berlin.de>...
> Hello,
> 
…[20 more quoted lines elided]…
> Thanks

Note that E is also treated as a sign. I had a blazing row with
someone who told me this and couldn't believe it when I ran a test (on
t'IBM mainframe).
```

##### ↳ ↳ Re: Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-18T23:10:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rZ9nd.3224041$yk.503744@news.easynews.com>`
- **References:** `<2vuenqF2p8il6U1@uni-berlin.de> <d487f04c.0411181456.52e39679@posting.google.com>`

```
NOTE WELL:
   with current (currently supported) IBM mainframe COBOLs whether or not A, B, 
and E are (or are not) considered "valid" sign-nibbles is determined by an 
installation (not user) compiler option.

See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3C120/2.41

This, of course, has nothing to do with what Assembler or machine instructions 
allow.  There are also rules about how other compiler options impact sign 
handling for COBOL - and there used to be a "usermod" for older COBOL's to do 
similar things.
```

###### ↳ ↳ ↳ Re: Internal sign encoding in DISPLAY and PACKED-DECIMAL usage

- **From:** Vincent Danion <vdaNOniSPAMon@scort.com>
- **Date:** 2004-11-22T10:03:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<30doaiF2tdil1U1@uni-berlin.de>`
- **In-Reply-To:** `<rZ9nd.3224041$yk.503744@news.easynews.com>`
- **References:** `<2vuenqF2p8il6U1@uni-berlin.de> <d487f04c.0411181456.52e39679@posting.google.com> <rZ9nd.3224041$yk.503744@news.easynews.com>`

```
William M. Klein wrote:

Hello,

> NOTE WELL:
>    with current (currently supported) IBM mainframe COBOLs whether or not A, B, 
> and E are (or are not) considered "valid" sign-nibbles is determined by an 
> installation (not user) compiler option.

As far as I have understood, it seems that most compilers are accepting 
different nibbles as valid, but use precise values when they are coding 
the numbers.

> See:
>   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3C120/2.41

Thanks. Cobol compilers seems to be highly configurable ! Do you see any 
reason (interoperability ?) why people would have configured a specific 
sign encoding ?

For instance, OS/400 compilers generally use F for unsigned or 
positives, except if CHGPOSSGN option is set (in this case, they use C).
Does anybody know if this option is often used on iSeries ?

> This, of course, has nothing to do with what Assembler or machine instructions 
> allow.  There are also rules about how other compiler options impact sign 
> handling for COBOL - and there used to be a "usermod" for older COBOL's to do 
> similar things.

Yes, I understand.

Regarding my initial question, we have done the test (under VA Cobol for 
a CICS on NT): the sign nibble is trailing as expected. Therefore, there 
is a bug in "IBM Websphere Studio COBOL PGM for Windows V5.11" p.37:

<quote>
For "PIC S9999 DISPLAY", the value -1234 is encoded like this (NATIVE):
71 32 33 34
</quote>

should be read as:

<quote>
For "PIC S9999 DISPLAY", the value -1234 is encoded like this (NATIVE):
31 32 33 74
</quote>

Have a nice week
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
