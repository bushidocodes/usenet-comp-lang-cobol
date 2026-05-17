[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC COBOL and EBCDIC question

_5 messages · 5 participants · 1996-08 → 1996-09_

---

### PC COBOL and EBCDIC question

- **From:** "brian mccarthy" <ua-author-2535103@usenetarchives.gap>
- **Date:** 1996-08-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<321A31A4.5538@utrc.utc.com>`

```

I've just been informed that I need to convert a file on a regular
basis from one format in ASCII (from an RS6000) to a different format,
in EBCDIC with packed EBCDIC numeric fields.

Up to this point we don't have a COBOL compiler for the RS6000, nor
even for a PC. My question is: would a COBOL program on either
the RS6000 or a PC be a good way to make the conversion, i.e. read
in an ASCII file, do various MOVE's and calculations, then write out
an EBCDIC file?

If so, which compilers can do this, or can they all?

EBCDIC is outside my comfort zone, since even in the old COBOL days
we were a Sperry 1100 shop and didn't do EBCDIC; so forgive me if
I'm asking a dumb question.

But please answer quickly before they make me do it in C!

Brian McCarthy
b.··.@utr··c.com
```

#### ↳ Re: PC COBOL and EBCDIC question

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1996-08-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-adc5632d2b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<321A31A4.5538@utrc.utc.com>`
- **References:** `<321A31A4.5538@utrc.utc.com>`

```


› I've just been informed that I need to convert a file on a regular
› basis from one format in ASCII (from an RS6000) to a different format,
› in EBCDIC with packed EBCDIC numeric fields.
 
› What format is the original RS6000 file in? sequential? indexed?
 
› Up to this point we don't have a COBOL compiler for the RS6000, nor
› even for a PC.

So how is the file produced? Is it an application written in COBOL? If it is,
you may have to go with the same compiler vendor as the people who wrote the
application.

› My question is: would a COBOL program on either
› the RS6000 or a PC be a good way to make the conversion, i.e. read
› in an ASCII file, do various MOVE's and calculations, then write out
› an EBCDIC file?
 
› If so, which compilers can do this, or can they all?

You may not have the choice if the file is in a proprietry vendors format. If
it's a Micro Focus generated file, Micro Focus provide tools to convert
between ASCII<>EBCDIC and into other formats automatically. see
http://www.mfltd.co.uk . I'm sure other vendors do similar products.

› EBCDIC is outside my comfort zone, since even in the old COBOL days
› we were a Sperry 1100 shop and didn't do EBCDIC; so forgive me if
› I'm asking a dumb question.

EBCDIC is truely evil. I had to write conversion routines for it when I was at
Micro Focus. If you want real evil, try converting Japanese EBCDIC to Shift-
JIS double byte characters. ;-(

› But please answer quickly before they make me do it in C!

Even more frightening! If you *have* to use a program to do it, Micro Focus
COBOL has EBCDIC to ASCII routines you can call called "CODESET". You do
something like...

call "_CODESET" using function
string
end-call

change the function number depending on the direction of conversion. This
doesn't help with the packed numbers but that isn't too hard to figure.


------------------------------------------------------------------------
-- Shaun C. Murray (E-mail: s.··.@ent··e.net) --
------------------------------------------------------------------------
```

#### ↳ Re: PC COBOL and EBCDIC question

- **From:** "neil duffee" <ua-author-5508101@usenetarchives.gap>
- **Date:** 1996-08-24T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-adc5632d2b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<321A31A4.5538@utrc.utc.com>`
- **References:** `<321A31A4.5538@utrc.utc.com>`

```

Brian McCarthy wrote:
› I've just been informed that I need to convert a file on a regular
› basis from one format in ASCII (from an RS6000) to a different format,
› in EBCDIC with packed EBCDIC numeric fields.

Here's an answer that's from way out in left field and contains a few
IFs but might solve your problem. I presume that you're talking about a
file of *data* rather than program sources. The main question is *how*
you will transfer the file from one machine to another. IF your data
can be massaged on the originating EBCDIC machine and presented to the
transfer process as strictly display text ie. no packed-numeric nor
binary fields - where 123='F1F2F3'H and not '123C'H or '01111011'B, you
might investigate IF you can FTP from one machine to another and let
*it* do the translation for you.

Sure you might spend a small amount of time learning how to set up the
utility on the EBCDIC machine to convert the Display format to packed
numeric but that's an easier converter to write. For example, on MVS,
IEBGENER can do such a thing or, at the worst, you have to write a quick
but easy Cobol program (Read, Move corresponding, Write).

Alternatively, most workstation 3270 emulators have *some* mechanism to
upload/download files. We use these kinds of things all the time to
allow our users to create lookup tables in WordPerfect which we upload
to DB2 via FTP then some DSN utility. (Of course, we have problems with
code-pages and accented characters in the upper ASCII range that don't
translate properly but we're Canadian, eh? ;^)
---------------> signature = 3 lines follows <-------------------
Neil Duffee, Joe Code Grinder, U d'Ottawa, Ottawa, Ontario, Canada
mailto:nj··.@uot··a.ca or http://aix1.uottawa.ca/~njd2e
"How *do* you plan for something like that?" Guardian Bob, Reboot
```

##### ↳ ↳ Re: PC COBOL and EBCDIC question

- **From:** "cr..." <ua-author-17087468@usenetarchives.gap>
- **Date:** 1996-09-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-adc5632d2b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-adc5632d2b-p3@usenetarchives.gap>`
- **References:** `<321A31A4.5538@utrc.utc.com> <gap-adc5632d2b-p3@usenetarchives.gap>`

```

Neil Duffee writes:

› Brian McCarthy wrote:
›› I've just been informed that I need to convert a file on a regular
›› basis from one format in ASCII (from an RS6000) to a different format,
›› in EBCDIC with packed EBCDIC numeric fields.
 
› Here's an answer that's from way out in left field and contains a few
› IFs but might solve your problem.  I presume that you're talking about a
…[6 more quoted lines elided]…
› *it* do the translation for you.  

I am tasked with translating EBCDIC data (Motor Vehicle Registration
Data from Mass.) into useable ASCII data (for input into RBase). I've
come up with a C program to strip all of the garbage characters after the
translation (no usefull data is lost in that), but the date fields are
all in some sort of packed format, and after translation to ASCII look
a garbled mess.
The original data is created and manipulated using COBOL on an IBM
mainframe; I'm using an HP workstation, but I have limited access to a
local IBM mainframe with COBOL on it. If anyone here can give me any
leads on how to recover those crucial date fields I would be eternally
thankful!

Chris Riggins
Air Quality Laboratory
Christopher Riggins                Graduate FASET             894-1943
Georgia Institute of Technology    Air Quality Lab            853-3095
cr··.@pri··h.edu
```

###### ↳ ↳ ↳ Re: PC COBOL and EBCDIC question

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-09-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-adc5632d2b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-adc5632d2b-p4@usenetarchives.gap>`
- **References:** `<321A31A4.5538@utrc.utc.com> <gap-adc5632d2b-p3@usenetarchives.gap> <gap-adc5632d2b-p4@usenetarchives.gap>`

```

›    The original data is created and manipulated using COBOL on an IBM
› mainframe; I'm using an HP workstation, but I have limited access to a
› local IBM mainframe with COBOL on it.  If anyone here can give me any 
› leads on how to recover those crucial date fields I would be eternally
› thankful!


Since you threw out those characters that had no 'obvious' value you
lost forever some data.

Except for the rightmost byte in the packed fields, each byte consists
of a pair of 4-bit values ranging from 0 to 9. Those pairs can
translate into whatever your table defaults these to.
Since you discarded non-understandable bytes....oops.

The right most byte is a pair of 4-bits where the first again ranges
from 0 to 9 and the second is a sign which is typically either hex F,
C, or D where the D is negative and both the others, during
translation, can be treated as positive. Again if these fields were
block translated from EBCDIC to ASCII....G-B...G-B...G-B...that's all
folks

Example:
last byte of packed value -100 is 0- is hex 0D
(carriage return as a character)

Try to get the original data flattened on the mainframe or get the
original data imported as binary for your own conversion.

Good luck

JR

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
