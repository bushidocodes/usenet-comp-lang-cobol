[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PPT entry for Statically/Dynamically called subprograms in CICS.

_8 messages · 5 participants · 2002-08 → 2002-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### PPT entry for Statically/Dynamically called subprograms in CICS.

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-08-28T06:17:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0208280517.79feeb85@posting.google.com>`

```
Hi,
               First of all sorry for putting CICS question on COBOL
group.
My assumptions are as follows:
1. For Statically called module no PPT entry is required because
called module is part of main routine.
2. For Dynamically called module PPT entry is required as called
module is loaded at run time.Simultaneously we have to put called
module in CICS linked pack area.


Please reply me whether my assumptions are correct or not.


Regards.
Shyam
```

#### ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS.

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2002-08-28T17:40:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akjfds$bah$1@slb3.atl.mindspring.net>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com>`

```
Yes, you are correct.

Bill

"shyam nivas" <nivas_shyam@indiatimes.com> wrote in message
news:c02fd744.0208280517.79feeb85@posting.google.com...
> Hi,
>                First of all sorry for putting CICS question on COBOL
…[13 more quoted lines elided]…
> Shyam
```

##### ↳ ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS.

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-08-28T18:11:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akjljl$aie$1@slb5.atl.mindspring.net>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com> <akjfds$bah$1@slb3.atl.mindspring.net>`

```
Is he correct that the dynamically called modules MUST be in the "CICS
linked pack area"?   It may be just the term used, but I thought that
application load modules could be DFHRPL or possibly STEPLIB.  But I could
be TOTALLY mistaken on this.
```

#### ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS. (2)

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2002-08-28T22:09:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akjv8q$9qc$1@slb0.atl.mindspring.net>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com>`

```
A correction. You don't need to place Dynamically Called modules in the LPA.
They can be placed into your normal User Load Lib.

Dynamically Called module PPT entries can be Autoinstalled or explicitly
defined.

A heads-up for Dynamically Called modules. Try to keep your WS to a minimum
as Dynamically Called modules WS is not released until Task Termination.

A heads up for Statically Called modules. If the Caller's WS is reentrant
(or as in CICS/COBOL, serially reusable), try to pass a chunk of the
Caller's WS to the Static module as a parameter, ensuring that the Static
module will not be accessing storage defined to itself, which will render it
non-reentrant and cause those ever-popular "unpredictable results" as
mentioned frequently in the IBM Manuals. This would be similar if a Static
Assembler module were Called and it modified storage defined to its own
CSECT, which also renders it non-reentrant.

Thanks BK. I read this too fast initially as I was going out the door....

Bill

"shyam nivas" <nivas_shyam@indiatimes.com> wrote in message
news:c02fd744.0208280517.79feeb85@posting.google.com...
> Hi,
>                First of all sorry for putting CICS question on COBOL
…[13 more quoted lines elided]…
> Shyam
```

#### ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS. (2)

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2002-08-28T22:09:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akjvjh$bio$1@nntp9.atl.mindspring.net>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com>`

```
A correction. You don't need to place Dynamically Called modules in the LPA.
They can be placed into your normal User Load Lib.

Dynamically Called module PPT entries can be Autoinstalled or explicitly
defined.

A heads-up for Dynamically Called modules. Try to keep your WS to a minimum
as Dynamically Called modules WS is not released until Task Termination.

A heads up for Statically Called modules. If the Caller's WS is reentrant
(or as in CICS/COBOL, serially reusable), try to pass a chunk of the
Caller's WS to the Static module as a parameter, ensuring that the Static
module will not be accessing storage defined to itself, which will render it
non-reentrant and cause those ever-popular "unpredictable results" as
mentioned frequently in the IBM Manuals. This would be similar if a Static
Assembler module were Called and it modified storage defined to its own
CSECT, which also renders it non-reentrant.

Thanks BK. I read this too fast initially as I was going out the door....

Bill

"shyam nivas" <nivas_shyam@indiatimes.com> wrote in message
news:c02fd744.0208280517.79feeb85@posting.google.com...
> Hi,
>                First of all sorry for putting CICS question on COBOL
…[13 more quoted lines elided]…
> Shyam
```

#### ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS.

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-08-29T01:22:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Icib9.10639$XV.352498@news4.srv.hcvlny.cv.net>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com>`

```
shyam nivas wrote:
> Hi,
>                First of all sorry for putting CICS question on COBOL
…[9 more quoted lines elided]…
> Please reply me whether my assumptions are correct or not.

Yes on no. 1.

For no. 2, you need a PPT entry for all dynamically called programs; but 
they don't have to be (and probably shouldn't be) in the LPA. They just 
have to be in the DFHRPL concatenation for the region. They're vanilla 
application programs, no special considerations, e.g., LPA.
```

#### ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS.

- **From:** naveen.masade <naveen.masade@eds.com>
- **Date:** 2002-11-20T17:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2068475.1037811621@dbforums.com>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com>`

```

Hi

 to me , your assumptions sounds good.
  But i have not seen a CICS program using static cobol calls...
  if u have seen your assumption is true..
 please do let me know.

QUOTE]Originally posted by Shyam Nivas 
Hi,
First of all sorry for putting CICS question on COBOL
group.
My assumptions are as follows:
1. For Statically called module no PPT entry is required because
   called module is part of main routine.
2. For Dynamically called module PPT entry is required as called
   module is loaded at run time.Simultaneously we have to put called
   module in CICS linked pack area.


Please reply me whether my assumptions are correct or not.


Regards.
Shyam 
```

##### ↳ ↳ Re: PPT entry for Statically/Dynamically called subprograms in CICS.

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-20T11:49:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<argi01$ut$1@slb9.atl.mindspring.net>`
- **References:** `<c02fd744.0208280517.79feeb85@posting.google.com> <2068475.1037811621@dbforums.com>`

```
All of this is pretty well documented in

  "3.1.1.4 Calling to or from COBOL programs"

at:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/3.1.1.4

and YES you need a PPT entry for dynamically called subroutines and do NOT
need it for statically linked routines
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
