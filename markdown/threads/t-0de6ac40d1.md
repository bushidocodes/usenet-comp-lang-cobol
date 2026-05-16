[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What's wrong with this DISPLAY command ?

_6 messages · 3 participants · 2005-01_

---

### What's wrong with this DISPLAY command ?

- **From:** ngaro@msn.com
- **Date:** 2005-01-23T08:48:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com>`

```
My compiler won't compile this statement:
DISPLAY wortel(getal) WITH FOREGROUND-COLOR 4 NO ADVANCING
It tells me NO ADVANCING is incorrect, if i type it like this
DISPLAY wortel(getal) NO ADVANCING WITH FOREGROUND-COLOR 4
then it thinks WITH FOREGROUND-COLOR 1 is incorrect.

How should i type it ? (I want to display "wortel(getal)" in color 4
without going to the next rule)
```

#### ↳ Re: What's wrong with this DISPLAY command ?

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-01-23T17:27:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jn7v05glgg654rnlij9frfs865llc8t81@4ax.com>`
- **References:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com>`

```
On 23 Jan 2005 08:48:27 -0800, ngaro@msn.com wrote:

>My compiler won't compile this statement:
>DISPLAY wortel(getal) WITH FOREGROUND-COLOR 4 NO ADVANCING
…[5 more quoted lines elided]…
>without going to the next rule)

That is correct in only one particular compiler.

What compiler are you using? Vendor and version please.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: What's wrong with this DISPLAY command ?

- **From:** ngaro@msn.com
- **Date:** 2005-01-23T09:32:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106501540.512192.240430@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<9jn7v05glgg654rnlij9frfs865llc8t81@4ax.com>`
- **References:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com> <9jn7v05glgg654rnlij9frfs865llc8t81@4ax.com>`

```
CA-Realia II Workbench
```

#### ↳ Re: What's wrong with this DISPLAY command ?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-23T10:24:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106504656.480604.129690@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com>`
- **References:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com>`

```
> DISPLAY wortel(getal) WITH FOREGROUND-COLOR 4 NO ADVANCING

I would assume that 'FOREGROUND-COLOR' is usable when you are
DISPLAYing UPON CRT, or using SCREEN-SECTION, while 'NO ADVANCING' is
only available when DISPLAYing UPON CONSOLE.  Thus these two cannot be
in the same statement.

You either need to use CONSOLE and forget colours, or use CRT and do
DISPLY AT nnnn (or whatever positioning you compiler allows).
```

##### ↳ ↳ Re: What's wrong with this DISPLAY command ?

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-01-23T20:41:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fl28v0p2v9lee0tp0q56trgn6svs2b9vj9@4ax.com>`
- **References:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com> <1106504656.480604.129690@f14g2000cwb.googlegroups.com>`

```
On 23 Jan 2005 10:24:16 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> DISPLAY wortel(getal) WITH FOREGROUND-COLOR 4 NO ADVANCING
>
…[6 more quoted lines elided]…
>DISPLY AT nnnn (or whatever positioning you compiler allows).

The following
 DISPLAY "ABC" at 0110
 with foreground-color 4 no advancing.
or
 DISPLAY "ABC"  line 1 COLUMN 1
 with foreground-color 4 no advancing.

Are perfectly valid with Acucobol.

No screen section involved.


But it may not be valid on CA-Realia.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: What's wrong with this DISPLAY command ?

- **From:** ngaro@msn.com
- **Date:** 2005-01-24T02:31:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106562709.182337.5280@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com>`
- **References:** `<1106498907.151899.230060@z14g2000cwz.googlegroups.com>`

```
I found it, if you use FOREGROUND-COLOR in your DISPLAY statement it
automaticly doesn't advance, you don't have to type NO ADVANCING
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
