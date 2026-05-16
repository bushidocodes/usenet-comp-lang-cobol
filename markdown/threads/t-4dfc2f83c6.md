[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can Cobol benefit from space....

_3 messages · 2 participants · 2004-10_

---

### Can Cobol benefit from space....

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-10-13T09:04:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0410130804.14a6551b@posting.google.com>`

```
Hello everyone,

I need your kind help again -  I am trying to print a name listing from
an indexed cobol file, However, I would like to utilize all the avaiable
space in the page regardless of the print orientation. So, the page detail
line area should have five columns, and after sorting the file the printed
out page should have this layout format:

aaaaaaaaaa	bbbbbbbbbb	cccccccccc	eeeeeeeeee	hhhhhhhhhh
aaaaaaaaaa	bbbbbbbbbb	cccccccccc	eeeeeeeeee	hhhhhhhhhh
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	eeeeeeeeee	hhhhhhhhhh
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	eeeeeeeeee	hhhhhhhhhh
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	ffffffffff	hhhhhhhhhh
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	ffffffffff	hhhhhhhhhh
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	ffffffffff	yyyyyyyyyy
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	ffffffffff	yyyyyyyyyy
aaaaaaaaaa	bbbbbbbbbb	dddddddddd	ffffffffff	yyyyyyyyyy
aaaaaaaaaa	cccccccccc	dddddddddd	ffffffffff	yyyyyyyyyy
bbbbbbbbbb	cccccccccc	dddddddddd	gggggggggg	yyyyyyyyyy
bbbbbbbbbb	cccccccccc	dddddddddd	gggggggggg	yyyyyyyyyy
bbbbbbbbbb	cccccccccc	dddddddddd	gggggggggg	yyyyyyyyyy
bbbbbbbbbb	cccccccccc	eeeeeeeeee	gggggggggg	zzzzzzzzzz
bbbbbbbbbb	cccccccccc	eeeeeeeeee	gggggggggg	zzzzzzzzzz
bbbbbbbbbb	cccccccccc	eeeeeeeeee	gggggggggg	zzzzzzzzzz
bbbbbbbbbb	cccccccccc	eeeeeeeeee	gggggggggg	zzzzzzzzzz
bbbbbbbbbb	cccccccccc	eeeeeeeeee	gggggggggg	zzzzzzzzzz

I am using micro focus Net Express 3.1 with windows 2000 professional. 
thank you so much. Kellie.
```

#### ↳ Re: Can Cobol benefit from space....

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-10-13T16:25:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EFcbd.12896$bZ3.1988@newssvr15.news.prodigy.com>`
- **References:** `<41758a6b.0410130804.14a6551b@posting.google.com>`

```
> Hello everyone,
>
> I need your kind help again -  I am trying to print a name listing from
> an indexed cobol file, However, I would like to utilize all the avaiable
> space in the page regardless of the print orientation. So, the page detail

So what's the question? How to use the space?

Try something like this..


01  PAGE-OUT.
    05  Column    occurs     5.                      << number of columns
          10   Row       PIC X (20) occurs 60    << number of  lines per
page

    MOVE 0 TO Row-sub    // because we increment first
    move 1  to column-sub  // because we don't
   move      space to page-out

    Get "data item" (one line of your label)

    PERFORM while we-still-have-data
         Add 1 to row-sub                       // advance to next row of
current column
         IF  row-Sub >rows-per-page       // oops, too far down the page
              ADD 1 TO column-Sub       // ok, so advance a column
              IF column-sub  >   columns-per-page   // oops, no more columns
left on this page
                 Print page-out, because it's full
                 move space to page-out
                 move 1 to column-sub    / and move to column one of new
page
              END-IF
              move 1 to row-sub         // and go to the first row of the
new column
        END-IF
        Move data-item  to PageOut (Column-sub, row-sub)    / because we are
now in the right place
        Get next data item
    END-PERFORM
    if page-out not equal space
      print out what's there, since we filled only part of a page.
```

##### ↳ ↳ Re: Can Cobol benefit from space....

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-10-13T18:43:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0410131743.5b9be490@posting.google.com>`
- **References:** `<41758a6b.0410130804.14a6551b@posting.google.com> <EFcbd.12896$bZ3.1988@newssvr15.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<EFcbd.12896$bZ3.1988@newssvr15.news.prodigy.com>...
>
> So what's the question? How to use the space?

> Kellie wrote:

> Hi,
> I am trying to figure out how to move my sorted data to the detail line
…[3 more quoted lines elided]…
> Kellie.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
