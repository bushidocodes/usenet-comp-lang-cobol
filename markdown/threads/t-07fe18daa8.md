[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Finding DB2 qualifiers from CICS.

_3 messages · 3 participants · 2005-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### Finding DB2 qualifiers from CICS.

- **From:** "Balaji Pooruli" <pnbalaji@yahoo.com>
- **Date:** 2005-01-20T11:58:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106251096.135969.169140@c13g2000cwb.googlegroups.com>`

```
Hi,

Can some one help me in finding the DB2 table qualifiers that a CICS
region is accessing?. The command CEMT I DB2E gives only the DB2 sub
system the CICS region is connected to, and not the table qualifiers.
Is there any way I can find it?.

We have 5 DB2 sub systems and 9 CICS regions at our work place.
Thanks,
Balaji
```

#### ↳ Re: Finding DB2 qualifiers from CICS.

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-01-23T02:38:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-66FC6F.02381923012005@knology.usenetserver.com>`
- **References:** `<1106251096.135969.169140@c13g2000cwb.googlegroups.com>`

```
In article <1106251096.135969.169140@c13g2000cwb.googlegroups.com>,
 "Balaji Pooruli" <pnbalaji@yahoo.com> wrote:

> Hi,
> 
…[7 more quoted lines elided]…
> Balaji

You can't get this from CICS, but you can connect to the DB2 subsystem 
and ask it.

I think the tables you want to query are SYSIBM.SYSOWNER, 
SYSIBM.SYSPACKAGE, and SYSIBM.SYSTABLE.
```

##### ↳ ↳ Re: Finding DB2 qualifiers from CICS.

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-25T07:50:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cTmJd.213923$8G4.20121@tornado.tampabay.rr.com>`
- **References:** `<1106251096.135969.169140@c13g2000cwb.googlegroups.com> <joe_zitzelberger-66FC6F.02381923012005@knology.usenetserver.com>`

```
You could check your bind packages if each region has separate modules.
You may find your programs have been bound with QUALIFIER option.

JCE

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-66FC6F.02381923012005@knology.usenetserver.com...
> In article <1106251096.135969.169140@c13g2000cwb.googlegroups.com>,
> "Balaji Pooruli" <pnbalaji@yahoo.com> wrote:
…[17 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
