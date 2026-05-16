[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXTERNAL clause

_3 messages · 2 participants · 2002-02_

---

### EXTERNAL clause

- **From:** Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com>
- **Date:** 2002-02-21T13:48:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C74EC96.E5818524@fujitsu-siemens.com>`

```
What is the meaning of VALUE clause for EXTERNAL data; I found the
following in the new standard draft:
"ï¿½. the VALUE clause specification, if any, for each record name of the
associated record description entries shall be identical;"
This description is different from VALUE clause within FILE SECTION or
LINKAGE SECTION where the VALUE clause is ignored unless there is an
INITIALIZE statement used. The effect of the VALUE clause within an
EXTERNAL data description is not clear. I hope somebody can help me.

Thanks in advance
Rosa
```

#### ↳ Re: EXTERNAL clause

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-21T12:51:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a53fji$14d$1@slb6.atl.mindspring.net>`
- **References:** `<3C74EC96.E5818524@fujitsu-siemens.com>`

```
Page 380, General Rule 4a says

"4) VALUE clauses in the working-storage, local-storage, and communication
sections take effect:
    a) for external items, during the execution of an INITIALIZE statement"

What I read the first part of GR(4) on page 289 (which says)

"4) Within a run unit, if two or more source elements describe the same
external data record, each name that is externalized to the operating
environment for the record description entries shall be the same; the VALUE
clause specification, if any, for each record name of the associated record
description entries shall be identical; and the records shall define the
same number of bytes."


to mean is that *if* you put a VALUE clause on an EXTERNAL item, that it
needs to be the same in every program defining that item.  This means that
no matter WHICH program does an INITIALIZE TO VALUE, the item will get the
same value.  (This is similar to other restrictions on EXTERNAL items - that
require them to "match" in each place that they are defined.)
```

##### ↳ ↳ Re: EXTERNAL clause

- **From:** Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com>
- **Date:** 2002-02-26T15:51:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C7BA0E0.8DB56F38@fujitsu-siemens.com>`
- **References:** `<3C74EC96.E5818524@fujitsu-siemens.com> <a53fji$14d$1@slb6.atl.mindspring.net>`

```
Thank you for your answer, it helps a lot. As you already realized I work for a
german computer company located in Munich, Bavaria. (Manual page of our COBOL
Department
http://manuals.fujitsu-siemens.com/servers/bs2_man/man_us/cobol.htm)

Sincerely
Rosa
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
