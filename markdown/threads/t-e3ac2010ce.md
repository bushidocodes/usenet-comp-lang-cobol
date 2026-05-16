[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Restore from corrupted ibm cobol/2 .dat file

_2 messages · 2 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Restore from corrupted ibm cobol/2 .dat file

- **From:** gstueb@okay.net (Gregor Stuebner)
- **Date:** 1999-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fycvU7zT9Qru-pn2-jmr0i467keR7@localhost>`

```
Hello,
 
i have a indexed file which is saved in two files called "file.dat"  
and "file.idx". The "file.idx" is corrupted.
 
How can i read the "file.dat" sequential, i.e. without reading the 
corrupted "file.idx"? The shipped rebuild.cbl program doesn't work 
(Runtime Error 13). 
 
The used compiler (DOS) is: 
 
IBM COBOL/2
Version 1.00   (C)Copyright IBM Corporation 1985, 1987, 1988
               (C)Copyright Micro Focus Ltd. 1985, 1988
 
any ideas?
Gregor
```

#### ↳ Re: Restore from corrupted ibm cobol/2 .dat file

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3834E5A2.67416C4A@siber.com>`
- **References:** `<fycvU7zT9Qru-pn2-jmr0i467keR7@localhost>`

```
Gregor Stuebner wrote:
> 
> Hello,
…[12 more quoted lines elided]…
>                (C)Copyright Micro Focus Ltd. 1985, 1988


Looks like you are using an old MF compiler that was licensed
to IBM for some reason (never heard about this before).

We have a datafile reader for MF files that uses only
*.dat file and not *.idx file (cannot do indices yet).

So you can use mfdata2flat from http://www.siber.com/datafile/
to convert your file to comma-separated text values
and then read them back in with Cobol program.

Or go straight to a big database.

Regards,
Vadim Maslov
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
