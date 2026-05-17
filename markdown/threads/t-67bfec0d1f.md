[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Workbench: How To UPLOAD IMS Database From PC To IBM/MVS?

_3 messages · 3 participants · 1995-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### Cobol Workbench: How To UPLOAD IMS Database From PC To IBM/MVS?

- **From:** "vinh duong" <ua-author-13551843@usenetarchives.gap>
- **Date:** 1995-11-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48rfl1$h0d@news.worldlinx.com>`

```
Hi,

Does anybody know how to UPLOAD Micro-Focus' IMS Database produced by
IMSVS86 from PC to IBM mainframe (MVS).

Micro Focus release: 3.1

Thanks

Vinh
Montreal
```

#### ↳ Re: Cobol Workbench: How To UPLOAD IMS Database From PC To IBM/MVS?

- **From:** "c82..." <ua-author-13525796@usenetarchives.gap>
- **Date:** 1995-11-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-67bfec0d1f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<48rfl1$h0d@news.worldlinx.com>`
- **References:** `<48rfl1$h0d@news.worldlinx.com>`

```
Vinh Duong (vdu··.@a··.ca) wrote:
› Hi,
 
› Does anybody know how to UPLOAD Micro-Focus' IMS Database produced by
› IMSVS86 from PC to IBM mainframe (MVS).

I'd like to know this too - and also how to do the opposite, download an IMS
database from a mainframe and use it in MicroFocus IMS. I have read (and tried)
the methods described in the manuals but don't get very far.

Thanks
Matt
```

#### ↳ Re: Cobol Workbench: How To UPLOAD IMS Database From PC To IBM/MVS?

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-11-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-67bfec0d1f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<48rfl1$h0d@news.worldlinx.com>`
- **References:** `<48rfl1$h0d@news.worldlinx.com>`

```
I remember when I worked with IMS on the PC and IMS on the Mainframe.
Stingray IMS came with a COBOL program source file that could be used
as a utility to read IMS segments on the Mainframe. The way I got it
to work was to transfer the source code to the Mainframe, run it to
extract various IMS records (segments) into a file. The utility would
place the IMS segment name in the output. A related utility on the
PC would take this data as input and load the IMS on the PC.

Another way to do this is to dump the IMS data into a flat file
and use the DLT0 like BMP program that comes with the PC.

When all else fails, you can write a COBOL program on the mainframe
side to dump IMS data to a sequential file(s) and then write an
IMS load or insert program on the PC side.

The data can be transfered from either platform using ftp or
send/receive irma board stuff.

Watch out for ASCII/versus EBCDIC gotchas.

Transfer comp or comp-3 fields as display with trailing seperate sign
fields.

Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
