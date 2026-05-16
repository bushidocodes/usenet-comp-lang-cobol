[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# data efficiency

_3 messages · 3 participants · 2002-10_

---

### data efficiency

- **From:** mel5133928@aol.com (MEl5133928)
- **Date:** 2002-10-02T21:56:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021002175640.14318.00006139@mb-bj.aol.com>`

```
I was wondering whether it is more efficient when comparing numeric items to
ensure they are of the same category e.g zoned v zoned or packed-decimal v
packed-decima?. Similarly, are matching sizes and the joint presence or absence
of signs useful?

Second, when having a record layout as such:

01 WS-YEAR.
    03  WS-CCYY    PIC 9(4).
    03  WS-MM       PIC 9(2).
    03  WS-DD        PIC 9(2).

....if I was to move a PIC 9(8) field containing a value e.g 20021002 to
WS-YEAR, would the fact that WS-YEAR is alphanumeric mean that more efficient
assembler would result if redefining this area as PIC 9(8) and moving here
instead. (I know this would be necessary if the sending field was packed or
binary to ensure conversion to display format.) 

Splitting hairs I'm sure!
```

#### ↳ Re: data efficiency

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-10-02T17:42:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<anfsok$vdg$1@slb3.atl.mindspring.net>`
- **References:** `<20021002175640.14318.00006139@mb-bj.aol.com>`

```
This is a definite "it depends".  The first question is what compiler and
operating system?

If your compiler has a "show the created assembler/object-code" option" -
use that on the specific comparisons and see what code is generated.  OFTEN
(not always) the more instructions, the less efficient.  (OTOH, there are -
on some OS's - some single instructions that are more expensive than
combinations of other instructions).   Also, do NOT assume that any tests
that you do with one set of picture clauses/usages will be the same when you
change to bigger/smaller sizes.

BOTTOM-LINE:
  Unless this comparison is in a "tight loop" in a HIGHLY speed-dependent
environment, this probably will not make a "big" difference in your total
application performance.  This isn't to say that learning "good techniques"
won't help you in the long run.  I can't think of any environments where
comparing "like" fields isn't AS good or better than comparing unlike items.
However, "getting" the fields to be the same MAY cost more than what you
would gain in total performance improvements.
```

#### ↳ Re: data efficiency

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-10-03T12:50:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<22Xm9.36907$bY5.224827@bin4.nnrp.aus1.giganews.com>`
- **References:** `<20021002175640.14318.00006139@mb-bj.aol.com>`

```

"MEl5133928" <mel5133928@aol.com> wrote in message
news:20021002175640.14318.00006139@mb-bj.aol.com...
> I was wondering whether it is more efficient when comparing numeric items
to
> ensure they are of the same category e.g zoned v zoned or packed-decimal v
> packed-decima?. Similarly, are matching sizes and the joint presence or
absence
> of signs useful?
>
…[8 more quoted lines elided]…
> WS-YEAR, would the fact that WS-YEAR is alphanumeric mean that more
efficient
> assembler would result if redefining this area as PIC 9(8) and moving here
> instead. (I know this would be necessary if the sending field was packed
or
> binary to ensure conversion to display format.)
>
> Splitting hairs I'm sure!

How hard is it for you to try this on your compiler and your system. Put the
possibilities in a 100-million iteration loop and time them.

You will find, I'll wager, less than two seconds difference in 100,000,000
comparisons. Now you have to ask whether this difference, a picosecond or
so, is worth the effort in program design.

In virtually every case we've seen, coding (or re-coding) for
micro-efficiency costs far more than it's worth.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
