[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM To Microsoft 5.0 Conversion

_5 messages · 5 participants · 1998-11_

---

### RM To Microsoft 5.0 Conversion

- **From:** John Simpson <jasimp@earthlink.net>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3641E4B8.B8CA0E62@earthlink.net>`

```
I have a client running an application in RM cobol in a unix
environment. They want to switch over to a Windows based system and
Microsoft networking. 

Has anyone had any experience doing the above mentioned cobol
conversion? The Microsoft compiler has an RM directive, but I suspect
it's for data structure (comp conversion) rather that code syntax. The
biggest problem that I see is the accept/display conversion. Data
conversion will be no problem.

Any insight on this will be greatly appreciated.

Thanks in advance.

John Simpson
```

#### ↳ Re: RM To Microsoft 5.0 Conversion

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71t41j$q2n@dfw-ixnews9.ix.netcom.com>`
- **References:** `<3641E4B8.B8CA0E62@earthlink.net>`

```
If you are considering using a product that is called "Microsoft COBOL" then
you are using a VERY ANCIENT product.  Microsoft has not had their own COBOL
compiler for years and hasn't even sold anyone else's for many years.  (The
old MS compiler did have an RM directive, so this may be what you are
looking at - but I sure would stop looking ASAP.)

John Simpson wrote in message <3641E4B8.B8CA0E62@earthlink.net>...
>I have a client running an application in RM cobol in a unix
>environment. They want to switch over to a Windows based system and
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: RM To Microsoft 5.0 Conversion

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298309.66923.20764@kcbbs.gen.nz>`
- **References:** `<71t41j$q2n@dfw-ixnews9.ix.netcom.com>`

```
In message <<71t41j$q2n@dfw-ixnews9.ix.netcom.com>> "William M. Klein" <wmklein@ix.netcom.com> writes:
> you are using a VERY ANCIENT product.  Microsoft has not had their own COBOL
> compiler for years and hasn't even sold anyone else's for many years.  (The
> old MS compiler did have an RM directive, so this may be what you are
> looking at - but I sure would stop looking ASAP.)

Microsoft Cobol 5.0 is dated 1992, this doesn't count as
Very Ancient to me (but then I remember when Sgt Pepper's
came out).  It is actually a rebadged and repackaged MF Cobol
3.0.  It does Windows and DOS and XM (but not OS/2, how odd).
I still use it, though I do have MF 3.4, due to more liberal
licencing terms.

> 
> John Simpson wrote in message <3641E4B8.B8CA0E62@earthlink.net>...
…[8 more quoted lines elided]…
> >conversion will be no problem.

There is a manual with MS Cobol 5.0 called Compatability Guide.
This has some chapters on converting RM Cobol, including the
use of Convert3 to take the data files.
```

#### ↳ Re: RM To Microsoft 5.0 Conversion

- **From:** "Uwe Baemayr" <uwe-nospam@liant.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OdcFqPUC#GA.322@news2.texas.rr.com>`
- **References:** `<3641E4B8.B8CA0E62@earthlink.net>`

```
John Simpson wrote in message <3641E4B8.B8CA0E62@earthlink.net>...

>I have a client running an application in RM cobol in a unix
>environment. They want to switch over to a Windows based system and
…[6 more quoted lines elided]…
>conversion will be no problem.

Why not just upgrade to the RM/COBOL for Windows develoment system?
Your programs can then simply be recompiled, and sometimes you don't
even need to do that.  Your data files will also move over without
conversion.  Finally, your Windows systems and your UNIX systems can
operate on the same data files, if your networking is set up properly.
See:

    http://www.liant.com/products/language/rm/index.html

You can also call (800) RMCOBOL or (512) 343-1010 for more information.

--- Uwe Baemayr [Liant Software]
```

#### ↳ Re: RM To Microsoft 5.0 Conversion

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<722j4l$8o6@lotho.delphi.com>`
- **References:** `<3641E4B8.B8CA0E62@earthlink.net>`

```
Why not just buy a R/M runtime for Windows and run the program 
on Windows? Chances are it will run the first time, and 
certainly the second or third time with inly minor fiddling. 

-Paul

(p.s. - I am *not* a R/M fan, I like the products, I don't like
the company's sales attitude.) 



John Simpson (jasimp@earthlink.net) wrote:
: I have a client running an application in RM cobol in a unix
: environment. They want to switch over to a Windows based system and
: Microsoft networking. 

: Has anyone had any experience doing the above mentioned cobol
: conversion? The Microsoft compiler has an RM directive, but I suspect
: it's for data structure (comp conversion) rather that code syntax. The
: biggest problem that I see is the accept/display conversion. Data
: conversion will be no problem.

: Any insight on this will be greatly appreciated.

: Thanks in advance.

: John Simpson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
