[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MVS to VSE

_4 messages · 4 participants · 1996-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MVS to VSE

- **From:** "dennis griffith" <ua-author-17071857@usenetarchives.gap>
- **Date:** 1996-10-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`

```

Can anyone tell me right off hand if I can just ship an MVS CICS COBOL
II compiled module which uses VSAM files to a VSE system and have it
run?

Or do I have to recompile the source on VSE? How compatible are the
two systems or will I need to modify the source quite a bit?

Thanks for any info.
```

#### ↳ Re: MVS to VSE

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1996-10-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fff4eb2177-p2@usenetarchives.gap>`
- **In-Reply-To:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`
- **References:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`

```

Dennis Griffith wrote:

› Can anyone tell me right off hand if I can just ship an MVS CICS COBOL
› II	compiled module which uses VSAM files to a VSE system and have it
› run?	
 
› Or do I have to recompile the source on VSE?   How compatible are the
› two systems or will I need to modify the source quite a bit?

Can't tell ya for sure. I know the JCL for both of 'em are QUITE
different...The code? I don't know.
```

#### ↳ Re: MVS to VSE

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-10-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fff4eb2177-p3@usenetarchives.gap>`
- **In-Reply-To:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`
- **References:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`

```

Dennis Griffith wrote:

› Can anyone tell me right off hand if I can just ship an MVS CICS COBOL
› II	compiled module which uses VSAM files to a VSE system and have it
…[3 more quoted lines elided]…
› two systems or will I need to modify the source quite a bit?
 
› Thanks for any info.

Without actually checking it, I would guess that there is no guarantee
that the executable file formats are compatible between VSE and MVS.

So I would recommend recompiling the program. If the CICS program is
command-level you should not need to make any source changes (unless
you are migrating to an earlier release of CICS AND the program uses
an API call that was not supported in the prior release (an unlikely
situation).

I haven't done any macro-level CICS in five years, but I think it
will probably recompile without requiring any source changes.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: MVS to VSE

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-10-11T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fff4eb2177-p4@usenetarchives.gap>`
- **In-Reply-To:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`
- **References:** `<325D2A6B.5BDA@cfrmvs.cfr.usf.edu>`

```

Dennis Griffith wrote:

› Can anyone tell me right off hand if I can just ship an MVS CICS COBOL
› II	compiled module which uses VSAM files to a VSE system and have it
…[3 more quoted lines elided]…
› two systems or will I need to modify the source quite a bit?
 
› Thanks for any info.
the two systems are close but various service modules have different
name.

a prelinked module will not work. an relocatable module probably will
not work (if it does anything usefull)

jr

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
