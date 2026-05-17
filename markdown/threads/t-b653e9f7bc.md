[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable Record, Variable Block

_2 messages · 2 participants · 1998-08_

---

### Variable Record, Variable Block

- **From:** "shr..." <ua-author-17084348@usenetarchives.gap>
- **Date:** 1998-08-19T17:30:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6rfg5l$gr3$1@nnrp1.dejanews.com>`

```
Hi Cobol Guru's, We receive a file in MVS format (ebcdic) in variable length,
ie each record has a Record descriptor word and DOES NOT have a block
descriptor word.

We process the file and need to send the file (Using Connect Direct) in
variable length and Variable block format, ie to add block descriptor word.
We have Microfocus Cobol in HP Unix.

Any help is appreciated. If you have a ready made code, that would be great!

Thanks in advance

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: Variable Record, Variable Block

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b653e9f7bc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6rfg5l$gr3$1@nnrp1.dejanews.com>`
- **References:** `<6rfg5l$gr3$1@nnrp1.dejanews.com>`

```
Check if your version of the MF product supports the RDW compiler option
(which should allow you to use and even access a pseudo-record descriptor
word). I am not really familiar with the HP products so you might want to
ask your MF support team if the program VRECGEN (for converting MVS variable
length files) is available and appropriate for your environment. (I think
it is only available/used for PC's - but I could be wrong about that.)

shr··.@ya··o.com wrote in message <6rfg5l$gr3$1.··.@nnr··s.com>...
› Hi Cobol Guru's, We receive a file in MVS format (ebcdic) in variable
› length,
…[13 more quoted lines elided]…
› http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
