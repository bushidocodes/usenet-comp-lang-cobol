[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Embedded SQL Toolkit Problem

_2 messages · 2 participants · 1997-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### MicroFocus Embedded SQL Toolkit Problem

- **From:** "pet..." <ua-author-855223@usenetarchives.gap>
- **Date:** 1997-08-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5tjoe0$flp$1@pithy.mincom.oz.au>`

```

We have some applications compiled through to 'int' files using the
Micro Focus Embedded SQL Toolkit for Microsoft SQL Server on
Window NT 4.

The programs run fine when executed by the 'run.exe' command that
comes with MF Cobol 4. However when we try and link together our
own executable to run the program we get message that it can't
locate the program '_sqlprld' whenever the RTS encounters a 'int'
program that has been generated form source that included embedded
SQL statements.

Does anyone have any ideas where this entry point is located?

Thanks in advance for any information on this problem.

Regards,
Peter
___________________________________________________________________________
Peter Moy           ACSnet: pet··.@min··z.au
                    Phone: +61 7 364-9999     Fax: +61 7 394-2844
Mincom Pty Ltd      P.O. Box 72, Stones Corner, Queensland, Australia  4120
```

#### ↳ Re: MicroFocus Embedded SQL Toolkit Problem

- **From:** "*kna..." <ua-author-17071452@usenetarchives.gap>
- **Date:** 1997-08-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a956bca9b0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5tjoe0$flp$1@pithy.mincom.oz.au>`
- **References:** `<5tjoe0$flp$1@pithy.mincom.oz.au>`

```

Peter Moy wrote:

› We have some applications compiled through to 'int' files using the
› Micro Focus Embedded SQL Toolkit for Microsoft SQL Server on
…[22 more quoted lines elided]…
› 4120



This is something Micro Focus "Techies" should answer...

I was quite annoyed by this problem... and it is documented somewhere in
the MF docs... (poorly though).

You have to load UTILS.LBR before calling your Cobol progs that contain
embedded SQL..
One way is just to CALL "$COBDIRÂ¥UTILS.LBR" before calling yor
app.progs..

I cant see why you need to link/build your apps... It is just as good to
have one EXE/DLL that loads the
Cobol RTS and the above trick, and call .GNT from then on...
It is faster,.. less overhead (duplicate "in-linked" RTS) and is the
recommended method by MF.



Regards

Geir Knaplund
"Chief Nerd"
Provida ASA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
