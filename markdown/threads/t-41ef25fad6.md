[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ignoring Duplicates

_21 messages · 15 participants · 1998-07_

---

### Ignoring Duplicates

- **From:** cslvt@hotmail.com
- **Date:** 1998-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
Hi folks,
I'm writing a program (COBOL 74) that, among other things, reads in records
from a file, applies some conditions to it and then stores the data in an
array.  One condition is that duplicate records should be ignored.  Only the
newest (closest to the end of the file) should be stored.  My first instinct
was to compare each record to all the other records, but I'm having problems
with intrementing the input (I'm a master programmer by no means). Any
suggestions or direction?

Kam

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Ignoring Duplicates

- **From:** dilbert_programmer@my-dejanews.com
- **Date:** 1998-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o886k$f51$1@nnrp1.dejanews.com>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
In article <6o85rb$c44$1@nnrp1.dejanews.com>,
  cslvt@hotmail.com wrote:
> Hi folks,
> I'm writing a program (COBOL 74) that, among other things, reads in records
…[11 more quoted lines elided]…
>
If it is possible can you sort the input file by the key you are trying to
compare.  It then becomes relatively simple to


- create a save record area
- initialize it to low-value or something
loop
   - read a record
   - save the key/record
   - is the record key the same as the last key
      - no
        - is the save area low-values
          - no - add the saved record to your array
          - yes - move current record to save area

      - yes replace save record with new record
end loop

If you are putting this into an array I hope the file isnt too big.

Another option assuming the file isng to big is

read a record
search the array for the same key if it found replace that element
if it is not found just add it to the array

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: Ignoring Duplicates

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AA1510.2A1AE5D9@zip.com.au>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com> <6o886k$f51$1@nnrp1.dejanews.com>`

```
When sorting using DFSORT use the EQUALS option to ensure that the
specific order of records is maintained.

dilbert_programmer@my-dejanews.com wrote:
> 
> In article <6o85rb$c44$1@nnrp1.dejanews.com>,
…[41 more quoted lines elided]…
> http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Ignoring Duplicates

- **From:** Grehom@my-dejanews.com
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oa89h$sho$1@nnrp1.dejanews.com>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
I'm a Cobol professional of fifteen years standing and when I read this I
thought sounds easy enough - but then I thought 'search' array for existing
key value and merely overwrite duplicates with newer later value, appending
new keys to end of array.  If you wanted to get clever could use 'search all'
but this requires that key is in sorted order so means a fair amount of
playing around inserting new values into existing array to keep it in sorted
order. I'm now going to commit sacrilege on a Cobol news group entry and say
if your new to Cobol try and learn Perl as well/instead. (see
http://language.perl.com/index.html) a short program like:

    #!/usr/bin/perl -w
    $key_start = 3;    # constant stating where on record key starts
    $key_length = 10;; # constant stating how long key is
    while (<>) {
        $key = substr($_,$key_start,$key_length);
        $array{$key} = $_;
    }
    foreach (@array) {
        print;
    }

would do it all!!  available on most machines and operating systems.

In article <6o85rb$c44$1@nnrp1.dejanews.com>,
  cslvt@hotmail.com wrote:
> Hi folks,
> I'm writing a program (COBOL 74) that, among other things, reads in records
…[11 more quoted lines elided]…
>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: Ignoring Duplicates

- **From:** RandallBart <Barticus@att.spam.net>
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ob6mc$nqk@bgtnsc03.worldnet.att.net>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com> <6oa89h$sho$1@nnrp1.dejanews.com>`

```
Grehom@my-dejanews.com wrote:
> 
>  I'm now going to commit sacrilege on a Cobol news group entry and say
…[3 more quoted lines elided]…
>     #!/usr/bin/perl -w

    IF  SUGGESTING-PERL IN COMP-LANG-COBOL IS SACRILEGE
        PERFORM DRAW THRU QUARTER. 
```

##### ↳ ↳ Re: Ignoring Duplicates

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298192.75223.8946@kcbbs.gen.nz>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com>`

```
> In article <6o85rb$c44$1@nnrp1.dejanews.com>,
>   cslvt@hotmail.com wrote:
…[7 more quoted lines elided]…
> > suggestions or direction?

Easy: write the data to an ISAM file keyed on what would be
considered duplicates - rewriting later records when they 
occur, then read the final file into the array.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

- **From:** "Dave Johnson" <systemad@globalnet.co.uk>
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6obedt$7ou$3@heliodor.xara.net>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz>`

```
Richard Plinston wrote in message <3298192.75223.8946@kcbbs.gen.nz>...
>> In article <6o85rb$c44$1@nnrp1.dejanews.com>,
>>   cslvt@hotmail.com wrote:
>> > Hi folks,
>> > I'm writing a program (COBOL 74) that, among other things, reads in
records
>> > from a file, applies some conditions to it and then stores the data in
an
>> > array.  One condition is that duplicate records should be ignored.
Only the
>> > newest (closest to the end of the file) should be stored.  My first
instinct
>> > was to compare each record to all the other records, but I'm having
problems
>> > with intrementing the input (I'm a master programmer by no means). Any
>> > suggestions or direction?
…[4 more quoted lines elided]…
>
Yes, removes all the 'how many do I expect' problems you'd get with tables.
Anyone got any thoughts on the method, eg whether you try an insert and trap
the 'duplicate key', or read first. According to the last sysprog I worked
with,
you were better off reading first as this loaded data and index blocks,
whereas
a write just loaded the index block.

DaveJ.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 4)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6obvvj$238@bgtnsc03.worldnet.att.net>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net>`

```
Dave Johnson wrote:
> 
> Richard Plinston wrote in message <3298192.75223.8946@kcbbs.gen.nz>...
…[26 more quoted lines elided]…
> a write just loaded the index block.

ISAM? Are you running on a PC platform? Sounds like a good idea, writing
to a keyed file and reading it in when done. Since the spec calls for
retaining the newest, i.e., the one closest to EOF, I'd precede every
WRITE with a DELETE for the key to eliminate the test for duplicate key,
read for update & rewrite. YMMV

Bill Lynch

> 
> DaveJ.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 5)_

- **From:** "Dennis J. Minette" <d.minette@computer.org>
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<usQaXXjr9GA.255@upnetnews05>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net> <6obvvj$238@bgtnsc03.worldnet.att.net>`

```


Bill Lynch wrote in message <6obvvj$238@bgtnsc03.worldnet.att.net>...
>Dave Johnson wrote:
>>
…[6 more quoted lines elided]…
>> >> > from a file, applies some conditions to it and then stores the data
in
>> an
>> >> > array.  One condition is that duplicate records should be ignored.
…[5 more quoted lines elided]…
>> >> > with intrementing the input (I'm a master programmer by no means).
Any
>> >> > suggestions or direction?
>> >
>> >Easy: write the data to an ISAM file keyed on what would be
>> >considered duplicates - rewriting later records when they
>> >occur, then read the final file into the array.


As an implementation of the "Easy" technique (maybe not so "easy" for a
non-master programmer?), here is an example of the coding methodology I have
used successfully in the past to save the most recent duplicate key records
from a sequential file into an ISAM file for subsequent loading of a table
(note that this works most efficiently if there are not an overly large
number of duplicates):

MAIN-CONTROL.
    OPEN INPUT SEQ-FILE.
    OPEN OUTPUT ISAM-FILE.
    CLOSE ISAM-FILE.
*       above 2 lines assures an empty isam file to start with
    OPEN I-O ISAM-FILE.
    MOVE "NO" TO SEQ-FILE-EOF-SW.
     READ SEQ-FILE INTO ISAM-FILE-REC
        AT END MOVE "YES" TO SEQ-FILE-EOF-SW.
   PERFORM DUPE_LOOP UNTIL SEQ-FILE-EOF.
    CLOSE SEQ-FILE ISAM-FILE.
    OPEN INPUT ISAM-FILE.
    MOVE "NO" TO ISAM-FILE-EOF-SW.
    READ ISAM-FILE NEXT RECORD
        AT END MOVE "YES" TO ISAM-FILE-EOF-SW.
    PERFORM TABLE-FILL-AND-PROCESS
        UNTIL ISAM-FILE-EOF.
    CLOSE ISAM-FILE.
    .....  perform main-line logic here that uses your table
    STOP RUN.

DUPE_LOOP.
    WRITE ISAM-FILE-REC
        INVALID KEY
            MOVE SEQ-FILE-REC TO ISAM-FILE-REC
            READ ISAM-FILE
                INVALID KEY
                    DISPLAY "......... READ ABEND INFO"
                    STOP RUN
            END-READ
            MOVE SEQ-FILE-REC TO ISAM-FILE-REC
            REWRITE ISAM-FILE-REC
                INVALID KEY
                    DISPLAY "......... REWRITE ABEND INFO"
                    STOP RUN.
    READ SEQ-FILE INTO ISAM-FILE-REC
        AT END MOVE "YES" TO SEQ-FILE-EOF-SW.

TABLE-FILL-AND-PROCESS.
    ....  do whatever you are going to do with this unique entry into your
table
    READ ISAM-FILE NEXT RECORD
        AT END MOVE "YES" TO ISAM-FILE-EOF-SW.


>> >
>> Yes, removes all the 'how many do I expect' problems you'd get with
tables.
>> Anyone got any thoughts on the method, eg whether you try an insert and
trap
>> the 'duplicate key', or read first. According to the last sysprog I
worked
>> with,
>> you were better off reading first as this loaded data and index blocks,
>> whereas
>> a write just loaded the index block.


Reading first would probably be most efficient if there is a relatively
large number of duplicate key records involved.  In that case, I would
replace the DUPE-LOOP paragraph in the sample I have given above with
something like the following:

DUPE-LOOP.
   READ ISAM-FILE
       INVALID KEY
            MOVE SEQ-FILE-REC TO ISAM-FILE-REC
            WRITE ISAM-FILE
                INVALID KEY
                    DISPLAY "......... WRITE ABEND INFO"
                    STOP RUN
            END-WRITE
       VALID KEY
            MOVE SEQ-FILE-REC TO ISAM-FILE-REC
            REWRITE ISAM-FILE
                INVALID KEY
                    DISPLAY "......... REWRITE ABEND INFO"
                    STOP RUN
            END-REWRITE.
    READ SEQ-FILE INTO ISAM-FILE-REC
        AT END MOVE "YES" TO SEQ-FILE-EOF-SW.

>
>ISAM? Are you running on a PC platform? Sounds like a good idea, writing
…[3 more quoted lines elided]…
>read for update & rewrite. YMMV


In the case of always DELETE and then WRITE, I would replace the DUPE-LOOP
paragraph in the sample I have given  with something like this (but I have
no feel for the relative efficiency of this method):

DUPE-LOOP.
   DELETE ISAM-FILE RECORD
       INVALID KEY
*    does not matter if record to be deleted does not exist!
            NEXT SENTENCE.
    MOVE SEQ-FILE-REC TO ISAM-FILE-REC.
    WRITE ISAM-FILE
            INVALID KEY
                DISPLAY "......... WRITE ABEND INFO"
                STOP RUN.
    READ SEQ-FILE INTO ISAM-FILE-REC
        AT END MOVE "YES" TO SEQ-FILE-EOF-SW.

>
>Bill Lynch
>
>>
>> DaveJ.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 6)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298193.73139.17092@kcbbs.gen.nz>`
- **References:** `<usQaXXjr9GA.255@upnetnews05>`

```
In message <<usQaXXjr9GA.255@upnetnews05>> "Dennis J. Minette" <d.minette@computer.org> writes:
> >
> >ISAM? Are you running on a PC platform? Sounds like a good idea, writing

Umm, yes, PC, for the last nearly 20 years if CP/M, MP/M and
other 8 bit and 16 bit platforms count as Personal Computers.

> >to a keyed file and reading it in when done. Since the spec calls for
> >retaining the newest, i.e., the one closest to EOF, I'd precede every
…[5 more quoted lines elided]…
> no feel for the relative efficiency of this method):

I would expect that DELETE and WRITE would be the least efficient
as the DELETE would update (or downdate) the index file only to
have it restored by the WRITE.  

It would be possible to always do a REWRITE and do a WRITE if
this fails, possibly the most efficient, but would look a
little odd, especially to those who think that a READ is
required first.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 6)_

- **From:** Binyamin_Dissen@theoffice.net (Binyamin Dissen)
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35b6181a.34909854@news.netvision.net.il>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net> <6obvvj$238@bgtnsc03.worldnet.att.net> <usQaXXjr9GA.255@upnetnews05>`

```
The easiest and fastest way to do this is sort of:

    SD  SORT-FILE .....
    01  SORT-REC.
        05   KEY-FIELD   ....
        05   remaining fields ....
        05   INPUT-SEQUENCE  PIC S9(8) COMP.


    77  INPUT-COUNTER   PIC  S9(8) COMP SYNC VALUE 0.
    01  SAVE-RECORD .....               

        SORT  SORT-FILE
            ASCENDING KEY KEY-FIELD INPUT-COUNTER  
            INPUT PROCEDURE  IN-PROC
            OUTPUT PROCEDURE OUT-PROC.

   IN-PROC SECTION.
        Open files, etc.
        READ  source-file AT END SET eof-detected TO TRUE.
        PERFORM  UNTIL  eof-detected
              ADD 1 TO INPUT-COUNTER
              MOVE input-fields TO sort-fields
              MOVE INPUT-COUNTER TO INPUT-SEQUENCE
              RELEASE SORT-REC
              READ source-file AT END SET eof-detected TO TRUE.
        Close files.

    OUT-PROC SECTION.
        Open files, etc.
        RETURN SORT-REC INTO SAVE-RECORD AT END SET eof-detected TO TRUE.
        PERFORM  UNTIL  eof-detected
              IF  KEY-FIELD OF SAVE-RECORD NOT EQUAL KEY-FIELD OF SORT-REC
                  MOVE SAVE-RECORD TO output-fields
                  WRITE output-file
              END IF
              MOVE SORT-REC TO SAVE-REC
              RETURN SORT-REC AT END SET eof-detected TO TRUE.
        MOVE SAVE-RECORD TO output-fields
        WRITE output-file
        Close files.

Probably a few syntax errors here and there, but using ISAM to sort a file is
probably about the slowest way to do it. And if there is support for SORT
DUPLICATES then USING / OUTPUT PROCEDURE will do the job.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 7)_

- **From:** "Dave Johnson" <systemad@globalnet.co.uk>
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6odt1s$h82$2@heliodor.xara.net>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net> <6obvvj$238@bgtnsc03.worldnet.att.net> <usQaXXjr9GA.255@upnetnews05> <35b6181a.34909854@news.netvision.net.il>`

```
Does this hold for PCs, Benyamin - last time I tried a big sort
(late '80s) I was less than impressed.

DaveJ.

Binyamin Dissen wrote in message
<35b6181a.34909854@news.netvision.net.il>...
>The easiest and fastest way to do this is sort of:
>
…[40 more quoted lines elided]…
>Probably a few syntax errors here and there, but using ISAM to sort a file
is
>probably about the slowest way to do it. And if there is support for SORT
>DUPLICATES then USING / OUTPUT PROCEDURE will do the job.
…[5 more quoted lines elided]…
>Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pmvq1.7$Gp.213556@news1.atlantic.net>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net> <6obvvj$238@bgtnsc03.worldnet.att.net> <usQaXXjr9GA.255@upnetnews05> <35b6181a.34909854@news.netvision.net.il> <6odt1s$h82$2@heliodor.xara.net>`

```
In my experience, especially with PCs!

I had numerous problems with memory fragmentation when
using the SORT verb. This created a problem wherein
the program would run to completion but the records
were not correctly sorted. By replacing the SORT with
an ISAM file, the problem was solved.
---------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >

Dave Johnson wrote in message <6odt1s$h82$2@heliodor.xara.net>...
>Does this hold for PCs, Benyamin - last time I tried a big sort
>(late '80s) I was less than impressed.
…[6 more quoted lines elided]…
>>
[...ISAM code deleted]
>>--
>>Binyamin_Dissen@theoffice.net
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 4)_

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35aa17c3.7857384@usenet.acw.vcu.edu>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net>`

```
"Dave  Johnson" <systemad@globalnet.co.uk> wrote:

>Richard Plinston wrote in message <3298192.75223.8946@kcbbs.gen.nz>...
>>> In article <6o85rb$c44$1@nnrp1.dejanews.com>,
…[25 more quoted lines elided]…
>a write just loaded the index block.

The way I would do it in VSAM is:

850-Write-record-VSAM.
Write input-record.
If ws-file-status is equal to 22
	Rewrite input-record
end-if.
If ws-file-status is not equal to zeros
	Perform 999-process-VSAM-Error
End-if.

Boyce G. Williams, Jr.

 .--------------------------------------------------------------------.
 | "People should have two virtues:  purpose- the courage to envisage |
 | and pursue valued goals uninhibited by the defeat of infantile     |
 | fantasies, by guilt and the failing fear punishment;  and wisdom- a|
 | detached concern with life itself, in the face of death itself."   |
 |                                                     Norman F. Dixon|
 '--------------------------------------------------------------------'
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oekr2$ijk@bgtnsc02.worldnet.att.net>`
- **References:** `<6oa89h$sho$1@nnrp1.dejanews.com> <3298192.75223.8946@kcbbs.gen.nz> <6obedt$7ou$3@heliodor.xara.net> <35aa17c3.7857384@usenet.acw.vcu.edu>`

```
Boyce G. Williams, Jr. wrote:
> 
> "Dave  Johnson" <systemad@globalnet.co.uk> wrote:
…[40 more quoted lines elided]…
> 

If the WRITE fails, wouldn't you have to do a READ for UPDATE before the
REWRITE? The one place where I have some experience with this is in a
CICS program, where I need the READ for UPDATE. The objective is not to
sort the incoming records, but to create a file with the latest occasion
of an externally generated id (from DTC, if that rings any bells). This
file is a user-maintained alternate index to our file of open trades
(way too many dupes to make it a real AIX).

Bill Lynch

> Boyce G. Williams, Jr.
> 
…[6 more quoted lines elided]…
>  '--------------------------------------------------------------------'
```

#### ↳ Re: Ignoring Duplicates

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35b0e450.3574299@nntp.ix.netcom.com>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
 One condition is that duplicate records should be ignored.  Only the
>newest (closest to the end of the file) should be stored.  My first instinct
>was to compare each record to all the other records, but I'm having problems
>with intrementing the input (I'm a master programmer by no means). Any
>suggestions or direction?



umm, yes. do the following (at your own risk) (pseudo code):

errm. bug report: write buffer should mean add that buffer
to your array.

declare alternating-buffer-variable
declare has-first-record-been-read
declare 2 record buffers

set alternating-buffer-variable to 1
set has-first-record-been-read to false

perform until end-of-file
	evaluate alternating-buffer and has-first-record
	when 1 and true
		read into buffer1 a record
		compare buffer2 to buffer1
		if different buffers, write buffer2
		set alt-buffer to 2
	when 1 and false
		read into buffer1 a record
		set alt-buffer to 2
	when 2 and true
		read into buffer2 a record
		compare
		if dif, write buf1
		set alt to 1
	end-evaluate
	set has-first to true
perform final-record.

end program


final-record.
evaluate alternating-buffer and has-first-record
	when 1 and true
		read into buffer1 a record
		compare buffer2 to buffer1
		if different fields, write buffer2
		set alt-buffer to 2
	when 1 and false
		read into buffer1 a record
		set alt-buffer to 2
	when 2 and true
		read into buffer2 a record
		compare
		if dif, write buf1
		set alt to 1
	end-evaluate



gvwmoore@ix.spam.netcom.com to reply remove the spam
```

##### ↳ ↳ Re: Ignoring Duplicates

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298193.71879.16074@kcbbs.gen.nz>`
- **References:** `<35b0e450.3574299@nntp.ix.netcom.com>`

```
In message <<35b0e450.3574299@nntp.ix.netcom.com>> gvwmoore@ix.netcom.com  writes:
> >newest (closest to the end of the file) should be stored.  My first instinct
> >was to compare each record to all the other records, but I'm having problems
…[11 more quoted lines elided]…
>  evaluate alternating-buffer and has-first-record

This seems to assume that the records are in ascending 
sequence of some key, which isn't stated.  It may be, for
example a log file of randomly changing states of several
devices where only the last state is required.  They
won't be adjacent.
```

###### ↳ ↳ ↳ Re: Ignoring Duplicates

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35adcd56.1785831@nntp.ix.netcom.com>`
- **References:** `<35b0e450.3574299@nntp.ix.netcom.com> <3298193.71879.16074@kcbbs.gen.nz>`

```
On 13 Jul 98 19:57:59 GMT, riplin@kcbbs.gen.nz (Richard Plinston)
wrote:

>This seems to assume that the records are in ascending 
>sequence of some key, which isn't stated.  It may be, for
>example a log file of randomly changing states of several
>devices where only the last state is required.  They
>won't be adjacent.

hmm. good point. before that code is executed, you
should write the entire record structure in ascending
order to a temporary file. and you might as well
apply the conditions (excluding the duplicate condition)
to that file, so that you dont have to read too many records
the second time around.








gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: Ignoring Duplicates

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35aa03eb.2776838@usenet.acw.vcu.edu>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
cslvt@hotmail.com wrote:

>Hi folks,
>I'm writing a program (COBOL 74) that, among other things, reads in records
…[5 more quoted lines elided]…
>suggestions or direction?

Let's see:  you want to process a file that will ignore duplicate
records except for the last record of the group.  Simple.

The trick to this is how to ID the last record of a group of records.
If you have a date or counter already in the record that makes each
record unique and in sequence desired then you can sort by your
"duplicate" primary key then by date/counter.  If you don't or the
file was just a "collection" file (the most recent data was the last
physical record entered) then assign a number to an unused field or
move the record to a working-stroage group with some extra fields at
the end to pad with and increment a number to the pad.  As long you
are not saving the record you don't have a problem.

Normally the code looks like this:

000-Mainline.
1.  Open the files.
2.  Initialize the variable fields.
3.  SORT file ascending key primary
              ascending key counter (or date, if used)
        input procedure 200-process-file-inputfile
       output procedure 300-process-file-sortfile.
4.  Close the files.

200-process-file-inputfile.
1.  Do a priming read.
Perform until end-of-file:
    2.  Assign an incremented counter to the record
          (assuming there is nothing that makes each record unique
           and in the order read already) 
    3.  Release the record
    4.  read the next record.
end-perform.

300-process-file-sortfile
1.  Do a priming return.
Perform until end-of-file:
	2. Assign the 1st group's primary key to a Working-stroage field.
	Perform until end-of-file
        or 1st group's primary key differs 
        from its Working-stroage counterpart:
		3.  Assign the record to a second group with the
               identical layout.
		4.  Return the next record.
	end-perform
	5.  Process the second group.
end-perform

This assumes you're using the "READ...INTO"/"RETURN...INTO" method,
hence the need for two identical layouts in WORKING-STORAGE.  The rest
is left as an exercise.

Boyce G. Williams, Jr.

 .--------------------------------------------------------------------.
 | "People should have two virtues:  purpose- the courage to envisage |
 | and pursue valued goals uninhibited by the defeat of infantile     |
 | fantasies, by guilt and the failing fear punishment;  and wisdom- a|
 | detached concern with life itself, in the face of death itself."   |
 |                                                     Norman F. Dixon|
 '--------------------------------------------------------------------'
```

#### ↳ Re: Ignoring Duplicates

- **From:** Len Lewandowski <leonardl@execpc.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ogsam$8a0@newsops.execpc.com>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
Assuming you are on an IBM mainframe, sort will eliminate duplicate records by
itself.  I believe you use a sort sum???  Otherwise sort on the your key. Then
run the sorted file into your program and do normal break logic (saving the
input record & processing it on a key break) and remember to process you last
record since you will not have a normal key break.  Easy as pie.  Good luck.

cslvt@hotmail.com wrote:

> Hi folks,
> I'm writing a program (COBOL 74) that, among other things, reads in records
…[10 more quoted lines elided]…
> http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Ignoring Duplicates

- **From:** aacinstrjc@aol.com (AACInstrJC)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071406271400.CAA19950@ladder01.news.aol.com>`
- **References:** `<6o85rb$c44$1@nnrp1.dejanews.com>`

```
Kam writes :
<<<Hi folks,
I'm writing a program (COBOL 74) that, among other things, reads in records
from a file, applies some conditions to it and then stores the data in an
array.  One condition is that duplicate records should be ignored.  Only the
newest (closest to the end of the file) should be stored.  My first instinct
was to compare each record to all the other records, but I'm having problems
with intrementing the input (I'm a master programmer by no means). Any
suggestions or direction? >>>

When you say that duplicates should be ignored you give me the impression that
there is a key field or fields identifiy the input record and if there is and
its numeric you may have an easy answer to your problem.   As a quick and
oversiplified example lets say we have have a file containing sales tax rates
for 50 states* in historical order.   A two digit state code identifies the
state and there are duplicates with the most current towards the rear of the
file.  If you do nothing more than :
         move in-state-rate to tab-state-rate(in-state-code)

the records will be placed in the proper order in the array and with the most
current overlaying the older records.

I couldn't really say any more without knowing how you identify dupilcates
coming from the input file.

Regards,
Jim Castro
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
