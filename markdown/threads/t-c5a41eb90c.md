[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Cobol Data Corruption Problem

_2 messages · 2 participants · 1999-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus Cobol Data Corruption Problem

- **From:** "Mirek" <mirekn@mksoftware.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z3b84.370$9O1.14583194@nnrp1.tor.metronet.ca>`

```
Hi,

I am trying to figure out a way to fix corrupted MicroFocus Cobol
data files. I have not found any tools or applications for doing such a
task. I was wondering if anyone knows of such utilities or possibly
a way to write such a tool in C/C++/VB. I am not a Cobol programmer thus I
am not familiar with the file format of the Cobol ISM files. Any
help would be greatly appreciated.

Mirek
```

#### ↳ Re: MicroFocus Cobol Data Corruption Problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83rnbf$156$1@nntp1.atl.mindspring.net>`
- **References:** `<z3b84.370$9O1.14583194@nnrp1.tor.metronet.ca>`

```
I think that all versions of Micro Focus (now MERANT) products include a
REBUILD function.  If you enter that command from a "dos prompt", I believe
it will give you some help.  One warning, be VERY careful that you don't use
the option that "rebuilds" a file from itself to itself - unless you already
have a backup of the file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
