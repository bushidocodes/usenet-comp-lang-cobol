[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A series decimal arithmetic was Re: Convert MainFrame Data [ EBCDIC ] To Ascii

_4 messages · 3 participants · 2003-05_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: A series decimal arithmetic was Re: Convert MainFrame Data [ EBCDIC ] To Ascii

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-05-14T11:22:52-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EC2513C.27FAB23A@istar.ca>`
- **References:** `<45147cf3.0303250704.6a7dd28@posting.google.com> <3e8d513b.5582563@news.optonline.net> <217e491a.0304041259.54d8d7cd@posting.google.com> <3e8ef7a0.37127268@news.optonline.net> <b6neh4$fi7$1@aklobs.kc.net.nz> <3e8f9b30.79006238@news.optonline.net> <b6s5g6$2v3c$1@si05.rsvl.unisys.com> <3E91A5CF.D7C18000@istar.ca>`

```
What hardware (microcode or chip) support is there for decimal
arithmetic in the A/NX/LX series and in whatever the Univac 1100/2200
evolved into?
```

#### ↳ Re: A series decimal arithmetic was Re: Convert MainFrame Data [ EBCDIC ] To Ascii

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-14T11:44:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9u2q7$1na5$1@si05.rsvl.unisys.com>`
- **References:** `<45147cf3.0303250704.6a7dd28@posting.google.com> <3e8d513b.5582563@news.optonline.net> <217e491a.0304041259.54d8d7cd@posting.google.com> <3e8ef7a0.37127268@news.optonline.net> <b6neh4$fi7$1@aklobs.kc.net.nz> <3e8f9b30.79006238@news.optonline.net> <b6s5g6$2v3c$1@si05.rsvl.unisys.com> <3E91A5CF.D7C18000@istar.ca> <3EC2513C.27FAB23A@istar.ca>`

```
Arithmetic on the MCP/AS system is done in binary.  There was some
discussion close to twenty years ago about the possibility of building
hardware to do decimal arithmetic directly as the V Series did, but
ultimately the architects reached the conclusion that much better "bang for
the buck" could be obtained by improving the decimal-to-binary and
binary-to-decimal conversion operators, and that the costs of a decimal
arithmetic box on the MCP/AS system could not be justified in terms of
performance gain.

I can't speak to the OS2200/IX line.

    -Chuck Stevens

"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3EC2513C.27FAB23A@istar.ca...
> What hardware (microcode or chip) support is there for decimal
> arithmetic in the A/NX/LX series and in whatever the Univac 1100/2200
> evolved into?
>
>
```

##### ↳ ↳ Re: A series decimal arithmetic was Re: Convert MainFrame Data [ EBCDIC ] To Ascii

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-14T12:16:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9u4mi$1ohi$1@si05.rsvl.unisys.com>`
- **References:** `<45147cf3.0303250704.6a7dd28@posting.google.com> <3e8d513b.5582563@news.optonline.net> <217e491a.0304041259.54d8d7cd@posting.google.com> <3e8ef7a0.37127268@news.optonline.net> <b6neh4$fi7$1@aklobs.kc.net.nz> <3e8f9b30.79006238@news.optonline.net> <b6s5g6$2v3c$1@si05.rsvl.unisys.com> <3E91A5CF.D7C18000@istar.ca> <3EC2513C.27FAB23A@istar.ca> <b9u2q7$1na5$1@si05.rsvl.unisys.com>`

```
I wrote:

<< Arithmetic on the MCP/AS system is done in binary.  >>

A clarification:  it's done in the native word-oriented format of the
machine.  Technically, the word contains a signed binary mantissa and a
signed exponent, the exponent representing the power of 8 by which the
mantissa is to be scaled.  Canonic single-precision integers form a subset
of that format, having an exponent of zero and the binary representation of
the value right-justified as the mantissa in the word.  Most COBOL-oriented
calculations start out with integer values and the results are integerized
(with rounding or with truncation as appropriate in context) before (and if)
they are to be converted back to some sort of external-decimal format.  The
"odometer effect" on intermediate results as they are stored in destinations
is handled as part of the scaling process through explicit instructions.

The B5/6/7000 series had an architectural anomaly with conversion
(determination of the sign of a decimal item was made based on contents, not
on PICTURE); so long as the data matched the PICTURE, everything was OK, but
if it didn't, the results presented some problems.  This anomaly was
resolved in the A Series by the addition of instructions that explicitly
stated whether there was a sign, and if so where it was located, for the
input conversion and pack operations.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: A series decimal arithmetic was Re: Convert MainFrame Data [ EBCDIC ] To Ascii

- **From:** gary drummond <gdrumm@sbcglobal.net>
- **Date:** 2003-05-22T02:27:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ECC35DC.9392FF57@sbcglobal.net>`
- **References:** `<45147cf3.0303250704.6a7dd28@posting.google.com> <3e8d513b.5582563@news.optonline.net> <217e491a.0304041259.54d8d7cd@posting.google.com> <3e8ef7a0.37127268@news.optonline.net> <b6neh4$fi7$1@aklobs.kc.net.nz> <3e8f9b30.79006238@news.optonline.net> <b6s5g6$2v3c$1@si05.rsvl.unisys.com> <3E91A5CF.D7C18000@istar.ca> <3EC2513C.27FAB23A@istar.ca> <b9u2q7$1na5$1@si05.rsvl.unisys.com> <b9u4mi$1ohi$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> 
> I wrote:
…[23 more quoted lines elided]…
>     -Chuck Stevens

The 1110 allowed 511/512? (I have trouble counting... :>) digits
in native ISO ASCII in decimal math hardware instructions. If I
could find my books, I could tell you if they had "packed" decimal
instructions, and the length of the addends/etc...

The follow-on systems supported the previous instructions, and also
added more of the IBM-type decimal instructions. All of them required
loading a register (pair?) with a binary editing mask for the edit
instructions, but with about 43 registers, they could be loaded once
during initial load and left there.

I'll email any other "facts" if I can find my books.

Gary
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
