[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# QSAM file

_3 messages · 3 participants · 1995-12_

---

### QSAM file

- **From:** "thomas fonseca" <ua-author-8626956@usenetarchives.gap>
- **Date:** 1995-12-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49tmsg$8gt@ultra.sonic.net>`

```
I wrote a program that reads a file on a tape (or multiple tapes). When
I run the program, it abends because the blocksize is not a multiple of
the record length. The blocksize is something large like 26,390 and the
record length is 900 bytes. I have no control over the blocksize, do I?
That is how it was set up, and not by me. I'm also having problems
trying to access this file randomly. (Access is dynamic)

What I've done out of panic is to copy the file in temporary storage
using JCL and syncsort. But that does not solve my problems. HELP.
```

#### ↳ Re: QSAM file

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-12-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bcde15c32-p2@usenetarchives.gap>`
- **In-Reply-To:** `<49tmsg$8gt@ultra.sonic.net>`
- **References:** `<49tmsg$8gt@ultra.sonic.net>`

```
Hello Thomas:
There seems to be a couple problems with your tape:

1. You can only read a file on a tape sequentially, not dynamically.

2. Is your input a (ugh!) variable length record?
DCB=(RECFM=VB)
Sometimes the variable length record has leading comp fields that
have the length of the block and the length of the records in question.
Yuck!

The only other thing I can think of is that the file could be an image
of a VSAM keyed file, and then you would use the repro command of the
idcams utility to restore the image back to VSAM from the tape.

Are you sure you have been told the right file record length and
type? Try using Iebgener to copy the tape to a disk file to
look at the data using ISPF PDF browse.

Here are the steps I would go through:
1. Try to find out the real length/type of the tape dataset.
A. Use a utility that reads the tape label to find out the
dataset name, lrecl, blksize.
B. Dump the tape to disk and look at it thru an editor.
Use iefbr14 and jcl to allocate datasets, or ISPF 3.2 to allocate the
disk dataset. Get someone to mount the tape and use Iebgener to
copy the tape to disk.

//step01 exec pgm=iebgener
//sysut1 dsn=mytape.name,disp=(old,pass)
//sysut2 dsn=mydisk.data,disp=shr
//sysin dd dummy
//


Good luck...

Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

#### ↳ Re: QSAM file

- **From:** "david_..." <ua-author-3348436@usenetarchives.gap>
- **Date:** 1995-12-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bcde15c32-p3@usenetarchives.gap>`
- **In-Reply-To:** `<49tmsg$8gt@ultra.sonic.net>`
- **References:** `<49tmsg$8gt@ultra.sonic.net>`

```
In article <49tmsg$8.··.@ult··c.net>, tho··.@so··c.net says...
› 
› I wrote a program that reads a file on a tape (or multiple tapes).  When 
…[8 more quoted lines elided]…
› 
In a cobol program you specify block contains ? on the FD statement to
control block size. You must code 'block contains 0' on the FD to let the
block size be taken from an existing file label or jcl statement (otherwise
the default is block contains 1 record). What is specified or defaulted in
program is used before anything else, if program has block contains 0, then
what is coded in jcl is used, and if nothing is in jcl, then what is in vtoc
or tape label (for existing file) is picked up.

Dynamic can not be used for a qsam file only sequential.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
