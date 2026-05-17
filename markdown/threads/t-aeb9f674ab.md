[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Are Debuggable Cobol DLLs possible?

_4 messages · 3 participants · 1998-06_

---

### Are Debuggable Cobol DLLs possible?

- **From:** "gary kelleher" <ua-author-17084178@usenetarchives.gap>
- **Date:** 1998-06-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd8e81$80130f20$e7b262cf@endxokep>`

```

Do any of the toolmakers support PDB files so that their code can be
debugged through MS Developer Studio at the assembly language level?
```

#### ↳ Re: Are Debuggable Cobol DLLs possible?

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-06-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeb9f674ab-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd8e81$80130f20$e7b262cf@endxokep>`
- **References:** `<01bd8e81$80130f20$e7b262cf@endxokep>`

```

Gary,

Currently Fujitsu does not support debugging through MS Developer Studio.
Fujitsu COBOL includes an option for the creation of an Assembler Listing
with Code and Comments.

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com



Gary Kelleher wrote in message <01bd8e81$80130f20$e7b262cf@endxokep>...
› Do any of the toolmakers support PDB files so that their code can be
› debugged through MS Developer Studio at the assembly language level?
›
›
```

##### ↳ ↳ Re: Are Debuggable Cobol DLLs possible?

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-06-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeb9f674ab-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aeb9f674ab-p2@usenetarchives.gap>`
- **References:** `<01bd8e81$80130f20$e7b262cf@endxokep> <gap-aeb9f674ab-p2@usenetarchives.gap>`

```

Gary,

My goodness, Fujitsu COBOL can't do something . Well, as far as
I am aware NetExpress DLLs cannot be debugged through Developer
Studio either. We could in theory get our compiler to generate PDB
files however, this would not be sufficient. The Developer Studio
environment would need to understand COBOL datatypes so that
variables could be queried correctly.

NetExpress and MSDS both use PTRACE debugging. It is not
possible to use two debuggers simultaneously in this environment
(as far as I am aware). NetExpress does have the ability to
dynamically start the COBOL debugger at runtime so it is
possible to debug mixed language applications.

Due to the PTRACE restriction you can either debug the C and run
the COBOL or vice versa.

I hope the above information is of help.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

Fujitsu Software Corporation wrote in message
<6l3mgq$hit$1.··.@nnt··t.com>...
› Gary,
› 
…[19 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Are Debuggable Cobol DLLs possible?

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-06-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeb9f674ab-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aeb9f674ab-p2@usenetarchives.gap>`
- **References:** `<01bd8e81$80130f20$e7b262cf@endxokep> <gap-aeb9f674ab-p2@usenetarchives.gap>`

```

Gary,

The Fujitsu COBOL WINSVD debugger will automatically debug any DLL compiled
with the TEST option.

What that means is if a C module calls a COBOL DLL then on invocation of the
COBOL DLL the WINSVD debugger will pop-up and you can begin to debug the
COBOL DLL.

Due to current restriction you can either debug the C module and run the
COBOL DLL or vice versa.

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


Fujitsu Software Corporation wrote in message
<6l3mgq$hit$1.··.@nnt··t.com>...
› Gary,
› 
…[19 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
