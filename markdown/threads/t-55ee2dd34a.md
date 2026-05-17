[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CURSOR POSITION IN MF COBOL

_3 messages · 3 participants · 1996-03_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### CURSOR POSITION IN MF COBOL

- **From:** "yoly ceron" <ua-author-17086581@usenetarchives.gap>
- **Date:** 1996-03-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<314E48C1.64AD@codetel.net.do>`

```
Can someone help he, and tell me how can I get the cursor
position in MF-COBOL?

Please Reply!!!!

Yoly Ceron
l.c··.@cod··t.do
```

#### ↳ Re: CURSOR POSITION IN MF COBOL

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-03-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-55ee2dd34a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<314E48C1.64AD@codetel.net.do>`
- **References:** `<314E48C1.64AD@codetel.net.do>`

```
In article <314··.@cod··t.do>, l.c··.@cod··t.do says...
›
› Can someone help he, and tell me how can I get the cursor
› position in MF-COBOL?

You don't say which version or if you are using a character interface or a GUI
interface but....

There is an RTS call...

call "CBL_GET_CSR_POS" using screen-position

screen-position is a group item eg.

01 screen-position.
03 row-number pic x comp-x.
03 column-number pic x comp-x.

top left screen positon is row 0, coulumn 0. If the cursor is invisible, 255
is returned.

There are also calls for setting the cursor position and dealing with the
mouse position also.

(it's in the manual btw)

Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

#### ↳ Re: CURSOR POSITION IN MF COBOL

- **From:** "george lewycky" <ua-author-12797862@usenetarchives.gap>
- **Date:** 1996-03-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-55ee2dd34a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<314E48C1.64AD@codetel.net.do>`
- **References:** `<314E48C1.64AD@codetel.net.do>`

```

rr = row
cc = column


DISPLAY ' xxxxxxxx ' at rrcc

accept field at rrcc

its easy.......


=========================================================

George R Lewycky "I'd rather be on Titan !!"
[ look at my home page to find out why ]

Windows 95 = Macintosh 1989 with dual air bags

Microsoft is a "follower" not a leader !!!!!!!!!

try me: http://soho.ios.com/~lewycky/
lew··.@soh··s.com
=========================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
