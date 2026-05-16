[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Code to print page numbers___another student's question

_2 messages · 2 participants · 1999-11_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### RE: Code to print page numbers___another student's question

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E47B36D9946CD311995000A0C9EA3E925F64ED@voyager.okc.disa.mil>`

```
How astute, yes, you are making sense...

No matter that you will ALWAYS know that you are only incrementing by one
and the increment in question will it will NEVER pass the limit without
equaling the limit and you will test for the condition EVERY time....

....testing for "less than or equal to" or "not less than" is just a small
insurance policy against the existence of Murphy's Law.....

-----Original Message-----
From: Pat [mailto:patp@cpinternet.com]

snip

PRINT-ENTRY.
    IF (LINE-COUNT NOT < MAX-LINES)
        PERFORM PAGE-HEADING
    END-IF.

The question I've had since last year - in my first few courses - is this:
do I need to say 'not less than' or can I say 'equal to' or 'less than or
equal to'????  Or could double spacing maybe mess us the 'equal to'?

Hope I'm making sense,
Thanks,
Pat

snip


 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

#### ↳ Re: Code to print page numbers___another student's question

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38219928.50611609@NOSPAMhome.com>`
- **References:** `<E47B36D9946CD311995000A0C9EA3E925F64ED@voyager.okc.disa.mil>`

```
> PRINT-ENTRY.
>     IF (LINE-COUNT NOT < MAX-LINES)
…[9 more quoted lines elided]…
> Pat

Let's say somewhere down the line someone decides to add a detail
paragraph.  Maybe the detail line gets expanded to two because they
wanted to add a field which just won't fit on the original detail line. 
And since these two lines always have to be together, they don't want to
go to top of page between the two lines.

Or the users just want double spacing...

The change is:
 PRINT-ENTRY.
     IF (LINE-COUNT NOT < MAX-LINES)
         PERFORM PAGE-HEADING
     END-IF.
     PRINT DETAIL-LINE-1   AFTER ADVANCING 2
     PRINT DETAIL-LINE-2   AFTER ADVANCING 1.
     ADD 3     TO LINE-COUNT.

Or worse, DETAIL-LINE-2 only gets printed sometimes.  Maybe your test
works quite nicely because it gets printed an even number of times.  But
in production, you get headings for the first 12 pages, and then
everything else is printed without a heading.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
