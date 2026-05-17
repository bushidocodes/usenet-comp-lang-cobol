[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL problem

_8 messages · 5 participants · 1998-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL problem

- **From:** "mshu..." <ua-author-10652@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com>`

```

I am running a DOS program compiled under MicroFocus COBOL/2 Version
2.4.31 L2.3 revision 002. I have been trying to get it to run under
Win95. I have gotten the following error message:
run-time error R6009 not enough space for enviornment

What I have tried to do is:
Add extra enviornment space to config.sys and also in the properties (I
have made it over 5K but it still did not help.)

Any suggestions on how to make a program compiled under this version of
MF COBOL run in WIN95 would be appreciated.
Moshe Shulman msh··.@ix.··m.com    718-438-7340 x21
Empire State Supply
```

#### ↳ Re: MF COBOL problem

- **From:** "mshu..." <ua-author-10652@usenetarchives.gap>
- **Date:** 1998-04-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com>`

```

I am running a DOS program compiled under MicroFocus COBOL/2 Version
2.4.31 L2.3 revision 002. I am doing some changes for Year 2K and I
need to know if the field 'date' can be made to return a valid year 2K
date.

Moshe Shulman msh··.@ix.··m.com    718-438-7340 x21
Empire State Supply
```

##### ↳ ↳ Re: MF COBOL problem

- **From:** "rick smith" <ua-author-44949@usenetarchives.gap>
- **Date:** 1998-04-20T14:08:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cb4ceb4852-p2@usenetarchives.gap>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com> <gap-cb4ceb4852-p2@usenetarchives.gap>`

```


Moshe Shulman wrote in message <6hftd2$p.··.@sjx··m.com>...
› I am running a DOS program compiled under MicroFocus COBOL/2 Version
› 2.4.31 L2.3 revision 002. I am doing some changes for Year 2K and I
…[5 more quoted lines elided]…
› Empire State Supply

If you are referring to "ACCEPT identifier FROM DATE", the answer
is NO. The ACCEPT will always return a DATE as YYMMDD and
cannot be changed.

Rick Smith
------------------------------------------
```

##### ↳ ↳ Re: MF COBOL problem

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cb4ceb4852-p2@usenetarchives.gap>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com> <gap-cb4ceb4852-p2@usenetarchives.gap>`

```

Moshe,

As previously stated the ACCEPT ... FROM DATE will only return a
2 digit year. However, if this version of COBOL supports intrinsic
functions then you could replace the ACCEPT ... FROM DATE with
CURRENT-DATE. For example:

move function current-date to ws-date

This function does return a 4 digit year.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International




Moshe Shulman wrote in message <6hftd2$p.··.@sjx··m.com>...
› I am running a DOS program compiled under MicroFocus COBOL/2 Version
› 2.4.31 L2.3 revision 002. I am doing some changes for Year 2K and I
…[5 more quoted lines elided]…
› Empire State Supply
```

###### ↳ ↳ ↳ Re: MF COBOL problem

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cb4ceb4852-p4@usenetarchives.gap>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com> <gap-cb4ceb4852-p2@usenetarchives.gap> <gap-cb4ceb4852-p4@usenetarchives.gap>`

```

In article <6hhgp7$q.··.@hyp··o.uk>, p.··.@mfl··o.uk says...
› 
› Moshe,
…[8 more quoted lines elided]…
› This function does return a 4 digit year.


Moshe is using 2.4. It doesn't support intrinsic functions as far as I recall.
v2.5 was the first to do that. (At least my 2.5.18 Workbench banner says 'NEW
- Intrinsic Functions')

Apart from that, Moshe, you'll have real problems with XM if you're using that
under Windows95/NT. You need to get hold of an XM v1.4.6 Ref 18. Ask Paddy for
one nicely.

Otherwise, you're going to have to stick to under 640K real mode DOS style
apps. I'm not so sure about the year 2000 compliance of other bits of the
runtime in 2.4. I'd guess that some of the file date/time runtime calls might
not be correct.


Shaun
```

###### ↳ ↳ ↳ Re: MF COBOL problem

_(reply depth: 4)_

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cb4ceb4852-p5@usenetarchives.gap>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com> <gap-cb4ceb4852-p2@usenetarchives.gap> <gap-cb4ceb4852-p4@usenetarchives.gap> <gap-cb4ceb4852-p5@usenetarchives.gap>`

```

Folks,

If you would like a clear statement of Micro Focus' Y2K compliancy then go
to:

http://www.microfocus.com/year2000/y2katmf.htm

and a list of our products which conform to this statement can be found at:

http://www.microfocus.com/year2000/y2kpcom.htm

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International

Shaun C. Murray wrote in message <6hkub3$2eg$2.··.@new··e.net>...
› In article <6hhgp7$q.··.@hyp··o.uk>, p.··.@mfl··o.uk says...
›› 
…[32 more quoted lines elided]…
›
```

#### ↳ Re: MF COBOL problem

- **From:** "rick smith" <ua-author-44949@usenetarchives.gap>
- **Date:** 1998-04-20T14:07:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com>`

```


Moshe Shulman wrote in message <6hfrj0$8.··.@dfw··m.com>...
› I am running a DOS program compiled under MicroFocus COBOL/2 Version
› 2.4.31 L2.3 revision 002. I have been trying to get it to run under
…[11 more quoted lines elided]…
› Empire State Supply

>From Microsoft C documentation:

"C Run-Time Error R6009

not enough space for environment

There was enough memory to load the program but not enough
memory to create the envp array.

One of the following may be a solution:

Increase the amount of memory available to the program.
Reduce the number and size of command-line arguments.
Reduce the environment size by removing unnecessary variables.

If your program uses the compact, large, or huge memory model,
this error may be avoided by using LINK's /CPARM:1 command-line
option. This option causes unused near heap space to be allocated
to the far heap."

Hope this helps.

Rick Smith
-----------------------------------------------------
```

##### ↳ ↳ Re: MF COBOL problem

- **From:** "stephen paul gennard" <ua-author-17075398@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4ceb4852-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cb4ceb4852-p7@usenetarchives.gap>`
- **References:** `<6hfrj0$86i@dfw-ixnews6.ix.netcom.com> <gap-cb4ceb4852-p7@usenetarchives.gap>`

```

Hi,

It sounds to me that you will need to give the 'C' RTS some extra memory
to work with via the COBPOOL environment var (which is documented).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
