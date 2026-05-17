[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol: SCO Unix .GNT = Windows NT .GNT = OS2 32bit .GNT ?

_3 messages · 3 participants · 1995-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol: SCO Unix .GNT = Windows NT .GNT = OS2 32bit .GNT ?

- **From:** "el..." <ua-author-17087548@usenetarchives.gap>
- **Date:** 1995-04-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3n18bu$51j@miwok.nbn.com>`

```
Can anyone comment ?
Regards, Elie.
```

#### ↳ Re: MF Cobol: SCO Unix .GNT = Windows NT .GNT = OS2 32bit .GNT ?

- **From:** "crookie" <ua-author-17071740@usenetarchives.gap>
- **Date:** 1995-04-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe8fed1634-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3n18bu$51j@miwok.nbn.com>`
- **References:** `<3n18bu$51j@miwok.nbn.com>`

```
› el··.@m··.com (Elie I. Mourad) wrote:
› Can anyone comment ?
› Regards, Elie.

at the 1993 Micro Focus Users conference i presented a demo
(which was a GUI version of reversi/othello). i asked anyone in
the audience to pick an Intel platform (SCO,NT or OS/2) on
which to compile the demo (i think SCO was chosen). i then took
the GNT to the other two platforms and executed them (no mods
whatsoever).

GNT code is a Micro Focus proprietary, dynamically-loadable,
optimized execution format. it's based on COFF and executes as
fast as OBJ code.

obviously the GNT code will only port to platforms running the
same processor instruction set.

by comparison, MF INT(termediate) code (and AcuCOBOL code) is
processor independent and is interpreted by a run-time system.
```

##### ↳ ↳ Re: MF Cobol: SCO Unix .GNT = Windows NT .GNT = OS2 32bit .GNT ?

- **From:** "d..." <ua-author-14212488@usenetarchives.gap>
- **Date:** 1995-04-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe8fed1634-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fe8fed1634-p2@usenetarchives.gap>`
- **References:** `<3n18bu$51j@miwok.nbn.com> <gap-fe8fed1634-p2@usenetarchives.gap>`

```
In article <3n2j36$a.··.@ice··o.uk>, Crookie wrote:
›› el··.@m··.com (Elie I. Mourad) wrote: 
›› Can anyone comment ? 
…[23 more quoted lines elided]…
› 

To make it very clear, there is no such thing as a Windows NT
.GNT file. WNT on a DEC Alpha cannot run a .GNT generated under
WNT on a Pentium, and vice-versa.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
