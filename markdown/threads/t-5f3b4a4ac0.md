[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Restore from corrupted ibm cobol/2 .dat file

_1 message · 1 participant · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Restore from corrupted ibm cobol/2 .dat file

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3835E773.CECE8378@siber.com>`
- **References:** `<fycvU7zT9Qru-pn2-jmr0i467keR7@localhost> <3834E5A2.67416C4A@siber.com> <fycvU7zT9Qru-pn2-vxZ12UDfXC5D@localhost>`

```
Gregor Stuebner wrote:
> 
> > So you can use mfdata2flat from http://www.siber.com/datafile/
…[7 more quoted lines elided]…
> incorrectly.

Soory, my mistake. The correct URL is:

http://www.siber.com/sct/datafile/

> 
> Anyway - that program could solve my problem.
> Where can i get information about the internal structure of a .DAT
> file?

You need to have a source of any Cobol program that can
read or write this file. I understand that you have it.

You let this source go thru cbl2fdd program that extracts
all file definitions (SELECT and FD statements) and
puts them into FDD and RDD files (our own proprietary text format)
that basically encode the file and record structure.

Then you use any of the DataFile readers, such as 
mfdata2flat, mfdata2dbf, or mfdata2cr to convert
the data from data file to your favorite format.

Hope this helps.

Regards,
Vadim Maslov
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
