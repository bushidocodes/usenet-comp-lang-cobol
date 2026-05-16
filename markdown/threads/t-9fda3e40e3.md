[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating INDEXED File fails Help Required

_4 messages · 2 participants · 2002-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Creating INDEXED File fails Help Required

- **From:** "Mark Miles" <milesfam@idirect.com>
- **Date:** 2002-02-18T21:21:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u73dmkn2cg8l16@corp.supernews.com>`

```
I am not a skilled Cobol program but know enough to perform simple tasks, I
have been using Microsoft COBOL Ver 4.5, old I know.

My problem is that I can Read and Write Sequential files OK but when I try
to amend a probgram I download to convert EBCIDC to ASCII (ZAP003C1) I get
an error
"Load failure (173) on file C:\DATA\COBOL\BINR\EXTERNL"

Thinking that I made a mistake, I tried the sample program that created an
indexed file and it too produced the error. (see sample below)

I have also tried using Fujitsu Cobol V3 but I'm obviuosly doing something
wrong there as I can not get any of there samples to work.

I will consider another compiler if required, just point me in the right
direction.

I'm running my Cobol 4.5 on Win 98, Win NT 4.0 and Win XP Pro.

Compile Command is : COBOL EXTFILE.CBL
Link Command is : LINK
EXTFILE+ADIS+ADISKEY+ADISINIT/NOD,,,COBfp87d+COBAPI+COBLIB;

Thanks

Mark

      $set ans85 mf noosvs
      ************************************************************
      *                                                          *
      *              (C) Micro Focus Ltd. 1989                   *
      *                                                          *
      *                     EXTFILE.CBL                          *
      *                                                          *
      *    This program demonstrates how to use EXTERNAL files.  *
      *    It calls WRITEFIL to write some records to a data     *
      *    file and READFILE to read the same records back       *
      *    (without opening or closing the file between calls).  *
      *    READFILE displays the output.                         *
      *                                                          *
      ************************************************************
       identification division.
       program-id. extfile.
       environment division.
       input-output section.
       file-control.
           select finfile assign to "isamfil.dat"
               organization is indexed
               record key is fd-tran-date
               access mode is dynamic.

       file section.
       fd finfile
          is external
          record contains 50 characters.
       01 fd-finfile-record.
           05 fd-tran-date     pic x(4).
           05 fd-with-or-dep   pic x(2).
           05 fd-amount        pic 9(5)v99.


       procedure division.
       main-line.
           perform open-file
           perform write-to-the-file
           perform start-file
           perform read-the-file
           perform close-file
           stop run.

       open-file.
           open i-o finfile.

       start-file.
           move 1111 to fd-tran-date
           start finfile key = fd-tran-date.

       write-to-the-file.
           call "writefil".

       read-the-file.
           call "readfile".

       close-file.
           close finfile.
       end program extfile.
      ************************************************************
       identification division.
       program-id. readfile.
       environment division.
       input-output section.
       file-control.
           select finfile assign to "isamfil.dat"
               organization is indexed
               record key is fd-tran-date
               access mode is dynamic.

       file section.
       fd finfile
          is external
          record contains 50 characters.
       01 fd-finfile-record.
           05 fd-tran-date     pic x(4).
           05 fd-with-or-dep   pic x(2).
           05 fd-amount        pic 9(5)v99.

       working-storage section.
       01 ws-end-of-file       pic 9       value 0.
       01 ws-subtotal          pic s9(5)v99 value 0.
       01 ws-total             pic -(4)9.99.

       procedure division.
       main-line.
           perform read-the-file.
           perform until ws-end-of-file = 1
               perform calculate-totals
               perform read-the-file
           end-perform.
           perform display-output.
           exit program.
           stop run.

       read-the-file.
           read finfile next record at end move 1 to ws-end-of-file.

       calculate-totals.
           evaluate fd-with-or-dep
             when "WI"
                 subtract fd-amount from ws-subtotal
             when "DE"
                 add fd-amount to ws-subtotal
           end-evaluate.

       display-output.
           move ws-subtotal to ws-total
           display "account balance = ", ws-total.

       end program readfile.
      ************************************************************
       identification division.
       program-id. writefil.
       environment division.
       input-output section.
       file-control.
           select finfile assign to "isamfil.dat"
               organization is indexed
               record key is fd-tran-date
               access mode is dynamic.

       file section.
       fd finfile
          is external
          record contains 50 characters.
       01 fd-finfile-record.
           05 fd-tran-date     pic x(4).
           05 fd-with-or-dep   pic x(2).
           05 fd-amount        pic 9(5)v99.

       procedure division.
       main-line.
           perform write-records
           exit program
           stop run.

       write-records.

      * write a WIthdrawal record
           move 1111 to fd-tran-date.
           move 'WI' to fd-with-or-dep.
           move 23.55 to fd-amount.
           write fd-finfile-record.

      * write a DEposit record
           move 2222 to fd-tran-date.
           move 'DE' to fd-with-or-dep.
           move 123.55 to fd-amount.
           write fd-finfile-record.

       end program writefil.
```

#### ↳ Re: Creating INDEXED File fails Help Required

- **From:** "Mark Miles" <milesfam@idirect.com>
- **Date:** 2002-02-19T10:26:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u74rmd4msr8ed5@corp.supernews.com>`
- **References:** `<u73dmkn2cg8l16@corp.supernews.com>`

```
I have test the sample below using ANIMATOR feature and it worked, so what
could I be missing?

Mark

"Mark Miles" <milesfam@idirect.com> wrote in message
news:u73dmkn2cg8l16@corp.supernews.com...
> I am not a skilled Cobol program but know enough to perform simple tasks,
I
> have been using Microsoft COBOL Ver 4.5, old I know.
>
…[180 more quoted lines elided]…
>
```

#### ↳ Re: Creating INDEXED File fails Help Required

- **From:** "Mark Miles" <milesfam@idirect.com>
- **Date:** 2002-02-19T14:17:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u7596lom2nup0a@corp.supernews.com>`
- **References:** `<u73dmkn2cg8l16@corp.supernews.com>`

```
I have gotten the Fujitsu Compiler working, it didn't like being installed
in "Program Files" and I'm a happy person again.

"Mark Miles" <milesfam@idirect.com> wrote in message
news:u73dmkn2cg8l16@corp.supernews.com...
> I am not a skilled Cobol program but know enough to perform simple tasks,
I
> have been using Microsoft COBOL Ver 4.5, old I know.
>
…[180 more quoted lines elided]…
>
```

#### ↳ Re: Creating INDEXED File fails Help Required

- **From:** Eden Server Support <TechSupport@RosebudUSA.com>
- **Date:** 2002-02-21T19:46:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C7594CE.9BA89695@RosebudUSA.com>`
- **References:** `<u73dmkn2cg8l16@corp.supernews.com>`

```
On your LINK line, try adding +EXTERNL



Mark Miles wrote:

> I am not a skilled Cobol program but know enough to perform simple tasks, I
> have been using Microsoft COBOL Ver 4.5, old I know.
…[175 more quoted lines elided]…
>        end program writefil.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
