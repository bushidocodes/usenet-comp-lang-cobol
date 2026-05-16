[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interface to create a commarea with data for testing ?

_6 messages · 4 participants · 2005-12_

---

### Interface to create a commarea with data for testing ?

- **From:** dingdongdingding@yahoo.com
- **Date:** 2005-12-02T06:24:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com>`

```
I have a copybook.  I need to create a file with a commarea.  Is there
a tool that runs on Windows that can allow me to do some data entry
with validation and create the commarea ?

Thanks.
```

#### ↳ Re: Interface to create a commarea with data for testing ?

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-12-02T09:14:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vZjf.47096$6y4.6250@bignews3.bellsouth.net>`
- **References:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com>`

```
<dingdongdingding@yahoo.com> wrote:
>I have a copybook.  I need to create a file with a commarea.  Is there
> a tool that runs on Windows that can allow me to do some data entry
> with validation and create the commarea ?


Could you define "commarea"?
```

##### ↳ ↳ Re: Interface to create a commarea with data for testing ?

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-12-06T15:30:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1133911849.171011.211050@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<6vZjf.47096$6y4.6250@bignews3.bellsouth.net>`
- **References:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com> <6vZjf.47096$6y4.6250@bignews3.bellsouth.net>`

```

Judson McClendon wrote:
> <dingdongdingding@yahoo.com> wrote:
> >I have a copybook.  I need to create a file with a commarea.  Is there
…[9 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."

This made me bark up the wrong tree (I thought about inter-partition
communications on an IBM DOS/VSE mainframe) but then I remembered
CICS/COBOL uses a commarea.

Do you think the email address of dingdongdingding  rings any bells?
```

#### ↳ Re: Interface to create a commarea with data for testing ?

- **From:** dingdongdingding@yahoo.com
- **Date:** 2005-12-06T21:21:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1133932899.108600.159420@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com>`
- **References:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com>`

```
Any know if there is such a tools on Windows ?  We are interfacing with
the mainframe applications and our software runs on Unix/Win.  We
currently FTP the copybook to the mainframe and use FileAid to enter
the test data, generate a file (of the commarea) and FTP it back to the
Win machine to test.

It would be good if there is a tool that we can use on Win.  Thanks.

dingdongdingding@yahoo.com wrote:
> I have a copybook.  I need to create a file with a commarea.  Is there
> a tool that runs on Windows that can allow me to do some data entry
> with validation and create the commarea ?
> 
> Thanks
```

##### ↳ ↳ Re: Interface to create a commarea with data for testing ?

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-12-07T14:08:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1133993330.782983.117990@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1133932899.108600.159420@g49g2000cwa.googlegroups.com>`
- **References:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com> <1133932899.108600.159420@g49g2000cwa.googlegroups.com>`

```

dingdongdingding@yahoo.com wrote:
> Any know if there is such a tools on Windows ?  We are interfacing with
> the mainframe applications and our software runs on Unix/Win.  We
…[11 more quoted lines elided]…
> > Thanks

There is a programming language called SELCOPY from a company called
Compute of Bridgend which comes with a version which runs on pcs. The
language has a GENERATE verb which can be used to create data within
bounds that you can define.

It won't be cheap.
```

###### ↳ ↳ ↳ Re: Interface to create a commarea with data for testing ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-12-07T22:42:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ozJlf.271637$Kr.213636@fe08.news.easynews.com>`
- **References:** `<1133533487.357436.53350@f14g2000cwb.googlegroups.com> <1133932899.108600.159420@g49g2000cwa.googlegroups.com> <1133993330.782983.117990@g44g2000cwa.googlegroups.com>`

```
If "dingdong" is currently licensed for MFEEE (Mainframe Express, Enterprise 
Edition), it comes with a PC version of IEBDG, which does this (sort-of).  I 
know of VERY few people who use that IBM utility on the mainframe, so I don't 
think it will/is "wildly popular" on the PC, but it could be used (if one so 
desired).

P.S.  Doesn't Compuware also sell a PC version of File-Aid?  If so, that would 
work "just like" the mainframe version currently being used.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
