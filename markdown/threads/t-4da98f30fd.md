[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# embedded subprograms

_3 messages · 3 participants · 2002-07_

---

### embedded subprograms

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2002-07-09T22:40:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020709184017.11120.00003054@mb-ci.aol.com>`

```
I am OJTing COBOL85 for mainframes.  
There is a copybook which inserts a complete little program for
handling database errors, with its own little working storage and
its own little procedure division, and so forth, just like a real program.  
It is pretty cool.  But I don't understand the purpose of it. 
It seems to me that it would be better to have an external
program and just make calls to it.
What are the advantgages of an embedded subprogram? 



Ross
http://community.webshots.com/user/ross_klatte
```

#### ↳ Re: embedded subprograms

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-07-09T17:50:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agfpc8$fne$1@slb0.atl.mindspring.net>`
- **References:** `<20020709184017.11120.00003054@mb-ci.aol.com>`

```
Nested programs (what you are referring to) perform BETTER than even
"statically called" subprograms in an IBM mainframe environment.  That is
the USUAL reason for their existence there.  Another reason, is that some
programmers coming from other programming languages "like" (and/or are used
to) "embedded procedures".
```

##### ↳ ↳ Re: embedded subprograms

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-07-11T02:07:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2D20A4.7050100@optonline.NOSPAM.net>`
- **References:** `<20020709184017.11120.00003054@mb-ci.aol.com> <agfpc8$fne$1@slb0.atl.mindspring.net>`

```
William M. Klein wrote:
> Nested programs (what you are referring to) perform BETTER than even
> "statically called" subprograms in an IBM mainframe environment.  That is
> the USUAL reason for their existence there.  Another reason, is that some
> programmers coming from other programming languages "like" (and/or are used
> to) "embedded procedures".

Another major advantage I found was that they are called like an 
external program, i.e., with parameters, so the nested program can 
address anything the caller can address. This is a difficult issue in 
PERFORMed logic.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
