[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rebuild indexes question

_2 messages · 1 participant · 2003-09_

---

### Rebuild indexes question

- **From:** Brian Lavender <brian@brie.com>
- **Date:** 2003-09-11T22:58:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hvn2mv8gesejgh4sgd1ettrki8g73qon0a@4ax.com>`

```
I just went through and rebuilt the indexes for my data files. I have
a series of files that have deleted records. Is there anything that I
am risking by doing a rebuild on a data file that has deleted records?

I am using AcuCobol-85. This is a binary app that I moving over to a
newer server. 

brian

$ vutil -rebuild AUDIT.DAT

Input = AUDIT.DAT, Output = VTMPa00827, 78 records
Rebuilding...
....10%....20%....30%....40%....50%....60%....70%....80%....90%....100%
78 records recovered, 124 deleted records skipped
Replace original file with new one?
```

#### ↳ Re: Rebuild indexes question

- **From:** Brian Lavender <brian@brie.com>
- **Date:** 2003-09-14T21:07:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1meamvcs91l65vngb1p368mkhlpbkh7kj6@4ax.com>`
- **References:** `<hvn2mv8gesejgh4sgd1ettrki8g73qon0a@4ax.com>`

```
On Thu, 11 Sep 2003 22:58:48 -0700, Brian Lavender <brian@brie.com>
wrote:

>I just went through and rebuilt the indexes for my data files. I have
>a series of files that have deleted records. Is there anything that I
…[13 more quoted lines elided]…
>Replace original file with new one?

Apparently it can. I rebuilt the indexes on all the data files, and I
experienced some problems.

brian
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
