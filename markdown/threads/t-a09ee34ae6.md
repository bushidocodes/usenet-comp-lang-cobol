[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VisualAge COBOL Remote Development

_5 messages · 4 participants · 1999-08_

---

### VisualAge COBOL Remote Development

- **From:** "Bill Diamond" <wdiamond@teleport.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Lzw3.8224$FG4.380607@news1.teleport.com>`

```
Hi:

I'm wondering if anybody has developed/maintained COBOL/CICS
applications on a PC using VisualAge COBOL Enterprise ver. 2.2.  The
application would run in production on an IBM mainframe.

I've been doing this using CA-Realia products, but CA no longer
supports their OS/2 versions.

Thank You,
```

#### ↳ Re: VisualAge COBOL Remote Development

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c376fc.11711584@news1.ibm.net>`
- **References:** `<6Lzw3.8224$FG4.380607@news1.teleport.com>`

```
I'm interested in any responses you receive also. Particulary, can I
emulate CICS (without a mainframe) with IBM Visual Age COBOL - and
what version supports LE and the IP socket calls.


On Tue, 24 Aug 1999 09:30:51 -0700, "Bill Diamond"
<wdiamond@teleport.com> wrote:

>Hi:
>
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: VisualAge COBOL Remote Development

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c37cff.2836849@news2.ibm.net>`
- **References:** `<6Lzw3.8224$FG4.380607@news1.teleport.com> <37c376fc.11711584@news1.ibm.net>`

```
On Wed, 25 Aug 1999 04:54:39 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>I'm interested in any responses you receive also. Particulary, can I
>emulate CICS (without a mainframe) with IBM Visual Age COBOL - and
…[20 more quoted lines elided]…
>>

Well, I have VA COBOL 2.2 on my computer. it is a two platform product, containing CDROMs
for NT and OS/2.

It contains a super b compiler (more or less equivalent to the COBOL for OS/390 and VM),
CICS for NT resp CICS for OS/2.  THe LE callable services in total are not available, but
I seem to remember that some of the services, like bit manipulation, was available in 2.1,
and assume therefore that they are available in 2.2 as well


with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: VisualAge COBOL Remote Development

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c3853d.4945761@news2.ibm.net>`
- **References:** `<6Lzw3.8224$FG4.380607@news1.teleport.com> <37c376fc.11711584@news1.ibm.net>`

```
On Wed, 25 Aug 1999 04:54:39 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>I'm interested in any responses you receive also. Particulary, can I
>emulate CICS (without a mainframe) with IBM Visual Age COBOL - and
…[20 more quoted lines elided]…
>>
Well, I'm going to try again, my news program got the hiccups.....

I have VA COBOL 2.2 installed on my laptop running NT, and it works like a charm.  The
package contains versions for both NT and OS/2, but I haven't bothered to install the OS/2
version - OS/2 is going away on my computers.

The package contains

	a superb compiler, on the same level as COBOL for OS/390 and VM, 
	including OO extensions
	a (not so superb) Visual Builder
	a full implementation o fCICS for NT (and OS/2)
	SMARTData utilities to use MVS VSAM files

As a separately chargeable feature (about $500) you also get a report writer preprocessor

I have used this setup to write COBOL BATCH and COBOL CICS Programs.  Also, this COBOL and
CICS setup works perfectly well with DB/2 (if you have it installed on the PC as well, of
course)

All in all, I am mightily impressed......  The bad news is, the price tag is very
impressing as well



with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: VisualAge COBOL Remote Development

- **From:** "Denis" <grosnou@antispam.skynet.be>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7q027c$iff$1@hardcopy.ny.jpmorgan.com>`
- **References:** `<6Lzw3.8224$FG4.380607@news1.teleport.com> <37c376fc.11711584@news1.ibm.net> <37c3853d.4945761@news2.ibm.net>`

```
Seems nice but:

- You obviously edit on your PC but do you compile on the PC or on the MF?
- Do you need all the copybooks on your PC in order to compile you pgms on
the PC or does the compiler 'fetch' them at compile time from the MF? In
other word do you need to replicate all your sources files from the MF to
the PC in order to be able to compile on the PC?
- Can you test on your PC your CICS/DB2 pgms? In this case, same questions
as before, do you need to produces PC-type load modules for all the modules
that your CICS transactions will use on the PC or does VACOBOL
'fetch/translate...' the MF load modules from the MF?
- When you 'push' your modules to the MF do you need to recompile to produce
MF-type executables (Load modules, DB2/MVS packages...)?

Many thanx in advance your explanations.



>Well, I'm going to try again, my news program got the hiccups.....
>
>I have VA COBOL 2.2 installed on my laptop running NT, and it works like a
charm.  The
>package contains versions for both NT and OS/2, but I haven't bothered to
install the OS/2
>version - OS/2 is going away on my computers.
>
…[8 more quoted lines elided]…
>As a separately chargeable feature (about $500) you also get a report
writer preprocessor
>
>I have used this setup to write COBOL BATCH and COBOL CICS Programs.  Also,
this COBOL and
>CICS setup works perfectly well with DB/2 (if you have it installed on the
PC as well, of
>course)
>
>All in all, I am mightily impressed......  The bad news is, the price tag
is very
>impressing as well
>
…[5 more quoted lines elided]…
>(BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
