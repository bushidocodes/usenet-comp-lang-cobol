[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling an external program in MF NetExpress

_3 messages · 3 participants · 1999-02_

---

### Calling an external program in MF NetExpress

- **From:** Renee Poerschke <poerschke@ksn.de>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CD669E.D5B0BAA0@ksn.de>`

```
Hi

I want to execute a programm (e.g. Word) from Micro Focus
Net Express. Has anyone solved this problem before? I can't
find a library function to do this

Renee
```

#### ↳ Re: Calling an external program in MF NetExpress

- **From:** smb@mfltdz.co.ukz (Steve Biggs)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ajre6$tbk@hyperion.mfltd.co.uk>`
- **References:** `<36CD669E.D5B0BAA0@ksn.de>`

```
Renee Poerschke <poerschke@ksn.de> wrote:
>I want to execute a programm (e.g. Word) from Micro Focus
>Net Express. Has anyone solved this problem before? I can't
>find a library function to do this

Hi Renee,
If you just want to start up Word and not do anything with it, then you 
could either call the Windows API "CreateProcessA" (using the right 
call-convention and parameters) or use the COBOL call CBL_EXEC_RUN_UNIT. 

If you want to create/amend/save Word documents from your COBOL program, 
you can use OLE automation from COBOL - there's an example of that in
\netexpress\base\demo\oledemos\report.

(The demo also demonstrates calling Excel, and some more general Object 
COBOL work, but this is quite easy to comment out. The current version of 
the demo uses the Word95 automation interface, rather than the newer 
Word97 interface, but the latter is just as accessible from COBOL.)

Steve.
MERANT Micro Focus Development.
```

#### ↳ Re: Calling an external program in MF NetExpress

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990220200936.12657.00000849@ng150.aol.com>`
- **References:** `<36CD669E.D5B0BAA0@ksn.de>`

```
Hi Renee,

If you would like an example of the create process API please e-mail me.

Thanks,
Bob
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
