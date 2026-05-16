[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VACOBOL FFS problem

_2 messages · 2 participants · 2002-10_

---

### VACOBOL FFS problem

- **From:** tom.austin@usa.xerox.com (Tom Austin)
- **Date:** 2002-10-02T13:20:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1f8b38c.0210021220.3f1e4a9a@posting.google.com>`

```
I have been working with vACOBOl and we now have the FFS installed on
OS390. I am having trouble connecting to my PDS's. Sometimes it
connnects properly but more often it fails. By failing I mean that I
cannot see any of the programs in the file window or inthe project
component window.

I have tried using both the program editor and the projects tool. 
When I have been successful I can change the program source with the
program editor but if I access program source I get a message that the
PDS is locked and i get read only access.

Here is an entry from the ffstrace log for a situation where i cannot
see the PDS.
I have been trying to locate the documentation for FFS errors but I
cannot find it. Please help me if you can.

13:42:36.421 ffsdir.cpp(591) .<exit>  DirectoryListing::getJListing()
     <result> Succesfully
13:42:36.421 ffsdir.cpp(675) .<exit> 
FFSFileDirectory::FFSFileDirectory("tazz01.tsour", 0)
     <result> succesful
13:42:36.421 ffsfile.cpp(425) .<entry> FFSFileObject::~FFSFileObject()
- name: tazz01.tsour
13:42:36.421 ffsfile.cpp(432) .<exit>  FFSFileObject::~FFSFileObject()
     <result> tazz01.tsour
13:43:14.046 ffscontrol.cpp(499) . ffstap() coeweb1.xcc.mc.xerox.com
portno: 97
13:43:15.531 ffscontrol.cpp(518) . Connect failed with error 10061
13:43:39.453 ffscontrol.cpp(319) .<entry> FFSControl::endTap(SYS21)
13:43:39.453 ffscontrol.cpp(351) .<exit>  FFSControl::endTap()
     <result> successful
```

#### ↳ Re: VACOBOL FFS problem

- **From:** "Al Shannon" <shannon@allover.com>
- **Date:** 2002-10-02T20:15:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mCOm9.2$qg1.4355@news.sjc.globix.net>`
- **References:** `<b1f8b38c.0210021220.3f1e4a9a@posting.google.com>`

```
Try posting your question in the ibm.software.cobol group on the
news.software.ibm.com newsserver.

Good luck.

Al...

"Tom Austin" <tom.austin@usa.xerox.com> wrote in message
news:b1f8b38c.0210021220.3f1e4a9a@posting.google.com...
> I have been working with vACOBOl and we now have the FFS installed on
> OS390. I am having trouble connecting to my PDS's. Sometimes it
…[28 more quoted lines elided]…
>      <result> successful
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
