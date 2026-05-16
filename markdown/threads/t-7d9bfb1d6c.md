[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS/NT and SFS files in "batch"

_2 messages · 2 participants · 1998-09 → 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS/NT and SFS files in "batch"

- **From:** "Niels Chr. Madsen" <ncm@memobase.dk>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<3611EB2A.22609228@memobase.dk>`

```
Has anyone any idea of how I can access my "VSAM" files in SFS from
"batch" programs.
The Files are created in CICS/NT (TS 4.0), and my programs are written
in Micro Focus Object COBOL (but original they are COBOL II mainframe
programs)

Niels Chr. Madsen
MemoBase Team
```

#### ↳ Re: CICS/NT and SFS files in "batch"

- **From:** Philip Morten <pmorten@transarc.com>
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<36190390.99CC703A@transarc.com>`
- **References:** `<3611EB2A.22609228@memobase.dk>`

```
Niels Chr. Madsen wrote:
> 
> Has anyone any idea of how I can access my "VSAM" files in SFS from
…[6 more quoted lines elided]…
> MemoBase Team

There is a section in the Application Programming Guide (1) entitled 
"Updating files from non-CICS applications", this explains how to use 
the SFS external file handler.

Philip Morten

(1) 	Transaction Server for Windows NT 
	Application Programming Guide (CICS) 
	Version 4 
	Document Number SC33-1888-01
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
