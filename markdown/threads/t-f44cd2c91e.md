[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Same Server different Micro Focus Versions

_2 messages · 2 participants · 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Same Server different Micro Focus Versions

- **From:** "scott warren" <ua-author-939265@usenetarchives.gap>
- **Date:** 1997-01-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32E049F8.4BE7@internetmci.com>`

```

I have to modify a Novell server that will have two different versions
of Micro Focus Cobol in use.
One will be using OSX and the run time system. The other will be using
a linked file (.exe) method.

They keep finding the others coblib.dle. Or can't find XM or the run
time system files.

There are some set statements in Micro Focus to locate XM and RUN. What
is the best way to handle this.
```

#### ↳ Re: Same Server different Micro Focus Versions

- **From:** "ken floyd" <ua-author-2409564@usenetarchives.gap>
- **Date:** 1997-01-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f44cd2c91e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32E049F8.4BE7@internetmci.com>`
- **References:** `<32E049F8.4BE7@internetmci.com>`

```

Let's say that two versions were installed, one under sys:\version1, the
other under sys:\version2. So under each version you'll have the
COBOL\EXEDLL and COBOL\LBR subdirectories.

If USER1 wants to use version1, he'll have to run a couple of set
statements:

SET PATH=%PATH%;\VERSION1\COBOL\EXEDLL;\VERSION2\COBOL\LBR
SET COBDIR=\VERSION1\COBOL\EXEDLL;\VERSION2\COBOL\LBR

If user2 want to use version2, he'll have the same type of sets, but using
the other directory structure.

Scott Warren wrote in article
<32E··.@int··i.com>...
› I have to modify a Novell server that will have two different versions
› of Micro Focus Cobol in use.  
…[9 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
