[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to pass parameters to a COBOL program in CMS?

_4 messages · 2 participants · 2002-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to pass parameters to a COBOL program in CMS?

- **From:** mikey.unsafe@gmx.net (Mikey)
- **Date:** 2002-02-15T07:47:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26282372.0202150747.26f8b4b3@posting.google.com>`

```
Hello

the question is in the headline

thx
```

#### ↳ Re: How to pass parameters to a COBOL program in CMS?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-15T12:50:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4jli9$mnc$1@slb4.atl.mindspring.net>`
- **References:** `<26282372.0202150747.26f8b4b3@posting.google.com>`

```
Assuming you mean a "user parameter" and not a "run-time parameter" AND
assuming you are using a currently supported COBOL compiler (under LE),
check out:

 CEE3PRM--Query Parameter String

at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3031/3.5.12

If you are NOT running under LE, then there are some other options also
available.  Tell us what compiler (version and release) you are using.
```

##### ↳ ↳ Re: How to pass parameters to a COBOL program in CMS?

- **From:** mikey.unsafe@gmx.net (Mikey)
- **Date:** 2002-02-16T08:34:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26282372.0202160834.2a424285@posting.google.com>`
- **References:** `<26282372.0202150747.26f8b4b3@posting.google.com> <a4jli9$mnc$1@slb4.atl.mindspring.net>`

```
Okay thx for the tip
Im not a specialist at the Host but the cee3prm seems to 
exist on our machine in school.
( I also dont know how to get version of our compiler, but 
its surely a cobol II )

Is there also a way to work with the LINKAGE SECTION ?

thx


"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<a4jli9$mnc$1@slb4.atl.mindspring.net>...
> Assuming you mean a "user parameter" and not a "run-time parameter" AND
> assuming you are using a currently supported COBOL compiler (under LE),
…[20 more quoted lines elided]…
> > thx
```

###### ↳ ↳ ↳ Re: How to pass parameters to a COBOL program in CMS?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-16T20:09:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4n3cp$kh4$1@nntp9.atl.mindspring.net>`
- **References:** `<26282372.0202150747.26f8b4b3@posting.google.com> <a4jli9$mnc$1@slb4.atl.mindspring.net> <26282372.0202160834.2a424285@posting.google.com>`

```
If you are still using the (currently unsupported by IBM) VS COBOL II
compiler and are NOT running under LE, then check out the information at:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igya1101/7.2#HDRE
XOPT

for another way to get user parameters in a COBOL (CMS) program.  You may
also want to read:

 "APPENDIX1.1.3.3.2 Using the CMS LOAD and START Commands"

at


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igya1101/APPENDIX
1.1.3.3.2?

for how to actually "pass" parameters to your COBOL program under CMS.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
