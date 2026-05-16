[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Display upon

_8 messages · 5 participants · 2000-07 → 2000-08_

---

### Display upon

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3985F479.7E74FE4D@brazee.net>`

```
The history of the DISPLAY command makes it less useful than it might.  

What would be nice is if you could define a dozen different locations to
make displays.

DISPLAY UPON SYSOUX1, or DISPLAY UPON FILE.NAME or DISPLAY UPON
set-name.
```

#### ↳ Re: Display upon

- **From:** "Charles W. Cribbs II" <CHARLESCRIBBS@prodigy.net>
- **Date:** 2000-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m55kj$2veq$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<3985F479.7E74FE4D@brazee.net>`

```

so why can't you do that?? if you define it as a screen section you can
display a screen at a time with hundreds of pieces of information.

Howard Brazee <howard@brazee.net> wrote in message
news:3985F479.7E74FE4D@brazee.net...
> The history of the DISPLAY command makes it less useful than it might.
>
…[4 more quoted lines elided]…
> set-name.
```

##### ↳ ↳ Re: Display upon

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m56he$8bi$1@nntp9.atl.mindspring.net>`
- **References:** `<3985F479.7E74FE4D@brazee.net> <8m55kj$2veq$1@newssvr05-en0.news.prodigy.com>`

```
I believe that Howard uses a COBOL compiler without the EXTENSION of a
"screen section".  That is not a part of ANSI/ISO COBOL (but will be in the
next revision).

FYI,
  X/Open also defined a way to use ACCEPT/DISPLAY to get and set "environment
variables".  This is NOT a part of the draft Standard - but is a relatively
common extension today (especially in UNIX COBOLs).
```

###### ↳ ↳ ↳ Re: Display upon

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3986CE3E.297DF46B@brazee.net>`
- **References:** `<3985F479.7E74FE4D@brazee.net> <8m55kj$2veq$1@newssvr05-en0.news.prodigy.com> <8m56he$8bi$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> I believe that Howard uses a COBOL compiler without the EXTENSION of a
> "screen section".  That is not a part of ANSI/ISO COBOL (but will be in the
> next revision).

I use mainframes (currently IBM).  A co-worker mentioned how she had to
do a bit of debugging in the production environment.  She put in some
displays which puzzled some users who saw them mixed with some output. 
Admittedly it might be a good idea to have standards that ALL user
output be to standard output files and not displayed.

But even still, it might be nice for debugging purposes to have
different displays going to different locations.  We just have them
going to SYSOUX.

In the olden days, installations were adamant about DISPLAY UPON CONSOLE
causing pages of debugging data to go on the console typewriter.
```

###### ↳ ↳ ↳ Re: Display upon

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m6mm2$ij0$1@slb2.atl.mindspring.net>`
- **References:** `<3985F479.7E74FE4D@brazee.net> <8m55kj$2veq$1@newssvr05-en0.news.prodigy.com> <8m56he$8bi$1@nntp9.atl.mindspring.net> <3986CE3E.297DF46B@brazee.net>`

```
In all (current and past) IBM COBOL compilers, you may specify DIFFERENT
locations in the DISPLAY UPON statement.  These are "associated" with
external media.  You might also want to look at the OUTDD compiler option
(available since VS COBOL II).
```

#### ↳ Re: Display upon

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m6kqh$5pv$1@news.igs.net>`
- **References:** `<3985F479.7E74FE4D@brazee.net>`

```
Funnily enough, Howard, I am finding that I am going back to the
original usage of the DISPLAY.  As I GUI-ize, the console becomes redundant.
That allows me to use it exclusively for debug information, fatal errors,
etc., much like an operator's console.

Howard Brazee wrote in message <3985F479.7E74FE4D@brazee.net>...
>The history of the DISPLAY command makes it less useful than it might.
>
…[4 more quoted lines elided]…
>set-name.
```

##### ↳ ↳ Re: Display upon

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<COJh5.17993$RG6.1485775@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3985F479.7E74FE4D@brazee.net> <8m6kqh$5pv$1@news.igs.net>`

```
Interesting.  When COBOL was first designed, there were only output
printers, and console printers.  Only IBM used their card oriented line
printers and JCL so that some control could be exercised. RRand used a RR
15 cps typewriter, and we called it a console for use as an operators
console.  Any messages not directed to the operator had to appear on a High
Speed Printer listing OR the typewriter page was divided into vertical
sections where output in each section had designated use.

Warren Simmons
"donald tees" <donald@willmack.com> wrote in message
news:8m6kqh$5pv$1@news.igs.net...
> Funnily enough, Howard, I am finding that I am going back to the
> original usage of the DISPLAY.  As I GUI-ize, the console becomes
redundant.
> That allows me to use it exclusively for debug information, fatal errors,
> etc., much like an operator's console.
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Display upon

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DOJh5.17994$RG6.1486504@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3985F479.7E74FE4D@brazee.net> <8m6kqh$5pv$1@news.igs.net>`

```
Interesting.  When COBOL was first designed, there were only output
printers, and console printers.  Only IBM used their card oriented line
printers and JCL so that some control could be exercised. RRand used a RR
15 cps typewriter, and we called it a console for use as an operators
console.  Any messages not directed to the operator had to appear on a High
Speed Printer listing OR the typewriter page was divided into vertical
sections where output in each section had designated use.

Warren Simmons
"donald tees" <donald@willmack.com> wrote in message
news:8m6kqh$5pv$1@news.igs.net...
> Funnily enough, Howard, I am finding that I am going back to the
> original usage of the DISPLAY.  As I GUI-ize, the console becomes
redundant.
> That allows me to use it exclusively for debug information, fatal errors,
> etc., much like an operator's console.
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
