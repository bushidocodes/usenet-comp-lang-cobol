[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL for MVS - using LIBEXIT

_3 messages · 2 participants · 1998-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL for MVS - using LIBEXIT

- **From:** brixford@my-dejanews.com
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ub7jd$oj7$1@nnrp1.dejanews.com>`

```
I am trying to use the LIBEXIT in COBOL for MVS (or COBOL II for that matter)
to filter the copybooks before compilation.  I am getting a very fatal Cobol
error when I pass the record back thru the linkage.  I am passing the length,
returncode and am 80 byte buffer but the compile burps and terminates.  I can
call the exit and not pass back a buffer and the base program will compile.
The IBM example shows a SYSIN exit and I copied that code BUT it does not work
on the LIBEXIT.

Clues???

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: COBOL for MVS - using LIBEXIT

- **From:** skyraven@home.com (Sue L. )
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360bb620.14528365@news>`
- **References:** `<6ub7jd$oj7$1@nnrp1.dejanews.com>`

```
>The IBM example shows a SYSIN exit and I copied that code BUT it does not work
>on the LIBEXIT.

You have a SYSIN... do you have a SYSOUT on there as well?? 

I know it's a dumb question but I have to ask....if not that could
very well be your problem...
```

##### ↳ ↳ Re: COBOL for MVS - using LIBEXIT

- **From:** brixford@my-dejanews.com
- **Date:** 1998-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uhr5k$nlq$1@nnrp1.dejanews.com>`
- **References:** `<6ub7jd$oj7$1@nnrp1.dejanews.com> <360bb620.14528365@news>`

```
I could  have been a little vague.  The SYSIN I was referring to was the
replacement code for the SYSIN reader that is supplied with the complier. 
The LIBEXIT is an EXITstub that will replace the code that the compiler uses
to read copy books (expanding COPY CPYBOOK staements by reading the PDS) with
your own reader.  The sample code from IBM shows only the code to replace the
SYSIN reader and not the Copybook reader.

On MVS, THE exit can be invoked via:
//GOSTEP EXEC PGM=IGYCRCTL,REGION=2M,COND=(5,LT),
//       PARM='EXIT(LIBEXIT(''SRT2'',BPAM))'

where BPAM is the program to exec to read the copybooks.  I was going to use
the exit to filter, on the fly, copybook source. But it will take a superior
programmer than I.

PS. Librarian systems(PANVALET, LIBRARIAN, CHANGEMAN) use this exit.


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
