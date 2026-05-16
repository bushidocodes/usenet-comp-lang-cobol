[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# other problem

_2 messages · 2 participants · 2000-04_

---

### Re: other problem

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-22T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8dtcrc$hbt$1@slb6.atl.mindspring.net>`
- **References:** `<39022443.EB66F92@free.fr>`

```
First, you may find that asking your questions in comp.lang.cobol instead of
alt.cobol will get more responses.  That is the "preferred" newsgroup for
COBOL questions.

Concatenation expressions (with "&") is currently an extension to Standard
COBOL - but will be part of the next Standard (due out sometime later this
decade - hopefully in just a few years).  HOWEVER, for those implementations
that do support it (and in the draft Standard) you are correct that you may
only concatenate two literals - not a literal and a data item.

To do what you want, there are a few ways to do it.

1) Use reference modification:
    Move truc to bidule
    Move "machin" to bidule (function Length (truc) + 1:)
       (this last statement figures out how long "truc" is and then moves the
literal after it in the receiving item.

2) Use the STRING statement
   String truc delimited by size
              "machin" delimited by size
        into bidule
```

#### ↳ Re: other problem

- **From:** Chow <chow@free.fr>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3902A99F.6C53BDDB@free.fr>`
- **References:** `<39022443.EB66F92@free.fr> <8dtcrc$hbt$1@slb6.atl.mindspring.net>`

```
sorry
I was looking for a french newsgroup about Cobol, but seems that it doesn't
interesting anyone here so I pick up the first one on my list :)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
