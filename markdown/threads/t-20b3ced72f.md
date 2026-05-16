[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# please help

_6 messages · 6 participants · 2000-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### please help

- **From:** "Matt Wieben" <mw5@dana.ucc.nau.edu>
- **Date:** 2000-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rel3l$r19$1@usenet.nau.edu>`

```
This program doesn't separate the coloumns and it repeats numbers, I've also
included the data file for this at the bottom.. I can't get any help at
all...my prof pretty much told me to f*ck off when I went to her for help on
why the output is STILL funky.
Thank you VERY VERY MUCH.


       IDENTIFICATION DIVISION.

       PROGRAM-ID.    PROJECT1.
       AUTHOR.        WIEBEN.
       DATE-WRITTEN.  10-3-00.

      *****************************************************************
      *                                                               *
      *  ASSIGNMENT NUMBER                                            *
      *  DATE ASSIGNED                                                *
      *  DATE DUE                                                     *
      *  PURPOSE:  THIS PROGRAM READS INVENTORY RECORDS AND           *
      *            PRINTS THEM OUT WITH NO HEADINGS OR SPACING        *
      *                                                               *
      *****************************************************************

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       FILE-CONTROL.
           SELECT 100-INVENTORY-FILE
                  ASSIGN TO "inventry.dat"
                  ORGANIZATION IS LINE SEQUENTIAL.


           SELECT 200-REPORT-FILE
                  ASSIGN TO "inventry.rpt"
                  ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.

       FILE SECTION.

       FD  100-INVENTORY-FILE
               RECORD CONTAINS 50 CHARACTERS.
       01  100-INVENTORY-RECORD PIC X(50).
               01 IN-ITEM-NUMBER              PIC 9(5).
               01 IN-ITEM-DESC                PIC X(25).
               01 IN-ITEM-QUANTITY            PIC 9(4).
               01 IN-ITEM-COUNT               PIC ZZ9(2).
               01 IN-ITEM-COST                PIC ZZZZ99v99.
               01 IN-ITEM-REORDER             PIC ZZ9(2).
               01 IN-SUPPLIER-CODE            PIC 9(2).
               01 IN-BUYER-CODE               PIC 9(2).

       FD  200-REPORT-FILE
               RECORD CONTAINS 133 CHARACTERS.
       01  200-REPORT-LINE PIC X(133).

       WORKING-STORAGE SECTION.

       01  ARE-THERE-MORE-RECORDS    PIC X(3)       VALUE 'YES'.
           88 MORE-RECORDS                          VALUE 'YES'.
           88 NO-MORE-RECORDS                       VALUE 'NO'.

       01  400-TITLE-LINE.
           05 FILLER   PIC X(15).
           05 FILLER   PIC X(14)   VALUE 'MATTHEW WIEBEN'.

       01  500-RECORD-IN                     PIC X(50).

       01  600-OUT                           PIC X(50).

       01  HEADING-LINE.
           05 FILLER                   PIC X(6)    VALUE'ITEM #'.
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 FILLER                   PIC X(10)   VALUE 'ITEM DESC.'.
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 FILLER                   PIC X(7)    VALUE 'ON HAND'.
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 FILLER                   PIC X(9)    VALUE 'COST/UNIT'.
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 FILLER                   PIC X(13)   VALUE 'REORDERLIMIT'.
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 FILLER                   PIC X(13)   VALUE 'SUPPLIERCODE'.
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 FILLER                   PIC X(10)   VALUE 'BUYER CODE'.

       01  INVENTORY-DATA.
           05 ITEM-NUMBER              PIC 9(5).
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 ITEM-DESC                PIC X(25).
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 ITEM-COUNT               PIC 9(2).
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 ITEM-COST                PIC ZZZZ9(4).
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 ITEM-REORDER             PIC ZZ9(2).
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 SUPPLIER-CODE            PIC 9(2).
           05 FILLER                   PIC X(2)    VALUE SPACES.
           05 BUYER-CODE               PIC 9(2).

       PROCEDURE DIVISION.

       A100-MAIN-PARA.
           PERFORM B100-INIT-PARA
           PERFORM C200-READ-PARA
           PERFORM B200-PROCESS-PARA
                   UNTIL NO-MORE-RECORDS
           PERFORM B300-CLOSE-PARA
           STOP RUN
           .

       B100-INIT-PARA.
           OPEN INPUT 100-INVENTORY-FILE
           OPEN OUTPUT 200-REPORT-FILE.
           WRITE 200-REPORT-LINE FROM 400-TITLE-LINE
              BEFORE 1

           MOVE HEADING-LINE TO 200-REPORT-LINE.
              WRITE 200-REPORT-LINE.
           MOVE SPACES TO 200-REPORT-LINE.
              WRITE 200-REPORT-LINE.
           *>MOVE 500-RECORD-IN TO 600-OUT.




       B200-PROCESS-PARA.
           PERFORM C100-WRITE-REPORT-PARA
           PERFORM C200-READ-PARA
           .

       C100-WRITE-REPORT-PARA.
           *>MOVE 500-RECORD-IN TO 600-OUT
           MOVE IN-ITEM-NUMBER     TO      ITEM-NUMBER.
           MOVE IN-ITEM-DESC       TO      ITEM-DESC.
           MOVE IN-ITEM-COUNT      TO      ITEM-COUNT.
           MOVE IN-ITEM-REORDER    TO      ITEM-REORDER.
           MOVE IN-SUPPLIER-CODE   TO      SUPPLIER-CODE.
           MOVE IN-BUYER-CODE      TO      BUYER-CODE.

           MOVE INVENTORY-DATA TO 200-REPORT-LINE.
               WRITE 200-REPORT-LINE.

           *>WRITE 200-REPORT-LINE FROM 600-OUT
             *>   AFTER 1

       C200-READ-PARA.
           READ 100-INVENTORY-FILE INTO 500-RECORD-IN
                AT END
                   MOVE 'NO' TO ARE-THERE-MORE-RECORDS
           END-READ
           .


       B300-CLOSE-PARA.
           CLOSE 100-INVENTORY-FILE
           CLOSE 200-REPORT-FILE
           .

02222ANTI-GLARE SCREEN        00100004000000050102
03001TURTLENECK SWEATER       00250000800000150101
08234SPARK PLUGS 1 DOZ        00400000120000500103
11653LEATHER JACKET           00070001500000050104
12345BROWN LEATHER BELT       00200000150000150201
12355BLACK LEATHER BELT       00220000150000150201
21100PRINT SILK SCARVES       00030000180000100301
21133T-SHIRT DRESSES          00080000210000050302
21143SWEATER DRESSES          00120000320000100303
22165DESIGNER SWEATER         00080000500000050301
22298ST COTTON SHORTS         00200000190000150304
22324BLUE JEANS PLEATS        00300000300000200202
22346SOLID SWEAT SHIRTS       00230000220000150302
22700LG COTTON SHORTS         00090000140000100202
22835SWEAT PANTS              00300000100000200302
22988DESIGN SWEAT SHIRT       00220000450000200103
23334BLUE JEANS STRAIGHT LEG  00400000230000250203
23342DRESS BLOUSES BOWTIE     00130000500000100104
23444DESIGNER POLO SHIRTS     00020000500000250301
23453COTTON BOTTONDOWNS       00380000450000300202
23552DESIGNER COTTON BLOUSES  00040000550000200301
23664BUDGET POLO SHIRTS       00210000260000200201
24345ACID WASHED JEAN JR      00130000180000100204
24350ACID WASHED J SKIRT      00080000220000150204
24355ACID WASHED MINI-SKIRT   00100000240000080203
```

#### ↳ Re: please help

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nLBC5.4637$wx5.132285@news2.giganews.com>`
- **References:** `<8rel3l$r19$1@usenet.nau.edu>`

```

On  3-Oct-2000, "Matt Wieben" <mw5@dana.ucc.nau.edu> wrote:

> This program doesn't separate the coloumns and it repeats numbers, I've
> also included the data file for this at the bottom.. I can't get any help
> at
> all...my prof pretty much told me to f*ck off when I went to her for help
> on why the output is STILL funky.

It won't even pass my compiler.  There are serious problems with this prog.
Read your book.

Hint:  there's WAY too many 01 levels on your input file.
Another hint:  your input fields don't match your output fields.

Also, you should either use periods by themselves at the end of paragraphs,
or not.

If this program compiled for you, I've GOT to get one of those compilers!

Cliff
```

#### ↳ Re: please help

- **From:** "Charles W. Cribbs II" <CHARLESCRIBBS@prodigy.net>
- **Date:** 2000-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rlqm8$6jjm$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<8rel3l$r19$1@usenet.nau.edu>`

```


Matt Wieben <mw5@dana.ucc.nau.edu> wrote in message
news:8rel3l$r19$1@usenet.nau.edu...
> This program doesn't separate the coloumns and it repeats numbers, I've
also
> included the data file for this at the bottom.. I can't get any help at
> all...my prof pretty much told me to f*ck off when I went to her for help
on
> why the output is STILL funky.
> Thank you VERY VERY MUCH.
…[34 more quoted lines elided]…
>

your file description is wrong.
when you define an 01 level all levels below it are subornate to it so must
not be an 01 level.  you can use any other number up to 50 i believe but it
is usually done line this:

    FD  100-INVENTORY-FILE
>         RECORD CONTAINS 50 CHARACTERS.
>        01  100-INVENTORY-RECORD.
…[7 more quoted lines elided]…
>                05 IN-BUYER-CODE               PIC 9(2).

you can not have numeric edited fields in a record layout

>        FD  100-INVENTORY-FILE
>                RECORD CONTAINS 50 CHARACTERS.
…[15 more quoted lines elided]…
>

if you use an 88 level of yes you don't want to give the initial value as
"YES"
>        01  ARE-THERE-MORE-RECORDS    PIC X(3)       VALUE 'YES'.
>            88 MORE-RECORDS                          VALUE 'YES'.
…[31 more quoted lines elided]…
>            05 FILLER                   PIC X(2)    VALUE SPACES.

do you really want a number that is 8 numeric characters long with the first
4 zero supressed?
>            05 ITEM-COST                PIC ZZZZ9(4).
>            05 FILLER                   PIC X(2)    VALUE SPACES.

this applies here too.
you usually don't need to zero suppress until you have moved the field to
your report field.  your report field would have a picture using zero
suppression.
>            05 ITEM-REORDER             PIC ZZ9(2).
>            05 FILLER                   PIC X(2)    VALUE SPACES.
…[5 more quoted lines elided]…
> you have got to more consistent in the use of periods.  if you are going
to use them do them at the end of statements and paragraphs just like
english.  don't use them within an if statment but after the end-if.  the
scope terminator functions as a period but most programs will use both
because it helps to block logic off in sections for the eye to see.
>        A100-MAIN-PARA.
>            PERFORM B100-INIT-PARA
…[11 more quoted lines elided]…
>               BEFORE 1
what are you doing here??  all you need to do is say write from report line
and it will write one line and advance to the next.

>            MOVE HEADING-LINE TO 200-REPORT-LINE.
>               WRITE 200-REPORT-LINE.
…[29 more quoted lines elided]…
>                 AT END

you have an 88 level of no more records don't make a move of it set the 88
level to true

that would be said:    set NO-MORE-RECORDS to true
by doing this you have set the condition once the at end has been reached.
>                    MOVE 'NO' TO ARE-THERE-MORE-RECORDS
>            END-READ
…[35 more quoted lines elided]…
>
```

##### ↳ ↳ Re: please help

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39DF2D0C.656D5705@brazee.net>`
- **References:** `<8rel3l$r19$1@usenet.nau.edu> <8rlqm8$6jjm$1@newssvr05-en0.news.prodigy.com>`

```
"Charles W. Cribbs II" wrote:
> 
> you can not have numeric edited fields in a record layout

I haven't tried one in an input record layout, but certainly have in
output record layouts. 
 

> if you use an 88 level of yes you don't want to give the initial value as
> "YES"
> >        01  ARE-THERE-MORE-RECORDS    PIC X(3)       VALUE 'YES'.
> >            88 MORE-RECORDS                          VALUE 'YES'.
> >            88 NO-MORE-RECORDS                       VALUE 'NO'.


Why not?

> >            WRITE 200-REPORT-LINE FROM 400-TITLE-LINE
> >               BEFORE 1
> what are you doing here??  all you need to do is say write from report line
> and it will write one line and advance to the next.

I tend to say AFTER ADVANCING 1.  Some places it is the standard.
```

###### ↳ ↳ ↳ Re: please help

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001007153046.04122.00000022@nso-cb.aol.com>`
- **References:** `<39DF2D0C.656D5705@brazee.net>`

```
In article <39DF2D0C.656D5705@brazee.net>, Howard Brazee <howard@brazee.net>
writes:

>"Charles W. Cribbs II" wrote:
>> 
…[4 more quoted lines elided]…
>

I know for a fact the you can have numeric edited as input or sending 
fields under OS\390/COBOL for OS\390.  We had a couple input sources 
that were basically trial balance reports on electronic media that had to be
reformatted into usable fields.  I did however find that the numeric edited 
fields have to move thru a display numeric field before being moved to 
packed or binary fields.
```

###### ↳ ↳ ↳ Re: please help

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rnv4e$p8a$1@slb0.atl.mindspring.net>`
- **References:** `<39DF2D0C.656D5705@brazee.net> <20001007153046.04122.00000022@nso-cb.aol.com>`

```
There is no restriction in any current OR PAST Standard that says that you
can't have edited (numeric-edited or alphanumeric-edited) fields in any
"record layout" (under FD or otherwise).  Now, the problem in using this in
an "input" record layout - is that the data may NOT come in that way.  For
example, if you have:

  05 NumEdit  Pic  ZZ9.

in your input field - and your data comes in as "001" instead of "  1"
(leading blanks), then you TECHNICALLY have "incompatible data" - and
results are "undefined".  However, it is EQUALLY true that if your data does
come in with leading blanks, then it would cause incompatible data if you
defined it as:

  05 NumEdit Pic 999.

Therefore, the answer is to define your input fields the way the data
actually exists in the files.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
