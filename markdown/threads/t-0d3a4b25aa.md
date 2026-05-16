[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Paged List box

_2 messages · 2 participants · 1998-12_

---

### Paged List box

- **From:** "Robert Annandale" <rob_a@unipharm.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<747ijo$jel$1@fountain.mindlink.net>`

```
In AcuCOBOL 4.0 GT under WinNT , is it possible, when programming paged list
boxes, to give them headings for each column.

Example.

heading 1  heading2     heading 3 ... ...
__________________________________________________________
column 1 | Column 2 |     column 3   | ... ...

I thought it was, but I just can't seem to recreate it...

Rob Annandale
```

#### ↳ Re: Paged List box

- **From:** cadams@acucorp.com (Chris Adams)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366823d0.342336894@news.acucorp.com>`
- **References:** `<747ijo$jel$1@fountain.mindlink.net>`

```
On Thu, 3 Dec 1998 18:48:12 -0000, "Robert Annandale" <rob_a@unipharm.com>
wrote:

>In AcuCOBOL 4.0 GT under WinNT , is it possible, when programming paged list
>boxes, to give them headings for each column.

Not with a paged list-box; the demonstration program uses labels above the
listbox to achieve this effect.

I would recommend that you take a look at the grid control if you need this sort
of functionality. It provides considerably more flexibility than the simpler
paged list-box.

# Chris Adams <cadams@acucorp.com>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
