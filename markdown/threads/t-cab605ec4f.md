[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ever use Dialog with XDB?

_2 messages · 2 participants · 1996-09_

---

### Ever use Dialog with XDB?

- **From:** "asm..." <ua-author-17087123@usenetarchives.gap>
- **Date:** 1996-09-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<51qacp$as3@test-sun.erols.com>`

```

I am working on a contract where the statement of work calls for using
microfocus cobol on an IBM mainframe accessing a DB2 database. Over a
LAN we plan to use PC workstations running windows and using Dialog to
communicate with CICS and then the mainframe. Our team has been
throwing arround the idea of getting rid of the CICS and using a ODBC
connection with XDB to communicate over the LAN. The only problem is
that I do not know anything about Dialog or XDB. If anyone out there
has experience in using such a configuration I would be interested in
hearing what you think. What are the possible pitfalls of this setup?

Thanks,
Brad Marshall
asm··.@er··s.com
```

#### ↳ Re: Ever use Dialog with XDB?

- **From:** "sa..." <ua-author-17071631@usenetarchives.gap>
- **Date:** 1996-09-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cab605ec4f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<51qacp$as3@test-sun.erols.com>`
- **References:** `<51qacp$as3@test-sun.erols.com>`

```

asm··.@er··s.com wrote:

› I am working on a contract where the statement of work calls for using
› microfocus cobol on an IBM mainframe accessing a DB2 database. Over a
…[6 more quoted lines elided]…
› hearing what you think. What are the possible pitfalls of this setup?
 
› Thanks,
› Brad Marshall
› asm··.@er··s.com

At our shop we have been using CICS/OS2 to link between IBM Mainframe
CICS and our Microfocus COBOL systems on the LAN.

Microfocus COBOL proggies use the External Call Interface of CICS/OS2
to pass a COMMAREA to the Mainframe CICS program. The LAN based prog
is essential carrying out an "EXEC CICS LINK" to the the mainframe
program.

This setup has proved to be resiliant in our production environment.

Hope this is of help.
Dave Sands
sa··.@eas··o.uk
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
