[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (ACU)Cobol Data File dump

_9 messages · 5 participants · 2001-05_

---

### (ACU)Cobol Data File dump

- **From:** "Art" <awgroeneveld@zonnet.nl>
- **Date:** 2001-05-09T14:36:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hOaK6.120$pH4.4743@zonnet-reader-1>`

```
Is there anybody who knows how to read (ACU)Cobol Datafiles. I already
recognized a block pattern, but it doesn't help me much yet.

Is there some GPL or freeware program that does the trick. The definition of
the files is available.

Thnx in advance

Art
```

#### ↳ Re: (ACU)Cobol Data File dump

- **From:** "Dennis Edward" <temp081100@ipipeline.net>
- **Date:** 2001-05-09T14:46:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fLcK6.1525$5R2.69974329@news1.van.metronet.ca>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1>`

```
Where is the definition available from? Is it complete?


"Art" <awgroeneveld@zonnet.nl> wrote in message
news:hOaK6.120$pH4.4743@zonnet-reader-1...
> Is there anybody who knows how to read (ACU)Cobol Datafiles. I already
> recognized a block pattern, but it doesn't help me much yet.
>
> Is there some GPL or freeware program that does the trick. The definition
of
> the files is available.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: (ACU)Cobol Data File dump

- **From:** "Art" <awgroeneveld@zonnet.nl>
- **Date:** 2001-05-09T19:13:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AReK6.134$pH4.5780@zonnet-reader-1>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1> <fLcK6.1525$5R2.69974329@news1.van.metronet.ca>`

```
I have a complete definition of the record structure, however, every 11KB
there is a chunk of index data or so. So this should be worked around :-((.
Otherwise it would be very straightforward to read.




"Dennis Edward" <temp081100@ipipeline.net> wrote in message
news:fLcK6.1525$5R2.69974329@news1.van.metronet.ca...
> Where is the definition available from? Is it complete?
>
…[6 more quoted lines elided]…
> > Is there some GPL or freeware program that does the trick. The
definition
> of
> > the files is available.
…[7 more quoted lines elided]…
>
```

#### ↳ Re: (ACU)Cobol Data File dump

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-09T16:54:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nDeK6.356$1k1.90344@dfiatx1-snr1.gtei.net>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1>`

```
You can get a tutorial on COBOL datatypes by downloading file COBDATA.ZIP
from www.flexus.com/softwaredownload.html

As long as you have the FD, you will be in pretty good shape as long as you
are not looking at an indexed file with some kind of internal index
structure. Even then, I think ParseRat has something specifically for
ACUCOBOL files. (That's commercial software; don't know the price of a
license).
```

##### ↳ ↳ Re: (ACU)Cobol Data File dump

- **From:** "Art" <awgroeneveld@zonnet.nl>
- **Date:** 2001-05-09T19:16:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IUeK6.136$pH4.5908@zonnet-reader-1>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1> <nDeK6.356$1k1.90344@dfiatx1-snr1.gtei.net>`

```
I tried Parserat(eval),  but it is not so very straightforward and lots of
manual handling. I'd prefer a library or so, in order to be able to load
data directly into a MySQL DB.


"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:nDeK6.356$1k1.90344@dfiatx1-snr1.gtei.net...
> You can get a tutorial on COBOL datatypes by downloading file COBDATA.ZIP
> from www.flexus.com/softwaredownload.html
>
> As long as you have the FD, you will be in pretty good shape as long as
you
> are not looking at an indexed file with some kind of internal index
> structure. Even then, I think ParseRat has something specifically for
…[15 more quoted lines elided]…
> > Is there some GPL or freeware program that does the trick. The
definition
> of
> > the files is available.
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: (ACU)Cobol Data File dump

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-09T18:28:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1%fK6.401$1k1.113180@dfiatx1-snr1.gtei.net>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1> <nDeK6.356$1k1.90344@dfiatx1-snr1.gtei.net> <IUeK6.136$pH4.5908@zonnet-reader-1>`

```
I don't know what you need to load the data into the MySQL DB, but to expect
you could find a "library" you could just 'plug in' is, well, 'ambitious.'
To think you could find such a library as freeware or PD software is just
plain wishful thinking.

I played with the ParseRat evauation package, too, and frankly I don't know
how you could find anything more straightforward than that; this kind of
data conversion is not an easy thing to do.

If you have an ACUCOBOL compiler - or know someone who does - the easiest
way to export this data is to write a program to extract data from the index
file and write it out into some "MySQL"-compatible format.

Meantime, read this:

http://www.flexus.com/ebd2asc.html

This deals with the whole issue of "I want to use COBOL-created data in my
non-COBOL application."


MCM
(author of said document)



Art <awgroeneveld@zonnet.nl> wrote in message
news:IUeK6.136$pH4.5908@zonnet-reader-1...
> I tried Parserat(eval),  but it is not so very straightforward and lots of
> manual handling. I'd prefer a library or so, in order to be able to load
…[5 more quoted lines elided]…
> > You can get a tutorial on COBOL datatypes by downloading file
COBDATA.ZIP
> > from www.flexus.com/softwaredownload.html
> >
…[32 more quoted lines elided]…
>
```

#### ↳ Re: (ACU)Cobol Data File dump

- **From:** "Ray Smith" <Ray.Smith@fujitsu.com.au>
- **Date:** 2001-05-10T09:14:17+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9dcf6j$e89@newshost.fujitsu.com.au>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1>`

```
Hi,

If you have an AcuCobol file I would assume somewhere someone you are
working with has a registered
AcuCobol runtime.  If they have a runtime they should have access to a
program called "vutil" which will
unload any AcuCobol file into a plain text file.  Which you can then import
into anything.

If the file(s) are small you could send them to me, I'll unload them to text
files and send them back.

Ray Smith


Art <awgroeneveld@zonnet.nl> wrote in message
news:hOaK6.120$pH4.4743@zonnet-reader-1...
> Is there anybody who knows how to read (ACU)Cobol Datafiles. I already
> recognized a block pattern, but it doesn't help me much yet.
>
> Is there some GPL or freeware program that does the trick. The definition
of
> the files is available.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: (ACU)Cobol Data File dump

- **From:** "Art" <awgroeneveld@zonnet.nl>
- **Date:** 2001-05-10T22:45:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S1DK6.530$pH4.15055@zonnet-reader-1>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1> <9dcf6j$e89@newshost.fujitsu.com.au>`

```
Why couldn't anyone else think of that. You've been of great help. Thanx !


"Ray Smith" <Ray.Smith@fujitsu.com.au> wrote in message
news:9dcf6j$e89@newshost.fujitsu.com.au...
> Hi,
>
…[4 more quoted lines elided]…
> unload any AcuCobol file into a plain text file.  Which you can then
import
> into anything.
>
> If the file(s) are small you could send them to me, I'll unload them to
text
> files and send them back.
>
…[8 more quoted lines elided]…
> > Is there some GPL or freeware program that does the trick. The
definition
> of
> > the files is available.
…[7 more quoted lines elided]…
>
```

#### ↳ Re: (ACU)Cobol Data File dump

- **From:** Vadim Maslov <vadik-nws@siber.com>
- **Date:** 2001-05-10T02:05:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF9F796.93454236@siber.com>`
- **References:** `<hOaK6.120$pH4.4743@zonnet-reader-1>`

```
There is one way...

Siber Systems has a library that can read AcuCobol data files.
Based on this library, we build a number of tools that can convert
Acu datafiles to CSV or DBF or even read them into Crystal Reports.

More on it here:
http://www.siber.com/sct/datafile/

The converter will cost you less than $500.
If you are only beginning to unedrstand the format
then the rest will take just 3 to 6 months.
So if you are not getting < $1/hour for your work,
our price should be relatively cheap.

Regards,
Vadim Maslov

Art wrote:
> 
> Is there anybody who knows how to read (ACU)Cobol Datafiles. I already
…[7 more quoted lines elided]…
> Art
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
