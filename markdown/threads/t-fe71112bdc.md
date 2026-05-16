[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I have a problem with a Data File

_7 messages · 7 participants · 2001-12_

---

### I have a problem with a Data File

- **From:** "Ambrosio" <AMBROS@nettaxi.com>
- **Date:** 2001-12-05T10:03:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9uknq6$sj3$1@diana.bcn.ttd.net>`

```
Hi all.

    I�m gonna make a new Visual Basic program to a dentist. He has right now
a cobol based program but he wants to upgrade.
    This cobol program has a huge data files, but I haven�t got any FD of
them.
    Well, I�m Searching a tool that allow me to read this file and export it
as a raw text, or Access Table or SQL table or anything else. So, from that
intermediate format I could attack it with  Visual Basic.

Thanks in advance.
```

#### ↳ Re: I have a problem with a Data File

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-12-05T11:56:03+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<nXnP7.35$Ko.15291@dfiatx1-snr1.gtei.net>`
- **References:** `<9uknq6$sj3$1@diana.bcn.ttd.net>`

```
Ambrosio <AMBROS@nettaxi.com> wrote in message
news:9uknq6$sj3$1@diana.bcn.ttd.net...
>
>     I�m gonna make a new Visual Basic program to a dentist. He has right
now
> a cobol based program but he wants to upgrade.
>     This cobol program has a huge data files, but I haven�t got any FD of
> them.
>     Well, I�m Searching a tool that allow me to read this file and export
it
> as a raw text, or Access Table or SQL table or anything else. So, from
that
> intermediate format I could attack it with  Visual Basic.

(I also posted reply to alt.cobol, where you asked in a separate post).

See, for sure: http://www.flexus.com/ebd2asc.html

That deals with the subject of "Using COBOL-created data across platforms or
with non-COBOL language products."

Unfortunately for you, the one requirement for using your data is you need
the FD.  Without it, you are reduced to "deducing" the FD by inspecting
bytes and guessing record lengths, PICTURE clauses and the like.

There are some software tools available which can make the guesswork a lot
easier and/or "guess" for you  and I'm sure those vendors will chime in, but
without an FD you are in deep doo-doo.

Contact the vendor of the other software. They have got to have the FD; and
if they are any form of life higher  than pond scum they will make it
available to you. They may not make available all the detailed meanings of
each field, but those are not always important when doing a data conversion.
```

##### ↳ ↳ Re: I have a problem with a Data File

- **From:** "Lansdale" <lansdale@optonline.net>
- **Date:** 2001-12-07T02:44:53+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<F2WP7.15251$MX1.4517733@news02.optonline.net>`
- **References:** `<9uknq6$sj3$1@diana.bcn.ttd.net> <nXnP7.35$Ko.15291@dfiatx1-snr1.gtei.net>`

```
One way interpret what the fields mean if you do not have source code is to
do some controled data entry.
Have the user enter some data of each type into form they use. Then scan the
text file for same data.




"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:nXnP7.35$Ko.15291@dfiatx1-snr1.gtei.net...
> Ambrosio <AMBROS@nettaxi.com> wrote in message
> news:9uknq6$sj3$1@diana.bcn.ttd.net...
…[4 more quoted lines elided]…
> >     This cobol program has a huge data files, but I haven�t got any FD
of
> > them.
> >     Well, I�m Searching a tool that allow me to read this file and
export
> it
> > as a raw text, or Access Table or SQL table or anything else. So, from
…[7 more quoted lines elided]…
> That deals with the subject of "Using COBOL-created data across platforms
or
> with non-COBOL language products."
>
…[5 more quoted lines elided]…
> easier and/or "guess" for you  and I'm sure those vendors will chime in,
but
> without an FD you are in deep doo-doo.
>
> Contact the vendor of the other software. They have got to have the FD;
and
> if they are any form of life higher  than pond scum they will make it
> available to you. They may not make available all the detailed meanings of
> each field, but those are not always important when doing a data
conversion.
>
> --
…[8 more quoted lines elided]…
>
```

#### ↳ Re: I have a problem with a Data File

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-05T13:56:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8IpP7.96210$ox2.5195907@bin4.nnrp.aus1.giganews.com>`
- **References:** `<9uknq6$sj3$1@diana.bcn.ttd.net>`

```
Depending on the file type, your quest may well be impossible, even with the
FD. For example, all ISAM files have proprietary formats that depend on the
vendor. While some have been translators, many have not. Two solutions we've
used are:

1. The existing system MAY have a method of exporting the data into a text
format.

2. The original vendor can be of immense help. Assuming your mutual client
is in good standing with the original vendor, they should willing (although
not pleased) to assist in the conversion.

Of course you know you are undertaking a life-time job. Medicare and
insurance requirements change almost daily (even more often than payroll tax
tables).


"Ambrosio" <AMBROS@nettaxi.com> wrote in message
news:9uknq6$sj3$1@diana.bcn.ttd.net...
> Hi all.
>
>     I�m gonna make a new Visual Basic program to a dentist. He has right
now
> a cobol based program but he wants to upgrade.
>     This cobol program has a huge data files, but I haven�t got any FD of
> them.
>     Well, I�m Searching a tool that allow me to read this file and export
it
> as a raw text, or Access Table or SQL table or anything else. So, from
that
> intermediate format I could attack it with  Visual Basic.
>
…[3 more quoted lines elided]…
>
```

#### ↳ Re: I have a problem with a Data File

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-12-05T08:06:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0E4607.2C7E@paralynx.com>`
- **References:** `<9uknq6$sj3$1@diana.bcn.ttd.net>`

```
Ambrosio wrote:
> 
> Hi all.
…[7 more quoted lines elided]…
> intermediate format I could attack it with  Visual Basic.

Take a look at ParseRat (http://www.parserat.com/).  Many people have used it in similar 
circumstances.  It's relatively easy if you know the file layout and will help you to 
deduce it if you don't - particularly if you know what the numeric data is SUPPOSED to 
be for a few records (text fields are easy, it's recognising which binary format, 
endianism etc. was used for numeric data that takes the time).
```

#### ↳ Re: I have a problem with a Data File

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 2001-12-06T00:54:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0EC228.17C96341@siber.com>`
- **References:** `<9uknq6$sj3$1@diana.bcn.ttd.net>`

```
You can use DataGuess tool/service from Siber Systems.
We can reverse-engineer the layout of your Cobo data file
even if FD information was lost.

http://www.siber.com/sct/datafile/

Vadim Maslov


Ambrosio wrote:
> 
> Hi all.
…[9 more quoted lines elided]…
> Thanks in advance.
```

#### ↳ Re: I have a problem with a Data File

- **From:** "Bill Indreboe" <bill@dutycalc.com>
- **Date:** 2001-12-06T06:15:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<22EP7.145838$WW.9313497@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<9uknq6$sj3$1@diana.bcn.ttd.net>`

```
there is a company in Texas, I believe
Tools and Techniques
they have a very good (and very expensive) program called  Data Junction
that as I recall can convert anything to anything
they claim to be able to convert some three thousand data types

if you can't afford that, snip a small (1k) portion of the file and email to
me at
bill (at) Dutycalc Dot Com and I might be able to tell you how to crack it
many files, even ISAM are easily converted

best luck to you,


Bill


Ambrosio wrote in message <9uknq6$sj3$1@diana.bcn.ttd.net>...
>Hi all.
>
>    I�m gonna make a new Visual Basic program to a dentist. He has right
now
>a cobol based program but he wants to upgrade.
>    This cobol program has a huge data files, but I haven�t got any FD of
>them.
>    Well, I�m Searching a tool that allow me to read this file and export
it
>as a raw text, or Access Table or SQL table or anything else. So, from that
>intermediate format I could attack it with  Visual Basic.
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
