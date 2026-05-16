[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ISPF Edit/View HILITE to HTML macros

_4 messages · 2 participants · 2007-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Web, XML, modern integration`](../topics.md#web)

---

### ISPF Edit/View HILITE to HTML macros

- **From:** prino <prino@bigfoot.com>
- **Date:** 2007-09-21T04:23:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190373798.830469.69440@g4g2000hsf.googlegroups.com>`

```
Hi all,

I've written a set of REXX edit macros/execs that might be useful for
documentation/presentation purposes. They basically parse the member
(assembler, COBOL, PL/I, REXX, assembler, JCL and, very limited,
output of SuperC) being viewed/edited and turn it into a format that
is for all intents and purposes the same as when the member is looked
at in ISPF's Edit or View using HI RESET + HI PAREN - there are a few
small differences,
mainly because I (hopefully) correctly parsing JCL in-stream data, no-
operand assembler opcodes/directives and removed the SuperC bug where
the last two columns are displayed in green. :)

The set of (currently) nine macros consists of:

EHIASM - convert assembler to Edit HILITE'd HTML
EHICOBOL - convert COBOL to Edit HILITE'd HTML
EHIHELP - general help 'screen'
EHIJCL - convert JCL to Edit HILITE'd HTML
EHINONE - convert any text to Edit HTML (no HILITE)
EHIPLI - convert PL/I to Edit HILITE'd HTML
EHIREXX - convert REXX to Edit HILITE'd HTML
EHISUPC - convert SuperC to Edit HILITE'd HTML (as yet limited to what
I required...)
EHISUPP - general support (generate the actual HTML)

BTW, besides working as edit macro under ISPF (and as TSO command) on
z/OS, they also work on Regina.

EHISUPP contains Javascript code to faithfully emulate an 80-character
wide ISPF VIEW screen with (obviously non-working) action bars,
horizontal and vertical scrollbars (the horizontal one updates the
column numbers) and non-left/right scrolling '... *** Top/Bottom of
Data ***...' lines. At my request (I actually paid for it for the
code!), the developer of this code, Derek Pattenson <http://
www.smallofficesolutions.co.uk/>, released it under GPL V3, which may
imply that if you use this fancy output (_it is also possible to
select plain HTML_) that your code will also be released under GPL
V3... (Only a "problem" if you put it on a _publicly_ accessible
website)

NB, the fancy output works OK in W3C standards based Firefox, but in
IE(6) it's slower than a snail on a very large dose of valium... (The
reason is that it uses 'white-space:pre' CSS rather than <pre>...</
pre> HTML tags)

As for the generating speed? EHIASM parses 'SYS1.MACLIB(CBDZPARS)' in
about 17 seconds and converting the parsed data into fancy HTML takes
another 15. A PL/I program of almost 11,000 lines takes around the
same total time. (Both on z/OS 1.7)

If you're interested in getting copies of the code (I think at almost
7,500 lines it's a bit to big post here) drop me a line, do not use
the bigfoot adress, but _ONLY_ use
x2c(88899389A3857C97998995964B9585A3) (EBCDIC), put '[HILITE]'
somewhere in the subject AND DO NOT SEND EMAIL IN HTML FORMAT!
Indicate if you want the code as eight zipped text files or as a PDS
in zipped XMIT format and make sure that any return message with
'[HILITE]' in the subject isn't stopped (or worse, returned to me) by
any spam filters.

I consider the code to be of RC-1 quality, but I would appreciate any
bug reports.

Finally, the code is released under GPL V3, I plan to put it on
Sourceforge in the near(ish) future, but if you find any problems with
it before then, please drop me a line!

Robert
```

#### ↳ Re: ISPF Edit/View HILITE to HTML macros

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T09:25:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190391917.258885.195760@57g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<1190373798.830469.69440@g4g2000hsf.googlegroups.com>`
- **References:** `<1190373798.830469.69440@g4g2000hsf.googlegroups.com>`

```
On 21 Sep, 12:23, prino <pr...@bigfoot.com> wrote:
> Hi all,
>
…[68 more quoted lines elided]…
> x2c(88899389A3857C97998995964B9585A3)

You might wish to contact the people who run the CBT Tape List as they
run the biggest repository of freely available code related to IBM
mainframes. Their web site is www.cbttape.org.
```

##### ↳ ↳ Re: ISPF Edit/View HILITE to HTML macros

- **From:** prino <prino@bigfoot.com>
- **Date:** 2007-09-21T15:46:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190414773.594660.79890@o80g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1190391917.258885.195760@57g2000hsv.googlegroups.com>`
- **References:** `<1190373798.830469.69440@g4g2000hsf.googlegroups.com> <1190391917.258885.195760@57g2000hsv.googlegroups.com>`

```
On Sep 21, 4:25 pm, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> On 21 Sep, 12:23, prino <pr...@bigfoot.com> wrote:

<snip announcement>

> You might wish to contact the people who run the CBT Tape List as they
> run the biggest repository of freely available code related to IBM
> mainframes. Their web site iswww.cbttape.org.

Have already done so, will go there next week. ;)

Robert
```

###### ↳ ↳ ↳ Re: ISPF Edit/View HILITE to HTML macros

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T19:03:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190426629.442627.87360@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<1190414773.594660.79890@o80g2000hse.googlegroups.com>`
- **References:** `<1190373798.830469.69440@g4g2000hsf.googlegroups.com> <1190391917.258885.195760@57g2000hsv.googlegroups.com> <1190414773.594660.79890@o80g2000hse.googlegroups.com>`

```
On 21 Sep, 23:46, prino <pr...@bigfoot.com> wrote:
> On Sep 21, 4:25 pm, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>
…[10 more quoted lines elided]…
> Robert

Whew! Now I've done my good-boy-scout-deed for the day. I can go to
sleep with a warm fuzzy feeling inside. Seriously - I'm glad that you
have contacted them.    :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
