[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CHAIN Command?

_4 messages · 4 participants · 1995-09_

---

### CHAIN Command?

- **From:** "charles j. statton" <ua-author-17088169@usenetarchives.gap>
- **Date:** 1995-09-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4399r0$p0m@txirvuhw302.gtetel.com>`

```
I apologize if this is covered in a FAQ, however I would like to know if there is a
command like CHAIN (RPG) available is some form in Cobol.

Also, could someone recommend a Cobol Compiler? The majority would be coded on a PC
but we would like portability to HP and Data General Unix boxes. Thanks for any
information you can provide me.
*===============================*====================================*
|   Chuck Statton               | GTE Telephone Operations           |
|   Asst - Information Security | Fort Wayne, IN                     |
|===============================*====================================|
|   Cha··.@GTE··t.com / Comments are mine not GTE's   |
*====================================================================*
```

#### ↳ Re: CHAIN Command?

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-09-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-83dd623bfc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4399r0$p0m@txirvuhw302.gtetel.com>`
- **References:** `<4399r0$p0m@txirvuhw302.gtetel.com>`

```
Charles J. Statton (Cha··.@gte··t.com) wrote:
: I apologize if this is covered in a FAQ, however I would like to know if there is a
: command like CHAIN (RPG) available is some form in Cobol.

: Also, could someone recommend a Cobol Compiler? The majority would be coded on a PC
: but we would like portability to HP and Data General Unix boxes. Thanks for any
: information you can provide me.
: --
: *===============================*====================================*
: | Chuck Statton | GTE Telephone Operations |
: | Asst - Information Security | Fort Wayne, IN |
: |===============================*====================================|
: | Cha··.@GTE··t.com / Comments are mine not GTE's |
: *====================================================================*

There is a CHAIN command in some COBOLs. Format is similar to that of CALL:

CHAIN program-name USING data-set.

Basically the first program terminates, the one CHAINed to takes over.
I have found no use for this command.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

#### ↳ Re: CHAIN Command?

- **From:** "bob wolfe" <ua-author-5416381@usenetarchives.gap>
- **Date:** 1995-09-14T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-83dd623bfc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4399r0$p0m@txirvuhw302.gtetel.com>`
- **References:** `<4399r0$p0m@txirvuhw302.gtetel.com>`

```
"Charles J. Statton" wrote:

[snip]
› Also, could someone recommend a Cobol Compiler? The majority would be coded on a PC
› but we would like portability to HP and Data General Unix boxes. Thanks for any
› information you can provide me.

Please take a look at:

http://www.cis.ohio-state.edu/hypertext/faq/usenet/cobol-faq/faq.html

This is the COBOL FAQ. It lists the various COBOL compiler companies and
includes telephone numbers so that you may contact each one.

By the way, if you are migrating an application, we have user
interface migration tool to help you move the program more easily.
Please feel free to send e-mail to me at if you have
additional questions.
Bob Wolfe, Flexus - COBOL spII-The only *truly* COBOL-Oriented GUI Tool
Phone:610-588-9400 - Fax:610-588-9475 - E-Mail: 
Warning!  This is a shameless, yet subtle product promo!  Reader Beware!
```

#### ↳ Re: CHAIN Command?

- **From:** "7330..." <ua-author-17087665@usenetarchives.gap>
- **Date:** 1995-09-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-83dd623bfc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4399r0$p0m@txirvuhw302.gtetel.com>`
- **References:** `<4399r0$p0m@txirvuhw302.gtetel.com>`

```
Charls,
Micro Focus COBOL supports CHAIN command (a form of a call) with
no expectation of return, in CICS (XCTL). Micro Focus COBOL
runs on PC, HP and many other UNIX platforms. Call
1-800-MF-COBOL for more info or send e-mail to lit··.@mfl··o.uk


Regards

IGGY
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
