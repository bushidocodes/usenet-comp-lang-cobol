[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Beginner

_1 message · 1 participant · 2006-02_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### COBOL Beginner

- **From:** "rohit" <rohit1712@gmail.com>
- **Date:** 2006-02-13T20:55:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139892938.003194.301180@g14g2000cwa.googlegroups.com>`

```
Working on Fujitsu COBOL85 V30L10.
Book: Teach Yourself COBOL in 21 Days.
Listing 9.5 Creating a file and adding records.

While working with examples after compiling and executing them I am
facing a peculiar problem. A sample of the program:

002100 01  PHONE-RECORD.
002200     05  PHONE-LAST-NAME      PIC X(20).
002300     05  PHONE-FIRST-NAME     PIC X(20).
002400     05  PHONE-NUMBER         PIC X(15).
002500     05  PHONE-EXTENSION      PIC X(5).
............................
.............................
...........................
006700     MOVE SPACE TO PHONE-RECORD.
006800     DISPLAY PROMPT-1 " ? ".
006900     ACCEPT PHONE-LAST-NAME.
007000     DISPLAY PROMPT-2 " ? ".
007100     ACCEPT PHONE-FIRST-NAME.
007200     DISPLAY PROMPT-3 " ? ".
007300     ACCEPT PHONE-NUMBER.
007400     DISPLAY PROMPT-4 " ? ".
007500     ACCEPT PHONE-EXTENSION.
007600     PERFORM VALIDATE-FIELDS.

Analysis:
At line 002100 the record name is defined with the size of the data to
be contained in it.
At line 006700 the said record is initialized with SPACE.
At line 006900 the user is asked to enter data in the field whose data
length is "20"

Problem:
When the above program is executed the user enters a value of length 6
(i.e. PHONE-LAST-NAME = GATES) But the program will not proceed to the
next field (In this case: PHONE-FIRST-NAME) until the former field is
filled with the entire length as defined in the structure i.e. "20" .
So the user is forced to fill the former field (i.e. PHONE-LAST-NAME)
with GATESSPACESSPACESSPACES................................ and press
enter to jump to the next field. What lines are to be added to the
program so that it moves to the next field after accepting the
PHONE-LAST-NAME Value regardless of the length of the data.

Please help....
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
