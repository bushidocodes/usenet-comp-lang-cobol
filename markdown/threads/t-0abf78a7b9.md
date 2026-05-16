[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with Fujitsu Cobol 4.0

_10 messages · 6 participants · 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help with Fujitsu Cobol 4.0

- **From:** f.regnier@worldonline.fr (Frédéric REGNIER)
- **Date:** 2001-01-04T17:32:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr>`

```
I try to learn Cobol with student package Fujitsu Cobol 4.0 but i can
compile new project.
Somebody, could send me a functionnal (win95) version?
With advance, great thanks.

f.regnier@worldonline.fr
```

#### ↳ Re: Help with Fujitsu Cobol 4.0

- **From:** "Brad Prothero" <brad.prothero@clarica.com>
- **Date:** 2001-01-04T10:50:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yS156.81$t6.7714@news.corpcomm.net>`
- **References:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr>`

```
What is the error that you are getting? Maybe we can help you get your copy
to work.
```

##### ↳ ↳ Re: Help with Fujitsu Cobol 4.0

- **From:** f.regnier@worldonline.fr (Frédéric REGNIER)
- **Date:** 2001-01-05T12:03:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1emrfmu.1s2841k1s3eimsN%f.regnier@worldonline.fr>`
- **References:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr> <yS156.81$t6.7714@news.corpcomm.net>`

```
Brad Prothero <brad.prothero@clarica.com> wrote:

> What is the error that you are getting? Maybe we can help you get your copy
> to work.

Thanks for your help.
I made a mistake, in fact i can't compile executable apps.
I can compile .cbl with cobol editor but when i try to compile project
with project manager i've this alert 
"Build Start
C:\FSC \COBOL97 \LINK.EXE /OUT:ESSAI.EXE
Microsoft (R) 32-Bit incremental Linker Version 5.0.2.7132
Copyright (C) Microsoft Corp 1992-1997. All rigths reserved.
Link fatal error LNK1181: cannot open input file
"DOCUMENTS\EXEMPLESLIVRES\ESSAI\FILE.001"
Build has been stopped.
Build Interrupted."

f.regnier@worldonline.fr
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-05T12:41:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a55c0a7.83351926@news1.attglobal.net>`
- **References:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr> <yS156.81$t6.7714@news.corpcomm.net> <1emrfmu.1s2841k1s3eimsN%f.regnier@worldonline.fr>`

```
It looks like your program is probably in the "My Documents" folder.
Early versions of Fujitsu COBOL had trouble with directory names that
had embedded spaces.  Create a new folder without spaces in the name
and move your source code there, then try compiling.



On Fri, 5 Jan 2001 12:03:52 +0100, f.regnier@worldonline.fr
(=?ISO-8859-1?Q?Fr=E9d=E9ric_REGNIER?=) wrote:

>Brad Prothero <brad.prothero@clarica.com> wrote:
>
…[16 more quoted lines elided]…
>f.regnier@worldonline.fr  

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

_(reply depth: 4)_

- **From:** f.regnier@worldonline.fr (Frédéric REGNIER)
- **Date:** 2001-01-05T17:19:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1emrtsn.y3cqwt1aiuyqaN%f.regnier@worldonline.fr>`
- **References:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr> <yS156.81$t6.7714@news.corpcomm.net> <1emrfmu.1s2841k1s3eimsN%f.regnier@worldonline.fr> <3a55c0a7.83351926@news1.attglobal.net>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote:

> It looks like your program is probably in the "My Documents" folder.
> Early versions of Fujitsu COBOL had trouble with directory names that
> had embedded spaces.  Create a new folder without spaces in the name
> and move your source code there, then try compiling.

You solve my problem! Great thanks. 
I made a new folder without space and i can compile apps.
A new question about the project manager, in file menu there is no
option to create new project? 

f.regnier@worldonline.fr
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

_(reply depth: 5)_

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-01-05T17:28:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<611c5tcnn7smcgmk0d71hh4qd6r6dq8fal@4ax.com>`
- **References:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr> <yS156.81$t6.7714@news.corpcomm.net> <1emrfmu.1s2841k1s3eimsN%f.regnier@worldonline.fr> <3a55c0a7.83351926@news1.attglobal.net> <1emrtsn.y3cqwt1aiuyqaN%f.regnier@worldonline.fr>`

```
On Fri, 5 Jan 2001 17:19:52 +0100, f.regnier@worldonline.fr (Frï¿½dï¿½ric
REGNIER) wrote:
....
>A new question about the project manager, in file menu there is no
>option to create new project? 
Just do a open project and put the name of the new project you
require.
It will create it.

FF
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-01-05T19:15:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010105141513.25954.00000004@nso-fm.aol.com>`
- **References:** `<1emrtsn.y3cqwt1aiuyqaN%f.regnier@worldonline.fr>`

```
In article <1emrtsn.y3cqwt1aiuyqaN%f.regnier@worldonline.fr>,
f.regnier@worldonline.fr (=?ISO-8859-1?Q?Fr=E9d=E9ric_REGNIER?=) writes:

>A new question about the project manager, in file menu there is no
>option to create new project? 
>

When you type in a name that does not exist, it should prompt you 
regarding creation of a new project.  Basically a confirmation that 
you intend on opening a new project.
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-01-05T20:32:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010105153205.17535.00000014@nso-fy.aol.com>`
- **References:** `<1emrtsn.y3cqwt1aiuyqaN%f.regnier@worldonline.fr>`

```
In article <1emrtsn.y3cqwt1aiuyqaN%f.regnier@worldonline.fr>,
f.regnier@worldonline.fr (=?ISO-8859-1?Q?Fr=E9d=E9ric_REGNIER?=) writes:

>A new question about the project manager, in file menu there is no
>option to create new project? 
>

When you type in a name that does not exist, it should prompt you 
regarding creation of a new project.  Basically a confirmation that 
you intend on opening a new project.
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

- **From:** f.regnier@worldonline.fr (Frédéric REGNIER)
- **Date:** 2001-01-05T15:46:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1emrhna.1a7qs41fgu83gN%f.regnier@worldonline.fr>`
- **References:** `<1empzr9.64vfgj1l4g7jqN%f.regnier@worldonline.fr> <yS156.81$t6.7714@news.corpcomm.net> <1emrfmu.1s2841k1s3eimsN%f.regnier@worldonline.fr>`

```
Frï¿½dï¿½ric REGNIER <f.regnier@worldonline.fr> wrote:

I've also an error
"Build Start.
Build : Error : " The 'C:\Mes' Target is a recursive reference. Check th
description of the makefile.
Build has been stopped.
Build Interrupted."

f.regnier@worldonline.fr
```

###### ↳ ↳ ↳ Re: Help with Fujitsu Cobol 4.0

_(reply depth: 4)_

- **From:** deek40@aol.com (Deek40)
- **Date:** 2001-01-08T18:34:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010108133430.24015.00000310@ng-fa1.aol.com>`
- **References:** `<1emrhna.1a7qs41fgu83gN%f.regnier@worldonline.fr>`

```
I am new to COBOL so this answer is probably wrong:), but give it a shot. 
Possibly an error in your code   look at you FD's.

Hopefully someone else will help ya too;)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
