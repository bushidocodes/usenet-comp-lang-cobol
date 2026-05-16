[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do you call a java program from a Cobol CICS program?

_3 messages · 3 participants · 2002-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### How do you call a java program from a Cobol CICS program?

- **From:** mwhitney26@aol.com (MWhitney26)
- **Date:** 2002-03-27T23:12:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020327181215.19030.00000435@mb-fm.aol.com>`

```
Does anyone know how to call a Java program from a CICS COBOL program?  We are
using CICS TS 1.3.
```

#### ↳ Re: How do you call a java program from a Cobol CICS program?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-27T21:26:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7u2gg$anv$1@slb2.atl.mindspring.net>`
- **References:** `<20020327181215.19030.00000435@mb-fm.aol.com>`

```
From my usually reliable source,

"1) Java does not run in CICS 1.3
2) In CICS V2 you can use EXEC CICS LINK between COBOL and Java

3) We are working on allowing INVOKE between Java-based OO COBOL and Java
under CICS

4) You can't ever use CALL statements with Java, you can only INVOKE methods
that you inherited from classes.

5) You can use connectors from Java in WebSphere to start CICS transactions
in COBOL, but that is the wrong direction, I think."
```

##### ↳ ↳ Re: How do you call a java program from a Cobol CICS program?

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2002-03-28T22:24:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a82naq$2deh$1@innferno.news.tiscali.de>`
- **References:** `<20020327181215.19030.00000435@mb-fm.aol.com> <a7u2gg$anv$1@slb2.atl.mindspring.net>`

```
Bill,

CICS TS 1.3 support Java, but only compiled JAVA using the HPJ compiler.
Also the JVM isn't reusable so it might not a good option to use JAVA in
case of performance.

Roland
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
