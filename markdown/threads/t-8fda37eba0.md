[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cics and alternate index with duplicate keys

_5 messages · 5 participants · 1997-09 → 1997-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cics and alternate index with duplicate keys

- **From:** "stephanie bonds" <ua-author-17073777@usenetarchives.gap>
- **Date:** 1997-09-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3432602C.76F0@usps.gov>`

```

I am trying to perform a previous browse on a VSAM file using an
alternate index that have duplicate keys. I'm also specifying EQUAL on
the STARTBR command. For some reason, it always starts at the first
record of key that's equal rather than at the point that I am at in the
file currently. Can someone please tell me how to perform this browse
correctly?

Thanks
```

#### ↳ Re: Cics and alternate index with duplicate keys

- **From:** "geng..." <ua-author-17072996@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8fda37eba0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3432602C.76F0@usps.gov>`
- **References:** `<3432602C.76F0@usps.gov>`

```

In article <343··.@us··s.gov>, Stephanie Bonds wrote:
› I am trying to perform a previous browse on a VSAM file using an
› alternate index that have duplicate keys. I'm also specifying EQUAL on
…[5 more quoted lines elided]…
› Thanks

STARTBR..EQ will always start at the key that is equal to.
Use GE.
for a prev browse do a
STARTBR GE
READNEXT
READPREV
READPREV

This is not a mistype. A readnext should always follow a startbr.
```

##### ↳ ↳ Re: Cics and alternate index with duplicate keys

- **From:** "yled..." <ua-author-6588948@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8fda37eba0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8fda37eba0-p2@usenetarchives.gap>`
- **References:** `<3432602C.76F0@usps.gov> <gap-8fda37eba0-p2@usenetarchives.gap>`

```

Grant Engelbrecht wrote:
› 
› In article <343··.@us··s.gov>, Stephanie Bonds  wrote:
…[17 more quoted lines elided]…
› This is not a mistype. A readnext should always follow a startbr.

You are wrong: A readnext is not mandatory. To backward browse, you have

1) STARTBR
2) READPREV: will read the record you pointed to with STARTBR (exactly
as READNEXT would do
3) READPREV's... to continue, and, finally
4) ENDBR

With the sequence you mention, supposing STARTBR points to record 200
- READNEXT will read record 200
- READPREV will invert the reading process and return record 200 another
time
- the 2nd READPREV will give you the previous record (say 199)
and so on

HTH

Yves
```

#### ↳ Re: Cics and alternate index with duplicate keys

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-10-04T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8fda37eba0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3432602C.76F0@usps.gov>`
- **References:** `<3432602C.76F0@usps.gov>`

```

On Wed, 01 Oct 1997 10:37:32 -0400, Stephanie Bonds
wrote:

› I am trying to perform a previous browse on a VSAM file using an
› alternate index that have duplicate keys. I'm also specifying EQUAL on
…[5 more quoted lines elided]…
› Thanks

stephanie,
i've read a few followup posts on the technical aspects. i 'think'
your basic question was "WHY does it go back and start over?" If i'm
interpreting your post correctly, the reason is that it appears from
your wording that you are accessing the same file with two different
keys concurrently. CICS allows that to be treated as two different
file so a STARTBR with a different key does not relate to the current
position in the file. am i close to your question? good luck.
david

David d.s··.@ix.··m.com
____________________________________
```

#### ↳ Re: Cics and alternate index with duplicate keys

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8fda37eba0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3432602C.76F0@usps.gov>`
- **References:** `<3432602C.76F0@usps.gov>`

```



Stephanie Bonds wrote in article
<343··.@us··s.gov>...
› I am trying to perform a previous browse on a VSAM file using an
› alternate index that have duplicate keys. I'm also specifying EQUAL on
…[4 more quoted lines elided]…
› 

Your problem is with Pseudoconversational programming. All file position
holding is lost when a return to the screen (CICS RETURN) is executed.
There are a couple of ways to handle the browse when using the duplicate
alternate keys. One way is to retain the prime key, so that the next time
the browse is done, you can check the prime key to see if it is the same
record you had before, and if so, read another record. Ideally you don't
want to have duplicated keyed records when this type of processing is
required. I usually append the uinque prime key to the allowing duplicates
alternate key when this sort of thing needs to be done.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
