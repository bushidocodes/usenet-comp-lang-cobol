[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF-RM differences???

_6 messages · 6 participants · 1998-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### MF-RM differences???

- **From:** "uk leem" <ua-author-14809067@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jv60g$jlv$1@news.nuri.net>`

```

Is there any source which summarizes
differences between MF and RM?
Have a lot of RM sources but only a
MF compiler,that's why.
```

#### ↳ Re: MF-RM differences???

- **From:** "sands" <ua-author-6589287@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8539aafee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6jv60g$jlv$1@news.nuri.net>`
- **References:** `<6jv60g$jlv$1@news.nuri.net>`

```

On 20 May 1998 18:05:04 GMT, Uk Leem wrote:

› Is there any source which summarizes
› differences between MF and RM?
› Have a lot of RM sources but only a
› MF compiler,that's why.
› 

There is a Compatability Guide manual with MF Workbench that documents
the differences. There is also a utility supplied for converting files
from RM to MF format.

Hope this helps
David.
```

#### ↳ Re: MF-RM differences???

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8539aafee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6jv60g$jlv$1@news.nuri.net>`
- **References:** `<6jv60g$jlv$1@news.nuri.net>`

```

Uk Leem wrote:
› Is there any source which summarizes
› differences between MF and RM?
› Have a lot of RM sources but only a
› MF compiler,that's why.

If you're just having trouble compiling stuff, the first step is
to use the RM compiler directive. You may also need the
PERFORM-TYPE(RM) directive. Also, check the "Compatibility Guide"
for other RM->MF migration tips.

Cheers,
Kev.
```

#### ↳ Re: MF-RM differences???

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8539aafee-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6jv60g$jlv$1@news.nuri.net>`
- **References:** `<6jv60g$jlv$1@news.nuri.net>`

```

Fujitsu COBOL supports a majority of the RM/COBOL specific features and most
users find a port of RM/COBOL to Fujitsu COBOL a straight recompile. You
can get the FREE unrestricted Fujitsu COBOL Starter Set at www.adtools.com

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


Uk Leem wrote in message <6jv60g$jlv$1.··.@new··i.net>...
› Is there any source which summarizes
› differences between MF and RM?
› Have a lot of RM sources but only a
› MF compiler,that's why.
›
```

##### ↳ ↳ Re: MF-RM differences???

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8539aafee-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8539aafee-p4@usenetarchives.gap>`
- **References:** `<6jv60g$jlv$1@news.nuri.net> <gap-f8539aafee-p4@usenetarchives.gap>`

```

On Thu, 21 May 1998 09:02:51 -0700, "Fujitsu Software Corporation"
wrote:

› Fujitsu COBOL supports a majority of the RM/COBOL specific features and most
› users find a port of RM/COBOL to Fujitsu COBOL a straight recompile. You
› can get the FREE unrestricted Fujitsu COBOL Starter Set at www.adtools.com
›
Can you tell me if it supports the following sentence

working ...
01 num-cursor pic 99.
01 variable pic x
procedure ...
Display variable line 1 column 1 no beep no tab reverse
erase eol
blink echo convert cursor num-cursor high.

I have tried it with no luck.

Best regards

Frederico Fonseca
```

##### ↳ ↳ Re: MF-RM differences???

- **From:** "albert ratzlaff" <ua-author-6589172@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8539aafee-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8539aafee-p4@usenetarchives.gap>`
- **References:** `<6jv60g$jlv$1@news.nuri.net> <gap-f8539aafee-p4@usenetarchives.gap>`

```



Fujitsu Software Corporation escribiÃ³:

› Fujitsu COBOL supports a majority of the RM/COBOL specific features and most
› users find a port of RM/COBOL to Fujitsu COBOL a straight recompile.  You
…[14 more quoted lines elided]…
›› 

Hello,

Does Fujitzu COBOL support ACCEPT SIZE? (Or is there a workaround)?

Regards
Albert Ratzlaff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
