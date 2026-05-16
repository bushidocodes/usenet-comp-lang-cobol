[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Test Before and Do While

_4 messages · 3 participants · 2001-02_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### Test Before and Do While

- **From:** Jim McNamara <mac3@slic.com>
- **Date:** 2001-02-07T23:35:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A824C27.5E65DA23@slic.com>`

```
Calvin Crumrine wrote:
> 
> Ummm, are you sure about that? Maybe it depends on what language you're using, but
>I don't see any necessary relationship between the difference between Do
>While/Do Until and the difference between testing at the beginning vs. the end of
>the loop. 

>If you test at the beginning of the loop then
>the While loop will not execute at all when the condition is false

Calvin-

  The following is taken verbatim from our text.
  ---------------------------------------------------------------
 

  The perform statement includes the Test Before and Test After
  phrases, corresponing to a do while and do until, respectively.
  Specification of test before tests the condition before perfoming
  the procedure, and corresponds to a do while.  Specification of
  Test After performs the procedure and then tests the condition,
  and corresponds to a do until. Omission of both test before and
  test after defaults to test before.
  ----------------------------------------------------------------
  Cobol from Micro to Mainframe
  3rd edition
  Robert Grauer, Carol Villar, Arthur Buss
  ISBN 0-13-085849-8
  page number 232

  some examples I made below... 
 WORKING-STORAGE SECTION.
 01 CONSTANTS.
    05    A                       PIC 9 VALUE 3.
    05    B                       PIC 9 VALUE 4.


 PROCEDURE DIVISION.
 GENERIC-PARAGRAPH.
   PERFORM WITH TEST BEFORE UNTIL A < B
    SUBTRACT 1 FROM A 
    DISPLAY 'IS ' A ' LESS THAN ' B ' ?'
    END-PERFORM.
    STOP RUN.

   Lets test it. Test Before tests the condition before executing
   statements. 3 is less than 4 is true and the statements aren't
   executed. If the above constant values are reversed, it loops
   twice until the condition is true (2 < 3).

   In paradox a while loop means repeats a sequence of statements
   as long as a specified condition is True.

while starts by evaluating the logical expression Condition. If
Condition is False,
 the Statements are not executed. If the value is True, the Statements
between the 
 Condition and endWhile are executed in sequence. 
 
        method pushButton(var eventInfo Event)
          while 4 < 3 
             msgstop ("Entered","Loop") {displays dialog box}
            {comment- while condition is false
              msgstop dialog not displayed} 
          endwhile
        endmethod

 Based on all this, I'm going to go out on a limb and say Test Before
does not 
correspond to a Do While in Cobol and the book is WRONG.  Calvin is
right and Meesha 
is probably confused.  Any comments or suggestions ???   
BTW I'm going into hiding if I'm wrong.
   
  Thanks
   jim
```

#### ↳ Re: Test Before and Do While

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2001-02-08T06:27:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A823C26.1C3F96D0@worldnet.att.net>`
- **References:** `<3A824C27.5E65DA23@slic.com>`

```
Jim McNamara wrote:
> (snip)
>  Based on all this, I'm going to go out on a limb and say Test Before
…[5 more quoted lines elided]…
> 

PERFORM UNTIL with TEST BEFORE (either explicitly or as the standard
default), is an initial test loop.  In that sense it is a DO WHILE
loop.  But the standard definition of a structured programming DO
WHILE loop is to execute the iteratated statements WHILE a condition
is true, and exit the loop when the condition is false.  

PERFORM UNTIL with TEST AFTER is a bottom-tested loop, and exits on a
true condition.  So TEST AFTER looks exactly like a structured DO
UNTIL.

The difference is that in COBOL the PERFORM UNTIL always exits on a
TRUE condition, whether it's an initial test loop or a bottom tested
loop.  Structured DO WHILE is an initial test loop that exits on a
FALSE condition.  Structured DO UNTIL is a bottom-tested loop that
exits on a TRUE condition.

COBOL's PERFORM UNTIL with TEST BEFORE is more like "DO WHILE
NOT(condition)".  I would accept it as a DO WHILE because it's easy to
invert TRUE and FALSE, and the most important consideration for me is
whether the exit test is first or last.   

The iterated statements in an initial test loop (DO WHILE) may be
bypassed completely because the exit condition is always tested
first.  The iterated statements in a bottom-tested loop (DO UNTIL)
will always be executed at least once, because the exit test is at the
end of the iterated statements.
```

##### ↳ ↳ Re: Test Before and Do While

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-02-08T08:42:56-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A82DAA0.972966F1@dced.state.ak.us>`
- **References:** `<3A824C27.5E65DA23@slic.com> <3A823C26.1C3F96D0@worldnet.att.net>`

```
Arnold Trembley wrote:

> Jim McNamara wrote:
> > (snip)
…[36 more quoted lines elided]…
> http://arnold.trembley.home.att.net/

Of interest to me is why you say that a DO WHILE loop is initial test & a
DO UNTIL loop is bottom test. WHILE & UNTIL don't relate to where the test
is performed. In fact in the languages I'm familiar with (that have both)
they're linguistically inverse. Your definition seems to make them
linguistically perverse. (Sorry-couldn't resist.)
```

###### ↳ ↳ ↳ Re: Test Before and Do While

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2001-02-09T06:53:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8393A6.15CC29C3@worldnet.att.net>`
- **References:** `<3A824C27.5E65DA23@slic.com> <3A823C26.1C3F96D0@worldnet.att.net> <3A82DAA0.972966F1@dced.state.ak.us>`

```
Calvin Crumrine wrote:
> (snip)
> Of interest to me is why you say that a DO WHILE loop is initial test & a
…[3 more quoted lines elided]…
> linguistically perverse. (Sorry-couldn't resist.)

I learned structured programming concepts in a flowcharting class back
in 1978.  We didn't write any programs in that class, we flowcharted
the solutions.  DO WHILE, when used in pseudocode or a flowchart for
design, was defined as an initial test loop with exit on a false
condition.  DO UNTIL was defined as a bottom tested loop with exit on
a true condition.  

DO WHILE and DO UNTIL are structured programming concepts, and don't
necessarily correspond to any specific programming language syntax.

I can't claim credit for these definitions, they probably belong to
Wirth or Knuth or some other big thinker.  So you don't need to
apologize to me!

With kindest regards,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
