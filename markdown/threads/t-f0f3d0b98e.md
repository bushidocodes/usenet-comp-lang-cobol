[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL options

_5 messages · 4 participants · 1996-08_

---

### COBOL options

- **From:** "jcas..." <ua-author-7154876@usenetarchives.gap>
- **Date:** 1996-08-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ub19v$ckp@news.dcccd.edu>`

```

We're still using IBM OS/VS COBOL 2.4 (5740-CB1, circa 1982)
and I'm trying to specify some parameters on the //EXEC card.
Unfortunately, it's an excessive number (>104 chars).
What I'd prefer to do is to set the default options in the
compiler itself, but I don't have any documentation on how
to do this to something this old.
Can any of you ol'COBOLers help me out?
```

#### ↳ Re: COBOL options

- **From:** "bakulesh thakker ph (r) 507 289 1671" <ua-author-17087343@usenetarchives.gap>
- **Date:** 1996-08-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0f3d0b98e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4ub19v$ckp@news.dcccd.edu>`
- **References:** `<4ub19v$ckp@news.dcccd.edu>`

```

Have you tried CBL option cards which are supposed to be part of your
source?

-Bakulesh Thakker
```

##### ↳ ↳ Re: COBOL options

- **From:** "jcas..." <ua-author-7154876@usenetarchives.gap>
- **Date:** 1996-08-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0f3d0b98e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0f3d0b98e-p2@usenetarchives.gap>`
- **References:** `<4ub19v$ckp@news.dcccd.edu> <gap-f0f3d0b98e-p2@usenetarchives.gap>`

```

In article <4ub2hf$r.··.@tri··o.edu>, vn0··.@pos··o.edu
says...
›
› Have you tried CBL option cards which are supposed to be part of your
…[3 more quoted lines elided]…
›

I'm unaware of such a facility. Could it be DOS/VSE related?
I'm running MVS/XA 2.2.0.
```

###### ↳ ↳ ↳ Re: COBOL options

- **From:** "thakker..." <ua-author-7089904@usenetarchives.gap>
- **Date:** 1996-08-09T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0f3d0b98e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0f3d0b98e-p3@usenetarchives.gap>`
- **References:** `<4ub19v$ckp@news.dcccd.edu> <gap-f0f3d0b98e-p2@usenetarchives.gap> <gap-f0f3d0b98e-p3@usenetarchives.gap>`

```

In article <4ug30r$g.··.@new··d.edu>, jca··.@dc··d.edu (John Cassidy) says:
› 
› In article <4ub2hf$r.··.@tri··o.edu>, vn0··.@pos··o.edu 
› says...
›› 
 
› 
› I'm unaware of such a facility. Could it be DOS/VSE related?
› I'm running MVS/XA 2.2.0.
› 
The CBL statement is very much an IBM mainframe cobol concept. I am very
sure it was there right from OS/360 days! I have given some info below:

Syntax:

-> CBL
->

A cbl-statement is placed before the Identification division header of program.
It can be preceded by a sequence number in columns 1 to 6. First character of
sequence number must be numeric. The wod CBL must begin in column 8
or after. If sequence number is not specified CBL can begin in column 1 or
after. The cbl-statement must end before column 72, and options cannot
continue across multiple cbl-statements. However, you can use more
than one cbl-statement. If you use multiple cbl-statements, they must
follow one another with no intervening statements of any other type.
The cbl-statement must be placed before any comment lines or other
compiler directing statements. This information is from: "VS COBOL II,
Application Programming Lnaguage Reference"

I have used standard garmmar notation. stands for any compiler
option. Compiler options are recognised in the order of precedence:

(Highest precedence) Fixed installation defaults
cbl-statement options
JCL PARM options
(Lowest precedence) Non-fixed installtion defaults

The manual "VS COBOL II, Application Programming Guide for MVS and CMS"
describes how conflicting options are tackled. For more info respond or email.

Regards. -Bakulesh Thakker.
```

#### ↳ Re: COBOL options

- **From:** "cmcam..." <ua-author-17086272@usenetarchives.gap>
- **Date:** 1996-08-11T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0f3d0b98e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4ub19v$ckp@news.dcccd.edu>`
- **References:** `<4ub19v$ckp@news.dcccd.edu>`

```

In <4ub19v$c.··.@new··d.edu>, jca··.@dc··d.edu (John Cassidy) writes:
› We're still using IBM OS/VS COBOL 2.4 (5740-CB1, circa 1982)
› and I'm trying to specify some parameters on the //EXEC card. 
…[5 more quoted lines elided]…
› 
John,
As some other posters have said, you could try using the CBL statement to supply
options to the compiler. However, I have a couple of other tips for you. I
assume you have access to the Programmer's Guide for OS/VS COBOL. If not, my
first tip is GET ONE!

First, compile with no options whatsoever, to get the compiler to show you the
default options. It is hard to imagine you need to change so many things that
you wouldn't have room in the PARM field. Match the defaults to what you're
specifying, and eliminate duplicates.

Second, refer to the figure that shows "Significant Characters" for each cmpiler
option. For example, SOURCE can be written SOU, CSYNTAX = CSY, etc. This can
save a lot of characters.
Colin Campbell,
Computer Sciences Corp.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
