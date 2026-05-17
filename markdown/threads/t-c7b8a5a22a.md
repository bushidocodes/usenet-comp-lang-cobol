[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol on AIX

_3 messages · 3 participants · 1997-06_

---

### Cobol on AIX

- **From:** "edgar" <ua-author-677339@usenetarchives.gap>
- **Date:** 1997-06-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3394E362.4248@ix.netcom.com>`

```

I need to port several systems written in Texas Instruments COBOL (circa
1980) to an IBM RS6000 running AIX version 4. I am looking for
advice/comments from anyone who has used a COBOL compiler/runtime
package and display manager on AIX. I understand several are available
- RM Cobol, Micro Focus, AcuCobol, IBM, etc. but I don't have personal
experience with any of them under AIX.

The systems are not that complicated but they do have a lot of multiply
indexed files and a good bit of user (non GUI) I/O. External sorts are
used so I need to be able to "CALL" system resources from within the
programs and occasionally pass parameters back and forth.

Any comments from experienced system designers/programmers are
appreciated.
```

#### ↳ Re: Cobol on AIX

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1997-06-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7b8a5a22a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3394E362.4248@ix.netcom.com>`
- **References:** `<3394E362.4248@ix.netcom.com>`

```

edgar wrote in article
<339··.@ix.··m.com>...
› I need to port several systems written in Texas Instruments COBOL (circa
› 1980) to an IBM RS6000 running AIX version 4.  I am looking for
…[3 more quoted lines elided]…
› experience with any of them under AIX.

I was the main COBOL person at TI. The TI compiler was produced by
Ryan-McFarland. [I later went to work for RM, and still work for Liant,
which bought the assets of RM.] There is no doubt that the RM/COBOL
product will be the most compatible.

› 
› The systems are not that complicated but they do have a lot of multiply
› indexed files and a good bit of user (non GUI) I/O.  External sorts are
› used so I need to be able to "CALL" system resources from within the
› programs and occasionally pass parameters back and forth.

The user I/O will match up well with the current RM/COBOL. You might
need to revert to the ANSI-74, "version 2" compiler compatibility switch.
External sorts are a different matter, however. Dependencies on the
TI DX10 operating system will need to be removed or modified. RM/COBOL
has a good internal sort (which DX10 COBOL did not have).

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

#### ↳ Re: Cobol on AIX

- **From:** "c..." <ua-author-6589031@usenetarchives.gap>
- **Date:** 1997-06-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7b8a5a22a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3394E362.4248@ix.netcom.com>`
- **References:** `<3394E362.4248@ix.netcom.com>`

```

In <339··.@ix.··m.com>, edgar writes:
› I need to port several systems written in Texas Instruments COBOL (circa
› 1980) to an IBM RS6000 running AIX version 4.  I am looking for
…[11 more quoted lines elided]…
› appreciated.

IBM has a Visual Age Cobol, that runs on OS/2 and AIX
Will do GUI and non-GUI. I am using the OS/2 version and like it a lot

-----------------------------------------------------------------------
Glenn Hoffman c.··.@atl··a.com voice: 770-795-0155
Team OS/2 fax: 770-795-0355
-----------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
