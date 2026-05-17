[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Cobol Workbench 4.0?

_5 messages · 5 participants · 1996-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus Cobol Workbench 4.0?

- **From:** "will..." <ua-author-472913@usenetarchives.gap>
- **Date:** 1996-05-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4nt29j$nnk@newsbf02.news.aol.com>`

```

I am working as a freelancer writing Cobol programs on IBM mainframe
computers.
Now I want to develop my programs at home, but I can't use a modem to
connect
to one of the company's mainframes because of security reasons. So I am
looking for a way to write and test cobol programs on a PC.

I have found the MicroFocus Homepage on the web and read their information
about the Cobol Workbench 4.0 (or 3.x) and think this is pretty much what
I would need.

Can anyone tell me, how similar the behavior of the workbench programs
will
be to that of the IBM VS Cobol II programs on a IBM3090? I will only need
batch and DB2 programs, no graphical windows and the like.

And can anyone tell me the approximate price for the Cobol Workbench,
because I can't find it anywhere on their web page.

Thanks.
Stefan
```

#### ↳ Re: MicroFocus Cobol Workbench 4.0?

- **From:** "saiful haque" <ua-author-17086393@usenetarchives.gap>
- **Date:** 1996-05-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3c644ffa3d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4nt29j$nnk@newsbf02.news.aol.com>`
- **References:** `<4nt29j$nnk@newsbf02.news.aol.com>`

```

wil··.@a··.com (Willfahrt) wrote:
› I am working as a freelancer writing Cobol programs on IBM mainframe
› computers.
…[18 more quoted lines elided]…
› Stefan

Codes are same for both environments.But you need to change the assign
clause in environment division. Otherwise it's pretty much same,or you can
the try the Microfocus for Mainframe environment.
thanks
saif
sa··.@jov··t.edu
```

##### ↳ ↳ Re: MicroFocus Cobol Workbench 4.0?

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-05-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3c644ffa3d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3c644ffa3d-p2@usenetarchives.gap>`
- **References:** `<4nt29j$nnk@newsbf02.news.aol.com> <gap-3c644ffa3d-p2@usenetarchives.gap>`

```

In article <4nvnd3$g.··.@pow··y.com>, sa··.@jcp··y.com says...
›
› [discussion of MF <> Mainframe compatibility]
 
› Codes are same for both environments.But you need to change the assign
› clause in environment division.

There's a facility called MFEXTMAP that gets around that problem allowing you
to map mainframe filenames onto PC ones. Comes with Workbench.


Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

##### ↳ ↳ Re: MicroFocus Cobol Workbench 4.0?

- **From:** "7473..." <ua-author-3314340@usenetarchives.gap>
- **Date:** 1996-05-28T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3c644ffa3d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3c644ffa3d-p2@usenetarchives.gap>`
- **References:** `<4nt29j$nnk@newsbf02.news.aol.com> <gap-3c644ffa3d-p2@usenetarchives.gap>`

```

In article <4nvnd3$g.··.@pow··y.co m>, From Saiful Haque
, the following was written:
› Codes are same for both environments.But you need to change the assign
› >
› clause in environment division.> .

No, you don't need to change it. Use the checker directive
"ASSIGN(EXTERNAL)" and use the MFEXTMAP.DAT file to connect DD names to
pc file names.
```

#### ↳ Re: MicroFocus Cobol Workbench 4.0?

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1996-05-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3c644ffa3d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4nt29j$nnk@newsbf02.news.aol.com>`
- **References:** `<4nt29j$nnk@newsbf02.news.aol.com>`

```

Willfahrt wrote:
› 
› I am working as a freelancer writing Cobol programs on IBM mainframe
…[19 more quoted lines elided]…
› Stefan

You will be quite happy with MF COBOL (using the mainframe compatiblity
option).
I have been working with that for a few years now, and can write and
test ALL my programs on the PC (running OS/2, MF COBOL 3.2/4.0,
MF CICS and DB2/2 v.1.2).
All I need to do is to do a file-transfer to TSO, recompile and link,
and the program work exactly as when unit-testing on the PC.

The prices in Norway is approx. 25.000 NOK (approx. 6.000 DM ???).

Regards
Geir
kna··.@s··.no
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
