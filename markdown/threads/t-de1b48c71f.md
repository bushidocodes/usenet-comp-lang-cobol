[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help in Finding Information

_16 messages · 11 participants · 2000-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help in Finding Information

- **From:** akent@seanet.com (Arthur M. Kent)
- **Date:** 2000-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
I need some assistance with locating a "string" within a record.  Let me
first explain the "particulars".

I am using COBOL in an OS 390 environment.  I will need to read a
sequential file, each record of fixed length 340 bytes.  The "string" I am
looking for is located within bytes 206 through 250 inclusive, but the
beginning of the "string" is not always in the same location within the
bytes 206 through 250 inclusive.

The "string" I am attempting to find is 11 bytes long, beginning with the
letter T (capitalized, as shown).  Once I have located this first
occurrence of the T, I need to be able to "easily" verify that the 11th
byte of this string is also the letter T.  Finally, once I have this 11
byte "string" with the two Ts, I need to determine if the 7th byte, within
the 11 bytes, is a dash "-".  The 2nd through 10th bytes will either
always be numeric, or will be of the format 99999-999, where each 9, of
course, is a number.  Here are two examples of such "strings":

   T120956688T

   T13466-122T

I don't believe the INSPECT verb will help be locate the first occurrence
of the letter T.  Even if it did, how can I "easily" analyze the 11 bytes
for the conditions stated above?

I realize that I could move bytes 206 through 250 into a array of length
45 bytes, and then analyze each byte sequentially, but this seems rather
"ugly" and complex.  I am looking for a simpler solution.

Any advice/comments etc. would be appreciated.  If you wish to send your
comments via EMail, my EMail address is akent@seanet.com.

Thank You,
Arthur M. Kent
```

#### ↳ Re: Help in Finding Information

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bZ7a5.12474$HD6.350172@iad-read.news.verio.net>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
In article <akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>,
Arthur M. Kent <akent@seanet.com> wrote:
>I need some assistance with locating a "string" within a record.  Let me
>first explain the "particulars".
…[5 more quoted lines elided]…
>bytes 206 through 250 inclusive.

    SET STRING-NOT-FOUND TO TRUE.
    PERFORM VARYING SUB1 FROM 206 BY 1
     UNTIL SUB1 > 250 OR STRING-FOUND
        IF WS-INREC(SUB1:1) = 'T'
            MOVE WS-INREC(SUB1:45) TO WS-PIC-X-45-FLD
            PERFORM DO-MORE-EDITS-N-TESTS THRU DMENT-EXIT
        END-IF
    END-PERFORM.

    IF STRING-FOUND
        (do some stuff)
    ELSE
        (do some other stuff)
    END-IF.

...
DO-MORE-EDITS-N-TESTS.

(I'll leave the rest of the coding to you... I set this up as a separate
paragraph rather than as a continuation of the inline PERFORM because over
time your edit requirements *will* change... easier to deal with in a
paragraph, I'd say)

    IF ALL-CONDITIONS-MET
        SET STRING-FOUND TO TRUE
    END-IF.

DMENT-EX.
    EXIT.    

[snippage]

>I realize that I could move bytes 206 through 250 into a array of length
>45 bytes, and then analyze each byte sequentially, but this seems rather
>"ugly" and complex.  I am looking for a simpler solution.

... to a complex problem?  What are you doing, bucking for Management?

DD
```

#### ↳ Re: Help in Finding Information

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000710173511.01839.00002629@nso-cb.aol.com>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
In article <akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>,
akent@seanet.com (Arthur M. Kent) writes:

>bytes 206 through 250 inclusive.
>
…[10 more quoted lines elided]…
>

Have you tried something like :

77 const-offset-206 pic 9(04) comp value 206.
77 var-offset-206-firstt pic 9(04) comp.
77 var-offset-206-lastt pic 9(04) comp.
77 var-offset-206-dash pic 9(04) comp.

move zero to tally
inspect <your-record>(const-offset-206:45) tallying all characters before
initial 'T'
if tally < 45  *>we have a hit!!
  compute var-offset-206-firstt = const-offset-206 + tally + 1 *> should be ON
'T'
  compute var-offset-206-lastt = var-offset-206-firstt + 10       *> should be
ON 'T'
  compute var-offset-206-dash = var-offset-206-firstt + 6       *> should be ON
'-'
  if var-offst-206-lastt <= 250   *> we have a good field to work with
    if (<your-record>(var-offset-206-firstt:1) = 'T') and
       (<your-record>(var-offset-206-lastt:1) = 'T')  *> we have your validated
string
       if <your-record>(var-offset-206-dash:1) = '-'  
           *** do what you need for dash formatted number ***
       else
           *** do what you need for NO dash formatted number ***
         end-if
      end-if
   end-if

Hope this helps
```

#### ↳ Re: Help in Finding Information

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YG8a5.2749$HD.449159@dfiatx1-snr1.gtei.net>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
Arthur M. Kent <akent@seanet.com> wrote in message
news:akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net...
> I need some assistance with locating a "string" within a record...
> I don't believe the INSPECT verb will help be locate the first occurrence
> of the letter T.....

Well, with your other edit requirements, I think the indexed table approach
is probably the right one, but you can use INSPECT to find the first
occurence of a literal in a string...AND I think you'll want to refresh your
memory on reference modification, too......


* working storage for later use with reference modification
01 CHECK-AREA.
    05 FILLER            PIC X(01).
    05 CHAR-2-7        PIC X(06).
    05 CHAR8            PIC X(01)
    05 FILLER            PIC X(02).
    05  LAST-CHAR    PIC X(01).


 MOVE ZERO TO WHERE-IT-IS
 INSPECT THE-DATA-NAME TALLYING WHERE-IT-IS FOR CHARACTERS BEFORE INITIAL
'T'
 IF WHERE-IT-IS NOT EQUAL FUNCTION LENGTH(THE-DATA-NAME)
   ADD 1 TO WHERE-IT-IS
   DISPLAY 'FOUND T AT ' WHERE-IT IS
   MOVE THE-DATA-NAME (Where-it-is:11) to CHECK-AREA
   IF CHAR-2-7 IS NUMERIC AND CHAR8 = '-' AND LAST-CHAR EQUAL 'T' THEN
      DISPLAY 'WHOOPEE ITS A GOOD RECORD'
.....

MCM
```

#### ↳ Re: Help in Finding Information

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396b97b2.5118955@news1.frb.gov>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
On Sun, 09 Jul 2000 14:27:11 -0700, Arthur M. Kent wrote:

[snip]
>
>The "string" I am attempting to find is 11 bytes long, beginning with the
>letter T (capitalized, as shown).  [...]

INSPECT record-area TALLYING counter FOR CHARACTERS BEFORE INITIAL "T"

...and then use the counter either as a subscript into a table or as a
pointer in an UNSTRING statement.
```

#### ↳ Re: Help in Finding Information

- **From:** "Alan H Russell" <RUSSELAH@apci.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kkodm$iar@netnews1.apci.com>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
"Arthur M. Kent" <akent@seanet.com> wrote in message
news:akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net...
> I need some assistance with locating a "string" within a record.  Let me
> first explain the "particulars".
…[32 more quoted lines elided]…
> Arthur M. Kent

Although the program is proprietary and I can't send it to you, we have a
"file split" program here (which I helped write in assembler) that can
accomplish your task with the proper PARM.  I would simply use a parm of
((206/250#TNNNNNNNNNT).OR.(206/250#TNNNNN-NNNNT))

Rather a powerful utility program, isn't it?  Sorry I can't send it to you.
```

##### ↳ ↳ Re: Help in Finding Information

- **From:** jack <jacksleightNOjaSPAM@hotmail.com.invalid>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1a5d65fc.f556b529@usw-ex0105-038.remarq.com>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net> <8kkodm$iar@netnews1.apci.com>`

```
Arthur,

I like WDS's solution of an inspect/tallying followed by an
unstring/pointer/not on overflow.

Add 1 to the tally fld and use it in the unstring delimited
by 'T'. On not oflow you perform the paragraph that does your
numeric checks etc.

The advantages:

    >  If no 'T's or not the right len then numchk not performed
    >  You don't clutter up your pgm w/logic
    >  If the number between the Ts is too short it will be flag-
       ged as non-numeric in numchk

The disadvantages:
    >  I ca't wait to find out


-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

##### ↳ ↳ Re: Help in Finding Information

- **From:** jack <jacksleightNOjaSPAM@hotmail.com.invalid>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<02046bac.f9545621@usw-ex0105-038.remarq.com>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net> <8kkodm$iar@netnews1.apci.com>`

```
testing. trouble posting


-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

##### ↳ ↳ Re: Help in Finding Information

- **From:** jack <jacksleightNOjaSPAM@hotmail.com.invalid>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<21552940.06c423a4@usw-ex0105-038.remarq.com>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net> <8kkodm$iar@netnews1.apci.com>`

```
Hi Arthur,

I like WDSs suggestion to use inspect/tallying followed by an
unstring/pointer/not on overflow. After the inspect add 1 to the
tally fld and use it as a start position to unstring into a work
fld using 'T' as a delimiter. Note that the wrk fld won't
contain the Ts as delimiters, but that's ok.

In the "not on oflow" phrase preform the paragraph that does the
numeric chk on the wrk fld.

The advantages of this approach:

    >  non T recs, flds > 11 pos are bypassed via oflow
    >  flds < 11 pos are rejected in numchk paragraph because
       unfilled positions are not numeric
    >  program is not cluttered up w/unnecessary logic

The disadvantages:

    >  Probably inefficient. If you have "biwions and biwions"
       of records this might be a problem.

Here's my cut at the numchk paragraph.

      evaluate true also true also true
          when pos-1-5-are-numeric
               also pos-6-is-numeric
               also po-7-9-are-numeric
               do numeric stuff
          when pos-1-5-are-numeric
               also pos-6-is-a-dash
               also po-7-9-are-numeric
               do dash stuff
          when other
               do ignore stuff
      end-evaluate


01  ws-wrk-fld.
    05  ws-1-5              pic 9(005).
        88  pos-1-5-are-numeric        value 0 thru 99999.

    05  ws-6                pic 9.
        88  pos-6-is-numeric           value 0 thru 9.
    05  redefines ws-6      pic x.
        88  pos6-is-a-dash             value '-'.

    05  ws-7-9              pic 9(003).
        88  pos-7-9-are-numeric        value 0 thru 999.

 Have fun, Jack.

Poster's note: None of this stuff was tested.



-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

#### ↳ Re: Help in Finding Information

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XQQb5.221$l73.68481@nnrp3.sbc.net>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
Might work--

PERFORM VARYING J FROM 206 BY 1 UNTIL J > 249
    COMPUTE K = J + 11
    COMPUTE L = J + 1
    COMPUTE M = J + 6
    COMPUTE N = J + 7
    IF REC(J:1) = 'T'
       AND REC(K:1) = 'T'
       IF REC(L:9) NUMERIC
       OR
       (REC(L:5) NUMERIC AND REC(M:1) = '-' AND REC(N:3) NUMERIC)
       do something important
       END-IF
    END-IF
END-PERFORM.


Arthur M. Kent <akent@seanet.com> wrote in message
news:akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net
...
> I need some assistance with locating a "string" within a record.
Let me
> first explain the "particulars".
>
> I am using COBOL in an OS 390 environment.  I will need to read a
> sequential file, each record of fixed length 340 bytes.  The
"string" I am
> looking for is located within bytes 206 through 250 inclusive, but
the
> beginning of the "string" is not always in the same location within
the
> bytes 206 through 250 inclusive.
>
> The "string" I am attempting to find is 11 bytes long, beginning
with the
> letter T (capitalized, as shown).  Once I have located this first
> occurrence of the T, I need to be able to "easily" verify that the
11th
> byte of this string is also the letter T.  Finally, once I have this
11
> byte "string" with the two Ts, I need to determine if the 7th byte,
within
> the 11 bytes, is a dash "-".  The 2nd through 10th bytes will either
> always be numeric, or will be of the format 99999-999, where each 9,
of
> course, is a number.  Here are two examples of such "strings":
>
…[4 more quoted lines elided]…
> I don't believe the INSPECT verb will help be locate the first
occurrence
> of the letter T.  Even if it did, how can I "easily" analyze the 11
bytes
> for the conditions stated above?
>
> I realize that I could move bytes 206 through 250 into a array of
length
> 45 bytes, and then analyze each byte sequentially, but this seems
rather
> "ugly" and complex.  I am looking for a simpler solution.
>
> Any advice/comments etc. would be appreciated.  If you wish to send
your
> comments via EMail, my EMail address is akent@seanet.com.
>
> Thank You,
> Arthur M. Kent
>
```

##### ↳ ↳ Re: Help in Finding Information

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<397059a2.118368408@207.126.101.100>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net> <XQQb5.221$l73.68481@nnrp3.sbc.net>`

```
If I had User defined functions I could write a SUBSTR function and
get at it.  


On Fri, 14 Jul 2000 22:24:03 -0500, "Jerry P" <jerryp@bisusa.com>
wrote:

>Might work--
>
…[70 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Help in Finding Information

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gmtc5.1021$oV.81756@nnrp3.sbc.net>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net> <XQQb5.221$l73.68481@nnrp3.sbc.net>`

```
Better (without all the J,K,L,M stuff) (I forgot - or didn't know -
the starting position in a reference modifier can be an arithmetic
expression)

 PERFORM VARYING J FROM 206 BY 1 UNTIL J > 249
     IF REC(J:1) = 'T'
        AND REC(J + 11:1) = 'T'
        IF REC(J + 1:9) NUMERIC
        OR
        (REC(J + 1:5) NUMERIC AND REC(J + 6:1) = '-' AND REC(J + 7:3)
NUMERIC)
        do something important
        END-IF
     END-IF
 END-PERFORM.

Jerry P <jerryp@bisusa.com> wrote in message
news:XQQb5.221$l73.68481@nnrp3.sbc.net...
> Might work--
>
…[17 more quoted lines elided]…
>
news:akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net
> ...
> > I need some assistance with locating a "string" within a record.
…[8 more quoted lines elided]…
> > beginning of the "string" is not always in the same location
within
> the
> > bytes 206 through 250 inclusive.
…[6 more quoted lines elided]…
> > byte of this string is also the letter T.  Finally, once I have
this
> 11
> > byte "string" with the two Ts, I need to determine if the 7th
byte,
> within
> > the 11 bytes, is a dash "-".  The 2nd through 10th bytes will
either
> > always be numeric, or will be of the format 99999-999, where each
9,
> of
> > course, is a number.  Here are two examples of such "strings":
…[7 more quoted lines elided]…
> > of the letter T.  Even if it did, how can I "easily" analyze the
11
> bytes
> > for the conditions stated above?
…[7 more quoted lines elided]…
> > Any advice/comments etc. would be appreciated.  If you wish to
send
> your
> > comments via EMail, my EMail address is akent@seanet.com.
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Help in Finding Information

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.13da9aa5880adf509896ce@news>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
Arthur,

	My solution to this uses a small called module and pointers...  it 
also is amode 31 rmode any and data 31 with trunc(bin) compiler option to 
allow for handling of binary data as true binary without any truncation. 
this is important as the program redefines pointers and increments them.

source code as follows....   

       CBL TRUNC(BIN) LIST DATA(31)
       IDENTIFICATION DIVISION.
       PROGRAM-ID.    UTL0050.
      *AUTHOR.        CHUCK HAATVEDT.
      *INSTALLATION.  PUBLIC DOMAIN.
      *DATE WRITTEN.  JULY 2000.
      *DATE COMPILED.
      *REMARKS.
      *    PURPOSE AND OBJECTIVES.
      *    THIS PROGRAM WILL SCAN A 45 BYTE AREA FOR AN 11 BYTE STRING
      *    OF THE FORMAT T999999999T
      *               OR T99999-999T
      *
      *    WHERE THE 9'S REPRESENT ANY VALID NUMERIC CHARACTER.
      *
      *    1    07/00 INITIAL PROGRAMMING                 C. HAATVEDT
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

       77  ABEND-CODE                      PIC S9(8)   COMP VALUE 501.

       01  PTR-POINTER-AREA.
           05  PTR-SCAN                    USAGE POINTER.
           05  PTR-SCAN-X  REDEFINES  PTR-SCAN
                                           PIC X(4).
           05  PTR-SCAN-BCNTR  REDEFINES  PTR-SCAN
                                           PIC 9(9)   COMP.
           05  PTR-END                    USAGE POINTER.
           05  PTR-END-X  REDEFINES  PTR-END
                                           PIC X(4).
           05  PTR-END-BCNTR  REDEFINES  PTR-END
                                           PIC 9(9)   COMP.
           05  PTR-MAX-ADDRESS             PIC X(4) VALUE X'7FFFFFD3'.

       01  BCNTR-BINARY-COUNTERS.
           05  BCNTR-OFFSET                PIC S9(9)   COMP.
           05  BCNTR-OFFSET-X  REDEFINES  BCNTR-OFFSET
                                           PIC X(4).
       LINKAGE SECTION.

       01  LP-LINKAGE-PARMS.
           05  LP-STRING-FOUND             PIC X.
               88  LP-STRING-FOUND-IS-Y                VALUE 'Y'.
               88  LP-STRING-FOUND-IS-N                VALUE 'N'.
           05  LP-STRING-OFFSET-INDEX      USAGE INDEX.
           05  LP-STRING-OFFSET-X  REDEFINES  LP-STRING-OFFSET-INDEX
                                           PIC X(4).
           05  LP-STRING-OFFSET-BCNTR
                           REDEFINES  LP-STRING-OFFSET-INDEX
                                           PIC S9(9)   COMP.

       01  LP-DATA-AREA                    PIC X(45).

       01  SA-SCAN-AREA.
           05  SA-BYTE-01                  PIC X.
               88  SA-BYTE-01-IS-T                     VALUE 'T'.
           05  SA-BYTE-02                  PIC X.
               88  SA-BYTE-02-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-03                  PIC X.
               88  SA-BYTE-03-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-04                  PIC X.
               88  SA-BYTE-04-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-05                  PIC X.
               88  SA-BYTE-05-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-06                  PIC X.
               88  SA-BYTE-06-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-07                  PIC X.
               88  SA-BYTE-07-IS-NUMERIC       VALUES ARE '0' THRU '9'.
               88  SA-BYTE-07-IS-DASH          VALUE '-'.
           05  SA-BYTE-08                  PIC X.
               88  SA-BYTE-08-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-09                  PIC X.
               88  SA-BYTE-09-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-10                  PIC X.
               88  SA-BYTE-10-IS-NUMERIC       VALUES ARE '0' THRU '9'.
           05  SA-BYTE-11                  PIC X.
               88  SA-BYTE-11-IS-T                     VALUE 'T'.
       PROCEDURE DIVISION USING LP-LINKAGE-PARMS
                                LP-DATA-AREA.

           SET PTR-SCAN         TO ADDRESS OF LP-DATA-AREA.
           MOVE PTR-SCAN-X             TO PTR-END-X.
           ADD +34                     TO PTR-END-BCNTR.

           IF PTR-SCAN-X GREATER THAN PTR-MAX-ADDRESS
               DISPLAY ' UTL0050 ===> SCAN FIELD ADDRESS MAXIMUM '
                   'AMODE 31 ADDRESS'
               CALL 'ILBOABN0'  USING ABEND-CODE
           END-IF.

           SET ADDRESS OF SA-SCAN-AREA TO PTR-SCAN.
           MOVE ZERO                   TO BCNTR-OFFSET.

           PERFORM WITH TEST BEFORE
               UNTIL PTR-SCAN-X GREATER THAN PTR-END-X
                  OR (    SA-BYTE-01-IS-T
                      AND SA-BYTE-11-IS-T
                      AND SA-BYTE-02-IS-NUMERIC
                      AND SA-BYTE-03-IS-NUMERIC
                      AND SA-BYTE-04-IS-NUMERIC
                      AND SA-BYTE-05-IS-NUMERIC
                      AND SA-BYTE-06-IS-NUMERIC
                      AND SA-BYTE-08-IS-NUMERIC
                      AND SA-BYTE-09-IS-NUMERIC
                      AND SA-BYTE-10-IS-NUMERIC
                      AND (    SA-BYTE-07-IS-NUMERIC
                            OR SA-BYTE-07-IS-DASH  ) )
               ADD +1                  TO PTR-SCAN-BCNTR
               ADD +1                  TO BCNTR-OFFSET
               SET ADDRESS OF SA-SCAN-AREA TO PTR-SCAN
           END-PERFORM.

           IF PTR-SCAN-X GREATER THAN PTR-END-X
               MOVE 'N'                TO LP-STRING-FOUND
               MOVE ZERO               TO LP-STRING-OFFSET-BCNTR
           ELSE
               MOVE 'Y'                TO LP-STRING-FOUND
               MOVE BCNTR-OFFSET-X     TO LP-STRING-OFFSET-X
           END-IF.

           MOVE ZERO                   TO RETURN-CODE.
           GOBACK.
       END PROGRAM UTL0050.


====>>>>  warning this code is NOT tested and is provided with NO 
warranty or guaranty of any kind...  as with any code it should be 
thoroughly tested and documented before being used in a production 
environment...

[This follow up was posted to comp.lang.cobol and a copy was sent to the 
cited author.]

In article <akent-0907001427110001@dialup-
209.245.162.150.seattle1.level3.net>, akent@seanet.com says...
> I need some assistance with locating a "string" within a record.  Let me
> first explain the "particulars".
…[33 more quoted lines elided]…
> 
```

##### ↳ ↳ Re: Help in Finding Information

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<crtc5.1022$oV.82449@nnrp3.sbc.net>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net> <MPG.13da9aa5880adf509896ce@news>`

```
Good Lord, Charles!

Do you bill by the line?


Charles Haatvedt Jr. <clastname@nospam.com> wrote in message
news:MPG.13da9aa5880adf509896ce@news...
> Arthur,
>
> My solution to this uses a small called module and pointers...  it
> also is amode 31 rmode any and data 31 with trunc(bin) compiler
option to
> allow for handling of binary data as true binary without any
truncation.
> this is important as the program redefines pointers and increments
them.
>
> source code as follows....
…[10 more quoted lines elided]…
>       *    THIS PROGRAM WILL SCAN A 45 BYTE AREA FOR AN 11 BYTE
STRING
>       *    OF THE FORMAT T999999999T
>       *               OR T99999-999T
…[3 more quoted lines elided]…
>       *    1    07/00 INITIAL PROGRAMMING                 C.
HAATVEDT
>        ENVIRONMENT DIVISION.
>        DATA DIVISION.
>        WORKING-STORAGE SECTION.
>
>        77  ABEND-CODE                      PIC S9(8)   COMP VALUE
501.
>
>        01  PTR-POINTER-AREA.
…[10 more quoted lines elided]…
>            05  PTR-MAX-ADDRESS             PIC X(4) VALUE
X'7FFFFFD3'.
>
>        01  BCNTR-BINARY-COUNTERS.
…[22 more quoted lines elided]…
>                88  SA-BYTE-02-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-03                  PIC X.
>                88  SA-BYTE-03-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-04                  PIC X.
>                88  SA-BYTE-04-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-05                  PIC X.
>                88  SA-BYTE-05-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-06                  PIC X.
>                88  SA-BYTE-06-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-07                  PIC X.
>                88  SA-BYTE-07-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>                88  SA-BYTE-07-IS-DASH          VALUE '-'.
>            05  SA-BYTE-08                  PIC X.
>                88  SA-BYTE-08-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-09                  PIC X.
>                88  SA-BYTE-09-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-10                  PIC X.
>                88  SA-BYTE-10-IS-NUMERIC       VALUES ARE '0' THRU
'9'.
>            05  SA-BYTE-11                  PIC X.
>                88  SA-BYTE-11-IS-T                     VALUE 'T'.
…[53 more quoted lines elided]…
> [This follow up was posted to comp.lang.cobol and a copy was sent to
the
> cited author.]
>
> In article <akent-0907001427110001@dialup-
> 209.245.162.150.seattle1.level3.net>, akent@seanet.com says...
> > I need some assistance with locating a "string" within a record.
Let me
> > first explain the "particulars".
> >
> > I am using COBOL in an OS 390 environment.  I will need to read a
> > sequential file, each record of fixed length 340 bytes.  The
"string" I am
> > looking for is located within bytes 206 through 250 inclusive, but
the
> > beginning of the "string" is not always in the same location
within the
> > bytes 206 through 250 inclusive.
> >
> > The "string" I am attempting to find is 11 bytes long, beginning
with the
> > letter T (capitalized, as shown).  Once I have located this first
> > occurrence of the T, I need to be able to "easily" verify that the
11th
> > byte of this string is also the letter T.  Finally, once I have
this 11
> > byte "string" with the two Ts, I need to determine if the 7th
byte, within
> > the 11 bytes, is a dash "-".  The 2nd through 10th bytes will
either
> > always be numeric, or will be of the format 99999-999, where each
9, of
> > course, is a number.  Here are two examples of such "strings":
> >
…[4 more quoted lines elided]…
> > I don't believe the INSPECT verb will help be locate the first
occurrence
> > of the letter T.  Even if it did, how can I "easily" analyze the
11 bytes
> > for the conditions stated above?
> >
> > I realize that I could move bytes 206 through 250 into a array of
length
> > 45 bytes, and then analyze each byte sequentially, but this seems
rather
> > "ugly" and complex.  I am looking for a simpler solution.
> >
> > Any advice/comments etc. would be appreciated.  If you wish to
send your
> > comments via EMail, my EMail address is akent@seanet.com.
> >
…[10 more quoted lines elided]…
> remove space in email address....
```

#### ↳ Re: Help in Finding Information

- **From:** "George E. Zielinski" <georgezielinski@retired.airforce.net>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<07020FD09B59C864.7F8F4C1B2BB33F37.EF59AD8D3F6ED29F@lp.airnews.net>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
You might want to do something on this order.  You may need to modify it to
fit your naming conventions, feel free.

        FIND-SUBSTRING.

             PERFORM VARYING SUB1 FROM 206 TO 239 BY 1 UNTIL

SUB1 > 239
                  IF SEARCH-FIELD (SUB1:1) = "T" AND
                      SEARCH-FIELD (SUB1 + 10:1) = "T"
                       EVALUATE TRUE
                           WHEN SEARCH-FIELD (SUB1 + 7:1) IS NUMERIC
                                  PERFORM DO-SOMETHING-NUMERIC-FIELD
                           WHEN SEARCH-FIELD (SUB1 + 7:1) = "-"
                                  PERFORM DO-SOMETHING-DASH-FIELD
                            WHEN OTHER
                                 CONTINUE
                      END-EVALUATE
                     ADD 50 TO SUB1
              END-PERFORM.

        FIND-SUBSTRING-EXIT.


"Arthur M. Kent" <akent@seanet.com> wrote in message
news:akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net...
> I need some assistance with locating a "string" within a record.  Let me
> first explain the "particulars".
…[32 more quoted lines elided]…
> Arthur M. Kent
```

#### ↳ Re: Help in Finding Information

- **From:** jack <jacksleightNOjaSPAM@hotmail.com.invalid>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2adc2a83.0b014b9b@usw-ex0106-046.remarq.com>`
- **References:** `<akent-0907001427110001@dialup-209.245.162.150.seattle1.level3.net>`

```
Hello again Arthur,

Just a side comment on your problem. If I'm not mistaken, if t
your target field is explicitly defined as alphanumeric(or
implicitly defined as such, e.g. FLD-A(2:3) ) a field of the
form nnC or nnD is considered numeric in addition to all
occurances of the field as X'FnFnFn'. In addition, if the
NUMPROC and NUMCLS have the right (or wrong) compiler settings
any occurance of A thru E in the low order position of the field
will result in a positive result of the class test IF NUMERIC.

Regards, Jack


-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
