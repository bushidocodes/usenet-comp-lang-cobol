[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need program to count delimiters

_6 messages · 6 participants · 2006-06_

---

### Need program to count delimiters

- **From:** sasquatch53@gmail.com
- **Date:** 2006-06-28T08:04:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com>`

```
I need a utility that validates the number of delimiters in a file on
our MVS mainframe. I'm sure this is a fairly common requirement when
loading data into a data warehouse.

I was thinking that COBOL would probably be the best thing to write it
in. The latest release of COBOL we have is "Enterprise COBOL for z/OS
and OS/390 3.2". Our MVS level is "MVS LEVEL: 0510.05 z/OS V1R7".
We are using JES2.

I know a little bit of COBOL but it would take me a couple of weeks (or
more) to hack something together.

Is there anybody out there that could provide me with the basic COBOL
program that I could modify if required?

The input file is Variable Blocked (VB) but it would be nice if the
program would work for VB or Fixed Block (FB) files.

I'd like to pass in three variables:
LRECL = The logical record length of the file (would this be
required?).
DELIM = Delimiter character in HEX  (in my case it's a HEX 2F).
DCOUNT = Delimiter count as an INTEGER.

There are no packed fields in these records. The entire record should
be able to be treated as a single character field.

The program should output records that have the matching number of
delimiters to one DD dataset and records that don't have the matching
number of delimiters to another DD dataset.

I looked at the COBOL manual on line and it looks like there is a
function called INSPECT that counts characters across a record/field.
Would this work?

Tim Lindsey
```

#### ↳ Re: Need program to count delimiters

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-06-28T19:26:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oJAog.101926$iF6.45600@pd7tw2no>`
- **In-Reply-To:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com>`
- **References:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com>`

```
sasquatch53@gmail.com wrote:

BOTTOM POSTING :

> I need a utility that validates the number of delimiters in a file on
> our MVS mainframe. I'm sure this is a fairly common requirement when
…[34 more quoted lines elided]…
> 
Not familiar with mainframes but if the IBM Enterprise you are using has 
OO - then you could use Java.

The INSPECT statement is very flexible - check out your IBM on-line help 
(not the Language Reference Manual, necessarily) for various examples.

The following is a bit crude but should give you some idea as to what 
you can do - I'm using commas instead of your Hex 2F :-

Jimmy

        *>--------------------------------------------------------------
        Program-id. InspectTallying.

        WORKING-STORAGE SECTION.

        *> Two input file records, varying in length :-

        01 Record-1.
           05 Rec1-FieldCount   pic 9(03) value 5.
           05 Rec1-Data         pic x(21) value
                                "ABCD,EFG,HIJ,KLM,NOP,".
        01 Record-2.
           05 Rec2-FieldCount   pic 9(03) value 6.
           05 Rec2-Data         pic x(28) value
                                "123,456,78910,111213,1415,16".

        *>  Note : I've left off the final comma after '16' above 


        01 ws-Record.
           05 pic x occurs 1 to 100 depending on ws-Length.

        01 Kounter-1 pic 9(03).
        01 Kounter-2 pic 9(03).
        01 ws-Length pic 9(03).

        Procedure Division.

        move Rec1-FieldCount to Kounter-1
        compute ws-Length    = function length (Rec1-Data)
        *> I'm using REFERENCE MODIFICATION below
        move Rec1-Data       to ws-Record(1:ws-Length)

        perform THE-INSPECT

        move Rec2-FieldCount to Kounter-1
        compute ws-Length    = function length (Rec2-Data)
        *> I'm using REFERENCE MODIFICATION below
        move Rec2-Data       to ws-Record(1:ws-Length)
        perform THE-INSPECT

        STOP RUN.

        THE-INSPECT.

        Initialize Kounter-2
        INSPECT ws-Record TALLYING Kounter-2 for all ","

        if Kounter-2 = Kounter-1
           display "Valid Record"

        else display "Invalid Record"
        End-if

        *>--------------------------------------------------------------
```

#### ↳ Re: Need program to count delimiters

- **From:** Ron S <NoSpam@Spamblocker.org>
- **Date:** 2006-06-28T20:28:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R4WdnQaLE-cisT7ZnZ2dneKdnZydnZ2d@giganews.com>`
- **References:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com>`

```
Example:
move zero to delimiter-count.
perform until eof-flag = 'Y' 
  read input-file 
       at end move to 'Y' eof-flag
   not at end 
       inspect input-record tallying delimiter-counter
           for all x'2F' 
  end-read
end-perform. 

Test for whether you want FB or VB and mod 
accordingly. 

You're going to need two FDs one VB and one FB. 
Not able to test this but I think this will work.
Somebody check me if I make a mistake.  

FD  FB-INPUT 
    label records are standard 
    block contains 0 records
    record contains 0 characters
    recording mode is F. 
01  FB-record pic x(32760). 
This will enable you read any FB file. 

FD  VB-INPUT
    label records are standard 
    block contains 0 records 
    record is varying from 1 to 32756 characters 
      depending on RDW 
    recording mode is V. 
01  VB-record pic x(32756). 

working-storage section. 

01  workarea.
    05  RDW  pic 9(9). 

This should enable you to read any VB file. When you 
read the record it will put the length in RDW (Record 
Descriptor Word)

Good Luck.
```

#### ↳ Re: Need program to count delimiters

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-06-29T17:38:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151627894.716777.13340@d56g2000cwd.googlegroups.com>`
- **References:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com>`

```
Hi:
Back in the day, I used to use both string and unstring with pointer
option to
string things together in cobol...

This was helpful in printer commands...
System Test FBM Legacy MWI DB2 Tables & Data to Oracle OWH
I think it would be difficult to write a generalized program for each
file.  programs usually are data dependant, and the record layout tends
to drive your code...


   D1000-STRING-THAT-THING.
 512700      STRING AREA-OF-HOLD

 512800          DELIMITED BY '%'

 512900          INTO STRING-WORK-AREA

 513000          WITH POINTER WS-STRING-POINTER.

string and unstring will be useful to handle the string or pulling
apart of the data...

sasquatch53@gmail.com wrote:
> I need a utility that validates the number of delimiters in a file on
> our MVS mainframe. I'm sure this is a fairly common requirement when
…[33 more quoted lines elided]…
> Tim Lindsey
```

##### ↳ ↳ Re: Need program to count delimiters

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-06-29T20:02:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E-idnTatJKjDCTnZnZ2dnUVZ_oWdnZ2d@adelphia.com>`
- **In-Reply-To:** `<1151627894.716777.13340@d56g2000cwd.googlegroups.com>`
- **References:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com> <1151627894.716777.13340@d56g2000cwd.googlegroups.com>`

```
Using UNSTRING on the record with COUNT IN in the DELIMITED phrase would 
give a count of all delimiters in the record with a single statement.  
I'm not positive, but I expect that the identifier associated with the 
COUNT IN phrase has to be initialized (set to zero) before processing 
each record.  The IBM documentation I read didn't make this clear.
```

###### ↳ ↳ ↳ Re: Need program to count delimiters

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-06-29T22:21:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12a966389csmmf9@news.supernews.com>`
- **References:** `<1151507063.027141.265970@i40g2000cwc.googlegroups.com> <1151627894.716777.13340@d56g2000cwd.googlegroups.com> <E-idnTatJKjDCTnZnZ2dnUVZ_oWdnZ2d@adelphia.com>`

```
Colin Campbell wrote:
> Using UNSTRING on the record with COUNT IN in the DELIMITED phrase
> would give a count of all delimiters in the record with a single
…[3 more quoted lines elided]…
> didn't make this clear.

COUNT provides the number of characters transferred, not the number of 
delimiters.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
