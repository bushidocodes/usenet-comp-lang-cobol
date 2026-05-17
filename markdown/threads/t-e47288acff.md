[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SMS

_3 messages · 3 participants · 1996-04_

---

### SMS

- **From:** "ainco..." <ua-author-17086364@usenetarchives.gap>
- **Date:** 1996-04-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4m3mmu$1io@newsbf02.news.aol.com>`

```

Is anyone familiar with IBMs SMS product. I have a need to backup SMS
managed datasets to tape and than rename the file when restoring. I need
to do this for flat files and VSAM Files.
```

#### ↳ Re: SMS

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e47288acff-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4m3mmu$1io@newsbf02.news.aol.com>`
- **References:** `<4m3mmu$1io@newsbf02.news.aol.com>`

```

AIncorvaia wrote:
›
› Is anyone familiar with IBMs SMS product. I have a need to backup SMS
› managed datasets to tape and than rename the file when restoring. I need
› to do this for flat files and VSAM Files.Why use SMS to do this, If you want to copy over the file an IDCAMS
repro for VSAM, an Iebgener for flat and an iebcopy for PDS will do you
just fine. SMS is used for space management and HSM for archiving. If
you have a backup of a PDS to recover but you dont want to lose your
most recent changes ask your DASD support people to recall it to another
name. The control cards are well documented but I would not reccomend a
novice to try it without onsite help.
```

#### ↳ Re: SMS

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-04-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e47288acff-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4m3mmu$1io@newsbf02.news.aol.com>`
- **References:** `<4m3mmu$1io@newsbf02.news.aol.com>`

```

SMS is not a single product, but a whole suite of products which mostly
work together. Some components can be omitted or replaced by 3rd party
stuff.

Good news - nothing really special about SMS datasets. You can use normal
20 year old tools and techniques to deal with these datasets. IEBGENER
(or better equivalents) can copy SMS managed flat files to SMS or non-SMS
managed devices and media. I.e. copy sequential file to a tape. IDCAMS
can copy SMS managed files to a flat file.

Bottom line, no special techniques are required. Yes special techniques
inherent in the SMS architecture can be used - i.e. HSM backups,
incremental backups, etc, DSS stuff, etc, etc, etc.

KISS!

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
