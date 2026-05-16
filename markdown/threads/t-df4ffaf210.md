[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Vs: First cobol-program

_4 messages · 3 participants · 2001-04_

---

### Re: Vs: First cobol-program

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-04-05T07:28:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ACC730C.15742143@brazee.net>`
- **References:** `<0Yyy6.15$AX2.990@read2.inet.fi> <3acb0f45_1@my.newsfeeds.com> <2D713F5028C5113F.C640D91E22085D00.E58BDCCEB6256DD0@lp.airnews.net> <SyWy6.75$Td4.3755@read2.inet.fi>`

```
Did this compile cleanly?   I haven't used many PC compilers but it seemed odd
to see Working-storage before I-O.

I'm also confused by your perform statement.  It appears that you have a
combination of performing a paragraph (oops I mean section) and an in-line
perform.  Use one or the other.

Some compilers give an error if they find a section without a paragraph name.
I myself prefer to not use sections in the procedure division, but other fine
programmers haven't been converted to my enlightened view. 8^)

"Jarkko Kï¿½hkï¿½nen" wrote:

> Thanks to everybody for help! I corrected my mistakes. Here is new version.
> (CUSTOMER-FILE was typo (what?!=)).
…[70 more quoted lines elided]…
>               Encoding: x-uuencode
```

#### ↳ Re: Vs: First cobol-program

- **From:** "Erlend Moen" <erlend.moen@disys.no>
- **Date:** 2001-04-05T16:14:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ahul0$oq4$1@oslo-nntp.eunet.no>`
- **References:** `<0Yyy6.15$AX2.990@read2.inet.fi> <3acb0f45_1@my.newsfeeds.com> <2D713F5028C5113F.C640D91E22085D00.E58BDCCEB6256DD0@lp.airnews.net> <SyWy6.75$Td4.3755@read2.inet.fi> <3ACC730C.15742143@brazee.net>`

```
Howard Brazee <howard@brazee.net> skrev i news:3ACC730C.15742143@brazee.net
> Did this compile cleanly?   I haven't used many PC compilers but it seemed
odd
> to see Working-storage before I-O.

I agree to that...

> I'm also confused by your perform statement.  It appears that you have a
> combination of performing a paragraph (oops I mean section) and an in-line
> perform.  Use one or the other.

...but not to this!

The best reason I have to use sections instead of top-down paragraphs is
just this that I can program "functions" in this way and performing these
just with a simple statement (i.e. PERFORM CONVERT_DATE). I adopted this
from my experience with programming in TurboPascal in early 80's. Since '88
I've used sections in CObOL all the time. In *my* opinion the code is much
cleaner, but it demands that you use obvious section-names and not to
mention variable-names. Another benefit is that it's easy to make "complex"
copy-files and integrate these very easy in many programs.

I know this has been debated over and over here, but I couldn't resist...
:-)

Regards,
Erlend Moen
```

##### ↳ ↳ Re: Vs: First cobol-program

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-04-05T14:49:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kC%y6.4407$Kr1.433547@newsread1.prod.itd.earthlink.net>`
- **References:** `<0Yyy6.15$AX2.990@read2.inet.fi> <3acb0f45_1@my.newsfeeds.com> <2D713F5028C5113F.C640D91E22085D00.E58BDCCEB6256DD0@lp.airnews.net> <SyWy6.75$Td4.3755@read2.inet.fi> <3ACC730C.15742143@brazee.net> <9ahul0$oq4$1@oslo-nntp.eunet.no>`

```

"Erlend Moen" <erlend.moen@disys.no>
>
> > I'm also confused by your perform statement.  It appears that you
have a
> > combination of performing a paragraph (oops I mean section) and an
in-line
> > perform.  Use one or the other.
>
> ...but not to this!
>
> The best reason I have to use sections instead of top-down
paragraphs is
> just this that I can program "functions" in this way and performing
these
> just with a simple statement (i.e. PERFORM CONVERT_DATE). I adopted
this
> from my experience with programming in TurboPascal in early 80's.
Since '88
> I've used sections in CObOL all the time. In *my* opinion the code
is much
> cleaner, but it demands that you use obvious section-names and not
to
> mention variable-names. Another benefit is that it's easy to make
"complex"
> copy-files and integrate these very easy in many programs.
>
> I know this has been debated over and over here, but I couldn't
resist...
> :-)

You don't have to PERFORM CONVERT-DATE, you can CALL 'CONVERT-DATE'
and get the target code completely out of the program, but that's
another story.

In this case, we have a homework assignment, not a stock-ticker
quotation system.

Lose the SECTION(s).

In this context, SECTIONS are superfluous, confusing, and a source of
error. In the unlikely event SECTIONs are ever encountered in the
wild, one can take steps at that time.
```

##### ↳ ↳ Re: Vs: First cobol-program

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-04-05T09:15:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ACC8C21.2355839B@brazee.net>`
- **References:** `<0Yyy6.15$AX2.990@read2.inet.fi> <3acb0f45_1@my.newsfeeds.com> <2D713F5028C5113F.C640D91E22085D00.E58BDCCEB6256DD0@lp.airnews.net> <SyWy6.75$Td4.3755@read2.inet.fi> <3ACC730C.15742143@brazee.net> <9ahul0$oq4$1@oslo-nntp.eunet.no>`

```


Erlend Moen wrote:

> Howard Brazee <howard@brazee.net> skrev i news:3ACC730C.15742143@brazee.net
> > Did this compile cleanly?   I haven't used many PC compilers but it seemed
…[20 more quoted lines elided]…
> I know this has been debated over and over here, but I couldn't resist...

I don't think I was clear.  While I would love to see procedure division
sections go away along with GO TO exit statements, I was referring to the
following code:

   PERFORM READ-MY-DATA-FILE UNTIL END-OF-FRIENDS-FILE = 1
     DISPLAY OWNSTRING
   END-PERFORM

He should either have it an in-line perform or an external perform, not both.


BTW:
When EXIT-PARAGRAPH is available, I suspect you won't mind working in a shop
which uses these instead of sections.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
