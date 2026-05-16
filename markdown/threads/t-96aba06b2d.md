[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM COBOL 6: Data extraction help request!

_4 messages · 4 participants · 1999-08 → 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM COBOL 6: Data extraction help request!

- **From:** "PHead" <jhutter@bellsouth.net>
- **Date:** 1999-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jONx3.8669$7d2.41929@news4.atl>`

```
I need to know if there is some program out there to convert RM Cobol 6
index and relative files to a flat file?  Please email me with response.

Thanks
```

#### ↳ Re: RM COBOL 6: Data extraction help request!

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-08-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z4by3.2367$z85.53417@dfiatx1-snr1.gtei.net>`
- **References:** `<jONx3.8669$7d2.41929@news4.atl>`

```
PHead wrote in message ...
>I need to know if there is some program out there to convert RM Cobol 6
>index and relative files to a flat file?  Please email me with response.


Yes. You need an RM COBOL compiler and the File Description of the files.
Then you write a program to read your files and rewrite the data as a "flat"
(whatever that means: sequential, non-keyed, non-indexed?) file.

Otherwise, you get to hunt through the *.dat files, attempting to figure out
what's in them and divining how they are laid out. This is not easy.
Assuming you get this far, now you write a program to read what's in there,
and write it out to a "flat" file. This part, too, is not not easy.

Better you should use the RM COBOL product to reformat the data. Much
easier.

MCM
```

#### ↳ Re: RM COBOL 6: Data extraction help request!

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C9DE47.EE68A4FB@siber.com>`
- **References:** `<jONx3.8669$7d2.41929@news4.atl>`

```
PHead wrote:
> 
> I need to know if there is some program out there to convert RM Cobol 6
> index and relative files to a flat file?  Please email me with response.
> 
> Thanks

Dear PHead,

Our data2flat converter http://www.siber.com/sct/datafile/
can read MF and FSC data files. We have not tried it on 
RM index files yet, but it might work for RM sequential files. 

If you send your files and the program to us 
at info@siber.com, we can try to read your data.
Our experiences shows that we can usually figure out
how to read a new format fairly quickly.

Regards,
Vadim Maslov
```

#### ↳ Re: RM COBOL 6: Data extraction help request!

- **From:** Brian <brian@ciphersys.com>
- **Date:** 1999-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7kC3.1882$Y6.219911@news1.telusplanet.net>`
- **References:** `<jONx3.8669$7d2.41929@news4.atl>`

```
We have a package that can do EXACTLY this task.  It is called Companion 
and is described (in part at least) at www.ciphersys.com  It is writen in 
and runs on any RMCOBOL supporting machine, or we can do the file 
conversion for you.

Contact Graham Kinmond at 800 661 9961 for more information.

PHead <jhutter@bellsouth.net> wrote in <jONx3.8669$7d2.41929@news4.atl>:

> I need to know if there is some program out there to convert RM Cobol 6
> index and relative files to a flat file?  Please email me with response.
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
