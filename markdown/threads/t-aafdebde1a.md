[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VSAM file from Mainframe to PC

_5 messages · 5 participants · 1998-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`VSAM, files, sorting`](../topics.md#files)

---

### VSAM file from Mainframe to PC

- **From:** "sbouc..." <ua-author-16821643@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980125181500.NAA08042@ladder02.news.aol.com>`

```

We use small KSDS and ESDS files(about 20 records) in our COBOL class but I
would like to get these files on my PC so I may use them with my Microfocus
compiler so I can complete my assignments without travelling to the computer
lab..

The files were created using IDCAMS and reside on an IBM S/370 DOS/VSE
Mainframe. Is this possible? Also, anyone with thoughts using this type of
setup with Microfocus are welcome. I am just learning and welcome any and all
suggestions.
```

#### ↳ Re: VSAM file from Mainframe to PC

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafdebde1a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980125181500.NAA08042@ladder02.news.aol.com>`
- **References:** `<19980125181500.NAA08042@ladder02.news.aol.com>`

```

SBouc16898 wrote:
› 
› We use small KSDS and ESDS files(about 20 records) in our COBOL class but I
…[7 more quoted lines elided]…
› suggestions.

Find someone who knows how to REPRO them into flatfiles and then
IND$FILE them to a diskette in ASCII... that'll give them to you in
sequential format and you'll have to rebuild them into indexed on your
PC.

DD
```

##### ↳ ↳ Re: VSAM file from Mainframe to PC

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafdebde1a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aafdebde1a-p2@usenetarchives.gap>`
- **References:** `<19980125181500.NAA08042@ladder02.news.aol.com> <gap-aafdebde1a-p2@usenetarchives.gap>`

```


The Goobers wrote in message <34C··.@er··s.com>...
› SBouc16898 wrote:
›› 
…[20 more quoted lines elided]…
› DD

However, watch out if the files have any COMP, COMP-3 (binary or packed)
fields in them. If they do, you will need an "intelligent" down-load
program. If you happen to know anyone who has the full Micro Focus
Workbench, there are tools to do this easily. (Workbench also lets you work
in EBCDIC on the PC easily - this can be done with just the compiler - but
it takes more effort.) Don't let me discourage you from your plan - for
most class work, this should make your life a lot easier.
```

#### ↳ Re: VSAM file from Mainframe to PC

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafdebde1a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19980125181500.NAA08042@ladder02.news.aol.com>`
- **References:** `<19980125181500.NAA08042@ladder02.news.aol.com>`

```

On 25 Jan 1998 18:15:55 GMT, sbo··.@a··.com (SBouc16898) wrote:


› The files were created using IDCAMS and reside on an IBM S/370 DOS/VSE
› Mainframe.  Is this possible?  Also, anyone with thoughts using this type of
› setup with Microfocus are welcome.  I am just learning and welcome any and all
› suggestions.


See if you have access to the host transfer facility, and the
associated PC recieve programs (probably built into your emulation
software if you login with a PC). Then move the VSAM file to the host
transfer. Then recieve it, using BINARY. Then, get the FD. Make a
program on the PC with that FD. Then use the WFL in MicroFocus to
convert the EBCDIC file to ASCII indexed file.
```

#### ↳ Re: VSAM file from Mainframe to PC

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aafdebde1a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19980125181500.NAA08042@ladder02.news.aol.com>`
- **References:** `<19980125181500.NAA08042@ladder02.news.aol.com>`

```

SBouc16898 wrote:
› 
› We use small KSDS and ESDS files(about 20 records) in our COBOL class but I
…[7 more quoted lines elided]…
› suggestions.

If for only 20 records. I would rather create it again my own on my PC.

Rgds,
Chip Ling
chi··.@sym··o.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
