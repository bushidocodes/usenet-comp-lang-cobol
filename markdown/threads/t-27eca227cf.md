[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TAB expansion in current Micro Focus (MERANT) products

_2 messages · 2 participants · 2001-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### TAB expansion in current Micro Focus (MERANT) products

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-11-15T09:16:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9t0mej$6lp$1@slb4.atl.mindspring.net>`

```
As a follow-up on another thread, I have been having a discussion with
various parts of Micro Focus concerning TAB expansion in the current
products.  (This is NOT necessarily true of earlier products - such as
Microsoft COBOL).  The following is the summary that "we" have come up with
(and which will be reflected in some future MF documentation)

   ***

A) The LRM is in ERROR.  The T run-time switch *never* impacts the handling
of TABs on a READ (of LINE SEQUENTIAL files).  (It does impact the WRITE -
and REWRITE statements)

B) The EXPANDTAB/INSERTAB feature is only available for the "NetExpress,
Mainframe Express, and Server Express external file handlers"

C) When EXPANDTAB is set to "off" in the NE, MFE and SX external file
handler
configuration file, then tabs are NOT expanded (for line sequential files)
on READs - in all other cases, they are.

D) For Object COBOL, there is (currently) *no* way to avoid TAB expansion on
READs.

  ***

Sorry for any confusion that my "vague memories" or reading of conflicting
documentation may have caused.
```

#### ↳ Re: TAB expansion in current Micro Focus (MERANT) products

- **From:** Paul Barnett <paul.barnett@microfocus.nospam.com>
- **Date:** 2001-11-16T17:08:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BF547F1.EAA8966D@microfocus.nospam.com>`
- **References:** `<9t0mej$6lp$1@slb4.atl.mindspring.net>`

```
Bill,

Regarding your Message Header. In case you are not aware, Micro Focus is now an
independant company and no longer part of MERANT. Micro Focus became
independant on 10th August 2001.

Regards,
Paul

www.microfocus.com

"William M. Klein" wrote:

> As a follow-up on another thread, I have been having a discussion with
> various parts of Micro Focus concerning TAB expansion in the current
…[28 more quoted lines elided]…
>  wmklein <at> ix.netcom.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
