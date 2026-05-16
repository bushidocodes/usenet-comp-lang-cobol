[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# y2k help

_2 messages · 2 participants · 2000-04_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### y2k help

- **From:** "DHMHTRHS MAYRIDIS" <dmavrid@acci.gr>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c98me$p48$1@newssrv.otenet.gr>`

```
Hi  all,
I am  teaching myself  Cobol.
I am  using  MS Cobol ver  2.10  &  Win 98.
On statement :  < Accept  d-date  from  date  >  ( yymmdd )
If  yy  <  80  moves  99  to yy.
Any  assistance  would  be  appreciated.
Regards.
Jim.
dmavrid@acci.gr
```

#### ↳ Re: y2k help

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8car78$th5$1@slb1.atl.mindspring.net>`
- **References:** `<8c98me$p48$1@newssrv.otenet.gr>`

```
MS COBOL ver 2.10 is "quite ancient".

With that compiler the best way to handle Y2K is to do an
   IF yy-field < some-number
        move 20 to CC-field
   Else
        move 19 to CC-field
   .

If you were using a "more recent" compiler, then you could do an

    ACCEPT date-field from Date YYYYMMDD

and it would provide you with the century of the current date.  ("YYYYMMDD"
is a sort-of-keyword)  You can also do

   Accept day-field from Day YYYYDDD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
