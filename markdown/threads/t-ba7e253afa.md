[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question on NetExpress running in NT

_3 messages · 3 participants · 1999-03_

---

### Question on NetExpress running in NT

- **From:** "Juan Rodriguez" <juanr@wilwel.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tBF2.15$FF.1117@news.ntr.net>`

```
We are in the initial stage of converting our Cobol product to NetExpress.
The programs and data will reside in an NT Server and the client
workstations will be running Win95/98.  We are unsure as to whether to use
the NetExpress Indexed Files or a DBMS such as SQL Server as the Data
Warehouse.

If anyone has had any experience with NetExpress addressing indexed files
residing on an NT Server or NetExpress addressing a SQL DataBase residing on
an NT Server, we would really appreciate your comments.

Thanks
```

#### ↳ Re: Question on NetExpress running in NT

- **From:** jack_b@my-dejanews.com
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cbh2f$kc1$1@nnrp1.dejanews.com>`
- **References:** `<1tBF2.15$FF.1117@news.ntr.net>`

```
In article <1tBF2.15$FF.1117@news.ntr.net>,
  "Juan Rodriguez" <juanr@wilwel.com> wrote:
> We are in the initial stage of converting our Cobol product to NetExpress.
> The programs and data will reside in an NT Server and the client
…[10 more quoted lines elided]…
>
I developed an application for a client in 1997 which does exactly what you
describe using MF indexed files and no DBMS.  It is a Direct Marketing
application that maintains several million member and purchase records as well
as many associated files necessary for running a business.

Our results have been excellent.  Of course, system design related to the
indexes is all important for a fast and user friendly outcome.

Keep in mind the 1GB file-size limitation.  I have not had to deal with that
and cannot advise you of the complications of the MF fix.

A good UPS will also keep you out of trouble.  Also the MF rebuild program is
useful.  Good luck.





-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Question on NetExpress running in NT

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E92403.54B55523@IMN.nl>`
- **References:** `<1tBF2.15$FF.1117@news.ntr.net>`

```
Juan,

Both options are possible. We use SQL Server, with some success. NetExpress 2.0
has a nasty ODBC-bug when using null-indicators on updates and inserts, I
recommend v3.0.

Good luck.

The COBOL Frog

Juan Rodriguez wrote:

> If anyone has had any experience with NetExpress addressing indexed files
> residing on an NT Server or NetExpress addressing a SQL DataBase residing on
> an NT Server, we would really appreciate your comments.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
