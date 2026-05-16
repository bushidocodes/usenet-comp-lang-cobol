[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic allocation of memory

_7 messages · 5 participants · 2000-04_

---

### Dynamic allocation of memory

- **From:** Harish Murthy <worm@NOSPAM.thewatercooler.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com>`

```
Hi,
How cud I possibly have dynamic allocation of memory done in COBOL ??
Something similiar to alloc()/malloc() of C ??
The main problem is that the buffer size is known only at run time and
may exceed
the size mentioned in the OCCURS.
Thanks + Rgds
Harish
```

#### ↳ Re: Dynamic allocation of memory

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O3bnE67o$GA.361@cpmsnbbsa04>`
- **References:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com>`

```
What platform are you working on?
Which compiler are you using? (please include release)

ODO (Occurs Depending On) may be an option.

Harish Murthy <worm@NOSPAM.thewatercooler.com> wrote in message
news:38F32042.5E5556F2@NOSPAM.thewatercooler.com...
> Hi,
> How cud I possibly have dynamic allocation of memory done in COBOL
??
> Something similiar to alloc()/malloc() of C ??
> The main problem is that the buffer size is known only at run time
and
> may exceed
> the size mentioned in the OCCURS.
> Thanks + Rgds
> Harish
>
```

##### ↳ ↳ Re: Dynamic allocation of memory

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05595718.f586d24c@usw-ex0105-037.remarq.com>`
- **References:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com> <O3bnE67o$GA.361@cpmsnbbsa04>`

```
If you are using NetExpress, the library routines CBL_ALLOC_MEM
and CBL_FREE_MEM can be used to dyamically allocate memory. The
minimum allocated memory is 8K.

Rich

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Dynamic allocation of memory

- **From:** "Searcher" <mangogwr@bellsouth.net>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3HPI4.485$t13.406@news4.mia>`
- **References:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com>`

```
You woul need a 'C' or 'Assembler' subroutine to allocate the memory.
HOWEVER, what you are stating really dones NOT make sense.

Do you mean that 'sometimes, in a file of VARIABLE-LENGTH BLOCKED records'
the actual Blocksize is GREATER than that calculated for the FD'?

That can be handled by using
(O L D)
FD SOMEFILE
       RECORD CONTAINS 50 TO 250 CHARACTERS
       BLOCK CONTAINS 4 RECORDS.
(==> calculates a Blocksize of 1020 Characters (250 * 4 + ( 4bytes * 4
records) + 4 bytes for block)
FD SOMEFILE
       RECORD CONTAINS 50 TO 250 CHARACTERS
       BLOCK CONTAINS 620 CHARACTERS.
(==> 2 * 50 + 2 * 250 = 100 + 500 = 600 + ( 4 * 4bytes + 4 bytes)

If the file was created in method 1 ( O L D )
and read in method 2, then you will get a buffer that is larger than
calculated.


Harish Murthy <worm@NOSPAM.thewatercooler.com> wrote in message
news:38F32042.5E5556F2@NOSPAM.thewatercooler.com...
> Hi,
> How cud I possibly have dynamic allocation of memory done in COBOL ??
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Dynamic allocation of memory

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d238f$nml$1@newssrv.otenet.gr>`
- **References:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com>`

```
Hi,
If you are using NetExpress have a look at 'malloc' and 'dealloc' methods
available in the BASE class. These methods are equivalent to malloc and
calloc functions of C.

Costas

Harish Murthy <worm@NOSPAM.thewatercooler.com> wrote in message
news:38F32042.5E5556F2@NOSPAM.thewatercooler.com...
> Hi,
> How cud I possibly have dynamic allocation of memory done in COBOL ??
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Dynamic allocation of memory

- **From:** Harish Murthy <worm@NOSPAM.thewatercooler.com>
- **Date:** 2000-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F595A0.B7BD32DF@NOSPAM.thewatercooler.com>`
- **References:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com> <8d238f$nml$1@newssrv.otenet.gr>`

```
Hi Costas,
Im using MicroFocus COBOL and no object oriented stuff.
Wud like to do it in plain old COBOL...
Efharisto,
Harish

Costas Giannoulis wrote:

> Hi,
> If you are using NetExpress have a look at 'malloc' and 'dealloc' methods
…[15 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Dynamic allocation of memory

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<08f36484.c7245296@usw-ex0105-037.remarq.com>`
- **References:** `<38F32042.5E5556F2@NOSPAM.thewatercooler.com> <8d238f$nml$1@newssrv.otenet.gr> <38F595A0.B7BD32DF@NOSPAM.thewatercooler.com>`

```
Harish,

Did you see my response early in the thread? I will give you an
example now on how to use the library routines to allocate and
free memory using NetExpress.

--------- Start of code --------------
.
.
working-storage section.
01 mem-ptr usage pointer.
01 mem-size pic x(04) comp-5.
01 mem-flags pic x(04) comp-5.
.
.
linkage section.
01 table-area.
05 ta-entries occurs 4096 times.
10 ta-data pic x(256).
.
.
procedure division.
.
.
move zeros to mem-flags
*> compute mem-size
move length of table-area to mem-size
if mem-size < 8192
move 8192 to mem-size
end-if

call 'CBL_ALLOC_MEM' using mem-ptr
by value mem-size mem-flags

set address of table-area to mem-ptr
*> now you have the memory assigned to the table. Note, table-
area is in the linkage section
*> now do all of your processing and when done, you should free
memory

call 'CBL_FREE_MEM' using by value mem-ptr
stop run
.
------------- End of code ----------------

Regards,
Rich

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
