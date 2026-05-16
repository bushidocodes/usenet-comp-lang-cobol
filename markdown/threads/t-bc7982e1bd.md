[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling an assembler (non-CICS) program from a CICS Cobol program

_4 messages · 3 participants · 2003-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Calling an assembler (non-CICS) program from a CICS Cobol program

- **From:** jacques_dilbert@hotmail.com (Jacques Dilbert)
- **Date:** 2003-09-09T12:40:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a9000c2.0309091140.1f65f9b8@posting.google.com>`

```
Is it true that a CICS Cobol program can dynamically call
a non-CICS program (mine is in assembler), provided that 
it has a PPT entry ?
I have sub-programs (non-CICS) used in both Batch and CICS, 
and I would like to have the same load-module usable
in both environments.
```

#### ↳ Re: Calling an assembler (non-CICS) program from a CICS Cobol program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-09T20:18:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Zzq7b.2677$c35.526@newsread1.news.atl.earthlink.net>`
- **References:** `<5a9000c2.0309091140.1f65f9b8@posting.google.com>`

```
See:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA4110/15.1.4.1

for what is and is not allowed for COBOL/Assembler ILC under CICS.

For other language considerations, see:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA4110/15.0

For PPT requirements, see:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/3.1.1.4
```

##### ↳ ↳ Re: Calling an assembler (non-CICS) program from a CICS Cobol program

- **From:** jacques_dilbert@hotmail.com (Jacques Dilbert)
- **Date:** 2003-09-09T22:25:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a9000c2.0309092125.16af7a88@posting.google.com>`
- **References:** `<5a9000c2.0309091140.1f65f9b8@posting.google.com> <Zzq7b.2677$c35.526@newsread1.news.atl.earthlink.net>`

```
"William M. Klein"  wrote 
> 
> For PPT requirements, see:
>  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/3.1.1.4
> 

From this link I understand that non-CICS sub-programs 
can be used in both Batch and CICS, provided a PPT entry
has been created for them (with the proper LANG(...) option).
This is exactly what I needed.
```

###### ↳ ↳ ↳ Re: Calling an assembler (non-CICS) program from a CICS Cobol program

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-09-10T21:20:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-740228.21201310092003@corp.supernews.com>`
- **References:** `<5a9000c2.0309091140.1f65f9b8@posting.google.com> <Zzq7b.2677$c35.526@newsread1.news.atl.earthlink.net> <5a9000c2.0309092125.16af7a88@posting.google.com>`

```
In article <5a9000c2.0309092125.16af7a88@posting.google.com>,
 jacques_dilbert@hotmail.com (Jacques Dilbert) wrote:

> "William M. Klein"  wrote 
> > 
…[7 more quoted lines elided]…
> This is exactly what I needed.

Depending on your CICS version you might not need a PPT entry.  The will 
be dynamically created for you in everything after (?)v4.1, or maybe 
TSv1.2.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
