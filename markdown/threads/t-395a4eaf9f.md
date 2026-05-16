[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compiler OPtions and CBL Statement

_9 messages · 6 participants · 2003-10 → 2003-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Compiler OPtions and CBL Statement

- **From:** akent29@comcast.net (Arthur M. Kent)
- **Date:** 2003-10-30T15:09:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akent29-3010030711570001@12.242.180.227>`

```
I need to compile a VS-COBOL program which contains some calls to
Assembler modules.  The organization I work for has setup COBOL "Processor
Groups", which are a short hand way of stating Compiler Options. 
Unfortuantely, the processor group which had been used before for this
program now "invokes" the compiler options RMODE=31 and AMODE=ANY.  What I
need are the options RMODE=ANY and AMODE=24.

I understand there is a "CBL (Process)" statement which can be inserted
before the IDENTIFICATION DIVISION sttaement which can accomplis this, but
I am unsure of the exact syntax.  Would it be:

   CBL (AMODE=24, RMODE=ANY)

Any advice/assitance etc. would be appreciared.
```

#### ↳ Re: Compiler OPtions and CBL Statement

- **From:** Colin Campbell <cmcampb@attgloabl.net>
- **Date:** 2003-10-30T10:37:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FA15A59.AB3CD553@attgloabl.net>`
- **References:** `<akent29-3010030711570001@12.242.180.227>`

```
I think you are getting Compiler options and Program Binder (Linkage Editor)
options mixed up.

The relevant COBOL compiler options are DATA(24) or DATA(31), RENT or NORENT,
and RMODE(AUTO) or RMODE(24) or RMODE(ANY).  These determine what AMODE and
RMODE are sent to the Program Binder.

If your "processor group" truly specifies AMODE(ANY) and RMODE(31) to the
Program Binder, you may have a hard time changing it, and you didn't supply
enough information for us to help you.  If these settings are a result of
COBOL compiler options, you can use the CBL statement to override the settings
(unless your shop has designated the options as non-overrideable).

I prefer to write CBL (which can also be specified as PROCESS, and is shown
under that heading in the Programming Guide) starting in the normal COBOL
columns - say, column 8.  You would code:

CBL DATA(24), RMODE(24)

That is all it takes....

"Arthur M. Kent" wrote:

> I need to compile a VS-COBOL program which contains some calls to
> Assembler modules.  The organization I work for has setup COBOL "Processor
…[11 more quoted lines elided]…
> Any advice/assitance etc. would be appreciared.
```

#### ↳ Re: Compiler OPtions and CBL Statement

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-01T06:09:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net>`
- **References:** `<akent29-3010030711570001@12.242.180.227>`

```
What compiler do you mean by "VS-COBOL"
  - OS/VS COBOL
  - VS COBOL II

or some other IBM compiler?

OS/VS COBOL programs are (and can only BE) AMODE(24) and RMODE(24).  If you
try and change these (via a Link-edit override) you will get ABENDs at
run-time.

 VS COBOL II *does* support AMODE(any) and RMODE((31) programs - but these
are determined by various compiler options such a RES, RENT, and DATA.

Both of those compilers are "long out of support" by IBM.

The current IBM compiler *does* include an RMODE compiler option - but ALL
of its code is AMODE(31)

   ***

I think you need to "dig further" into exactly what you are after to get a
"good reply"
```

##### ↳ ↳ Re: Compiler OPtions and CBL Statement

- **From:** Joseph Katnic <usrr@mac.kat>
- **Date:** 2003-11-01T19:57:55+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<011120031957556611%usrr@mac.kat>`
- **References:** `<akent29-3010030711570001@12.242.180.227> <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net>`

```
Lets clear up some confusion on AMODE 31/24.

Firstly AMODE 31 just means that the program is capable of accepting 31
bit addresses for it's variables. It does not a-priori mean that the
program will in fact use 31 bit addresses at run time.

THAT is accomplished by the Language Environment settings for the
program. By default, these will probably be set to allocate storage
above the line for AMODE 31 and below the line for AMODE 24.

This can be changed at runtime:
Specify the following parms in the JCL parameter field;
   ,PARM='STACK(,,BELOW),BELOWHEAP(8K,4K,FREE)/pgm parms'

If the COBOL program is the first program executed (as it must be for
the above to work) then this will force the entire enclave to obtain
storage below the line for all Working-Storage and Local-Storage
assignments.

Also you don't have to run the entire program with below the line
storage. You can leave the defaults as the are and use Language
Environment calls to Allocate a HEAP below the line. Then after you
allocate some storage from this heap and assign it to a Linkage Section
dataname, you can then move the appropriate information into this area
and call the assembler routine using this below the line storage.

All of this is explained in great detail in the Language Environment
manuals, which I would have thought that any mainframe programmer would
have read cover to cover.

In article <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:

> What compiler do you mean by "VS-COBOL"
>   - OS/VS COBOL
…[19 more quoted lines elided]…
> "good reply"
```

###### ↳ ↳ ↳ Re: Compiler OPtions and CBL Statement

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-01T07:14:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vq7cdtbp6n6lcb@corp.supernews.com>`
- **In-Reply-To:** `<011120031957556611%usrr@mac.kat>`
- **References:** `<akent29-3010030711570001@12.242.180.227> <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net> <011120031957556611%usrr@mac.kat>`

```
Joseph Katnic wrote:
> All of this is explained in great detail in the Language Environment
> manuals, which I would have thought that any mainframe programmer would
> have read cover to cover.

You must work with some well-read programmers...  :)
```

###### ↳ ↳ ↳ Re: Compiler OPtions and CBL Statement

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-11-01T20:07:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C336D8.20075301112003@corp.supernews.com>`
- **References:** `<akent29-3010030711570001@12.242.180.227> <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net> <011120031957556611%usrr@mac.kat> <vq7cdtbp6n6lcb@corp.supernews.com>`

```
In article <vq7cdtbp6n6lcb@corp.supernews.com>,
 LX-i <lxi0007@netscape.net> wrote:

> Joseph Katnic wrote:
> > All of this is explained in great detail in the Language Environment
…[3 more quoted lines elided]…
> You must work with some well-read programmers...  :)

Actually most of them are still somewhat green-on-black...;-)
```

###### ↳ ↳ ↳ Re: Compiler OPtions and CBL Statement

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-01T21:25:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bxVob.706$qh2.269@newsread4.news.pas.earthlink.net>`
- **References:** `<akent29-3010030711570001@12.242.180.227> <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net> <011120031957556611%usrr@mac.kat>`

```
Sorry - but your description of AMODE (vs RMODE) is confusing at best.

AMODE is a linkage editor (or binder) attribute.  You can "mark" a program
as AMODE(31) - even if it is not programmed correctly to handle such data.
Furthermore, AMODE (and RMODE) both PRE-date LE; they were introduced with
MVS/XA.

For a program with CORRECTLY set AMODE and RMODE attributes, the following
is true:

1) AMODE(24) - the program only (correctly) understands 24-bit addresses
(for data)
2) AMODE(31) - the program "understands" any 24- or 31-bit address (but not
"above the bar 64-bit addresses)
3) RMODE(24) - the program's INSTRUCTIONS must be loaded below the 16M line
4) RMODE(ANY) - the program's instructions may be loaded anywhere (below the
2G bar) and will execute correctly

  ***

OS/VS COBOL programs *must* be AMODE(24) and RMODE(24) to run - regardless
of whether using the original (now unsupported) OS/VS COBOL run-time or the
LE run-time (and link-edit) libraries

VS COBOL II - programs could have almost any valid combination of AMODE and
RMODE

(currently supported) Enterprise COBOL programs are ALWAYS AMODE(31) which
means that they "understand" 31-bit data addresses - regardless of any
compiler options that are set.  The RMODE for both RENT (compiler option,
not link-edit option) and NORENT programs may be either RMODE(ANY) *or*
RMODE(24) - and this is set by the (relatively new) RMODE compiler option.

It is "valid" to change a link-edit option DOWNWARD (e.g. RMODE(ANY) ->
RMODE(24)   or AMODE(31) -> AMODE(24) ) but not vice versa.  There are even
times that you might want to do this.

If you compile any VS COBOL II or later RENT program with DATA(24), that
means that its working-storage is allocated below the 16M line.  For COBOL
compilers that have LOCAL-STORAGE, where that is allocated is determined by
the LE STACK compiler option.  All enterprise COBOL programs (regardless of
compiler options) can understand LINKAGE section items above the 16M line
(but below the 2G bar).

For LE references on "restrictions" on LE (not linkage-editor/binder
restrictions), see:

  ALL31

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3130/2.3.4

  HEAP

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3130/2.3.24

  STACK

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3130/2.3.52

For a discussion of when/how to override AMODE/RMODE  Linkage Editor
options, see:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igymg202/APPENDIX1.10

"Joseph Katnic" <usrr@mac.kat> wrote in message
news:011120031957556611%usrr@mac.kat...
> Lets clear up some confusion on AMODE 31/24.
>
…[37 more quoted lines elided]…
> > OS/VS COBOL programs are (and can only BE) AMODE(24) and RMODE(24).  If
you
> > try and change these (via a Link-edit override) you will get ABENDs at
> > run-time.
> >
> >  VS COBOL II *does* support AMODE(any) and RMODE((31) programs - but
these
> > are determined by various compiler options such a RES, RENT, and DATA.
> >
> > Both of those compilers are "long out of support" by IBM.
> >
> > The current IBM compiler *does* include an RMODE compiler option - but
ALL
> > of its code is AMODE(31)
> >
> >    ***
> >
> > I think you need to "dig further" into exactly what you are after to get
a
> > "good reply"
```

###### ↳ ↳ ↳ Re: Compiler OPtions and CBL Statement

_(reply depth: 4)_

- **From:** Joseph Katnic <usrr@mac.kat>
- **Date:** 2003-11-02T20:41:50+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<021120032041508126%usrr@mac.kat>`
- **References:** `<akent29-3010030711570001@12.242.180.227> <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net> <011120031957556611%usrr@mac.kat> <bxVob.706$qh2.269@newsread4.news.pas.earthlink.net>`

```
Which all this gobbledegook reduces to :
1. Compile all your programs to run with the biggest address space
AMODE(31). The RMODE is only used to determine where the program will
be loaded. The Current Supported Compiler will automatically give you
RMODE(ANY). The defaults are AMODE(31) RMODE(ANY).
2. Allocate storage below the line for any routines that need it.
This can be accomplished by LE runtime options or via programmer
control using the LE call interface.


In article <bxVob.706$qh2.269@newsread4.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:

> Sorry - but your description of AMODE (vs RMODE) is confusing at best.
> 
…[126 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Compiler OPtions and CBL Statement

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-02T17:51:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hubpb.2204$qh2.1620@newsread4.news.pas.earthlink.net>`
- **References:** `<akent29-3010030711570001@12.242.180.227> <t6Iob.10649$Px2.4368@newsread4.news.pas.earthlink.net> <011120031957556611%usrr@mac.kat> <bxVob.706$qh2.269@newsread4.news.pas.earthlink.net> <021120032041508126%usrr@mac.kat>`

```
Which all boils down to (in answer to the ORIGINAL question) - if you are
trying to interface with OS/VS COBOL modules (which *is* still supported -
if you are using the LE run-time library) that there is NO SIMPLE answer.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
