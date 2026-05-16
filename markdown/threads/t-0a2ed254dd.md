[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Bug alert Fujitsu !

_7 messages · 4 participants · 1999-05 → 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Bug alert Fujitsu !

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hs2pe$kjf$1@news.igs.net>`

```
I suspect that a bug I just discovered in Fujitsu (3 and 4) is affecting
a whole lot of people.  It is in the cbl_copy_file routine, that often gets
used
as a spool method.

The routine crashes both Windows95 and 98 if the file being copied goes
beyond
2*64 bytes.  Here is the code I have been using.  It will work fine as long
as the file named in FILENAME-IN is less than 2*64k bytes long. As soon
as the file being copied exceeds that length, it causes a machine reset.

If you are using the copy subroutine, you have a pending bug.

000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. "_NEWSPLR".
000030 AUTHOR. D. L. Tees.
000040 SECURITY.
000050     Copyright(C), 1999, DONALD L TEES.
000060 ENVIRONMENT DIVISION.
000070 CONFIGURATION SECTION.
000080 SOURCE-COMPUTER. IBM-PC.
000090 OBJECT-COMPUTER. IBM-PC.
000100 SPECIAL-NAMES.
000110 INPUT-OUTPUT SECTION.
000120 FILE-CONTROL.
000130 DATA DIVISION.
000140 FILE SECTION.
000150 WORKING-STORAGE SECTION.
000160 LINKAGE SECTION.
000170 01 FILENAME-IN       PICTURE X(40).
000180 01 PRINTER-NAME-IN   PICTURE X(40).
000190 PROCEDURE DIVISION USING FILENAME-IN PRINTER-NAME-IN.
000200 MAIN-LINE.
000210     CALL "CBL_COPY_FILE" USING
000220                          BY REFERENCE FILENAME-IN
000230                                       PRINTER-NAME-IN
000240                          END-CALL.
000250     EXIT PROGRAM.

```

#### ↳ Re: Bug alert Fujitsu !

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OVVcZRYo#GA.275@nih2naab.prod2.compuserve.com>`
- **References:** `<7hs2pe$kjf$1@news.igs.net>`

```
Just what do we mean by 2*64?  Is this a bug that we should worry about, or
a bug that will never happen in this lifetime.
```

##### ↳ ↳ Re: Bug alert Fujitsu !

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hub9t$1h9$1@news.igs.net>`
- **References:** `<7hs2pe$kjf$1@news.igs.net> <OVVcZRYo#GA.275@nih2naab.prod2.compuserve.com>`

```
I meant 2*16.  I think I am getting senile.  65,000 roughly.  It is just big
enough
that it will probably get through testing, and crash in the first real world
test.

Sorry about that.

Russell Styles wrote in message ...
>Just what do we mean by 2*64?  Is this a bug that we should worry about, or
>a bug that will never happen in this lifetime.
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Bug alert Fujitsu !

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37435c65@news3.us.ibm.net>`
- **References:** `<7hs2pe$kjf$1@news.igs.net> <OVVcZRYo#GA.275@nih2naab.prod2.compuserve.com> <7hub9t$1h9$1@news.igs.net>`

```

Donald Tees <donald@willmack.com> wrote in message
news:7hub9t$1h9$1@news.igs.net...
> I meant 2*16.  I think I am getting senile.  65,000 roughly.

Probably more like 2**16, as 2*16 = 32 only.
```

###### ↳ ↳ ↳ Re: Bug alert Fujitsu !

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i19c6$2hk$1@news.igs.net>`
- **References:** `<7hs2pe$kjf$1@news.igs.net> <OVVcZRYo#GA.275@nih2naab.prod2.compuserve.com> <7hub9t$1h9$1@news.igs.net> <37435c65@news3.us.ibm.net>`

```
Leif Svalgaard wrote in message <37435c65@news3.us.ibm.net>...
>
>Donald Tees <donald@willmack.com> wrote in message
…[4 more quoted lines elided]…
>
It is all wearing out ... brains, eyes, etc.  ... the etc. really hurts ...
```

#### ↳ Re: Bug alert Fujitsu !

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990610093016.06545.00001901@ngol01.aol.com>`
- **References:** `<7hs2pe$kjf$1@news.igs.net>`

```
In article <7hs2pe$kjf$1@news.igs.net>, "Donald Tees" <donald@willmack.com>
writes:

>I suspect that a bug I just discovered in Fujitsu (3 and 4) is affecting
>a whole lot of people.  It is in the cbl_copy_file routine, that often gets
…[8 more quoted lines elided]…
>

Not to be difficult or anything, but WHY on earth would you WANT to print
a file that is 2*64K in size?  Isn't this getting out near the 1-2G file size
limit?
My puny windows calculator (and my head) don't quite manage such a number
very easily. If a report is that large, it is usually NEVER looked at for fear
of being crushed under the weight of handling it.   Are you printing some form
of complete formatted file dump or trial balance on x million acounts?
```

##### ↳ ↳ Re: Bug alert Fujitsu !

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7joi5b$aq9$3@news.igs.net>`
- **References:** `<7hs2pe$kjf$1@news.igs.net> <19990610093016.06545.00001901@ngol01.aol.com>`

```
Sorry about that.  It was a mental glitch.  64k.  2*16. 65,536 bytes.
The classic intel overflow. Damned Mondays.

Sff5ky wrote in message <19990610093016.06545.00001901@ngol01.aol.com>...
>In article <7hs2pe$kjf$1@news.igs.net>, "Donald Tees" <donald@willmack.com>
>writes:
>
>>I suspect that a bug I just discovered in Fujitsu (3 and 4) is affecting
>>a whole lot of people.  It is in the cbl_copy_file routine, that often
gets
>>used
>>as a spool method.
…[3 more quoted lines elided]…
>>2*64 bytes.  Here is the code I have been using.  It will work fine as
long
>>as the file named in FILENAME-IN is less than 2*64k bytes long. As soon
>>as the file being copied exceeds that length, it causes a machine reset.
…[3 more quoted lines elided]…
>a file that is 2*64K in size?  Isn't this getting out near the 1-2G file
size
>limit?
>My puny windows calculator (and my head) don't quite manage such a number
>very easily. If a report is that large, it is usually NEVER looked at for
fear
>of being crushed under the weight of handling it.   Are you printing some
form
>of complete formatted file dump or trial balance on x million acounts?
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
