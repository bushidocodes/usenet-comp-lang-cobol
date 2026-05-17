[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Stupid JCL tricks

_3 messages · 3 participants · 1995-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Stupid JCL tricks

- **From:** "hcm..." <ua-author-17087505@usenetarchives.gap>
- **Date:** 1995-09-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00001a84+00000810@msn.com>`

```
Hello:
Today I tripped on a JCL problem. It seems that
in IBM COBOL, the blocksize is taken from JCL or the
dataset usually, but if a jes2 parm overides the
output, the block size is ignored. So, be careful.
Make sure if your FD looks like this:
FD GERBILS-FILE
BLOCK CONTAINS 0 RECORDS
RECORD CONTAINS 80 CHARACTERS.
01 GERBILS-RECORD PIC X(80).

AND
your JCL has somethin' like this:
/*OUTPUT FORM=(1313)

And your dd statement refers to it somehow...

//Gerbils DD sysout=(M,,1313),
// DCB=(lrecl=80, blksize=100,recfm=fba)

note the bad block is IGNORED as long as the /*OUTPUT
JES2 (or is it 3, tee hee...) is used.
Take it off, and it is SOC4 city!!!!

The fix is to make sure your block size is a integer
multiple of the LRECL...(record length)

Regards,
The unknown cobol programmer,
now using Microsoft Network. Long Live Windows95
AND MVS...
```

#### ↳ Re: Stupid JCL tricks

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-09-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-52ac2f7cb8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<00001a84+00000810@msn.com>`
- **References:** `<00001a84+00000810@msn.com>`

```
FYI - related to FDs vs JCL (vs label if dealing with INPUT file
rather than output).

A couple things that you should know -

OS/VS COBOL works differently than VS COBOL II and COBOL for MVS
& VM (which work the same).

There are a number of IBM APARs which have changed how things
work when the DCB doesn't match the FD. If you need APAR
reference numbers, let me know.

File-Status 39 "is your friend". If you are using an MVS
compilebr that supports the NOCMPR2 (ANS'85) compiler option, get
used to checking for a file-status 39 which is what happens when
you don't get your JCL to match your program which must match the
file's "internal" label.
```

#### ↳ Re: Stupid JCL tricks

- **From:** "garyb..." <ua-author-17088195@usenetarchives.gap>
- **Date:** 1995-09-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-52ac2f7cb8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<00001a84+00000810@msn.com>`
- **References:** `<00001a84+00000810@msn.com>`

```
Another new trick that I have been using for the last couple of years in
JCL...

An undocumented feature of the JCL 'IF Then/Else" code.

you can specify a symbolic parameter with a value of either 'TRUE' or
'FALSE'. One use of this is to allow you to toggle proc steps at
execution time from the job. For instance I set up compile JCL/Procs so
that I can select linkedit, debugger support etc.

For example, here is a view of my linkedit step from the proc and some of
the supporting symbolic definitions.

//cmplonl PROC PRCLASS='*',
// DEVL='TRUE',
// LKED='TRUE',
// LLLVL4=P,
// MEMBER=TEMPNAME
....
//DOWELKED IF ((COB.RC < 8) & &LKED) THEN
(email note ie DO WE LinKEDit)
//*####################################################################
//* LINKAGE EDITOR
//*####################################################################
//LKED EXEC PGM=IEWL,REGION=1M,
// PARM='LIST,&LKW,&XMODE,MAP,SIZE=(999K,180K)'
//SYSLIB DD DISP=S. . .
...
//SYSUT1 DD UNIT=SYSDA,SPACE=(CYL,(5,5))
//SYSLIN DD DSN=&&OBJECT,DISP=(OLD,DELETE)
//DOWELKED ENDIF

Calling this proc with no overrides would cause the if stmt to be
translated to if ((COB.RC < 8) & TRUE) and assuming you had a clean
compile... the step LKED would execute. To cause this same proc to not
linkedit, simply override the LKED symbolic to LKED=FALSE.

I use this a lot for debug compile tools (ie xpeditor, intertest etc.) I
define the PROC with both Xpeditor and non-xpeditor steps and then use
symbolic XPED to rout me done the correct path. Be creative

Enjoy.
Gary Butler
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
