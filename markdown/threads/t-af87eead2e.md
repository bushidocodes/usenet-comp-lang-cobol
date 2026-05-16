[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [Fwd: STRING, UNstring & INSPECT are not recommended]

_5 messages · 4 participants · 2000-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### [Fwd: STRING, UNstring & INSPECT are not recommended]

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.cics-l
- **Message-ID:** `<39587336.17BE2312@istar.ca>`

```
I am forwarding this to comp.lang.cobol to verify my impression that VS
COBOL II, COBOL for MVS and VM and COBOL for MVS and VM have no
restrictions on the use of STRING, UNSTRING and INSPECT.  All of these
are 31 bit compilers.

Clark Morris, CFM Technical Programming Services Inc., cfmtech@istar.ca

-------- Original Message --------
Subject: STRING, UNstring & INSPECT are not recommended
Date: Tue, 27 Jun 2000 09:14:00 GMT
From: Patrick Lee <patricklee@whbhk.com>
Organization: Deja.com - Before you buy.
Newsgroups: bit.listserv.cics-l

Dear all,
According to IBM APAR II06138, we should not use STRING, UNSTRING,
INSPECT because they will eat up our 24bit Getvis area. Any
recommendation of alternatives for these 3 words????

Thanks.

Patrick.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: STRING, UNstring & INSPECT are not recommended]

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.cics-l
- **Message-ID:** `<8jalpm$d5t$1@slb7.atl.mindspring.net>`
- **References:** `<39587336.17BE2312@istar.ca>`

```
I believe that you are correct.  I tried to find this documented in the COBOL
manuals, but couldn't (easily).  HOWEVER, I can find the list of what "is"
restricted under the current COBOL with CICS - and it doesn't include those
verbs.  Check out:


http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/4%2e10%2e1%2e6
```

##### ↳ ↳ Re: STRING, UNstring & INSPECT are not recommended

- **From:** Kerry Ellis <Kerry.Ellis@msdw.com>
- **Date:** 2000-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.cics-l
- **Message-ID:** `<3959284F.3C8D8027@msdw.com>`
- **References:** `<39587336.17BE2312@istar.ca> <8jalpm$d5t$1@slb7.atl.mindspring.net>`

```
OS/VS Cobol was oblivious to the CICS environment.  The Inspect,
String and Unstring statements invoked routines that issued OS (not
CICS) Getmains.  Because OS/VS Cobol programs had to be term-
inated with an EXEC CICS RETURN, the Cobol runtime routines
were never given a chance to clean up; eventually, the CICS region
would run out of what used to be called "OSCOR" and incur an OS
abend such as S80A.  Nowadays, with Cobol II and the "new" LE
conforming compilers, all run time storage acquisition requests are
handled by environment specific library routines, so Inspect, String
and Unstring are given CICS DSA storage that is not different than
any other piece of transaction storage.  In addition, such programs
can be ended with a STOP RUN or an EXEC CICS RETURN;
both will go through normal program/run unit cleanup; however,
any task duration storage that is missed will be freed by task term-
ination.  (BTW, the restrictions against String, Unstring and Inspect
were dropped IIRC with the arrival of the Cobol II compiler which
was æons ago.)

Kerry


"William M. Klein" wrote:

> I believe that you are correct.  I tried to find this documented in the COBOL
> manuals, but couldn't (easily).  HOWEVER, I can find the list of what "is"
…[35 more quoted lines elided]…
> > Before you buy.
```

###### ↳ ↳ ↳ Re: STRING, UNstring & INSPECT are not recommended

- **From:** Patrick Lee <patricklee@whbhk.com>
- **Date:** 2000-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.cics-l
- **Message-ID:** `<8jbq6r$eif$1@nnrp1.deja.com>`
- **References:** `<39587336.17BE2312@istar.ca> <8jalpm$d5t$1@slb7.atl.mindspring.net> <3959284F.3C8D8027@msdw.com>`

```
Kerry,
Thanks for your detail explanation. But IBM guy told me the issue
applies to COBOL/VSE even through it state in the COBOL manual that it
only applies to DOS/COBOL. Is that true??

PL.
In article <3959284F.3C8D8027@msdw.com>,
  Kerry Ellis <Kerry.Ellis@MSDW.com> wrote:
> OS/VS Cobol was oblivious to the CICS environment.  The Inspect,
> String and Unstring statements invoked routines that issued OS (not
…[20 more quoted lines elided]…
> > I believe that you are correct.  I tried to find this documented in
the=
>  COBOL
> > manuals, but couldn't (easily).  HOWEVER, I can find the list of
what "=
> is"
> > restricted under the current COBOL with CICS - and it doesn't
include t=
> hose
> > verbs.  Check out:
> >
> > http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/4%
2e10%2=
> e1%2e6
> >
…[5 more quoted lines elided]…
> > > I am forwarding this to comp.lang.cobol to verify my impression
that =
> VS
> > > COBOL II, COBOL for MVS and VM and COBOL for MVS and VM have no
> > > restrictions on the use of STRING, UNSTRING and INSPECT.  All of
thes=
> e
> > > are 31 bit compilers.
> > >
> > > Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.=
> ca
> > >
…[20 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: STRING, UNstring & INSPECT are not recommended

_(reply depth: 4)_

- **From:** Kerry Ellis <Kerry.Ellis@msdw.com>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.cics-l
- **Message-ID:** `<395D0385.76ADF25D@msdw.com>`
- **References:** `<39587336.17BE2312@istar.ca> <8jalpm$d5t$1@slb7.atl.mindspring.net> <3959284F.3C8D8027@msdw.com> <8jbq6r$eif$1@nnrp1.deja.com>`

```
Sorry, I wouldn't have the foggiest idea.  I think that the
last time I worked on an IBM DOS system was in 1971.
Anyway, I doubt that the "IBM Guy" is anywhere near
being correct.  See:

 4.8.1.6 "COBOL/VSE Programming Guide" via IBM BookManager BookServer

which appears to have become applicable as long ago
as 1983.  Even DOS/VSE has emerged into the 20th
century (even if everybody else is in the 21st).

Kerry

Patrick Lee wrote:

> Kerry,
> Thanks for your detail explanation. But IBM guy told me the issue
…[84 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
