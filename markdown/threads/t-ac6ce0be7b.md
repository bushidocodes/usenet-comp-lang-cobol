[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fun with CA-Realia COBOL: Recursive PERFORMs

_1 message · 1 participant · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fun with CA-Realia COBOL: Recursive PERFORMs

- **From:** Jeffrey Friedman <jfriedm@ibm.net>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369031D0.718CA028@ibm.net>`

```
CA-Realia has a compile directive which instructs the compiler to
generate CALL and RET instructions for PERFORM and perform EXIT (the
CALL directive).  While this could lead to non-standard (and quite
non-portable) code if abused, it is a perfectly acceptable
implementation for compliant code which also happens to obey the
constraint that a perform exit point is always an exit point (PERFORM A
THRU B and PERFORM A THRU C would not work with this directive in place,
as there would be a RET instruction generated at the end of paragraph
B). What I demonstrate here is a side benefit (or detriment depending on
your way of thought) in that programs "get away" with recursive PERFORMs
(as they nicely stack their exit points). Here is an example I had
written a while back to demonstrate this, and solve the Knight's Tour
problem.  Note that this program uses the SMALLCOMP directive (which
allocates a single byte to a binary number if the precision is small
enough), and it uses the ANSI escape sequences to interact with the
screen (ANSI.SYS should be loaded in CONFIG.SYS), and is obviously not
an GUI program so run it at a DOS prompt. It should also be cut and
pasted to a file with a .CBL extension as columns 1-6 are not present
(or set COBEXT to that extension with the /r option).  Have Fun!

Jeff Friedman, Developer
CA-Realia COBOL

*$CALL,SMALLCOMP
 IDENTIFICATION DIVISION.
 PROGRAM-ID. KTOUR.
*
*    This program does an entire knight's tour on the screen
*    (if you have the time to watch).
*
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 SOURCE-COMPUTER. IBM-PC.
 OBJECT-COMPUTER. IBM-PC.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01  MISC-STACK-AREAS.
     05 DEPTH                 VALUE 1          PIC S9(2) COMP-5.
     05 DEPTH-FORMATTED-X.
         10 DEPTH-FORMATTED                    PIC 99.
     05 NEW-POSITION                           PIC S9(2) COMP-5.
     05 CURRENT-POSITION      VALUE 22         PIC S9(2) COMP-5.
     05 CURRENT-POSITION-STACK OCCURS 65       PIC S9(2) COMP-5.
*
*    Board is 12 wide by 10 high for convienience
*
 01 BOARD-AREA.
     05  BOARD OCCURS 120 TIMES INDEXED BY BX PIC S9(2) COMP-5.
 01 FILLER REDEFINES BOARD-AREA.
     05  FILLER PIC X(21).
     05  BOARD-LINES-GRP OCCURS 8 TIMES.
         10  BOARD-LINE PIC X(8).
         10  FILLER     PIC XX.
*
 01 MISC-AREAS.
     05  MOVE-NO  OCCURS 65 TIMES          PIC S9(2) COMP-5.
 01  OPEN-SQ-AREAS.
     05  OPEN-SQ-PTR                       PIC S9(4) COMP-5.
     05  FILLER REDEFINES OPEN-SQ-PTR.
         10  OPEN-SQ-PTR-LSB               PIC S9(2) COMP-5.
         10  OPEN-SQ-PTR-MSB               PIC S9(2) COMP-5.
     05  SAVE-SQUARE                       PIC S9(2) COMP-5.
     05  OPEN-SQUARE      OCCURS 64 TIMES  INDEXED BY OIX
                                           PIC S9(2) COMP-5.
*
 01 MOVE-TYPE-DEFINITIONS.
     05  FILLER VALUE +08                  PIC S9(2) COMP-5.
     05  FILLER VALUE -21                  PIC S9(2) COMP-5.
     05  FILLER VALUE +21                  PIC S9(2) COMP-5.
     05  FILLER VALUE +12                  PIC S9(2) COMP-5.
     05  FILLER VALUE -19                  PIC S9(2) COMP-5.
     05  FILLER VALUE +19                  PIC S9(2) COMP-5.
     05  FILLER VALUE -12                  PIC S9(2) COMP-5.
     05  FILLER VALUE -08                  PIC S9(2) COMP-5.
 01  FILLER REDEFINES MOVE-TYPE-DEFINITIONS.
     05  MOVE-OFFSET OCCURS 8 TIMES INDEXED BY MOVE-TYPE
                                           PIC S9(2) COMP-5.
*
 01  POSSIBLE-FLAG          VALUE 'y'      PIC X.
     88  WIN-POSSIBLE   VALUE 'y'.
     88  WIN-IMPOSSIBLE VALUE 't'.
*
 01  WS-ROW                                PIC S9(2) COMP-5.
 01  WS-COLUMN                             PIC S9(2) COMP-5.
 01  LAST-RECURSE-DEPTH VALUE 65           PIC S9(2) COMP-5.
 01  COUNT-REACHABLE-FROM-1                PIC S9(2) COMP-5.
 01  REACHABLE-FROM-COUNT                  PIC S9(2) COMP-5.
 01  WIN-COUNT                             PIC S9(9) COMP-5.
 01  CTRL-BRK-FLAG VALUE LOW-VALUES        PIC X.
 01  WS-START-TIME.
     05  ST-HH                             PIC 99.
     05  ST-MM                             PIC 99.
     05  ST-SS                             PIC 99V99.
 01  WS-CURRENT-TIME.
     05  CT-HH                             PIC 99.
     05  CT-MM                             PIC 99.
     05  CT-SS                             PIC 99V99.
 01  START-DELAY-TIME.
     05  SD-HH                             PIC 99.
     05  SD-MM                             PIC 99.
     05  SD-SS                             PIC 99V99.
 01  END-DELAY-TIME.
     05  ED-HH                             PIC 99.
     05  ED-MM                             PIC 99.
     05  ED-SS                             PIC 99V99.
 01  TIME-PER-SOLUTION                     PIC 999.9(5).
 01  DELAY-TIME                            PIC S9(4)V99 COMP-5.
*
 01  WS-POSITION-CURSOR.
     05  FILLER                            PIC X VALUE X'1B'.
     05  FILLER                            PIC X VALUE '['.
     05  WS-POS-ROW                        PIC 99.
     05  FILLER                            PIC X VALUE ';'.
     05  WS-POS-COL                        PIC 99.
     05  FILLER                            PIC X VALUE 'f'.
*
 01  WS-BOARD.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(3) VALUE '[2J'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[3;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[4;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[5;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[6;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[7;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[8;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(5) VALUE '[9;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[10;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[11;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[12;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[13;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[14;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[15;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[16;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[17;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[18;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL 'I    '.
     05  FILLER PIC X VALUE X'1B'.
     05  FILLER PIC X(6) VALUE '[19;10'.
     05  FILLER PIC X VALUE 'f'.
     05  FILLER PIC X(41) VALUE ALL '-'.
*
 PROCEDURE DIVISION.
 B000-INITIALIZATION.
*
*    The basic loop is display a move, try another, backup
*    when completed or stuck.
*    First display the board outline and initialize areas.
*    Note that the board is 8X8 but inside of a 12X10 grid.
*    This way no need to test if a move takes knight off the
*    board: just mark these positions as already used. First
*    mark top and bottom as in-use (non-zero), then mark sides.
*
     PERFORM VARYING BX FROM 1 BY 1 UNTIL BX IS GREATER THAN 21
         MOVE 65 TO BOARD (BX)
     END-PERFORM.
     PERFORM VARYING BX FROM 120 BY -1 UNTIL BX IS LESS THAN 100
         MOVE 65 TO BOARD (BX)
     END-PERFORM.
     MOVE 65 TO BOARD (20) BOARD (21)
                BOARD (30) BOARD (31)
                BOARD (40) BOARD (41)
                BOARD (50) BOARD (51)
                BOARD (60) BOARD (61)
                BOARD (70) BOARD (71)
                BOARD (80) BOARD (81)
                BOARD (90) BOARD (91).
*
*    Maintain a table of open squares - points into BOARD
*
     MOVE 22 TO OPEN-SQ-PTR.
     SET OIX TO 1.
     PERFORM 8 TIMES
         PERFORM 8 TIMES
             MOVE OPEN-SQ-PTR-LSB TO OPEN-SQUARE (OIX)
             ADD 1 TO OPEN-SQ-PTR
             SET OIX UP BY 1
         END-PERFORM
         ADD 2 TO OPEN-SQ-PTR
     END-PERFORM.
     MOVE 2 TO OPEN-SQ-PTR.
*
*    Display the empty board
*
     DISPLAY WS-BOARD.
*
*    Make first move to upper left hand corner, display the
*    move, and start recursing.
*
     MOVE CURRENT-POSITION TO CURRENT-POSITION-STACK(1)
                              NEW-POSITION.
     MOVE 1 TO BOARD(CURRENT-POSITION) DEPTH-FORMATTED.
     PERFORM B200-DISPLAY-MOVE.
*
 B100-MAKE-MOVE.
*
*    See if the board configuration is already unwinnable.
*    If so, just back up and try other moves, else try all
*    possible moves from this arrangement.
*
     PERFORM B300-CHECK-FOR-IMPOSSIBLE THRU B300-EXIT.
     IF WIN-POSSIBLE
       PERFORM VARYING MOVE-NO(DEPTH) FROM 1 BY 1
               UNTIL MOVE-NO(DEPTH) IS GREATER THAN 8
         SET MOVE-TYPE TO MOVE-NO(DEPTH)
         ADD CURRENT-POSITION
             MOVE-OFFSET (MOVE-TYPE)
             GIVING NEW-POSITION
         IF BOARD (NEW-POSITION) IS EQUAL TO ZERO
             ADD 1 TO DEPTH
             MOVE DEPTH TO BOARD (NEW-POSITION)
                           DEPTH-FORMATTED
             PERFORM B200-DISPLAY-MOVE
*
*            If depth is 64, board filled, backup and keep
*            searching for other solutions
*
             IF DEPTH IS EQUAL TO 64
                 PERFORM B400-RECORD-WIN
                 MOVE ZERO TO BOARD(NEW-POSITION)
                 MOVE SPACE TO DEPTH-FORMATTED-X
                 PERFORM B200-DISPLAY-MOVE
                 SUBTRACT 1 FROM DEPTH
             ELSE
*
*                Need to try subsequent moves from here
*                Mark square no longer open, and recurse
*                Note: recursive PERFORM requires CALL
*                directive to work properly.
*
                 PERFORM B300-OPEN-SQ-MAINT
                 MOVE NEW-POSITION TO CURRENT-POSITION
                                     CURRENT-POSITION-STACK(DEPTH)
                 PERFORM B100-MAKE-MOVE
             END-IF
         END-IF
       END-PERFORM.
*
*    Have tried all possible moves or current configuration
*    is unwinnable. Back up a move and try other moves.
*
     MOVE CURRENT-POSITION-STACK (DEPTH) TO NEW-POSITION.
     MOVE ZERO TO BOARD(NEW-POSITION).
     MOVE SPACE TO DEPTH-FORMATTED-X.
     PERFORM B200-DISPLAY-MOVE
     SUBTRACT 1 FROM DEPTH
                     OPEN-SQ-PTR.
     MOVE CURRENT-POSITION-STACK (DEPTH) TO CURRENT-POSITION.
*
 B100-END.  EXIT.
*
*    It will take quite a while, but when entire tree is traversed
*    - fall through and stop.
*
     STOP RUN.
*
*    Come here to display current move (or clean last move)
*
 B200-DISPLAY-MOVE.
*
     DIVIDE NEW-POSITION BY 10
         GIVING WS-ROW REMAINDER WS-COLUMN.
     MULTIPLY WS-ROW BY 2 GIVING WS-POS-ROW.
     MULTIPLY WS-COLUMN BY 5 GIVING WS-POS-COL
     ADD 2 TO WS-POS-COL.
     DISPLAY WS-POSITION-CURSOR DEPTH-FORMATTED-X
         WITH NO ADVANCING.
*
*    If any open square cannot be reached, impossible to win
*    Also, if more than 1 square which can only be reached
*    from one other square, then cannot win. A square cannot
*    be reached if all square around it are used (and none
*    are the current position); same for other optimization.
*
 B300-CHECK-FOR-IMPOSSIBLE.
*
     SET WIN-POSSIBLE TO TRUE.
*
*    If almost done, just try combinations - faster than
*    checking if impossible win. 57 is a guess at probable
*    break-even point.
*
     IF DEPTH IS GREATER THAN 57
         GO TO B300-EXIT.
*
*    Temporarily zero the current square so looks reachable
*    and zero count of squares reachable from only one other
*    square.
*
     MOVE ZERO TO BOARD (CURRENT-POSITION)
                  COUNT-REACHABLE-FROM-1.
*
*    Only test squares listed as open in the OPEN-SQUARE table
*
     PERFORM VARYING OIX FROM OPEN-SQ-PTR BY 1
             UNTIL OIX IS GREATER THAN 64
         SET BX TO OPEN-SQUARE (OIX)
         MOVE ZERO TO REACHABLE-FROM-COUNT
*
*        Count number of square this square is
*        is reachable from.
*
         IF BOARD (BX - 12) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX - 08) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX + 08) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX + 12) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX - 19) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX - 21) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX + 21) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
         IF BOARD (BX + 19) EQUAL ZERO
             ADD 1 TO REACHABLE-FROM-COUNT
         END-IF
*
         IF REACHABLE-FROM-COUNT IS EQUAL TO ZERO
             SET WIN-IMPOSSIBLE TO TRUE
             GO TO B300-EXIT-WITH-RESTORE
         END-IF
*
*        If this square is reachable from only 1 square
*        and already found another square only reachable
*        from one square, win is impossible.
*        Cannot do test when depth is greater than 62 as
*        there WILL only be if winning position.
*
         IF REACHABLE-FROM-COUNT IS EQUAL TO 1
             IF COUNT-REACHABLE-FROM-1 IS EQUAL TO 1
                 SET WIN-IMPOSSIBLE TO TRUE
                 GO TO B300-EXIT-WITH-RESTORE
             ELSE
                 MOVE 1 TO COUNT-REACHABLE-FROM-1
             END-IF
         END-IF
     END-PERFORM.
*
*    Must restore depth to current position before leaving.
*
 B300-EXIT-WITH-RESTORE.
*
     MOVE DEPTH TO BOARD (CURRENT-POSITION).
*
 B300-EXIT.  EXIT.
*
*    Come here to maintain list of open squares.
*
 B300-OPEN-SQ-MAINT.
*
     SET OIX TO OPEN-SQ-PTR.
     MOVE OPEN-SQUARE (OIX) TO SAVE-SQUARE.
     SEARCH OPEN-SQUARE VARYING OIX
         AT END
             DISPLAY 'Impossible NF during open sq maint'
             STOP RUN
         WHEN OPEN-SQUARE (OIX) IS EQUAL TO NEW-POSITION
             MOVE NEW-POSITION TO OPEN-SQUARE (OPEN-SQ-PTR)
             MOVE SAVE-SQUARE TO OPEN-SQUARE (OIX)
             ADD 1 TO OPEN-SQ-PTR
     END-SEARCH.
*
*    Come here to display the number of solutions found
*    so far.
*
 B400-RECORD-WIN.
*
     ADD 1 TO WIN-COUNT.
     DISPLAY X'1B' '[24;5f' 'Solutions:' WIN-COUNT
         WITH NO ADVANCING.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
