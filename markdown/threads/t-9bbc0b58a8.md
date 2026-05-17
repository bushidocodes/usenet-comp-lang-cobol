[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indenting

_3 messages · 3 participants · 1997-02_

---

### Indenting

- **From:** "steven lang" <ua-author-6639575@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<331597B5.3EF8@gssec.bt.co.uk>`

```

Hi

Does anyone know of a utility which automatically adds indentation to
COBOL code? The code in question has gone though custom IDMS to DB2
conversion utilities, but this has removed all of the indentation. We've
tried COBCLEAN, but this doesn't do the job.

Thanks
```

#### ↳ Re: Indenting

- **From:** "nor..." <ua-author-17071493@usenetarchives.gap>
- **Date:** 1997-02-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bbc0b58a8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<331597B5.3EF8@gssec.bt.co.uk>`
- **References:** `<331597B5.3EF8@gssec.bt.co.uk>`

```

On Thu, 27 Feb 1997 14:18:29 +0000, Steven Lang
wrote:

>Hi
>
…[5 more quoted lines elided]…
>Thanks

Now wait just a minute here.
As the author of that program I can assure you it does indeed
do the job.

I have been working with your Blain Cowen and have pointed out to him
exactly how to have Cobclen work properly.

Your problems are twofold
(1) Your source code has no file extension which Cobclen uses to determin
what sort of structure is being used (where the "A" area begins,

2)and more importantly,
There is no PROCEEDURE DIVISION statement in the code samples you
provided.

Upon fixing those two items I successfully cleaned sample code that
Blair provided.
Both of these two items are documented in the manual and the revision
document on the diskette.

I would reply directly, but since your email (and Blairs) have been
rejecting messages for 3 days I can only reply here.
```

#### ↳ Re: Indenting

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-02-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bbc0b58a8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<331597B5.3EF8@gssec.bt.co.uk>`
- **References:** `<331597B5.3EF8@gssec.bt.co.uk>`

```

In article <331··.@gss··o.uk>,
Steven Lang wrote:
› Hi
› 
…[5 more quoted lines elided]…
› Thanks


I have exactly what you want: a COBOL beautifier by the name CBL-BEAU.
You can check it out at

http://www.siber.com/sct/

The beautifier itself is free, in the hope that you buy
CobolTransformer ToolKit that will allow you infinitely
customize your beautification process --
you can program any indentation style
into our table-driven indentation algorithm.


Vadim Maslov


P.S. Announcement of the offering that includes CBL-BEAU is enclosed:


Siber Systems Inc. is pleased to announce CobolTransformer reengineering
toolkit. It includes the following:

- High quality Cobol Parser capable of parsing the following Cobol
dialects: ANSI-74, ANSI-85, OSVS, VS II, SAA, X/Open, Microsoft,
Microfocus, Ryan McFarland, DOSVS, UNIVAC.

- Internal Representation for Cobol programs (expression trees) and
C++ library to manipulate this representation that includes.

- PrettyPrint library (also in C++) that transforms our internal
representation back into beautifully indented COBOL program with fully
preserved comments. What's most important, pretty-printing is totally
customizable, that is, you can directly encode your COBOL formatting
rules into our table-driven pretty-printer.


So we offer a complete and well-designed Cobol compiler toolkit
written in C++ that lets you focus on particulars of your Cobol
reengineering project (including but not limited to Year 2000
projects) and not worry about handling complexity of quality Cobol
lexing, parsing, and generation.

To learn more about CobolTransformer, please check out
our Web site at http://www.siber.com/sct/


A free demo/evaluation program cbl-beau is available for
immediate download from http://www.siber.com/sct/.

cbl-beau beautifies (pretty prints) your Cobol program.

The primary goal of cbl-beau is to demonstrate speed and versatility
of our parser and code generator.


For pricing and other questions please e-mail to: in··.@si··r.com.


Vadim Maslov
Siber Systems
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
