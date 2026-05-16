[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu PoweCobol: TreeView Control, problem...

_2 messages · 2 participants · 2001-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu PoweCobol: TreeView Control, problem...

- **From:** "fulvio" <fulvio.ruberti@microdatanet.it>
- **Date:** 2001-05-10T21:31:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9deqa1$bhq$1@pegasus.tiscalinet.it>`

```
I'm, trying to use the "TreeView Control" like a "men�" to call my programs.

+---Procedure
               |
               ----Program

How can i know the index values of the mouse's selected item (root and
child)?

Any help is appreciated, thanks in advance.

Fulvio
```

#### ↳ Re: Fujitsu PoweCobol: TreeView Control, problem...

- **From:** Jeff Campbell <jcampbell@ins-msi.com>
- **Date:** 2001-05-11T02:12:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AFB4440.19FFD989@ins-msi.com>`
- **References:** `<9deqa1$bhq$1@pegasus.tiscalinet.it>`

```
I have not yet tried to use the treeview control,
but I think the tree must be "walked" (scanned) to find the selected
node. Each node has a "path" property, and a "selected" property.

There is not an "index" property like the "listindex" of a listbox
control, or the "isselected(a)" flag array (also used by a listbox).

You will want to read the user's guide and the reference manuals.

HTH,

Jeff Campbell
n8wxs@arrl.net

fulvio wrote:
> 
> I'm, trying to use the "TreeView Control" like a "menù" to call my programs.
…[10 more quoted lines elided]…
> Fulvio
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
