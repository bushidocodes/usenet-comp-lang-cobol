[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can Cobol benefit from space....

_2 messages · 2 participants · 2004-10_

---

### Re: Can Cobol benefit from space....

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-10-14T19:10:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MaAbd.101227$a41.38205@pd7tw2no>`
- **In-Reply-To:** `<9IpR0wp9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<41758a6b.0410130804.14a6551b@posting.google.com> <Lcnbd.735170$gE.42255@pd7tw3no> <9IpR0wp9flB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:

>.    Am  14.10.04
>schrieb  jjgavan@shaw.ca (James J. Gavan)
…[47 more quoted lines elided]…
>
Originally, prior to Michael's suggestion (back in '99), I was thinking 
in terms of getting the index positioning per column - see following 
comments from source, I've added periods as it didn't tab correctly in 
this message) Note the 'Sort Key' is the name and not the mnemonic code 
preceding it :-

*> This program prints an alphabetical listing of description records.
*> The Print Table has MaxLines and MaxColumns. The alphabetically
*> sequenced Collection, (by name) is put in the table "down" and
*> "across" the page. If the Collection contains only 11 records then
*> they would be printed as follows :-
*>
*>               Alphabetical List of - Systems/Services
*>
*> AI...Air (Injection).......................IW.. Injection 
Water............  O...Oil
*> C.. ..Condensate.........................ICO. Inlet Crude Oil  
............PW..Produced Water
*> FG...Flare Gas............................ISO...Inlet Sour 
Oil............... RG.. Residual Gas
*> HMG Heating Medium (Glycol).. IA.....Instrument Air

Problem I had taking each print line and the indexing positions from the 
SortedCollection  was :-

Line 1 - 1, 5, 9
Line 2 - 2, 6, 10
Line 3 - 3, 7, 11
Line 4 - 4, 8,  0

OK you could use just ONE print line and a  formula to work out where to 
'plonk' each description, so that the equivalent to Line 3 above 
contains records for index positions 3, 7 and 11 from the Collection, 
but for simplicity, (and when you come back to program maintenance), it 
appeared easier to use a  two-dimensional print-table approach.

The relevant code :-

WORKING-STORAGE SECTION (Global).

       78 MaxLine                       value 58.
       78 MaxColumn                     value 3.
       01 ws-ActualPageSize             pic x(4) comp-5.

- Create a SortedCollection
- Read ISAM sequentially, (or Table with Cursor) and add elements to 
Collection
- invoke MyCollection "size" returning ls-numberOfElements - so now I 
*know* total size
- If ls-NumberOfElements = 355 then I know I have two full pages plus 
last page with 7 elements, occupying three lines..

       *>---------------------------------------------------------------
       Method-id. "P30-print-detail".
       *>---------------------------------------------------------------
       Local-storage section.
       01 ls-CurrentSize                  pic x(4) comp-5.
       01 ls-LinestoPrint                 pic x(4) comp-5.
       01 ls-Remainder                    pic x(4) comp-5.
       01 ls-TempSize                     pic x(4) comp-5.

       Procedure Division.
        move ws-CollectionSize to ls-TempSize
        perform until ls-TempSize = zeroes

            Evaluate true
                when ls-TempSize = zeroes
                     EXIT METHOD
                when ls-TempSize < ws-ActualPageSize
                     move ls-TempSize to ls-CurrentSize
                when other
                     move ws-ActualPageSize to ls-CurrentSize
            End-Evaluate

            divide MaxColumn into ls-CurrentSize
                  giving ls-LinestoPrint remainder ls-Remainder

            if  ls-Remainder <> zeroes
                add 1 to ls-LinestoPrint
            End-if

            invoke self "P50-print-lines" using ls-LinesToPrint
            subtract ls-CurrentSize from ls-TempSize
        End-perform

        if  ContinueProgram
            invoke os-PrintFile "page-throw" using     PageNumber
                                             returning ws-ErrorCode
        End-if

        if CancelProgram
           invoke self "error-exit"
        End-if

       End Method "P30-print-detail".
       *>---------------------------------------------------------
       Method-id. "P50-print-lines".
       *>---------------------------------------------------------
       Working-Storage section.
       01 PrintTable.
          05                            pic x(26) value spaces.
          05 PrintLine occurs MaxLine.
             10 PrintColumn occurs MaxColumn.
                15                      pic x(09) value spaces.
                15 Detail-key           pic x(04).
                15                      pic x(05) value space.
                15 Detail-name          pic x(35).

       Local-storage section.
       01 c                               pic x(4) comp-5.
       01 k                               pic x(4) comp-5.
       01 l                               pic x(4) comp-5.
       01 n                               pic x(4) comp-5.
       01 ls-length                       pic x(4) comp-5.
       01 ls-record                       pic x(des-record-length).
       01 ls-string                       object reference.

       Linkage Section.
       01 lnk-LinesToPrint              pic x(4) comp-5.
       Procedure Division using lnk-LinesToPrint.

        initialize PrintTable, n
        move length of ls-Record to ls-Length
        perform varying c from 1 by 1 until c > MaxColumn
             after L from 1 by 1 until L > lnk-LinestoPrint

                if    L > lnk-LinestoPrint
                      Exit Perform

                else  add 1 to n

                      if     n > ws-CollectionSize
                             Exit Perform

                      else   invoke os-Collection "at"
                                using n returning ls-string
                             invoke ls-string "getValuewithSize"
                                  using ls-length returning ls-record
                             move ls-record(ws-KeyStart:4)
                                    to Detail-key (L, C)
                             move ls-record(1:ws-NameLength)
                                    to Detail-Name (L, C)
                      End-if
                End-if
        End-perform

        move zeroes to LineCount PageNumber
        invoke self "P900-print-heading"

        move length of PrintLine(1) to PrintBufferLen
        perform varying k from 1 by 1 until k > MaxLine
            move PrintLine(k) to PrintBuffer
            invoke os-PrintFile "write-and-newline"
                   using PrintBuffer by value PrintBufferLen
                   returning ws-ErrorCode
        End-perform

        if CancelProgram
           invoke self "error-exit"
        End-if

       End Method "P50-print-lines".
       *>---------------------------------------------------------

Perhaps above could be more efficient - but it works !

When I look at your original code and latest change,  I could be wrong, 
but I don't think it allows for the format I'm showing from the source 
code - and from Kellie's original message it appears to be the 
sequencing that she wants. (?).

Jimmy, Calgary AB
```

#### ↳ Re: Can Cobol benefit from space....

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-10-15T06:37:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ItZ9OHuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<41758a6b.0410130804.14a6551b@posting.google.com> <9IpR0wp9flB@jpberlin-l.willms.jpberlin.de> <MaAbd.101227$a41.38205@pd7tw2no>`

```
.    Am  14.10.04
schrieb  jjgavan@shaw.ca (James J. Gavan)
    auf  /COMP/LANG/COBOL
     in  MaAbd.101227$a41.38205@pd7tw2no
  ueber  Re: Can Cobol benefit from space....

JJG>        End Method "P50-print-lines".
JJG>        *>---------------------------------------------------------
JJG>
JJG> Perhaps above could be more efficient - but it works !

   Interesting. I'm not familiar with OO COBOL, and I don't have a  
compiler capable for that (only the free Fujitsu 3.0)

JJG> When I look at your original code and latest change,  I could be
JJG> wrong, but I don't think it allows for the format I'm showing from
JJG> the source code - and from Kellie's original message it appears to
JJG> be the sequencing that she wants. (?).

   I'm not sure what you mean.

   The program (parts) which I had prevented would fill the last page  
columnwise, i.e. possibly just the first column nearly to the bottom  
of the page, and leave the three other columns empty.

   I do know now that this could be changed by adjusting the leaps  
thru the table of items to be placed on one page to the result of the  
division of the number of available items by the number of columns.

   This also allows for dynamic allocation of the number of columns  
and number of lines per page.

   If I had a 2002-conforming compiler, I would do that using the  
REPORT WRITER and a detail item with a "OCCURS DEPENDING ON number-of- 
columns" and a "VARYING subscript-number", with the SOURCE for those  
items being an item in the table of items collected for filling a  
page.

   In the print-out process I would just set those subscripts resp.  
indexes to the indexes into the table of items to be printed.

   As a work-around with a compiler which does not support those  
enhancements to the REPORT WRITER in COBOL-2002, one could use several  
alternative DETAIL items with different number of columns (I mean  
logical columns) and use different GENERATE statemens in a EVALUATE  
selection based on the number of (logical) columns on that page.



Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Regierung aus dem Volke, durch das Volk und fï¿½r das Volk"
   - Abraham Lincoln, Ansprache in Gettysburg, 19.11.1863
"... was in die revolutionï¿½re Sprache von heute ï¿½bersetzt heiï¿½t:
eine Regierung von Arbeitern, durch Arbeiter und fï¿½r Arbeiter"
                                  - Fidel Castro, November 1994
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
