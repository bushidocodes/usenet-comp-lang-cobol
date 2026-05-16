[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol identifiers

_7 messages · 4 participants · 2003-04_

---

### cobol identifiers

- **From:** Kris De Schutter <legolas.greenleaf@advalvas.be>
- **Date:** 2003-04-01T13:43:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6bto8$ak5$1@gaudi2.rug.ac.be>`

```
Hi,

According to this (http://www.cs.vu.nl/grammars/browsable/vs-cobol-ii/) 
grammar of cobol an identifier can have something called a "leftmost 
character position".

Could any of you tell me what this is used for, and whether this is used 
frequently in real-life applications ?

Many thanks,

Kris De Schutter
```

#### ↳ Re: cobol identifiers

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-01T07:20:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AN6cnaSgktWuDxSjXTWcoA@giganews.com>`
- **References:** `<b6bto8$ak5$1@gaudi2.rug.ac.be>`

```

"Kris De Schutter" <legolas.greenleaf@advalvas.be> wrote in message
news:b6bto8$ak5$1@gaudi2.rug.ac.be...
> Hi,
>
…[7 more quoted lines elided]…
> Many thanks,

You have an alphanumeric data field. It contains characters (blank is a
character). The one on the left is the "leftmost character position."

Alternatively, you have an alphanumeric data field. It contains characters
(blank is a character). You want to access some of the field. The beginning
byte you wish to access is the leftmost character position. In the example:

01 MyData    Pic X(10) Value 'manuscript'.

Move MyData(3:2) to Whats-C-Over-Lamda

"n" is the leftmost character position of the intended move.

I'm guessing you are a beginner at COBOL. DO NOT read any more of the
document you referenced. The document is intended pick-noses, blowhards,
pedants, and four-flushers more interested in process than progress.
```

##### ↳ ↳ Re: cobol identifiers

- **From:** Kris De Schutter <legolas.greenleaf@advalvas.be>
- **Date:** 2003-04-01T15:49:22+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6c552$d5o$1@gaudi2.rug.ac.be>`
- **In-Reply-To:** `<AN6cnaSgktWuDxSjXTWcoA@giganews.com>`
- **References:** `<b6bto8$ak5$1@gaudi2.rug.ac.be> <AN6cnaSgktWuDxSjXTWcoA@giganews.com>`

```
Is this feature used often in realistic code ?

JerryMouse wrote:
> I'm guessing you are a beginner at COBOL.

True :-)

> DO NOT read any more of the
> document you referenced. The document is intended pick-noses, blowhards,
> pedants, and four-flushers more interested in process than progress.

Actually, I don't have much choice in the matter. I'm using their parser 
(in bison) for a project, and therefore that document is very relevant 
to my work.

Thanks for your help.

Kris De Schutter
```

###### ↳ ↳ ↳ Re: cobol identifiers

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-01T10:48:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f7ucnckLMLxcXxSjXTWcow@giganews.com>`
- **References:** `<b6bto8$ak5$1@gaudi2.rug.ac.be> <AN6cnaSgktWuDxSjXTWcoA@giganews.com> <b6c552$d5o$1@gaudi2.rug.ac.be>`

```

"Kris De Schutter" <legolas.greenleaf@advalvas.be> wrote in message
news:b6c552$d5o$1@gaudi2.rug.ac.be...
> Is this feature used often in realistic code ?
>
…[12 more quoted lines elided]…
>

The "left-most character" notation used in this document is an attempt to
define the obvious by academic fuddy-duddies. In the instance I gave, the
construct is called "Reference Modification." By that is meant: You
reference something (a data name), then you modify the reference (start at
the 15th byte) instead of using the implicit beginning of the variable as
originally contemplated by the language developers.

Almost every other language has the ability to reference data fields at the
byte level; COBOL did too, in the beginning, but the method was entirely too
cumbersome. Later implementations of the standard gave us other tools -
Reference Modification being one.

Is it used? You bet! Daily. Hourly. By almost every COBOL programmer.
Nobody, however, uses the "Leftmost Character" nomenclature.

If you can't avoid further reading of the document, drop the course and
demand your money back. Or at least threaten to put a hex (not base sixteen,
the other one) on the professor.
```

###### ↳ ↳ ↳ Re: cobol identifiers

_(reply depth: 4)_

- **From:** Kris De Schutter <legolas.greenleaf@advalvas.be>
- **Date:** 2003-04-02T09:13:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6e2al$196$1@gaudi2.rug.ac.be>`
- **In-Reply-To:** `<f7ucnckLMLxcXxSjXTWcow@giganews.com>`
- **References:** `<b6bto8$ak5$1@gaudi2.rug.ac.be> <AN6cnaSgktWuDxSjXTWcoA@giganews.com> <b6c552$d5o$1@gaudi2.rug.ac.be> <f7ucnckLMLxcXxSjXTWcow@giganews.com>`

```

JerryMouse wrote:
> The "left-most character" notation used in this document is an attempt to
> define the obvious by academic fuddy-duddies. In the instance I gave, the
…[3 more quoted lines elided]…
> originally contemplated by the language developers.

Ah, ok. I can see the use for this. :-)

> Almost every other language has the ability to reference data fields at the
> byte level; COBOL did too, in the beginning, but the method was entirely too
> cumbersome. Later implementations of the standard gave us other tools -
> Reference Modification being one.

Right.

> Is it used? You bet! Daily. Hourly. By almost every COBOL programmer.
> Nobody, however, uses the "Leftmost Character" nomenclature.

That's all I wanted to know. Many thanks for your help. :-)

> If you can't avoid further reading of the document, drop the course and
> demand your money back. Or at least threaten to put a hex (not base sixteen,
> the other one) on the professor.

This is not for a course (though my calling it a project may have hinted 
at that). It is very much work related. So you'll forgive me for holding 
back the hexes. ;-)

Cheers,

Kris
```

#### ↳ Re: cobol identifiers

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-01T14:51:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6c91h$oar$1@peabody.colorado.edu>`
- **References:** `<b6bto8$ak5$1@gaudi2.rug.ac.be>`

```

On  1-Apr-2003, Kris De Schutter <legolas.greenleaf@advalvas.be> wrote:

> According to this (http://www.cs.vu.nl/grammars/browsable/vs-cobol-ii/)
> grammar of cobol an identifier can have something called a "leftmost
…[3 more quoted lines elided]…
> frequently in real-life applications ?

My guess is that this is referring to limits in how an identifier can be named.
 e.g.   MYVARIABLE1 vs 1MYVARIABLE.

It isn't something I ever think about.
```

#### ↳ Re: cobol identifiers

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-02T19:15:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6coh8$bbj$1@aklobs.kc.net.nz>`
- **References:** `<b6bto8$ak5$1@gaudi2.rug.ac.be>`

```
Kris De Schutter wrote:

> According to this (http://www.cs.vu.nl/grammars/browsable/vs-cobol-ii/)
> grammar of cobol an identifier can have something called a "leftmost
> character position".

Are you talking about source code or data content ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
