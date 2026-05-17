[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu -disappointing, RM-Cobol -primitive, anything else?

_7 messages · 6 participants · 1998-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "gerry walsh" <ua-author-571229@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34EF281B.CDE773DA@indigo.ie>`

```

I'm helping a friend who is learning cobol as part of an evening course.
I'm trying
to find a reasonable compiler & IDE for PC so that the friend can
concentrate
on learning cobol rather than watch me do battle with various software
packages.

The friend uses VAX cobol at college, and got RM-cobol as advised by the
college for
doing homework.

The RM-cobol devlopment environment is, er, primitive and the supplied
documentation
er, challenging. Ok for a programmer with a Unix background (like me)
but difficult
for someone relatively new to programming.

I've tried the Fujitsu Cobol85 but it has its own irritations (eg can't
compile if source
file is loaded in the editor or output msgs from last compilation
attempt still being
displayed) documentation is in pdf format, supplied reader s-l-o-w
[especially
backing up a page]) and more annoyingly does not seem to handle the
DISPLAY
clause correctly (ie uses COLUMN rather than POSITION and does not seem
to
accept DISPLAY ERASE). In fact, accessing the documentation is awkward
full stop.
Perhaps I shouldn't be so critical as it is free, but all the extra
bundled stuff (like
CGI & windowing support) is of little use to me.

The Accucobol demo expires after a short time so I don't really want the
hassle of
getting to grips with it and then tossing it out (apologies Acucobol).

I guess an IDE like Turbo C of the '80s is out of the question but I
would be
greatful of any pointers to a free (or cheap) compiler+IDE which really
supports
cobol 85. Or confirmation that no other candidates exist and that I
should make
the best of what I've already got... (sigh). I don't really want to
print out 1000's of
relatively empty pages of Fujitsu documentation...)

If ever a suitable package could be found, there is the possibility of
the
college in question making it the recommended package for students.

regards,
Gerry

and apologies for yet another "want PC compiler..." type posting.
```

#### ↳ Re: Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3cafbb06f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34EF281B.CDE773DA@indigo.ie>`
- **References:** `<34EF281B.CDE773DA@indigo.ie>`

```


Gerry Walsh wrote in message <34E··.@ind··o.ie>...
› I'm helping a friend who is learning cobol as part of an evening course.
› I'm trying
…[56 more quoted lines elided]…
› I think that the Micro Focus Personal COBOL might meet your needs.  It
isn't as "full-functioned" as the Workbench or NetExpress products - but
then it costs a LOT less too. By the way, the DISPLAY stuff that you are
talking about isn't part of Standard COBOL - so it does tend to vary from
vendor to vendor. However, Micro Focus does have support for an RM
"emulation" so it might well do for your friends excersies.
```

#### ↳ Re: Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "kk..." <ua-author-3129200@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3cafbb06f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34EF281B.CDE773DA@indigo.ie>`
- **References:** `<34EF281B.CDE773DA@indigo.ie>`

```

On Sat, 21 Feb 1998 19:16:44 +0000, Gerry Walsh
wrote:

› If ever a suitable package could be found, there is the possibility of
› the
…[6 more quoted lines elided]…
› 
Gee, I'm glad I've always worked mainframes! There's enough
environmental quirks from shop to shop on mainframes but at least I
don't have to worry about which Cobol I'm using and it's limitations.
Maybe learning on a S/3 with punch cards wasn't that bad many years
back?

Sorry,
Kevin
```

#### ↳ Re: Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "jerry peacock" <ua-author-36061@usenetarchives.gap>
- **Date:** 1998-02-21T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3cafbb06f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34EF281B.CDE773DA@indigo.ie>`
- **References:** `<34EF281B.CDE773DA@indigo.ie>`

```


Get the book: "From Micro to Mainframe" (Grauer & Villar), Prentice Hall
Press,
ISBN 0-13-310764-7 ($67.00). It comes with the CA-REALIA compiler which
produces stand-alone executables and supports the following dialects of
COBOL

REALIA4 Default
REALIA4-74 With ANSI-74 features
VS2 IBM VS COBOL II, release 3
SAA IBM System App Architecture,
OSVS IBM VS COBOL for OS/VS Release 2.4
ANS IBM full ANS, based on ANSI X3.23-1968
ANSI85 ANSI COBOL Standard X3.23-1985
ANSI74 ANSI COBOL x3.23-1974

and maybe some others.

I think the compiler is crippled to permit programs of 500 lines or less,
but
permits subprograms. The package contains a debugger, editor, linker,
and indexed file utilities (copy, reorg, etc.)
```

##### ↳ ↳ Re: Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-02-21T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3cafbb06f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3cafbb06f-p4@usenetarchives.gap>`
- **References:** `<34EF281B.CDE773DA@indigo.ie> <gap-d3cafbb06f-p4@usenetarchives.gap>`

```

Jerry Peacock wrote:
› 
› Get the book: "From Micro to Mainframe" (Grauer & Villar), Prentice Hall
…[19 more quoted lines elided]…
› and indexed file utilities (copy, reorg, etc.)

Back in 1992, you could order this book direct from Prentice-Hall by
calling 1-800-223-1360 before 4:30 PM Eastern Time (USA). But my notes
show a different ISBN, so maybe they've finally upgraded the book. I
don't know if the phone number is still good. I'll have to give it a
try.

In 1992 the compiler, debugger, and examples came on a 5-1/4 inch
floppy. There was definitely no linker (I used MS-Link from QuickBasic
4.5) and no editor that I remember.

The compiler is limited to 500 lines of code, excluding comments. Files
were limited to 64K bytes or less, unless you used the DOS CALLS to
access files. There was a pretty good library of DOS calls, but they
were only documented in the Realia 4.2 full compiler. If you could get
that documentation every one I tried would work with the educational
version of the compiler. I wrote a DOS "touch" utility and a directory
lister for practice.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

###### ↳ ↳ ↳ Re: Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-02-21T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3cafbb06f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3cafbb06f-p5@usenetarchives.gap>`
- **References:** `<34EF281B.CDE773DA@indigo.ie> <gap-d3cafbb06f-p4@usenetarchives.gap> <gap-d3cafbb06f-p5@usenetarchives.gap>`

```

Arnold Trembley wrote:
› 
› Jerry Peacock wrote:
…[20 more quoted lines elided]…
› 4.5) and no editor that I remember.

I forgot to mention that even though the compiler was limited to short
programs, it was pretty easy to get around that problem by using
subprogram calls. I wonder if the newest version is compatible with
Win95? I would expect it to support text mode processing only.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

###### ↳ ↳ ↳ Re: Fujitsu -disappointing, RM-Cobol -primitive, anything else?

- **From:** "gypsy" <ua-author-45425@usenetarchives.gap>
- **Date:** 1998-02-22T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3cafbb06f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3cafbb06f-p5@usenetarchives.gap>`
- **References:** `<34EF281B.CDE773DA@indigo.ie> <gap-d3cafbb06f-p4@usenetarchives.gap> <gap-d3cafbb06f-p5@usenetarchives.gap>`

```



Arnold Trembley wrote in article
<6cr2ah$s.··.@bgt··t.net>...
› Jerry Peacock wrote:
›› 
…[5 more quoted lines elided]…
›› <
 
 
›› I think the compiler is crippled to permit programs of 500 lines or
›› less,
…[26 more quoted lines elided]…
› 

As I posted recently about this particular book...Was in touch with
Prentice Hall about 3 weeks ago trying to get a copy for a friend--the 2nd
Edition is currently out of print and PH hasn't any more copies (nor do any
major booksellers--Although Barnes & Noble claimed to have a copy in the
warehouse and then *whoops* didn't).

According to the rep @ PH, the 3rd edition is due out sometime in
March--but as he said late March, I'm thinking it's more like April (given
past experience). Who knows how much it will cost, but it should come
along with about the same equipage as the 2d edition...

Which essentially consists of the Scaled down Realia compiler (yep...you
got it 500 line max!) but does have a linker and a debugger that come on
one 3.5 floppy...although maybe they'll splurge and put it on CD ROM in the
new version...just to annoy me.

Still...great book, easy to follow and to the point.
Lucretia M. Pruitt
gy··.@nos··l.com
Remove the NOSPAM to reply :)

********************************************
"I was talking to myself about a piece of
code the other day...and we were wondering
if we should get a third opinion on it..."
LMP
********************************************
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
