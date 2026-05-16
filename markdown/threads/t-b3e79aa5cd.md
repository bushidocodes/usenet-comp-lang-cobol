[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL language on OS/390 and LBI

_4 messages · 4 participants · 2002-01 → 2002-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL language on OS/390 and LBI

- **From:** billlalonde@rocketmail.com (Bill)
- **Date:** 2002-01-15T08:37:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<28b8d30e.0201150837.6e621019@posting.google.com>`

```
I've encountered a bit of a interface challenge in COBOL on OS/390.
I found that COBOL has support for LBI (tape block sizes > 32760).
As far as I know so far, this support has not turned up in other high
level languages. I thought that RECORDING MODE IS U would provide a
useful tool for looking at tape datasets using LBI. However, because
of language coding peculiarities, when you work with this type of file
in COBOL, you need to specify the block size as the record length:
   RECORD VARYING FROM 1 TO 32760 DEPENDING ON BLOCK-LEN
would return the size of the output block. If you want to look at
bigger blocks than 32760, you can (for the moment at least) code a
larger maximum value. Note that COBOL won't be able to return the
whole block because a record can't be longer than 32760, but you can
at least find out the actual block size.

The problem is that COBOL compares the maximum value in the RECORD
VARYING clause to the LRECL of the file even though for RECORDING MODE
IS U these values actually relate to the blocksize. So, unless the
input LRECL=0, since you can't specify an LRECL > 32760 in JCL, you
can't open a file using RECORDING MODE IS U if the block size is >
32760. Well, actually you can, but then COBOL will tell you that all
the blocks are less than or equal to the maximum value in the RECORD
VARYING clause, which some folks might consider a data integrity
issue.

All this to say, does anyone out there have any creative suggestions
for making this work in this somewhat wacky environment?
Alternatively, is there any support out there for asking for a
rethinking of the rules for RECORDING MODE IS U?
```

#### ↳ Re: COBOL language on OS/390 and LBI

- **From:** Don Devlin <dondev1@attbi.com>
- **Date:** 2002-01-30T05:13:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C5780F0.7030701@attbi.com>`
- **References:** `<28b8d30e.0201150837.6e621019@posting.google.com>`

```
You might try having an assembler program do your I/O against the 
   file in locate mode and then pass the address of the buffer 
containing the complete block back to the COBOL program fro 
whatever processing you need to accomplish.  The maximum block 
size will be 64K.

Bill wrote:

> I've encountered a bit of a interface challenge in COBOL on OS/390.
> I found that COBOL has support for LBI (tape block sizes > 32760).
…[26 more quoted lines elided]…
>
```

#### ↳ Re: COBOL language on OS/390 and LBI

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-01-30T21:31:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0201302131.3a08d31b@posting.google.com>`
- **References:** `<28b8d30e.0201150837.6e621019@posting.google.com>`

```
Hi Bill,

You may want to look at Enterprise COBOL for z/OS and OS/390 V3R1
Programming Guide - SC27-1412-00, Section 1.9.1.2.3 - Taking advantage
of LBI. You may be running into hw/sw support level problems.

HTH, Jack.

billlalonde@rocketmail.com (Bill) wrote in message news:<28b8d30e.0201150837.6e621019@posting.google.com>...
> I've encountered a bit of a interface challenge in COBOL on OS/390.
> I found that COBOL has support for LBI (tape block sizes > 32760).
…[25 more quoted lines elided]…
> rethinking of the rules for RECORDING MODE IS U?
```

##### ↳ ↳ Re: COBOL language on OS/390 and LBI

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2002-02-01T01:47:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C59F387.B660A690@istar.ca>`
- **References:** `<28b8d30e.0201150837.6e621019@posting.google.com> <8a2d426e.0201302131.3a08d31b@posting.google.com>`

```
The problem is the maximum record length.  While COBOL can handle the
large block size, It is restricted to 32k for record length.

Jack Sleight wrote:
> 
> Hi Bill,
…[35 more quoted lines elided]…
> > rethinking of the rules for RECORDING MODE IS U?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
