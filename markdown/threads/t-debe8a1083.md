[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DFSORT / Syncsort Question

_2 messages · 2 participants · 1998-01_

---

### DFSORT / Syncsort Question

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34B8FC1F.6C569AFB@cutthejunk.xmission.com>`

```

I am currently involved in a task of merging our data center with
another. Our center uses Syncsort, the other center uses IBM's DFSORT.
We use the capabilities of Syncsort's OUTFIL reporting options quite
heavily. I noticed that DFSORT introduced this feature in the current
release (Release 13). Has anyone experienced compatibility problems
going from Syncsort to DFSORT? I've never noticed any compatibility
problems from Syncsort, but I'm not sure how compatible IBM keeps DFSORT
features compatible to competing products like Syncsort.

Any info. will be greatly appreciated.

Mike Dodas

(Remove cutthejunk for e-mail replies)
```

#### ↳ Re: DFSORT / Syncsort Question

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-debe8a1083-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34B8FC1F.6C569AFB@cutthejunk.xmission.com>`
- **References:** `<34B8FC1F.6C569AFB@cutthejunk.xmission.com>`

```

Michael Dodas wrote:
› 
› I am currently involved in a task of merging our data center with
…[6 more quoted lines elided]…
› features compatible to competing products like Syncsort.

Ahh, yes... the delights of working with jobstreams left behind by a
REAL SyncSort jockey... y'know, I've seen entire inventory maintenance
systems which consisted of nothing more than complex invocations of
SyncSort... or so it seemed.

Anyhow, I cannot give you anything definite, one way or the other... but
at my present client site I took a gander into SYS1.SORTLIB where I saw
modules named IECR00, SORT, SYNCSORT and DFSORT... and when I read the
modules they were all the same, the latest version of SYNCSORT.

Pretty cute... rather than change the JCL to reflect a new program just
make multiple copies of and rename the new program... and hope there are
no discrepancies.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
