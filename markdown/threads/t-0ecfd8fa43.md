[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL, AS/400, Linux

_3 messages · 3 participants · 2002-05 → 2002-06_

**Topics:** [`AS/400, iSeries, RPG`](../topics.md#as400)

---

### COBOL, AS/400, Linux

- **From:** david.silber@hpdsoftware.com (David Silber)
- **Date:** 2002-05-17T08:39:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad85f189.0205170739.19440de1@posting.google.com>`

```
Q.1 Has IBM or another vendor (MF? Acucorp?) announced a COBOL
compiler to work in the AS/400 Linux environment?
Q.2 If so, or if it will be forthcoming, is there any doubt that ASCII
will be the default collating sequence?
Q.3 I've read that there are tools to convert EBCDIC files to ASCII.
Does anyone know where I could get further information?
Thanks. David Silber

P.S. Has anyone heard whether IBM has YET made a commitment to provide
a COBOL 2002-compliant compiler for the AS/400 (i-Series)? This was a
question I posted some months back and William Klein, among others,
reported no commitment by IBM --- not even for the flagship S390
(z-Series).
```

#### ↳ Re: COBOL, AS/400, Linux

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-05-17T15:29:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ac3p8a$1le$1@slb6.atl.mindspring.net>`
- **References:** `<ad85f189.0205170739.19440de1@posting.google.com>`

```
Having looked at:
  http://www-1.ibm.com/servers/eserver/iseries/linux/faq.html

which says,
 "iSeries provides the support for OS/400, Linux, Java, Domino, WebSphere,
UNIX, and Windows 2000 Server applications. In a single server, you can run
your core business and e-business applications, ..."

and

 http://www-1.ibm.com/servers/eserver/iseries/linux/resc.html

and  (more generally)

 http://www-1.ibm.com/servers/eserver/iseries/linux/edition/index.html

It does *not* appear that IBM has (yet) announced any COBOL solution for
Linux on OS/400.  HOWEVER,  given the "full" Java support, I would expect
PERCobol to work there (now - or soon).  Also, if you look at:

 http://www.microfocus.com/press/releases/20020219.asp

which is the Micro Focus (and IBM) announcement that they (MF) will be
providing the (a?) COBOL for Linux on  z/OS, it wouldn't surprise me if they
also provide an OS/400 version (as they do already for a number of other
Linux environments).

 ***

My personal GUESS is that this Linux will be EBCDIC and not ASCII "as the
default" - but I could be completely wrong.  I have looked at:
  http://www-1.ibm.com/servers/eserver/zseries/os/linux/facts.html

and can't tell what Linux on z/OS is, but I would GUESS that OS/400 would be
"comparable".

I know that Micro Focus has an "intelligent" ASCII/EBCDIC data converter
(that can read COBOL copy books and convert DISPLAY data while leaving
COMP-? data alone.   I think that Reallia does as well, but I am not certain
about Fujitsu.  IBM's VA product has ways of telling whether to use an ASCII
or EBCDIC "solution" - but I don't think they have an "intelligent"
conversion tool.

  ***

No, IBM has *NOT* yet made any public statement about when/if they will
support the next COBOL Standard on *any* platform.  It should be noted that
although there is now a 99.99999 probability that there will be an approved
2002 (or at worst 2003) Standard, until it actually finishes its ISO
approval steps, there is no guarantee.  Therefore, any vendor (such as Micro
Focus) that announces support for a 2002 Standard *could* end up as
embarrassed as Fujitsu did when they announced support for a 2000 Standard.


  ***

I hope that this helps.
```

#### ↳ iSeries Network Forum for COBOL/400

- **From:** "Hassan Farooqi" <hassanfarooqi@sympatico.ca>
- **Date:** 2002-06-15T18:35:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<opPO8.14185$Ju2.2683505@news20.bellglobal.com>`
- **References:** `<ad85f189.0205170739.19440de1@posting.google.com>`

```
You are invited to join the iSeries Network Forum for COBOL/400 questions.

http://www.iseriesnetwork.com/Forums/Main.cfm?CFApp=19

Hassan Farooqi
Forum Pro
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
