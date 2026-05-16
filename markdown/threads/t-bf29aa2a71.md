[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: IBM specific question

_2 messages · 2 participants · 2000-06_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: IBM specific question

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<642A954DD517D411B20C00508BCF23B00127A3AC@mail.sauder.com>`

```
Does anyone know of a method/utility/product that can scan a loadlib
and report on the content of the PDS?  This utility also needs to be able
to locate and report the compile date of each member.

Other items that might be useful information would be the internal 'Program
Name'
and identify the primary compile language (PL/1, COBOL, C, ASM, .....)

I have already collected a sample from this newsgroup that is able to 
get the member names of a PDS.   The next piece that I am looking for in
particular is for the ability to change the DSN name associated to a DDname
so that the program can open and read each of the members to get the 
internal details for reporting.  

Any help/pointers to OS\390 manuals would be greatly appreciated.
I would need the Manual Titles in order to find the same documents 
on my set of reference CDs.   

Thanks in advance for all your help.
```

#### ↳ Re: OT: IBM specific question

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394E1C95.29A80844@cusys.edu>`
- **References:** `<642A954DD517D411B20C00508BCF23B00127A3AC@mail.sauder.com>`

```


Sff5ky wrote:
> 
> Does anyone know of a method/utility/product that can scan a loadlib
> and report on the content of the PDS?  This utility also needs to be able
> to locate and report the compile date of each member.
 
This might be overkill:
//ZHBAMBST   JOB (24981,'NON-ENDEVOR DC COBOL/MVS'),
//             'U56,H BRAZEE',
//             MSGCLASS=W,CLASS=N,    WHITE PAPER
//             NOTIFY=D44201
/*ROUTE PRINT R0010
//******** LOOK AT LOAD MODULE ***************
//STEP1    EXEC PGM=AMBLIST
//SYSLIB   DD DISP=SHR,DSN=UMS.TEST.LOAD
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
 LISTIDR
//
 LISTIDR MEMBER=SIPR702
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
