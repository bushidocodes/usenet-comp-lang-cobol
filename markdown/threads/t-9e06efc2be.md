[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Was Date Standardizing or Patching

_2 messages · 2 participants · 1997-05_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Was Date Standardizing or Patching

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc5acf$2599d560$8a609fcf@corkery1>`

```

Hello All ...

I previously posted an example to this thread of a three byte "packed"
date field and (thanks to William Murray) an error was pointed out ... I
should be multiplying by 10 instead of 100 ... As he pointed out, this
could be construed as another reason this is not such a good idea or that
anything done in haste can at times come back to haunt you ... Anyway, the
corrected posting follows:
======================================================
01 DATE-WORK.
05 DATE-FULL PIC S9(7) COMP-3.
05 FILLER REDEFINES DATE-FULL.
07 DATE-MOVE PIC X(03).

COMPUTE DATE-FULL = * 10.
MOVE DATE-MOVE TO

I've seen code like this in an IBM mainframe COBOL environment used to pack
a six position date into three bytes ... The same could be done if you
cared to use a four position date ... Interesting enough, this stripping
technique does result in a field that can be interrogate via a SORT
include/omit and other utilities, i.e. the fields are in byte-to-byte
accordingly to CC, YY, MM, DD order ... A little clever programming can
make this field more useful than leaving the components float across byte
positions ... Anyway, I said I've seen it done ... I don't however
recommend its use.

Kevin Corkery
Independent Consultant
Voorhees, New Jersey
```

#### ↳ Re: Was Date Standardizing or Patching

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-05-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e06efc2be-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5acf$2599d560$8a609fcf@corkery1>`
- **References:** `<01bc5acf$2599d560$8a609fcf@corkery1>`

```

On 7 May 1997 10:16:13 GMT, "Kevin P Corkery"
wrote:

› Hello All ...
› 
…[28 more quoted lines elided]…
› Voorhees, New Jersey

I concur, Kevin. I don't recommend it either. Some inexperienced
programmer may need to change the code in a few months, won't know
what it's doing, and will botch it up. I really don't like making
cobol act like assembler. I would also question why anyone would want
to do this.

David d.s··.@ix.··m.com
____________________________________
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
