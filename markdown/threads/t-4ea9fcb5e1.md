[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Datatype Translation

_16 messages · 9 participants · 2001-07_

---

### Cobol Datatype Translation

- **From:** Gary Scott <scottg@flash.net>
- **Date:** 2001-07-29T05:53:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B63A526.67F44A1D@flash.net>`

```

Hi,

I need to read in an MVS "binary" file (via Visual Fortran) created by
Cobol with a data
item(s) defined by:

PIC ... S9(005) COMP-3

The record description states that this takes 3 bytes and is signed.

Is that basically a definition for an integer with a range of -99999 -
+99999 stored in 20 bits with the rightmost 4 bits of the 3rd byte
representing the sign (sorry, don't know Cobol, just trying to interpret
from Murach's "Structured Cobol")?

Thanks
```

#### ↳ Re: Cobol Datatype Translation

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-07-28T23:33:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B63AE4C.CAD@paralynx.com>`
- **References:** `<3B63A526.67F44A1D@flash.net>`

```
Gary Scott wrote:
> 
> Hi,
…[12 more quoted lines elided]…
> from Murach's "Structured Cobol")?

In most implementations this is "packed decimal", which you might want to look up.

Basically, it squeezes 2 decimal digits into each byte (i.e. one digit in each nibble) 
except the last one which holds the sign in the low order nibble (a "nibble" is 4 bits, 
or half a byte - we were all great punsters 30 years ago).

You are right about the magnitude, but not about the storage method - it's not a 20 bit 
binary.  You'll have to "unpack" it nibble by nibble. The easiest way may be to do take 
each byte and do a /16 to get the high order nibble's decimal value and a %16 to get the 
low one. I'm not sure whether Visual Fortran (my Fortran stopped at Fortran IV) can bit 
twiddle, but I'm sure it can do modulo arithmetic.
```

##### ↳ ↳ Re: Cobol Datatype Translation

- **From:** Gary Scott <Gary.L.Scott@lmtas.lmco.com>
- **Date:** 2001-07-29T08:54:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B6415A5.5075C69@lmtas.lmco.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B63AE4C.CAD@paralynx.com>`

```
Thanks very much.  Yes bit twiddling is standard in Fortran 95.  It has
come a long way since Fortran IV:  free form source, a step towards
object orientation with modules, derived types, array syntax, and
overloading.  It's not your father's Fortran (or yours apparently) :-).

Ed Guy wrote:
> 
> Gary Scott wrote:
…[35 more quoted lines elided]…
>  and ParseRat, the File Parser, Converter and Reorganizer"
```

#### ↳ Re: Cobol Datatype Translation

- **From:** Gary Scott <Gary.L.Scott@lmtas.lmco.com>
- **Date:** 2001-07-29T08:58:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B641689.4D9953B5@lmtas.lmco.com>`
- **References:** `<3B63A526.67F44A1D@flash.net>`

```
Hi,
A followup:  This storage format does not seem to make very efficient
use of most systems native number crunching abilities.  Is this
definition intended for storage compactness or data portability?  Does
that not slow down the processing of large datasets?

Gary Scott wrote:
> 
> Hi,
…[14 more quoted lines elided]…
> Thanks
```

##### ↳ ↳ Re: Cobol Datatype Translation

- **From:** "Charles Godwin" <charles@godwin.ca>
- **Date:** 2001-07-29T10:39:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LcV87.4346$uH4.172992@news20.bellglobal.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com>`

```
The IBM mainframe has native opcodes / machine instructions for working with
pack numeric data. The chips are fast and efficient and include invalid
numeric hardware interrupts. I believe the data format was designed to allow
for arbitrary sized compressed business numeric data when approximations
implemented by floating point would not do the job.
"Gary Scott" <Gary.L.Scott@lmtas.lmco.com> wrote in message
news:3B641689.4D9953B5@lmtas.lmco.com...
> Hi,
> A followup:  This storage format does not seem to make very efficient
…[21 more quoted lines elided]…
> > Thanks
```

##### ↳ ↳ Re: Cobol Datatype Translation

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-07-29T18:57:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w0Z87.5823$bl1.869263@newsread1.prod.itd.earthlink.net>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com>`

```
Just the reverse.

The earliest 360 mainframes had circuitry to handle packed decimal
values up to a whole bunch of digits of precision (I seem to remember
18): far, far more than double-precision in Fortran. Remember, for the
most part, early mainframes did commercial work.


"Gary Scott" <Gary.L.Scott@lmtas.lmco.com> wrote in message
news:3B641689.4D9953B5@lmtas.lmco.com...
> Hi,
> A followup:  This storage format does not seem to make very
efficient
> use of most systems native number crunching abilities.  Is this
> definition intended for storage compactness or data portability?
Does
> that not slow down the processing of large datasets?
>
…[4 more quoted lines elided]…
> > I need to read in an MVS "binary" file (via Visual Fortran)
created by
> > Cobol with a data
> > item(s) defined by:
…[3 more quoted lines elided]…
> > The record description states that this takes 3 bytes and is
signed.
> >
> > Is that basically a definition for an integer with a range
of -99999 -
> > +99999 stored in 20 bits with the rightmost 4 bits of the 3rd byte
> > representing the sign (sorry, don't know Cobol, just trying to
interpret
> > from Murach's "Structured Cobol")?
> >
> > Thanks
>
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-07-29T22:46:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xm097.2807$XI.404299@paloalto-snr1.gtei.net>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <w0Z87.5823$bl1.869263@newsread1.prod.itd.earthlink.net>`

```
Jerry P <jerryp@bisusa.com> wrote in message
news:w0Z87.5823$bl1.869263@newsread1.prod.itd.earthlink.net...
>..  for the most part, early mainframes did commercial work.

So do most of the *current* mainframes.....

MCM
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-07-30T12:27:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pc97.36387$Cu6.2869784@bin3.nnrp.aus1.giganews.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <w0Z87.5823$bl1.869263@newsread1.prod.itd.earthlink.net> <Xm097.2807$XI.404299@paloalto-snr1.gtei.net>`

```
Well, of course.

The PC generation tend to think in terms of colors and JPGs and
counting mouse movements and stuff like that. Decimal notation was
some human evil that one must visit on user input and user output, not
something that could (or should) be native to the machine.

I meant to say that the rationale for getting a mainframe in the first
place was to do commercial work. As such, the mainframe had to be able
to handle commercial - base 10 - arithmetic.

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:Xm097.2807$XI.404299@paloalto-snr1.gtei.net...
> Jerry P <jerryp@bisusa.com> wrote in message
> news:w0Z87.5823$bl1.869263@newsread1.prod.itd.earthlink.net...
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol Datatype Translation

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-29T14:37:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B647412.AAC63A7D@sprynet.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com>`

```
Hi Gary.  Packed-decimal is a natural native number storage for IBM
S/390 mainframes (and it's predecessors), which is probably why it came
to be defined in COBOL.  In other words, S/390 machine code has
instructions to handle packed-decimal as easy (or easier? I don't know
much about assembler) as binary data.

Gary Scott wrote:
> 
> Hi,
…[22 more quoted lines elided]…
> > Thanks
```

##### ↳ ↳ Re: Cobol Datatype Translation

- **From:** Gary Scott <scottg@flash.net>
- **Date:** 2001-07-30T01:52:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B64BE0E.ED9E0AEB@flash.net>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com>`

```
Hi,

Thanks to all.  I finished my packed decimal and zoned decimal
conversion routines this morning.  They work perfectly, but I'll
probably need to tune them for performance.  With a multi-hundred
megabyte mainframe dump of accounting data, it takes way too long to
crunch it on my puny little PC.

Gary Scott wrote:
> 
> Hi,
…[22 more quoted lines elided]…
> > Thanks
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-07-29T21:03:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B64DC82.3EAB@paralynx.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <3B64BE0E.ED9E0AEB@flash.net>`

```
Gary Scott wrote:
> 
> Hi,
…[5 more quoted lines elided]…
> crunch it on my puny little PC.

With today's PC speeds I'd be surprised if the conversion routines are the bottleneck, 
you'll more likely be I/O bound.

I just repeated a test I did for a ParseRat user with a 1040 character input record 
length and 95 fields. The conversions were from a binary file to an ASCII delimited 
string file with some being binary-number-to-string conversions and others simple string 
extractions. On a 455 MHz PC it did 1627 records in ten seconds (almost 10,000 records 
per minute) and I'm sure I/O was the limiting factor.
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

_(reply depth: 4)_

- **From:** Gary Scott <Gary.L.Scott@lmtas.lmco.com>
- **Date:** 2001-07-30T09:05:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B6569C4.B35BA53@lmtas.lmco.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <3B64BE0E.ED9E0AEB@flash.net> <3B64DC82.3EAB@paralynx.com>`

```
Hi,
Yes, likely I/O bound, however conversion using Fortran formatted reads
is also somewhat slow.  I'll probably change it to use stream I/O
("binary") into a single data item of sufficient size to hold one
complete record.  This usually significantly improves I/O performance. 
Then, change it to only convert the particular portion of the record
that I'm using to sort on and only convert the remaining parts of the
record if it is the record of interest. 

Ed Guy wrote:
> 
> Gary Scott wrote:
…[25 more quoted lines elided]…
>  and ParseRat, the File Parser, Converter and Reorganizer"
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

_(reply depth: 5)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-30T11:46:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107301046.7a762ef6@posting.google.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <3B64BE0E.ED9E0AEB@flash.net> <3B64DC82.3EAB@paralynx.com> <3B6569C4.B35BA53@lmtas.lmco.com>`

```
Gary Scott <Gary.L.Scott@lmtas.lmco.com> wrote 
.
> Hi,
> Yes, likely I/O bound, however conversion using Fortran formatted reads
…[6 more quoted lines elided]…
> 
*-----------------------------------

On MOST mainframes, record size is not important (unless the records
are "spanned", i.e., too large for a block).  The crucial factors in
I/O management are blocksize and number of buffers.

Stephen J Spiro
Wizard Systems
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

_(reply depth: 6)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-07-30T12:58:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B65BC6E.5FF8@paralynx.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <3B64BE0E.ED9E0AEB@flash.net> <3B64DC82.3EAB@paralynx.com> <3B6569C4.B35BA53@lmtas.lmco.com> <4145699b.0107301046.7a762ef6@posting.google.com>`

```
Stephen J Spiro wrote:
> 
> Gary Scott <Gary.L.Scott@lmtas.lmco.com> wrote
…[14 more quoted lines elided]…
> I/O management are blocksize and number of buffers.

The question was about using Visual Fortran (I think) on a PC to do the conversion. The 
speed limiting factor is likely the actual volume of bytes per second processed through 
the disk controller.

I'll agree that on a mainframe the situation is different.  I once worked with a man who 
would bet people that he could double their application speeds by adjusting JCL alone, 
and he didn't lose many bets.
```

###### ↳ ↳ ↳ Re: Cobol Datatype Translation

_(reply depth: 6)_

- **From:** Gary Scott <Gary.L.Scott@lmtas.lmco.com>
- **Date:** 2001-07-30T15:12:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B65BFC4.72AF4985@lmtas.lmco.com>`
- **References:** `<3B63A526.67F44A1D@flash.net> <3B641689.4D9953B5@lmtas.lmco.com> <3B64BE0E.ED9E0AEB@flash.net> <3B64DC82.3EAB@paralynx.com> <3B6569C4.B35BA53@lmtas.lmco.com> <4145699b.0107301046.7a762ef6@posting.google.com>`

```
Hi, the source has been downloaded on to a PC.  The PC performance
problem is largely the result of my reading the file in as a series of
separate data items rather than as a single 135 byte stream.  I've shown
about a 20% increase in performance by reading multiple whole records
before performing the datatype conversions.

Stephen J Spiro wrote:
> 
> Gary Scott <Gary.L.Scott@lmtas.lmco.com> wrote
…[17 more quoted lines elided]…
> Wizard Systems
```

#### ↳ Re: Cobol Datatype Translation

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-07-29T19:36:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mBZ87.10678$ar1.32543@www.newsranger.com>`
- **References:** `<3B63A526.67F44A1D@flash.net>`

```
Hi Gary, 

The only thing you left out is that each 4 bit group (nibble) except for the
sign nibble represents a decimal digit (0-9).
And if the data is EBCIDIC the sign nibble is hex C, A, E or F (positive) ; D or
B (negative).

Regards, Jack.  

In article <3B63A526.67F44A1D@flash.net>, Gary Scott says...
>
>
…[15 more quoted lines elided]…
>Thanks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
