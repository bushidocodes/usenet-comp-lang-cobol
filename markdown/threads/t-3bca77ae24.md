[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to create portable print files from MicroFocus NetExpress?

_5 messages · 5 participants · 2002-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### How to create portable print files from MicroFocus NetExpress?

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-06-21T08:02:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0206210702.190c150d@posting.google.com>`

```
Any ideas please on how to produce print files that are both printable
and viewable on the screen, from a MicroFocus NetExpress application? 
I want to be able to include different fonts, underlining, bold, page
throws, etc., and possibly pictures.  I need to be able to print the
files myself, and email them to clients for them to view or print as
they choose, using standard tools they would already have.  Some ideas
include:
1)  Create plain asci text file, including printer control characters.
2)  Create a Word document by calling MS Word using OLE Automation.
3)  Create an html file, using html codes to change font etc.
4)  Use a Report Writer such as Crystal Reports.
5)  Create a .pdf file.

Any other ideas?  What would be best?  What do other COBOL users use?

But each of these methods have problems, at least for me!:
1)  Include printer control characters:  produces good prints, but is
not viewable on the screen, without extra software packages (such as
Visual PCL/2 from www.visual.co.uk).  (It is probably possible to
write a viewer using COBOL, but I am not sure how?)
2)  Calling Word:  very laborious, every action such as changing fonts
takes several commands.
3)  html:  I have experimented, and it has potential, but also seems
laborious.
4)  Report Writer:  I have no knowledge of them.
5)  .pdf:  again have no knowledge of how to do this.

Many thanks in advance.
Phil Hickling.
```

#### ↳ Re: How to create portable print files from MicroFocus NetExpress?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-06-21T16:42:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DHIQ8.452$cE5.29@nwrddc02.gnilink.net>`
- **References:** `<6a371be2.0206210702.190c150d@posting.google.com>`

```

You could create 'standard' rich text files. On screen, display in a
richedit control and the formatting is automatic . To print, send to MS word
*or any other software* which handles 'standard' rich text - and the
formatting is automatic.

MS-word format is a lot like rich text, but does have some differences, so
why not go with the more 'universal' Rich Text?
```

#### ↳ Re: How to create portable print files from MicroFocus NetExpress?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-21T17:14:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D135F8D.97525C3@shaw.ca>`
- **References:** `<6a371be2.0206210702.190c150d@posting.google.com>`

```


Phil Hickling wrote:

> Any ideas please on how to produce print files that are both printable
> and viewable on the screen, from a MicroFocus NetExpress application?
…[26 more quoted lines elided]…
> Phil Hickling.

Taking your options :-

1) I don't really think you want to start writing a 'viewer' do you <G>

2) Calling Word very laborious - but not anymore laborious than using
PC_PRINT to do the same thing. Now here's the trick - all the *resuable*
stuff that you want to keep invoking for different reports -  put it into
"Print Classes" where you can send invokes from your calling program with
a set of parameters - now if you aren't comfortable with OO this is
*definitely* a non-starter but it would be the way to do it.

3) HTML - can't help - but again to get over the "laborious" put
repetitive stuff into
"Print Classes"

4) Don't know the product, but Crystal Report seems like a good option.

5) PDF - no knowledge.

Option (2) above, Word as an OLE,  is the route I intend to go, but
haven't even started yet. To give you an idea what you can do, I have
turned the PC_PRINT routines into an invokeable class. If interested in
taking a look to see how you could use a similar concept invoking Word
from COBOL (tied in with that example from Wayne Rippin), let me know and
I'll send you a copy.

Jimmy, Calgary AB
```

#### ↳ Re: How to create portable print files from MicroFocus NetExpress?

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2002-06-22T05:35:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H0UQ8.33730$EP.2666@sccrnsc03>`
- **References:** `<6a371be2.0206210702.190c150d@posting.google.com>`

```
The website you mention has another product which will convert your (since
you say you get good prints I assume you might be using it) PCL into
PDF.....(i use it and love it and i don't work for them)   then you just
spawn that converted file off into Acrobat Reader using a Windows API like
ShellExecute.

Good Luck,
Mike Kinasz


"Phil Hickling" <philhickling@compuserve.com> wrote in message
news:6a371be2.0206210702.190c150d@posting.google.com...
> Any ideas please on how to produce print files that are both printable
> and viewable on the screen, from a MicroFocus NetExpress application?
…[26 more quoted lines elided]…
> Phil Hickling.
```

#### ↳ Re: How to create portable print files from MicroFocus NetExpress?

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2002-06-22T14:34:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20285920550e811bb2993e3186c260e0.40368@mygate.mailgate.org>`
- **References:** `<6a371be2.0206210702.190c150d@posting.google.com>`

```
Hello

I suggest you to visit www.pdf995.com.
You can also download the demo (a nag screen appears) and try
the product.
It is a small pdf device driver that allows you to generate
a Pdf file from any application, simply choosing through the
printer dialog.
Also there is an option to set the name of Pdf file in a way
you have no modify it. Or you can set the Pdf file name
directly each time you print a document.
It costs about $20. No more expensive and very easy to use.

I don't know Net Express, i'm using Fujitsu Powercobol and i
use this method to obtain the preview of my print works.
The pdf995 allows you to start Acrobat reader after the file
is created. This setting must be done with the pdfedit program
downloadable from the site above. 

Gianni


"Phil Hickling" <philhickling@compuserve.com> wrote in message
news:6a371be2.0206210702.190c150d@posting.google.com

> Any ideas please on how to produce print files that are both printable
> and viewable on the screen, from a MicroFocus NetExpress application? 
…[26 more quoted lines elided]…
> Phil Hickling.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
