[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FUNCTION Reserved Word

_5 messages · 2 participants · 1999-09_

---

### FUNCTION Reserved Word

- **From:** "Steve Wright" <swright@bfsec.bt.co.uk>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7snpcs$9lg$1@pheidippides.axion.bt.co.uk>`

```
Folks,

Does anyone know a web address or can give me a brief description of the
FUNCTION keyword.  How do you define a function and is it only arithmetic
operations that can be performed with it ?

Any help much appreciated.

Cheers
Steve
```

#### ↳ Re: FUNCTION Reserved Word

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7snqdq$787@dfw-ixnews10.ix.netcom.com>`
- **References:** `<7snpcs$9lg$1@pheidippides.axion.bt.co.uk>`

```
Tell us which compiler, which release, and on which platform you are
working - and we can point you to the correct documentation.  The original
ANSI'85 Standard did not include support for Intrinsic Functions - they were
added by an amendment in '89.  Therefore, your compiler may NOT support them
(yet?).  If your compiler does support them, it may include some additional
ones as extensions.

Current COBOL does not support "user-defined" functions.  However, in MOST
cases, those who are looking for "user-defined functions" in COBOL can get
the exact same functionality (or at least what they are really looking for)
by writing COBOL subprograms.
```

##### ↳ ↳ Re: FUNCTION Reserved Word

- **From:** "Steve Wright" <swright@bfsec.bt.co.uk>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7snrbb$aeu$1@pheidippides.axion.bt.co.uk>`
- **References:** `<7snpcs$9lg$1@pheidippides.axion.bt.co.uk> <7snqdq$787@dfw-ixnews10.ix.netcom.com>`

```
The current compiler does not support functions, but we are going to be
upgrading to a new compiler soon.

The platform is an IBM MVS Mainframe and the new Compiler is COBOL for MVS
and VM and is part of LE/370.  That's all the information I have on the new
compiler.  I'm just trying to find out about the features of the new
compiler, but have drawn a blank with our own people about this one.

Thanks
Steve
William M. Klein wrote in message <7snqdq$787@dfw-ixnews10.ix.netcom.com>...
>Tell us which compiler, which release, and on which platform you are
>working - and we can point you to the correct documentation.  The original
>ANSI'85 Standard did not include support for Intrinsic Functions - they
were
>added by an amendment in '89.  Therefore, your compiler may NOT support
them
>(yet?).  If your compiler does support them, it may include some additional
>ones as extensions.
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: FUNCTION Reserved Word

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sns39$b85@dfw-ixnews8.ix.netcom.com>`
- **References:** `<7snpcs$9lg$1@pheidippides.axion.bt.co.uk> <7snqdq$787@dfw-ixnews10.ix.netcom.com> <7snrbb$aeu$1@pheidippides.axion.bt.co.uk>`

```
OK,
  With that information, I can help.  First, check out
     http://www-4.ibm.com/software/ad/cobol/coblib.htm#COBOLOS390VM

which has links to all the latest IBM COBOL's latest manuals.

Three that you want to look at are:

1) Migration Guide
     (which will tell you everything - well lots - about what will be
new/changing)

2) The LRM
    (which gives you the syntax for functions)

3) The Programming Guide
   (which tells you how to use all the various types of functions).

"Normally" I would give you the web-links for all the manuals, but the IBM
bookserver seems to be "Monday morning busy" - and I can't get a link to it
at the moment.
```

###### ↳ ↳ ↳ Re: FUNCTION Reserved Word

_(reply depth: 4)_

- **From:** "Steve Wright" <swright@bfsec.bt.co.uk>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sns80$ar5$1@pheidippides.axion.bt.co.uk>`
- **References:** `<7snpcs$9lg$1@pheidippides.axion.bt.co.uk> <7snqdq$787@dfw-ixnews10.ix.netcom.com> <7snrbb$aeu$1@pheidippides.axion.bt.co.uk> <7sns39$b85@dfw-ixnews8.ix.netcom.com>`

```
Thanks for the help Bill

Much appreciated.

Thanks

Steve
William M. Klein wrote in message <7sns39$b85@dfw-ixnews8.ix.netcom.com>...
>OK,
>  With that information, I can help.  First, check out
…[29 more quoted lines elided]…
>> The platform is an IBM MVS Mainframe and the new Compiler is COBOL for
MVS
>> and VM and is part of LE/370.  That's all the information I have on the
>new
…[50 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
