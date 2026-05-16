[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# reading input files and then output

_9 messages · 9 participants · 2001-11_

---

### reading input files and then output

- **From:** "Playahp" <playahp@hotmail.com>
- **Date:** 2001-11-21T14:35:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
How do I read from a file, store it into another file and then output that
stored file into a printable format?
```

#### ↳ Re: reading input files and then output

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-21T19:49:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9th0b6$k1q$1@peabody.colorado.edu>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```

On 21-Nov-2001, "Playahp" <playahp@hotmail.com> wrote:

> How do I read from a file, store it into another file and then output that
> stored file into a printable format?

I strongly recommend writing two programs.
```

#### ↳ Re: reading input files and then output

- **From:** "Jeff Farkas" <JeffFarkas@noland.com>
- **Date:** 2001-11-21T15:04:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9th1d5$2g9hp$1@ID-101435.news.dfncis.de>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```

"Playahp" <playahp@hotmail.com> wrote in message
news:vmTK7.61669$Z2.922478@nnrp1.uunet.ca...
> How do I read from a file, store it into another file and then output
that
> stored file into a printable format?

One or two COBOL programs might be the
trick.

Jeff..
```

#### ↳ Re: reading input files and then output

- **From:** "alex" <alex@gofuckyourself.com>
- **Date:** 2001-11-21T21:01:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uCUK7.199673$W8.7507475@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
pick up the file
put it in a cabinet
then put the cabinet on a printer dumbass


Playahp wrote in message ...
>How do I read from a file, store it into another file and then output that
>stored file into a printable format?
>
>
```

#### ↳ Re: reading input files and then output

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-11-21T22:07:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xAVK7.71962$2w.3856975@bin4.nnrp.aus1.giganews.com>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
I bid THREE programs.

"Playahp" <playahp@hotmail.com> wrote in message
news:vmTK7.61669$Z2.922478@nnrp1.uunet.ca...
> How do I read from a file, store it into another file and then output that
> stored file into a printable format?
>
>
>
```

#### ↳ Re: reading input files and then output

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-11-21T23:31:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DPWK7.2599$rY1.228699@dfiatx1-snr1.gtei.net>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
Playahp <playahp@hotmail.com> wrote in message
news:vmTK7.61669$Z2.922478@nnrp1.uunet.ca...
> How do I read from a file, store it into another file and then output that
> stored file into a printable format?
>

You don't.

You read from the file, output it in printable format, then store it in
another file.

(What *are* they teaching in programming class these days?)

MCM
```

#### ↳ Re: reading input files and then output

- **From:** Steve Thompson <s_thompson@ix.netcom.com>
- **Date:** 2001-11-21T19:01:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BFC4053.802698DC@ix.netcom.com>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
It might be a good thing if you were to do your own
homework. Most of us here can recognize a homework question
before we've finished reading the first sentence. And I'd
bet that the majority could come up with three different
ways to do what you ask inside of 1 program.

Playahp wrote:
> 
> How do I read from a file, store it into another file and then output that
> stored file into a printable format?
```

#### ↳ Re: reading input files and then output

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-11-22T04:54:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ix%K7.179123$3d2.7862572@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
That's easy.  Define two output files.  One it the print file.
Prior to the write of the output file, edit a print line for the second file
(if needed.)
Write to output file, write to printer file.

Warren Simmons
CobolSimmons@tinycobol.org

Playahp <playahp@hotmail.com> wrote in message
news:vmTK7.61669$Z2.922478@nnrp1.uunet.ca...
> How do I read from a file, store it into another file and then output that
> stored file into a printable format?
>
>
```

#### ↳ Re: reading input files and then output

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2001-11-22T01:50:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0111220150.24b0ec9c@posting.google.com>`
- **References:** `<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>`

```
"Playahp" <playahp@hotmail.com> wrote in message news:<vmTK7.61669$Z2.922478@nnrp1.uunet.ca>...
> How do I read from a file, store it into another file and then output that
> stored file into a printable format?

Before asking any question in CLC, please go to
http://objectz.com/faqs/cobolfaq.htm and learn how to formulate an
"answerable" one!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
