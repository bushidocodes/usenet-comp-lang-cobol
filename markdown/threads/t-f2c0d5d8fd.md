[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Tips and Techniques

_26 messages · 10 participants · 2003-03 → 2003-05_

---

### COBOL Tips and Techniques

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-17T12:42:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E763341.30E6C603@attglobal.net>`

```
Thinking that perhaps I hadn't "used" CLC enough yet, I would like to
ask you for one more set of comments on the following document.  As
before, you should feel free to tell me whatever you like.  Also as
before, I thank you for your input!
/ / / / / / / /  Start of document: / / / / / / / /
Guidelines for Efficient Table Handling in COBOL Programs


1. This paper is strictly concerned with the use of the table handling
features
available in the COBOL language.  It does not attempt to talk about any
external table
related software packages or techniques.

2. Enterprise COBOL for z/OS and OS/390 and COBOL for OS/390 & VM
Programmers:
For COBOL for OS/390 & VM, the Language Reference (SC26-4769) no longer
shows table
handling language elements in a separate chapter.  Read the Programming
Guide
(SC26-4767) 'Chapter 4: Handling Tables'.  It discusses some new
features, including
the INITIALIZE verb (which a good program should never need to use) and
new rules for
the VALUE clause which can simplify initializing small tables.  This
discussion will
lead the programmer back to the appropriate language elements in the
Language
Reference manual.

3. OS/VS COBOL Programmers:

First, stop using this compiler!  It has been unsupported by IBM since
June 30, 1996.

Read IBM VS COBOL for OS/VS (order number GC26-3857), Part 5: Special
Features, Table
Handling.  This discussion of the language features involved with table
handling will
serve as a refresher course for some, or an introduction for others.  It
is about 23
pages.  Read IBM OS/VS COBOL Compiler and Library Programmer's Guide
(order
SC28-6483), Programming Techniques, Table Handling Considerations.  This
discussion
gives a few facts which make the importance of using indexing (as
opposed to
subscripting) clear.  It also contains some terrible examples which no
one should
follow; they use ALTER verbs and have no relationship to good structured
techniques.

4. Remember that COBOL can manage arrays of up to seven dimensions
(three for
OS/VS COBOL); i.e., multiple nested occurs clauses.  However, probably
95% of the
arrays actually coded in programs are one dimensional.  While
multi-dimensional
arrays would tend to present even greater potential performance
pitfalls, we will
discuss the most used type.  The programmer who does a good job with
'tables' (one
dimensional arrays) should be able to figure out how to work with more
complex
structures.

5. Defining and Loading One Dimensional Arrays or Tables:

a. If you know exactly how many items there are in a table, use the
OCCURS
clause without the DEPENDING option.  This is a relatively rare
situation, usually
occurring only when the table values are  predefined in the program
(such as error
messages, etc.).  Such tables are usually not referenced in a SEARCH,
but only by
the setting of an index.

b. For tables loaded from external sources, define the table using
OCCURS...DEPENDING, with appropriate KEY clauses and at least one INDEX
name.
Define the DEPENDING  'object' as usage BINARY, with a PIC S9(4) if the
number of
occurs is less than 32K, or S9(8) if greater.  Assign it a value of
zero.  Define
a 'table-limit' item the same way, with a value equal to the maximum
size of the
table.  While loading the table, check that the INDEX does not exceed
the
'table-limit'  (This sounds basic, but programs in production do
occasionally fail
due to having omitted this checking.)  Once the table load is completed,
set the
DEPENDING 'object' to the actual number of occurrences.  This is usually
done by:

SET 'index' DOWN BY 1,   SET 'object' TO 'index'.

If you want to do a really super job of table management, you might want
to output
a message when the load is complete showing the table size and actual
number of
entries.

c. In COBOL for OS/390 & VM, tables are limited to 16M (16,277,215)
bytes.  In
OS/VS COBOL, the limit is 128K (131071) bytes.  For OS/VS, if the table
data is too
large to fit the maximum size of an 01 item in Working-Storage, a
technique can be
employed to process a larger table.  This involves defining the 'start'
of the table
in the normal manner and defining FILLER after the table to allow for
overflow.  If
this technique is employed, keep the following in mind:

1) The 'start' of the table should be defined as having a number of
entries
which is an exact multiple of eight, so that the FILLER defined after
the table will
start exactly where the table ends.

2) The FILLER item(s), which are limited to 32767 bytes or less, also
should be
defined as being a multiple of eight bytes long.

3) Tables defined in this way cannot be searched using the SEARCH verb,
since
this verb uses the number of occurrences to limit its activity, and the
table is
actually larger.  In this case, the subroutine LOOKUP or other code
which can be given
a separate 'number of entries' must be used.

d. If overflow occurs, perform a procedure which reads the remaining
input records
and writes a message giving the actual size of the input file versus the
table limit.
(Note that this could be the same message you might have decided to put
out when the
table didn't overflow.)  This will simplify making a program correction
to increase
table size, and will save time in the middle of the night....

e. Sample definition for a "fixed" table:

            01  MESSAGE-ARRAY.
             05                   PIC X(60) VALUE
                'This is error message 01.'
             05                   PIC X(60) VALUE
                'This is error message 02.'
                ...
             05                   PIC X(60) VALUE
                'This is error message 99.'
            01  MESSAGE-TABLE     REDEFINES
                MESSAGE-ARRAY.
             05 MESSAGE-TEXT      PIC X(60)
                           OCCURS 99
                          INDEXED MSG-X.
Note that the word FILLER was omitted from the definition of each
message entry.  In
OS/VS COBOL, the word must be supplied.

f. Sample definition for a "loaded" table:
            01  SOURCE-CODE-LIMIT PIC S9(4) BINARY VALUE +4096.
            01  SOURCE-CODE-SIZE  PIC S9(4) BINARY VALUE ZERO.
            01  SOURCE-CODE-TABLE.
             05 SOURCE-CODE-ENTRY
                           OCCURS 1 TO 4096
                        DEPENDING SOURCE-CODE-SIZE
                        ASCENDING SOURCE-CODE
                          INDEXED SC-X.
             10 SOURCE-CODE       PIC X(06).

TIP:
To guard against mistakes when table sizes get changed, code the
following statement
in the 'housekeeping' area for each table that has a 'table-limit' item:

            COMPUTE 'table-limit' =  LENGTH OF 'table-name' /
                                     LENGTH OF 'table-entry'(1)
(In the sample above, 'table-limit' corresponds to SOURCE-CODE-LIMIT,
'table-name'
corresponds to SOURCE-CODE-TABLE, and 'table-entry' corresponds to
SOURCE-CODE-ENTRY.)
The COMPUTE verb will set the 'table-limit' item to the correct value,
even if the
programmer forgot to change it!  However, every effort should be made to
keep the
OCCURS clause and 'table-limit' in synch, because this will aid
maintainability of
the program.
NOTE:  LENGTH OF is not available in OS/VS COBOL.


6. Searching One Dimensional Arrays or Tables:

a. Why should you use OCCURS...DEPENDING?

1) It becomes unnecessary to 'pad' unused table items with high-values,
etc.,
because you will never reference them.

2) COBOL will use the current value of 'object' to limit the SEARCH
verb, whether
serial or binary searching.  This can save significant amounts of time
for a large
table with few active entries.  (The current value of 'object' affects
other verbs,
too, such as UNSTRING, MOVE, etc.)

3) During debugging, CEEDUMP and the Debug Tool will dump only as much
of a table
as is in use.  The OS/VS COBOL compiler's SYMDMP option and, on TSO, the
TESTCOB
command's LIST subcommand will work the same way.  This can save many
lines of printing.

b. In some cases, the most efficient way to search a table is using a
serial
search.  This usually implies a small table, or a table in which the
keys are in the
same sequence as other data being processed, such as a master file.  In
such cases,
look for conditions which allow searching beginning at an entry later
than the first
and ending before the last.  Always try to maintain an index with the
last entry found
(or searched), so that another search for the same search key (in a
subsequent input
record, for instance) will not require any search at all.  This logic is
applicable
to binary searches as well.
(Any table can be defined with multiple index items.  The first index
item is used
by default by the SEARCH verb.  When serial searching, an index item
other than the
first can be specified.)

c. If the table must be in sequence, document this fact by use of the
ASCENDING
/ DESCENDING KEY phrase of the OCCURS clause.  (Try to limit the number
of key
fields.  Usually, one contiguous field can be made.  Remember that
ascending or
descending sequences are allowed; you'll usually use ascending.)  An
algorithm can
be written which will load in the proper sequence (see below).  You
might also issue
a message if you detect a sequence error in the input asking that the
data be sorted,
to speed up the load process.

d. If the table is sequenced, SEARCH it using a binary search rather
than a
serial search.  (Certain very small tables are not worth searching using
the binary
technique - they also aren't worth sequencing.)  In the absence of exact
numbers for
"payoff" in binary searching; you may assume binary would be faster for
32 or more
occurences, unless you have access to a better number.


e. Binary searches can be accomplished by the COBOL verb SEARCH ...
ALL.  Many
installations also have a subroutine such as the IBM supplied LOOKUP.
The
subroutine may perform better, but SEARCH has good KEY flexibility and
requires
fewer source statements.  Also, since it is a part of the COBOL
standard, it is
transportable if the program is moved to another platform.  There may be
small
differences in the action taken when no match is found.  For example,
when
SEARCH ... ALL executes the END clause, it leaves the INDEX name
unchanged.
LOOKUP, on the other hand, returns a non-zero return code and sets a
field
called 'entry-returned' to point to the next higher item in the table as
compared
to the key being searched for.  Sometimes you can take advantage of
these actions,
such as when an exact match is not made, and further searching for a
'next best'
match is required.  In such a case, the possibilities for a 'next best'
match could
be found by looking backward from the 'entry-returned' number.

f. Dynamic tables: Sometimes an application will add or delete table
items,
perhaps adding an item which must be searched for later, and deleting
the item once
it has been found.  Assuming that the table is large enough to require
binary
searching and sequencing, two simple algorithms can be coded to
accomplish inserts
and deletes.  One is the same code used to sequence a table while
loading.

g. Adding an item in sequence to a table:
The method is to move the last item in the table to the next occurrence,
repeating
this move until there is room for the new entry at the proper point to
maintain the
table's sequence.

                  ADD 1            TO 'object'
                  IF  'object'     >  'table-limit'
                      PERFORM TABLE-OVERFLOW
                  END-IF
                  SET 'index'      TO 'object'
                  SET 'index' DOWN BY 1
                  IF  'object'     >  1
                      PERFORM MAKE-ROOM-IN-TABLE
                          VARYING 'index' FROM 'index' BY -1
                          UNTIL   'index'   <  1
                             OR   'new-entry-key' >  'entry-key(index)'
                  END-IF
                  MOVE 'new-entry' TO 'entry(index + 1)'
                  .
The MAKE-ROOM-IN-TABLE procedure reads:
              MAKE-ROOM-IN-TABLE                             SECTION.
                  MOVE 'entry(index)' TO 'entry(index + 1)'
                  .
The TABLE-OVERFLOW procedure is the one mentioned earlier as being used
to read and
count the rest of the table input and output a message which specifies
table size
vs. the size of the table input file.


h. Deleting an item from a table:
The method is to move the next  item in the table over the item being
deleted,
repeating this move until the end of the table is reached.  The result
is a table
one item shorter than before, even to the point of becoming 'empty'
(zero
occurrences).

The item to be deleted is pointed to by 'index', and the size of the
table is
contained in 'object'.  The value of 'object' must be greater than zero,
and
'index' must be in the range of 1 to 'object', inclusive.

                  IF 'object'  >  1
                      PERFORM TAKE-ITEM-OUT-OF-TABLE
                          VARYING 'index' FROM 'index' BY 1
                          UNTIL   'index'   =  'object'
                  END-IF
                  SUBTRACT 1 FROM 'object'
                  .
The TAKE-ITEM-OUT-OF-TABLE procedure reads:
              TAKE-ITEM-OUT-OF-TABLE                         SECTION.
                  MOVE 'entry(index + 1)' TO 'entry(index)'
                  .
=====
Obtaining TRACE Output for 1985 ANSI COBOL Programs

One of the most basic but popular debugging techniques used in 1968 ANSI
COBOL
programming was the READY / RESET TRACE feature.  This allows the
programmer to
obtain a "flow trace" of the procedures executed in a program.  It is
useful both
as a way to improve understanding of a program which the programmer has
never seen,
and to learn what paths led to a certain condition, such as an abnormal
termination.
The feature was removed from the 1974 ANSI COBOL standard, but IBM kept
it in OS/VS
COBOL as an extension.  However, it was removed from IBM compilers
beginning with
VS COBOL II.  Traces of program activity could be obtained using the IBM
debugging
tool for a given compiler (TESTCOB, COBTEST, or Debug Tool).

It is possible to obtain this information in another way.  The Debug
Language
feature of COBOL allows use of the DEBUGGING MODE switch, debugging
lines (ï¿½Dï¿½ in
column 7), debugging sections, and the DEBUG-ITEM special register to
produce output
similar, and in some ways, superior to that from READY TRACE.  (The
Debug Language
feature, according to the 1985 ANSI COBOL standard, is an obsolete
element that is
scheduled to be deleted from the next standard.  However, the draft of
the possible
2002 ANSI COBOL standard still has the feature, and still has the
statement about
it being obsolete.)

In SOURCE-COMPUTER, code (WITH) DEBUGGING MODE after the computer-name.

At the start of the PROCEDURE DIVISION, code DECLARATIVES, followed by
one or more
SECTIONS, and terminated by END DECLARATIVES.  A debugging section must
begin with
"USE (FOR) DEBUGGING ALL PROCEDURES.", followed by a paragraph name,
followed by
the COBOL statement(s) that produce the desired output.  The DEBUG-ITEM
contains a
line number, DEBUG-NAME, optional subscript values, and an item named
DEBUG-CONTENTS.

A useful statement to code in the paragraph might be:
DISPLAY DEBUG-NAME ', ' DEBUG-CONTENTS

This would provide both the procedure-name being executed, and tell how
the procedure
was given control (GO TO, PERFORM, Fall-Through, etc.).  This is
actually more
information than READY TRACE would provide.  An example of using this
feature follows.

This sample program will generate a trace of the "interesting" parts of
a program.
Parts that are already known not to be problematic are not traced, to
reduce the
amount of output.

 IDENTIFICATION                                          DIVISION.
 PROGRAM-ID.    READYTRC.
*AUTHOR.        COLIN CAMPBELL
*DATE-WRITTEN.  MARCH 25, 1999.
 ENVIRONMENT                                             DIVISION.
 CONFIGURATION                                            SECTION.
 SOURCE-COMPUTER.  IBM-S390        DEBUGGING MODE.
 OBJECT-COMPUTER.  IBM-S390.
 DATA                                                    DIVISION.
/
 WORKING-STORAGE                                          SECTION.
 77  PIC X(032) VALUE 'BEGIN READYTRC   WORKING-STORAGE'.
*
 01  TRACE-SWITCH     PIC X(01) VALUE '1'.
  88 TRACE-ACTIVE               VALUE '1'.
  88 TRACE-INACTIVE             VALUE '0'.
 01  TIME-STAMP PIC X(23).
 01  PIC X(032) VALUE 'END   READYTRC   WORKING-STORAGE'.
/*****************************************************************
 PROCEDURE                                               DIVISION.
DDECLARATIVES.
DREADY-TRACE                                              SECTION.
D    USE     DEBUGGING ALL PROCEDURES.
DSHOW-PROCEDURE-NAME.
D    IF      TRACE-ACTIVE
D    DISPLAY DEBUG-NAME ', ' DEBUG-CONTENTS
D    .
DEND DECLARATIVES.
DREMAINDER-OF-PGM                                         SECTION.
 MAINLINE.
     MOVE    FUNCTION CURRENT-DATE TO TIME-STAMP
     DISPLAY 'READYTRC WAS RUN '      TIME-STAMP
     SET     TRACE-INACTIVE        TO TRUE
     PERFORM UNTRACED-PROC
     SET     TRACE-ACTIVE          TO TRUE
     GOBACK
     .
 UNTRACED-PROC.
     DISPLAY 'UNTRACED-PROC DOES NOT APPEAR IN TRACE LISTING'
     .
```

#### ↳ Re: COBOL Tips and Techniques

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-03-18T02:26:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mtvda.320$QW6.113@newssvr19.news.prodigy.com>`
- **References:** `<3E763341.30E6C603@attglobal.net>`

```
When loading a table, I always display the table name, number of entries,
AND % full, so the table growth can be monitored and the size increased
BEFORE it abends.
```

##### ↳ ↳ Re: COBOL Tips and Techniques

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-17T21:40:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E76B160.C19012C4@attglobal.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <mtvda.320$QW6.113@newssvr19.news.prodigy.com>`

```


Terry Heinze wrote:

> When loading a table, I always display the table name, number of entries,
> AND % full, so the table growth can be monitored and the size increased
…[4 more quoted lines elided]…
> ....Terry

Terry,
That sounds very professional, and the type of thing I'm hoping for in this
document.  Would you mind if I incorporate your suggestions in the document?
Of course, the one problem I see is that once you write the program, you might
not be around to monitor the table growth, and I wonder who would do it in
your absence?  (This will happen to me pretty soon -- retirement looms on the
horizon.  And it might happen to others not so old, given the current thinking
about off shore programming.)

You got me thinking, though.  Maybe these data elements could be passed to a
subroutine which records the data about lots of tables, and sounds the alarm
at some threshhold.  Then, your good idea and technique could "live on", so to
speak.
Thanks,
Colin
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-03-18T08:18:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7DAda.11788$ja4.810023@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <mtvda.320$QW6.113@newssvr19.news.prodigy.com> <3E76B160.C19012C4@attglobal.net>`

```

Colin Campbell <cmcampb@attglobal.net> wrote in message news:3E76B160.C19012C4@attglobal.net...
> 
> You got me thinking, though.  Maybe these data elements could be passed to a
> subroutine which records the data about lots of tables, and sounds the alarm
> at some threshhold.  Then, your good idea and technique could "live on", so to
> speak.

The standard practice could be to set up a production support email group,
and code the program to generate a warning email to the production support team 
whenever the table hits a predetermined percentage of capacity.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 4)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-03-19T01:15:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TwPda.12$5J6.2@newssvr19.news.prodigy.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <mtvda.320$QW6.113@newssvr19.news.prodigy.com> <3E76B160.C19012C4@attglobal.net> <7DAda.11788$ja4.810023@bgtnsc05-news.ops.worldnet.att.net>`

```
I'm sure I was the last person to monitor these table sizes at previous
shops!  :(  The production support e-mail sounds like a good idea.  There
are other solutions too.  Write table size/growth information to a DB2
table, VSAM file, or whatever and generate a report daily to be distributed
to prod support.  After calculations, I'd put out a 1-liner for each table
to SYSOUT as follows:

01  WS-TABLE-INFO-MSG.
     05   WS-TABLE-DESC           PIC  X(20)  JUST RIGHT.
     05                                         PIC  X(17)  VALUE
           ' TABLE SIZE .... '.
     05   WS-TABLE-SIZE           PIC  Z(4)9.
     05                                         PIC  XX      VALUE ' ('.
     05   WS-TABLE-PCT-FULL    PIC  ZZ9.
     05                                         PIC  X(7)  VALUE '% FULL)'.
```

#### ↳ Re: COBOL Tips and Techniques

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e767401.36895768@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:

> Read the Programming Guide
>(SC26-4767) 'Chapter 4: Handling Tables'.  It discusses some new
>features, including
>the INITIALIZE verb (which a good program should never need to use) 

Applause. 

>a. If you know exactly how many items there are in a table, use the
>OCCURS
…[17 more quoted lines elided]…
>table. 

Very good! I advocate defining ALL tables variable length. The ones which appear
to be fixed length when a program is written will change due to maintenance.
For example: 

 01  word-values.
     05  filler value 'advertising              ' pic x(25).
     05  filler value 'aerospace                ' pic x(25).
    ... 500 more words
    05  filler value high-values                 pic x(25000).
01  filler redefines word-values.
    05  word-value occurs 1 to 1000 depending on dictionary-size
        indexed x-word ascending key word-value pic x(25).

 if  dictionary-size equal to 1000
     set x-word to 1
     search word-value
         at end display 'dictionary too small. program maintenance required'
              goback
         when word-value (x-word) equal to high-values
         set dictionary-size to x-word
     end-search
 end-if
```

##### ↳ ↳ Re: COBOL Tips and Techniques

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-18T00:23:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303180023.4b76d25f@posting.google.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

>  01  word-values.
>      05  filler value 'advertising              ' pic x(25).
…[5 more quoted lines elided]…
>         indexed x-word ascending key word-value pic x(25).

Why would you build such data items into the source code.  Any chages
would require programmer involvement and recompiling + retesting etc
(if you do this).

It is likely to be much better to have it as a text file, or somesuch,
and read it in when required.  Then the user can add whatever words
they wish.
 
>  if  dictionary-size equal to 1000

It seems that the 1000 is what the 'dictionary-size' is initially set
to so that this acts as a 'first-time' flag.

>      set x-word to 1
>      search word-value
…[5 more quoted lines elided]…
>  end-if

I don't think that this is particularly useful.  There will only be
more words added by the programmer, if he adds more so that there are
999 words (thus the first high-values is 1000) then the 'first-time'
code will run _every_ time.

Using a literal 1000 as a 'first-time' flag value is also flawed
because the programmer will need to find and change the test when the
table is increased, otherwise it will fail to match and the first-time
code won't be done.

The aim seems to be to get code where words can just be added and the
rest looks after itself and is self-checking, without, say, counting
(ie for lazy programmers).  By having a pic x(25000) for the
high-values then you are wasting as much space as the table uses, yet
even though the table is _twice_ the neccessary size it will report
'too small'.

Why not just have pic x(25) occurs 2000 and read the words into the
program and check against the actual available size.
   
   01  dictionary-size                 pic s9(8) binary value ZERO.
   01  dictionary-occurs               pic s9(8) binary value 2000.
   01  word-table.
       05  word-value occurs 1 to 2000 depending on dictionary-size
           indexed x-word ascending key word-value pic x(25).
  
   IF ( Dictionary-Size = ZERO )
       OPEN ...
       READ
           ....
           IF ( Dictionary-Size >= Dictionary-Occurs )
               error too small ..
           ELSE
               ADD 1         TO Dictionary-Size
               SET X-Word    TO Dictionary-Size               MOVE
....
           END-IF
       ...
    END-IF  
Eventually after adding many words the user may exceed the size
allowed.  The change required is in _one_ place . This code is not
sensitive to specific values and changes to table size won't stop code
working.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77cecf.14630807@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <217e491a.0303180023.4b76d25f@posting.google.com>`

```

riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[15 more quoted lines elided]…
>they wish.

Good point. In this case, the program's vocabulary wasn't expected to change
much. If it did, I (the programmer) would make the change. So I took the lazy
approach. You're right, I should have stored it in a file. 
>
>>  if  dictionary-size equal to 1000
…[16 more quoted lines elided]…
>code will run _every_ time.

Another valid, but highly improbable, criticism. The table might overflow in ten
years, probably never. 

>The aim seems to be to get code where words can just be added and the
>rest looks after itself and is self-checking, without, say, counting
…[3 more quoted lines elided]…
>'too small'.

Memory management is performed by the operating system. Unreferenced high values
will never be paged in (or will be paged out). 

>Why not just have pic x(25) occurs 2000 and read the words into the
>program and check against the actual available size.
…[23 more quoted lines elided]…
>working.

Yes, I agree that's a BETTER approach.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-19T04:50:02
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77db97_2@text-west.newsgroups.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <217e491a.0303180023.4b76d25f@posting.google.com> <3e77cecf.14630807@news.optonline.net>`

```
 Excellent!

We are starting to see importance attached to WHAT's right, rather than
WHO's right.

This mail is a piece of gold amongst the mica that has been posted lately...

Pete.


"Robert Wagner" <robert@wagner.net> wrote in message
news:3e77cecf.14630807@news.optonline.net...
>
> riplin@Azonic.co.nz (Richard) wrote:
…[20 more quoted lines elided]…
> Good point. In this case, the program's vocabulary wasn't expected to
change
> much. If it did, I (the programmer) would make the change. So I took the
lazy
> approach. You're right, I should have stored it in a file.
> >
…[7 more quoted lines elided]…
> >>          at end display 'dictionary too small. program maintenance
required'
> >>               goback
> >>          when word-value (x-word) equal to high-values
…[9 more quoted lines elided]…
> Another valid, but highly improbable, criticism. The table might overflow
in ten
> years, probably never.
>
…[7 more quoted lines elided]…
> Memory management is performed by the operating system. Unreferenced high
values
> will never be paged in (or will be paged out).
>
…[27 more quoted lines elided]…
> Yes, I agree that's a BETTER approach.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-19T17:26:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b58v6u$a4f$1@aklobs.kc.net.nz>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <217e491a.0303180023.4b76d25f@posting.google.com> <3e77cecf.14630807@news.optonline.net>`

```
Robert Wagner wrote:

> Another valid, but highly improbable, criticism. The table might overflow
> in ten years, probably never.

Maybe, in this particular case, but you had this as an example of a general 
approach.  In anyone copied this it may fail to work correctly at other 
times.
 
> Memory management is performed by the operating system. Unreferenced high
> values will never be paged in (or will be paged out).

Many memory management mechanisms work on segments, and thus the whole 
table would be in memory including the wasted space.  Others use fixed 
pages and the whole page is loaded if _any_ byte is referenced.

Your optimism about VM is unjustified.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-20T01:31:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e790783.32036012@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <217e491a.0303180023.4b76d25f@posting.google.com> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[12 more quoted lines elided]…
>pages and the whole page is loaded if _any_ byte is referenced.

The only reason why I wrote the big filler was to avoid a compiler warning. Some
compilers, such as Fujitsu, issue a warning when the redefinition is bigger than
the original; others, such as Micro Focus, do not. I'm averse to compiler
warnings

Most modern memory managers operate on page sizes of 2K or  256 bytes. Really
enlightened ones operate on page size = object size. The hardware pretty much
dictates the independence of page size from anything related to the program.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-20T13:57:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b7bf$mcm$1@aklobs.kc.net.nz>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz> <3e790783.32036012@news.optonline.net>`

```
Robert Wagner wrote:

>>> Memory management is performed by the operating system. Unreferenced
>>> high values will never be paged in (or will be paged out).
…[3 more quoted lines elided]…
>>pages and the whole page is loaded if _any_ byte is referenced.
 
> The only reason why I wrote the big filler was to avoid a compiler
> warning. Some compilers, such as Fujitsu, issue a warning when the
> redefinition is bigger than the original; others, such as Micro Focus, do
> not. I'm averse to compiler warnings

The point that you seemed to want to show was that table size could be set 
and checked.  It seems that if the table may 'run out' then at least get it 
to use all the space given to it.
 
> Most modern memory managers operate on page sizes of 2K or  256 bytes.
> Really enlightened ones operate on page size = object size. The hardware
> pretty much dictates the independence of page size from anything related
> to the program.

Exactly, which is why 'unreferenced high values' _will_ be paged in when a 
reference is made to a byte that is in the segment or page that the 
high-values are also in.

The only way that your claim would be true is if the first high-value 
happened to fall _exactly_ on a page boundary, and other data items in W-S 
beyond the table were not in that/those pages.

It is still lazy programming.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-20T10:43:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e799af3.69785850@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz> <3e790783.32036012@news.optonline.net> <b5b7bf$mcm$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[5 more quoted lines elided]…
>>>pages and the whole page is loaded if _any_ byte is referenced.

>> Most modern memory managers operate on page sizes of 2K or  256 bytes.
>> Really enlightened ones operate on page size = object size. The hardware
…[9 more quoted lines elided]…
>beyond the table were not in that/those pages.

Your thinking is rooted in the days when we programmers had to compensate for
machine and OS inadequacies. Give it up; those days are over.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-20T16:16:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5cpgj$c1o$1@peabody.colorado.edu>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz> <3e790783.32036012@news.optonline.net> <b5b7bf$mcm$1@aklobs.kc.net.nz> <3e799af3.69785850@news.optonline.net>`

```

On 20-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> Your thinking is rooted in the days when we programmers had to compensate for
> machine and OS inadequacies. Give it up; those days are over.

We have to compensate less and less as the years go by.  But what can be called
"machine and OS inadequacies" will still be around when I am done programming.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-20T11:42:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303201142.6ba73754@posting.google.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz> <3e790783.32036012@news.optonline.net> <b5b7bf$mcm$1@aklobs.kc.net.nz> <3e799af3.69785850@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> Your thinking is rooted in the days when we programmers had to compensate for
> machine and OS inadequacies. Give it up; those days are over.

Lazy programming rulz.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-03-20T21:33:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-AE0EAB.21331120032003@corp.supernews.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz> <3e790783.32036012@news.optonline.net> <b5b7bf$mcm$1@aklobs.kc.net.nz> <3e799af3.69785850@news.optonline.net>`

```
In article <3e799af3.69785850@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

<snip> 
> ... we programmers had to compensate formachine and
> OS inadequacies. Give it up; those days are over. 


Hmmm, for some reason I thought you used Windows...


;-)
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-21T04:48:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7a9149.132857542@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e77cecf.14630807@news.optonline.net> <b58v6u$a4f$1@aklobs.kc.net.nz> <3e790783.32036012@news.optonline.net> <b5b7bf$mcm$1@aklobs.kc.net.nz> <3e799af3.69785850@news.optonline.net> <joe_zitzelberger-AE0EAB.21331120032003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <3e799af3.69785850@news.optonline.net>,
> robert@wagner.net (Robert Wagner) wrote:
…[6 more quoted lines elided]…
>Hmmm, for some reason I thought you used Windows...

Let's not turn this into a Microsoft-bashing religious war. I think W2K/NT is a
respectable operating system. As for Win95 and 98, the problem wasn't the OS per
se, it was allowing 16-bit drivers into the inner circle. At the time, it was
necessary due to marketing pressures.
```

##### ↳ ↳ Re: COBOL Tips and Techniques

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-18T15:05:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57ckl$h9l$1@peabody.colorado.edu>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net>`

```

On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> Very good! I advocate defining ALL tables variable length. The ones which
> appear
> to be fixed length when a program is written will change due to maintenance.
> For example:

How about?

05   Days-of-week  .
       10   Day-of-Week     occurs 07   pic x(09).
05    Days-redefined      redefines Days-Of-Week.
        10   Filler              pic x(09)    value 'Monday'.
        10   Filler              pic x(09)    value 'Tuesday'.
        10   Filler              pic x(09)    value 'Wednesday'.
        10   Filler              pic x(09)    value 'Thursday'.
        10   Filler              pic x(09)    value 'Friday'.
        10   Filler              pic x(09)    value 'Saturday'.
        10   Filler              pic x(09)    value 'Sunday'.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-18T08:39:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E774BD8.1BCB5F63@attglobal.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <b57ckl$h9l$1@peabody.colorado.edu>`

```
Howard,
I believe that my company may have a strategy in mind to guarantee employees
Saturday and Sunday off every week, if we agree to adding another day (Workday?)
to the week.  Today, they just expect us to donate an extra 10% billable hours.

So, maybe that table does need to be variable!
j/k,
Colin

Howard Brazee wrote:

> On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-18T16:41:35
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7730da$1_1@text-west.newsgroups.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <b57ckl$h9l$1@peabody.colorado.edu>`

```
Now, now, Howard...

That's an obscure, deliberately concocted example, for the sole purpose of
making Robert wrong <G>...

Pete.

"Howard Brazee" <howard@brazee.net> wrote in message
news:b57ckl$h9l$1@peabody.colorado.edu...
>
> On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
> > Very good! I advocate defining ALL tables variable length. The ones
which
> > appear
> > to be fixed length when a program is written will change due to
maintenance.
> > For example:
>
…[12 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77d31c.15731589@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <b57ckl$h9l$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
…[17 more quoted lines elided]…
>        10   Filler              pic x(09)    value 'Sunday'.

You got me there .. although someone will concoct an eighth day of week to prove
you wrong.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com>
- **Date:** 2003-05-08T07:28:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB9EAFF.C6D94B7D@fujitsu-siemens.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <b57ckl$h9l$1@peabody.colorado.edu>`

```


Howard Brazee schrieb:

> On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[17 more quoted lines elided]…
>

I think that redefines clause doesn't work with subordinate value. So it should be
the other way around.

Rosa
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-09T02:03:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebb0013.33246665@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <b57ckl$h9l$1@peabody.colorado.edu> <3EB9EAFF.C6D94B7D@fujitsu-siemens.com>`

```
Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com> wrote:

>Howard Brazee schrieb:
>
…[4 more quoted lines elided]…
>> > to be fixed length when a program is written will change due to
maintenance.
>> > For example:
>>
…[14 more quoted lines elided]…
>I think that redefines clause doesn't work with subordinate value. So it should
be
>the other way around.

You are correct, using standard COBOL.
```

##### ↳ ↳ Re: COBOL Tips and Techniques

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-18T09:05:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303180905.e09784b@posting.google.com>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e767401.36895768@news.optonline.net>...
<snip>
>  01  word-values.
>      05  filler value 'advertising              ' pic x(25).
…[15 more quoted lines elided]…
>  end-if


This seems like it would be a better candidate for a text tree
structure than a fixed table.  For those not familiar, a text tree
used the characters of a word as keys to the nodes of the tree.  If a
terminal leaf is found at the end of the word it is valid, if a
terminal leaf is not found the word is not valid.

You can get very compressed dictionaries and the search time is less
than that of a binary search.
```

###### ↳ ↳ ↳ Re: COBOL Tips and Techniques

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77e1c9.19489059@news.optonline.net>`
- **References:** `<3E763341.30E6C603@attglobal.net> <3e767401.36895768@news.optonline.net> <16e2f010.0303180905.e09784b@posting.google.com>`

```
psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e767401.36895768@news.optonline.net>...
><snip>
>>  01  word-values.
…[26 more quoted lines elided]…
>than that of a binary search.

I wrote a spell checker which worked exactly that way. But the amount of code is
non-trivial. The above code is a quick and dirty COBOL solution using SEARCH
ALL, which is reasonably close to a leaf search.
```

#### ↳ Re: COBOL Tips and Techniques

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-18T08:55:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303180855.2d1374a6@posting.google.com>`
- **References:** `<3E763341.30E6C603@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote in message news:<3E763341.30E6C603@attglobal.net>...

> TIP:
> To guard against mistakes when table sizes get changed, code the
…[4 more quoted lines elided]…
>                                      LENGTH OF 'table-entry'(1)
<snip>

This is a good question for the standards people.  Is there anything
in 2002 that will allow this to be done a compile time?  I would love
to see something like:

    05 my-table  occurs lots Pic X(?).

    05 size-of-my-table Binary Pic S9(8)
       Value (Length of my-table / Length of my-table (1)).


If such a thing is not possible I would think it might be worth a
write up for the upcoming 'future of Cobol' event.  Sure, it is small
and trivial, but it is also a great time saver too.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
