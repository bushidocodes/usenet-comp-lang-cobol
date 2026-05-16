[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Demo: convert Cobol file to csv

_12 messages · 5 participants · 2004-07 → 2005-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Demo: convert Cobol file to csv

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-22T16:21:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40ffe958.70772793@news.optonline.net>`

```
*              Convert Cobol file to comma or tab delimited
*
* This program interprets a Cobol copybook describing a record layout,
* then converts the file to either csv or tsv (comma or tab delimited).
*
* This program would best be used by the organization sending the file,
* because it has a Cobol compiler and could better deal with
* ideisyncrasies in its file system. When used by the organization
* receiving the file, the program need be compiled only once. The
* executable will convert all files.
*
* This program also provides a simple demo of how to parse
* and interpret source code.
*
* Copybook file: cob2csv.cpy
* Input data file: cob2csv.in
* Output data file: cob2csv.out
* Environment variable: delimiter=tab (default is comma)
*   This program filters out data characters matching the delimiter.
* Supported formats: string, display numeric, binary and packed decimal,
* simple OCCURS. REDEFINES is ignored, the first definition is used.
* Not supported: editing pictures, scaling, OCCURS at group level,
* OCCURS DEPENDING ON.
*
* If your machine is big-endian (a PC) or 32-bit, required changes
* are in comments below.
*
* Example copybook:
*        01  WWICTLG.
*            10 CTLGOP-CO-NO              PIC X(3).
*            10 CTLGCONTROL-SET-SEQ-NO    PIC S9(9) USAGE COMP.
*            10 CTLGINVOICE-SEQ-NO        PIC S9(4) USAGE COMP.
*            10 CTLGAP-CNTRL-ENTITY-CD    PIC X(4).
*            10 CTLGINVOICE-TYPE-CD       PIC X(2).
*            10 CTLGLEGACY-VENDOR-NO      PIC X(10).
*            10 CTLGAP-VENDOR-NO          PIC X(30).
*            10 CTLGAP-PO-NO              PIC X(30).
*            10 CTLGAP-INVOICE-NO         PIC X(30).
*            10 CTLGINVOICE-DT            PIC X(10).
*            10 CTLGTOTAL-INVOICE-AM      PIC S9(11)V9(2) USAGE COMP-3.
*            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V99   USAGE COMP-3.
*            10 CTLGTERMS-CD              PIC XX.
*            10 CTLGCARRIER-CD            PIC X(10).
*            10 CTLGCARRIER-PRO-NO        PIC X(10).
*            10 CTLGSHIP-DT               PIC X(10).
*            10 CTLGSHIP-VIA-CD           PIC X(3).
*            10 CTLGSHIP-LOC-NO           PIC X(3).
*            10 CTLGSHIP-WT               PIC X(10).
*            10 x redefines CTLGSHIP-WT   PIC X(10).
*            10 CTLGSHIP-UNITS-DC         PIC X(10).
*            10 CTLGSHIP-TY               PIC X(2).
*
* Example results:
* > cob2csv
*     Lvl Name                           Pos Len Typ Occ
*    1 10 ctlgop-co-no                     1   3   x   1
*    2 10 ctlgcontrol-set-seq-no           4   4   b   1
*    3 10 ctlginvoice-seq-no               8   2   b   1
*    4 10 ctlgap-cntrl-entity-cd          10   4   x   1
*    5 10 ctlginvoice-type-cd             14   2   x   1
*    6 10 ctlglegacy-vendor-no            16  10   x   1
*    7 10 ctlgap-vendor-no                26  30   x   1
*    8 10 ctlgap-po-no                    56  30   x   1
*    9 10 ctlgap-invoice-no               86  30   x   1
*   10 10 ctlginvoice-dt                 116  10   x   1
*   11 10 ctlgtotal-invoice-am           126   7 2 p   1
*   12 10 ctlgtotal-merch-am             133   7 2 p   1
*   13 10 ctlgterms-cd                   140   2   x   1
*   14 10 ctlgcarrier-cd                 142  10   x   1
*   15 10 ctlgcarrier-pro-no             152  10   x   1
*   16 10 ctlgship-dt                    162  10   x   1
*   17 10 ctlgship-via-cd                172   3   x   1
*   18 10 ctlgship-loc-no                175   3   x   1
*   19 10 ctlgship-wt                    178  10   x   1
*   20 10 ctlgship-units-dc              188  10   x   1
*   21 10 ctlgship-ty                    198   2   x   1
*         Record length                  199
* Record count:          10
* > cat cob2csv.out
* 123,1,-1,,T,,test 0001,,,,1.00,-1.00,,,,,,,,,SH
* 123,2,-2,,T,,test 0002,,,,2.00,-2.00,,,,,,,,,SH
* 123,3,-3,,T,,test 0003,,,,3.00,-3.00,,,,,,,,,SH
* 123,4,-4,,T,,test 0004,,,,4.00,-4.00,,,,,,,,,SH
* 123,5,-5,,T,,test 0005,,,,5.00,-5.00,,,,,,,,,SH
* 123,6,-6,,T,,test 0006,,,,6.00,-6.00,,,,,,,,,SH
* 123,7,-7,,T,,test 0007,,,,7.00,-7.00,,,,,,,,,SH
* 123,8,-8,,T,,test 0008,,,,8.00,-8.00,,,,,,,,,SH
* 123,9,-9,,T,,test 0009,,,,9.00,-9.00,,,,,,,,,SH
* 123,10,-10,,T,,test 0010,,,,10.00,-10.00,,,,,,,,,SH
* >

      $SET SOURCEFORMAT"FREE"
   identification division
 . program-id. cob2csv
*> author. Robert Wagner
*>  Convert Cobol file to comma-delimited file using copybook.

 . data division
 . working-storage section
 . 01  global-variables value low-values global
 .     05  pic x
 .         88  end-of-copybook value 'e'
 .     05  pic x
 .         88  end-of-sentence value 'e'
 .         88  not-end-of-sentence value low-value
 .     05  pic x
 .         88  end-of-data-file value 'e'
 . 01  word-area global
 .     05  word-count                     binary   pic s9(04)
 .     05  word-limit value 200           binary   pic s9(04)
 .     05  word-entry occurs 1 to 200 depending on word-count
 .         10  word-length                binary   pic s9(04)
 .         10  word-text
 .             15  word-byte occurs 50             pic  x(01)
 . 01  line-text-area global
 .     05  line-length value zero         binary   pic s9(04)
 .     05  line-limit  value 256          binary   pic s9(04)
 .     05  line-text
 .         10  line-byte occurs 1 to 256 depending on line-length pic x
 . 01  layout-area global
 .     05  layout-count value zero        binary   pic s9(04)
 .     05  layout-limit value 200         binary   pic s9(04)
 .     05  layout-entry occurs 1 to 200 depending on layout-count
 .         10  layout-level                        pic  x(02)
 .         10  layout-name                         pic  x(30)
 .         10  layout-occurs              binary   pic s9(04)
 .         10  layout-offset              binary   pic s9(04)
 .         10  layout-length              binary   pic s9(04)
 .         10  layout-decimals            binary   pic s9(04)
 .         10  layout-type                         pic  x(01)
 .             88  type-string  value 'x' space
 .             88  type-number  value '9'
 .             88  type-signed  value 's'
 .             88  type-binary  value 'b'
 .             88  type-packed  value 'p'

 . procedure division.
     perform phase-1-copybook
     perform phase-2-data-file
     goback

 . phase-1-copybook.
     display '    Lvl Name                           Pos Len Typ Occ'
     perform one-sentence until end-of-copybook

 . one-sentence.
     set not-end-of-sentence to true
     move zero to word-count
     perform one-word until end-of-sentence or end-of-copybook or
         word-count not less than word-limit
     if  word-count not equal to zero and layout-count < layout-limit
         call 'syntax'
     end-if
 . one-word.
     call 'parse'

 . phase-2-data-file.
       call 'convert-file'

 . identification division
 . program-id. syntax
*>  Transforms a free-form Cobol sentence into a layout-entry.

 . data division
 . working-storage section
 . 01  unqualified-variables
 .     05  n value zero               binary   pic s9(04)
 .     05  n-minus-1                  binary   pic s9(04)
 .     05  m value zero               binary   pic s9(04)
 .     05  x9-count-in-word           binary   pic s9(04)
 .     05  pic-count-in-word          binary   pic s9(04)
 .     05  numeric-count-in-word      binary   pic s9(04)
 .     05  digits-after-v             binary   pic s9(04)
 .     05                                      pic  x(01)
 .           88 picture-word value 'p'
 .           88 not-picture-word value 'n'
 .     05                                      pic  x(01)
 .           88 type-seen     value 'y'
 .           88 type-not-seen value 'n'
 .     05                                      pic  x(01)
 .           88 s-seen        value 'y'
 .           88 s-not-seen    value 'n'
 .     05                                      pic  x(01)
 .           88 v-seen        value 'y'
 .           88 v-not-seen    value 'n'
 .     05  byte-type                           pic  x(01)
 .         88  pic-type          value 'x' '9' 'v' 's'
 .         88  x9-type           value 'x' '9'
 .         88  v-type            value 'v'
 .         88  s-type            value 's'
 .         88  numeric-type      value '0' thru '9'
 .     05  redefines-level value spaces        pic  x(02)
 .     05  work-number                         pic  9(04)
 .     05   redefines work-number.
 .        10                                   pic  x(03)
 .        10  work-number-4                    pic  x(01)
 . 01  display-line.
 .     05  edited-count                        pic  z(04)-
 .     05  edited-level                        pic  x(03)
 .     05  edited-name                         pic  x(30)
 .     05  edited-offset                       pic  z(04)
 .     05  edited-length                       pic  z(04)
 .     05  edited-decimals                     pic  z(02)-
 .     05  edited-type                         pic  x(01)
 .     05  edited-occurs                       pic  z(04)

 . procedure division.
     if  redefines-level not equal to spaces
         if  word-text (1) greater than redefines-level
             move zero to word-count
             goback
         else
             move spaces to redefines-level
         end-if
     end-if

     add 1 to layout-count
     initialize layout-entry (layout-count)
     move 1 to layout-occurs (layout-count)
     move word-text (1) to layout-level (layout-count)
     move word-text (2) to layout-name (layout-count)
     perform varying n from 2 by 1 until n > word-count
         evaluate word-text (n)
             when 'pic'
             when 'picture'
                 perform pickup-picture
             when 'occurs'
                 perform pickup-occurs
             when 'binary'
             when 'comp'
             when 'computational'
             when 'comp-4'
             when 'comp-5'
                 set type-binary (layout-count) to true
             when 'packed-decimal'
             when 'comp-3'
             when 'computational-3'
                 set type-packed (layout-count) to true
             when 'redefines'
                 move word-text (1) to redefines-level
                 move zero to word-count
                 subtract 1 from layout-count
                 goback
         end-evaluate
     end-perform
     if  layout-length (layout-count) equal to zero
         subtract 1 from layout-count
         goback
     end-if
     if  type-binary (layout-count)
         evaluate layout-length (layout-count)
             when 1 thru 4
                 move 2 to layout-length (layout-count)
             when 5 thru 9
                 move 4 to layout-length (layout-count)
             when other
                 move 8 to layout-length (layout-count)
         end-evaluate
     end-if
     if  type-packed (layout-count)
         compute layout-length (layout-count) rounded =
             (layout-length (layout-count) + 1) / 2
     end-if
     if  layout-count equal to 1
         move 1 to layout-offset (layout-count)
     else
         compute n-minus-1 = layout-count - 1
         compute layout-offset (layout-count) =
                 layout-offset (n-minus-1) +
                 (layout-length (n-minus-1) *
                  layout-occurs (n-minus-1))
     end-if

     move layout-count                   to edited-count
     move layout-level    (layout-count) to edited-level
     move layout-name     (layout-count) to edited-name
     move layout-offset   (layout-count) to edited-offset
     move layout-length   (layout-count) to edited-length
     move layout-decimals (layout-count) to edited-decimals
     move layout-type     (layout-count) to edited-type
     move layout-occurs   (layout-count) to edited-occurs
     display display-line

     goback
 . pickup-occurs.
     add 1 to n
     perform pickup-number
     move work-number to layout-occurs (layout-count)
 . pickup-picture.
*  Picture s9(9)v9(2) will be in four words: s9, 9, v9, 2.
     add 1 to n
     set picture-word to true
     set type-not-seen to true
     set s-not-seen to true
     set v-not-seen to true
     perform varying n from n by 1 until n > word-count or
         not-picture-word
         move zero to pic-count-in-word, numeric-count-in-word,
             x9-count-in-word, digits-after-v, work-number
         perform varying m from 1 by 1 until m > word-length (n)
             move word-byte (n, m) to byte-type
             if  numeric-type
                 add 1 to numeric-count-in-word
                 multiply 10 by work-number
                 move byte-type to work-number-4
                 if  v-seen
                     add 1 to digits-after-v
                 end-if
             end-if
             if  pic-type
                 add 1 to pic-count-in-word
             end-if
             if  x9-type
                 add 1 to x9-count-in-word
             end-if
             if  s-type
                 set s-seen to true
             end-if
             if  v-type
                 set v-seen to true
                 set type-not-seen to true
             end-if
         end-perform
         evaluate true
             when numeric-count-in-word equal to word-length (n) and
                 type-seen
                 add work-number -1 to layout-length (layout-count)
                 if  v-seen
                     add work-number -1 to layout-decimals (layout-count)
                 end-if
             when pic-count-in-word equal to word-length (n) and
                 type-not-seen
                 set type-seen to true
                 add x9-count-in-word to layout-length (layout-count)
                 if  v-seen
                     add digits-after-v to layout-decimals (layout-count)
                 end-if
                 if  type-string (layout-count)
                     move byte-type to layout-type (layout-count)
                 end-if
                 if  s-seen and type-number (layout-count)
                     set type-signed (layout-count) to true
                 end-if
             when other
                 set not-picture-word to true
                 subtract 2 from n
         end-evaluate
     end-perform

 . pickup-number.
     move zero to work-number
     perform varying m from 1 by 1 until m > word-length (n)
         multiply 10 by work-number
         move word-byte (n, m) to work-number-4
     end-perform
 . end program syntax

 . identification division
 . program-id. parse
*>  Parser. Returns the next word.

 . data division
 . working-storage section
 . 01  unqualified-variables
 .     05  n value 1                  binary   pic s9(04)
 .     05  n-plus-1                   binary   pic s9(04)
 .     05  m                          binary   pic s9(04)
 .     05  byte-type                           pic  x(01)
 .         88  in-a-word         value 'x' '9'
 .         88  alpha-character   value 'x'
 .         88  numeric-character value '9'
 .         88  full-stop         value '.'
 .     05  quote-character                     pic  x(01)
 .         88  in-a-quote value x'22' x'27'
 .     05  a-byte                              pic  x(01)

 . procedure division.
     move space to byte-type
     perform varying n from n by 1 until in-a-word or in-a-quote
         if  n greater than line-length
             call 'read-copybook'
             move zero to n
             if  end-of-copybook goback end-if
         else
             perform pickup-byte
             move a-byte to quote-character
             compute n-plus-1 = n + 1
             if  full-stop and
                 (n less than line-length or
                  line-byte (n-plus-1) equal to space)
                 set end-of-sentence to true
                 add 1 to n
                 goback
             end-if
         end-if
     end-perform

     add 1 to word-count
     move spaces to word-text (word-count)
     subtract 1 from n

     perform varying word-length (word-count) from 1 by 1 until
         not (in-a-word or in-a-quote) or
         word-length (word-count) not less length of word-text
         move word-length (word-count) to m
         move a-byte to word-byte (word-count, m)
         if  in-a-quote and a-byte equal to quote-character and
             word-length (word-count) greater than 1
             move space to quote-character
         end-if
         add 1 to n
         if  n greater than line-length exit paragraph end-if
         perform pickup-byte
     end-perform
     subtract 1 from word-length (word-count)

     goback

 . pickup-byte.
     move line-byte (n) to a-byte, byte-type
     inspect byte-type converting
        'abcdefghijklmnopqrstuvwxyz-0123456789' to
        'xxxxxxxxxxxxxxxxxxxxxxxxxxx9999999999'

 . identification division
 . program-id. read-copybook
*>  Returns the next line
*>  Deletes comments
 . environment division
 . input-output section
 . file-control
 .    select copybook-file assign to 'cob2csv.cpy'
          organization is line sequential

 . data division
 . file section
 . fd  copybook-file
 . 01  input-record                       pic x(256)
 . 01  input-card.
 .     05  columns-1-6                    pic  x(06)
 .     05  columns-7-72
 .         10                             pic  x(01)
 .         10  columns-8-72               pic  x(65)
 .     05  columns-73-80                  pic  x(08)

 . working-storage section
 . 01  persistent-variables
 .     05   value low-value               pic  x(01)
 .         88  file-open value 'y'
 .         88  file-closed value low-value
 .     05   value low-value               pic  x(01)
 .         88  free-form value 'f'.
 .         88  fixed-form value low-value.
 . 01  unqualified-variables.
 .     05  n                      binary  pic s9(04)
 .     05  n-plus-1               binary  pic s9(04)

 . procedure division.
       if  file-closed
           open input copybook-file
           set file-open to true
       end-if

       read copybook-file at end
           set end-of-copybook to true
           close copybook-file
           set file-closed to true
           move zero to line-length
           goback
       end-read

       if  fixed-form
           move 66 to line-length, line-limit
           move columns-7-72 to line-text
       else
           move 256 to line-length, line-limit
           move input-record to line-text
       end-if

       if  columns-7-72 equal to '$SET SOURCEFORMAT"FREE"' or
           columns-8-72 equal to '@OPTIONS SRF(FREE,FREE)'
           set free-form to true
           move zero to line-limit
       end-if
       if  columns-7-72 equal to '$SET SOURCEFORMAT"FIXED"' or
           columns-8-72 equal to '@OPTIONS SRF(FIX,FIX)'
           set fixed-form to true
           move zero to line-limit
       end-if
       if  line-byte (1) equal to '*' or '/'
           move zero to line-limit
       end-if
       move zero to line-length
       perform varying n from 1 by 1 until n greater than line-limit
           compute n-plus-1 = n + 1
           if  line-byte (n) equal to '*' and
               n less than line-length and
               line-byte (n-plus-1) equal to '>'
               exit perform
           end-if
           if  line-byte (n) not equal to space
               move n to line-length
           end-if
       end-perform
       if  line-length greater than zero
           inspect line-text converting
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ' to
              'abcdefghijklmnopqrstuvwxyz'
       end-if
       goback
 . end program read-copybook
 . end program parse

 . identification division
 . program-id. convert-file
*>  Copies the data file, converting to tsv format
 . environment division
 . input-output section
 . file-control
 .    select input-file assign to 'cob2csv.in'
          organization is record sequential
 .    select output-file assign to 'cob2csv.out'
          organization is line sequential

 . data division
 . file section
 . fd  input-file
 . 01                                     pic x(01)
 . fd  output-file
 . 01  output-record
 .     05  output-byte occurs 2000        pic  x(01)
 . working-storage section
 . 01  unqualified-variables.
 .     05  n                      binary  pic s9(04)
 .     05  l                      binary  pic s9(04)
 .     05  i                      binary  pic s9(04)
 .     05  o                      binary  pic s9(04)
 .     05  t                      binary  pic s9(04)
 .     05  t-limit                binary  pic s9(04)
 .     05  record-length          binary  pic s9(04)
 .     05  record-length-edited           pic  z(04)
 .     05  record-count value 0   binary  pic s9(09)
 .     05  record-count-edited            pic zzz,zzz,zzz
 .     05  input-number                   pic s9(15)
 .     05   redefines input-number
 .         10  input-number-byte occurs 15 pic  x(01)
 .     05  input-binary           comp-5  pic s9(18)
 .     05   redefines input-binary
 .         10  input-binary-byte occurs 8 pic  x(01)
*. If your machine is 32-bit, replace the above with:
*.     05  input-binary           comp-5  pic s9(09)
*.     05   redefines input-binary
*.         10  input-binary-byte occurs 4 pic  x(01)
 .     05  input-packed    packed-decimal pic s9(15)
 .     05   redefines input-packed.
 .         10  input-packed-byte occurs 8 pic  x(01)
 .     05  work-number                    pic s9(11)v9(04)
 .     05  edited-number                  pic -(11).9(04)
 .     05   redefines edited-number
 .         10  output-number-byte occurs 16 pic  x(01)
 .     05                                 pic  x(01)
 .         88  positive-number value '+'
 .         88  negative-number value '-'
 .     05  the-delimiter value ','        pic  x(01)
 . 01  input-record
 .     05  input-byte occurs 1 to 2000 depending on record-length pic x

 . procedure division.
*  If your compiler does not support the following, comment it
*  out and hardcode the delimiter above.
     display 'delimiter' upon environment-name
     accept the-delimiter from environment-value
     if  the-delimiter equal to space or low-value or high-value
         move ',' to the-delimiter
     end-if
     if  the-delimiter equal to 't' or 'T'
         move x'09' to the-delimiter
     end-if
     open input input-file output output-file
     compute record-length =
             layout-offset (layout-count) - 1 +
             (layout-length (layout-count) *
              layout-occurs (layout-count))
     move record-length to record-length-edited
     display '        Record length                 ' record-length-edited
     if  record-length greater than length of output-record
         display 'record too big ' record-length
         goback
     end-if

     perform until end-of-data-file
         perform varying i from 1 by 1 until i > record-length
             read input-file into input-byte (i) at end
                 set end-of-data-file to true
                 exit perform
             end-read
         end-perform
         if  not end-of-data-file
             add 1 to record-count
             perform reformat-record
             write output-record
         end-if
     end-perform

     close input-file output-file
     move record-count to record-count-edited
     display 'Record count: ' record-count-edited

     goback
 . reformat-record.
     move spaces to output-record
     move 1 to o
     perform varying l from 1 by 1 until l > layout-count
         move layout-offset (l) to i
         perform layout-occurs (l) times
             evaluate true
                 when type-string (l)
                     perform convert-string
                 when type-number (l)
                 when type-signed (l)
                     perform convert-number
                     perform output-a-number
                 when type-binary (l)
                     perform convert-binary
                     perform output-a-number
                 when type-packed (l)
                     perform convert-packed
                     perform output-a-number
             end-evaluate
             if  l < layout-count
                 move the-delimiter to output-byte (o)
                 add 1 to o
             end-if
             if  o greater than length of output-record
                 display 'output too big ' o space output-record
                 goback
             end-if
         end-perform
     end-perform
 . convert-string.
     perform layout-length (l) times
         move input-byte (i) to output-byte (o)
         if  output-byte (o) equal to the-delimiter
             subtract 1 from o
         end-if
         add 1 to i, o
     end-perform
     subtract 1 from o
     perform varying o from o by -1 until
         output-byte (o) not = space or o = 1
     end-perform
     add 1 to o
 . convert-number.
     move zero to input-number
     compute t = length of input-number - layout-length (l) + 1
     perform layout-length (l) times
         move input-byte (i) to input-number-byte (t)
         add 1 to i, t
     end-perform
     move input-number to work-number
 . convert-binary.
     move zero to input-binary
     if  input-byte (i) greater than x'7F'
         move -1 to input-binary
     end-if
     compute t = length of input-binary - layout-length (l) + 1
     perform layout-length (l) times
         move input-byte (i) to input-binary-byte (t)
         add 1 to i, t
     end-perform
*  If your machine is big-endian (e.g. a PC), replace the above with:
*    compute t = layout-length (l)
*    perform layout-length (l) times
*        move input-byte (i) to input-binary-byte (t)
*        add 1 to i
*        subtract 1 from t
*    end-perform
     move input-binary to work-number
 . convert-packed.
     move zero to input-packed
     compute t = length of input-packed - layout-length (l) + 1
     perform layout-length (l) times
         move input-byte (i) to input-packed-byte (t)
         add 1 to i, t
     end-perform
     move input-packed to work-number
 . output-a-number.
     perform layout-decimals (l) times
         divide 10 into work-number
     end-perform
     if  layout-decimals (l) equal to zero
         move 11 to t-limit
     else
         compute t-limit = 12 + layout-decimals (l)
     end-if
     move work-number to edited-number
     perform varying t from 1 by 1 until t > t-limit
         if  output-number-byte (t) not equal to space
             move output-number-byte (t) to output-byte (o)
             add 1 to o
         end-if
     end-perform
 . end program convert-file
 . end program cob2csv
 .
```

#### ↳ Re: convert Cobol file to csv

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-22T15:53:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QvGdnWpjjaPNqp3cRVn-ow@comcast.com>`
- **References:** `<40ffe958.70772793@news.optonline.net>`

```
How do I run this program?
```

##### ↳ ↳ Re: convert Cobol file to csv

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-22T23:35:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410047fe.95006951@news.optonline.net>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>How do I run this program?

Same as any other program -- compile to an executable and run by typing its name
on the command line or using a shortcut.

The problem is you don't have a Cobol compiler. Convince the organization who
sent the file to do it for you and send you the executable. Find a friend who
will do the same. Download the free Fujitsu compiler.
```

##### ↳ ↳ Re: convert Cobol file to csv

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T00:19:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41005795.98998162@news.optonline.net>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>How do I run this program?

We're not permitted to post in this newsgroup 'binary attachments' i.e. an
executable program.

Try stroking a programmer with access to a compiler.
```

###### ↳ ↳ ↳ Re: convert Cobol file to csv

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-23T13:03:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<---dnQtg6_-O_JzcRVn-oA@comcast.com>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com> <41005795.98998162@news.optonline.net>`

```
Would that be someone like you?

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:41005795.98998162@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
…[5 more quoted lines elided]…
> Try stroking a programmer with access to a compiler.
```

###### ↳ ↳ ↳ Re: convert Cobol file to csv

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-23T13:05:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vP2dnbiu3bPF_JzcRVn-sA@comcast.com>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com> <41005795.98998162@news.optonline.net>`

```
If you need to explain to me what a  'binary attachment' i.e. an  executable
program is, don't you think I may be a little bit er, dense to run your
compiler program?



"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:41005795.98998162@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
…[5 more quoted lines elided]…
> Try stroking a programmer with access to a compiler.
```

###### ↳ ↳ ↳ Re: convert Cobol file to csv

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T00:13:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4101a62e.25907446@news.optonline.net>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com> <41005795.98998162@news.optonline.net> <vP2dnbiu3bPF_JzcRVn-sA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>If you need to explain to me what a  'binary attachment' i.e. an  executable
>program is, don't you think I may be a little bit er, dense to run your
>compiler program?

I used to have a girlfriend who had Dumb Blonde refined to such a level that car
mechanics would drop what they were doing to work on her car first, then wave
off payment. Sample of her style "I want you to check allll my fluids." 

She had a physics degree from MIT, authored several books and was a feminist.
Wasn't Dumb Blonde demeaning to women? She shrugged, saying it got the job done
and was lots of fun.

She would have turned binary attachment into a double entendre joke.



>"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
>news:41005795.98998162@news.optonline.net...
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: convert Cobol file to csv

_(reply depth: 5)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T00:37:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P82dnYpYFcoVnp_cRVn-rg@comcast.com>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com> <41005795.98998162@news.optonline.net> <vP2dnbiu3bPF_JzcRVn-sA@comcast.com> <4101a62e.25907446@news.optonline.net>`

```
Sounds like she dumped you.


"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:4101a62e.25907446@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
> >If you need to explain to me what a  'binary attachment' i.e. an
executable
> >program is, don't you think I may be a little bit er, dense to run your
> >compiler program?
>
> I used to have a girlfriend who had Dumb Blonde refined to such a level
that car
> mechanics would drop what they were doing to work on her car first, then
wave
> off payment. Sample of her style "I want you to check allll my fluids."
>
> She had a physics degree from MIT, authored several books and was a
feminist.
> Wasn't Dumb Blonde demeaning to women? She shrugged, saying it got the job
done
> and was lots of fun.
>
…[10 more quoted lines elided]…
> >> We're not permitted to post in this newsgroup 'binary attachments' i.e.
an
> >> executable program.
> >>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: convert Cobol file to csv

_(reply depth: 6)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-07-24T11:59:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9MvMc.44380$Gf7.1570298@news20.bellglobal.com>`
- **In-Reply-To:** `<P82dnYpYFcoVnp_cRVn-rg@comcast.com>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com> <41005795.98998162@news.optonline.net> <vP2dnbiu3bPF_JzcRVn-sA@comcast.com> <4101a62e.25907446@news.optonline.net> <P82dnYpYFcoVnp_cRVn-rg@comcast.com>`

```
Carol wrote:
> Sounds like she dumped you.
> 

LOL ... you do have away with words ...

Donald
```

###### ↳ ↳ ↳ Re: convert Cobol file to csv

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T17:41:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41029ef8.18106826@news.optonline.net>`
- **References:** `<40ffe958.70772793@news.optonline.net> <QvGdnWpjjaPNqp3cRVn-ow@comcast.com> <41005795.98998162@news.optonline.net> <vP2dnbiu3bPF_JzcRVn-sA@comcast.com> <4101a62e.25907446@news.optonline.net> <P82dnYpYFcoVnp_cRVn-rg@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>Sounds like she dumped you.

She wanted to play; I wanted a long-term relationship. She thought they were
mutually exclusive; I didn't.
```

#### ↳ Re: Demo: convert Cobol file to csv

- **From:** "Dub" <scott.robbs@firstextended.com>
- **Date:** 2005-01-05T14:39:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bf6774ef45cbb16ccf7146d83be26d9@localhost.talkaboutprogramming.com>`
- **References:** `<40ffe958.70772793@news.optonline.net>`

```
I see the copybook, but not a delemited file of it, I also don't see a data
file.  Also what does it take to get complete copies of the programs, as
advertized this is what I need.
Dub
```

##### ↳ ↳ Re: Demo: convert Cobol file to csv

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-05T21:42:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fhnot0pp1n9k5ml7omh2mpps170epvq169@4ax.com>`
- **References:** `<40ffe958.70772793@news.optonline.net> <7bf6774ef45cbb16ccf7146d83be26d9@localhost.talkaboutprogramming.com>`

```
On Wed, 05 Jan 2005 14:39:31 -0500, "Dub"
<scott.robbs@firstextended.com> wrote:

>I see the copybook, but not a delemited file of it, I also don't see a data
>file.  Also what does it take to get complete copies of the programs, as
>advertized this is what I need.

The delimited file is shown right after the copybook. An input data
file can easily be made with your text editor; columns for the fields
are shown on the sample report. The complete program is in Google's
archive. Get it in your browser and do a SaveAs.

http://groups-beta.google.com/group/comp.lang.cobol/browse_thread/thread/dc52411acc35c5c0/41ceca276724555f
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
