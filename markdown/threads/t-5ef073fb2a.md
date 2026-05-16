[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A Kind of XML parser ??? (like Java)

_19 messages · 11 participants · 2004-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web) · [`Help requests and how-to`](../topics.md#help)

---

### A Kind of XML parser ??? (like Java)

- **From:** jorenders@hotmail.com (JR)
- **Date:** 2004-02-05T01:05:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
Hi,

Does anybody know of you can read a xml
file intelligently with a Cobol program.
How can you tell cobol that a tag 25 times
returns and etc...


Thanks

JR
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-02-05T12:29:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040205072908.13115.00001008@mb-m20.aol.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
Jorenders writes ...

>Hi,
>
…[7 more quoted lines elided]…
>

Yes, you can, if you are using current compilers from IBM.

<ad>
Check out the course description (and follow the link to the detailed topical
outline) for our new course "Enterprise COBOL: Unicode and XML Support" at
http://www.trainersfriend.com/d705descr.htm

</ad>

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-02-05T14:32:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fusUb.404$PY.151@newssvr26.news.prodigy.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
"JR" <jorenders@hotmail.com> wrote in message
news:4096148f.0402050105.28c56df4@posting.google.com...
> Does anybody know of you can read a xml
> file intelligently with a Cobol program.
> How can you tell cobol that a tag 25 times
> returns and etc...

If your O/S is windows or Unix, the expat parser (freeware) can be used, as
long as you can supply a callback address (PROCEDURE-POINTER) with your
particular COBOL compiler. You'll also need to handle your own data storage
, which will require either dynamic memory allocation/de-allocation OR you
can write the data to a disk file  (counting tags as you go, if you'd like)
and get your tag values back from that file later.

No, it is not real simple if you haven't done this kind of programming
before, but expat is fast, reliable and the price is certainly right.

MCM
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-02-05T15:38:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvto29$sa1$1@peabody.colorado.edu>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```

On  5-Feb-2004, jorenders@hotmail.com (JR) wrote:

> Does anybody know of you can read a xml
> file intelligently with a Cobol program.
> How can you tell cobol that a tag 25 times
> returns and etc...

It's called programming.
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-05T10:40:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402051040.2bd9dac3@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
jorenders@hotmail.com (JR) wrote in

> Does anybody know of you can read a xml
> file intelligently with a Cobol program.
> How can you tell cobol that a tag 25 times
> returns and etc...

Here's one that I got from the net and modified. It is called as a
subroutine with the XML passed to it.  For any serious work you may
need to change this.

      *--Version: 4.10  30/07/02  10:46:58

       IDENTIFICATION DIVISION.
       PROGRAM-ID.             xmlparse.

      *    xmlparse.LST
      *    \xml\xml.cbl

      *AUTHOR. Miami-Dade Community College.
      *DATE-WRITTEN.  July, 2000.
      *DATE-COMPILED.
      *REMARKS.
      *
      *    LAST CHANGE:  09/12/00 12:02:24 SAHWC
      *
      *    This program will parse any valid XML document into its
      *    component parts.
      *

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

       DATA DIVISION.
       FILE SECTION.

       WORKING-STORAGE SECTION.

       01  FILLER.
           05  FILLER                  PIC X(32) VALUE
               'WORKING-STORAGE FOR XMLPARSE>>>:'.
           05  WK-INDEX                PIC S9(9)           COMP SYNC.
           05  WK-INDEX-1              PIC S9(9)           COMP SYNC.
           05  WK-INDEX-2              PIC S9(9)           COMP SYNC.
           05  WK-START-INDEX          PIC S9(9)           COMP SYNC.
           05  WK-SEQ-NBR              PIC S9(9)           COMP SYNC.
           05  ENDING-PTR              PIC S9(9)           COMP SYNC.
           05  BASE-PTR                PIC S9(9)           COMP SYNC.
           05  WK-LENGTH               PIC S9(4)           COMP SYNC.
           05  ENTITY-LENGTH           PIC S9(4)           COMP SYNC.
           05  RESULT                  PIC 9.
           05  WK-FIND-CHAR            PIC X.
           05  SKIP-WHITE-SPACE-CHECK  PIC X.
           05  WK-ENTITY               PIC X(6).
           05  FILLER REDEFINES WK-ENTITY.
               10  WK-ENTITY-X         PIC X     OCCURS 6 TIMES.
           05  WK-MARKUP-CHARACTER     PIC X.
           05  ATTR-NAME               PIC X(50).
           05  ELEM-NAME               PIC X(50).
           05  DATA-VALUE              PIC X(1010).
           05  FILLER REDEFINES DATA-VALUE.
               10  DATA-VALUE-X        PIC X     OCCURS 1010 TIMES.
           05  NAME-VALUE              PIC X(1000).
           05  FILLER REDEFINES NAME-VALUE.
               10  NAME-VALUE-X        PIC X     OCCURS 1000 TIMES.
           05  FILLER REDEFINES NAME-VALUE.
               10  FILLER              PIC X(5).
                   88  NAME-VALUE-START-WITH-CDATA
                                                 VALUE 'CDATA'.
           05  WK-END-OF-MSG-SWITCH    PIC X.
               88  WK-END-OF-MSG                 VALUE '1'.
           05  WK-FOUND-SWITCH         PIC X.
               88  WK-FOUND                      VALUE '1'.
           05  WK-PARSING-ERROR-SWITCH PIC X.
               88  WK-PARSING-ERROR              VALUE '1'.

       01  ToUpper.
           03  Char-Comp               PIC 9(4) COMP SYNC.
           03  FILLER REDEFINES Char-Comp.
               05  FILLER              PIC X.
               05  Char-X              PIC X.

       01  FILLER.
      *    05  LEFT-BRACKET-X          PIC S9(4) VALUE 173 COMP SYNC.
      *    05  FILLER REDEFINES LEFT-BRACKET-X.
      *        10  FILLER              PIC X.
      *        10  LEFT-BRACKET        PIC X.
      *    05  RITE-BRACKET-X          PIC S9(4) VALUE 189 COMP SYNC.
      *    05  FILLER REDEFINES RITE-BRACKET-X.
      *        10  FILLER              PIC X.
      *        10  RITE-BRACKET        PIC X.
      *    05  VALUE-TAB-X             PIC S9(4) VALUE 5   COMP SYNC.
      *    05  FILLER REDEFINES VALUE-TAB-X.
      *        10  FILLER              PIC X.
      *        10  VALUE-TAB           PIC X.
      *    05  VALUE-LF-X              PIC S9(4) VALUE 37 COMP SYNC.
      *    05  FILLER REDEFINES VALUE-LF-X.
      *        10  FILLER              PIC X.
      *        10  VALUE-LF            PIC X.
      *    05  VALUE-CR-X              PIC S9(4) VALUE 13 COMP SYNC.
      *    05  FILLER REDEFINES VALUE-CR-X.
      *        10  FILLER              PIC X.
      *        10  VALUE-CR            PIC X.

      *    ASCII values
           05  LEFT-BRACKET            PIC X     VALUE "<".
           05  RITE-BRACKET            PIC X     VALUE ">".
           05  VALUE-TAB               PIC X     VALUE x"09".
           05  VALUE-LF                PIC X     VALUE x"0A".
           05  VALUE-CR                PIC X     VALUE x"0D".
           05  VALUE-QUOTE             PIC X     VALUE QUOTE.

           05  FILLER                  PIC S9(4) VALUE ZERO COMP SYNC.

           05  TTL-ACCEPTABLE-CHARS    PIC S9(4) VALUE 66 COMP SYNC.
           05  TTL-ACCEPTABLE-FIRST-CHARS
                                       PIC S9(4) VALUE 53 COMP SYNC.

           05  ACCEPTABLE-CHARS        PIC X(66) VALUE
               '_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012
      -        '3456789-.:'.
           05  FILLER REDEFINES ACCEPTABLE-CHARS.
               10  ACCEPTABLE-CHARS-X  PIC X     OCCURS 66 TIMES.

           05  TTL-ENTITY-REFERENCE    PIC S9(4) VALUE 5  COMP SYNC.
           05  ENTITY-REFERENCE.
               10  FILLER              PIC X(7)  VALUE '&gt;  >'.
               10  FILLER              PIC X(7)  VALUE '&lt;  <'.
               10  FILLER              PIC X(7)  VALUE '&amp; &'.
               10  FILLER.
                   15  FILLER          PIC X(6)  VALUE '&apos;'.
                   15  FILLER          PIC X     VALUE QUOTE.
               10  FILLER              PIC X(7)  VALUE '&quot;"'.
           05  FILLER REDEFINES ENTITY-REFERENCE.
               10  FILLER                        OCCURS 5 TIMES.
                15 ENTITY-REFERENCE-X  PIC X(6).
                15 MARKUP-CHARACTER    PIC X.

           05  RESULT-TABLE.
               10  FILLER              PIC X(3)  VALUE '1  '.
               10  FILLER              PIC X(3)  VALUE '1  '.
               10  FILLER              PIC X(3)  VALUE '111'.
               10  FILLER              PIC X(3)  VALUE '1 1'.
               10  FILLER              PIC X(3)  VALUE '   '.
               10  FILLER              PIC X(3)  VALUE '   '.
               10  FILLER              PIC X(3)  VALUE '111'.
               10  FILLER              PIC X(3)  VALUE '111'.
               10  FILLER              PIC X(3)  VALUE '111'.
           05  FILLER REDEFINES RESULT-TABLE.
               10  FILLER                        OCCURS 9 TIMES.
                   15  FILLER          PIC X.
                       88  ELEM-NAME-REQUIRED    VALUE '1'.
                   15  FILLER          PIC X.
                       88  ATTR-NAME-REQUIRED    VALUE '1'.
                   15  FILLER          PIC X.
                       88  DATA-VALUE-REQUIRED   VALUE '1'.

       LINKAGE SECTION.

           COPY "xmlparse.ws".     *> \az\include\xmlparse.ws

       PROCEDURE DIVISION USING XML-Interface
                                XML-Document
                                .
       Program-XMLParse.

           MOVE '0'            TO WK-END-OF-MSG-SWITCH
                                  WK-PARSING-ERROR-SWITCH

           IF ( XML-RESERVED = ZEROES )
               MOVE ZERO       TO CHAR-PTR
                                  WK-SEQ-NBR
               MOVE 00         TO STATE
               MOVE 6          TO RESULT
           END-IF

           PERFORM MAIN-RTN
               UNTIL WK-END-OF-MSG
                  OR WK-PARSING-ERROR

           IF ( WK-PARSING-ERROR )
               PERFORM PARSED-DATA-RTN
               PERFORM PARSING-ERROR-RTN
           END-IF

           MOVE ZERO           TO RETURN-CODE
           .

           EXIT PROGRAM
           .

       MAIN-RTN.

           ADD 1                   TO CHAR-PTR

           IF ( STATE > 00 AND < 07 )
               PERFORM PARSED-DATA-RTN
           END-IF
           .

           IF ( CHAR-PTR > XML-LENGTH
      *      OR          > 9216
              )
               MOVE '1'             TO WK-END-OF-MSG-SWITCH
               PERFORM PARSED-DATA-RTN
           ELSE

               EVALUATE State
               WHEN ZERO
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '<' )
                       MOVE 07         TO STATE
                   ELSE
                       MOVE 33         TO STATE
                       SUBTRACT 1    FROM CHAR-PTR
                   END-IF

               WHEN 1
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '/' )
                       MOVE 21         TO STATE
                   ELSE
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '>' )
                       MOVE 00         TO STATE
                   ELSE
                       PERFORM FIND-VALID-FIRST-NAME-RTN
                       IF ( WK-FOUND )
                           MOVE CHAR-PTR   TO BASE-PTR
                           MOVE 27         TO STATE
                       ELSE
                           MOVE '1'        TO WK-PARSING-ERROR-SWITCH
                       END-IF
                   END-IF
                   END-IF

               WHEN 2
               WHEN 3
               WHEN 4
               WHEN 5
               WHEN 6
                   CONTINUE

               WHEN 7
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '/' )
                       MOVE 25         TO STATE
                   ELSE
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '?' )
                       MOVE 22         TO STATE
                   ELSE
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '!' )
                       MOVE 08         TO STATE
                   ELSE
                       PERFORM FIND-VALID-FIRST-NAME-RTN
                       IF ( WK-FOUND )
                           MOVE CHAR-PTR   TO BASE-PTR
                           MOVE 20         TO STATE
                       ELSE
                           MOVE '1'        TO WK-PARSING-ERROR-SWITCH
                       END-IF
                   END-IF
                   END-IF
                   END-IF

               WHEN 8
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '-' )
                       MOVE 09         TO STATE
                   ELSE
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = LEFT-BRACKET )
                       MOVE 14         TO STATE
                   ELSE
                       MOVE '1'        TO WK-PARSING-ERROR-SWITCH
                   END-IF
                   END-IF

               WHEN 9
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '-' )
                       MOVE 10         TO STATE
                   ELSE
                       MOVE '1'        TO WK-PARSING-ERROR-SWITCH
                   END-IF

               WHEN 10
                   MOVE '-'            TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 12         TO STATE
                   END-IF

               WHEN 11
                   CONTINUE

               WHEN 12
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '-' )
                       MOVE 13         TO STATE
                   ELSE
                       MOVE 10         TO STATE
                   END-IF

               WHEN 13
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '>' )
                       MOVE 00         TO STATE
                   ELSE
                       MOVE 10         TO STATE
                   END-IF

               WHEN 14
                   MOVE CHAR-PTR       TO BASE-PTR
                   PERFORM FIND-VALID-NAME-RTN
                   IF ( NAME-VALUE-START-WITH-CDATA )
                       MOVE 15         TO STATE
                   END-IF
                   SUBTRACT 1        FROM CHAR-PTR

               WHEN 15
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = LEFT-BRACKET )
                       MOVE 16         TO STATE
                   END-IF
                   COMPUTE BASE-PTR = CHAR-PTR + 1

               WHEN 16
                   MOVE RITE-BRACKET   TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 18         TO STATE
                   END-IF

               WHEN 17
                   CONTINUE

               WHEN 18
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = RITE-BRACKET )
                       MOVE 19         TO STATE
                   ELSE
                       MOVE 16         TO STATE
                   END-IF

               WHEN 19
                   MOVE '>'            TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 02         TO STATE
                   ELSE
                       MOVE 16         TO STATE
                   END-IF

               WHEN 20
                   PERFORM FIND-VALID-NAME-RTN
                   MOVE NAME-VALUE     TO ELEM-NAME
                   MOVE 01             TO STATE
                   SUBTRACT 1        FROM CHAR-PTR

               WHEN 21
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '>' )
                       MOVE 03         TO STATE
                   END-IF

               WHEN 22
                   MOVE '?'            TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 24         TO STATE
                   END-IF

               WHEN 23
                   CONTINUE

               WHEN 24
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '>' )
                       MOVE 00         TO STATE
                   END-IF

               WHEN 25
                   PERFORM FIND-VALID-FIRST-NAME-RTN
                   IF ( WK-FOUND )
                       MOVE CHAR-PTR   TO BASE-PTR
                       MOVE 26         TO STATE
                   ELSE
                       MOVE '1'        TO WK-PARSING-ERROR-SWITCH
                   END-IF

               WHEN 26
                   PERFORM FIND-VALID-NAME-RTN
                   MOVE NAME-VALUE     TO ELEM-NAME
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '>' )
                       MOVE 05         TO STATE
                   END-IF

               WHEN 27
                   PERFORM FIND-VALID-NAME-RTN
                   MOVE NAME-VALUE     TO ATTR-NAME
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '=' )
                       MOVE 28         TO STATE
                   END-IF

               WHEN 28
                   PERFORM SKIP-WHITE-SPACE-RTN
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = VALUE-QUOTE )
                       MOVE 29         TO STATE
                   ELSE
                   IF ( XML-DOCUMENT-X(CHAR-PTR) = '"' )
                       MOVE 31         TO STATE
                   ELSE
                       MOVE '1'        TO WK-PARSING-ERROR-SWITCH
                   END-IF
                   END-IF
                   COMPUTE BASE-PTR = CHAR-PTR + 1

               WHEN 29
                   MOVE VALUE-QUOTE    TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 04         TO STATE
                   END-IF

               WHEN 30
                   CONTINUE

               WHEN 31
                   MOVE '"'            TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 04         TO STATE
                   END-IF

               WHEN 32
                   CONTINUE

               WHEN 33
                   MOVE CHAR-PTR       TO BASE-PTR
                   MOVE '<'            TO WK-FIND-CHAR
                   PERFORM FIND-THIS-CHARACTER-RTN
                   IF ( WK-FOUND )
                       MOVE 06         TO STATE
                   SUBTRACT 1        FROM CHAR-PTR

               WHEN OTHER
                   MOVE '1'            TO WK-PARSING-ERROR-SWITCH

               END-EVALUATE
           END-IF
           .

       PARSED-DATA-RTN.

           IF ( WK-PARSING-ERROR )
               MOVE 6              TO RESULT
           ELSE
           IF ( WK-END-OF-MSG )
               MOVE 5              TO RESULT
           ELSE
           IF ( STATE = 01 )
               MOVE ELEM-NAME      TO SAVE-ELEM-NAME
               MOVE 1              TO RESULT
           ELSE
           IF ( STATE = 02 )
               MOVE SAVE-ELEM-NAME TO ELEM-NAME
               COMPUTE ENDING-PTR = CHAR-PTR - 3
               PERFORM GET-DATA-VALUE-RTN
               MOVE 00             TO STATE
               MOVE 4              TO RESULT
           ELSE
           IF ( STATE = 03 )
               MOVE SAVE-ELEM-NAME TO ELEM-NAME
               MOVE 00             TO STATE
               MOVE 2              TO RESULT
           ELSE
           IF ( STATE = 04 )
               MOVE SAVE-ELEM-NAME TO ELEM-NAME
               COMPUTE ENDING-PTR = CHAR-PTR - 1
               PERFORM GET-DATA-VALUE-RTN
               MOVE ZERO           TO WK-INDEX-1
               PERFORM ENTITY-REFERENCE-RTN
                   VARYING WK-INDEX FROM 1 BY 1
                     UNTIL WK-INDEX > 1000
               MOVE 01             TO STATE
               MOVE 3              TO RESULT
           ELSE
           IF ( STATE = 05 )
               MOVE 00             TO STATE
               MOVE 2              TO RESULT
           ELSE
           IF ( STATE = 06 )
               MOVE SAVE-ELEM-NAME TO ELEM-NAME
               MOVE CHAR-PTR       TO ENDING-PTR
               PERFORM GET-DATA-VALUE-RTN
               MOVE ZERO           TO WK-INDEX-1
               PERFORM ENTITY-REFERENCE-RTN
                  VARYING WK-INDEX FROM 1 BY 1
                    UNTIL WK-INDEX > 1000

               MOVE 00             TO STATE
               MOVE 4              TO RESULT
           END-IF
           END-IF
           END-IF
           END-IF
           END-IF
           END-IF
           END-IF
           END-IF

           ADD 1                   TO WK-SEQ-NBR

           IF ( WK-SEQ-NBR > SAVE-INDEX )
               MOVE '1'            TO WK-END-OF-MSG-SWITCH
               MOVE WK-SEQ-NBR     TO SAVE-INDEX

               MOVE SPACES         TO XML-PARSED-AREA
               MOVE RESULT         TO XML-RETURN-CODE
               IF ( ELEM-NAME-REQUIRED(RESULT) )
                   MOVE ELEM-NAME  TO XML-ELEMENT-NAME
               END-IF
               IF ( ATTR-NAME-REQUIRED(RESULT) )
                   MOVE ATTR-NAME  TO XML-ATTRIBUTE-NAME
               END-IF
               IF ( DATA-VALUE-REQUIRED(RESULT) )
                   MOVE DATA-VALUE TO XML-DATA-VALUE
               END-IF
           END-IF
           .

       SKIP-WHITE-SPACE-RTN.

           IF ( CHAR-PTR NOT > XML-LENGTH )
               MOVE XML-DOCUMENT-X(CHAR-PTR) TO SKIP-WHITE-SPACE-CHECK
               IF ( SKIP-WHITE-SPACE-CHECK = SPACES
                 OR                          VALUE-TAB
                 OR                          VALUE-LF
                 OR                          VALUE-CR
                  )
                   ADD 1           TO CHAR-PTR
               END-IF
           END-IF
           .

       FIND-THIS-CHARACTER-RTN.

           MOVE '0'                TO WK-FOUND-SWITCH
           PERFORM
               UNTIL CHAR-PTR > XML-LENGTH
                  OR WK-FOUND

               IF ( XML-DOCUMENT-X(CHAR-PTR) = WK-FIND-CHAR )
                   MOVE '1'        TO WK-FOUND-SWITCH
               ELSE
                   ADD 1           TO CHAR-PTR
               END-IF
           END-PERFORM
           .

       FIND-VALID-FIRST-NAME-RTN.

           MOVE '0'                TO WK-FOUND-SWITCH
           PERFORM SEARCH-FOR-CHAR-RTN
               VARYING WK-INDEX FROM 1 BY 1
                 UNTIL WK-INDEX > TTL-ACCEPTABLE-FIRST-CHARS
                    OR WK-FOUND
            .

       SEARCH-FOR-CHAR-RTN.

           IF ( XML-DOCUMENT-X(CHAR-PTR)
                       = ACCEPTABLE-CHARS-X(WK-INDEX) )
               MOVE '1'            TO WK-FOUND-SWITCH
           END-IF
           .

       FIND-VALID-NAME-RTN.

           MOVE '1'                TO WK-FOUND-SWITCH
           PERFORM
               UNTIL CHAR-PTR > XML-LENGTH
                  OR NOT WK-Found

               MOVE '0'            TO WK-FOUND-SWITCH
               PERFORM SEARCH-FOR-CHAR-RTN
                   VARYING WK-INDEX FROM 1 BY 1
                     UNTIL WK-INDEX > TTL-ACCEPTABLE-CHARS
                        OR WK-FOUND
               IF ( WK-FOUND )
                   ADD 1           TO CHAR-PTR
               END-IF
           END-PERFORM

           MOVE ZERO               TO Char-Comp
           MOVE ZERO               TO WK-INDEX-1
           MOVE SPACES             TO NAME-VALUE
           PERFORM MOVE-NAME-VALUE-RTN
               VARYING WK-INDEX FROM BASE-PTR BY 1
                 UNTIL WK-INDEX = CHAR-PTR
           .

       MOVE-NAME-VALUE-RTN.

           ADD 1                   TO WK-INDEX-1
           MOVE XML-DOCUMENT-X(WK-INDEX)
                                   TO Char-X
           IF ( Char-X >= 'a' AND <= 'z' )
               SUBTRACT 32       FROM Char-Comp
           END-IF
           MOVE Char-X             TO NAME-VALUE-X(WK-INDEX-1)
           .

       GET-DATA-VALUE-RTN.

           MOVE SPACES             TO DATA-VALUE
           MOVE ZERO               TO WK-INDEX-1
           PERFORM MOVE-DATA-VALUE-RTN
               VARYING WK-INDEX FROM BASE-PTR BY 1
                 UNTIL WK-INDEX = ENDING-PTR

           MOVE '0'                TO WK-FOUND-SWITCH
           PERFORM REMOVE-DATA-VALUE-RTN
              VARYING WK-INDEX FROM WK-INDEX-1 BY -1
                UNTIL WK-INDEX < 1
                   OR WK-FOUND

           MOVE '0'                TO WK-FOUND-SWITCH
           MOVE ZERO               TO WK-LENGTH
           PERFORM COUNT-LEADING-SPACES-RTN
               VARYING WK-INDEX FROM 1 BY 1
                 UNTIL WK-INDEX > 1000
                    OR DATA-VALUE = SPACES
                    OR WK-FOUND

           IF ( WK-LENGTH > ZERO )
               PERFORM REMOVE-LEADING-SPACES-RTN
                   VARYING WK-INDEX FROM 1  BY 1
                     UNTIL WK-INDEX > 1010
           END-IF
           .

       MOVE-DATA-VALUE-RTN.

           ADD 1                   TO WK-INDEX-1
           MOVE XML-DOCUMENT-X(WK-INDEX) TO DATA-VALUE-X(WK-INDEX-1)
           .

       REMOVE-DATA-VALUE-RTN.

           MOVE DATA-VALUE-X(WK-INDEX) TO SKIP-WHITE-SPACE-CHECK
           IF ( SKIP-WHITE-SPACE-CHECK = SPACES
             OR                          VALUE-TAB
             OR                          VALUE-LF
             OR                          VALUE-CR
              )
               MOVE SPACES         TO DATA-VALUE-X(WK-INDEX)
           ELSE
               MOVE '1'            TO WK-FOUND-SWITCH
           END-IF
           .

       COUNT-LEADING-SPACES-RTN.

           IF ( DATA-VALUE-X(WK-INDEX) = SPACES )
               ADD 1               TO WK-LENGTH
           ELSE
               MOVE '1'            TO WK-FOUND-SWITCH
           END-IF
           .

       REMOVE-LEADING-SPACES-RTN.

           ADD 1                   TO WK-LENGTH
           MOVE DATA-VALUE-X(WK-LENGTH)
                                   TO DATA-VALUE-X(WK-INDEX)
           MOVE SPACES             TO DATA-VALUE-X(WK-LENGTH)
           .

       ENTITY-REFERENCE-RTN.

           IF ( DATA-VALUE-X(WK-INDEX) = '&' )
               MOVE '0'            TO WK-FOUND-SWITCH
               MOVE SPACES         TO WK-ENTITY
               MOVE 1              TO ENTITY-LENGTH
               MOVE WK-INDEX       TO WK-INDEX-1
               PERFORM FIND-MARKUP-CHARACTER-RTN
                   6 TIMES

               IF ( WK-FOUND )
                   MOVE '0'        TO WK-FOUND-SWITCH
                   MOVE SPACES     TO WK-MARKUP-CHARACTER
                   PERFORM MATCH-ENTITY-RTN
                       VARYING WK-INDEX-1 FROM 1 BY 1
                         UNTIL WK-INDEX-1 > TTL-ENTITY-REFERENCE
                            OR WK-FOUND
               END-IF
               IF ( WK-FOUND )
                   MOVE WK-MARKUP-CHARACTER TO DATA-VALUE-X(WK-INDEX)
                   COMPUTE WK-START-INDEX = WK-INDEX + 1
                   PERFORM MOVE-DATA-VALUE-UP-RTN
                       VARYING WK-INDEX-1 FROM WK-START-INDEX BY 1
                         UNTIL WK-INDEX-1 > 1100
               END-IF
           END-IF
           .

       FIND-MARKUP-CHARACTER-RTN.

           IF ( WK-INDEX-1 < 1000 )
               IF NOT ( WK-FOUND )
                   MOVE DATA-VALUE-X(WK-INDEX-1)
                                   TO WK-ENTITY-X(ENTITY-LENGTH)
               END-IF
               IF ( DATA-VALUE-X(WK-INDEX-1) = ';' )
                   MOVE '1'        TO WK-FOUND-SWITCH
               ELSE
                   ADD 1           TO WK-INDEX-1
                                      ENTITY-LENGTH
               END-IF
           END-IF
           .

       MATCH-ENTITY-RTN.

           IF ( WK-ENTITY = ENTITY-REFERENCE-X(WK-INDEX-1) )
               MOVE MARKUP-CHARACTER(WK-INDEX-1)
                                   TO WK-MARKUP-CHARACTER
               MOVE '1'            TO WK-FOUND-SWITCH
           END-IF
           .

       MOVE-DATA-VALUE-UP-RTN.

           COMPUTE WK-INDEX-2 = WK-INDEX-1 + ENTITY-LENGTH - 1
           MOVE DATA-VALUE-X(WK-INDEX-2)
                                   TO DATA-VALUE-X(WK-INDEX-1)
           .

       PARSING-ERROR-RTN.

           DISPLAY '**************************************************'
           DISPLAY '**************ERROR IN PGM
XMLPARSE***************'
           DISPLAY '**************************************************'
           DISPLAY 'RESULT: '              RESULT
           DISPLAY 'SEQ-NBR: '             WK-SEQ-NBR
           DISPLAY 'STATE: '               STATE
           DISPLAY 'CHAR-PTR: '            CHAR-PTR
           DISPLAY 'BASE-PTR: '            BASE-PTR
           DISPLAY 'ELEM-NAME: '           ELEM-NAME
           DISPLAY 'SAVE-ELEM-NAME: '      SAVE-ELEM-NAME
           DISPLAY 'ATTR-NAME: '           ATTR-NAME
           DISPLAY 'DATA-VALUE: '          DATA-VALUE
           DISPLAY 'NAME-VALUE: '          NAME-VALUE
           DISPLAY 'SAVE-INDEX: '          SAVE-INDEX
           DISPLAY 'XML-DOCUMENT-X(CHAR-PTR): '
                                           XML-DOCUMENT-X(CHAR-PTR)
           DISPLAY 'XML-RETURN-CODE: '     XML-RETURN-CODE
           DISPLAY 'XML-ELEMENT-NAME: '    XML-ELEMENT-NAME
           DISPLAY 'XML-ATTRIBUTE-NAME: '  XML-ATTRIBUTE-NAME
           DISPLAY 'XML-DATA-VALUE: '      XML-DATA-VALUE
           .

      * ================================================================
      *    end of source
      * ================================================================
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-05T10:41:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402051041.516f3a4a@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
jorenders@hotmail.com (JR) wrote 

> Does anybody know of you can read a xml

XMLParse.WS

  *--Version: 4.10  29/07/02  10:28:09

       01  XML-Interface.
           05  XML-Occurs              PIC 9(9) VALUE 10000.
           05  XML-Length              PIC 9(9).
           05  XML-Reserved.
               10  Save-Index          PIC 9(9).
               10  Char-Ptr            PIC 9(9).
               10  State               PIC 99.
               10  Save-Elem-Name      PIC X(50).
               10  FILLER              PIC X(30).
           05  XML-Parsed-Area.
               10  XML-Return-Code     PIC 9.
               10  XML-Element-Name    PIC X(50).
               10  XML-Attribute-Name  PIC X(50).
               10  XML-Data-Value      PIC X(1000).

       01  XML-Document.
           05  XML-Document-X          PIC X     OCCURS 10000.

      * ================================================================
      *    end of source code
      * ================================================================
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-05T10:43:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402051043.4a6190fc@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
jorenders@hotmail.com (JR) wrote 

> Does anybody know of you can read a xml
> file intelligently with a Cobol program.

      *--Version: 4.10  15/08/02  15:05:07
       IDENTIFICATION DIVISION.
       PROGRAM-ID.             xmltest.

      *    xmltest.lst
      *    xmlparse.cbl
      *    \az\xmltest.dta
      *

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

           SELECT XML-File
               ASSIGN       XML-Name
               ORGANIZATION LINE SEQUENTIAL
               FILE STATUS  File-Status
               .

       DATA DIVISION.
       FILE SECTION.

       FD  XML-File.

       01  XML-Record.
           03  XMLC                    PIC X OCCURS 256.

       WORKING-STORAGE SECTION.

       01  File-Status.
           03  FS-B1                   PIC X.
           03  FS-B2                   PIC X.

       01  DA-Index                    PIC S9(4).
       01  DA-Limit                    PIC S9(4).
       01  DA-Found                    PIC S9(4).

       01  XML-Data-Array.
           03  DA-Item                 OCCURS 100.
            05 DA-Level                PIC 99.
            05 DA-Name                 PIC X(20).
            05 DA-Attribute            PIC X(20).
            05 DA-Repeats              PIC X.
            05 DA-Value                PIC X(100).

       01  Work-Text.
           03  Work-Level.
            05 Work-LevelZ             PIC ZZZ9.
           03  Work-Name               PIC X(20).
           03  Work-Repeat             PIC X(8).

       01  FILLER.
           05  FILLER                  PIC X(32) VALUE
               'WORKING-STORAGE FOR XMLTEST >>>:'.
           05  WK-EOF-SW               PIC X.
           05  WK-TAG                  PIC X(21).
           05  TAG-TABLE.
               10  FILLER  PIC X(21) VALUE 'Start tag:'.
               10  FILLER  PIC X(21) VALUE 'End tag:'.
               10  FILLER  PIC X(21) VALUE 'Attribute-Value pair:'.
               10  FILLER  PIC X(21) VALUE 'Character data:'.
               10  FILLER  PIC X(21) VALUE 'End-of-document'.
               10  FILLER  PIC X(21) VALUE 'Parsing error.'.
               10  FILLER  PIC X(21) VALUE 'Unknown return code 7'.
               10  FILLER  PIC X(21) VALUE 'Unknown return code 8'.
               10  FILLER  PIC X(21) VALUE 'Unknown return code 9'.
           05  FILLER REDEFINES TAG-TABLE.
               10  TAG-X   PIC X(21) OCCURS 9 TIMES.

       01  File-Parameter              PIC X(80).
       01  WS-XML-Name                 PIC X(80).
       01  WS-Control-Name             PIC X(80).

       01  Tag-Level                   PIC 9(4).
       01  White                       PIC S9(4) COMP.
       01  I                           PIC S9(4) COMP.

           COPY "xmlparse.ws".     *>  \az\include\xmlparse.ws

       01  XML-Element-Name-xxx        PIC X(20).
       01  XML-Attribute-Name-xxx      PIC X(15).
       01  XML-Data-Value-xxx          PIC X(60).

       PROCEDURE DIVISION.
       Program-XMLTest.

           MOVE SPACES             TO XML-Data-Array
           MOVE ZERO               TO DA-Index
                                      DA-Limit

           MOVE SPACES             TO WS-XML-Name
                                      WS-Control-Name
           ACCEPT File-Parameter FROM COMMAND-LINE
           UNSTRING File-Parameter
               DELIMITED BY ALL SPACES
               INTO WS-XML-Name
                    WS-Control-Name

           IF ( WS-Control-Name NOT = SPACES )
               PERFORM Read-Control
           END-IF

           MOVE WS-XML-Name        TO XML-Name

           MOVE ALL ZEROES         TO XML-Reserved
           MOVE SPACES             TO XML-Parsed-Area
                                      XML-Document
           MOVE ZERO               TO XML-Return-Code
           MOVE 1                  TO XML-Length

           MOVE '0'                TO WK-EoF-Sw
           OPEN INPUT XML-File
           IF ( FS-B1 NOT = ZERO )
               DISPLAY "File Failed: " File-Status
               MOVE '1'            TO WK-EOF-SW
           END-IF

           PERFORM
               UNTIL WK-EoF-Sw = "1"

               READ XML-File
                   AT END
                       MOVE '1'    TO WK-EOF-SW
                   NOT AT END

      *            DISPLAY XML-Record

                   IF ( XML-Record = SPACES )
                       CONTINUE
                   ELSE
                       MOVE 1          TO White
                       PERFORM
                           VARYING I FROM 1 BY 1
                              UNTIL I > 256
                                 OR XML-Length >= XML-Occurs

                           IF ( XMLC(I) = SPACE
                            AND White = 1
                              )
                               CONTINUE
                           ELSE
                               MOVE XMLC(I)
                                           TO XML-Document-X(XML-Length)
                               ADD 1       TO XML-Length
                           END-IF
                           IF ( XMLC(I) = SPACE )
                               MOVE 1      TO White
                           ELSE
                               MOVE ZERO   TO White
                           END-IF
                       END-PERFORM
                   END-IF
               END-READ
           END-PERFORM
           CLOSE XML-File

      *    DISPLAY XML-Document
      *    DISPLAY "Length = " XML-Length
           MOVE ZERO           TO Tag-Level

           PERFORM Get-XML-Item
               UNTIL XML-Return-Code > 4

           MOVE ZERO           TO Return-Code

           STOP RUN
           .

       Get-XML-Item.

FJON  *    CALL 'XMLPARSE'
FJOFF      CALL 'xmlparse'
               USING XML-Interface
                     XML-Document

           MOVE XML-Element-Name       TO XML-Element-Name-xxx
           MOVE XML-Attribute-Name     TO XML-Attribute-Name-xxx
           MOVE XML-Data-Value         TO XML-Data-Value-xxx
           MOVE TAG-X(XML-Return-Code) TO WK-Tag

           MOVE ZERO                   TO DA-Found
           EVALUATE XML-Return-Code
           WHEN 1      ADD 1           TO Tag-Level
           WHEN 2      SUBTRACT 1    FROM Tag-Level
           WHEN 3      PERFORM Find-Data-Table
           WHEN 4      MOVE "CDATA"    TO XML-Attribute-Name-xxx
                       PERFORM Find-Data-Table
           END-EVALUATE

           IF ( DA-Found > ZERO )
               PERFORM Display-Data-Found
           END-IF
           .

       Display-Data-Found.

      *    DISPLAY  WK-Tag
           DISPLAY  Tag-Level
                    '/' XML-Element-Name-xxx
                    '/' XML-Attribute-Name-xxx
                    '/' XML-Data-Value-xxx
           .

       Read-Control.

           MOVE WS-Control-Name    TO XML-Name
           MOVE '0'                TO WK-EoF-Sw
           OPEN INPUT XML-File
           IF ( FS-B1 NOT = ZERO )
               DISPLAY "File Failed: " File-Status
               MOVE '1'            TO WK-EOF-SW
           END-IF

           PERFORM
               UNTIL WK-EoF-Sw = "1"

               READ XML-File
                   AT END
                       MOVE '1'    TO WK-EOF-SW
                   NOT AT END

      *            DISPLAY XML-Record

                   MOVE SPACES     TO Work-Text
                   IF ( XML-Record = SPACES )
                       CONTINUE
                   ELSE
                   IF ( XML-Record(1:1) = "+" )
                       PERFORM Add-Attribute

                   ELSE
                       UNSTRING XML-Record
                           DELIMITED BY ","
                           INTO Work-Level
                                Work-Name
                                Work-Repeat
                       ADD 1               TO DA-Limit
                       MOVE Work-LevelZ    TO DA-Level    (DA-Limit)
                       MOVE Work-Name      TO DA-Name     (DA-Limit)
                       MOVE SPACES         TO DA-Attribute(DA-Limit)
                       MOVE Work-Repeat    TO DA-Repeats  (DA-Limit)
                       MOVE SPACES         TO DA-Value    (DA-Limit)
                   END-IF
                   END-IF
               END-READ
           END-PERFORM
           CLOSE XML-File
           MOVE '0'                TO WK-EoF-Sw

      *    PERFORM Display-Data-Table
           .

       Add-Attribute.

           IF ( DA-Limit < 1 )
               CONTINUE
           ELSE
               IF ( DA-Attribute(DA-Limit) NOT = SPACES )
                   MOVE DA-Limit             TO DA-Index
                   ADD 1                     TO DA-Limit
                   MOVE DA-Level  (DA-Index) TO DA-Level  (DA-Limit)
                   MOVE DA-Name   (DA-Index) TO DA-Name   (DA-Limit)
                   MOVE DA-Repeats(DA-Index) TO DA-Repeats(DA-Limit)
                   MOVE SPACES               TO DA-Value  (DA-Limit)
               END-IF
               MOVE XML-Record(2:)           TO DA-Attribute(DA-Limit)
           END-IF
           .

       Display-Data-Table.

           PERFORM
               VARYING DA-Index FROM 1 BY 1
                 UNTIL DA-Index > DA-Limit

               DISPLAY DA-Level    (DA-Index)
                       DA-Name     (DA-Index)
                       DA-Attribute(DA-Index)
                       DA-Repeats  (DA-Index)

           END-PERFORM
           .

       Find-Data-Table.

           MOVE ZERO                   TO DA-Found
           PERFORM
               VARYING DA-Index FROM 1 BY 1
                 UNTIL DA-Index > DA-Limit
                    OR DA-Found NOT = ZERO

               IF ( XML-Element-Name-xxx   = DA-Name     (DA-Index)
                AND XML-Attribute-Name-xxx = DA-Attribute(DA-Index)
                  )
                   MOVE DA-Index       TO DA-Found
               END-IF
           END-PERFORM
           .

      * ================================================================
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-02-05T19:12:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1025qfe9f0q875e@corp.supernews.com>`
- **In-Reply-To:** `<4096148f.0402050105.28c56df4@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
JR wrote:
> Hi,
> 
…[3 more quoted lines elided]…
> returns and etc...

Speaking of this - Bill, what ever happed with the J4 discussion of the 
native language XML support document?  It looked quite promising...
```

##### ↳ ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-02-06T02:38:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com>`

```
I haven't seen minutes of the meeting yet.  Maybe Thane or Chuck have more
current information.
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-02-06T12:08:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c00s8o$29gm$1@si05.rsvl.unisys.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>`

```
ISO/IEC JTC1 has approved the New Work Item to develop a Technical Report
describing Native COBOL Syntax for XML (along with the NWI for the TR on
Collection Classes).

The committee spent quite a lot of time and effort at the January meeting
discussing the draft XML TR that was distributed and posted on the J4
website on January 23 as document 04-0008.  An updated version of this
draft, reflecting input from the committee and further refinement on the
author's part, is expected before the March J4 meeting, though I wouldn't
expect it to be posted in the first batch of documents associated with the
January meeting, which I await (the same is true for the draft Collection
Classes TR draft, 04-0009 posted on January 24, also discussed at length).

My expectation is that the XML document will ultimately be published as a
separate Technical Report against the 2002 standard, prior to the
publication of the 2008 standard (into which it will ultimately be
incorporated), in a manner similar to that I expect for Object Finalization
for Programming Language COBOL, already published as ISO/IEC TR 19755:2003.
Ditto for the Collection Classes document.

Thus, in direct answer to LXi's question, native COBOL syntax for XML is
very much an active project.

    -Chuck Stevens

.
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net...
> I haven't seen minutes of the meeting yet.  Maybe Thane or Chuck have more
> current information.
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-02-06T18:40:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1028cvt7i8rud70@corp.supernews.com>`
- **In-Reply-To:** `<c00s8o$29gm$1@si05.rsvl.unisys.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net> <c00s8o$29gm$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> Thus, in direct answer to LXi's question, native COBOL syntax for XML is
> very much an active project.

Excellent!  That looked very useful, especially as we're being directed 
to convert our interfaces to XML - it would allow us to use "regular" 
COBOL syntax to generate and receive what we're now sending as 
column-delimited files.  :)
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-02-08T18:36:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4025cbb1_1@news.athenanews.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net> <c00s8o$29gm$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:c00s8o$29gm$1@si05.rsvl.unisys.com...
<>
> Thus, in direct answer to LXi's question, native COBOL syntax for XML is
> very much an active project.
>
That MIGHT be delivered in 4 years time... <G>

(Makes you wonder about the INACTIVE and LOW priority projects, doesn't
it...?)

Pete.
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-02-09T17:02:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c09aj4$1f6j$1@si05.rsvl.unisys.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net> <c00s8o$29gm$1@si05.rsvl.unisys.com> <4025cbb1_1@news.athenanews.com>`

```
Well, could be, Peter, but that'd run it dangerously close to ISO/IEC's
mandated December 2008 publication date for the next full revision of the
standard.

The plan here is to get this Technical Report (and the Collection Classes TR
as well) published early enough  to allow some field experience with
implementations early enough so that corrections for any design problems
discovered in practice can be incorporated into that full revision.

As the first of the three planned TR's applicable to the 2002 COBOL standard
is already done (ISO/IEC 19755:2003 was published December 5), I think the
publication of the other two will likely occur rather earlier than 2008.

Maybe if you got a copy of the draft XML proposal as distributed a couple of
weeks back and submitted some constructive comments to the author it'd help
speed things along?

    -Chuck Stevens

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:4025cbb1_1@news.athenanews.com...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-02-10T05:14:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7NZVb.22120$uM2.17447@newsread1.news.pas.earthlink.net>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net> <c00s8o$29gm$1@si05.rsvl.unisys.com> <4025cbb1_1@news.athenanews.com> <c09aj4$1f6j$1@si05.rsvl.unisys.com>`

```
For those interested in the "official" time-table for the XML work, see:
  http://www.cobolportal.com/j4/files/03-0170.htm

which indicates,

"Stage 5, TR to ITTF (within 2 months of DTR ballot close)
August 1, 2006
      {Note:  Stage 5, TR to ITTF - if only one public review:  November 1,
2005}"



which to tie into what Chuck indicated below, the MORE comments that reach the
development group EARLIER, the better chance there will be that only one public
review will be required and that the "official" document will be available
November of 2005.
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** jorenders@hotmail.com (JR)
- **Date:** 2004-02-06T12:10:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4096148f.0402061210.7b353d0c@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>`

```
But the mean thing is that i have a XML file that has 
to be converted to a cobol file.

Does anybody know such a program.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>...
> I haven't seen minutes of the meeting yet.  Maybe Thane or Chuck have more
> current information.
…[28 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-02-06T18:42:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1028d3esnercr49@corp.supernews.com>`
- **In-Reply-To:** `<4096148f.0402061210.7b353d0c@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net> <4096148f.0402061210.7b353d0c@posting.google.com>`

```
JR wrote:

> But the mean thing is that i have a XML file that has 
> to be converted to a cobol file.

A "COBOL File" is simply a flat text file (in a lot of ways).  If this 
is a one-time or rarely-used process, try using Access to import the 
data from XML, then export the data in a columnar flat text file.  Once 
you make sure all the columns are lined up, it should work like a 
charm...  :)
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-02-06T13:02:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0402061302.191b7b9@posting.google.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>`

```
I haven't seen the minutes either.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>...
> I haven't seen minutes of the meeting yet.  Maybe Thane or Chuck have more
> current information.
…[28 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: A Kind of XML parser ??? (like Java)

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-02-09T13:30:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c08u59$17g2$1@si05.rsvl.unisys.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com> <1025qfe9f0q875e@corp.supernews.com> <y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net> <bfdfc3e8.0402061302.191b7b9@posting.google.com>`

```
The draft minutes for the J4 meeting are reviewed by the INCITS secretariat
before they are published.  That process is not yet complete.

    -Chuck Stevens

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0402061302.191b7b9@posting.google.com...
> I haven't seen the minutes either.
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:<y6DUb.15851$uM2.7751@newsread1.news.pas.earthlink.net>...
> > I haven't seen minutes of the meeting yet.  Maybe Thane or Chuck have
more
> > current information.
> >
…[13 more quoted lines elided]…
> > > Speaking of this - Bill, what ever happed with the J4 discussion of
the
> > > native language XML support document?  It looked quite promising...
> > >
…[11 more quoted lines elided]…
> > >
```

#### ↳ Re: A Kind of XML parser ??? (like Java)

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2004-02-08T00:30:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JqfVb.3661$um1.2914@twister.nyroc.rr.com>`
- **References:** `<4096148f.0402050105.28c56df4@posting.google.com>`

```
There are of course many ways to get at this and some of the variances depnd
upon what platform(s)/compiler(s) are at your disposal. For my purposes, two
products we are evaluating are XMLBooster (www.xmlbooster.com) and XML
Thunder (www.canamsoftware.com). Both generate custom XML parsers for a
given XML document description or schema in COBOL (or other languages). My
mainframe does not have any XML parser so these products fit my needs.

If I were using a Windows box, some of the MS .NET stuff would be very
appealing. The use of MicroFocus NetExpress might also be tempting with
their XML extensions (similar to what is being proposed for a standard).


"JR" <jorenders@hotmail.com> wrote in message
news:4096148f.0402050105.28c56df4@posting.google.com...
> Hi,
>
…[8 more quoted lines elided]…
> JR
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
