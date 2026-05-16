[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Length of string

_24 messages · 9 participants · 1998-10 → 1998-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Length of string

- **From:** "Patrick L Archibald" <Patrick.Archibald@HomeTelco.Com>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71cndj$22a$1@news3.infoave.net>`

```
Hi

I am trying to determine the fastest method for
finding the length of a string.  I have a working-storage
variable that is PIC X(1024) and the strings I place
in it can be from 1 character to 1024 characters long.

The following statment works good until my string
value contains large spaces in it. "S" is the name of
my PIC X(1024) variable.

           INSPECT S TALLYING WS-STRING-LENGTH
                   FOR CHARACTERS
                   BEFORE INITIAL '    '.

I could also do:

PERFORM VARYING X FROM 1024 BY -1
                  UNTIL X = 1 OR
                            S(X:1) NOT = SPACES
              do-nothing-here
END-PERFORM.

Does anyone else have a suggestion or comments?

Thanx, Patrick
Patrick.Archibald@HomeTelco.com
http://Hometelco.com/pla/
```

#### ↳ Re: Length of string

- **From:** "Patrick L Archibald" <Patrick.Archibald@HomeTelco.Com>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71d3nq$bbe$1@news3.infoave.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net>`

```
Thanks fellow programmers.  I decided to use the STRING verb like
this to solve my string length problem.

COMPUTE WS-STRING-LENGTH = 1.
MOVE SPACES TO S.

STRING '<HTML><BODY BGCOLOR=#FFFFFF>'
       '<HEAD><TITLE>'
       'Home Telephone Company, Inc AS/400 CGI'
       '</TITLE></HEAD>'
       '<A HREF="/intranet/Welcome.html">Home</A>'
       '<H1>Display Subscriber By Name</H1>'
       DELIMITED BY SIZE
       INTO S
       POINTER WS-STRING-LENGTH
END-STRING.

Thanx for the suggestions, Patrick



Patrick L Archibald wrote in message <71cndj$22a$1@news3.infoave.net>...
>Hi
>
…[28 more quoted lines elided]…
>
```

#### ↳ Re: Length of string

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net>`

```
Patrick L Archibald wrote:
>
>I am trying to determine the fastest method for
…[20 more quoted lines elided]…
>Does anyone else have a suggestion or comments?

We had a long thread on just this subject about a month ago.  You
can look it up in DejaNews.  I think you will find the code below
about as quick as any on most compilers.  As an alternate, you can
try REDEFINING SW-STRING as a PIC X OCCURS 1024 TIMES and use an
index rather than address modification.  Which is faster depends
on the compiler.  Testing for spaces first adds some overhead, but
eliminate one of the end tests within the loop.  Again, the trade
is system and compiler dependent.

       01  STRING-WORK-AREA.
           03  SW-SIZE                     PIC  9(04)   COMP.
           03  SW-STRING                   PIC  X(1024) VALUE SPACES.

           IF (SW-STRING = SPACES)
               MOVE 0 TO SW-SIZE
           ELSE
               MOVE FUNCTION LENGTH(SW-STRING) TO SW-SIZE
               PERFORM UNTIL SW-STRING(SW-SIZE:1) NOT = SPACE
                   SUBTRACT 1 FROM SW-SIZE
               END-PERFORM
           END-IF.
```

##### ↳ ↳ Re: Length of string

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3639f5cb.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net>`

```
Judson McClendon wrote in message ...
>Patrick L Archibald wrote:
>>
…[44 more quoted lines elided]…
>--


Often when you have the situation you describe, the string is
potentially up to 1024 chars long, but most of the time is a lot
smaller, so it pays to have a faster way of skipping large amounts
of trailing spaces.  The following program illustrates a portable
way of doing that. This method is likely to be very efficient on all
platforms and can easily be generalized to any string size.

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.    TLEN.
000300
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
001800 01  STRING-HANDLING.
001900     02  STRING-LENGTH           PIC S9(5)  COMP.
002000     02  THE-STRING
002100         03  THE-STRING-CHAR     PIC X      OCCURS 1024 TIMES.
002200     02  THE-STRING-PIECES       REDEFINES  THE-STRING.
002300         03  THE-STRING-1        PIC X(256).
002400         03  THE-STRING-2        PIC X(256).
002500         03  THE-STRING-3        PIC X(256).
002600         03  THE-STRING-4        PIC X(256).
002700
002800 PROCEDURE DIVISION.
002900 BEGIN-PROGRAM.
003000     MOVE ZEROES TO THE-STRING
003100     PERFORM GET-STRING-LENGTH
003200     DISPLAY STRING-LENGTH
003300
003400     MOVE SPACES TO THE-STRING
003500     PERFORM GET-STRING-LENGTH
003600     DISPLAY STRING-LENGTH
003700
003800     MOVE "ABCD" TO THE-STRING
003900     PERFORM GET-STRING-LENGTH
004000     DISPLAY STRING-LENGTH
004100
004200     STOP RUN
004300     .
004400
004500 GET-STRING-LENGTH.
004600     MOVE 1024 TO STRING-LENGTH
004700     IF THE-STRING-4 = SPACES
004800         SUBTRACT 256 FROM STRING-LENGTH
004900     .
005000     IF THE-STRING-3 = SPACES
005100         SUBTRACT 256 FROM STRING-LENGTH
005200     .
005300     IF THE-STRING-2 = SPACES
005400         SUBTRACT 256 FROM STRING-LENGTH
005500     .
005600     IF THE-STRING-1 = SPACES
005700         SUBTRACT 256 FROM STRING-LENGTH
005800     ELSE
005900         PERFORM CHECK-STRING-FOR-SPACE
006000           VARYING STRING-LENGTH FROM STRING-LENGTH BY -1
006100             UNTIL THE-STRING-CHAR (STRING-LENGTH) NOT = SPACE
006200     .
006300
006400 CHECK-STRING-FOR-SPACE.
006500     EXIT
006600     .
```

###### ↳ ↳ ↳ Re: Length of string

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3639fccc.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net>`

```
let me quickly correct my hasty code.
Leif Svalgaard wrote in message <3639f5cb.0@news1.ibm.net>...
>Judson McClendon wrote in message ...
>>Patrick L Archibald wrote:
…[117 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Length of string

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lyn_1.1564$Hr5.2508172@news3.mia.bellsouth.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
>
>000100 IDENTIFICATION DIVISION.
…[60 more quoted lines elided]…
>006600     .

I like your idea, but there is a logic bug in the code above.  If you
have one or more 256 byte blocks of spaces at the right points in the
string, it will not find the correct length.  It is only valid to
check a block for spaces if all the blocks to the right are also
spaces, except for the rightmost block, of course.  The following code
will correct this, and should also run faster, on average.  And since
you have hard coded the string size, don't use subtract, but move.

004600     IF THE-STRING-4 NOT = SPACES
004700         MOVE 1024 TO STRING-LENGTH
004800     ELSE
004900         MOVE 768 TO STRING-LENGTH
005000         IF THE-STRING-3 = SPACES
005100             MOVE 512 TO STRING-LENGTH
005300             IF THE-STRING-2 = SPACES
005400                 MOVE 256 TO STRING-LENGTH
005600                 IF THE-STRING-1 = SPACES
005700                     MOVE 1 TO STRING-LENGTH
005800     .
005900         PERFORM CHECK-STRING-FOR-SPACE
006000           VARYING STRING-LENGTH FROM STRING-LENGTH BY -1
006100             UNTIL THE-STRING-CHAR (STRING-LENGTH) NOT = SPACE
006200     .

Also, performing a paragraph, even an empty one, is likely going to
generate a subroutine call, probably killing the efficiency gained
above.  If I were going to perform a paragraph instead of an inline
perform, I would use GOTO for the loop, it's much more efficient, with
only one subroutine call.  Note that if you were using PERFORM THRU,
you could code a GOTO EXIT if THE-STRING-1 = SPACES and bypass the
perform altogether.  This is why most languages support a block exit
construct, which a GOTO EXIT (or EXIT PARAGRAPH when available) serves
well for.  Consider this alternative:

               03  THE-STRING-CHAR     PIC X      OCCURS 1024 TIMES
                                                  INDEXED BY TSX.

           MOVE ... TO THE-STRING
           PERFORM GET-STRING-LENGTH
              THRU GET-STRING-LENGTH-EXIT
           DISPLAY STRING-LENGTH
           .

       GET-STRING-LENGTH.
           IF (THE-STRING-4 NOT = SPACES)
               SET STX TO 1024
           ELSE
               SET STX TO 768
               IF (THE-STRING-3 = SPACES)
                   SET STX TO 512
                   IF (THE-STRING-2 = SPACES)
                       SET STX TO 256
                       IF (THE-STRING-1 = SPACES)
                           MOVE 0 TO STRING-LENGTH
                           GO TO GET-STRING-LENGTH-EXIT
           .
               PERFORM CHECK-STRING-FOR-SPACE
                  THRU CHECK-STRING-FOR-SPACE-EXIT
               SET STRING-LENGTH TO STX
           .
       GET-STRING-LENGTH-EXIT.
           EXIT
           .

       CHECK-STRING-FOR-SPACE.
           IF (THE-STRING-CHAR(STX) = SPACE)
               SET STX DOWN BY 1
               GO TO CHECK-STRING-FOR-SPACE
           .
       CHECK-STRING-FOR-SPACE-EXIT.
           EXIT
           .

I know a lot of you get convulsions at the sight of a GOTO or a PERFORM
THRU, but the above CODE is not only portable from COBOL 74 up, it is
about as efficient as you can get, for this algorithm on most compilers
I am familiar with.  Personally, the sight of single periods on a line
after a block of code gives me convulsions. :-)
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363a0cfc.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net> <lyn_1.1564$Hr5.2508172@news3.mia.bellsouth.net>`

```
You were right about the bug (I've corrected it).
But, Judson, there is really no need for the EXITs:
>           .
>               PERFORM CHECK-STRING-FOR-SPACE
…[14 more quoted lines elided]…
>           .


Just clean it up to look like this (also no need for extraneous parentheses
for the  IF):
>               PERFORM CHECK-STRING-FOR-SPACE
>               SET STRING-LENGTH TO STX
…[6 more quoted lines elided]…
>           .

No need for a GO TO, it is just as good to simply test it in the
perform .

BTW, the SUBTRACT 256 were there to make it easier to maintain
(fewer hard-coded constants).

Anyway, now we are nit-picking. The basic idea of my posting
(no matter what the silly details) was to use the very efficient
group tests on 256 chars at a time to cut out 256 times thru the
loop.
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GEo_1.1574$Hr5.2552359@news3.mia.bellsouth.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net> <lyn_1.1564$Hr5.2508172@news3.mia.bellsouth.net> <363a0cfc.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
>You were right about the bug (I've corrected it).

Sorry, I had already written my post before I saw it.

>But, Judson, there is really no need for the EXITs:

The EXIT was just to eliminate the final test for length zero
before the perform.  In this particular case, there was only
one test, but sometimes there could be many tests.  That's
why most languages, including the new COBOL standard, provide
a block exit construct.

>BTW, the SUBTRACT 256 were there to make it easier to maintain
>(fewer hard-coded constants).

I agree.

>Anyway, now we are nit-picking. The basic idea of my posting
>(no matter what the silly details) was to use the very efficient
>group tests on 256 chars at a time to cut out 256 times thru the
>loop.


I wasn't trying to be critical, it is a good idea.
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 5)_

- **From:** "Hugh Candlin" <hugh.candlin@getridofspam.worldnet.att.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71gvjn$bie@bgtnsc03.worldnet.att.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net> <lyn_1.1564$Hr5.2508172@news3.mia.bellsouth.net> <363a0cfc.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <363a0cfc.0@news1.ibm.net>...
<SNIP>
>Anyway, now we are nit-picking. The basic idea of my posting
>(no matter what the silly details) was to use the very efficient
>group tests on 256 chars at a time to cut out 256 times thru the
>loop.

What do you think of this:
The problem can be solved in 21 executed statements maximum,
using a hard-coded binary search, counting each IF / ELSE as 2 statements.

The example is structured using an 8-byte variable length to keep
the size of my post down.  The technique will work equally well
for a 1024-byte variable with some cut-and-paste expansion
of the Procedure Division logic and the Working Storage definition.

No loop, no compute, no goto.

PROCEDURE DIVISION logic:

IF  POS-0005-THRU-0008 > SPACES
 IF  POS-0007-THRU-0008 > SPACES
  IF  POS-0008-THRU-0008 > SPACES
      MOVE +0008 TO STRING-LENGTH
  ELSE
      MOVE +0007 TO STRING LENGTH
 ELSE
  IF  BE-0006-THRU-0006 > SPACES
      MOVE +0006 TO STRING-LENGTH
  ELSE
      MOVE +0005 TO STRING LENGTH
ELSE
 IF  POS-0003-THRU-0004 > SPACES
  IF  POS-0004-THRU-0004 > SPACES
      MOVE +0004 TO STRING-LENGTH
  ELSE
      MOVE +0003 TO STRING LENGTH
 ELSE
  IF  POS-0002-THRU-0002 > SPACES
      MOVE +0002 TO STRING-LENGTH
  ELSE
      MOVE +0001 TO STRING LENGTH.

WORKING-STORAGE SECTION.
01  STRING-LENGTH                 PIC S9(05) COMP-3.
01  POS-0001-THRU-0008.
    05  POS-0001-THRU-0004.
        10  POS-0001-THRU-0002.
            15  POS-0001-THRU-0001 PIC X.
            15  POS-0002-THRU-0002 PIC X.
        10  POS-0003-THRU-0004.
            15  POS-0003-THRU-0003 PIC X.
            15  POS-0004-THRU-0004 PIC X.
    05  POS-0005-POS-0008.
        10  POS-0005-THRU-0006.
            15  POS-0005-THRU-0005 PIC X.
            15  POS-0006-THRU-0006 PIC X.
        10  POS-0007-THRU-0008.
            15  POS-0007-THRU-0007 PIC X.
            15  POS-0008-THRU-0008 PIC X.
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363c749b.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net> <lyn_1.1564$Hr5.2508172@news3.mia.bellsouth.net> <363a0cfc.0@news1.ibm.net> <71gvjn$bie@bgtnsc03.worldnet.att.net>`

```
This is actually not very efficient, because some characters will be tested
several times (in the previous posts the maximum number was 2).
Even in your little example character 8 is tested 3 times.. For a 1024
character string the maximum rises to 10 times.

The test *should* be NOT EQUAL rather than GREATER to be strictly
accurate (which probanly is not needed, so more nit-picking).

Hugh Candlin wrote in message <71gvjn$bie@bgtnsc03.worldnet.att.net>...
>
>Leif Svalgaard wrote in message <363a0cfc.0@news1.ibm.net>...
…[60 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363ca799.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <v3m_1.1540$Hr5.2461890@news3.mia.bellsouth.net> <3639f5cb.0@news1.ibm.net> <lyn_1.1564$Hr5.2508172@news3.mia.bellsouth.net> <363a0cfc.0@news1.ibm.net> <71gvjn$bie@bgtnsc03.worldnet.att.net> <363c749b.0@news1.ibm.net>`

```
I retract my 1st comment on this post.

Leif Svalgaard wrote in message <363c749b.0@news1.ibm.net>...
>This is actually not very efficient, because some characters will be tested
>several times (in the previous posts the maximum number was 2).
…[71 more quoted lines elided]…
>
```

#### ↳ Re: Length of string

- **From:** Jeff Farkas <JeffreyFarkas@~nospam~earthlink.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71cpqv$b47$1@fir.prod.itd.earthlink.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net>`

```


Patrick L Archibald wrote:

> Hi
>
…[25 more quoted lines elided]…
> http://Hometelco.com/pla/

Hi Patrick,

    I have found that the second method, scanning from right to left
to work out the best when you can never be sure what is in the
string.
```

##### ↳ ↳ Re: Length of string

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981030131322.28289.00001266@ng76.aol.com>`
- **References:** `<71cpqv$b47$1@fir.prod.itd.earthlink.net>`

```
On Fri, 30 Oct 1998 10:56:19 -0500
"Patrick L Archibald" <Patrick.Archibald@HomeTelco.Com>
asked

>>
I am trying to determine the fastest method for
finding the length of a string.  I have a working-storage
variable that is PIC X(1024) and the strings I place
in it can be from 1 character to 1024 characters long.

The following statment works good until my string
value contains large spaces in it. "S" is the name of
my PIC X(1024) variable.

           INSPECT S TALLYING WS-STRING-LENGTH
                   FOR CHARACTERS
                   BEFORE INITIAL '    '.

I could also do:

PERFORM VARYING X FROM 1024 BY -1
                  UNTIL X = 1 OR
                            S(X:1) NOT = SPACES
              do-nothing-here
END-PERFORM.

Does anyone else have a suggestion or comments?


<<

It is some time effective to guard scanned fields with sentries

 01  S-SCAN.
       05 S-SENTRY  PIC X(1) VALUE SPACES.
       05 S-WORK     PIC X(1024) VALUE SPACES.
       05 S-SENTRY  PIC X(1) VALUE SPACES.


*REINIT S-SENTRY AS NECESSARY.

*WITHIN ITERATION
  MOVE WS-NEXT-INPUT TO S-WORK.

 PERFORM VARYING X FROM 1 BY 1
       UNTIL   S(X:1)  = SPACES
              do-nothing-here
 END-PERFORM.
```

###### ↳ ↳ ↳ Re: Length of string

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981030141854.28289.00001278@ng76.aol.com>`
- **References:** `<19981030131322.28289.00001266@ng76.aol.com>`

```
My previous response got cut short, sorry.
Let me try again.

On Fri, 30 Oct 1998 10:56:19 -0500
"Patrick L Archibald" <Patrick.Archibald@HomeTelco.Com>
asked

>>
I am trying to determine the fastest method for
finding the length of a string.  I have a working-storage
variable that is PIC X(1024) and the strings I place
in it can be from 1 character to 1024 characters long.

The following statment works good until my string
value contains large spaces in it. "S" is the name of
my PIC X(1024) variable.

           INSPECT S TALLYING WS-STRING-LENGTH
                   FOR CHARACTERS
                   BEFORE INITIAL '    '.

I could also do:

PERFORM VARYING X FROM 1024 BY -1
                  UNTIL X = 1 OR
                            S(X:1) NOT = SPACES
              do-nothing-here
END-PERFORM.

Does anyone else have a suggestion or comments?


<<

It is sometimes effective to guard scanned fields with a sentry

 01  S-SCAN.
       05 S-WORK     PIC X(1024) VALUE SPACES.
       05 S-SENTRY  PIC X(1) VALUE SPACES.


*REINIT S-SENTRY AS NECESSARY.

*WITHIN ITERATION
  MOVE WS-NEXT-INPUT TO S-WORK.

 PERFORM VARYING X FROM 1 BY 1
       UNTIL   S(X:1)  = SPACES
              do-nothing-here
 END-PERFORM.

This approach eliminates the test for the max index from within the inner loop.
This is a classic technique.  It starts from the begining and will always only
scan the exact number of characters.  It also allows for a max string length of
1024 (some other approaches posted could have trouble with the length 1024).  

The value X will point to the delimitter, which is at a position of
string-length-plus-one.

As far as I know there is no way to inform INSPECT that you have a sentry, so
it will always have a max index (field length as max) check within the loop it
generates.  Also compilers tend to generate service module calls for
elaborately architected verbs like INSPECT. It has all kinds of bells and
wistles and special features that must be checked for in general, but are not
needed by your specific scan requirement.  (Those things are good just like all
other Santa Claus grab bag items, but you asked about performance).

Your data occurence pattern will make a big difference in this situation.  If
your strings are typically less than 1/2 the length of the work area ( that is
512 = 1/2 of 1024).  Then a forward scan will exit quickest on average.  If on
the other hand the data occurence is that typically strings are greater than
1/2 the scanned work area, then a reverse scan would be best.

*REVERSE SCAN SKETCH
 01  S-SCAN.
       05 S-SENTRY  PIC X(1) VALUE 'X'.
       05 S-WORK     PIC X(1024) VALUE SPACES.


*REINIT S-SENTRY AS NECESSARY.

*WITHIN ITERATION
  MOVE WS-NEXT-INPUT TO S-WORK.

 PERFORM VARYING X FROM 1025 BY -1
       UNTIL   S(X:1)  IS ALPHABETIC
              do-nothing-here
 END-PERFORM.
*HERE THE SENTRY MAY NEED TO BE IMPROVED, 
*AND THE UNTIL TEST ALSO;
*FOR EXAMPLE HIGH-VALUES IN BOTH
*BUT THIS SHOWS MY POINT

In this approach, like the previous X=1 means a string length of zero, X=1025
means a string length of 1024.

And it is not unreasonable to build a switcher, if this is really super
critical code, AND YOUR DATA IS AS CLEAN AS YOU HAVE IMPLIED.  

*ASSUMING ALWAYS FILL S-WORK
*WITH TRAILING BLANKS
 IF S-WORK(512:1) = SPACES
    PERFORM S-SCAN-LEFT-TO-RIGHT-SHORTIE
 ELSE
    PERFORM S-SCAN-RIGHT-TO-LEFT-BIG-BURTHA 
 END-IF.
*WHEREIN INCIDENTALLY THE INDEX
*CALLED 'X' GETS PRIMED TO 512 OR SO
*(A SINGLE IF ELIMINATES 512 CHECKS, BUT
*ONLY IF DATA IS AS CLEAN AS YOU INDICATE).

You can, of course, nest further IFs, eliminating 256 tests on the second
depth, and only 128 on the third depth. And certainly you could use an EVALUATE
expression for the same short-cuts.

This is actually just a variation of the posted suggestion to check subsections
of 256-byte areas for spaces (that takes 256 memory references each, the above
sketch takes 1/2/3 depending upon your interest in dividing the issue into
half/quarter/eighth).


All of the 'clean data' stuff raises the other issue that is behind the
question.  Actually, it is much  better to NOT use MOVEs that do alot of
wasteful blank filling, followed by scans to try to find where the waste
starts.  You have not asked about that, but it is relevant if you can at all
get control before the X(1024) area is populated.

That is, you will save CPU time all over the place, IF you can get the notion
of delimitters and 'sentries' built into the data flow from the begining by
design. (similar savings can result from preserving the meaning of input record
lengths of variable lenght records, for example).

Always move only what you need to move, possibly using UNSTRING and STRING
verbs.

I know that you may not be able to, but when ever you can influence the design
of the data flow; try vigorously to avoid scanning fixed length buffers when
the typical item is way less than max length.

This matter can be stated another way. You are able to cut the long scan short
by testing certain bytes or fields for blanks only because you wasted the
resources to put the blanks there! Yes maybe there is nothing you can do about
it, but if there is, do it as early in the sequence as possible.

Best Wishes


Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363a26e0.0@news1.ibm.net>`
- **References:** `<19981030131322.28289.00001266@ng76.aol.com> <19981030141854.28289.00001278@ng76.aol.com>`

```
Try one more time!

You always have to scan from the rear.
If you scan from the beginning you stop on the first space.

RKRayhawk wrote in message <19981030141854.28289.00001278@ng76.aol.com>...
>My previous response got cut short, sorry.
>Let me try again.
…[49 more quoted lines elided]…
>This approach eliminates the test for the max index from within the inner
loop.
>This is a classic technique.  It starts from the begining and will always
only
>scan the exact number of characters.  It also allows for a max string
length of
>1024 (some other approaches posted could have trouble with the length
1024).
>
>The value X will point to the delimitter, which is at a position of
>string-length-plus-one.
>
>As far as I know there is no way to inform INSPECT that you have a sentry,
so
>it will always have a max index (field length as max) check within the loop
it
>generates.  Also compilers tend to generate service module calls for
>elaborately architected verbs like INSPECT. It has all kinds of bells and
>wistles and special features that must be checked for in general, but are
not
>needed by your specific scan requirement.  (Those things are good just like
all
>other Santa Claus grab bag items, but you asked about performance).
>
>Your data occurence pattern will make a big difference in this situation.
If
>your strings are typically less than 1/2 the length of the work area ( that
is
>512 = 1/2 of 1024).  Then a forward scan will exit quickest on average.  If
on
>the other hand the data occurence is that typically strings are greater
than
>1/2 the scanned work area, then a reverse scan would be best.
>
…[20 more quoted lines elided]…
>In this approach, like the previous X=1 means a string length of zero,
X=1025
>means a string length of 1024.
>
…[16 more quoted lines elided]…
>depth, and only 128 on the third depth. And certainly you could use an
EVALUATE
>expression for the same short-cuts.
>
>This is actually just a variation of the posted suggestion to check
subsections
>of 256-byte areas for spaces (that takes 256 memory references each, the
above
>sketch takes 1/2/3 depending upon your interest in dividing the issue into
>half/quarter/eighth).
…[5 more quoted lines elided]…
>starts.  You have not asked about that, but it is relevant if you can at
all
>get control before the X(1024) area is populated.
>
>That is, you will save CPU time all over the place, IF you can get the
notion
>of delimitters and 'sentries' built into the data flow from the begining by
>design. (similar savings can result from preserving the meaning of input
record
>lengths of variable lenght records, for example).
>
…[3 more quoted lines elided]…
>I know that you may not be able to, but when ever you can influence the
design
>of the data flow; try vigorously to avoid scanning fixed length buffers
when
>the typical item is way less than max length.
>
>This matter can be stated another way. You are able to cut the long scan
short
>by testing certain bytes or fields for blanks only because you wasted the
>resources to put the blanks there! Yes maybe there is nothing you can do
about
>it, but if there is, do it as early in the sequence as possible.
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 5)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981030173831.28289.00001332@ng76.aol.com>`
- **References:** `<363a26e0.0@news1.ibm.net>`

```
On Fri, 30 Oct 1998 14:51:42 -0600
 "Leif Svalgaard" <leif@ibm.net>
disagreed with a proposed solution, saying

>>
Try one more time!

You always have to scan from the rear.
If you scan from the beginning you stop on the first space.
<<

(The try one more time was in reference to a previous post that got chopped,
and Leif is kind enough to be looking at my re-attempt to transmit).

Leif,

I respect your comment, however... 

If you review the original post from Patrick L Archibald, there is an implied
contiguous sequence of CHARACTER data until the first SPACE.  Thats why I have
elaborate notes to the effect "... AND YOUR (the origirnal poster's) DATA IS AS
CLEAN AS YOU (he) HAVE IMPLIED." 

Going back to original ...

On Fri, 30 Oct 1998 10:56:19 -0500
"Patrick L Archibald" Patrick.Archibald@HomeTelco.Com>
>>           INSPECT S TALLYING WS-STRING-LENGTH
>                   FOR CHARACTERS
>                   BEFORE INITIAL '    '.
>
<<

I just took that at face value, and elaborated.  The forward scan I suggest
uses SPACE as the delimitter, just as the original INSPECT. The backward scan
uses, simplistically, an 'X', and comments suggest use of special encoding like
HIGH-VALUE.


You actually are very right: in many situations, the original INSPECT would
come up short, and so would my forward scan. I assumed that the original poster
either did consider that or would see the point of my emphasis on CLEAN DATA.

Many unpredictable buffer content situations will completely destroy any hope
of processing them quickly, I think you will agree. Sometimes requiring us to
pre-init the whole (1024 byte) work buffer before moving variable length input
to it, or STRINGing things into it.  Sometimes requiring us to INSPECT ...
REPLACING to get rid of the byte values we want to use as sentries.

I worked with a CICS system some time ago that presented data from an outside
communication line on several screens.  Much of the data was encoded and we had
to translate it, so we were entirely responsible for establishing those values
on the screen.  But a number of fields were just nominal text data for
presentation.  And the protocol called for guaranteed valid text.

But it didn't turn out that way. We would get PROGs (a screen failure) on many
SENDs because of utter trash in these fields.  In the begining we tried to
understand the problems at the other end, and put in limited clean up logic. 
The problems in production were very expensive, however, so we learned to
simply INSPECT ... CONVERTING every text field destined for the screens,
scrubbing up anything that was not printable, ON EVERY TEXT FIELD.

In retrospect it would have been cheaper to give in early.  But we had these
guarnatees, you see.
And we had this dream of minimum CPU time for handling these messages.

Yet it remains true that in environments where you have control of the data,
use of well chosen sentries are a proven traditional method of eliminating the
max index check from wihtin the scan loop.  

This method is used in table searches as well, where the item you are scanning
for is always placed at table position max-plus-one. And you scan from one
until found. You always find it.  If you find it at max-plus-one, of course, it
not there! Piece of cake.

If the data in a buffer is reliable enough, and flush left, and contiguous, you
can scan forward looking for the first fill character, and backwards looking
for the first meaningful cipher; using sentries eliminates the need for max
index check wihtin the scan. With adjustment, more rare flush right data can be
handled with similar efficiency.

Best Wishes,










 
Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363a527c.0@news1.ibm.net>`
- **References:** `<363a26e0.0@news1.ibm.net> <19981030173831.28289.00001332@ng76.aol.com>`

```

RKRayhawk wrote in message <19981030173831.28289.00001332@ng76.aol.com>...
>On Fri, 30 Oct 1998 14:51:42 -0600
> "Leif Svalgaard" <leif@ibm.net>
…[5 more quoted lines elided]…
>(The try one more time was in reference to a previous post that got
chopped,
>and Leif is kind enough to be looking at my re-attempt to transmit).
>
…[4 more quoted lines elided]…
>If you review the original post from Patrick L Archibald, there is an
implied
>contiguous sequence of CHARACTER data until the first SPACE.  Thats why I
have
>elaborate notes to the effect "... AND YOUR (the origirnal poster's) DATA
IS AS
>CLEAN AS YOU (he) HAVE IMPLIED."
>
…[8 more quoted lines elided]…
><<


The original follows here:
----------------------------------
The following statment works good until my string
value contains large spaces in it. "S" is the name of
my PIC X(1024) variable.

           INSPECT S TALLYING WS-STRING-LENGTH
                   FOR CHARACTERS
                   BEFORE INITIAL '    '.
----------------------------------
and seems to imply that the inspect didn't work when
there were embedded spaces (although the meaning
of "large spaces" is not quite clear)

Anyway, I don't want to quibble. The benefit of several
people presenting different solutions is clear.

So far in this thread we have seen the following *fundamental*
techniques:
1) sequential searching
2) sentinels
3) quick test of large contiguous pieces of the string to avoid
    looping over every character.
4) exiting loops in the middle using GO TOs

The details don't matter, *unless* the routine is
*really* in the innermost loop and is the source of
most of the CPU time spent (AND that the time
spent is considerable). In this case, you should
experiment with your specific compiler to find
*the* solution that works on your system. In all
other cases a portable solution with reasonable
(i.e. cheap) optimization is preferable.

-----------------

end of thread....
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 7)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298304.63261.15201@kcbbs.gen.nz>`
- **References:** `<363a527c.0@news1.ibm.net>`

```
In message <<363a527c.0@news1.ibm.net>> "Leif Svalgaard" <leif@ibm.net> writes:
> 
>            INSPECT S TALLYING WS-STRING-LENGTH
…[5 more quoted lines elided]…
> of "large spaces" is not quite clear)

It would also fail to give the correct result when the 
string was > 1020 as it would fail to find the terminator
and would respond with 1024.

> So far in this thread we have seen the following *fundamental*
> techniques:
…[4 more quoted lines elided]…
> 4) exiting loops in the middle using GO TOs

It may also be that a binary chop technique would work
reasonably efficiently.

Because the variable is 1024, start with Sp = 513 and Sl = 512

         PERFORM
             UNTIL Sl < 1

              IF ( Str(Sp:Sl) = SPACES )
                   DIVIDE 2 INTO Sl
                   SUBTRACT Sl FROM Sp
              ELSE
                   DIVIDE 2 INTO Sl
                   ADD Sl        TO Sp
              END-IF
         END-PERFORM
         < final coding not implemented >
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 6)_

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71gc3n$3no_002@news.netdirect.net>`
- **References:** `<363a26e0.0@news1.ibm.net> <19981030173831.28289.00001332@ng76.aol.com>`

```
In article <19981030173831.28289.00001332@ng76.aol.com>,
   rkrayhawk@aol.com (RKRayhawk) wrote:
+On Fri, 30 Oct 1998 14:51:42 -0600
+ "Leif Svalgaard" <leif@ibm.net>
+disagreed with a proposed solution, saying
+
+>>
+Try one more time!
+
+You always have to scan from the rear.
+If you scan from the beginning you stop on the first space.
+<<
+
+(The try one more time was in reference to a previous post that got chopped,
+and Leif is kind enough to be looking at my re-attempt to transmit).
+
+Leif,
+
+I respect your comment, however... 
+
+If you review the original post from Patrick L Archibald, there is an implied
+contiguous sequence of CHARACTER data until the first SPACE.  Thats why I 
have
+elaborate notes to the effect "... AND YOUR (the origirnal poster's) DATA IS 
AS
+CLEAN AS YOU (he) HAVE IMPLIED." 
+
+Going back to original ...

Yes, indeed, let's go back to the original. I think if you look carefully
at what you have cited here...

+On Fri, 30 Oct 1998 10:56:19 -0500
+"Patrick L Archibald" Patrick.Archibald@HomeTelco.Com>
+>>           INSPECT S TALLYING WS-STRING-LENGTH
+>                   FOR CHARACTERS
+>                   BEFORE INITIAL '    '.

.. you will find that the literal consists of *four* spaces. Hence the
original poster's comment that the method works unless the data contains
"large spaces."
+>
+<<
+
+I just took that at face value, and elaborated.  The forward scan I suggest
+uses SPACE as the delimitter, just as the original INSPECT.

Except that the original INSPECT uses a delimiter of four spaces, not one.
```

#### ↳ Re: Length of string

- **From:** Cityboy@Concentric.Net [Ron]
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71irj0$lhb@journal.concentric.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net>`

```

01  INPUT-AREA    PIC X(1024).
01  TALLY-COUNTER PIC 9(4).
01  DATA-LENGTH   PIC 9(4).

MOVE ZERO TO TALLY-COUNTER.
INSPECT FUNCTION REVERSE(INPUT-AREA)
    TALLYING TALLY-COUNTER FOR LEADING SPACES.
COMPUTE DATA-LENGTH = LENGTH OF INPUT-AREA - TALLY-COUNTER.
```

##### ↳ ↳ Re: Length of string

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363cf8d7.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <71irj0$lhb@journal.concentric.net>`

```
We timed this one several weeks ago in this NG. It is extremely slow, so
does not meet the requirement of being *efficient*.

Cityboy@Concentric.Net [Ron] wrote in message
<71irj0$lhb@journal.concentric.net>...
>
>01  INPUT-AREA    PIC X(1024).
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Length of string

- **From:** Cityboy@Concentric.Net [Ron]
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71jakc$ic6@chronicle.concentric.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <71irj0$lhb@journal.concentric.net> <363cf8d7.0@news1.ibm.net>`

```
In <363cf8d7.0@news1.ibm.net>, "Leif Svalgaard" <leif@ibm.net> writes:
>We timed this one several weeks ago in this NG. It is extremely slow, so
>does not meet the requirement of being *efficient*.

"Extremely slow" on what platform?
```

###### ↳ ↳ ↳ Re: Length of string

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363d359d.0@news1.ibm.net>`
- **References:** `<71cndj$22a$1@news3.infoave.net> <71irj0$lhb@journal.concentric.net> <363cf8d7.0@news1.ibm.net> <71jakc$ic6@chronicle.concentric.net>`

```
Cityboy@Concentric.Net [Ron] wrote in message
<71jakc$ic6@chronicle.concentric.net>...
>In <363cf8d7.0@news1.ibm.net>, "Leif Svalgaard" <leif@ibm.net> writes:
>>We timed this one several weeks ago in this NG. It is extremely slow, so
>>does not meet the requirement of being *efficient*.
>
>"Extremely slow" on what platform?


This is a good question. We did not test it on all
possible platforms with all possible compilers.

As I recall, the platform was a PC and the compilers were
MicroFocus and Fujitsu.


I'm reproducing one of the posts from then:

Judson McClendon wrote in message ...
>Since we're starting to really get into the optimization thing, let's
>take a look at another tweak.  I took Rick's program and tweaked it
…[8 more quoted lines elided]…
>   0.33 jud-coded


I have converted the TEST3 program to Cobol-85 (the issue, I learned
-thanks Bill and Andreas - was the non-standard 'move function' statements).
I left in the comp-5 in order to compare with your times. I also timed
separately
the reverse function and the inspect statement, as well as cirrected for the
loop overhead. Here are my results for two different compilers on a 266MHz
PC MMX; I used your loop count of 500,000. The first number is for Fujitsu
V3.10 (32-bit). The second is for MicroFocus V3.1 DOS (16-bit).
My program are at the end of this after yours.

loop:           3.19   4.01
times below are corrected for loop:
rick:            58.38  28.03
reverse:     26.41  10.22
inspect:      2.91    3.13
Judson:     34.05  16.31
HandRick:   6.32    3.41
HandJud:    3.62    2.04


I'm puzzled the hand-coded results are about 10 times
slower than yours, while the functions are 2 times as
fast.

It would be interesting to see what Acucobol and RM
give. I suspect that at least with Acucobol, then results would be
reversed, with the hand-coded versions being the slowest.

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.  TEST3.
000300* RIGHT JUSTIFY
000400
000500 ENVIRONMENT DIVISION.
000600 CONFIGURATION SECTION.
000700 SOURCE-COMPUTER.  IBM-PC.
000800 OBJECT-COMPUTER.  IBM-PC.
000900
001000 DATA DIVISION.
001100 WORKING-STORAGE SECTION.
001200
001300 01  INPUT-FIELD                 PIC X(30).
001400 01  OUTPUT-FIELD                PIC X(30).
001500
001600 01  COUNTERS.
001700     02  COUNTER                 PIC S9(4) COMP-5.
001800     02  I                       PIC S9(4) COMP-5.
001900     02  J                       PIC S9(4) COMP-5.
002000     02  K                       PIC S9(4) COMP-5.
002100     02  LOOP                    PIC S9(9) COMP-5 VALUE +5000000.
002200
002300 01  TEST-VARIABLES.
002400     02  THE-TIME                PIC 9(8).
002500     02  FILLER                  REDEFINES  THE-TIME.
002600         03  THE-HOURS           PIC 99.
002700         03  THE-MINUTES         PIC 99.
002800         03  THE-SECONDS         PIC 99.
002900         03  THE-CENTISECONDS    PIC 99.
003000
003100     02  TIME-CENTISECONDS       PIC 9(8).
003200     02  TIME-BEFORE             PIC 9(8).
003300     02  TIME-AFTER              PIC 9(8).
003400     02  TIME-OVERHEAD           PIC 9(8)   VALUE ZEROES.
003500     02  SECONDS-ELAPSED         PIC 9(3).99.
003600     02  CHAR                    PIC X.
003700
003800 PROCEDURE DIVISION.
003900 TEST-3-START.
004000     ACCEPT THE-TIME FROM TIME
004100     DISPLAY "start " NO ADVANCING
004200     PERFORM DISPLAY-TIME-ELAPSED
004300
004400     PERFORM TEST3-START-LOOP LOOP TIMES
004500     DISPLAY "loop  " NO ADVANCING
004600     PERFORM DISPLAY-TIME-ELAPSED
004700     COMPUTE TIME-OVERHEAD = TIME-AFTER - TIME-BEFORE
004800     DISPLAY "times below are corrected for loop"
004900
005000     PERFORM TEST3-START-RICK LOOP TIMES
005100     DISPLAY "rick      " NO ADVANCING
005200     PERFORM DISPLAY-TIME-ELAPSED
005300
005400     PERFORM TEST3-START-REVERSE LOOP TIMES
005500     DISPLAY "reverse   "  NO ADVANCING
005600     PERFORM DISPLAY-TIME-ELAPSED
005700
005800     PERFORM TEST3-START-INSPECT LOOP TIMES
005900     DISPLAY "inspect   " NO ADVANCING
006000     PERFORM DISPLAY-TIME-ELAPSED
006100
006200     PERFORM TEST3-START-JUDSON LOOP TIMES
006300     DISPLAY "judson    " NO ADVANCING
006400     PERFORM DISPLAY-TIME-ELAPSED
006500
006600     PERFORM TEST3-START-HAND-RICK LOOP TIMES
006700     DISPLAY "hand rick " NO ADVANCING
006800     PERFORM DISPLAY-TIME-ELAPSED
006900
007000     PERFORM TEST3-START-HAND-JUD  LOOP TIMES
007100     DISPLAY "hand jud  " NO ADVANCING
007200     PERFORM DISPLAY-TIME-ELAPSED
007300
007400     ACCEPT CHAR
007500     STOP RUN
007600     .
007700
007800 DISPLAY-TIME-ELAPSED.
007900     PERFORM GET-CENTISECONDS
008000     MOVE TIME-CENTISECONDS TO TIME-BEFORE
008100
008200     ACCEPT THE-TIME FROM TIME
008300     PERFORM GET-CENTISECONDS
008400     COMPUTE TIME-AFTER = TIME-CENTISECONDS - TIME-OVERHEAD
008500
008600     COMPUTE SECONDS-ELAPSED = (TIME-AFTER - TIME-BEFORE) / 100
008700     DISPLAY SECONDS-ELAPSED
008800     .
008900
009000 GET-CENTISECONDS.
009100     COMPUTE TIME-CENTISECONDS = (THE-HOURS    * 3600
009200                               +  THE-MINUTES  * 60
009300                               +  THE-SECONDS) * 100
009400                               +  THE-CENTISECONDS
009500     .
009600
009700 TEST3-START-LOOP.
009800     MOVE "ABCDEFGHIJKLM" TO INPUT-FIELD
009900     .
010000
010100 TEST3-START-RICK.
010200     MOVE "ABCDEFGHIJKLM" TO INPUT-FIELD
010300     IF INPUT-FIELD NOT = SPACES
010400         MOVE FUNCTION REVERSE (INPUT-FIELD) TO INPUT-FIELD
010500         MOVE 1 TO COUNTER
010600         INSPECT INPUT-FIELD TALLYING COUNTER FOR LEADING SPACES
010700         MOVE FUNCTION REVERSE (INPUT-FIELD (COUNTER:))
010800           TO INPUT-FIELD (COUNTER:)
010900     END-IF
011000     .
011100
011200 TEST3-START-REVERSE.
011300     MOVE "ABCDEFGHIJKLM" TO INPUT-FIELD
011400     IF INPUT-FIELD NOT = SPACES
011500         MOVE FUNCTION REVERSE (INPUT-FIELD) TO INPUT-FIELD
011600     END-IF
011700     .
011800
011900 TEST3-START-INSPECT.
012000     MOVE "                  ABCDEFGHIJKLM" TO INPUT-FIELD
012100     IF INPUT-FIELD NOT = SPACES
012200         MOVE 1 TO COUNTER
012300         INSPECT INPUT-FIELD TALLYING COUNTER FOR LEADING SPACES
012400     END-IF
012500     .
012600
012700 TEST3-START-JUDSON.
012800     MOVE "ABCDEFGHIJKLM" TO INPUT-FIELD
012900     IF INPUT-FIELD NOT = SPACES
013000         MOVE FUNCTION REVERSE(INPUT-FIELD) TO OUTPUT-FIELD
013100         MOVE 1 TO COUNTER
013200         INSPECT OUTPUT-FIELD TALLYING COUNTER FOR LEADING SPACES
013300         STRING INPUT-FIELD DELIMITED BY SIZE
013400           INTO OUTPUT-FIELD WITH POINTER COUNTER
013500         MOVE OUTPUT-FIELD TO INPUT-FIELD
013600     END-IF
013700     .
013800
013900 TEST3-START-HAND-RICK.
014000     MOVE "ABCDEFGHIJKLM" TO INPUT-FIELD
014100     IF INPUT-FIELD NOT = SPACES
014200         COMPUTE I, J = FUNCTION LENGTH (INPUT-FIELD)
014300         PERFORM UNTIL INPUT-FIELD (I:1) NOT = SPACE
014400             SUBTRACT 1 FROM I
014500         END-PERFORM
014600         PERFORM UNTIL I = 0
014700             MOVE INPUT-FIELD (I:1) TO INPUT-FIELD (J:1)
014800             SUBTRACT 1 FROM I
014900             SUBTRACT 1 FROM J
015000         END-PERFORM
015100         IF J > 0
015200             MOVE SPACES TO INPUT-FIELD (1:J)
015300         END-IF
015400     END-IF
015500     .
015600
015700 TEST3-START-HAND-JUD.
015800     MOVE "ABCDEFGHIJKLM" TO INPUT-FIELD
015900     IF INPUT-FIELD NOT = SPACES
016000         COMPUTE I, J = FUNCTION LENGTH (INPUT-FIELD)
016100         PERFORM UNTIL INPUT-FIELD (I:1) NOT = SPACE
016200             SUBTRACT 1 FROM I
016300         END-PERFORM
016400         SUBTRACT I FROM J
016500         ADD J, 1 GIVING K
016600         MOVE INPUT-FIELD (1:I) TO OUTPUT-FIELD (K:I)
016700         IF J > 0
016800             MOVE SPACES TO OUTPUT-FIELD (1:J)
016900         END-IF
017000         MOVE OUTPUT-FIELD TO INPUT-FIELD
017100     END-IF
017200     .

>
>Note that with the overhead of 500,000 perform loops, the time to
…[121 more quoted lines elided]…
>
```

#### ↳ Re: Length of string

- **From:** d.s.kirk@ix.netcom.com (David)
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363fb5fa.33588987@nntp.ix.netcom.com>`
- **References:** `<71cndj$22a$1@news3.infoave.net>`

```
On Fri, 30 Oct 1998 10:56:19 -0500, "Patrick L Archibald"
<Patrick.Archibald@HomeTelco.Com> wrote:

>Hi
>
…[27 more quoted lines elided]…
>
hmmm.... ok, i've read several constructive and innovative posts...
all well and good.  i'm wondering though, if we would help you better
if you explained WHY you need to do this. For example, if we knew the
business need, it may be that a well-constructed UNSTRING statement
may eliminate the need to count the size of the characters in the
array. If the elements that are filling the array have a consistent
pattern of data elements, then there may be a better solution than
counting. I mention this because we often see questions that assume a
particular technique without explaining the issue.  
david
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
