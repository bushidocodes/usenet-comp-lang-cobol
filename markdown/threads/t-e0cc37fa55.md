[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Status 96 !?!

_7 messages · 6 participants · 1997-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### File Status 96 !?!

- **From:** "bibi..." <ua-author-17071849@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<334cf3ab.423141@news.ibm.net.il>`

```

Hi All, (URGENT)

I'm trying to open for input an index file access mode sequential and
the file ststus is not '00' but '96'.

the FD is correct and the SELECT decleration is correct.


What does 96 mean?, What is the problem and how can i fix it ?

Thanks and best regards

R a m i
```

#### ↳ Re: File Status 96 !?!

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0cc37fa55-p2@usenetarchives.gap>`
- **In-Reply-To:** `<334cf3ab.423141@news.ibm.net.il>`
- **References:** `<334cf3ab.423141@news.ibm.net.il>`

```

In message <<334··.@new··t.il>> bib··.@inf··l.com writes:
› 
› I'm trying to open for input an index file access mode sequential and
…[5 more quoted lines elided]…
› What does 96 mean?, What is the problem and how can i fix it ?

'96' is '9'/036 - File already exists.

You need to specify SELECT OPTIONAL ... or use the OPTIONAL-FILE
directive when compiling.
```

#### ↳ Re: File Status 96 !?!

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0cc37fa55-p3@usenetarchives.gap>`
- **In-Reply-To:** `<334cf3ab.423141@news.ibm.net.il>`
- **References:** `<334cf3ab.423141@news.ibm.net.il>`

```

Bibi Rami (bib··.@inf··l.com) wrote:
: Hi All, (URGENT)
: I'm trying to open for input an index file access mode sequential and
: the file ststus is not '00' but '96'.
: the FD is correct and the SELECT decleration is correct.
: What does 96 mean?, What is the problem and how can i fix it ?
: Thanks and best regards
: R a m i
--------------------------

9 = Misc'l errors
6 = No DD statement
```

#### ↳ Re: File Status 96 !?!

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0cc37fa55-p4@usenetarchives.gap>`
- **In-Reply-To:** `<334cf3ab.423141@news.ibm.net.il>`
- **References:** `<334cf3ab.423141@news.ibm.net.il>`

```

Bibi Rami wrote:
› 
› Hi All, (URGENT)
…[10 more quoted lines elided]…
›   R a m i


The 9X file status series, like the '96' you're having problems with,
have vendor-implemented meanings. You need to tell us which Cobol
compiler you use.

Mike Dodas
```

##### ↳ ↳ Re: File Status 96 !?!

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-04-10T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0cc37fa55-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e0cc37fa55-p4@usenetarchives.gap>`
- **References:** `<334cf3ab.423141@news.ibm.net.il> <gap-e0cc37fa55-p4@usenetarchives.gap>`

```

Michael Dodas wrote:
› 
› Bibi Rami wrote:
…[18 more quoted lines elided]…
› Mike Dodas



Rami:

I tried to reply to your e-mail, but it was returned to my as
undeliverable. Could you please check it and let me know what the
correct e-mail address is.

Mike Dodas
```

#### ↳ Re: File Status 96 !?!

- **From:** "ads" <ua-author-17072050@usenetarchives.gap>
- **Date:** 1997-04-10T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0cc37fa55-p6@usenetarchives.gap>`
- **In-Reply-To:** `<334cf3ab.423141@news.ibm.net.il>`
- **References:** `<334cf3ab.423141@news.ibm.net.il>`

```

bib··.@inf··l.com (Bibi Rami) wrote:

› Hi All, (URGENT)
 
› I'm trying to open for input an index file access mode sequential and
› the file ststus is not '00' but '96'.
 
› the FD is correct and the SELECT decleration is correct.
 
 
› What does 96 mean?, What is the problem and how can i fix it ?

if the first byte of the status is 9 then the second byte is
"implementor dependant" -- that is, different compiler vendors may use
different numbers in the second byte when the first is 9.

In Micro Focus COBOL, when the 1st byte is 9 then the 2nd is the
run-time error number in binary (not ascii). If your COBOL is not
Micro Focus you will have to check the manual.

If your '6' is binary six then the Micro Focus error would be "attempt
to write to a file open for INPUT"

If your '6' is ascii (ie 36 binary hex) then the MF error would be
"File already exists".

Al
from field mangled to avoid spam
remove no.spam to email me
```

#### ↳ Re: File Status 96 !?!

- **From:** "0ve..." <ua-author-1712774@usenetarchives.gap>
- **Date:** 1997-04-10T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0cc37fa55-p7@usenetarchives.gap>`
- **In-Reply-To:** `<334cf3ab.423141@news.ibm.net.il>`
- **References:** `<334cf3ab.423141@news.ibm.net.il>`

```

bib··.@inf··l.com (Bibi Rami) wrote:

[file status]

› What does 96 mean?, What is the problem and how can i fix it ?

'9x' - implementor defined.

Hmm.. that's no help... try your manual?

Groetjes, JAVE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
