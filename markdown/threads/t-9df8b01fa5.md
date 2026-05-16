[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Show me your code...

_27 messages · 11 participants · 2000-10_

---

### Show me your code...

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-06T01:32:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%W9D5.7211$Ly1.83712@news5.giganews.com>`

```
Anyone interested in showing their coding style?

Here's a complete procedure division circa 1993 - a vendor package.  How
would you change it, or is it perfect-o just like it is?

Yes, students, you'll see a ton of this at your first job...

Cliff
--------------------------------------------
       PROCEDURE DIVISION.
       START-OF-PGM.
           OPEN INPUT I04.
           OPEN INPUT P07.
           OPEN OUTPUT I00.
       INITIALIZE-OUTPUT-REC.
           MOVE SPACES TO I00-P.
           MOVE 'DCI' TO SYS-ID-I00-P.
           MOVE 'I00' TO FILEID-I00-P.
           MOVE 'P' TO REC-ID-I00-P.
           PERFORM READ-I04 THRU READ-I04-EXIT.
           PERFORM READ-P07 THRU READ-P07-EXIT.
       COMPARE-KEYS.
           IF KEY-I04 IS EQUAL TO 99999
             AND KEY-P07 IS EQUAL TO 99999
               PERFORM WRITE-I00 THRU WRITE-I00-EXIT
               GO TO END-OF-PROGRAM.
           IF KEY-I04 IS EQUAL TO KEY-P07
               IF PROJ-LEVEL-I04-P IS GREATER THAN SAVE-PROJ-LEVEL
                   MOVE PROJ-LEVEL-I04-P TO SAVE-PROJ-LEVEL
                   MOVE EDP-SEQ-NO-I04-P TO SAVE-EDP-SEQ-NO
                   MOVE PROJ-ID-I04-P TO SAVE-PROJ-ID
                   PERFORM READ-I04 THRU READ-I04-EXIT
                   PERFORM READ-P07 THRU READ-P07-EXIT
                   GO TO COMPARE-KEYS
               ELSE
                   PERFORM WRITE-I00 THRU WRITE-I00-EXIT
                   MOVE PROJ-LEVEL-I04-P TO SAVE-PROJ-LEVEL
                   MOVE EDP-SEQ-NO-I04-P TO SAVE-EDP-SEQ-NO
                   MOVE PROJ-ID-I04-P TO SAVE-PROJ-ID
                   PERFORM READ-I04 THRU READ-I04-EXIT
                   PERFORM READ-P07 THRU READ-P07-EXIT
                   GO TO COMPARE-KEYS.
           IF KEY-I04 IS GREATER THAN KEY-P07
               IF PROJ-LEVEL-P07-P IS GREATER THAN SAVE-PROJ-LEVEL
                   MOVE PROJ-LEVEL-P07-P TO SAVE-PROJ-LEVEL
                   MOVE EDP-SEQ-NO-P07-P TO SAVE-EDP-SEQ-NO
                   MOVE PROJ-ID-P07-P TO SAVE-PROJ-ID
                   PERFORM READ-P07 THRU READ-P07-EXIT
                   GO TO COMPARE-KEYS
               ELSE
                   PERFORM WRITE-I00 THRU WRITE-I00-EXIT
                   MOVE PROJ-LEVEL-P07-P TO SAVE-PROJ-LEVEL
                   MOVE EDP-SEQ-NO-P07-P TO SAVE-EDP-SEQ-NO
                   MOVE PROJ-ID-P07-P TO SAVE-PROJ-ID
                   PERFORM READ-P07 THRU READ-P07-EXIT
                   GO TO COMPARE-KEYS.
           MOVE 1 TO DUMP-CODE.
           GO TO DUMP-ROUTINE.
       READ-I04.
           READ I04
           AT END
               MOVE 99999 TO KEY-I04
               GO TO READ-I04-EXIT.
           IF SYS-ID-I04-P EQUAL TO 'EOF'
               GO TO READ-I04.
           MOVE REC-ID-I04-P TO LTR-HOLD.
           PERFORM SEARCH-FOR-LTR THRU SEARCH-FOR-LTR-EXIT.
           MOVE LTR (LTR-NDX) TO REC-ID-I04-P.
           IF REC-ID-I04-P IS NOT EQUAL TO 'P'
               GO TO READ-I04.
           IF DELETED-I04-P EQUAL TO 'Y'
               GO TO READ-I04.
           MOVE EDP-SEQ-NO-I04-P TO KEY-I04.
       READ-I04-EXIT.
           EXIT.
       READ-P07.
           READ P07
           AT END
               MOVE 99999 TO KEY-P07
               GO TO READ-P07-EXIT.
           IF REC-ID-P07-P IS NOT EQUAL TO 'P'
               GO TO READ-P07.
           IF DELETED-P07-P EQUAL TO 'Y'
               GO TO READ-P07.
           IF EDP-SEQ-NO-P07-P IS EQUAL TO 1
               GO TO READ-P07.
           MOVE EDP-SEQ-NO-P07-P TO KEY-P07.
       READ-P07-EXIT.
           EXIT.
       WRITE-I00.
           MOVE SAVE-EDP-SEQ-NO TO EDP-SEQ-NO-I00-P.
           MOVE SAVE-PROJ-ID TO PROJ-ID-I00-P.
           WRITE I00-REC FROM I00-P
               .
           IF  I00-STATUS NOT EQUAL TO '00'
               MOVE I00-STATUS TO DUMP-STATUS
               MOVE 'STATUS RETURN FROM WRITE' TO DUMP-TEXT2
               MOVE 2 TO DUMP-CODE
               GO TO DUMP-ROUTINE.
       WRITE-I00-EXIT.
           EXIT.
       SEARCH-FOR-LTR.
           MOVE 1 TO LTR-NDX.
       SEARCH-LTR-LOOP.
           IF  LTR-HOLD NOT EQUAL TO LTR (LTR-NDX)
               IF  LTR-NDX NOT EQUAL TO 26
                   ADD 1 TO LTR-NDX
                   GO TO SEARCH-LTR-LOOP
               ELSE
                   MOVE 1 TO LTR-NDX.
           COMPUTE LTR-NDX = 27 - LTR-NDX.
       SEARCH-FOR-LTR-EXIT.
           EXIT.
       DUMP-ROUTINE.
      * REMOVED THIS CODE FOR BREVITY AND REPLACED WITH...
           CONTINUE.
       END-OF-PROGRAM.
           CLOSE I00
                 I04
                 P07
                 .
           STOP RUN.
-----------------------------
```

#### ↳ Re: Show me your code...

- **From:** David Bretz <DBretz@mescoma.com>
- **Date:** 2000-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39DD45D9.CBF03ABA@mescoma.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com>`

```
hey....at least there are no ALTER GO TO commands!!  :-)

Cliff Peterson wrote:
> 
> Anyone interested in showing their coding style?
…[121 more quoted lines elided]…
> -----------------------------
```

##### ↳ ↳ Re: Show me your code...

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cghD5.13218$l35.199696@iad-read.news.verio.net>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <39DD45D9.CBF03ABA@mescoma.com>`

```
In article <39DD45D9.CBF03ABA@mescoma.com>,
David Bretz  <DBretz@mescoma.com> wrote:
>This is a multi-part message in MIME format.
>--------------C4EBA21424A5EF157DBAE6E3
…[3 more quoted lines elided]…
>hey....at least there are no ALTER GO TO commands!!  :-)

Hey, where'd *you* learn COBOL... isn't it ALTER [name] TO PROCEED TO?

DD
```

##### ↳ ↳ Re: Show me your code...

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-06T05:38:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wzdD5.8771$bI6.414805@news1.giganews.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <39DD45D9.CBF03ABA@mescoma.com>`

```

On  5-Oct-2000, David Bretz <DBretz@mescoma.com> wrote:

> hey....at least there are no ALTER GO TO commands!!  :-)

You know, when someone asked about ALTERs in another thread, I did a scan of
our production source library and found five (of about 18,000).  Shoulda
picked one of those...
```

#### ↳ Re: Show me your code...

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GclD5.26421$WK6.599529@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com>`

```
       PROCEDURE DIVISION.
       START-OF-PGM.
           OPEN OUTPUT I00
           MOVE SPACES TO I00-P
           MOVE 'DCI' TO SYS-ID-I00-P
           MOVE 'I00' TO FILEID-I00-P
           MOVE  'P'  TO REC-ID-I00-P

           OPEN INPUT I04, P07
           PERFORM READ-I04
           PERFORM READ-P07
           PERFORM COMPARE-AND-READ
              UNTIL KEY-I04 = 99999
                AND KEY-P07 = 99999

           PERFORM WRITE-I00
           PERFORM END-OF-PROGRAM
           .

       COMPARE-AND-READ.
           IF KEY-I04 = KEY-P07
               IF PROJ-LEVEL-I04-P NOT > SAVE-PROJ-LEVEL
                   PERFORM WRITE-I00
               END-IF
               MOVE PROJ-LEVEL-I04-P TO SAVE-PROJ-LEVEL
               MOVE EDP-SEQ-NO-I04-P TO SAVE-EDP-SEQ-NO
               MOVE PROJ-ID-I04-P    TO SAVE-PROJ-ID
               PERFORM READ-I04
           ELSE
           IF KEY-I04 > KEY-P07
               IF PROJ-LEVEL-P07-P NOT > SAVE-PROJ-LEVEL
                   PERFORM WRITE-I00
               END-IF
               MOVE PROJ-LEVEL-P07-P TO SAVE-PROJ-LEVEL
               MOVE EDP-SEQ-NO-P07-P TO SAVE-EDP-SEQ-NO
               MOVE PROJ-ID-P07-P    TO SAVE-PROJ-ID
           ELSE
           IF KEY-I04 < KEY-P07
               MOVE 1 TO DUMP-CODE
               PERFORM FATAL-DUMP-AND-STOP
           .
           PERFORM READ-P07
           .

       READ-I04.
           MOVE ZEROES TO KEY-I04
           READ I04
           PERFORM READ-MORE-I04
             UNTIL KEY-I04 > ZEROES
           .

       READ-MORE-I04.
           IF I04-STATUS > ZEROES
               MOVE 99999 TO KEY-I04
           ELSE
           IF SYS-ID-I04-P = 'EOF'
               READ I04
           ELSE
               MOVE REC-ID-I04-P TO LTR-HOLD
               PERFORM SEARCH-FOR-LTR
               MOVE LTR (LTR-NDX) TO REC-ID-I04-P
               IF REC-ID-I04-P NOT = 'P'
               OR DELETED-I04-P    = 'Y'
                   READ I04
               ELSE
                   MOVE EDP-SEQ-NO-I04-P TO KEY-I04
           .

       READ-P07.
           MOVE ZEROES TO KEY-P07
           READ P07
           PERFORM READ-MORE-P07
             UNTIL KEY-P07 > ZEROES
           .

       SEARCH-FOR-LTR.
           PERFORM SEARCH-LTR-TABLE
             VARYING LTR-NDX FROM 26 BY -1
               UNTIL LTR-HOLD = LTR (LTR-NDX)
                  OR LTR-NDX  = 1

           COMPUTE LTR-NDX = 27 - LTR-NDX
           .

       SEARCH-LTR-TABLE.
           EXIT
           .

       READ-MORE-P07.
           IF P07-STATUS > ZEROES
               MOVE 99999 TO KEY-P07
           ELSE
           IF REC-ID-P07-P NOT = 'P'
           OR DELETED-P07-P    = 'Y'
           OR EDP-SEQ-NO-P07-P =  1
               READ P07
           ELSE
               MOVE EDP-SEQ-NO-P07-P TO KEY-P07
           .

       WRITE-I00.
           MOVE SAVE-EDP-SEQ-NO TO EDP-SEQ-NO-I00-P
           MOVE SAVE-PROJ-ID    TO PROJ-ID-I00-P
           WRITE I00-REC FROM I00-P

           IF  I00-STATUS > ZEROES
               MOVE  I00-STATUS                TO DUMP-STATUS
               MOVE 'STATUS RETURN FROM WRITE' TO DUMP-TEXT2
               MOVE  2                         TO DUMP-CODE
               PERFORM FATAL-DUMP-AND-STOP
           .

       FATAL-DUMP-AND-STOP.
      * REMOVED SOME CODE FOR BREVITY
           PERFORM END-OF-PROGRAM
           .

       END-OF-PROGRAM.
           CLOSE I00, I04, P07
           STOP RUN
           .


Cliff Peterson <cliff.peterson@spamcop.net> wrote in message
news:%W9D5.7211$Ly1.83712@news5.giganews.com...
> Anyone interested in showing their coding style?
>
…[120 more quoted lines elided]…
> -----------------------------
```

##### ↳ ↳ Re: Show me your code...

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rCsD5.37693$355.5232822@typhoon.nyroc.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com>`

```
   I've only been programming in COBOL for 2 years, but I have one pet peeve
with those trying to eliminate all GO TOs:
   Do "good" programmers think it is proper to PERFORM a paragraph which
always executes a STOP RUN or GO BACK? IMHO, a GO TO is much more clear,
especially if the paragraph name does not make it obvious that there is no
return. If I see PERFORM ERROR-RTN, I assume (without looking at ERROR-RTN)
that an error will be handled, ant the line following the PERFORM will be
executed next. If ERROR-RTN always stops the processing, shouldn't it be
accessed with a GO TO, so the reader knows it will never return?
   At least the FATAL-DUMP-AND-STOP and END-OF-PROGRAM names make it clear
there is no return. However, PERFORM still _implies_ a return.

Leif Svalgaard <leif@leif.org> wrote in message
news:GclD5.26421$WK6.599529@typhoon.austin.rr.com...
>        PROCEDURE DIVISION.
>        START-OF-PGM.
…[119 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Show me your code...

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0SsD5.26501$WK6.609416@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com>`

```

William Bub <fathafluff@hotmail.com> wrote in message
news:rCsD5.37693$355.5232822@typhoon.nyroc.rr.com...
>    I've only been programming in COBOL for 2 years, but I have one pet
peeve
> with those trying to eliminate all GO TOs:

it is not that we are 'trying' to avoid a GO TO. The GO TO simply never
is needed in the first place. A 'disaster bail-out' is part a structured
programming anyway. Now, I tried to stay close to the spirit of the
original program, but if I had to design (not re-design) the program
my way, I would have worked the logic differently. As it is, the program
is too simple-minded about errors.

>    Do "good" programmers think it is proper to PERFORM a paragraph which
> always executes a STOP RUN or GO BACK? IMHO, a GO TO is much more clear,
> especially if the paragraph name does not make it obvious that there is no
> return.

but the paragraph name DOES make it clear that there is no return:

> At least the FATAL-DUMP-AND-STOP and END-OF-PROGRAM names make it clear
> there is no return.

> However, PERFORM still _implies_ a return.

that is debatable.  the phrases PERFORM QUIT or PERFORM STOP do not
suggest a return. Conversely GO TO may not always means that you are
assured of no return:

A.
   GO TO B.
C.
  ....
B.
  ....
  GO TO C.
```

###### ↳ ↳ ↳ Re: Show me your code...

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zGLD5.13628$bI6.643246@news1.giganews.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com>`

```

On  6-Oct-2000, "William Bub" <fathafluff@hotmail.com> wrote:

>    Do "good" programmers think it is proper to PERFORM a paragraph which
> always executes a STOP RUN or GO BACK?

Show me your code.  You can even take Leif's or my version, change it to
show your preferences, then post it.

The intent of this thread was not to provoke a battle, but just to let
programmers show their preferences and style.  We'd love to see yours!

Cliff
```

###### ↳ ↳ ↳ Re: Show me your code...

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39DF2DDA.747DB025@brazee.net>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com>`

```


William Bub wrote:
> 
>    I've only been programming in COBOL for 2 years, but I have one pet peeve
…[9 more quoted lines elided]…
> there is no return. However, PERFORM still _implies_ a return.

I agree with you.  However, there are some compilers which create more
efficient code if they do not find any GO TOs in the code, and some
shops which have no GO TO standards.

I code GO TO only to get to a paragraph which exits the program.
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JkHD5.43983$3y3.828831@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39DF2DDA.747DB025@brazee.net>`

```
> >    I've only been programming in COBOL for 2 years, but I have one pet
peeve
> > with those trying to eliminate all GO TOs:
> >    Do "good" programmers think it is proper to PERFORM a paragraph which
> > always executes a STOP RUN or GO BACK? IMHO, a GO TO is much more clear,
> > especially if the paragraph name does not make it obvious that there is
no
> > return. If I see PERFORM ERROR-RTN, I assume (without looking at
ERROR-RTN)
> > that an error will be handled, ant the line following the PERFORM will
be
> > executed next. If ERROR-RTN always stops the processing, shouldn't it be
> > accessed with a GO TO, so the reader knows it will never return?
> >    At least the FATAL-DUMP-AND-STOP and END-OF-PROGRAM names make it
clear
> > there is no return. However, PERFORM still _implies_ a return.
>
> I agree with you.  However, there are some compilers which create more
> efficient code if they do not find any GO TOs in the code, and some
> shops which have no GO TO standards.


I did not want to start a new GO TO war. I have no problems with
GO TO FATAL-DUMP-AND-STOP, it is just that I didn't use the
GO TO out of pure habit. Howard's point is also true, my main
compiler (Realia) is one of them. In tight loops (such as the one
in the example: SEARCH-FOR-LTR) this can really make a
difference.
```

###### ↳ ↳ ↳ Re: Show me your code...

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e64428.7836029@news1.frb.gov>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com>`

```
On Fri, 06 Oct 2000 22:45:43 GMT, William Bub wrote:

>Leif Svalgaard <leif@leif.org> wrote in message
>news:GclD5.26421$WK6.599529@typhoon.austin.rr.com...
[snip most of program]
>>        FATAL-DUMP-AND-STOP.
>>       * REMOVED SOME CODE FOR BREVITY
>>            PERFORM END-OF-PROGRAM
>>            .

>>        END-OF-PROGRAM.
>>            CLOSE I00, I04, P07
>>            STOP RUN
>>            .

>[...]If ERROR-RTN always stops the processing, shouldn't it be
>accessed with a GO TO, so the reader knows it will never return?

This has merit, but the reader could also know the program will not
return by comments in the error procedure, or in the procedure name
(such as the FATAL-DUMP-AND-STOP, in this case).

>   At least the FATAL-DUMP-AND-STOP and END-OF-PROGRAM names make it clear
>there is no return. However, PERFORM still _implies_ a return.

Another thing to consider is the disposition of the aborted program.
If, for example, in the area indicated by * REMOVED SOME CODE FOR
BREVITY, a program dump is produced, the usability of the dump could
be affected.   In this instance, if the FATAL-DUMP-AND-STOP procedure
is PERFORMed, rather than accessed by GO TO, the stack information in
the dump may provide a clue as to where in the program the error
procedure was PERFORMed.  (There would be no such clue if the routine
was accessed via GO TO.)  This becomes particularly important if the
FATAL-DUMP-AND-STOP procedure could be PERFORMed from any of several
places.


Just my $0.02 (speaking as someone who occasionally must use such
techniques in program failure analysis).
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 4)_

- **From:** Jeff York <jeff@jakfield.xu-netx.com>
- **Date:** 2000-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j04ousocivf145mb1rhos9ponrtu57l7ia@4ax.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39e64428.7836029@news1.frb.gov>`

```
WDS@WDS.WDS.5 (WDS) wrote:

>On Fri, 06 Oct 2000 22:45:43 GMT, William Bub wrote:
>
…[32 more quoted lines elided]…
>places.

I must admit that I don't like the idea of PERFORMING a procedure that
has no return..  Old habits die hard I suppose and as an assembler
programmer I was taught that "the stack is like a bathroom..  Please
leave it in the same condition as you entered it.."..   :-)
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QVYG5.7210$Fe4.142306@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39e64428.7836029@news1.frb.gov> <j04ousocivf145mb1rhos9ponrtu57l7ia@4ax.com>`

```
If you PERFORM something, then inside the PERFORM make
a GO TO, what does that correspond to in your bathroom
analogy? Even a STOP RUN is at some lower level a call
with no return. GO TO DUMP is just as 'damaging' to the
stack (if there is one - not all compilers generate stack
oriented code). But as I've said before, if you MUST have
a GO TO instead of PERFORM DUMP, then do so.
That was not the main point of the original exercise
(which seems to have been forgotten as the thread
degenerated into the 10 millionth GO TO debate).


Jeff York <jeff@jakfield.xu-netx.com> wrote in message
news:j04ousocivf145mb1rhos9ponrtu57l7ia@4ax.com...
> WDS@WDS.WDS.5 (WDS) wrote:
>
…[22 more quoted lines elided]…
> >>   At least the FATAL-DUMP-AND-STOP and END-OF-PROGRAM names make it
clear
> >>there is no return. However, PERFORM still _implies_ a return.
> >
…[18 more quoted lines elided]…
> jeff@jakfield.xu-netx.com  (remove the x..x round u-net for return
address)
>
> ... "There are few hours in life more agreeable
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 6)_

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39f0b68d.3288363@news1.frb.gov>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39e64428.7836029@news1.frb.gov> <j04ousocivf145mb1rhos9ponrtu57l7ia@4ax.com> <QVYG5.7210$Fe4.142306@typhoon.austin.rr.com>`

```
On Tue, 17 Oct 2000 13:58:08 GMT, "Leif Svalgaard" <leif@leif.org>
wrote:

>If you PERFORM something, then inside the PERFORM make
>a GO TO, what does that correspond to in your bathroom
>analogy? 

If that is done in a loop, then this could correspond to an
overflowing toilet.
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ELgI5.13850$P14.327941@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39e64428.7836029@news1.frb.gov> <j04ousocivf145mb1rhos9ponrtu57l7ia@4ax.com> <QVYG5.7210$Fe4.142306@typhoon.austin.rr.com> <39f0b68d.3288363@news1.frb.gov>`

```

WDS <WDS@WDS.WDS.5> wrote
> On Tue, 17 Oct 2000 13:58:08 GMT, "Leif Svalgaard" <leif@leif.org>

> >If you PERFORM something, then inside the PERFORM make
> >a GO TO, what does that correspond to in your bathroom
…[4 more quoted lines elided]…
>

people do it all the time:

PERFORM READ-NEXT-RECORD
...
READ-NEXT-RECORD.
     READ file
         AT-END GO TO EOF
    ...


But you are correct, it is bad style.
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 4)_

- **From:** "mangogwr" <mangogrower@telocity.co>
- **Date:** 2000-10-29T13:31:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l6_K5.24810$Q8.5289888@newsrump.sjc.telocity.net>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39e64428.7836029@news1.frb.gov>`

```
well, the fact is (IMNSHO), if your code is about to transfer control to a
routine that
STOPS all processing prematurely, then it is YOUR responsibility to setup
whatever
indicators / values to describe the error condition BEFORE transferring
control.

To do otherwise is futile, wasteful and unprofessional.

WDS <WDS@WDS.WDS.5> wrote in message news:39e64428.7836029@news1.frb.gov...
> On Fri, 06 Oct 2000 22:45:43 GMT, William Bub wrote:
>
…[20 more quoted lines elided]…
> >   At least the FATAL-DUMP-AND-STOP and END-OF-PROGRAM names make it
clear
> >there is no return. However, PERFORM still _implies_ a return.
>
…[17 more quoted lines elided]…
> -------------------Decoy@Spammer.Trasher----------------
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-10-29T15:21:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ti0to$qle$1@news.igs.net>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <rCsD5.37693$355.5232822@typhoon.nyroc.rr.com> <39e64428.7836029@news1.frb.gov> <l6_K5.24810$Q8.5289888@newsrump.sjc.telocity.net>`

```
My current abort method prints the name and version of the module
that it is in, the date compiled, and the file name of the source code
module.  All those are set by each module before they can access
system parameters.  To do otherwise forces and immediate invocation
of the module containing the code, and that is then debugged first.

There is only one "stop" in the entire code, and that is also in the abort
method.  Whether or not it is a normal or abnormal exit is determined
by presetting a flag in the system object to allow a normal exit.

mangogwr wrote in message ...
>well, the fact is (IMNSHO), if your code is about to transfer control to a
>routine that
…[53 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Show me your code...

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-07T03:42:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qWwD5.11216$Ly1.156202@news5.giganews.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com>`

```
Excellent.  I noticed your handling of the SEARCH-FOR-LTR - I came up with
the same answer... You want to end up with 1 if nothing is found?  Start at
26 and work backward.

By the way, the LTR is 26 bytes long (obviously) containing ABCDEF... you
get the idea.

Cliff
```

###### ↳ ↳ ↳ Re: Show me your code...

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52ED5.43964$3y3.820966@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <qWwD5.11216$Ly1.156202@news5.giganews.com>`

```

Cliff Peterson <cliff.peterson@spamcop.net> wrote in message
news:qWwD5.11216$Ly1.156202@news5.giganews.com...
> Excellent.  I noticed your handling of the SEARCH-FOR-LTR - I came up with
> the same answer... You want to end up with 1 if nothing is found?  Start
at
> 26 and work backward.
>
> By the way, the LTR is 26 bytes long (obviously) containing ABCDEF... you
> get the idea.


what I do not get is why you do the final compute:
LTR-NDX = 27 - LTR-NDX
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 4)_

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LsKD5.14092$Ly1.198061@news5.giganews.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <qWwD5.11216$Ly1.156202@news5.giganews.com> <52ED5.43964$3y3.820966@typhoon.austin.rr.com>`

```

On  7-Oct-2000, "Leif Svalgaard" <leif@leif.org> wrote:

> what I do not get is why you do the final compute:
> LTR-NDX = 27 - LTR-NDX

----------------------------------
From the original code:

 MOVE REC-ID-I04-P TO LTR-HOLD.
 PERFORM SEARCH-FOR-LTR THRU SEARCH-FOR-LTR-EXIT.
 MOVE LTR (LTR-NDX) TO REC-ID-I04-P.
 IF REC-ID-I04-P IS NOT EQUAL TO 'P'
     GO TO READ-I04.
---------------------------------

They search LTR-HOLD's position in LTR, then turn it around.  If it's 1 it
becomes 26, if it's 26 it becomes 1.
Since LTR contains 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', A becomes Z, B becomes Y,
etc.  Their desired outcome is "P", the 16th letter, so LTR has to
originally contain K, the 11th letter.  27-11=16, or "P".

All I can figure is that the vendor developed a "trick" to decode
REC-ID-104-P, or they came up with the "P".  It was named the "P" record in
their documentation, perhaps, but contains a "K" in the record ID.

Maybe it's code.  Maybe it's a trademark doo-da.  Pretty strange.  It could
have been eliminated and check for "K".

Cliff
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LLKD5.44266$3y3.838858@typhoon.austin.rr.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <qWwD5.11216$Ly1.156202@news5.giganews.com> <52ED5.43964$3y3.820966@typhoon.austin.rr.com> <LsKD5.14092$Ly1.198061@news5.giganews.com>`

```
jeez.

Cliff Peterson <cliff.peterson@spamcop.net> wrote in message
news:LsKD5.14092$Ly1.198061@news5.giganews.com...
>
> On  7-Oct-2000, "Leif Svalgaard" <leif@leif.org> wrote:
…[21 more quoted lines elided]…
> REC-ID-104-P, or they came up with the "P".  It was named the "P" record
in
> their documentation, perhaps, but contains a "K" in the record ID.
>
> Maybe it's code.  Maybe it's a trademark doo-da.  Pretty strange.  It
could
> have been eliminated and check for "K".
>
> Cliff
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 6)_

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jDLD5.13622$bI6.642668@news1.giganews.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <GclD5.26421$WK6.599529@typhoon.austin.rr.com> <qWwD5.11216$Ly1.156202@news5.giganews.com> <52ED5.43964$3y3.820966@typhoon.austin.rr.com> <LsKD5.14092$Ly1.198061@news5.giganews.com> <LLKD5.44266$3y3.838858@typhoon.austin.rr.com>`

```

On  7-Oct-2000, "Leif Svalgaard" <leif@leif.org> wrote:

> jeez.

Real world... :-)

Some of the code I run across was written in the 60s and modified 100 times.
 Weird stuff.

Cliff
```

#### ↳ Re: Show me your code...

- **From:** "pwmeister" <pwm@nomail.se>
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rjuuf$emg$1@news1.enator.se>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com>`

```
If this program has run error free since 1993, there is
no point in rewriting it (although this is a very small program
and could be rewritten in a couple of hours).

Peter Meister

Cliff Peterson wrote in message
>Anyone interested in showing their coding style?
>
…[5 more quoted lines elided]…
>Cliff
```

##### ↳ ↳ Re: Show me your code...

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jhD5.13219$l35.199742@iad-read.news.verio.net>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <8rjuuf$emg$1@news1.enator.se>`

```
In article <8rjuuf$emg$1@news1.enator.se>, pwmeister <pwm@nomail.se> wrote:
>If this program has run error free since 1993, there is
>no point in rewriting it (although this is a very small program
>and could be rewritten in a couple of hours).

With all due respect, Mr Meiste, I believe the point was *not* about the
code's need, or lack thereof, to be rewritten, but what kind of code -
fresh, new, shiny, clean code, code developed by a Respected Vendor and
supplied rather recently. code that isn't even old enough to vote! - can
be found in systems where the New Programmers might be working.

DD
```

###### ↳ ↳ ↳ Re: Show me your code...

- **From:** "pwmeister" <pwm@nomail.se>
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rkksf$lsn$1@news1.enator.se>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <8rjuuf$emg$1@news1.enator.se> <9jhD5.13219$l35.199742@iad-read.news.verio.net>`

```
Sorry. I didn't read the post that carefully and misinterpreted it (English
not my
first or second language). My initial thougt was here comes another post on
GO TO
and/or structured programming and how and when a program should be
rewritten.
Hm. [reading the post again - looking at the code again].
Yes. Merge - homework. Should have been more structured if programmed
in 1993.
Btw what is the definition on 'New Programmer' and in what way does it
differ from 'Old Programmer' especially in coding techniques?
P Meister

NA wrote in message <9jhD5.13219$l35.199742@iad-read.news.verio.net>...
>In article <8rjuuf$emg$1@news1.enator.se>, pwmeister <pwm@nomail.se> wrote:
>>If this program has run error free since 1993, there is
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Show me your code...

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0rlD5.13258$l35.200522@iad-read.news.verio.net>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com> <8rjuuf$emg$1@news1.enator.se> <9jhD5.13219$l35.199742@iad-read.news.verio.net> <8rkksf$lsn$1@news1.enator.se>`

```
In article <8rkksf$lsn$1@news1.enator.se>, pwmeister <pwm@nomail.se> wrote:
>Sorry. I didn't read the post that carefully and misinterpreted it (English
>not my
…[3 more quoted lines elided]…
>rewritten.

Not to worry... glad that was clarified.

>Hm. [reading the post again - looking at the code again].
>Yes. Merge - homework. Should have been more structured if programmed
>in 1993.
>Btw what is the definition on 'New Programmer' and in what way does it
>differ from 'Old Programmer' especially in coding techniques?

I cannot speak for anyone but myself, Mr Meister, but I'd imagine that
someone trained under COBOL74 would code a bit differently than someone
trained under COBOL85... for example, it seems to me that, as of late
('late' being defined as after 1983) there is more encouragement of the
'one period/full stop per paragraph' school.

DD

>NA wrote in message <9jhD5.13219$l35.199742@iad-read.news.verio.net>...
>>In article <8rjuuf$emg$1@news1.enator.se>, pwmeister <pwm@nomail.se> wrote:
…[13 more quoted lines elided]…
>
```

#### ↳ Re: Show me your code...

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-10-07T03:30:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sNwD5.11339$bI6.544780@news1.giganews.com>`
- **References:** `<%W9D5.7211$Ly1.83712@news5.giganews.com>`

```
      ***********************************************
      * I'M ASSUMING THESE "FILE STATUS" FIELDS, BUT
      * DIDN'T ADD FILE STATUS CHECKING TO THE CODE.
      ***********************************************
       01  FILE-STATUS-FIELDS.
           05  I00-STATUS   PIC 99.
               88  I00-STATUS-OK        VALUE 00.
           05  I04-STATUS   PIC 99.
               88  I04-STATUS-OK        VALUE 00 10.
               88  I04-STATUS-EOF       VALUE 10.
           05  P07-STATUS   PIC 99.
               88  P07-STATUS-OK        VALUE 00 10.
               88  P07-STATUS-EOF       VALUE 10.
*************************************************************
       PROCEDURE DIVISION.
           OPEN INPUT  I04.
           OPEN INPUT  P07.
           OPEN OUTPUT I00.

           PERFORM READ-I04.
           PERFORM READ-P07.
           PERFORM UNTIL KEY-I04 = 99999 AND KEY-P07 = 99999
               EVALUATE TRUE
               WHEN KEY-I04 = KEY-P07
                   IF PROJ-LEVEL-I04-P NOT > SAVE-PROJ-LEVEL
                       PERFORM WRITE-I00
                   END-IF
                   MOVE PROJ-LEVEL-I04-P TO SAVE-PROJ-LEVEL
                   MOVE EDP-SEQ-NO-I04-P TO SAVE-EDP-SEQ-NO
                   MOVE PROJ-ID-I04-P    TO SAVE-PROJ-ID
                   PERFORM READ-I04
               WHEN KEY-I04 > KEY-P07
                   IF PROJ-LEVEL-P07-P NOT > SAVE-PROJ-LEVEL
                       PERFORM WRITE-I00
                   END-IF
                   MOVE PROJ-LEVEL-P07-P TO SAVE-PROJ-LEVEL
                   MOVE EDP-SEQ-NO-P07-P TO SAVE-EDP-SEQ-NO
                   MOVE PROJ-ID-P07-P    TO SAVE-PROJ-ID
               WHEN OTHER
                   MOVE 1 TO DUMP-CODE
                   PERFORM DUMP-AND-END
               END-EVALUATE
               PERFORM READ-P07
           END-PERFORM.
           PERFORM WRITE-I00.
           PERFORM END-OF-PROGRAM.

       READ-I04.
           MOVE ZEROES TO KEY-I04.
           PERFORM UNTIL KEY-I04 > ZERO
               READ I04
               EVALUATE TRUE
               WHEN I04-STATUS-EOF
                   MOVE 99999 TO KEY-I04
               WHEN SYS-ID-I04-P NOT = 'EOF'
                   PERFORM VARYING LTR-NDX FROM 26 BY -1
                       UNTIL REC-ID-I04-P = LTR (LTR-NDX)
                          OR LTR-NDX  = 1
                   END-PERFORM
                   COMPUTE LTR-NDX = 27 - LTR-NDX
                   MOVE LTR (LTR-NDX) TO REC-ID-I04-P
                   IF REC-ID-I04-P      = 'P' AND
                      DELETED-I04-P NOT = 'Y'
                       MOVE EDP-SEQ-NO-I04-P TO KEY-I04
                   END-IF
               END-EVALUATE
           END-PERFORM.

       READ-P07.
           MOVE ZEROES TO KEY-P07.
           PERFORM UNTIL KEY-P07 > ZERO
               READ P07
               EVALUATE TRUE
               WHEN P07-STATUS-EOF
                   MOVE 99999 TO KEY-P07
               WHEN REC-ID-P07-P = 'P'
                   IF DELETED-P07-P    NOT = 'Y' AND
                      EDP-SEQ-NO-P07-P NOT = 1
                       MOVE EDP-SEQ-NO-P07-P TO KEY-P07
                   END-IF
               END-EVALUATE
           END-PERFORM.

       WRITE-I00.
           INITIALIZE I00-P.
           MOVE 'DCI'           TO SYS-ID-I00-P.
           MOVE 'I00'           TO FILEID-I00-P.
           MOVE 'P'             TO REC-ID-I00-P.
           MOVE SAVE-EDP-SEQ-NO TO EDP-SEQ-NO-I00-P.
           MOVE SAVE-PROJ-ID    TO PROJ-ID-I00-P.
           WRITE I00-REC FROM I00-P.
           IF NOT I00-STATUS-OK
               MOVE I00-STATUS TO DUMP-STATUS
               MOVE 'STATUS RETURN FROM WRITE' TO DUMP-TEXT2
               MOVE 2 TO DUMP-CODE
               PERFORM DUMP-AND-END
           END-IF.

       DUMP-AND-END.
      * REMOVED THIS CODE FOR BREVITY
           PERFORM END-OF-PROGRAM.

       END-OF-PROGRAM.
           CLOSE I00
                 I04
                 P07.
           STOP RUN.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
