[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call wordpad from mf cobol v3,2

_4 messages · 4 participants · 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Call wordpad from mf cobol v3,2

- **From:** "Massimo Morgia" <areasoftware@tiscalinet.it>
- **Date:** 1999-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ji9pq$22a$1@aquila.tiscalinet.it>`

```
I want to call wordpad of w98/95 from a pgm write in microfocus cbl v 3,2

Tanks Massimo Morgia From Rome
```

#### ↳ Re: Call wordpad from mf cobol v3,2

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Bqd4dmSdzlFF@Dwight_Miller.iix.com>`
- **References:** `<7ji9pq$22a$1@aquila.tiscalinet.it>`

```
On Tue, 8 Jun 1999 05:28:04, "Massimo Morgia" 
<areasoftware@tiscalinet.it> wrote:

> I want to call wordpad of w98/95 from a pgm write in microfocus cbl v 3,2
> 
> Tanks Massimo Morgia From Rome
> 
> 

For that version a X"91" with X"35" call works pretty well.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Call wordpad from mf cobol v3,2

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Oea2Zios#GA.357@nih2naae.prod2.compuserve.com>`
- **References:** `<7ji9pq$22a$1@aquila.tiscalinet.it> <Jl0PnHJ5PvPd-pn2-Bqd4dmSdzlFF@Dwight_Miller.iix.com>`

```
    Here is a sample program.  Note that when calling a dos program,
it pauses and does not continue until the external program has exited.
When I tried it with WORDPAD however, the calling program continued running.
I suppose that the easy solution would be an accept after the external call.
This would
also allow the user to see that an error other than program not found
existed.

    If you want a blank command prompt, you must specify "COMMAND".


000100 WORKING-STORAGE SECTION.
000200
000300 01  FUNCTION-X          PIC X VALUE X"91".
000400 01  RESULT              PIC 99 COMP         VALUE ZERO.
000500 01  CALL-PGM            PIC 99 COMP         VALUE 35.
000600 01  SET-CMD-LINE        PIC 99 COMP         VALUE 2.
000700 01  PARAMETER.
000800     05  PARM-SIZE       PIC 99 COMP.
000900     05  PARM            PIC X.
001000
001100 PROCEDURE DIVISION.
001200 0100-MENU.
001300     DISPLAY SPACES AT 0101.
001400     DISPLAY "CALL WORDPAD" AT 0101.
001500     DISPLAY "WORDPAD"   UPON COMMAND-LINE.
001600
001700     MOVE ZERO       TO PARM-SIZE.
001800     MOVE SPACES     TO PARM.
001900     CALL FUNCTION-X USING RESULT CALL-PGM PARAMETER.
002000     IF RESULT NOT = ZERO
002100       DISPLAY "ERROR CALLING EXTERNAL PGM" AT 1001.
002200     DISPLAY "ALL DONE"   AT 1501.
002300 THE-END.
002400     STOP RUN.





Thane Hubbell wrote in message ...
>On Tue, 8 Jun 1999 05:28:04, "Massimo Morgia"
><areasoftware@tiscalinet.it> wrote:
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Call wordpad from mf cobol v3,2

- **From:** "Timothy Nicholson" <kf4rtx@nospam.arrl.net>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jpqe7$d5e$1@nntp8.atl.mindspring.net>`
- **References:** `<7ji9pq$22a$1@aquila.tiscalinet.it>`

```
Why not just call the SYSTEM routine with the command line?

01  WORDPAD-COMMAND.
       05  FILLER            PIC X(08)  VALUE "WORDPAD ".
       05  FILE-TO-EDIT PIC X(20) VALUE SPACES.
.
.
.
MOVE "MYFILE.TXT" TO FILE-TO-EDIT.
CALL "SYSTEM" USING WORDPAD-COMMAND.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
