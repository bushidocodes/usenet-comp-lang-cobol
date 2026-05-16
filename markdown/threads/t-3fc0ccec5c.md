[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help! CICS WRITE is closing and disabling my file!

_3 messages · 3 participants · 2002-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Help! CICS WRITE is closing and disabling my file!

- **From:** randy@radiorandy.com (Randy Woods)
- **Date:** 2002-05-23T09:11:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e40710b8.0205230811.149f15a6@posting.google.com>`

```
I am issuing a CICS WRITE command from inside a COBOL program, which
executes perfectly.  When the program tries to execute another CICS
WRITE command, EIBRESP is 19, indicating FILE NOT OPEN.  Seems that
the WRITE command closed the file, and now nobody can use it.

Does anyone have an idea of what's going on here?  

randy at radiorandy dot com
```

#### ↳ Re: Help! CICS WRITE is closing and disabling my file!

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-05-23T12:39:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n8aqeuc05mphc7nkn2qua7qvn5rqvsat92@4ax.com>`
- **References:** `<e40710b8.0205230811.149f15a6@posting.google.com>`

```
On 23 May 2002 09:11:26 -0700 randy@radiorandy.com (Randy Woods) wrote:

:>I am issuing a CICS WRITE command from inside a COBOL program, which
:>executes perfectly.  When the program tries to execute another CICS
:>WRITE command, EIBRESP is 19, indicating FILE NOT OPEN.  Seems that
:>the WRITE command closed the file, and now nobody can use it.

I would suggest that more likely that the filename got messed up.

Why not check it?
```

#### ↳ Re: Help! CICS WRITE is closing and disabling my file!

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-05-25T06:47:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CEF337E.5010007@optonline.net>`
- **References:** `<e40710b8.0205230811.149f15a6@posting.google.com>`

```
Randy Woods wrote:

> I am issuing a CICS WRITE command from inside a COBOL program, which
> executes perfectly.  When the program tries to execute another CICS
…[3 more quoted lines elided]…
> Does anyone have an idea of what's going on here?  


There's nothing inherent in a Write command that will close a file. Have 
you checked the SYSOUT for the region to see if you're getting file 
errors? If you're using a file manager like CAFC, something might be 
wrong for this file's specification.

Is there now a "close on first reference" option for FCT's? <g>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
