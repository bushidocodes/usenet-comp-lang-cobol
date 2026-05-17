[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help needed on MOVES

_3 messages · 2 participants · 1998-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help needed on MOVES

- **From:** "sbou..." <ua-author-6191657@usenetarchives.gap>
- **Date:** 1998-03-02T05:32:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6de1ri$1pr$1@nnrp1.dejanews.com>`

```

I am a little confused how data is represented in memory when it comes to
using the move statement. For example:

01 FLDA PIC S999.
Move 675 to FLDA

Would this data be in memory as zoned decimal? F6F7C5

What about moving groups. Do I understand correctly groups are moved as
Pic(x).

Thanks
Scott

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Help needed on MOVES

- **From:** "huib cobol frog klink" <ua-author-17074505@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0efe4c784b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6de1ri$1pr$1@nnrp1.dejanews.com>`
- **References:** `<6de1ri$1pr$1@nnrp1.dejanews.com>`

```

sbo··.@m··.com wrote:

› I am a little confused how data is represented in memory when it comes to
› using the move statement.  For example:
…[7 more quoted lines elided]…
›  Pic(x).

Scott,

Right, in MOVE A TO B, if a, b, or both are a group, the entire move is a
pic X move without editing, even if b is an alphanumeric-edited field.

675 is indeed represented in memory as f6f7c5 (assuming IBM type hardware
under ebcdic (rumours about an ascii mainframe mady by big blue elsewhere in
this group!)). The literal itself is stored in the literal pool. This pool
can be seen as a big collection of all numeric and aphanumeric literals used
throughout the program. The pool has a certain structure, but thats
compiler-dependent. Some people have the habit to write
move constfield to flda
with
01 constfield pic s999 value 675.
in working storage, but beside other effects, the storage requirements and
resulting machine instructions are the same is when using 675 directly in the
move statement.

Does this answer your question?

Huib
```

##### ↳ ↳ Re: Help needed on MOVES

- **From:** "sbou..." <ua-author-6191657@usenetarchives.gap>
- **Date:** 1998-03-02T13:25:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0efe4c784b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0efe4c784b-p2@usenetarchives.gap>`
- **References:** `<6de1ri$1pr$1@nnrp1.dejanews.com> <gap-0efe4c784b-p2@usenetarchives.gap>`

```

In article <34F··.@i··.nl>, H.K··.@i··.nl wrote: > >
sbo··.@m··.com wrote: > > > I am a little confused how data is represented
in memory when it comes to > > using the move statement. For example: > > >
› 01 FLDA PIC S999. > > Move 675 to FLDA > > > > Would this data be in
memory as zoned decimal? F6F7C5 > > > > What about moving groups. Do I
understand correctly groups are moved as > > Pic(x). > > Scott, > > Right,
in MOVE A TO B, if a, b, or both are a group, the entire move is a > pic X
move without editing, even if b is an alphanumeric-edited field. > > 675 is
indeed represented in memory as f6f7c5 (assuming IBM type hardware > under
ebcdic (rumours about an ascii mainframe mady by big blue elsewhere in > this
group!)). The literal itself is stored in the literal pool. This pool > can
be seen as a big collection of all numeric and aphanumeric literals used >
throughout the program. The pool has a certain structure, but thats >
compiler-dependent. Some people have the habit to write > move constfield to
flda > with > 01 constfield pic s999 value 675. > in working storage, but
beside other effects, the storage requirements and > resulting machine
instructions are the same is when using 675 directly in the > move statement.
› > Does this answer your question? > > Huib > Your response is more than
adequate. Just to keep my head clear, unless the field is defined as COMP-3
or COMP , then memory has the value as display data. Correct? Below is an
example as to how I believe memory should display a value in three formats:
FLDA PIC S999 Move 100 to FLDA ANSWER F1F0C0 FLDA PIC S999 COMP-3 Move
100 to FLDA ANSWER 100C FLDA PIC S999 COMP ANSWER 0064 Move 100 FLDA
Thanks Scott

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
