[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM and "Next Sentence" extension

_7 messages · 5 participants · 2003-03 → 2003-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### IBM and "Next Sentence" extension

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-31T20:05:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6as5f$nv0$1@slb6.atl.mindspring.net>`

```
I was sent a private email indicating that you-know-what (oops - I mean
you-know-whom <G>) has claimed that IBM had an extension allowing NEXT
SENTENCE in source code other than IF and SEARCH.

I believe that they did allow it in their (long "dropped" ON statement), but
they certainly did NOT allow it either as a "phrase" in general conditional
statements, e.g.

   READ ABC
       AT END
              NEXT SENTENCE

nor did they allow it (as Micro Focus does - and documents - as an
extension) as a "general" imperative statement.

One *could* argue that when the IBM "PC" COBOL compiler (COBOL/2) was
actually a "re-badged" Micro Focus compiler, that this meant that "IBM
supported it" - but no "built-by-IBM" compiler has EVER allowed "NEXT
SENTENCE" to be used with many (non-Standard) statements.

Anyone claiming that this was a "general" IBM extension, should post a
"clean compile" listing from such an IBM compiler.
```

#### ↳ Re: IBM and "Next Sentence" extension

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-01T04:21:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e890f0d.111630208@news.optonline.net>`
- **References:** `<b6as5f$nv0$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>I was sent a private email indicating that you-know-what (oops - I mean
>you-know-whom <G>) has claimed that IBM had an extension allowing NEXT
…[19 more quoted lines elided]…
>"clean compile" listing from such an IBM compiler.

There is no way to provide corrigible evidence because the '74 compliant
compilers are long extinct. 

I tried it with the oldest compiler I have: Realia 3.1 dated 1987. It chokes on
divide a into b on size error next sentence. It says next sentence should be
under IF, which confirms your point.
```

##### ↳ ↳ Re: IBM and "Next Sentence" extension

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-01T13:00:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304011300.18b1a22b@posting.google.com>`
- **References:** `<b6as5f$nv0$1@slb6.atl.mindspring.net> <3e890f0d.111630208@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >you-know-whom <G>) has claimed that IBM had an extension allowing NEXT
> >SENTENCE in source code other than IF and SEARCH.

> >nor did they allow it (as Micro Focus does - and documents - as an
> >extension) as a "general" imperative statement.
 
> There is no way to provide corrigible evidence because the '74 compliant
> compilers are long extinct. 

So, is it your stance that you will consider that your are 'correct'
until someone fires one up and demonstrates that it _won't_ take a
NEXT SENTENCE ?
```

###### ↳ ↳ ↳ Re: IBM and "Next Sentence" extension

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-02T01:23:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8a2bb1.58733416@news.optonline.net>`
- **References:** `<b6as5f$nv0$1@slb6.atl.mindspring.net> <3e890f0d.111630208@news.optonline.net> <217e491a.0304011300.18b1a22b@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[11 more quoted lines elided]…
>NEXT SENTENCE ?

I did fire up a 'pre-85' Realia compiler and fed it 'divide a into b on size
error next sentence'. It barfed, saying next sentence could only be used in an
IF.  Are you happy?
```

##### ↳ ↳ Re: IBM and "Next Sentence" extension

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-01T14:54:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6d5as$1ud4$1@si05.rsvl.unisys.com>`
- **References:** `<b6as5f$nv0$1@slb6.atl.mindspring.net> <3e890f0d.111630208@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e890f0d.111630208@news.optonline.net...

> There is no way to provide corrigible evidence because the '74 compliant
> compilers are long extinct.

Maybe on IBM systems, but not everywhere.  Unisys MCP/AS COBOL74 is alive
and well and has a very devoted following.  In that implementation there are
a few cases in which NEXT SENTENCE is allowed beyond those provided for in
the standard, but they are clearly documented as extensions to the standard.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: IBM and "Next Sentence" extension

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-01T17:30:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6d7f2$7kk$1@slb3.atl.mindspring.net>`
- **References:** `<b6as5f$nv0$1@slb6.atl.mindspring.net> <3e890f0d.111630208@news.optonline.net> <b6d5as$1ud4$1@si05.rsvl.unisys.com>`

```
Chuck,
  This thread was simply limited to the (incorrect) claim that IBM allowed
NEXT SENTENCE in "non-Standard" situations.

FYI,
  Many sites do still have/use IBM's OS/VS COBOL (their '74 Standard
compiler).  If someone thinks that OS/VS COBOL *did* have such extensions,
they could post some code and I'll bet it could be tested with their
compiler.
```

#### ↳ Re: IBM and "Next Sentence" extension

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-02T15:13:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6eumv$iqs$1@peabody.colorado.edu>`
- **References:** `<b6as5f$nv0$1@slb6.atl.mindspring.net>`

```

On 31-Mar-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> I believe that they did allow it in their (long "dropped" ON statement), but
> they certainly did NOT allow it either as a "phrase" in general conditional
…[4 more quoted lines elided]…
>               NEXT SENTENCE

I just pulled out an old compiler and tried this - getting a compiler error.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
