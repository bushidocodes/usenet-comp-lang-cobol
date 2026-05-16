[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In Line perform in Evaluate

_6 messages · 6 participants · 1998-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### In Line perform in Evaluate

- **From:** lvenick@aol.com (LVenick)
- **Date:** 1998-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071120083600.QAA04493@ladder03.news.aol.com>`

```
Is it possible to use an Inline-Perform with an Evaluate?-
 I'm tring to evaluate 4 different trans-codes, with each one triggering
a different routine.  It works fine when I use out-of-line performs ie:
EVALUATE TRANS-CODE
    WHEN '0'
         PERFORM 0-RTN THRU 0-EXIT
     WHEN '1'
          PERFORM.........
END-VALUATE
But if i try it as:
EVALUATE TRANS-CODE
     WHEN '0'
           PERFORM
                  ADD..........
                  MOVE.......
                  MOVE....
            END-PERFORM
      WHEN '1'
              PERFORM
                   ............
                   ............ 
               END-PERFORM
   END-EVALUATE

I get serious  syntax errors ......  
Can anyone help.
thanx,
Larry V (an eager student)
```

#### ↳ Re: In Line perform in Evaluate

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35A800CB.7994@netbox.com>`
- **References:** `<1998071120083600.QAA04493@ladder03.news.aol.com>`

```
LVenick wrote:
> 
> Is it possible to use an Inline-Perform with an Evaluate?-
…[15 more quoted lines elided]…
> I get serious  syntax errors ......

I have done this countless times without problem. Please post your exact
code and the error messages that result. There must be more to the
problem than you are showing.

Bob
```

#### ↳ Re: In Line perform in Evaluate

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a7d0a5.0@news1.ibm.net>`
- **References:** `<1998071120083600.QAA04493@ladder03.news.aol.com>`

```

LVenick wrote in message
<1998071120083600.QAA04493@ladder03.news.aol.com>...
>Is it possible to use an Inline-Perform with an Evaluate?-
> I'm tring to evaluate 4 different trans-codes, with each one triggering
…[11 more quoted lines elided]…
>I get serious  syntax errors ......


As stated you *would* get serious syntax errors: there are way too many
periods
after the verbs. Now, I bet that you don't really have that many. Only one,
right?
But even ONE is too many. Get rid of the periods and you should be ok.
The PERFORM END-PERFORM brackets are not needed, you can have several
statements after a WHEN, but no SENTENCES. Most people don't make any
distinction between a STATEMENT and a SENTENCE and usually write
one statement sentences, like:
   move a to b.
   move zero to x.
   perform xyz.

Note the period after each statement making it a sentence. These are totally
redundant and often dangerous (in IF statements and as you have discovered:
evaluate statements.

Here is program that I just ran, try it on your compiler and see.

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.    EVAL.
000300
000400 AUTHOR.        LEIF SVALGAARD.
000500 DATE-WRITTEN.  98/07/11
000600     -REVISED:  98/07/11.
000700
000800 ENVIRONMENT DIVISION.
000900
001000 CONFIGURATION SECTION.
001100 SOURCE-COMPUTER. PORTABLE.
001200 OBJECT-COMPUTER. PORTABLE.
001300
001400 DATA DIVISION.
001500
001600 WORKING-STORAGE SECTION.
001700
001800 01  EVAL                        PIC X.
001900
002000 PROCEDURE DIVISION.
002100 BEGIN-OF-PROGRAM.
002200     ACCEPT EVAL
002300     EVALUATE EVAL
002400       WHEN "A"
002500             DISPLAY "AAA"
002600             PERFORM P1
002700       WHEN "B"
002800          PERFORM
002900             DISPLAY "BBB"
003000             PERFORM P2
003100          END-PERFORM
003200       WHEN OTHER
003300          DISPLAY "OTHER"
003400     END-EVALUATE
003500     ACCEPT EVAL
003600     STOP RUN
003700     .
003800
003900 P1.
004000     DISPLAY "P1"
004100     .
004200
004300 P2.
004400     DISPLAY "P3"
004500     .

you may have to replace the standard " by the IBM style '

Here are some further style guide-lines (this will get me in trouble with
some
people, but it is sound advice). Another word: never change style in the
middle
of a program or somebody else's program:



           3.                    Coding Style


             As  emphasized   by  Somerville:  "The   style   of
           programming used  by an  individual programmer is the single
           most  important   factor  affecting   the  readability   and
           understandability of  programs".   A uniform set of sensible
           and proven  standards goes  a long  way towards a maximizing
           the benefit  of a  good programming  style.   ETK itself  is
           coded to  a uniform  standard  as  set  forth  below.    The
           overriding principle  for good  style  is  to  increase  the
           readability of  the program.   Sometimes,  the program  does
           become more  readable by  breaking some  of the  style guide
           lines, but  remember,  you  are  never  the  judge  of  what
           constitutes a readable program; your readers are.


           a.        The Structured Period


             Only use  a period  in the PROCEDURE DIVISION, where it is
           absolutely necessary, namely at the end of a paragraph or an
           IF-clause.   Always place  the period in column 12 on a line
           by itself  so that  it stands  out and  is clearly  visible.
           More errors  stem from  misplaced,  missing,  or  overlooked
           periods than from any other source.


           b.        Blank Lines


             Use precisely  one blank  line between  paragraphs.    The
           screen is  too small  to allow  for several blank lines.  Do
           not follow  a line  with a period by a blank line, unless at
           the end  of a  paragraph -  where you  should have  a single
           blank line before the next paragraph.


           c.        Paragraph Names


             Make paragraph  names descriptive  of what  the  paragraph
           does.   Do not waste characters on prefixes - either numeric
           or others - to the paragraph name.  It is common practice to
           use a  (say four-digit) numeric prefix to indicate the order
           of  paragraphs,  e.g..  1000-INITIALIZE,  2000-PROCESS,  3000-
           CLOSE-UP; there  are several  problems with  this: first, it
           leaves fewer characters for the meaningful part of the name,
           second,  during  maintenance  it  is  hard  to  respect  the
           original ordering,  and third, the numbering scheme makes it
           harder to reuse code in another program.  All these problems
           get worse  if you use some structure within the prefix, like
           all  paragraphs   executed  directly   from  the  1000-level
           paragraph  having  prefixes  1100,  1200,  1300,  etc,  with
           paragraphs on  the next  level having  prefixes  like  1110,
           1120, etc.

             Long names  should not  differ in  one  or  two  character
           positions only,  e.g.. PROCESS-MASTER-RECORD1, PROCESS-MASTER-
           RECORD2, etc.,  or  worse:  PROCESS-MASTER-RECORD,  PROCESS-
           MASTER-RECRD, etc.

             COBOL requires  that a paragraph name directly follows the
           PROCEDURE DIVISION  key words.  Always use the same name for
           this to  make it  clear that  you are  just complying with a
           (silly) rule,  e.g.. BEGIN-PROGRAM.   Do not use just BEGIN or
           START as  these are  reserved  words  (at  least  with  some
           compilers).

             Do not  be cute, e.g.. BE4-IMAGE, or SALES-TO-TALS.  Most of
           the guide  lines for  paragraph names  also apply  to  data-
           names.


           d.        Paragraph Order


             Paragraphs should  be written  in the order they are first
           encountered in the code.  Below is an example (disregard the
           fact  that  the  names  are  meaningless  and  -arghh  -  in
           alphabetical order):

             AAA.
                 MOVE ...
                 PERFORM BBB
                 PERFORM CCC
                 PERFORM DDD
                 .

             BBB.
                 PERFORM EEE
                 PERFORM CCC
                 .

             EEE.
                 PERFORM FFF
                 .

             FFF.
                 MOVE ...
                 .

             CCC.
                 MOVE ...
                 .

             DDD.
                 PERFORM CCC
                 PERFORM GGG
                 MOVE ...

             GGG.
                 MOVE ...
                 .

             This order  makes it  obvious where to insert new code and
           where to  find old  code (if  CCC is not just before GGG, it
           must be  before DDD).   It  makes it easy to cut and paste a
           paragraph and  its PERFORMed  paragraphs.   It also tends to
           maximize locality  (things being close together) which gives
           you a  performance boost  on machines using virtual or paged
           memory.


           e.        Empty Paragraphs


             An empty  paragraph contains  only the  keyword EXIT.   At
           least in  COBOL 74,  empty paragraphs  are needed for small,
           tight loops  where the  condition on  the PERFORM  statement
           itself is sufficient.  A typical example is:

                 PERFORM FIND-END-OF-TEXT-IN-WORK
                   VARYING CHAR-NBR FROM MAX-WORK BY -1
                     UNTIL CHAR-NBR < 1
                        OR WORK-CHAR (CHAR-NBR) > SPACE
                 .

              FIND-END-OF-TEXT-IN-WORK.
                 EXIT
                 .

             The example as shown with its free comment explaining what
           it does is superior to the following alternative:

                 PERFORM EMPTY-PAR
                   VARYING CHAR-NBR FROM MAX-WORK BY -1
                     UNTIL CHAR-NBR < 1
                        OR WORK-CHAR (CHAR-NBR) > SPACE
                 .

              EMPTY-PAR.
                 EXIT
                 .

             A modern  compiler will  not even  generate code  to  jump
           to/return from  the empty  paragraph, so  nothing is  gained
           trying to  reuse or  share  the  EMPTY-PAR  between  several
           loops.

             The Cobol-85 in-line empty paragraph is just as bad:

                 PERFORM
                 END-PERFORM
                   VARYING CHAR-NBR FROM MAX-WORK BY -1
                     UNTIL CHAR-NBR < 1
                        OR WORK-CHAR (CHAR-NBR) > SPACE
                 .

             In-line paragraphs  in general  do not  buy you much; they
           often obscure  the  code  by  increasing  the  span  of  the
           paragraph (especially  if nested),  and you loose the useful
           explanatory comment the named paragraph provides.


           f.        Abbreviations and Data Names


             If you  must use  abbreviations, use  a consistent  set of
           (documented and  recommended) abbreviations.   Do not invent
           abbreviations  helter-skelter,   e.g..  NO,   NBR,  NUMB,  all
           referring to  NUMBER, and do not use different abbreviations
           just  to   make  data-names   differ,  e.g..  CUSTOMER-NO  and
           CUSTOMER-NBR.

             Often, established  abbreviations present  themselves, e.g..
           SSN or  ISBN.   Use them,  even if  they are  local to  your
           company, but  try not  to invent  jargon only  understood by
           your programming team.

             Do not  use the  same variable for several things.  If you
           have a  counter to  count customer records, do not use it to
           count transaction records as well in a different part of the
           program.   Especially, avoid  temporary or  general  purpose
           variables, such  as the  infamous TEMP,  TEMP1,  TEMP2,  etc
           variables.   It  is  much  too  hard  to  keep  the  various
           simultaneous uses apart.


           g.        Comments


             COBOL is  wordy and  with the  proper coding  style can be
           almost self-documenting.   No  amount of comments can rescue
           bad code  (and it  is likely that the comment aren't too hot
           either).  Remember that comments must be maintained as well.
           It is  my (and many others) experience that comments are not
           maintained nearly as carefully as the code, if at all.

             Some people  include a  change  history  as  part  of  the
           program's comments.   A  better place  to do  this  (because
           changes rarely  stand alone  - often  several  programs  are
           changed together  to include  a feature or cure an interface
           problem) is  in an external (machine-readable) change log or
           diary.   If your  editor can  datestamp changes in col.73-80
           you have  an excellent  way of  keeping track of when things
           changed.   The bottom line here is that tools can be brought
           to bear on the problem of comments.


           h.        Indentation


             Proper and  consistent indentation is vital for making the
           program readable.  Studies have shown that no indentation and
           too much  indentation both  lead to  less readable programs.
           The optimum number of spaces to indent is four.

             Here is an example of too little or spotty indentation:

             01 DMACT-PARAMETERS.
               05 DMACT-OPERATION PIC X.
               05 DMACT-FEEDBACK PIC X.
               88 ACTION-OK VALUE IS SPACE.
               88 ACTION-CANCEL VALUE IS "C".
               88 ACTION-RESHOW VALUE IS "R".
               05 DMACT-CURSOR-POSN.
               10 DMACT-CURSOR-ROW PIC 9(2) VALUE ZERO.
               10 DMACT-CURSOR-COL PIC 9(2) VALUE ZERO.
               05 DMACT-CONTROLS.
               10 DMACT-CONTROL PIC X(2) OCCURS 16 TIMES.
               05 DMACT-SD-LINE PIC X(80).
               05 DMACT-WA-LINE PIC X(80).
               05 DMACT-SELECTION.
               10 DMACT-ACTION-MENU PIC X(2).
               10 DMACT-ACTION-CHOICE PIC X(2).
               05 DMACT-PRESENTATION.
               10 DMACT-BORDER-TYPE PIC 9.
               10 DMACT-PR-INDICATOR PIC X.
               10 DMACT-PR-MAPPING PIC X.
               10 DMACT-PR-MAPS PIC X(32).

             UPDATE-THE-RECORD.
                 PERFORM CHECK-IF-SAME-KEY-VALUES
                 IF NOT SAME-KEY-VALUES PERFORM SIGNAL-KEY-CHANGED
                 ELSE PERFORM SPECIAL-UPDATE-VALIDATION
                 IF ENTRIES-ARE-VALID
                  PERFORM GET-DATA-FIELDS-FROM-SCREEN
                     MOVE "UPDATE" TO CMPYIO-OPERATION
                  PERFORM CALL-CMPYIO
                 IF CMPYIO-FEEDBACK = SPACE
                  PERFORM PUT-DATA-FIELDS-ON-SCREEN ELSE
                 IF CMPYIO-FEEDBACK = "N" PERFORM SIGNAL-RECORD-NOT-FOUND.

             And  here  is  an  example  of  too  much  and  (therefore
           inconsistent) indentation:

             01  DMACT-PARAMETERS.
                     02      DMACT-OPERATION         PIC X.
                     02      DMACT-FEEDBACK          PIC X.
                         88  ACTION-OK                      VALUE IS SPACE.
                         88  ACTION-CANCEL                  VALUE IS "C".
                         88  ACTION-RESHOW                  VALUE IS "R".
                     02  DMACT-CURSOR-POSN.
                             03  DMACT-CURSOR-ROW    PIC 9(2)   VALUE ZERO.
                             03  DMACT-CURSOR-COL    PIC 9(2)   VALUE ZERO.
                     02  DMACT-CONTROLS.
                             03  DMACT-CONTROL       PIC X(2)
                                                            OCCURS 16 TIMES.
                     02  DMACT-SD-LINE           PIC X(80).
                     02  DMACT-WA-LINE           PIC X(80).
                     02  DMACT-SELECTION.
                             03  DMACT-ACTION-MENU     PIC X(2).
                             03  DMACT-ACTION-CHOICE     PIC X(2).
                     02  DMACT-PRESENTATION.
                             03  DMACT-BORDER-TYPE           PIC 9.
                             03  DMACT-PR-INDICATOR          PIC X.
                             03  DMACT-PR-MAPPING            PIC X.
                             03  DMACT-PR-MAPS               PIC X(32).

             UPDATE-THE-RECORD.
                 PERFORM CHECK-IF-SAME-KEY-VALUES
                 IF      NOT SAME-KEY-VALUES
                                    PERFORM SIGNAL-KEY-CHANGED
                         ELSE
                                    PERFORM SPECIAL-UPDATE-VALIDATION
                                    IF ENTRIES-ARE-VALID
                                           PERFORM
GET-DATA-FIELDS-FROM-SCREEN
                                           MOVE "UPDATE" TO CMPYIO-OPERATION
                                           PERFORM CALL-CMPYIO
                                           IF ( CMPYIO-FEEDBACK = SPACE )
                                             PERFORM
PUT-DATA-FIELDS-ON-SCREEN
                                           ELSE
                                               IF ( CMPYIO-FEEDBACK = "N")
                                               PERFORM
SIGNAL-RECORD-NOT-FOUND.

             Finally, here  is the  same code  properly indented.    It
           speaks for itself:

             01  DMACT-PARAMETERS.
                 02  DMACT-OPERATION         PIC X.
                 02  DMACT-FEEDBACK          PIC X.
                     88  ACTION-OK                      VALUE IS SPACE.
                     88  ACTION-CANCEL                  VALUE IS "C".
                     88  ACTION-RESHOW                  VALUE IS "R".
                 02  DMACT-CURSOR-POSN.
                     03  DMACT-CURSOR-ROW    PIC 9(2)   VALUE ZERO.
                     03  DMACT-CURSOR-COL    PIC 9(2)   VALUE ZERO.
                 02  DMACT-CONTROLS.
                     03  DMACT-CONTROL       PIC X(2)   OCCURS 16 TIMES.
                 02  DMACT-SD-LINE           PIC X(80).
                 02  DMACT-WA-LINE           PIC X(80).
                 02  DMACT-SELECTION.
                     03  DMACT-ACTION-MENU   PIC X(2).
                     03  DMACT-ACTION-CHOICE PIC X(2).
                 02  DMACT-PRESENTATION.
                     03  DMACT-BORDER-TYPE   PIC 9.
                     03  DMACT-PR-INDICATOR  PIC X.
                     03  DMACT-PR-MAPPING    PIC X.
                     03  DMACT-PR-MAPS       PIC X(32).

             UPDATE-THE-RECORD.
                 PERFORM CHECK-IF-SAME-KEY-VALUES
                 IF NOT SAME-KEY-VALUES
                     PERFORM SIGNAL-KEY-CHANGED
                 ELSE
                     PERFORM SPECIAL-UPDATE-VALIDATION
                     IF ENTRIES-ARE-VALID
                         PERFORM GET-DATA-FIELDS-FROM-SCREEN
                         MOVE "UPDATE" TO CMPYIO-OPERATION
                         PERFORM CALL-CMPYIO
                         IF CMPYIO-FEEDBACK = SPACE
                             PERFORM PUT-DATA-FIELDS-ON-SCREEN
                         ELSE
                         IF CMPYIO-FEEDBACK = "N"
                             PERFORM SIGNAL-RECORD-NOT-FOUND
                 .


           i.        Data Division Level Numbers


             Without indentation  it makes sense to space level numbers
           apart by  (say 5)  as in  the first  example above.  You can
           then easily  insert group levels before a collection of data
           items by  giving the group an intermediate level number such
           as 03  or 07.   As soon as you indent, the level numbers can
           no longer  be changed  like  that,  unless  you  change  the
           indentation  as  well,  and  the  rationale  for  not  using
           consecutive level  numbers has  now disappeared.  So, simply
           number levels 01, 02, 03, etc.


           j.        Numeric Literals


             Some purists  outlaw all  numeric literals except 0 and 1.
           This is  too radical.   There  are times where this does not
           improve the  readability (may even degrade it).  Compare the
           following two statements and judge for yourself.

             COMPUTE NBR-OF-SECONDS = HOURS * 3600 + MINUTES * 60 +
             SECONDS
             COMPUTE NBR-OF-SECONDS = HOURS * SECONDS-IN-ONE-HOUR
                                    + MINUTES * SECONDS-IN-ONE-MINUTE
                                    + SECONDS

             On the  other hand,  high-precision or  long  numbers  are
           prone to  typing errors,  if they  occur more than once, and
           are better defined once and for all, e.g..:

             02  PI           PIC S9.9(17) COMP VALUE +3.14159265358979324.


           k.        Parentheses


             Parentheses are  used  in  subscripting  and  to  clarify
           precedence in expressions.  Always use a space before a left
           parenthesis and  after a  right parenthesis  (except between
           two parentheses,  as in  ((abc))).   Do not  have extraneous
           spaces inside a parenthesized expression.

             Here are  some examples  of what  to do  (don't worry that
           some of the data-names are not very readable):

               MOVE SPACES TO DATA-ARRAY (SUBSCRIPT)
               COMPUTE THE-RESULT = ((OP-1 + OP-2) * OP-3 - OP-4) / OP-5

             Here are some examples of what not to do:

               MOVE SPACES TO DATA-ARRAY(SUBSCRIPT)
               MOVE SPACES TO DATA-ARRAY ( SUBSCRIPT )
               COMPUTE THE-RESULT = (ABC * DEF) + (GHI / KLM)
               IF (ABC > 123)
                   MOVE ...
               .


           l.        Alignment


             People often align the keyword TO to the same column as in
           the following  example; this  looks neat  and tidy,  but  is
           never-the-less not good style:

             BEFORE-PUTTING-SCREEN.
                 PERFORM GET-TIME-NOW
                 MOVE TIME-HH              TO PROGRAM-TIME-HH
                 MOVE TIME-MM              TO PROGRAM-TIME-MM

                 IF DATE-NOW > DATEPK-INT-DATE
                     MOVE SCREEN-DATE-SEP  TO DATEPK-DATE-SEP
                     MOVE SCREEN-DATA-MODE TO DATEPK-DATA-MODE
                     MOVE   DATE-NOW       TO DATEPK-INT-DATE
                 .
                 MOVE ERROR-MESSAGE        TO DMPOP-DATA-TEXT
                 MOVE   "MESSAGE"          TO DMPOP-HELP-SUBJECT
                 MOVE    ERROR-ID          TO DMPOP-HELP-TOPIC
                                              DMPOP-BOX-TITLE
                 MOVE 1                    TO LINE-NBR
                 PERFORM GET-MESSAGE-CONTINUATION
                   UNTIL ERROR-ATTRIBUTE NOT = "P"
                 .

             Here is the same code fragment, but with TO's only aligned
           if  the  moves  are  to  data-items  within  the  same  data
           structure.   In this  way you  subtly tell  the reader which
           data items are related and the readability improves:

             BEFORE-PUTTING-SCREEN.
                 PERFORM GET-TIME-NOW
                 MOVE TIME-HH TO PROGRAM-TIME-HH
                 MOVE TIME-MM TO PROGRAM-TIME-MM

                 IF DATE-NOW > DATEPK-INT-DATE
                     MOVE SCREEN-DATE-SEP  TO DATEPK-DATE-SEP
                     MOVE SCREEN-DATA-MODE TO DATEPK-DATA-MODE
                     MOVE   DATE-NOW       TO DATEPK-INT-DATE
                 .
                 MOVE ERROR-MESSAGE TO DMPOP-DATA-TEXT
                 MOVE   "MESSAGE"   TO DMPOP-HELP-SUBJECT
                 MOVE    ERROR-ID   TO DMPOP-HELP-TOPIC
                                       DMPOP-BOX-TITLE
                 MOVE 1 TO LINE-NBR
                 PERFORM GET-MESSAGE-CONTINUATION
                   UNTIL ERROR-ATTRIBUTE NOT = "P"
                 .
```

#### ↳ Re: In Line perform in Evaluate

- **From:** Grehom@my-dejanews.com
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oa6kf$o4e$1@nnrp1.dejanews.com>`
- **References:** `<1998071120083600.QAA04493@ladder03.news.aol.com>`

```
As far as I'm aware it's perfectly possible - preferable if the in-line code
is fairly short show me the real listing and I'll revise my opinion (NOT).

In article <1998071120083600.QAA04493@ladder03.news.aol.com>,
  lvenick@aol.com (LVenick) wrote:
> Is it possible to use an Inline-Perform with an Evaluate?-
>  I'm tring to evaluate 4 different trans-codes, with each one triggering
…[26 more quoted lines elided]…
>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: In Line perform in Evaluate

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071214031800.KAA26523@ladder01.news.aol.com>`
- **References:** `<6oa6kf$o4e$1@nnrp1.dejanews.com>`

```
>In article <1998071120083600.QAA04493@ladder03.news.aol.com>,
>  lvenick@aol.com (LVenick) wrote:
…[29 more quoted lines elided]…
>
Hard to tell from the fragment, but I would look for any periods in your
in-line perform statements. Remember, a period terminates the entire EVALAUATE,
so following WHEN clauses and the END-EVALUATE are going to get flagged.

Cheers,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: In Line perform in Evaluate

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298192.75628.9222@kcbbs.gen.nz>`
- **References:** `<6oa6kf$o4e$1@nnrp1.dejanews.com>`

```
> > But if i try it as:
> > EVALUATE TRANS-CODE
…[13 more quoted lines elided]…
> > I get serious  syntax errors ......


   1) you do not need the PERFORM and END-PERFORM to do a
        sequence of statements under a WHEN unless you
        need to do that sequence multiple times.

   2) however, there is nothing wrong with the structure of
        your code, in-line PERFORMs are perfectly valid (as
        are a sequence of statements.

   3) you probably left a full stop or two on the lines of
        code when you moved them from the performed paragraph
        to the in-line perform.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
