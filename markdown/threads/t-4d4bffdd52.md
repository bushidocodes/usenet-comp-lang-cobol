[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using Fujitsu COBOL V3 on Sun Solaris together with a C main program

_7 messages · 6 participants · 1999-03 → 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Using Fujitsu COBOL V3 on Sun Solaris together with a C main program

- **From:** smDelta@t-online.de (Martin Herbst)
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d7hnp$hla$1@news08.btx.dtag.de>`

```
I created a shared library from a COBOL subprogram using the Fujitsu COBOL
Compiler Version 3 on a Sun Solaris. If I try to load this library with the
dlopen function from a program written in C, I get the following error
message:  symbol JMP1TJOB: referenced symbol not found.
Can anybody help me and send some information about how to create the COBOL
subprogram and how to link the C main program.

Martin Herbst
smDelta GmbH
http://www.delta-software.de
```

#### ↳ Re: Using Fujitsu COBOL V3 on Sun Solaris together with a C main program

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d7uis$bbs$1@news.igs.net>`
- **References:** `<7d7hnp$hla$1@news08.btx.dtag.de>`

```
You may have a problem with case sensitivity. I have seen this error in
calling C from Cobol fairly often, and it is usually fixed by using the
Cobol option that turns off link sensitively to case.  Going in the opposite
direction, I do not know.

Martin Herbst wrote in message <7d7hnp$hla$1@news08.btx.dtag.de>...
>I created a shared library from a COBOL subprogram using the Fujitsu COBOL
>Compiler Version 3 on a Sun Solaris. If I try to load this library with the
…[11 more quoted lines elided]…
>
```

#### ↳ Re: Using Fujitsu COBOL V3 on Sun Solaris

- **From:** "Hajo Schepker" <schepker@geocities.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dgdb9$alr$1@namib.north.de>`
- **References:** `<7d7hnp$hla$1@news08.btx.dtag.de>`

```
I did'nt know that fujitsu makes compiler for solaris.
Can it be downloaded from www.adtools.com?
Dows it run under X?

Thanks
H. Schepker
www.schepker.de
```

##### ↳ ↳ Re: Using Fujitsu COBOL V3 on Sun Solaris

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-QuLNM7tRXrKS@Dwight_Miller.iix.com>`
- **References:** `<7d7hnp$hla$1@news08.btx.dtag.de> <7dgdb9$alr$1@namib.north.de>`

```
On Thu, 25 Mar 1999 11:27:32, "Hajo Schepker" <schepker@geocities.com>
wrote:

> I did'nt know that fujitsu makes compiler for solaris.
> Can it be downloaded from www.adtools.com?
> Dows it run under X?

You can get it by ordering the CD, or if you get my book:
Sams Teach Yourself COBOL in 24 Hours, there is also a version on the 
CD that comes with the book.

Don't know about "running under X".  I'm not very familiar with Unix.
```

###### ↳ ↳ ↳ Re: Using Fujitsu COBOL V3 on Sun Solaris

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36fc0a76.34024414@news.enter.net>`
- **References:** `<7d7hnp$hla$1@news08.btx.dtag.de> <7dgdb9$alr$1@namib.north.de> <Jl0PnHJ5PvPd-pn2-QuLNM7tRXrKS@Dwight_Miller.iix.com>`

```
redsky@ibm.net (Thane Hubbell) wrote:

>On Thu, 25 Mar 1999 11:27:32, "Hajo Schepker" <schepker@geocities.com>
>wrote:
…[10 more quoted lines elided]…
>

Thane:

Hajo is just wondering if it either:

A. Supports the X Windows (Motif GUI environment) or
B. Can run in a character mode window under Motif.

I'd venture to say that he's wondering whether or not it supports the
Motif GUI environment.

My understanding is that it does not, but perhaps Ron Langer of
Fujitsu can correct me on this if I am wrong.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Using Fujitsu COBOL V3 on Sun Solaris

- **From:** "Gary Roush" <gkr@adtools.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0iO2.249$Bs3.33798@news20.ispnews.com>`
- **References:** `<7d7hnp$hla$1@news08.btx.dtag.de> <7dgdb9$alr$1@namib.north.de>`

```
Hajo,

There is no V3 for Sun Solaris. The compiler for V4 only will run on the
Sun Solaris platform and only if you purchase it specifically for that
platform. It is explained on the website at: http://www.adtools.com  Look
up products and then click on Sun Solaris and go from there.  Hope this
helps.

Regards,
Gary Roush
Fujitsu COBOL Support

-----------

Hajo Schepker wrote in message <7dgdb9$alr$1@namib.north.de>...
>I did'nt know that fujitsu makes compiler for solaris.
>Can it be downloaded from www.adtools.com?
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Using Fujitsu COBOL V3 on Sun Solaris

- **From:** "Hajo Schepker" <schepker@geocities.com>
- **Date:** 1999-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e12mh$56$1@namib.north.de>`
- **References:** `<7d7hnp$hla$1@news08.btx.dtag.de>`

```
I did'nt know that fujitsu makes compiler for solaris.
Can it be downloaded from www.adtools.com?
Dows it run under X?

Thanks
H. Schepker
www.schepker.de
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
