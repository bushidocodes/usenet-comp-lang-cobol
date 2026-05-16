[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do GO TO in ANSI85 COBOL

_2 messages · 2 participants · 1994-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Help requests and how-to`](../topics.md#help)

---

### Re: How to do GO TO in ANSI85 COBOL

- **From:** vadik@cs.umd.edu (Vadim Maslov)
- **Date:** 1994-12-08T19:03:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c86ro$1do@elan.cs.umd.edu>`
- **References:** `<3b882g$9qk@ixnews1.ix.netcom.com> <3bvgcs$8ud@gnat.cs.nyu.edu> <3c0nh6$5fn@elan.cs.umd.edu> <D0ICvG.L1x@belgium.eu.net>`

```
In article <D0ICvG.L1x@belgium.eu.net>,
Pieter Hintjens <pahint@eunet.be> wrote:
>Vadim Maslov (vadik@cs.umd.edu) wrote:
>: Not using GOTOs is the same kind of extremism as drinking decaffeinated
…[10 more quoted lines elided]…
>clients will one day forgive me. :-(

I understand your sarcasm. As you may have guessed, the word
'disaster' here is an element of style and it was not supposed to
mean a disaster in a common sense of a word. I know that it's
possible to introduce a sufficient number of guard variables and
leave happily thereafter. Even more, as far as I remember, there
is a theorem that states that any non-structured code can be converted
to structured code without GOTOs, however it may involve code
duplication.

I was speaking more about convinience and about twisting one's
hands to write a particular analyzer or any other program.


Summary: there are several disciplines of writing code.
The discipline "don't use GOTOs at any price" is more or less
senseless to me, since price may be too high.
What's more important, structured control flow is only
a part of a general programming style that contributes
to the program correcteness. I would even say, it's not
the most important part.


Vadim Maslov
```

#### ↳ Re: How to do GO TO in ANSI85 COBOL

- **From:** Jeff Gentile <Jeff.Gentile@DaytonOH.NCR.COM>
- **Date:** 1994-12-09T20:02:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0K7nv.70M@ncrcae.ColumbiaSC.NCR.COM>`
- **References:** `<3c86ro$1do@elan.cs.umd.edu>`

```
>==========Vadim Maslov, 12/8/94==========
>

(Stuff deleted to save bandwidth.  See comment below.)

>
>Summary: there are several disciplines of writing code.
…[9 more quoted lines elided]…
>

My first COBOL teacher from my college days, had a suggestion which
I took to heart regarding GO TOs.  It was basically that, if your GO TO 
procedure name isn't one page up or down on your printout, you might
want to rethink your code.  Of course, now days it might be one screen
display up or down.  Like most things in life, the good/badness of GO 
TOs are in shades of gray.

For most PERFORM and GO TO bigots,  it is a mute issue in ANSI 
COBOL 85 because of nested programs.  The implementations I've seen
of this feature, make is a structured programers dream.  Nested programs
end up being equated to modules that some of us are familiar with in 
other languages.

Jeff Gentile
AT&T GIS Service Technology
jeff.gentile@daytonoh.ncr.com
513 445-5283
"Never trust a distorted mirror"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
