[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# reading a csv file generated with access

_12 messages · 8 participants · 2004-03_

---

### reading a csv file generated with access

- **From:** "frank" <applied_software@msn.com>
- **Date:** 2004-03-04T12:26:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c283cb$ak9$1@zook.lafn.org>`

```
Hi there,
I am trying to read a file generated with access (comma delimited), but when
opening it gives a 48 status.
It is described as sequential.
```

#### ↳ Re: reading a csv file generated with access

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-03-04T20:59:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org>`

```
On Thu, 4 Mar 2004 12:26:02 -0800, "frank" <applied_software@msn.com>
wrote:

>Hi there,
>I am trying to read a file generated with access (comma delimited), but when
>opening it gives a 48 status.
>It is described as sequential.
Please post the following.

1- Compiler used (vendor and version)
2- Full source code used to describe the file, open and read it.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: reading a csv file generated with access

- **From:** "frank" <applied_software@msn.com>
- **Date:** 2004-03-04T13:17:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c286co$bkv$1@zook.lafn.org>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com>`

```
Hi Frederico,

The compiler is fujitsu v3.
and the way is presented below is sending a 39 status at opening, it does
not pass through it so i am sending the open code only.

  SELECT MICLIENT
               ASSIGN TO "H:\ACCOUNTS.CSV"
                    ORGANIZATION IS SEQUENTIAL
      *              PADDING CHARACTER IS ","
      *              RECORD DELIMITER STANDARD-1
                    FILE STATUS IS CU-STAT.

      FD  MICLIENT
      *      BLOCK CONTAINS 2 RECORDS
            RECORD CONTAINS 10 TO 109 CHARACTERS
            LABEL RECORD IS STANDARD.
      *
       01  SHORT-REC PIC X(10).
       01  LONG-REC PIC X(109).
       01  CMX-RECORD.
           02 CMX-CODS.
               04 CMX-COD     PIC 9(4).
           02 CMX-REFR.
               04 CMX-COMPANY    PIC X(30).
           02 CMX-SUITE.
               04 CMX-SUITE1    PIC X(8).
           02 CMX-REFA.
               04 CMX-ADDRESS  PIC X(20).
               04 CMX-ADDRESS1 PIC X(20).
               04 CMX-ATTN     PIC X(20).
               04 CMX-TAX      PIC 9(5)V99.

               OPEN INPUT MICLIENT.

Your help is appreciated,


"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com...
> On Thu, 4 Mar 2004 12:26:02 -0800, "frank" <applied_software@msn.com>
> wrote:
>
> >Hi there,
> >I am trying to read a file generated with access (comma delimited), but
when
> >opening it gives a 48 status.
> >It is described as sequential.
…[9 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-03-04T21:37:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org>`

```
Chances are that your file is a LINE SEQUENTIAL not (default - ANSI conforming)
RECORD Sequential.  Make the following changes and see how it goes:

   SELECT MICLIENT
                ASSIGN TO "H:\ACCOUNTS.CSV"
                     ORGANIZATION IS  line SEQUENTIAL
       *              PADDING CHARACTER IS ","
       *              RECORD DELIMITER STANDARD-1
                     FILE STATUS IS CU-STAT.
    ...

       FD  MICLIENT
       *      BLOCK CONTAINS 2 RECORDS
       *      RECORD CONTAINS 10 TO 109 CHARACTERS
       *     LABEL RECORD IS STANDARD
                            .
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

_(reply depth: 4)_

- **From:** "frank" <applied_software@msn.com>
- **Date:** 2004-03-04T21:21:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c292p5$lak$1@zook.lafn.org>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org> <RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net>`

```
    Hi there,
If I change to line sequential, it togles the file status to 48 from 39; and
doesn't pass over the open statement. I know 48 shouldn't be there because
is not doing any i-o operation.
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net...
> Chances are that your file is a LINE SEQUENTIAL not (default - ANSI
conforming)
> RECORD Sequential.  Make the following changes and see how it goes:
>
…[23 more quoted lines elided]…
> > and the way is presented below is sending a 39 status at opening, it
does
> > not pass through it so i am sending the open code only.
> >
…[38 more quoted lines elided]…
> > > >I am trying to read a file generated with access (comma delimited),
but
> > when
> > > >opening it gives a 48 status.
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-03-05T10:59:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B4Z1c.22408$aT1.22108@newsread1.news.pas.earthlink.net>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org> <RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net> <c292p5$lak$1@zook.lafn.org>`

```
Did you OPEN INPUT - or some other way?
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

_(reply depth: 5)_

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-03-05T05:55:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0403050555.7ec90e14@posting.google.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org> <RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net> <c292p5$lak$1@zook.lafn.org>`

```
Hello,

You will have to give us much more code, for us to be able to help.

One possibility is that you use the same file-status data-item for
more than one file and are seeing the result of another i/o operation.

Do you always test the file-status after every i/o operation on all
files and fully account for all exceptional cases?

Regards,  Robert

"frank" <applied_software@msn.com> wrote in message news:<c292p5$lak$1@zook.lafn.org>...
> Hi there,
> If I change to line sequential, it togles the file status to 48 from 39; and
…[20 more quoted lines elided]…
> >                             .
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-03-05T09:21:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0403050921.3367b0e1@posting.google.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org> <RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net> <c292p5$lak$1@zook.lafn.org>`

```
My guess is that you didn't catch all of Bill's changes.  In addition
to changing to line sequential, the variable length record
specification was removed form the FD.

Contrary to other messages "39" is not a file not found, that would
have given you a "35".  "39" is a fixed file attribute problem - which
I expect to see if you use Line Sequential WITH the variable length
record specification.

"frank" <applied_software@msn.com> wrote in message news:<c292p5$lak$1@zook.lafn.org>...
> Hi there,
> If I change to line sequential, it togles the file status to 48 from 39; and
…[91 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

_(reply depth: 6)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-03-05T14:32:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DI42c.9352$jw2.647785@news20.bellglobal.com>`
- **In-Reply-To:** `<bfdfc3e8.0403050921.3367b0e1@posting.google.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org> <RkN1c.19225$yZ1.18131@newsread2.news.pas.earthlink.net> <c292p5$lak$1@zook.lafn.org> <bfdfc3e8.0403050921.3367b0e1@posting.google.com>`

```
Thane Hubbell wrote:
> My guess is that you didn't catch all of Bill's changes.  In addition
> to changing to line sequential, the variable length record
…[6 more quoted lines elided]…
> 
This is what I use for fujitsu cobol CSV files. I think you will get a 
39 error if you try to read a line over 1000 characters long, but 
otherwise you should get the line length back in sequential-record-size 
up until an "AT END" statement. The data persists after both errors and 
closes if you want to code up a DECLARATIONS section.  That's 
non-standard, but it is there.

Donald

            SELECT SEQUENTIAL-FILE ASSIGN TO SEQUENTIAL-ID
                ACCESS MODE IS SEQUENTIAL
                FILE STATUS IS SEQUENTIAL-STATUS
                ORGANIZATION IS LINE SEQUENTIAL.
        DATA DIVISION.
        FILE SECTION.
        FD SEQUENTIAL-FILE
            RECORD IS VARYING IN SIZE
            FROM 1 TO 1000 CHARACTERS
            DEPENDING ON SEQUENTIAL-RECORD-SIZE.
        01 SEQUENTIAL-RECORD                 PICTURE X(1000).
        WORKING-STORAGE SECTION.
        77 sequential-record-size            picture 9(4).
        77 SEQUENTIAL-STATUS                 picture xx.
        77 SEQUENTIAL-ID                     PICTURE X(80).
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-03-04T21:05:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0403042105.50d86efd@posting.google.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org>`

```
"frank" <applied_software@msn.com> wrote

> The compiler is fujitsu v3.
> and the way is presented below is sending a 39 status at opening, it does
…[3 more quoted lines elided]…
>                ASSIGN TO "H:\ACCOUNTS.CSV"

File staus '39' is file not found.  There is no file called
'H:\ACCOUNTS.CSV' so the OPEN INPUT failed.

If you had ignored this and gone on to do something else with the file
then you would get strange file status codes because the file is not
open.

The implication of the '.CSV' on the file name is that it is a Comma
Separated Value file.  This cannot be read into a record area directly
as the fields are not in fixed positions.  If it is a CSV then you
will need to declare it LINE SEQUENTIAL and separate the fields
yourself.
```

###### ↳ ↳ ↳ Re: reading a csv file generated with access

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-03-05T06:42:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q8OdnUj33JEG6NXdRVn-hw@giganews.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org> <h36f40lsrjul7c60pljf13so50g9j9pkp8@4ax.com> <c286co$bkv$1@zook.lafn.org> <217e491a.0403042105.50d86efd@posting.google.com>`

```
Richard wrote:
> "frank" <applied_software@msn.com> wrote
>
…[8 more quoted lines elided]…
> 'H:\ACCOUNTS.CSV' so the OPEN INPUT failed.

No, "39" is "Conflict between fixed and defined file attributes."

This means that the actual file on the disk does not conform to the
program's file definition.

"35" is file not found.
```

#### ↳ Re: reading a csv file generated with access

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-03-04T15:56:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nICdnR2FzLJ4ONrd4p2dnA@giganews.com>`
- **References:** `<c283cb$ak9$1@zook.lafn.org>`

```
frank wrote:
> Hi there,
> I am trying to read a file generated with access (comma delimited),
> but when opening it gives a 48 status.
> It is described as sequential.

Huh?

"48" is "Write on file not opened in appropriate mode"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
