[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 805 problem

_3 messages · 3 participants · 1998-08_

---

### 805 problem

- **From:** "news.onaustralia.com.au" <ua-author-17074068@usenetarchives.gap>
- **Date:** 1998-08-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdbda2$514d1640$cc11868b@default>`

```
Hi,
When you run DB2-COBOL program, its compare loadmodule timestamp
with PACAKGE timestamp, if it doesnt match it gives 805.

Do you know how to find LOADMODULE/ and PACKAGE timestamp?

Any comment will highly appriciated

Regards
Sam
```

#### ↳ Re: 805 problem

- **From:** "gene webb" <ua-author-6589136@usenetarchives.gap>
- **Date:** 1998-08-04T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcb07cea0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bdbda2$514d1640$cc11868b@default>`
- **References:** `<01bdbda2$514d1640$cc11868b@default>`

```
I belive you will find a package table in the database. That has a date and
timestamp column.
news.onaustralia.com.au wrote in message
<01bdbda2$514d1640$cc11868b@default>...
› Hi,
› When you run DB2-COBOL program, its compare loadmodule timestamp
…[10 more quoted lines elided]…
›
```

#### ↳ Re: 805 problem

- **From:** "am" <ua-author-33177@usenetarchives.gap>
- **Date:** 1998-08-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcb07cea0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bdbda2$514d1640$cc11868b@default>`
- **References:** `<01bdbda2$514d1640$cc11868b@default>`

```
-805 not found in plan.
-818 is timestamp difference

Select timestamp
from Sysibm.Sysdbrm
where name =
and plname =

Select timestamp
from Sysibm.Syspackage
where name =


news.onaustralia.com.au wrote in article
<01bdbda2$514d1640$cc11868b@default>...
| Hi,
| When you run DB2-COBOL program, its compare loadmodule timestamp
…[11 more quoted lines elided]…
|
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
