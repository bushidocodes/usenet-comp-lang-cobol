[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL and DB2 CLI (OS/2 & AIX)

_4 messages · 3 participants · 1996-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### MF COBOL and DB2 CLI (OS/2 & AIX)

- **From:** "nhe..." <ua-author-12239418@usenetarchives.gap>
- **Date:** 1996-02-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fmch4$6rg@cloner3.netcom.com>`

```
I would like to write an application utilizing the DB2 CLI interface with MicroFocus COBOL.

Anyone done this?
```

#### ↳ Re: MF COBOL and DB2 CLI (OS/2 & AIX)

- **From:** "gary long" <ua-author-107076@usenetarchives.gap>
- **Date:** 1996-02-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1be71c8b6f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4fmch4$6rg@cloner3.netcom.com>`
- **References:** `<4fmch4$6rg@cloner3.netcom.com>`

```
nhe··.@ix.··m.com wrote:
›
› I would like to write an application utilizing the DB2 CLI interface with MicroFocus COBOL.
›
› Anyone done this?

We have written a C layer over the CLI, then called it from COBOL. Worked
great.

We have also written COBOL E/SQL for DB2/6000.

I think you will find the CLI to be a little tedious from COBOL. That's why
we wrote the intermediate layer. Made it higher-level and more
COBOL-friendly.

-- Gary
```

##### ↳ ↳ Re: MF COBOL and DB2 CLI (OS/2 & AIX)

- **From:** "#nhe..." <ua-author-12495530@usenetarchives.gap>
- **Date:** 1996-02-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1be71c8b6f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1be71c8b6f-p2@usenetarchives.gap>`
- **References:** `<4fmch4$6rg@cloner3.netcom.com> <gap-1be71c8b6f-p2@usenetarchives.gap>`

```
In <311··.@ca··s.com>, Gary Long writes:
› nhe··.@ix.··m.com wrote:
››
 
› We have written a C layer over the CLI, then called it from COBOL. Worked
› great.
›

I have written a bit of ODBC in COBOL and you're right-it's very tedious. Unfortunately I don't have time to write my own layers. Would you be willing to post what it takes to make a CLI call from MF COBOL?
Not so much the source code, but the environment, directives, linking, etc. would be very helpful.

I am running 16-bit MF COBOL on OS/2 Warp.
```

###### ↳ ↳ ↳ Re: MF COBOL and DB2 CLI (OS/2 & AIX)

- **From:** "gary long" <ua-author-107076@usenetarchives.gap>
- **Date:** 1996-02-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1be71c8b6f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1be71c8b6f-p3@usenetarchives.gap>`
- **References:** `<4fmch4$6rg@cloner3.netcom.com> <gap-1be71c8b6f-p2@usenetarchives.gap> <gap-1be71c8b6f-p3@usenetarchives.gap>`

```
#nhe··.@ix.··m.com wrote:
› 
› In <311··.@ca··s.com>, Gary Long  writes:
…[13 more quoted lines elided]…
› I am running 16-bit MF COBOL on OS/2 Warp.

I'd be glad too, but as I said in the earlier post we don't do the CLI
from COBOL, only from C. From COBOL we use DB2(AIX) E/SQL.

-- Gary

------------------------------------------------------------------------
Gary Long gl··.@ma··a.com
Vice President, Product Development
Magna Software Corporation Phone: 703/222-3500
12450 Fair Lakes Circle Fax: 703/222-8433
Fairfax, Virginia 22033

Technical data on "MAGNA X" CS/TP Application Generator: in··.@ma··a.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
