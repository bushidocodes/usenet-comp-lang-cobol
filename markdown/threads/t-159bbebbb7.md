[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with linking on Fujitsu Cobol V3

_2 messages · 2 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help with linking on Fujitsu Cobol V3

- **From:** "Luke Medland" <luke.medland@virgin.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6utjog$iv7$1@nclient5-gui.server.virgin.net>`

```
Please help me, I am studying computers at college and can not seem to link
a .obj file into an .exe.
It comes up with "No entry point defined"!!
How do I fix this?


Regards

Luke Medland
```

#### ↳ Re: Help with linking on Fujitsu Cobol V3

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-YVSIivvHvU5S@Dwight_Miller.iix.com>`
- **References:** `<6utjog$iv7$1@nclient5-gui.server.virgin.net>`

```
On Wed, 30 Sep 1998 15:31:47, "Luke Medland" <luke.medland@virgin.net>
wrote:

> Please help me, I am studying computers at college and can not seem to link
> a .obj file into an .exe.
…[6 more quoted lines elided]…
> Luke Medland

The comp.lang.cobol FAQ has the answer.  But the short answer is, you 
need to set a compile option - to MAIN, or even easier:

Insert one line of source code at the begining of the program.  Start 
in Column 8 - and it MUST be all uppercase:

@OPTIONS MAIN

Then it will compile and link.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
