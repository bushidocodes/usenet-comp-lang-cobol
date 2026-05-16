[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What's Missing in a COBOL Style Guide?

_258 messages · 22 participants · 2003-03 → 2003-04_

---

### What's Missing in a COBOL Style Guide?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-12T15:51:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E6FC7EC.8EF66036@attglobal.net>`

```
Folks,
You provided lots of great input when I posted a proposed COBOL
Programming Standard a few days ago.  One thing that came up repeatedly,
both in this newsgroup and within my company was "show us examples of
how to code, not just the prohibitions about what we cannot code".

So, I'm dusting off a Style Guide that has been laying around, probably
largely ignored.  I think I can sneak it into the standard without
alarming the management too badly.

How about looking it over and telling me what else it needs to say, what
it says wrong, etc.?  It is unabashedly IBM Mainframe COBOL oriented.
I'd be willing to have suggestions that apply to other platforms,
though.

Here's the document:
                1985 ANSI/ISO COBOL -- Style Guide
                                1
                          Introduction

From: Colin Campbell

Date: 12 March 2003

This Style Guide for writing 1985 ANSI/ISO COBOL is intended to
suggest ways that programmers can write more readable and more
maintainable programs.  Nothing in this guide needs to be taken
as a rule.  Programmers are free to follow some suggestions and
ignore others.  Programmers are, however, encouraged to think
about the suggestions and how they might help in programming;
also, they should read the entire document, because they may see
programs in the future which use some of these suggestions, and
need to understand the code they're seeing.

Contributions to the Style Guide are welcome from anyone coding
COBOL at CoX-ORG; they may be sent to:

Colin Campbell at xxx

                       General Suggestions

1.Use of comment lines:

  Both the '/' and '*' in Column 7 (the 'Continue Column', in
  COBOL terminology) can be used to signify comments.  The '/'
  causes a page eject on the output listing of any compiler,
  according to the 1985 ANSI standard.  Many programmers use the
  '/' without any other text to start a new page, then put
  comment lines starting with '*' after it, to tell what a set
  of data items is for or what a procedure does.  Since the '/'
  is also a comment line, go ahead and start the 'comment text'
  on that line, and continue with '*' lines.

  Comments are often interspersed within source code, especially
  in the Procedure Division, to explain to a reader the intent
  of some code.  Such comments should be general in their nature
  (such as 'This is the case of a keyword coded without its
  value'), and the code itself should be clear enough to be
  understandable once the 'general idea' is given by the
  comment.  If the comment has to tell the reader a lot of
  detail, this may mean that the code should be changed -
  perhaps to improve the names of data items or conditions.
  Watch for this situation.

  Programmers sometimes put code in a program which they do not
  intend to use in the production version of the program, such
  as debugging lines, or logic which it is later decided is not
  needed (but the programmer thinks might be wanted in the
  future).  The normal thing to do in this case is to turn
  thecode into comments by putting '*' in the continue column.
  Two variations on this practice might be useful.

  One is to put a distinctive string, perhaps '**' or '*==>' on
  such lines.  This makes it easy to find all of them when
  editing a program.  When the saved lines prove to be needed,
  you'll save time locating them.  You could even use different
  'comment strings' for different related groups, since there
  are often data items and procedure statements which both
  relate to a feature.

  If you've used 'debugging lines' (usually DISPLAY verbs, with
  perhaps some data items to allow conversion of indexes, etc.)
  in testing your program, you may want to keep them for future
  testing.  COBOL contains a little used feature called the
  Debug Module which can help with this.  Change these lines to
  true 'debug lines' by coding 'D' in the continue column.  Such
  lines are treated as comments unless the SOURCE-COMPUTER
  paragraph contains the phrase 'WITH DEBUGGING MODE '.  The
  following method of coding the SOURCE-COMPUTER paragraph is
  suggested:

        *SOURCE-COMPUTER. IBM-390 DEBUGGING MODE.

  By changing the '*' to a space, all of the 'D' lines in the
  program are activated (that is, compiled and executed); by
  changing the space to '*', they are all deactivated (that is,
  ignored by the compiler).  Since the SOURCE-COMPUTER paragraph
  has no other purpose except to set the debugging mode on or
  off, it may be commented or omitted.
                       General Suggestions

2.Use of EJECT and SKIP1/2/3:

  These compiler directives are IBM extensions to COBOL, while
  comment lines are defined as part of the language by ANSI.
  Therefore, it would be better to use the standard method to
  control the listing.

  If an existing program containing EJECT and/or SKIPn
  directives is being converted to ANSI 1985 COBOL, it is
  relatively simple to change all of the EJECT lines to the '/'
  in the continue column.  The process using the ISPF/PDF Editor
  would be to exclude all lines and find all occurrences of
  EJECT, change all space in column 7 to '/' in the non-excluded
  lines, and finally, remove all occurrences of EJECT.  The
  editor commands would be:

        X ALL;
 F ALL ' EJECT ';
 C ALL NX ' ' '/' 7;
 C ALL NX ' EJECT ' ''

  A similar sequence could be used for SKIP1, SKIP2, and SKIP3
  replacement (these would be changed to '*' in the continue
  column).

  While this not a document to teach ISPF, command sequences
  like the one shown above can be retrieved and modified easily
  by setting one of the PF keys to the value 'RETRIEVE' or
  'CRETRIEV'.  (Type 'KEYS' on any ISPF command line to get
  access to the key meanings.)

3.Coding a COBOL Program in Mixed Case:

  Beginning with 1985 ANSI COBOL, the 26 lower case alphabetic
  characters may be used anywhere the 26 upper case alphabetic
  characters can be used, and the lower case and upper case
  equivalents are considered equal.

  This means that reserved words and user defined names may be
  coded in either case - "identification", "Identification",
  "IdEnTiFiCaTiOn", and "IDENTIFICATION" are all equivalent and
  valid.  A procedure name may be defined as "READ-A-RECORD" and
  referenced as "read-a-record".

  Should you use upper case, as in the past, or start using
  lower case, or use a mixture?  This is your choice.  To the
  compiler, it makes no difference, because every reserved word
  or name is translated to upper case for the purposes of
  matching.  To you, however, there is a difference.  First, non-
  numeric literals are NOT translated, so if you wish them to
  appear in  upper case on output, for example, you must enter
  them in upper case.  Second, while the ISPF Editor's FIND
  command will find strings in either case, there may be
  utilities that will not.  Third, there is the question of
  readability.  You must decide, but the vast majority of COBOL
  programs now in existence are written in upper case, so it may
  be hard for a programmer to read a lower or mixed case program
  as quickly.

  All in all, it may be better to continue to code COBOL in
  upper case, only using lower case characters in places where
  they are needed, such as to compare against input, to create
  mixed case messages, or the like.

                    Procedure Division Ideas

4.Creating Data and Procedure Names:

  It is usually a good idea to choose user defined names, such
  as data names and procedure names, which contain at least one
  hyphen ('-') to reduce the chance that they may conflict with
  current or future COBOL reserved words.

  Avoid very simple words, and common words, especially if they
  are Data Processing terms.

  Very short names are desirable for use as subscripts and
  indexes, but make them at least  two characters long, to
  simplify finding them when editing a program.  (Think how
  difficult it would be to find the occurrences of the words 'I'
  or 'X' as opposed to the word 'IX'!)

  If you've tried to convert an old program to 1985 ANSI COBOL
  and find that the program used what is now a reserved word,
  one technique for converting it might be to append '--X' to
  the name (assuming it is short enough).    There are no COBOL
  reserved words with consecutive hyphens, and very few user
  defined names.

                    Procedure Division Ideas

1.Coding of Periods

  Code periods very sparingly in the Procedure Division.
  Periods are required only at the end of a procedure header
  (paragraph name, or section name followed by the word SECTION)
  and at the end of a procedure (paragraph or section).  The
  period at the end of a procedure should be coded on a new line
  in column 12 (the start of 'margin B' in COBOL terms).  Since
  periods are easy to overlook, this helps make it easier to
  check visually that they are present.

  The practice of coding a period after each statement makes
  changing a program harder.  For example, a series of MOVE
  statements might have started out being unconditional, but
  later need to be executed only if a condition is met.  If each
  MOVE ends with a period, then the periods must be removed to
  make the whole group execute only under the condition.

  One of the most common errors in COBOL programming is
  misplacing periods, either putting one where it shouldn't be,
  or leaving one out that is needed.  Most often, this is
  related to use of the IF statement.  Instead of terminating IF
  statements with a period, use the END-IF 'scope terminator',
  and line it up with the IF to which it corresponds.

  When coding nested IF's, it is not always practical to use END-
  IF, because it may require two, three, four, or more to 'end'
  all of the conditions.  In this case, the period is a great
  convenience, so it should be used, but code it on a new line
  at the start of margin B.  Doing this is valid COBOL syntax,
  and it makes modification of the IF statement simpler, because
  the period doesn't have to be removed from the 'old' last line
  and replaced on a 'new' last line.

2.Aligning procedural statements:

  For a set of statements in a single procedure, try to align
  the word 'TO' and all of the relational operators (think of
  them as being two characters long, since there are now '<='
  and '=>' as well as  '= ', etc.) for improved readability.
  For example:

              MOVE     DATE--NAME              TO DATA--NAME-2
              IF       DATA--NAME-3            =  DATA--NAME-4
                       MOVE     DATA--NAME-2   TO DATA--NAME-3
              END-IF

  In addition, code verbs in 'fixed' columns, leaving room for
  the longer verbs (EVALUATE, SUBTRACT, and UNSTRING are each
  eight characters).  This generally helps the eye see each
  statement more easily.  Most editors can be set up to provide
  tab characters so that entering the statements doesn't require
  excessive use of the space bar.

  The ISPF Edit and View facilities offer an aid to looking at
  COBOL and other types of source code.  This is the HILITE
  command.  In order to use it, the PC 3270 Emulator tool must
  support 'Extended Attributes', and the user must choose a
  terminal type that includes extended attributes.  Then, when
  editing a COBOL member, type "HI AUTO" on the commend line.
  The result should be that the COBOL source becomes colored.
  Immediately after, type "HI", which will bring up a dialog
  where there are choices that can be selected using a "/".
  Select all of them.  Then, while still in this dialog, use the
  Action Bar choice "Languages", and type the number for COBOL,
  then press Enter.  Yet another dialog will be started to allow
  you to specify color choices for various COBOL elements.  The
  important one right now is "Special Characters".  Choose a
  distinctive color and under hilighting, type "Reverse".  Then,
  go to the next field, "Special Characters to highlight" and
  enter the period and the semicolon.  Save the changes by
  pressing the End function key.  When you return to viewing
  your program, you'll see that all of the periods are enclosed
  in a character box, and are extremely visible.  These settings
  will be saved in the user's profile data set for use with
  every Edit or View of a COBOL program.

3.Using NOT:
  If you've ever coded 'NOT >' or 'NOT <' relational operators,
  it is time to stop, because 1985 ANSI COBOL allows coding '<='
  (less than or equal to, the equivalent of not greater than)
  and '>=' (greater than or equal to, the equivalent of not less
  than).  Many programmers and theorists believe that humans
  have a hard time understanding the use of NOT.
                    Procedure Division Ideas

4.Improving PERFORM Readability:

  Sequences of code which require repetitive (loop controlled)
  execution and are used only once in a program used to have to
  be coded as a separate procedure  (paragraph or section).  In
  1985 ANSI COBOL, they may be written as part of an 'in line
  PERFORM'.  Using this option allows the programmer to avoid
  creating another procedure name and also puts the code where
  it is actually used, like a FORTRAN DO-loop.  Here is a 1974
  to 1985 ANSI COBOL comparison:
  Old:
        PERFORM  MAKE-ROOM-IN-TABLE
                 VARYING 'index'       FROM 'index' BY -1
                 UNTIL   'index'         <  1
                    OR   'new-entry-key' >  'entry-key(index)'
        MOVE     'new-entry'             TO 'entry(index + 1)'
        ...
    MAKE-ROOM-IN-TABLE  SECTION.
        MOVE     'entry(index)'          TO 'entry(index + 1)'
        .
  New:
        PERFORM
                 VARYING 'index'       FROM 'index' BY -1
                 UNTIL   'index'         <  1
                    OR   'new-entry-key' >  'entry-key(index)'
          MOVE   'entry(index)'          TO 'entry(index + 1)'
        END-PERFORM
        MOVE     'new-entry'             TO 'entry(index + 1)'
        ...

5.Using 'switches' or 'flags':

  Define the item where such a 'state variable' is stored
  without a data name, and change  the state with SET
  statements.  One example of needing such a variable might be
  in loading a table in a subprogram when it is called for the
  first time.  Testing for zero occurrences in the table
  wouldn't take into account the possibility of an empty input
  file, so some type of first time indicator is needed.  Here is
  a 1974 to 1985 ANSI COBOL comparison:
  Old:
    77    LOAD-TABLE-FLAG       PIC X(01) VALUE 'N'.
      88  TABLE-LOAD-REQD                 VALUE 'N'.
      88  TABLE-LOADED                    VALUE 'Y'.
        ...
        IF       TABLE-LOAD-REQD
                 PERFORM  TABLE-LOAD
                 MOVE     'Y'          TO LOAD-TABLE-FLAG

  New:
    77                          PIC X(01) VALUE 'N'.
      88  TABLE-LOAD-REQD                 VALUE 'N'.
      88  TABLE-LOADED                    VALUE 'Y'.
        ...
        IF       TABLE-LOAD-REQD
                 PERFORM  TABLE-LOAD
                 SET      TABLE-LOADED TO TRUE
        END-IF
  As you can see, there are two advantages to this technique.
  First, the need to invent another data name is avoided.
  Second, the values associated with the 'state' of the variable
  don't have to be known in the Procedure Division; in fact,
  they could be changed to '0' and '1' or anything else without
  requiring any change to the Procedure Division.

                    Procedure Division Ideas

6.   Writing compound conditional expressions:

  Compound conditional expressions (multiple simple conditions
  connected by AND or OR) can be the source of problems in
  programs, especially when maintenance is done by someone not
  familiar with a program.

  One reason is that the AND or OR words usually 'hide' at the
  end of a line.  Consider moving them to the start of the next
  line, and limiting the number of conditions per line to one.
  This will make the 'AND' and 'OR' more visible, and if they
  are aligned under the related 'IF' or 'WHEN', there will be
  more room on the line to write the condition.  Finally, if one
  of the conditions is deleted, or a new condition is added, it
  will usually only be necessary to delete or insert one line,
  and the danger of leaving a 'hanging' AND or OR or forgetting
  to put one in is reduced.  Here is an example:
        IF       TABLE-LOAD-REQD
          AND    TABLE-STATUS          =  '00'
                 PERFORM  TABLE-LOAD
                 SET      TABLE-LOADED TO TRUE
        END-IF

7.Writing expressions:

  Expressions used in COMPUTE, IF, and elsewhere are handled by
  COBOL compilers according to a set of rules which control the
  order of evaluation, such as those for AND and OR in
  conditional expressions and those for '**', '*', '/', '+', and
  '-' in arithmetic expressions.

  Parentheses are required only to force expressions to be
  evaluated in a different order than the rules of COBOL would
  normally cause them to be evaluated.  Some programmers use
  them to 'clarify' a program, so that there will be no doubt
  about the order of evaluation.  You might consider whether
  code which 'needs' such clarification is what you want to
  write.  Sometimes, however, the parentheses are required.  In
  such cases, consider coding each parenthesis on a line by
  itself, or no more than one set of left and right parentheses
  on a line.  The first technique makes the parentheses more
  visible, and the second makes it easier to be sure that they
  are balanced, especially when changing the expression.
  Here is an example:
        COMPUTE  ANSWER =  (
                            C
                        +  (A + 1)
                        *  (B - 2)
                           )
  Remember that the ISPF Editor now can help with this task.
  There is a "HILITE" command available, which can be used to
  colorize COBOL code and check for balanced parentheses.  You
  must have your terminal emulator set up to use "Extended
  Attributes".
```

#### ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-13T00:41:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E6FD423.3F821009@shaw.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net>`

```


Colin Campbell wrote:

> Folks,
> You provided lots of great input when I posted a proposed COBOL
…[3 more quoted lines elided]…
>

Colin, As it's Mainframe - just a couple of pointers which are fairly
universal :-

>
> 5.Using 'switches' or 'flags':
…[32 more quoted lines elided]…
>   requiring any change to the Procedure Division.

My preference, use numerics for 88s. Agreed you can do it with alpha, but :-

01 MYFLAG                          PIC 9(03) VALUE ZERO..
    88 VALIDATION-OK        VALUE 0.
    88 ERROR-NAME             VALUE 1.
    88 ERROR-ZIPCODE     VALUE 2.
    88 ERROR-                         VALUE 3. ETC....

     88 WARNING-ERRORS   VALUE 1 THRU 9
     88 CRITICAL-ERRORS     VALUE 20 THRU 35.

Groupings like VALIDATION-OK, WARNING-ERRORS and CRITICAL-ERRORS allow you
to make specific decisions.

Doesn't always work avoiding that "need to invent another data name". (OK -
so now I'm going back to lowercase - phew !). Here's one I'm currently
testing with sorting collections into different sequences:-

01 SequenceFlag                pic 9.
   88 NewByName                value 1.
   88 NewByCountry             value 2.
   88 NewByType                value 3.
   88 ValidSequence            value 1 thru 3.
01 Old-SequenceFlag            pic 9.
   88 OldByName                value 1.
   88 OldByCountry             value 2.
   88 OldByType                value 3.
................
display "Phase 2 - Default Sort using MOVE CORRESPONDING"
move 9 to SequenceFlag
perform CHOICE-PARA until SequenceFlag = zeroes
EXIT METHOD.

CHOICE-PARA.

display " "
display "Select sequence :"
display "(1) By name (2) By Country (3) By Type (0) Quit routine"
accept SequenceFlag

Evaluate true
  when Old-SequenceFlag = SequenceFlag
       display "*** Already in sequence you requested ***"
  when ValidSequence
       move zeroes to Kounter
etc..........

Note that when I have finished doing the callback which displays the
re-sorted list I then move SequenceFlag to Old-SequenceFlag.

>
>
…[24 more quoted lines elided]…
>

Some have a tendency to 'bracket' the conditions - and I think that's a good
idea for clarity :-

        IF      ( TABLE-LOAD-REQD)  AND
                  ( TABLE-STATUS  =  '00')
                    etc.,,,,,,

Just my $0.02

Jimmy, Calgary AB
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-13T11:50:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E70E0F1.45868E9D@attglobal.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3E6FD423.3F821009@shaw.ca>`

```


"James J. Gavan" wrote:

>
>
…[40 more quoted lines elided]…
> Jimmy, Calgary AB

I'm sorry, I cannot see any "clarity" gain by placing parentheses around a
condition-name or a simple condition, just because there is a logical connector
between them.  You can't fool the compiler, who won't mind either way of writing
it.  But I don't think this would help a human reader, either.

Even if a program coded the IF this way, it would still be my preference to put
the logical connector at the start of the line, to make it more visible.
Colin
```

#### ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-12T19:36:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303121936.4eb13406@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote in message news:<3E6FC7EC.8EF66036@attglobal.net>...
> Folks,
> You provided lots of great input when I posted a proposed COBOL
…[13 more quoted lines elided]…
> Here's the document:

... Snipped ...

Colin,

I really like the guide.  I like the fact that it is a GUIDE - the
TONE is excellent!!!  The REASONS for the specified suggestions were
plain, clear and logical.  I like the document a lot.
```

#### ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-13T04:45:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7005d6.243228562@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:

I'll restrict these comments to what I see wrong rather than missing. 

>2.Aligning procedural statements:
>
…[9 more quoted lines elided]…
>              END-IF

No, no. Goofy spacing doesn't make a program more readable.

>3.Using NOT:
>  If you've ever coded 'NOT >' or 'NOT <' relational operators,
…[4 more quoted lines elided]…
>  have a hard time understanding the use of NOT.

It's true that humans have a hard time understanding NOT. We programmers who
understand Boolean algebra don't. Constructs such as <= contain an unnecessary
OR whereas not > is a single condition.  Please delete this paragraph. 

>7.Writing expressions:
>
…[23 more quoted lines elided]…
>                           )

Forget the 'rules of COBOL'. Parentheses should always be written when a
statement contains a mixture of AND and OR, or +/- and multiply or divide.

Robert
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-13T06:04:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303130604.3eb4e5d6@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net>`

```
Comments on the comments below...

robert@wagner.net (Robert Wagner) wrote in message news:<3e7005d6.243228562@news.optonline.net>...
> Colin Campbell <cmcampb@attglobal.net> wrote:
> 
…[16 more quoted lines elided]…
> 

But it sure makes it more editable, and helps automated conversion
tools extend the life of the program, especially if the alignment
rules are strictly followed.  I had the great pleasure of converting a
customers system from Realia to Fujitsu COBOL and since he religiously
followed rules like this a majority of the conversion was automated
via a conversion program.  I don't PERSONALLY follow this style, but I
don't see anything at all wrong with it.

> >3.Using NOT:
> >  If you've ever coded 'NOT >' or 'NOT <' relational operators,
…[9 more quoted lines elided]…
> 

I'm one of the people who says "don't be afraid of negative logic",
but some otherwise quite capable and talented programmers do seem to
have trouble.  Could be because of the symbolic logic course I took a
long time ago, but overall from a maintenance standpoint I think the
original advice is excellent.

> >7.Writing expressions:
> >
…[26 more quoted lines elided]…
> statement contains a mixture of AND and OR, or +/- and multiply or divide.

<Sarcasm>There's some good advice for a COBOL programmer.  </Sarcasm>
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-14T03:54:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e713fe0.323635175@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <bfdfc3e8.0303130604.3eb4e5d6@posting.google.com>`

```
haneh@softwaresimple.com (Thane Hubbell) wrote:

>> No, no. Goofy spacing doesn't make a program more readable.
>
…[6 more quoted lines elided]…
>don't see anything at all wrong with it.

We don't program to make conversion easier; we program to make maintenance
easier . 

>> Forget the 'rules of COBOL'. Parentheses should always be written when a
>> statement contains a mixture of AND and OR, or +/- and multiply or divide.
>
><Sarcasm>There's some good advice for a COBOL programmer.  </Sarcasm>

I deliberately inserted a logic error to see whether anyone would catch it.
Nobody did. If they don't catch it here, they won't in source programs either.
The statement should have read: 

 when a statement contains a mixture of (AND and OR) or (+/- and (multiply or
divide))
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-15T13:00:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303151300.1fd019fa@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <bfdfc3e8.0303130604.3eb4e5d6@posting.google.com> <3e713fe0.323635175@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e713fe0.323635175@news.optonline.net>...
> haneh@softwaresimple.com (Thane Hubbell) wrote:
> 
…[13 more quoted lines elided]…
>

Conversion is maintenance.
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-13T16:14:41
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e709310_1@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net>`

```
Robert/Colin,

I simply haven't had time to read the whole Guide, however I have quickly
browsed the responses.

I agree with Thane that the TONE is right.

30 years ago I had to formulate exactly such a guide for a COBOL shop in New
Zealand. (I still have a copy of it somewhere in the attic <G>...was so
proud of it I kept it). I remember that then as now, the secret is to
ENCOURAGE programmers (rather than COERCE them) into agreeing a consistent
coding style.

Colin's document, in its introduction, does this.

Programmers are usually intelligent people who don't react well to words
like "MANDATORY" "REQUIRED" or "YOU WILL DO THIS".

In hindsight ,with broader and longer experience, having seen many flame
wars over style, I have a much more relaxed attitude now than I had even
then. But I can afford that indulgence; most corporate shops can't. We do
need standards and gudelines for consistency, but we need to be open minded
and gentle in enforcing them.

I have to say that I also endorse 100% Robert's comments  on points 3 and 7
below. (I don't really care about "goofy spacing"...)

I too am from the school where programmers were required to learn Logic, and
Boolean Algebra and Propositional Calculus are both very dear to my heart
(as previous posts here have demonstrated.)

There is nothing difficult about learning the proper Boolean use of
Negation, and a single day is more than enough for any programmer who wants
to learn the basics of  AND, OR, NOT, De Morgan's Laws (which many old hands
learn by bitter experience without even knowing they learned it <G>) and the
use of Boolean simplification to take the knots out of complex conditions
and nested IFs. I have run such courses in-house on countless occasions. If
anyone here is interested in a tutorial or would like more on this, simply
indicate your interest and I'll gladly provide it.

I think it would be a pity to see NOT being banned in relational conditions
because it is considered by "humans" <G> to simply be a means of saying
"greater than or equal to" or "less than or equal to" or "unequal to"...

For the same reason, I hate to see flags being set to "Y" or "N" when 1
indicates TRUE and 0 indicates FALSE. (I hate it even more when certain
languages corrupt this pure concept into letting a negative value indicate
FALSE, just because it is easier to implement on certain hardware...). But
that's just me, and those are simply MY preferences. I don't think it is
RIGHT or WRONG to set flags to "Y" or "N" (as Paul Simon says, "...I have no
opinion about that...").

Pete.

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e7005d6.243228562@news.optonline.net...
> Colin Campbell <cmcampb@attglobal.net> wrote:
>
…[25 more quoted lines elided]…
> It's true that humans have a hard time understanding NOT. We programmers
who
> understand Boolean algebra don't. Constructs such as <= contain an
unnecessary
> OR whereas not > is a single condition.  Please delete this paragraph.
>
…[30 more quoted lines elided]…
> Robert




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-14T03:54:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e71366b.321213406@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>I remember that then as now, the secret is to
>ENCOURAGE programmers (rather than COERCE them) into agreeing a consistent
>coding style.

The shops I managed for 20+ years had no published programming standards. Yet
style was so standardized that you couldn't tell from reading code who wrote it.
I accomplished it through social pressure (pride) and deliberately assigning
maintenance to someone other than the original author. They knew the code they
wrote today would need to be understood and modified by a cohort tomorrow. 

>Colin's document, in its introduction, does this.
>
>Programmers are usually intelligent people who don't react well to words
>like "MANDATORY" "REQUIRED" or "YOU WILL DO THIS".

That's ok if the Standards author knows what he's talking about, and
substantiates strictures with examples. If he doesn't, we'll find ways around
the Standard. 

>In hindsight ,with broader and longer experience, having seen many flame
>wars over style, I have a much more relaxed attitude now than I had even
>then. But I can afford that indulgence; most corporate shops can't. We do
>need standards and gudelines for consistency, but we need to be open minded
>and gentle in enforcing them.

Mainframe shops are seldom 'gentle in enforcing them'. 

>There is nothing difficult about learning the proper Boolean use of
>Negation, and a single day is more than enough for any programmer who wants
…[5 more quoted lines elided]…
>indicate your interest and I'll gladly provide it.

I wrote one in Best Practices. Nobody commented on it. 

>I think it would be a pity to see NOT being banned in relational conditions
>because it is considered by "humans" <G> to simply be a means of saying
>"greater than or equal to" or "less than or equal to" or "unequal to"...

Computer: a machine not as intelligent as a human being but more intelligent
than a programmer.  :)

>For the same reason, I hate to see flags being set to "Y" or "N" when 1
>indicates TRUE and 0 indicates FALSE. (I hate it even more when certain
…[4 more quoted lines elided]…
>opinion about that...").

I use flags extensively. I always use low-value as false. True value may be 'y'
or may be a letter representing the proposition. It is never 1.  I don't see
what difference it makes.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-14T12:38:32
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e71b1e6_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e71366b.321213406@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> I use flags extensively. I always use low-value as false. True value may
be 'y'
> or may be a letter representing the proposition. It is never 1.  I don't
see
> what difference it makes.
>
The difference is that 1 represents the multiplicative identity  and 0
represents the additive identity in ANY algebra. In a Boolean Algebra,  the
multiplicative identity represents universal truth; and the additive
identity represents the negation of this.

Like I said, these are preferences... it really doesn't matter.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-14T13:36:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com>`

```
On Fri, 14 Mar 2003 12:38:32 -0000, "Peter E.C. Dashwood"
<dashwood@enternet.co.nz> enlightened us:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[17 more quoted lines elided]…
>

Also the actual value of the literal low-value is not the same on
every system.  Therefore its use may not be portable or make sense.
Much better to use 0 (zero) = off; 1 = on; or y = yes or on; n = no or
off; all of which are portable and readable.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #109

Program aborting:
Close all that you have worked on.
You ask far too much.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T01:56:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e728355.406452311@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Fri, 14 Mar 2003 12:38:32 -0000, "Peter E.C. Dashwood"
><dashwood@enternet.co.nz> enlightened us:
…[25 more quoted lines elided]…
>off; all of which are portable and readable.

Name one system where low-values is other than binary zeros.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-15T00:22:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v75df0ckqdne48@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e728355.406452311@news.optonline.net...
[snip]
> Name one system where low-values is other than binary zeros.

LOW-VALUE depends upon the native character set
only by default. LOW-VALUE is defined as the lowest
value in the PROGRAM COLLATING SEQUENCE.
Different programs running together on the same
machine may have different characters for LOW-VALUE.

If you understood the "Rules of COBOL" you might have
known that.

The program below displays '048' as the LOW-VALUE
character from the subprogram. Note the directives
for checking conformance to ANS 85 COBOL.

      $set ans85 flag"ans85" flagas"S"
       identification division.
       program-id. hex-test.
       data division.
       working-storage section.
       77 hex-low-value pic x.
       77 value-of-hex-low-value pic 9(3).
       procedure division.
       begin.
           call "hex-low"
               using hex-low-value
           compute value-of-hex-low-value =
               function ord (hex-low-value) - 1
           display value-of-hex-low-value
           stop run.
       end program hex-test.

       identification division.
       program-id. hex-low.
       environment division.
       configuration section.
       source-computer. PC-DOS.
       object-computer. PC-DOS
           program collating sequence is hex.
       special-names.
           alphabet hex is
               "0" "1" "2" "3" "4"
               "5" "6" "7" "8" "9"
               "a" also "A" "b" also "B"
               "c" also "C" "d" also "D"
               "e" also "E" "f" also "F".
       data division.
       working-storage section.
       linkage section.
       77 hex-low-value pic x.
       procedure division
           using hex-low-value.
       begin.
           move low-value to hex-low-value
           exit program.
       end program hex-low.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T11:21:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e72ff00.438115975@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
>news:3e728355.406452311@news.optonline.net...
>[snip]
>> Name one system where low-values is other than binary zeros.

I wonder why people go to such extraordinary lengths. Because they feel
threatened? 

I earlier cited Burroughs Medium Systems, where the default was the lowest
character in the 'program collating sequence', to wit: a space. Thankfully,
Burroughs expired into Unisys. Chuck Stevens confirms that current Unisys
compilers produce x'00' for low-values and x'FF' for high-values, as do all
other compilers excepting the code below. 


>LOW-VALUE depends upon the native character set
>only by default. LOW-VALUE is defined as the lowest
…[54 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-15T15:24:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v7728rteo51p71@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e72ff00.438115975@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[7 more quoted lines elided]…
> threatened?

I don't know who 'they' are; but I don't feel theatened. I am
interested in correcting your misunderstanding and
misrepresentation of the rules of COBOL.

Your statement was flawed because there is no direct
relationship between the use of LOW-VALUES and the
storage of a particular value in the memory of the computer.

Furthermore, your suggestion to use LOW-VALUES in a
situation (representation of logic state) where a unique value
is required is flawed because LOW-VALUES, by definition,
is not unique. At the very least, LOW-VALUES will match one
other character, a character that is unique within the character
set. Then, because LOW-VALUES is not unique, it is
guaranteed to introduce logic errors when, for some program
collating sequence, LOW-VALUES, representing one logic
state, and a unique character, representing another logic state,
have the same value. Therefore, your recommendation is not
portable and is not "best practice."

> I earlier cited Burroughs Medium Systems, where the default was the lowest
> character in the 'program collating sequence', to wit: a space.
Thankfully,
> Burroughs expired into Unisys. Chuck Stevens confirms that current Unisys
> compilers produce x'00' for low-values and x'FF' for high-values, as do
all
> other compilers excepting the code below.

[code snipped]

Are you saying that you knew you were wrong but made
your flawed statement anyway?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T23:22:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73a68f.481017107@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>

>Furthermore, your suggestion to use LOW-VALUES in a
>situation (representation of logic state) where a unique value
…[8 more quoted lines elided]…
>portable and is not "best practice."

Kindly point out the logical flaw in this code. 

05  filler pic x value low-value.
     88  end-of-file value 'e' false low-value.

Do you seriously think some compiler will use 'e' as low-value?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-15T23:39:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v77vapbe05vd29@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e73a68f.481017107@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[19 more quoted lines elided]…
> Do you seriously think some compiler will use 'e' as low-value?

It is the *program*, not the compiler, that determines the
*program* collating sequence. If the *programmer* sets the
alphabet for the *program* collating sequence, such that
'e' is the first character in the collating sequence, then every
conforming compiler will use 'e' as low-value. Whenever 'e'
is the first character in the *program* collating sequence,
the code, above, will treat 'end-of-file' as always true.

Note that flagging is OFF due to use of the non-standard
'SET condition TO FALSE'.

      *set ans85 flag"ans85" flagas"S"
       identification division.
       program-id. lv-test.
       environment division.
       configuration section.
       source-computer. PC-DOS.
       object-computer. PC-DOS
           program collating sequence is e-start.
       special-names.
           alphabet e-start is
               "efgop930".
       data division.
       working-storage section.
       77 filler pic x value low-value.
         88 end-of-file value "e" false low-value.
       procedure division.
       begin.
           perform display-state
           set end-of-file to true
           perform display-state
           set end-of-file to false
           perform display-state
           stop run.
       display-state.
           if end-of-file
               display "True"
           else
               display "False"
           end-if.
       end program lv-test.

The program displays "True" three times.

The general rule you suggest is to use LOW-VALUE as
'False' and as the default value for the field and some other
character for the 'True' value. It is not just that 'e' could result
in failure; but that any character value could result in failure
for a particular collating sequence.

It is not the use of 'e' in particular, that is the problem. It is
the reliance upon LOW-VALUE as never being equivalent
to any other character that is the problem.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T07:37:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e742223.512658577@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[76 more quoted lines elided]…
>to any other character that is the problem.

In all my years of programming, I've never seen anyone use 'collating sequence
is'. You just pulled that up for the sake of debate. 

I'm concerned with Practice in the real world. Diluting Practice with such
hypotheticals does a disservice to struggling programmers.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-16T09:39:50
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e742b05_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net>`

```
Robert,

this response is completely unworthy of you.

"In all my years ...I've never seen..." is no form of real argument.

I wouldn't mind betting I've had more years than  you (36 in COBOL;38 in
programming) and I've never seen Collating Sequence used either.

But the point is that it COULD be.

People are not presenting these arguments just to make you wrong.

It's because they are valid arguments.

I shouldn't think anyone really cares whether you use low values to
represent FALSE or not (I certainly don't), but if you're going to have
debate, then expect people to present cases.

You are smart enough to recognise a good case when you see it, and to adopt
the approach that it is an obscure oddity, being presented to make you
wrong, is simply selling yourself short.

You can do much better than this. Would it be so painful to accept that this
is a valid point and acknowledge it?

Or is your whole time here to be about making yourself right?

Think on't...

Pete.

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e742223.512658577@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[80 more quoted lines elided]…
> In all my years of programming, I've never seen anyone use 'collating
sequence
> is'. You just pulled that up for the sake of debate.
>
> I'm concerned with Practice in the real world. Diluting Practice with such
> hypotheticals does a disservice to struggling programmers.
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-03-16T13:58:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bq%ca.1357$we1.525415@newssrv26.news.prodigy.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3e742b05_2@text-west.newsgroups.com...
> Robert,
>
…[7 more quoted lines elided]…
> But the point is that it COULD be.

Pete, I shocked.  Of course it could be, but it's immaterial.. because once
the program has been compiled, the value of LOW-VALUE is locked into the
program... you cannot change the COLLATING SEQUENCE of a compiled program.
(This may not be true of a p-code compiler; but let's forget they exist for
a moment).

OTOH, if the programmer used LOW-VALUE here then tested ZEROES there, then
the program is not source-code compatible; not that ANYONE would EVER
recompile a program on a new machine/with a new compiler/new version of a
compiler/adding a COLLATING SEQUENCE clause to an FD without thoroughly
testing every piece of logic in the code.

Would they?

MCM
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T17:56:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74ba67.23834107@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>I wouldn't mind betting I've had more years than  you (36 in COBOL;38 in
>programming) and I've never seen Collating Sequence used either.

You'd lose the bet. 

>this response is completely unworthy of you.
>
…[4 more quoted lines elided]…
>People are not presenting these arguments just to make you wrong.

I think they are. They are constructing improbable cases to rebut my points
about realistic use of COBOL. For instance, an alphabet beginning with 'e'. 

>It's because they are valid arguments.
>
>I shouldn't think anyone really cares whether you use low values to
>represent FALSE or not (I certainly don't), but if you're going to have
>debate, then expect people to present cases.

This isn't an ivory tower debate forum. It's a place where people come for
practical advice. They will leave if they see crotchety old men quibbling over
minutiae.

>You are smart enough to recognise a good case when you see it, and to adopt
>the approach that it is an obscure oddity, being presented to make you
>wrong, is simply selling yourself short.

I get it -- you're the 'good cop' playing against Richard's 'bad cop'.

>You can do much better than this. Would it be so painful to accept that this
>is a valid point and acknowledge it?

Fine. It's a valid hypothetical point. 

>Or is your whole time here to be about making yourself right?

I've admitted to being wrong several times here.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-16T16:12:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v79pf26jvnqvb7@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e74ba67.23834107@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
[snip]
> >People are not presenting these arguments just to make you wrong.
>
> I think they are. They are constructing improbable cases to rebut my
points
> about realistic use of COBOL. For instance, an alphabet beginning with
'e'.

A portable subprogram translating character commands
to numeric values might need to translate 'e' also 'E' to the
value 1. In this case, an alphabet beginning with 'e' would
mean that the expression 'FUNCTION ORD (command-char)'
would return 1 whenever command-char is 'e' or 'E'.
LOW-VALUE would be 'e'.

Such a program may not have a state variable unless
a command sequence needs special translation.

01 filler value low-value.
  88 end-command-received value 'e' false low-value.

In which case, the program has a logic error.

And yes, I made this up just to demonstrate that there are
practical, realistic cases, even if unlikely, that will result in
failure if your methods are used. I can do this easily because
I understand the flaw.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-17T09:34:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e751995.48203421@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[28 more quoted lines elided]…
>I understand the flaw.

In the domain of science, you'd be a theoritician and I'd be an experimenter.
Experimenters are not necessarily stupid (cf. Madame Wu), we're just more
practical-minded. 

This a role reversal. In real life, I'm usually the abstract thinker resented by
operations people and mediocre programmers. 

I don't harbor any anger. You blind-sided me with 'collating sequence', which is
fine in this little debating society. In the real world, low-values still means
x'00' 99.999% of the time. 

WMK thinks english-speakers are parochial. How many languages does he speak
fluently?

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 17)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-18T07:23:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b557he$lo8$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net>`

```
Robert Wagner wrote:

> In the domain of science, you'd be a theoritician and I'd be an
> experimenter. Experimenters are not necessarily stupid (cf. Madame Wu),
> we're just more practical-minded.

I suspect that you see yourself quite differently than everyone else.

For example Cobol is deterministic, there is no need for you to 
'experiment', the answers already exist.

Then again, given the examples you have posted where you have looked at (I 
deliberately refrain from using 'read') the standard, then perhaps you have 
decades where your code hasn't matched your expectations.

You've never accepted that it could be your expectations that were flawed, 
so you set yourself up as being an 'experimenter', finding ways that 
'work', and discarding things that you never understood.

> This a role reversal. In real life, I'm usually the abstract thinker
> resented by operations people and mediocre programmers.

Are you sure that they resent you because you are am 'abstarct thinker' ? 
Given your time here I would say that it is because you are arrogant in 
your assertions that are simply wrong, and you just stonewall until either 
they tell you to fuck off, or they just stop talking to you.

Either way counts as a 'win' in your arrogant way.

Do you know the difference between ignorence and stupidity ?  - One can be 
cured.

I also suspect that your 'mediocre programmers' consists of everyone who 
doesn't agree with you.

> I don't harbor any anger. You blind-sided me with 'collating sequence',
> which is fine in this little debating society. In the real world,
> low-values still means x'00' 99.999% of the time.

Was the 99.999% of the time found from actual experiments throughout the 
'real world' ?  If you were _actually_ an experimenter, instead of claiming 
it in self-puffery, and as an excuse for failing to understand the subject, 
then you wouldn't make such extreme claims which are based on an almost 
complete _lack_ of actual evidence.
 
> WMK thinks english-speakers are parochial. 

Another of your one spot dog -> all logic failures.  I thought that he 
implied _you_singular_ were parochial.

But, of course, this doesn't penetrate into your ego.

> How many languages does he speak fluently?

He speaks Cobol fluently, while you stutter something that sometimes 
resembles it.
```

###### ↳ ↳ ↳ Huh ??? (was: What's Missing in a COBOL Style Guide?

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-17T15:02:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55d4b$e6j$1@slb0.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net> <b557he$lo8$1@aklobs.kc.net.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b557he$lo8$1@aklobs.kc.net.nz...
> Robert Wagner wrote:
>
<snip>
>
> > WMK thinks english-speakers are parochial.
>

I can't even guess which of my posts gave him this idea.  I assume that he
hoped I would never see this comment - so he was safe putting this concept
in my mouth.
```

###### ↳ ↳ ↳ Re: Huh ??? (was: What's Missing in a COBOL Style Guide?

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7678cc.38122974@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net> <b557he$lo8$1@aklobs.kc.net.nz> <b55d4b$e6j$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
>news:b557he$lo8$1@aklobs.kc.net.nz...
…[9 more quoted lines elided]…
>in my mouth.

I thought so because of your frequent references to double-byte characters and
non-Latin alphabets. 

It's not a biggie. Let it pass.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e768cca.43241859@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net> <b557he$lo8$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[7 more quoted lines elided]…
>'experiment', the answers already exist.

Facts already exist too. The experimenter's job is to find them. 

>You've never accepted that it could be your expectations that were flawed, 
>so you set yourself up as being an 'experimenter', finding ways that 
>'work', and discarding things that you never understood.

Gimme a break. I made an analogy to the roles of scientists, that's all. Don't
play amateur psychologist. 

>Are you sure that they resent you because you are am 'abstarct thinker' ? 
>Given your time here I would say that it is because you are arrogant in 
…[3 more quoted lines elided]…
>Either way counts as a 'win' in your arrogant way.

It does count as a win. If they cannot present cogent argumentation, they lose. 

This is the Big Pond. Socially-oriented techniques that worked in high school --
I like you, I don't like you -- don't cut it here. If you cannot present a
rational case, you lose. I really don't give a shit whether you like me. Just
rebut my arguments or remain silent. 

Forming an argument is simple. You start with premises, which can be facts or
conclusions from successful arguments. You glue them together with logic to form
a conclusion. That's how we synthesize knowledge. We don't do it by name
calling.

>I also suspect that your 'mediocre programmers' consists of everyone who 
>doesn't agree with you.

We all know their poor style because we've all worked on their code. 

>> I don't harbor any anger. You blind-sided me with 'collating sequence',
>> which is fine in this little debating society. In the real world,
…[6 more quoted lines elided]…
>complete _lack_ of actual evidence.

It is based on experience with millions of lines of production COBOL.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 19)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-18T01:31:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303180131.1ccbd4df@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net> <b557he$lo8$1@aklobs.kc.net.nz> <3e768cca.43241859@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >For example Cobol is deterministic, there is no need for you to 
> >'experiment', the answers already exist.
> 
> Facts already exist too. The experimenter's job is to find them. 

Try reading the manual.  You have been considerably misled by your
experiments where your conclusions failed to match how the language is
defined.
 
> >Either way counts as a 'win' in your arrogant way.
> 
> It does count as a win. If they cannot present cogent argumentation, they lose. 

But, it seems, you have defined 'cogent argument' as 'one that agrees
with you'.

Sometimes you eventually back down such as your 'no standard file
status for missing file', but only after you had rejected quotes from
the amnuals and standards several times.

In other arguments you completely ignore cogent arguments, such as
with 'INITIALIZE'. Will you claim a 'win' over this ?

> If you cannot present a rational case, you lose.

The definition of what Cobol _is_, isn't a debate as you try to make
it.

> Just rebut my arguments or remain silent. 

No. That has been shown to not be sufficient. You only 'accept' what
agrees with you, you just plough on with your misinformation.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T17:44:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e775283.93866179@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net> <b557he$lo8$1@aklobs.kc.net.nz> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>Try reading the manual.  You have been considerably misled by your
>experiments where your conclusions failed to match how the language is
>defined.

Noplace in the Fujitsu manual does it say one can use IBM/Micro Focus syntax for
pointers. Experimentation revealed that fact.

What would you have us do when the manual contradicts itself? Tell somebody? I
tried twice and got flamage in return. 

>Sometimes you eventually back down such as your 'no standard file
>status for missing file', but only after you had rejected quotes from
>the manuals and standards several times.

I cited a Fujitsu support page that agreed with me. 

>In other arguments you completely ignore cogent arguments, such as
>with 'INITIALIZE'. Will you claim a 'win' over this ?

Difference of opinion. 

>The definition of what Cobol _is_, isn't a debate as you try to make
>it.

If you are referring to INITIALIZE, I began by saying I don't use it because it
does not clear fillers and pointers. That's not disputing how it works.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 21)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-19T07:26:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57s0k$qdb$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net>`

```
Robert Wagner wrote:

> If you are referring to INITIALIZE, I began by saying I don't use it
> because it does not clear fillers and pointers. That's not disputing how
> it works.

No you didn't. You claimed it was 'wrong' and then disputed how it worked 
by claiming that they should 'fix' it:

""Yes, it is wrong. It doesn't initialize FILLERs nor pointers.""

""But lacking an initial value, it should restore pointers to null andf 
illers to spaces (pic x)  or zeros (pic 9 display) or low-values (any other 
pic). ""

""'ll write 'move low-values to ...' until they get it right.""

You also misrepresented what WMK said, probably because you failed to 
understand what he actually said:

""WMK thinks INITIALIZE should restore initial values.""

And then showed that you completely failed to understand Thane's point with:

""that would address your objection.""

It wasn't an 'objection', it was an explanation, a clarification.

You claimed that you wanted to give newbies the benefit of your wisdom. 
What are you trying to teach them: 'to whine and complain' when they don't 
understand ?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77d770.16839616@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b57s0k$qdb$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[13 more quoted lines elided]…
>""'ll write 'move low-values to ...' until they get it right.""

The  original posting was what I said. The ones you quoted were followups in
which I got a little emotional. I was talking about how I thought it should work
rather than how I knew it actually worked. 

>You also misrepresented what WMK said, probably because you failed to 
>understand what he actually said:
>
>""WMK thinks INITIALIZE should restore initial values.""

He said that .. either here or in email. It is supported in 2002, but requires
additional syntax. I think it should be the default. 

>And then showed that you completely failed to understand Thane's point with:
>
>""that would address your objection.""
>
>It wasn't an 'objection', it was an explanation, a clarification.

It didn't address my objection. I want junk fillers, pointers and indicators
initialized. 

>You claimed that you wanted to give newbies the benefit of your wisdom. 
>What are you trying to teach them: 'to whine and complain' when they don't 
>understand ?

No, to stand up to cavilers like you.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 21)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-19T09:47:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b58496$ttb$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net>`

```
Robert Wagner wrote:

> Noplace in the Fujitsu manual does it say one can use IBM/Micro Focus
> syntax for pointers. Experimentation revealed that fact.

If it is not in the manual, or some other document, then there is no 
assurance that it is supported, or will work correctly.  If you found a bug 
and reported it they will simply tell you to rewrite to some supported 
syntax.

Other versions may not have the facility, or it may be broken.  When you 
suggest that it be used you may find that programmers are using versions 
that are not yours and they fail.
 
> What would you have us do when the manual contradicts itself? Tell
> somebody? I tried twice and got flamage in return.

Which manual was that ?  

When you asserted what should happen with bound checks on index your 
arguments were simply wrong (incorrect).  The reasons why you were wrong 
was explained carefully to you.

When you asserted that the standard had errors WNK took time to carefully 
explain how to read the document and work out why your argument was wrong.

When you fail to understand and keep making the same error then eventually 
you get told in firmer terms.

Of course, you probably count this as a 'win'.

>>Sometimes you eventually back down such as your 'no standard file
>>status for missing file', but only after you had rejected quotes from
>>the manuals and standards several times.
> 
> I cited a Fujitsu support page that agreed with me.

You certainly did not 'cite a support page that agreed with you'.  The 
Fujitsu support page clearly states that 'file not present' is a '85 
standard response.

That page was another that showed you to be wrong.

Are you continuing to claim that it 'agreed with you' ?
```

###### ↳ ↳ ↳ What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 22)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-18T16:29:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b586kl$2h1$1@slb4.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz>`

```
IBM (in the early '80s) introduced two terms that amused me then and still
do. They are/were:

  "Undocumented extension"
        versus
  "Undetected user error"

For any programmer that has done any conversions from IBM's older "OS/VS
COBOL" (or DOS/VS COBOL) to VS COBOL II or its follow-on products, this
distinction has proved a real "experience" not to be forgotten.  (And I
suggest that anyone relying on existing Fujitsu support for SET ADDRESS OF
learns from this PAINFUL migration.)

At one time in the 90's I tried to get J4 (the ANSI-ish Standards group) to
"deal" with this - as it ties into the requirements in the '85 Standard both
for documentation and flagging of "extensions".  The bottom-line (both from
J4's position *and* from my experiences in the real world) is that

"support for a feature in any specific COBOL implementation is EXACTLY as
much - or as little as the specific vendor says that it is"

In cases where the documentation and the software do not agree, one *MUST*
get explicit reconciliation from the vendor - in order to have any
expectation of support (in current and/or future products).  The vendor may
(and I have seen each of these with IBM, with Micro Focus, and with
Fujitsu):

 A) Say the documentation is correct and that relying on the software's
CURRENT behavior is unsupported.  Future releases and/or maintenance HAVE
removed or changed the feature.

 B) Say the software is correct and the documentation is in error (and they
have "promised" to fix the documentation)

 C) Say that both the software and the documentation are in error and
created "fixes" to both that didn't work the way that either "used to"

 D) Say that the software will PROBABLY continue to work as it does today,
but this is an unsupported interface.  Caveat Programmer!!!

   ***

I have NEVER (personally) been "flamed" by any vendor when reporting
discrepancies between their software and their documentation.  I do,
however, (and I suspect that I *completely* differ from "you-know-who" on
this) accept that it is the vendor - not me that has the final say on which
(if either) is correct. In cases where their final "decision" differs from
my understanding of existing ANSI/ISO Standards, I have (in some cases)
referred the question to the appropriate Standards group for a final
determination of whether this vendor is implementing a required feature
correctly.

Because Fujitsu has had (and I suspect still does have) such a "larger
target audience" of programmers moving code from IBM and Micro Focus
compilers, I would be SURPRISED if they (in the future) remove support for
the current

    Set ADDRESS OF

syntax that their software accepts, but that their documentation does not
include.  On the other hand, given that the 2002 Standard *does* introduce
(somewhat conflicting, i.e. use of BASED attribute - rather than Linkage
Section definitions) of items to which you can ASSIGN a new address, I can
easily see this feature NEVER being officially supported by Fujitsu.  I
would expect (but am not holding my breath) that Fujitsu will (eventually -
possibly after Micro Focus provides it) support the BASED attribute and SET
ADDRESS OF for such items - rather than the current BASED-Storage Section
and ADDR function.

Bottom-Line:
  He/she who relies on current UN-documented software support in a compiler
deserves what she/he gets.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T00:49:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77b35b.7601275@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:


>Because Fujitsu has had (and I suspect still does have) such a "larger
>target audience" of programmers moving code from IBM and Micro Focus
…[3 more quoted lines elided]…
>    Set ADDRESS OF

That's unlikely because it is in the 2002 standard. Look at 14.10.35, Format 7,
which says we can use it. Contrast that with 8.4.2.11.2.5, which says we cannot.


This is not a nit-picking 'typo' error. It reflects a fundamental conflict
between two schools of thought about pointer syntax. On the one hand we have
advocates of 'set address of', which I call 'COBOL-style'; on the other hand we
have supporters of 'based-', which I call 'C/Pascal style'. The standards people
or person who wrote documentation of SET supported the former while the people
who wrote 'address of' supported the latter. 

We'll get 'set address of' thanks to backward compatibility with 'vendor
extensions'. At any rate, the standard is internally discrepant. 

This is the third time I've pointed out the error. Why do you avoid addressing
it rather than answering with flammage?

> I can
>easily see this feature NEVER being officially supported by Fujitsu.  I
…[3 more quoted lines elided]…
>and ADDR function.

You wish, because you support the 'C/Pascal' convention.

>Bottom-Line:
>  He/she who relies on current UN-documented software support in a compiler
>deserves what she/he gets.

FUD. 

Robert
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 24)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-18T21:22:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v7fkcvfdqatlf5@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e77b35b.7601275@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[3 more quoted lines elided]…
> >compilers, I would be SURPRISED if they (in the future) remove support
for
> >the current
> >
> >    Set ADDRESS OF
>
> That's unlikely because it is in the 2002 standard. Look at 14.10.35,
Format 7,
> which says we can use it.

Look at syntax rule 18 for FORMAT 7.
"18) Data-name-1 shall be a based data item."

Which means that existing support is different than the standard,
which, if I understand correctly, is part of what Bill is saying.

> Contrast that with 8.4.2.11.2.5, which says we cannot.

"E.9.1 Data-addresses and data-pointers

A data-address is a conceptual entity identifying the location
of a data item. It is referenced by specifying a
data-address-identifier. A data-address-identifier cannot be
a receiving operand. Note that the ADDRESS OF phrase in
the receiving operand of a SET statement is not considered
a data-address-identifier, but a syntactical notation for setting
the address of a based item to the value specified by the
sending operand."

[snip]
> This is the third time I've pointed out the error.

I have not been following this issue because I do not currently
use Fujitsu; but If this does not clear up this issue, let me know
what is missing.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 25)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-18T23:52:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b590i7$9a2$1@slb3.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com>`

```
I don't see Robert's notes (Thank Goodness!!!), but as far as I know there
is no "error" in the 2002 Standard.

It is entirely possible to use

   Set ADDRESS OF Based-Data-item TO pointer-data-item

It is totally impossible (and not included anywhere) to do (as IBM and Micro
Focus document as extensions to the '85 Standard)

   Set ADDRESS OF Linkage-Section-item TO pointer-data-item

The "ADDRESS OF" part of a Format 7 Set statement has NOTHING to do with the
data-address-identifier which also has
   "ADDRESS OF" in its syntax.

A data-address-identifier explicitly may NOT be a receiving item (via Move,
Set, or any other statement)

The "address of" in a Format 7 Set statement *must* be followed by the name
of a data item with the BASED phrase (similar to - but not quite identical
to the existing Fujitsu Based-Storage Section extension).  Neither IBM nor
Micro Focus currently have any way (section or phrase) that I am aware of
for identifying an item as "BASED"  - therefore, there is no "overlap"
between existing IBM and Micro Focus (and undocumented Fujitsu) syntax and
the Format 7 Set statement of the 2002 Standard - when it comes to
"assigning" an address to a field.  IBM, Micro Focus, and (undocumented for
Fujitsu) do currently support the same syntax for assigning the existing
address of a data item to a data-pointer item.

  ***

If Mr. Wagner does respond to this note and actually does provide any
indication of a REAL error (not just his mis-reading) - of the 2002
Standard:

A) I hope someone responds to his note, so I will see it

B) He should submit it directly to J4 as a "defect report".   Anyone may
submit such a report to J4.  It is true that if they don't understand what
the 2002 Standard actually SAYS, they may get back a "RTFM" type answer, but
I can't see that stopping certain people. <G>
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-20T01:31:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e78f7f6.28054222@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[33 more quoted lines elided]…
>sending operand."

I didn't read far enough. I saw "SET ADDRESS OF .."  and thought it meant what
it said. The above makes a distinction between "syntactical notation" and
grammar. Silly me, I thought grammar was nothing but lexicon and syntax. (What
do you expect from a high-school dropout?) The committee would have us believe
there is an unnamed third dimension which gives meaning to the distinction
between "syntactical notation" and 'language definition'. Linguistics scholars
and students would applaud the revelation .. if only they could figure out what
it is. 

Sarcasm aside, thank you for the informative and noninflammatory reply. It's a
breath of fresh air in this newsgroup. You answered my question/complaint.

Robert
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 26)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-20T01:39:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v7insvfn4je22e@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e78f7f6.28054222@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
[snip]
> >"E.9.1 Data-addresses and data-pointers
> >
…[9 more quoted lines elided]…
> I didn't read far enough. I saw "SET ADDRESS OF .."  and thought it meant
what
> it said. The above makes a distinction between "syntactical notation" and
> grammar. Silly me, I thought grammar was nothing but lexicon and syntax.
(What
> do you expect from a high-school dropout?) The committee would have us
believe
> there is an unnamed third dimension which gives meaning to the distinction
> between "syntactical notation" and 'language definition'. Linguistics
scholars
> and students would applaud the revelation .. if only they could figure out
what
> it is.
>
> Sarcasm aside, thank you for the informative and noninflammatory reply.
It's a
> breath of fresh air in this newsgroup. You answered my question/complaint.

ADDRESS OF, wherever it appears *is* syntax. Consider,

   SET ADDRESS OF record-2 TO ADDRESS OF record-1

The first ADDRESS OF is syntax for SET statement, format 7.
The second is syntax for a data-address-identifier.

This is useful because a data-address-identifier may be used
in other statements, for example, the USING phrase of CALL
or INVOKE, as in USING ADDRESS OF record-1. It reduces
the complexity of syntax formats by reusing 'syntactical notation'
within the 'language definition' (if I understood you correctly), thus
easing the implementers task; but it increases the difficulty of
understanding what the programmer may write. This is in keeping
with the goal that the standard is a specification for the COBOL
language, not a language reference for programmers.

Thus the committee (J4) succeeds when the COBOL standard,
as a specification, is clear and unambiguous. This is true
eventhough the document is complex and difficult to follow.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-20T11:37:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303201137.33b9f860@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote

> The first ADDRESS OF is syntax for SET statement, format 7.
> The second is syntax for a data-address-identifier.

A distinction that seems to serve the same function that C does with
lvalue and rvalue.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-20T18:59:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v7kkofivvcmc1f@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <217e491a.0303201137.33b9f860@posting.google.com>`

```

Richard <riplin@Azonic.co.nz> wrote in message
news:217e491a.0303201137.33b9f860@posting.google.com...
> "Rick Smith" <ricksmith@mfi.net> wrote
>
…[4 more quoted lines elided]…
> lvalue and rvalue.

The implementation of based (or other dynamically
allocated) items in COBOL is unlike other languages,
including PL/I from which it was apparently "lifted".

Every based item in COBOL has an implicit data address
pointer that holds the current address of the based item,
that the pointer is implicit tests our preception of
ADDRESS OF.

For non-based items, ADDRESS OF, as an rvalue, is the
actual storage address of the item. lvalue does not apply.
This is our normal perception.

For based items, ADDRESS OF, as an rvalue, is the content
of the implicit data address pointer for the based item.

For based items, ADDRESS OF, as an lvalue, is the address
of the implicit data address pointer that is to receive the new
address of the based item. In other words, for SET statement,
format 7, ADDRESS OF is actually the *address of* the
*address of* the based item.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-21T01:08:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7a6382.121136933@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <217e491a.0303201137.33b9f860@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>"Rick Smith" <ricksmith@mfi.net> wrote
>
…[4 more quoted lines elided]…
>lvalue and rvalue.

If the COBOL compiler were OO, ADDRESS OF would be in class COBOL.AmbiguousName
which would look at _context_. If the context was receiving field (lvalue), it
would override the ADDRESS OF method to operate on a BASED DATA-POINTER; if the
context was sending (rvalue), it would invoke the default method to return a
data-address-identifier. In the latter case, if the source is BASED, reference
would be to the same DATA-POINTER but without an explicit override (too late
once you're into the method). 

I'm not comfortable with having two methods return the same output. It would be
more reliable if both cases routed through a single method. How to accomplish
that? The AmbiguousName guy uses syntax to disambiguate (but incompletely)
whereas the default ADDRESS OF guy uses lexicon. 

C++ cannot deal with the dilemma. It makes the programmer resolve it by
prefixing the variable name with & or * to designate rvalue, and nothing to
designate lvalue. Neophyte programmers have a hard time understanding the
difference between the three. The three notations were invented to benefit
compilers and language designers who couldn't come up with a solution, not to
benefit programmers. 

IMHO, a well-designed language like COBOL should be designed for programmer
understanding rather than compiler convenience. The 2002 standard does that 2/3
of the way by allowing us to write SET ADDRESS OF, but it waffles by requiring a
BASED pointer and the internal ugliness of two methods (hopefully) duplicating
each other's logic. I would hope there is a cleaner solution. 

Robert
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T16:07:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea16766.61476936@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>Robert Wagner <robert@wagner.net> wrote in message
>news:3e78f7f6.28054222@news.optonline.net...
…[50 more quoted lines elided]…
>eventhough the document is complex and difficult to follow.

The only difference between the two forms of ADDRESS OF would be a statement
where the pointer was a receiving operand -- something like MOVE ADDRESS OF
record-1 TO ADDRESS OF record-2. But that statement is invalid in the standard.
Also invalid is:

 CALL 'a-program' USING ADDRESS OF record-2, record-1

One must say BY CONTENT ADDRESS OF record-2, which is the same as USING
record-2. The reason for the prohibition of passing pointers BY REFERENCE is not
syntactic simplicity, it is to protect them from modification outside the SET
verb.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-19T14:21:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va35257evgc5e0@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ea16766.61476936@news.optonline.net...
[snip]
> Also invalid is:
>
…[3 more quoted lines elided]…
> record-2.

Assuming that record-2 describes a group item defined in
the file, working-storage, local-storage, linkage, or
communication section of a program, the following applies.

The CALL statement, Format 2, specifies that operands in the
USING phase, whether BY REFERENCE or BY CONTENT,
are described as identifier-2. [FDIS page 420]

The CALL statement, Syntax rules, futher state that identifier-2
"shall reference an address-identifier or a data item defined ...".
[FDIS page 421]

Identifiers, Format 9, describes an address-identifier as
data-address-identifier-1 or program-address identifier-1.
[FDIS page 88]

Data-address-identifier is described as ADDRESS OF identifier-1
and "shall reference a data item defined ..." and "creates a unique
data item of class pointer and category data-pointer that contains
the address of ...". [FDIS page 99]

Also, some restrictions apply in some cases; but not this general
case.

The conformance rules for parameters states "If either the
argument or the formal parameter is of class pointer, the
corresponding formal parameter or argument shall be of class
pointer and the corresponding items shall be of the same
category." [FDIS page 405]

Thus, whether passed by reference or content, ADDRESS OF
record-2 will cause the argument to be passed as a data-pointer
containing the address of record-2, and the corresponding
parameter in the called program must be described as USAGE
POINTER.

This is as I understand it.

> The reason for the prohibition of passing pointers BY REFERENCE is not
> syntactic simplicity, it is to protect them from modification outside the
SET
> verb.

Since the prohibition does not exist, your speculation is
not applicable.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-19T16:11:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va3bujgtgr7f0f@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com>`

```

Rick Smith <ricksmith@mfi.net> wrote in message
news:va35257evgc5e0@corp.supernews.com...
>
> Robert Wagner <robert@wagner.net> wrote in message
…[7 more quoted lines elided]…
> > record-2.

[snipped long description]

Or, I could have shown that one need not say BY CONTENT
by supplying the example from Annex E.9.1, Data-addresses
and data-pointers. [FDIS pages 745-746]

--- example
Consider a second example based on the fact that many Application
Program Interfaces (APIs) require a pointer as a parameter. The data
division contains the following declarations:

  01 p2 usage pointer.
  01 data-record. >* the full record layout is described
    02 ...

If you want to pass a pointer to the program process-record, you could
code:

  Set p2 to address of data-record
  Call "process-record" using p2

Or, you could pass the address of data-record with the following single
statement:

  Call "process-record" using address of data-record
--- end example
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-20T00:44:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea1e804.94408627@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <va3bujgtgr7f0f@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Rick Smith <ricksmith@mfi.net> wrote in message
…[37 more quoted lines elided]…
>--- end example

Both examples will pass a pointer to a pointer, not a pointer to a record. 
They should have said Call "process-record" using data-record.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 31)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-19T22:36:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va4238qa5miqd6@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <va3bujgtgr7f0f@corp.supernews.com> <3ea1e804.94408627@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ea1e804.94408627@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[11 more quoted lines elided]…
> >> > One must say BY CONTENT ADDRESS OF record-2, which is the same as
USING
> >> > record-2.
> >
…[28 more quoted lines elided]…
> They should have said Call "process-record" using data-record.

There is a 'strangeness', as I recall, from an old discussion,
that, in standard COBOL, items passed BY REFERENCE
are not passed as addresses or pointers. Keep in mind that
this is in standard COBOL; not necessarily its implementation.

If I recalled correctly,
    call "process-record" using data-record
means that the standard only requires that a reference to
data-record be passed; not its address. For many(?)
implementations, there is no difference. However, the COBOL
standard needs to make a distinction for the purpose of
specifiying the language.

Thus, where you see "a pointer to a pointer", the standard
calls it a reference to a pointer and all the rules rely on what
the standard calls it! <g>
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 32)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-20T16:57:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea2bada.148390123@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <va3bujgtgr7f0f@corp.supernews.com> <3ea1e804.94408627@news.optonline.net> <va4238qa5miqd6@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[51 more quoted lines elided]…
>this is in standard COBOL; not necessarily its implementation.

In that case, programs written in other languages would not work. In the course
of writing assembly language on a variety of platforms, I've never seen COBOL
pass anything other than a pointer. 

>If I recalled correctly,
>    call "process-record" using data-record
…[8 more quoted lines elided]…
>the standard calls it! <g>

The standard says in Appendix C:

"A run unit may also contain runtime modules and data storage areas derived from
the compilation of compilation
units written in languages other than COBOL; in this case the requirements for
the relationship between the COBOL
and the non-COBOL modules are defined by the implementors."

I cannot imagine an implementation which did not support communication with
other languages, therefore parameter passing is, as a practical matter, always
defined by the implementor.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 33)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-20T15:19:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va5snv2th69i70@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <va3bujgtgr7f0f@corp.supernews.com> <3ea1e804.94408627@news.optonline.net> <va4238qa5miqd6@corp.supernews.com> <3ea2bada.148390123@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ea2bada.148390123@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
[snip]
> >There is a 'strangeness', as I recall, from an old discussion,
> >that, in standard COBOL, items passed BY REFERENCE
…[3 more quoted lines elided]…
> In that case, programs written in other languages would not work. In the
course
> of writing assembly language on a variety of platforms, I've never seen
COBOL
> pass anything other than a pointer.

In many of those cases, I have no doubt that extensions were
used to facilitate calling programs in those other languages.
The 2002 COBOL standard is the first to provide non-COBOL
language support.

> >If I recalled correctly,
> >    call "process-record" using data-record
…[12 more quoted lines elided]…
> "A run unit may also contain runtime modules and data storage areas
derived from
> the compilation of compilation
> units written in languages other than COBOL; in this case the requirements
for
> the relationship between the COBOL
> and the non-COBOL modules are defined by the implementors."
>
> I cannot imagine an implementation which did not support communication
with
> other languages, therefore parameter passing is, as a practical matter,
always
> defined by the implementor.

As a practical matter, the COBOL standard is incomplete.
It has a requirement for implementors to 'fill-in' certain items
that are "implementor defined." What the new standard does
accomplish is to make it easier for implementors to do such
things as support non-COBOL modules in a 'standard' way;
that is, one which requires fewer source code changes between
implementations.

One of these is the availability of ADDRESS OF, which, strictly
speaking, is not required for a single implementor, COBOL-only
solution.
```

###### ↳ ↳ ↳ Syntax error in standard? (was: Re: What is supported (was: What's Missing in a COBOL Style Guide?)

_(reply depth: 30)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-19T21:53:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va3vl890ob5c7c@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <va3bujgtgr7f0f@corp.supernews.com>`

```

Rick Smith <ricksmith@mfi.net> wrote in message
news:va3bujgtgr7f0f@corp.supernews.com...
[snip]
> Or, I could have shown that one need not say BY CONTENT
> by supplying the example from Annex E.9.1, Data-addresses
…[15 more quoted lines elided]…
>   Call "process-record" using p2

Bill, to add more confusion, see page 422, CALL, SR(11),
Formats 1 and 2.

"11) If the BY REFERENCE phrase is specified or implied
for an identifier-2, that identifier shall be neither a strongly-typed
group item nor a data item of class object or pointer."

The CALL statement appears to be passing a data item of
class pointer by reference. What am I missing?

>
> Or, you could pass the address of data-record with the following single
> statement:
>
>   Call "process-record" using address of data-record

Also ADDRESS OF data-record is an unique data item of
class pointer, again, passed by reference.

> --- end example
```

###### ↳ ↳ ↳ Re: Syntax error in standard? (was: Re: What is supported (was: What's Missing in a COBOL Style Guide?)

_(reply depth: 31)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-19T21:25:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7t0ea$m0u$1@slb6.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <va3bujgtgr7f0f@corp.supernews.com> <va3vl890ob5c7c@corp.supernews.com>`

```
SR(11) applies to Format 1 and 2 - not to Format 3 (which must have a
program-prototype). When there *is* a program-prototype, then there is no
restriction on indenter-2 being an address-identifier (I think).
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-19T16:23:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7seot$ten$1@slb2.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com>`

```
Rick,
   I think that I made the same mistake when I first started looking at
this.

GR(4) on page 421 states,

"4) If the BY REFERENCE phrase is not specified or implied for an
identifier-2 or if identifier-2 is an addressidentifier, identifier-2 is a
sending operand."

However, 14.5.7 Sending and receiving operands on page 389 says,

"An operand is a sending operand if its contents prior to the execution of a
statement may be used by the execution of the statement. An operand is a
receiving operand if its contents may be changed by the execution of the
statement."

I read this to mean that an "ADDRESS OF" data-pointer may be used in a CALL
BY REFERENCE (identifier-2) - but *only* if that data-item is *not* changed
by any action of the CALLed subprogram.

This seems a little "misleading" to me, but does (as far as I read it)
reflect the 2002 Standard.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-20T14:33:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va5q62ai9pqrf8@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <b7seot$ten$1@slb2.atl.mindspring.net>`

```
Bill,
I reviewed the FDIS and came to the conclusion that my
understanding is correct; that is, when an address-identifier
is identifier-2, it meets the requirements for all formats by way
of SR(4). When indentifer-2 is a pointer data item (not an
address-identifier), it is not allowed by SR(11) for formats 1 and 2
and only for BY REFERENCE.

I then wrote a set of programs to test the concept using the older
MF COBOL/2 3.2. My thinking is that it should have the same
behavior as the standard, even though the syntax is slightly
different. MF uses ENTRY for ADDRESS OF PROGRAM,
PROCEDURE-POINTER for PROGRAM-POINTER, and uses
the linkage section rather than BASED items.

The programs pass only the addresses of pointers on calls,
including both program (procedure) pointers and data pointers.

Note that where a prefix is 'adr-of-' the content is the address
of a pointer and must be understood as holding a pointer to
a pointer of either program or data of some type.

----- The test program
       program-id. main.
       data division.
       working-storage section.
       1 next-program procedure-pointer.
       1 next-data-ptr pointer.
       procedure division.
           set next-program to null
           set next-data-ptr to null
           perform until exit
               call "get-prog"
                   using address of next-program
                         address of next-data-ptr
               if next-program = null
                   exit perform
               end-if
               call next-program
                 using address of next-data-ptr
           end-perform
           stop run.
       end program main.

       program-id. get-prog.
       data division.
       working-storage section.
       1 current-program-number comp pic 9(4).
       66 random-value renames current-program-number.
       1 next-data.
        2 text-msg pic x(30).
       linkage section.
       1 adr-of-next-program pointer.
       1 adr-of-next-data-ptr pointer.
       1 next-program procedure-pointer.
       1 next-data-ptr pointer.
       procedure division
         using adr-of-next-program adr-of-next-data-ptr.
           set address of next-program to adr-of-next-program
           if next-program = null
               compute random-value =
                 function integer (
                   function random (
                     function numval (
                       function current-date (9:8))) * 6 ) + 1
               set address of next-data-ptr to adr-of-next-data-ptr
               set next-data-ptr to address of next-data
           else
               subtract 1 from current-program-number
           end-if
           evaluate current-program-number
             when 6
               set next-program to entry "prog-6"
               move "In program 6" to text-msg
             when 5
               set next-program to entry "prog-5"
               move "In program 5" to text-msg
             when 4
               set next-program to entry "prog-4"
               move "In program 4" to text-msg
             when 3
               set next-program to entry "prog-3"
               move "In program 3" to text-msg
             when 2
               set next-program to entry "prog-2"
               move "In program 2" to text-msg
             when 1
               set next-program to entry "prog-1"
               move "In program 1" to text-msg
             when other
               set next-program to null
               move "Done" to text-msg
           end-evaluate
           exit program.
       end program get-prog.

       program-id. prog-1.
       data division.
       linkage section.
       1 adr-of-next-data-ptr pointer.
       1 next-data-ptr pointer.
       1 next-data.
        2 text-msg pic x(30).
       procedure division using adr-of-next-data-ptr.
           set address of next-data-ptr to adr-of-next-data-ptr
           set address of next-data to next-data-ptr
           display text-msg
           exit program.
       end program prog-1.

       program-id. prog-2.
       data division.
       linkage section.
       1 adr-of-next-data-ptr pointer.
       1 next-data-ptr pointer.
       1 next-data.
        2 text-msg pic x(30).
       procedure division using adr-of-next-data-ptr.
           set address of next-data-ptr to adr-of-next-data-ptr
           set address of next-data to next-data-ptr
           display text-msg
           exit program.
       end program prog-2.

       program-id. prog-3.
       data division.
       linkage section.
       1 adr-of-next-data-ptr pointer.
       1 next-data-ptr pointer.
       1 next-data.
        2 text-msg pic x(30).
       procedure division using adr-of-next-data-ptr.
           set address of next-data-ptr to adr-of-next-data-ptr
           set address of next-data to next-data-ptr
           display text-msg
           exit program.
       end program prog-3.

       program-id. prog-4.
       data division.
       linkage section.
       1 adr-of-next-data-ptr pointer.
       1 next-data-ptr pointer.
       1 next-data.
        2 text-msg pic x(30).
       procedure division using adr-of-next-data-ptr.
           set address of next-data-ptr to adr-of-next-data-ptr
           set address of next-data to next-data-ptr
           display text-msg
           exit program.
       end program prog-4.

       program-id. prog-5.
       data division.
       linkage section.
       1 adr-of-next-data-ptr pointer.
       1 next-data-ptr pointer.
       1 next-data.
        2 text-msg pic x(30).
       procedure division using adr-of-next-data-ptr.
           set address of next-data-ptr to adr-of-next-data-ptr
           set address of next-data to next-data-ptr
           display text-msg
           exit program.
       end program prog-5.

       program-id. prog-6.
       data division.
       linkage section.
       1 adr-of-next-data-ptr pointer.
       1 next-data-ptr pointer.
       1 next-data.
        2 text-msg pic x(30).
       procedure division using adr-of-next-data-ptr.
           set address of next-data-ptr to adr-of-next-data-ptr
           set address of next-data to next-data-ptr
           display text-msg
           exit program.
       end program prog-6.
-----

William M. Klein <wmklein@ix.netcom.com> wrote in message
news:b7seot$ten$1@slb2.atl.mindspring.net...
> Rick,
>    I think that I made the same mistake when I first started looking at
…[10 more quoted lines elided]…
> "An operand is a sending operand if its contents prior to the execution of
a
> statement may be used by the execution of the statement. An operand is a
> receiving operand if its contents may be changed by the execution of the
> statement."
>
> I read this to mean that an "ADDRESS OF" data-pointer may be used in a
CALL
> BY REFERENCE (identifier-2) - but *only* if that data-item is *not*
changed
> by any action of the CALLed subprogram.
>
…[17 more quoted lines elided]…
> > > One must say BY CONTENT ADDRESS OF record-2, which is the same as
USING
> > > record-2.
> >
…[45 more quoted lines elided]…
> > not applicable.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 31)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-20T22:55:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea2fcc7.165270154@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <b7seot$ten$1@slb2.atl.mindspring.net> <va5q62ai9pqrf8@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>Bill,
>I reviewed the FDIS and came to the conclusion that my
…[4 more quoted lines elided]…
>and only for BY REFERENCE.

When the referenced data item is in local-storage, its address-identifier will
be the contents of the data-pointer on which it is BASED. They are one and the
same. I tried to show that in the examples. 

As a practical matter, it will work the same in the other sections. The only
difference being the pointers are not visible; they don't have a name. 

>I then wrote a set of programs to test the concept using the older
>MF COBOL/2 3.2. My thinking is that it should have the same
…[3 more quoted lines elided]…
>the linkage section rather than BASED items.

Micro Focus does not have the restriction introduced by SR(11). If you had a
conforming 2002 compiler, the CALL in your first program would not have
compiled.

What's objectionable about SR(11) is the unstated implication that structures
containing pointers cannot be passed BY REFERENCE. Using my Best Practices Demo
Program as an example, it contains structures like this:

01  line-entry.
     05  line-length		comp-5 pic s9(04).
     05  fixed-portion.
         10  previous-line		pointer.
         10  next-line		pointer.
         10  line-number		comp-5 pic s9(09).
         10  word-count		comp-5 pic s9(04).
         10  first-word		pointer.
         10  last-word		pointer.
     05  line-text.
         10  line-byte occurs 1 to 256 depending on line-length pic x.

     call 'mfree' using line-entry

The intention of SR(11) is to protect pointers from being modified. Because
line-entry contains pointers, SR(11) implies it cannot be passed in this way ..
because mfree could modify those pointers. This is a SERIOUS structural problem.

--- history follows --

>The programs pass only the addresses of pointers on calls,
>including both program (procedure) pointers and data pointers.
…[259 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 32)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-20T23:57:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va6r4ni3b5u5f2@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <b7seot$ten$1@slb2.atl.mindspring.net> <va5q62ai9pqrf8@corp.supernews.com> <3ea2fcc7.165270154@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ea2fcc7.165270154@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[8 more quoted lines elided]…
> When the referenced data item is in local-storage, its address-identifier
will
> be the contents of the data-pointer on which it is BASED. They are one and
the
> same. I tried to show that in the examples.

Your example was, in part:

 working-storage section.
 01  a-pointer  data-pointer.
 01  record-1  pic x(80).
 local-storage section.
 01  record-2  pic x(80) BASED a-pointer.

The standard, as approved, to the best of my knowledge,
and according to the FDIS, does not use BASED in the
way you used it here. PL/I uses it that way and an older
committee draft may have had such syntax. The correct
data description entry would be:

 01  record-2  pic x(80) BASED.

that is, record-2 would have its own implicit pointer which
is modified by the SET statement, such as,

  set address of record-2 to a-pointer.

What this means is than when passing the address of a
based item, there is no way that a called program can change
the location of a based item in the calling program, for example.

> As a practical matter, it will work the same in the other sections. The
only
> difference being the pointers are not visible; they don't have a name.
>
…[7 more quoted lines elided]…
> Micro Focus does not have the restriction introduced by SR(11). If you had
a
> conforming 2002 compiler, the CALL in your first program would not have
> compiled.

As I tried to say, I believe the restriction in SR(11) does not
apply. This is a result of the use of 'address-identifier' in SR(3)
and SR(4).

> What's objectionable about SR(11) is the unstated implication that
structures
> containing pointers cannot be passed BY REFERENCE.

SR(11) does not apply when calls are made BY REFERENCE
with the conformance checking of a program prototype and the
restriction on structures is only for strongly-typed group items.

USAGE SR(13), FDIS page 362,
"13) A USAGE clause with the OBJECT REFERENCE,
POINTER, or PROGRAM-POINTER phrase may be specified
only for an elementary data item with level 1 or subordinate to
a type declaration that includes the STRONG phrase."

Use a program prototype and the problem goes away.

> Using my Best Practices Demo
> Program as an example, it contains structures like this:
…[15 more quoted lines elided]…
> The intention of SR(11) is to protect pointers from being modified.
Because
> line-entry contains pointers, SR(11) implies it cannot be passed in this
way ..
> because mfree could modify those pointers. This is a SERIOUS structural
problem.

See above.

> --- history follows --
>
…[175 more quoted lines elided]…
> >> identifier-2 or if identifier-2 is an addressidentifier, identifier-2
is a
> >> sending operand."
> >>
> >> However, 14.5.7 Sending and receiving operands on page 389 says,
> >>
> >> "An operand is a sending operand if its contents prior to the execution
of
> >a
> >> statement may be used by the execution of the statement. An operand is
a
> >> receiving operand if its contents may be changed by the execution of
the
> >> statement."
> >>
…[65 more quoted lines elided]…
> >> > > The reason for the prohibition of passing pointers BY REFERENCE is
not
> >> > > syntactic simplicity, it is to protect them from modification
outside
> >> the
> >> > SET
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 33)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T16:06:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea4113b.236052308@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <b7seot$ten$1@slb2.atl.mindspring.net> <va5q62ai9pqrf8@corp.supernews.com> <3ea2fcc7.165270154@news.optonline.net> <va6r4ni3b5u5f2@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[28 more quoted lines elided]…
>committee draft may have had such syntax.

My draft --1.8 -- says the pointer is optional.

> 01  record-2  pic x(80) BASED.
>
…[35 more quoted lines elided]…
>restriction on structures is only for strongly-typed group items.

Are we talking about the same passage? Mine reads:

"If the BY REFERENCE phrase is specified or implied for an identifier-2, that
identifier shall not be a strongly typed group item, object reference, or
pointer."

>USAGE SR(13), FDIS page 362,
>"13) A USAGE clause with the OBJECT REFERENCE,
>POINTER, or PROGRAM-POINTER phrase may be specified
>only for an elementary data item with level 1 or subordinate to
>a type declaration that includes the STRONG phrase."

I missed that passage. I think tt answers my question -- structures containing
pointers may not be passed BY REFERENCE.


>Use a program prototype and the problem goes away.
>
…[298 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 34)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-21T13:10:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va89jd7r0nqle9@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <b7seot$ten$1@slb2.atl.mindspring.net> <va5q62ai9pqrf8@corp.supernews.com> <3ea2fcc7.165270154@news.optonline.net> <va6r4ni3b5u5f2@corp.supernews.com> <3ea4113b.236052308@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ea4113b.236052308@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[13 more quoted lines elided]…
> >> When the referenced data item is in local-storage, its
address-identifier
> >will
> >> be the contents of the data-pointer on which it is BASED. They are one
and
> >the
> >> same. I tried to show that in the examples.
…[14 more quoted lines elided]…
> My draft --1.8 -- says the pointer is optional.

The FDIS (Final Draft International Standard) does not
mention an optional pointer.

> > 01  record-2  pic x(80) BASED.
> >
…[20 more quoted lines elided]…
> >> Micro Focus does not have the restriction introduced by SR(11). If you
had
> >a
> >> conforming 2002 compiler, the CALL in your first program would not have
…[14 more quoted lines elided]…
> Are we talking about the same passage?

I'll rephrase. When a program prototype is used, Format 3 applies.
In Format 3, identifier-2 items may only be passed BY REFERENCE;
and because Format 3 is used SR(11) does not apply. [Strongly-
typed group items are reference in USAGE SR(13) mentioned, below.]

> Mine reads:
>
> "If the BY REFERENCE phrase is specified or implied for an identifier-2,
that
> identifier shall not be a strongly typed group item, object reference, or
> pointer."

FYI, the FDIS reads:
"FORMATS 1 AND 2
11) If the BY REFERENCE phrase is specified or implied for
an identifier-2, that identifier shall be neither a strongly-typed
group item nor a data item of class object or pointer."

> >USAGE SR(13), FDIS page 362,
> >"13) A USAGE clause with the OBJECT REFERENCE,
…[4 more quoted lines elided]…
> I missed that passage. I think tt answers my question -- structures
containing
> pointers may not be passed BY REFERENCE.

In Format 3 (program-prototype), structures containing pointers
may be passed BY REFERENCE.

> >Use a program prototype and the problem goes away.

As I said, "Use a program prototype and the problem goes away."
And, keep in mind, that we are discussing the writing of programs
that conform to the standard.
------------
Rick

> >> Using my Best Practices Demo
> >> Program as an example, it contains structures like this:
…[17 more quoted lines elided]…
> >> line-entry contains pointers, SR(11) implies it cannot be passed in
this
> >way ..
> >> because mfree could modify those pointers. This is a SERIOUS structural
…[175 more quoted lines elided]…
> >> >>    I think that I made the same mistake when I first started looking
at
> >> >> this.
> >> >>
…[3 more quoted lines elided]…
> >> >> identifier-2 or if identifier-2 is an addressidentifier,
identifier-2
> >is a
> >> >> sending operand."
…[3 more quoted lines elided]…
> >> >> "An operand is a sending operand if its contents prior to the
execution
> >of
> >> >a
> >> >> statement may be used by the execution of the statement. An operand
is
> >a
> >> >> receiving operand if its contents may be changed by the execution of
…[3 more quoted lines elided]…
> >> >> I read this to mean that an "ADDRESS OF" data-pointer may be used in
a
> >> >CALL
> >> >> BY REFERENCE (identifier-2) - but *only* if that data-item is *not*
…[3 more quoted lines elided]…
> >> >> This seems a little "misleading" to me, but does (as far as I read
it)
> >> >> reflect the 2002 Standard.
> >> >>
…[14 more quoted lines elided]…
> >> >> > > One must say BY CONTENT ADDRESS OF record-2, which is the same
as
> >> >USING
> >> >> > > record-2.
…[10 more quoted lines elided]…
> >> >> > "shall reference an address-identifier or a data item defined
...".
> >> >> > [FDIS page 421]
> >> >> >
…[5 more quoted lines elided]…
> >> >> > and "shall reference a data item defined ..." and "creates a
unique
> >> >> > data item of class pointer and category data-pointer that contains
> >> >> > the address of ...". [FDIS page 99]
…[18 more quoted lines elided]…
> >> >> > > The reason for the prohibition of passing pointers BY REFERENCE
is
> >not
> >> >> > > syntactic simplicity, it is to protect them from modification
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ BASED Clause (was: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 34)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T14:41:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b81hgv$lg$1@slb3.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <b7seot$ten$1@slb2.atl.mindspring.net> <va5q62ai9pqrf8@corp.supernews.com> <3ea2fcc7.165270154@news.optonline.net> <va6r4ni3b5u5f2@corp.supernews.com> <3ea4113b.236052308@news.optonline.net>`

```
Just so there is a "clear" thread on this (although Rick has already
provided the correct answer).

The final 2002 Standard does *NOT* include any optional "pointer" data item
in the BASED Clause.  See Page 263 of the FDIS.

RW - if you are going to comment on the 2002 Standard, I really suggest that
you get a copy of this document. It is still available for free from:

 http://www.incits.org/tc_home/j4.htm
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T21:27:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea1b9fa.82620167@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[53 more quoted lines elided]…
>not applicable.

Page 421 says:

10) If the BY REFERENCE phrase is specified or implied for an identifier-2, that
identifier shall not be a strongly typed group item, object reference, or
pointer.

Here is an example:

 working-storage section.
 01  a-pointer  data-pointer.
 01  record-1  pic x(80).
 local-storage section.
 01  record-2  pic x(80) BASED a-pointer.

The following two statements do the same thing:
 SET ADDRESS OF record-2 TO ADDRESS OF record-1
 SET a-pointer TO ADDRESS OF record-1

Likewise, the following are equivalent. 
 CALL 'a-program' USING record-2
 CALL 'a-program' USING BY CONTENT ADDRESS OF record-2
 CALL 'a-program' USING BY CONTENT a-pointer

But the following would not pass a pointer to record-2, as you said, they would
pass a pointer to a-pointer:
 CALL 'a-program' USING ADDRESS OF record-2
 CALL 'a-program' USING a-pointer

This would enable the called program to modify the pointer. The committee was
afraid this would happen:

a-program
 linkage section.
 01  a-record   pic x(80).
 
 MOVE SPACES TO a-record

..which would put spaces into a-pointer. The correct syntax should be:

a-program
 local-storage section.
 01  a-record   pic x(80) BASED a-pointer.
 linkage section.
 01  a-pointer   data-pointer. 

 MOVE SPACES to a-record

The committee is trying to prevent us from shooting ourselves in the foot. Other
languages go in the other direction; they make the syntax easy to use but hard
(for some) to understand. For instance, in C it would be **a_record.

I find this restriction a SERIOUS flaw because it implies, without explicitly
saying, that not only is pointer prohibited in the USING but also a group item
containing pointers cannot be passed BY REFERENCE.  I routinely work with
structures which contain pointers to other structures and I routinely pass their
address as a parameter. This limitation, not found in implimentor extensions to
COBOL 85, would invalidate every one of my programs. 

Tell me if I'm mistaken about group items. I can't find where the standard says
one way or the other.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-19T21:54:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va3vlabogr2180@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <3ea1b9fa.82620167@news.optonline.net>`

```
I am going to delay replying to this post, and to Bill's post,
until I can get clarification as to what the standard says.

You are using an older Committee Draft, so your quotes
from the draft are a bit out-of-date. I have used text from
the FDIS, to raise the question from the example in E.9.1.2,
for discussion.

Robert Wagner <robert@wagner.net> wrote in message
news:3ea1b9fa.82620167@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
>
…[50 more quoted lines elided]…
> >> syntactic simplicity, it is to protect them from modification outside
the
> >SET
> >> verb.
…[6 more quoted lines elided]…
> 10) If the BY REFERENCE phrase is specified or implied for an
identifier-2, that
> identifier shall not be a strongly typed group item, object reference, or
> pointer.
…[18 more quoted lines elided]…
> But the following would not pass a pointer to record-2, as you said, they
would
> pass a pointer to a-pointer:
>  CALL 'a-program' USING ADDRESS OF record-2
>  CALL 'a-program' USING a-pointer
>
> This would enable the called program to modify the pointer. The committee
was
> afraid this would happen:
>
…[16 more quoted lines elided]…
> The committee is trying to prevent us from shooting ourselves in the foot.
Other
> languages go in the other direction; they make the syntax easy to use but
hard
> (for some) to understand. For instance, in C it would be **a_record.
>
> I find this restriction a SERIOUS flaw because it implies, without
explicitly
> saying, that not only is pointer prohibited in the USING but also a group
item
> containing pointers cannot be passed BY REFERENCE.  I routinely work with
> structures which contain pointers to other structures and I routinely pass
their
> address as a parameter. This limitation, not found in implimentor
extensions to
> COBOL 85, would invalidate every one of my programs.
>
> Tell me if I'm mistaken about group items. I can't find where the standard
says
> one way or the other.
```

###### ↳ ↳ ↳ Re: What is supported (was: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-20T16:28:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va60ov4oecag82@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz> <b586kl$2h1$1@slb4.atl.mindspring.net> <3e77b35b.7601275@news.optonline.net> <v7fkcvfdqatlf5@corp.supernews.com> <3e78f7f6.28054222@news.optonline.net> <v7insvfn4je22e@corp.supernews.com> <3ea16766.61476936@news.optonline.net> <va35257evgc5e0@corp.supernews.com> <3ea1b9fa.82620167@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ea1b9fa.82620167@news.optonline.net...
[snip]
> Page 421 says:
>
> 10) If the BY REFERENCE phrase is specified or implied for an
identifier-2, that
> identifier shall not be a strongly typed group item, object reference, or
> pointer.
…[18 more quoted lines elided]…
> But the following would not pass a pointer to record-2, as you said, they
would
> pass a pointer to a-pointer:
>  CALL 'a-program' USING ADDRESS OF record-2
>  CALL 'a-program' USING a-pointer
>
> This would enable the called program to modify the pointer. The committee
was
> afraid this would happen:
>
…[16 more quoted lines elided]…
> The committee is trying to prevent us from shooting ourselves in the foot.
Other
> languages go in the other direction; they make the syntax easy to use but
hard
> (for some) to understand. For instance, in C it would be **a_record.
>
> I find this restriction a SERIOUS flaw because it implies, without
explicitly
> saying, that not only is pointer prohibited in the USING but also a group
item
> containing pointers cannot be passed BY REFERENCE.  I routinely work with
> structures which contain pointers to other structures and I routinely pass
their
> address as a parameter. This limitation, not found in implimentor
extensions to
> COBOL 85, would invalidate every one of my programs.
>
> Tell me if I'm mistaken about group items. I can't find where the standard
says
> one way or the other.

I just spent several hours looking through the FDIS and
even wrote a test program that should have the same
behavior as the standard. I can find no restriction on using
pointers that would prevent using pointers in COBOL in a
manner similar to how they may be used in C, which, as we
*all* know, is the benchmark for "do whatever you want."

The one restriction that COBOL places on the use of
pointers is, what I might call, 'single-level access'; that is
one must set a data item to the address contained in the
pointer before accessing the data 'pointed to'. C permits,
what I might call, 'multi-level access' with a single expression.

I think "the committee," as you call them, gave us an automatic
weapon with a hair-trigger. One might shoot one's self in the
foot or destroy it entirely depending upon how one uses
pointers. It is just what I wanted! <g>
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77db2e.17797796@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e768cca.43241859@news.optonline.net> <217e491a.0303180131.1ccbd4df@posting.google.com> <3e775283.93866179@news.optonline.net> <b58496$ttb$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[6 more quoted lines elided]…
>syntax.

They cannot say that because it's in the 2002 standard. 

>> What would you have us do when the manual contradicts itself? Tell
>> somebody? I tried twice and got flamage in return.
>
>Which manual was that ?  

The 2002 standard. See related posting to WMK. 

>When you asserted what should happen with bound checks on index your 
>arguments were simply wrong (incorrect).  The reasons why you were wrong 
>was explained carefully to you.

"Was explained carefully to you" is disparaging language. I'm not a child. 

Granted, you were correct on that one. Bounds _used to be checked_ on SET. They
no longer are. 

>When you asserted that the standard had errors WNK took time to carefully 
>explain how to read the document and work out why your argument was wrong.

Nope, he flamed me. My objections were, and still are, valid.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 17)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-18T07:26:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b557kb$lo8$2@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <v79pf26jvnqvb7@corp.supernews.com> <3e751995.48203421@news.optonline.net>`

```
Robert Wagner wrote:

> I'm usually the abstract thinker

I saw an absract painting once.  It had been done by a Chimpanzee throwing 
paint at a wall.  Now why did that come to mind ?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-17T10:43:16
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e758b62_1@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e74ba67.23834107@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> This isn't an ivory tower debate forum. It's a place where people come for
> practical advice. They will leave if they see crotchety old men quibbling
over
> minutiae.
>

They are far more likely to leave if they just see a flame war. Although CLC
is far from perfect, people DO get helped here.


> >You are smart enough to recognise a good case when you see it, and to
adopt
> >the approach that it is an obscure oddity, being presented to make you
> >wrong, is simply selling yourself short.
>
> I get it -- you're the 'good cop' playing against Richard's 'bad cop'.
>
Nope. There are NO cops here...like I said before, it is an UNMODERATED NG.
You can say anything you like...(and I notice you are not reticent in taking
advantage of this facility <G>). However, this precious "Freedom of Speech",
does carry SOME responsibility. To waste it simply trolling for the worst
kind of argument, is a sad and unnecessary waste of brain cells and time.

Besides, if I WERE a cop, I certainly wouldn't be a GOOD one...<G>

I guess my point is that you are smart enough to be able to argue
effectively and persuasively, without simply resorting to to an oafish
argumentation device like "Nobody understands me. They're making up obscure
cases just to humiliate me."

Paranoid or what? <G>

In this forum, being smart isn't enough...there's plenty of "smart" around
here. You need to be big enough to accept that you will lose a few as well
as win some.

> >You can do much better than this. Would it be so painful to accept that
this
> >is a valid point and acknowledge it?
>
> Fine. It's a valid hypothetical point.

Good. I don't believe that hurt at all... Can you do it without the
"hypothetical" cuddle blanket <G>?

>
> >Or is your whole time here to be about making yourself right?
>
> I've admitted to being wrong several times here.
>
OK, maybe I missed it. If I did, sorry.

Anyway, it isn't about being right or wrong, it is about the WAY in which
rightness and wrongness are pursued <G>.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e767af9.38679759@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <3e758b62_1@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>I guess my point is that you are smart enough to be able to argue
>effectively and persuasively, without simply resorting to to an oafish
…[3 more quoted lines elided]…
>Paranoid or what? <G>

I was responding to the question: do you think they're just making this stuff
up? 

I'm not paranoic, not do I think nobody understands me. They understand me very
well .. as a threat to their comfortable world. 

>In this forum, being smart isn't enough...there's plenty of "smart" around
>here. You need to be big enough to accept that you will lose a few as well
>as win some.

I do lose a few, and am comfortable with the 'small fish, big pond' analogy. 

>Anyway, it isn't about being right or wrong, it is about the WAY in which
>rightness and wrongness are pursued <G>.

You're correct there, because right and wrong are emotional metrics. Correct and
incorrect, on the other hand, are unequivocal.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-03-18T09:38:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57b1r$kg7$1@panix1.panix.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <v77vapbe05vd29@corp.supernews.com> <3e767af9.38679759@news.optonline.net>`

```
In article <3e767af9.38679759@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

[snip]

>>Anyway, it isn't about being right or wrong, it is about the WAY in which
>>rightness and wrongness are pursued <G>.
…[3 more quoted lines elided]…
>

Mr Wagner, given that the ways that words are defined are to be found in 
dictionaries then 'right', 'wrong', 'correct' and 'incorrect' are all 
defined as or synonymous with each other.

for 'right':

OED: 7. a. Agreeing with some standard or principle; correct, proper.  
Also, agreeing with facts; true.

AHD: 2.In accordance with fact, reason, or truth; correct: the right 
answer.

WRU: 2. Fit; suitable; proper; correct; becoming; as, the right man in the 
right place; the right way from London to Oxford.

MW: 3 a : agreeable to a standard b : conforming to facts or truth : 
CORRECT <the right answer>

for 'wrong':

OED: 5. a. Not in conformity with some standard, rule, or principle; 
deviating from that which is correct or proper; contrary to, at variance 
with, what one approves or regards as right.

AHD: 1.Not in conformity with fact or truth; incorrect or erroneous.

WRU: Syn: Injurious; unjust; faulty; detrimental; incorrect; erroneous; 
unfit; unsuitable.

MW: 3 : the state, position, or fact of being or doing wrong: as a : the 
state of being mistaken or incorrect

for 'correct':

OED: 2. In accordance with fact, truth, or reason; free from error; exact, 
true, accurate; right.

AHD: Synonyms: correct, rectify, remedy, redress, reform, revise, amend.  
These verbs mean to make right what is wrong.

WRU: Syn: Accurate; right, exact; precise; regular; faultless.

MW: 1 a : to make or set right.

for 'incorrect':

OED: 3. Of style, action, etc.: Not in conformity with a recognized 
standard; improper, faulty.

(note - although the word 'wrong' is not used in the definition please 
compare with OED def'n 'wrong' cited above... moderately similar)

AHD: 1.Not correct; erroneous or wrong.

WRU: Syn: Inaccurate; erroneous; wrong; faulty.

MW: 2 a : INACCURATE, FAULTY b : not true : WRONG

When adopting a particular or idiosyncratic use of a word for the purposes 
of discussion or argument it might be fruitful to state the definition for 
this use from the outset.

DD
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T16:54:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b54ukb$76l$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net>`

```

On 16-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> I think they are. They are constructing improbable cases to rebut my points
> about realistic use of COBOL. For instance, an alphabet beginning with 'e'.

Agreed.   But "e" is an absurdly unlikely low-values.   You picked it for that
very purpose.    But it isn't a coding question whether it is portable to
compare LOW-VALUES with 'e'.    The question is whether it is portable in
general.


Portability isn't my issue - as a mainframer, I find portable code the least of
my problems when doing a conversion.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e767e06.39460475@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <3e74ba67.23834107@news.optonline.net> <b54ukb$76l$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>Portability isn't my issue - as a mainframer, I find portable code the least of
>my problems when doing a conversion.

As a multi-platform guy, I agree. I've moved hundreds-to-thousands of COBOL
programs from mainframe to Unix or PC. Code portability was almost never an
issue. They almost always get a clean compile the first or second time.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-16T15:54:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b52rqv$u8j$1@slb2.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com>`

```
Just to confirm, the use of COLLATING SEQUENCE clause is QUITE common in two
types of programs:

1) Programs intended to run in both ASCII and EBCDIC environments - where
the use of the COLLATING SEQUENCE makes the program "portable" across
environments.

2) In environments intended for "international use" - where additional
"alphabetic" characters (accented, umlauted vowels - diagraphs, etc) exist
and need to be "put" in their correct collating order.

For those of us who HAVE worked in either of these environments, this phrase
is "relatively" common.  For those used to coding in a "single" environment,
I agree that it is probably unusual.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-17T01:27:45
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e75092f_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <3e742b05_2@text-west.newsgroups.com> <b52rqv$u8j$1@slb2.atl.mindspring.net>`

```
Bill,

I'm not taking issue with your post...

All I will say is that when working on Mainframes (IBM and NCR as it
happens), when we needed to translate a character set from one system to
another we used the TRANSFORM verb, NOT the COLLATING SEQUENCE.

I know it is non-standard COBOL, but it certainly did the job. I have
personally never used COLLATING SEQUENCE or seen it used, in 36 years,
DESPITE having done conversions across different platforms and had programs
that must deal with the relative formats.

Having said that, I accept totally that there are legitimate uses for it as
Rick in particular has demonstrated.

Pete.

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b52rqv$u8j$1@slb2.atl.mindspring.net...
> Just to confirm, the use of COLLATING SEQUENCE clause is QUITE common in
two
> types of programs:
>
…[8 more quoted lines elided]…
> For those of us who HAVE worked in either of these environments, this
phrase
> is "relatively" common.  For those used to coding in a "single"
environment,
> I agree that it is probably unusual.
>
…[139 more quoted lines elided]…
> > ---= 19 East/West-Coast Specialized Servers - Total Privacy via
Encryption
> =---
>
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-03-16T13:02:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uvs87v0g3son3l3vp4qm946vc8cmbkjar7@4ax.com>`
- **References:** `<3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net>`

```
On Sun, 16 Mar 2003 07:37:55 GMT, robert@wagner.net (Robert Wagner)
wrote:

>"Rick Smith" <ricksmith@mfi.net> wrote:
>
…[22 more quoted lines elided]…
>>         88 end-of-file value "e" false low-value.

anip
>>It is not the use of 'e' in particular, that is the problem. It is
>>the reliance upon LOW-VALUE as never being equivalent
…[3 more quoted lines elided]…
>is'. You just pulled that up for the sake of debate. 
Then YOU have not seen enough of others shops programs.
I have been using this construce for at least 12 years now in
production programs, and in several of the shops I have worked with.

And in all the COBOL courses I have given I have always mentioned that
the LOW-VALUES figurative constant is dependent in the usage of clause
"alphabet is" so that the students were aware of the dangers of using
"low-values" or "high-values".
>
>I'm concerned with Practice in the real world. Diluting Practice with such
>hypotheticals does a disservice to struggling programmers. 
Assuming that real world is your company, then yes you are correct.
Fortunately there are a few thousands others companies that have never
heard of you (and never will).


FF
Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T17:56:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74ba24.23767018@news.optonline.net>`
- **References:** `<3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <uvs87v0g3son3l3vp4qm946vc8cmbkjar7@4ax.com>`

```
Frederico Fonseca <real-email-in-msg-spam@email.com> wrote:

>On Sun, 16 Mar 2003 07:37:55 GMT, robert@wagner.net (Robert Wagner)
>wrote:
…[33 more quoted lines elided]…
>>is'. You just pulled that up for the sake of debate. 

>Then YOU have not seen enough of others shops programs.
>I have been using this construct for at least 12 years now in
>production programs, and in several of the shops I have worked with.

Two translations for every comparison will make your program run slowly. When I
want to do that, I do a single translation into the machine's collating
sequence.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-16T12:09:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<700C50ED0F306145.ABB400F39384D63B.DE56A32DAA54F03A@lp.airnews.net>`
- **References:** `<3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net>`

```
On Sun, 16 Mar 2003 07:37:55 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"Rick Smith" <ricksmith@mfi.net> wrote:
>
…[82 more quoted lines elided]…
>

You stated your argument as an absolute truth.  Mr. Smith has just
illustrated that truth was false.  Whether you've never seen it or not
is irrelevant as the possibility exists and must be accounted for in
any intelligent encompassing "best practice".  Any practice that
ignores a possibility that is known through the understanding of Cobol
and its standards isn't worth snot.

>I'm concerned with Practice in the real world. Diluting Practice with such
>hypotheticals does a disservice to struggling programmers. 

Any good programmer when coding a solution to a problem takes all
hypotheticals into consideration so that a thorough solution can be
coded.  Failure to do so is bad programming even if you don't use
periods.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #109

Program aborting:
Close all that you have worked on.
You ask far too much.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T18:15:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74bcb8.24427541@news.optonline.net>`
- **References:** `<3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <700C50ED0F306145.ABB400F39384D63B.DE56A32DAA54F03A@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Sun, 16 Mar 2003 07:37:55 GMT, robert@wagner.net (Robert Wagner)
>enlightened us:
…[3 more quoted lines elided]…
>>>

>>In all my years of programming, I've never seen anyone use 'collating sequence
>>is'. You just pulled that up for the sake of debate. 
…[15 more quoted lines elided]…
>periods.

I disagree. My Best Practices says:

"Over its history, the COBOL language has accumulated many features that are Bad
Practices and/or obsolete. Encyclopedic reference books describe them all in
alphabetical order without giving the reader a clue as to which are good, bad
and superfluous. Rather than compiling a list of negatives.. don't do this and
that .. I simply omitted the bad features. The syntax in the first three
chapters is all you need to write the most complex programs under COBOL '85."

The three chapters do not mention 'collating sequence is', nor GO TO, nor ALTER.


Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-17T10:23:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E1FEA8D430DC8C3A.DF21FCF152572805.A695663B1184BEE2@lp.airnews.net>`
- **References:** `<3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <700C50ED0F306145.ABB400F39384D63B.DE56A32DAA54F03A@lp.airnews.net> <3e74bcb8.24427541@news.optonline.net>`

```
On Sun, 16 Mar 2003 18:15:47 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:
>
…[38 more quoted lines elided]…
>Robert

By the ommission of "collating sequence", a valuable and oft used
option (yes...I have used it several times when doing programming for
some Thai banks), you are saying its use is a "Bad Practice".  That is
nonsense.  I don't even agree with GO TO, but I can at least accept
its non-use and understand some of the arguments against its use.
ALTER really has no place.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #110

With searching comes loss
And the presence of absence:
"My Novel" not found.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-16T13:38:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v79gf2q2acfa6f@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e742223.512658577@news.optonline.net...
> "Rick Smith" <ricksmith@mfi.net> wrote:
[snip]
> In all my years of programming, I've never seen anyone use 'collating
sequence
> is'. You just pulled that up for the sake of debate.

It is because I have used it that I understood your assumption,
that LOW-VALUES is always X"00", was wrong; but you never
saw me use it or saw my post to the group in October 2000.

<
http://groups.google.com/groups?q=collating+sequence+group:comp.lang.cobol&h
l=en&lr=&ie=UTF-8&selm=8stgh6%246de%241%40news.hitter.net&rnum=7 >

> I'm concerned with Practice in the real world. Diluting Practice with such
> hypotheticals does a disservice to struggling programmers.

In the referenced post, I demonstrated the practical use of
PROGRAM COLLATING SEQUENCE and a programmer-
defined ALPHABET to handle hexi-decimal conversions
in a portable manner.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T16:51:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b54ue8$76e$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net>`

```

On 16-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> In all my years of programming, I've never seen anyone use 'collating sequence
> is'. You just pulled that up for the sake of debate.

Interesting.   I have seen it.   Maybe he did.  Is looking in the manual an
improper debating tactic?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-17T14:46:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55c82$4lr$1@slb6.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <b54ue8$76e$1@peabody.colorado.edu>`

```
My least favorite CLC "spammer" claims to use IBM as one of his
"state-of-the-art" environments.  However, he apparently hasn't read their
manuals - or he couldn't say that he has never seen any examples of
collating sequence.  See for example,

 (for showing how to treat upper-/lower-case equivalence)

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.1.2.2.
1

But I forget, I think that he has already said that he tends to ignore the
manuals when they don't agree with what he learnt 40 years ago - or saw once
in a program with an currently unsupported compilers.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-17T16:33:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49rda.1088$K37.244046@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <b54ue8$76e$1@peabody.colorado.edu> <b55c82$4lr$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b55c82$4lr$1@slb6.atl.mindspring.net...
> My least favorite CLC "spammer" claims to use IBM as one of his
> "state-of-the-art" environments.  However, he apparently hasn't read their
…[5 more quoted lines elided]…
>
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.1.2.2.
> 1
>
> But I forget, I think that he has already said that he tends to ignore the
> manuals when they don't agree with what he learnt 40 years ago - or saw
once
> in a program with an currently unsupported compilers.
>
…[17 more quoted lines elided]…
>

I was wondering when someone was going to bring up the problem of
upper/lower case alphabetical sorting.  I have used colating sequence for
just that.  The colating sequence of ASCII, in it's evolved form, bears no
relationship at all to the collating sequence of "alphabetical order".
Then, of course, there is also the problem of the extra characters in other
languages.  Certainly here in Canada, you have to integrate any specialized
"e" characters into your sort sequence correctly.

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7686fd.41756488@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <v7728rteo51p71@corp.supernews.com> <3e73a68f.481017107@news.optonline.net> <v77vapbe05vd29@corp.supernews.com> <3e742223.512658577@news.optonline.net> <b54ue8$76e$1@peabody.colorado.edu> <b55c82$4lr$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>My least favorite CLC "spammer" claims to use IBM as one of his
>"state-of-the-art" environments.  However, he apparently hasn't read their
…[6 more quoted lines elided]…
>1

I thought it very good, actually. The only problem is that it's slow. It implies
translating BOTH fields on every comparison. If I'm looking up words in a
dictionary, I don't need dictionary words translated, they're already in lower
case. And the source could better be translated once rather than on every
'look'. 

It would be good for one-time use, such as processing the command line.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T20:22:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4vukv$de8$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net>`

```
Robert Wagner wrote:

> I wonder why people go to such extraordinary lengths. Because they feel
> threatened?

It is not _us_ that is threatened, it is truth and significance.

Most of the statements you make are in the _form_ of statements of fact, 
but are either merely opinions or are wrong.  Often they are but one aspect 
of a range of options, but stated as if it were the only option.

No one really cares what it is that you believe, but when you make what you 
intend to be definitive statements then some others may not have the 
experience or perspective to know that your pronouncements are rather 
shallow and that other options exist.

I have no particular interest in making systems that do not have low-values 
as all bits zero, or even of using them.  But I do know that they exist.

Over many years you seem to have developed mechanisms to protect your ego.  
Instead of learning, from what others say to and about you, to make less 
stupid and uninformed statements, you have learnt to blame others for the 
corrections and 'insults' that you get.

In this particular case you are shown to be wrong in form and content and 
yet your reaction is not one of learning that there is more to systems than 
you thought.  

Your reaction is that we contrived these because we feel 'threatened'.

'Threatened' by what ? your 'superior intellect' ?  your 'ability to change 
the world' ?

No. we are only threatened by ignorence and stupidity.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T21:47:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73912b.475540979@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <b4vukv$de8$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
>> I wonder why people go to such extraordinary lengths. Because they feel
>> threatened?

>Over many years you seem to have developed mechanisms to protect your ego.  
>Instead of learning, from what others say to and about you, to make less 
>stupid and uninformed statements, you have learnt to blame others for the 
>corrections and 'insults' that you get.

Over the years I've learned to expect hostility from stupid people; friendship
from smart people. And I've learned the most effective way to motivate stupid
people is to threaten them ..  not so much from personal practice, but from
watching their managers (and news media) do it. 

>'Threatened' by what ? your 'superior intellect' ?  your 'ability to change 
>the world' ?
>
>No. we are only threatened by ignorence and stupidity.

Given the surplus of ignorance and stupidity in the world, you must feel _very_
threatened.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T16:48:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b54u9l$708$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <b4vukv$de8$1@aklobs.kc.net.nz> <3e73912b.475540979@news.optonline.net>`

```

On 15-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> Over the years I've learned to expect hostility from stupid people; friendship
> from smart people. And I've learned the most effective way to motivate stupid
> people is to threaten them ..  not so much from personal practice, but from
> watching their managers (and news media) do it.

So if you insult us enough that we become hostile, we also become stupid?    The
world must be full of stupid people, and this group is getting fuller and fuller
of stupid people - who used to be smart before you came here.   At least there
is one smart person left, the rest of us are getting stupider and stupider.  
Particularly as we don't seem willing to learn from the one person who knows.  
It's probably an emotional lack - we are called stupid so many times that we
became hostile and refuse to see the light.

Or maybe you are filling this newsgroup up with something else.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e768c98.43191769@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <b4vukv$de8$1@aklobs.kc.net.nz> <3e73912b.475540979@news.optonline.net> <b54u9l$708$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 15-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
>> Over the years I've learned to expect hostility from stupid people;
friendship
>> from smart people. And I've learned the most effective way to motivate stupid
>> people is to threaten them ..  not so much from personal practice, but from
>> watching their managers (and news media) do it.
>
>So if you insult us enough that we become hostile, we also become stupid?
The
>world must be full of stupid people, and this group is getting fuller and
fuller
>of stupid people - who used to be smart before you came here.  

I was talking about people in general, not posters to CLC. I have _never_ called
anyone here stupid. Perhaps Old Guard mainframe programmers, referred to
generically, but not individuals posting here. Obviously, the same courtesy has
not been returned.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-18T15:29:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57e1b$hvg$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e728355.406452311@news.optonline.net> <v75df0ckqdne48@corp.supernews.com> <3e72ff00.438115975@news.optonline.net> <b4vukv$de8$1@aklobs.kc.net.nz> <3e73912b.475540979@news.optonline.net> <b54u9l$708$1@peabody.colorado.edu> <3e768c98.43191769@news.optonline.net>`

```

On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> I was talking about people in general, not posters to CLC. I have _never_
> called
> anyone here stupid. Perhaps Old Guard mainframe programmers, referred to
> generically, but not individuals posting here.

Someone must have been faking your ID then.

> Obviously, the same courtesy has not been returned.

Whomever has been posting with your name has alienated quite a few of us -
calling us idiots and putting us down.   We probably missed the courtesy part
within this noise.

In general we don't care to be insulted repeatedly.  And we appreciate it
greatly when people post examples about how the person doing the insulting is
misinformed about how CoBOL works in our environments.

See, we are real people out here, not just words on your screen.   And we are
professionals who have been posting on this newsgroup for years - because we
care more about our profession than most.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-14T22:44:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jixca.352$yX1.98795@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e728355.406452311@news.optonline.net...
> SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:
>
…[8 more quoted lines elided]…
> >>> I use flags extensively. I always use low-value as false. True value
may
> >>be 'y'
> >>> or may be a letter representing the proposition. It is never 1.  I
don't
> >>see
> >>> what difference it makes.
> >>>
> >>The difference is that 1 represents the multiplicative identity  and 0
> >>represents the additive identity in ANY algebra. In a Boolean Algebra,
the
> >>multiplicative identity represents universal truth; and the additive
> >>identity represents the negation of this.
…[11 more quoted lines elided]…
> Name one system where low-values is other than binary zeros.

DISPLAY-7, with odd parity, on an 8 bit machine.

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T05:32:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4uafg$ipi$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net>`

```
Robert Wagner wrote:

> Name one system where low-values is other than binary zeros.

The Cogar/Singer/ICL 1500 series.

This originated by Cogar in late 60s was a desktop networked system using 
coax cabling.  Singer acquired Cogar systems in the early 70s and ICL 
bought Singer Computer division around 1976.

This used a mechanism called 'excess-3' to make the mini-computer CPU 
easier to design and manufacture.

To keep on topic: the founders of MicroFocus Cobol had previously worked 
for ICL Dataskill in Reading, England and had written a Cobol system for 
the ICL 1500.  The MF CIS Cobol had much in common, surprisingly.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T11:21:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e72fdee.437841706@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e71b1e6_2@text-west.newsgroups.com> <40BEA2257607BD82.C723B1DC34012CC4.B745EF7F7E6A1CE4@lp.airnews.net> <3e728355.406452311@news.optonline.net> <b4uafg$ipi$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[13 more quoted lines elided]…
>the ICL 1500.  The MF CIS Cobol had much in common, surprisingly. 

What value does the  Cogar/Singer/ICL 1500 series use for low-values?

Does this have any relevance today?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T19:57:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4vt5b$cla$2@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e728355.406452311@news.optonline.net> <b4uafg$ipi$1@aklobs.kc.net.nz> <3e72fdee.437841706@news.optonline.net>`

```
Robert Wagner wrote:

> Richard Plinston <riplin@Azonic.co.nz> wrote:
> 
…[6 more quoted lines elided]…
> What value does the  Cogar/Singer/ICL 1500 series use for low-values?

Excess-3 has zero as x"03", which is why it is called excess-3.
 
> Does this have any relevance today?

You didn't ask for a _relevant_ system, you just asked for a system.  As it 
happens it did have a form of Cobol on it, and I do have some around here 
still in my pile of obsolete machines, though they haven't been switch on 
for 15 years or so.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T01:56:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7274a3.402689723@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[12 more quoted lines elided]…
>identity represents the negation of this.

Any non-zero value represents 'multiplicative identity' and 'universal truth'..
The value 1 has no special significance. 

I use meaningful values so I can understand them on diagnostic DISPLAYs. 

COBOL doesn't offer bit-sized variables. The smallest we get is a byte. We might
as well use the eight bits to convey human-readable information.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-03-15T00:22:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v75df553hb44b@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e7274a3.402689723@news.optonline.net...
[snip]
> COBOL doesn't offer bit-sized variables. The smallest we get is a byte. We
might
> as well use the eight bits to convey human-readable information.

The COBOL 2002 standard does offer BIT variables.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-14T22:40:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303142240.10dfe29c@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> True value may be 'y'

> COBOL doesn't offer bit-sized variables. 

I used bit fields in ICL 1900 Cobol in the 70s and 80s.  The 24 bit
word of these machines could be PIC S1(23) SYNC RIGHT or PIC 1 OCCURS
24 (or PIC S9(6) COMP SYNC RIGHT).

Fujitsu also has BOOLEAN and BIT usage, as will '2002 standard.

These can only have values 0 or 1.

> The smallest we get is a byte. We might
> as well use the eight bits 

A 'byte' is not necessarily 8 bits, it may be any number of bits as
determined by the machine's architecture.  Common sizes are 6, 8, 9.

> to convey human-readable information.

A 'y' may indicate 'yes' to you, but other languages may interpret
this in different ways.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-15T13:00:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C154220AD8AD60C8.65EAEBF40FA2C418.76907AF29DBAB98A@lp.airnews.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net>`

```
On Sat, 15 Mar 2003 01:56:17 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[18 more quoted lines elided]…
>

It does in Binary which is the very heart and soul of any computer.
How long you been programming?  

>I use meaningful values so I can understand them on diagnostic DISPLAYs. 
>

So displaying 0 (zero) and 1 are not meaningful values if you're just
looking for a switch or flag value?  Easy to say IF 1 display ON.  

>COBOL doesn't offer bit-sized variables. The smallest we get is a byte. We might
>as well use the eight bits to convey human-readable information. 

The 2002 Standard offers bit values.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #109

Program aborting:
Close all that you have worked on.
You ask far too much.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T21:47:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7394d5.476478612@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <C154220AD8AD60C8.65EAEBF40FA2C418.76907AF29DBAB98A@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Sat, 15 Mar 2003 01:56:17 GMT, robert@wagner.net (Robert Wagner)
>enlightened us:
…[19 more quoted lines elided]…
>>Any non-zero value represents 'multiplicative identity' and 'universal
truth'..
>>The value 1 has no special significance. 

>>I use meaningful values so I can understand them on diagnostic DISPLAYs. 
>>
>
>So displaying 0 (zero) and 1 are not meaningful values if you're just
>looking for a switch or flag value?  Easy to say IF 1 display ON.  

I often display multiple indicators on a line. If it reads '1 0 1 1 0', I must
look at code to determine which indicators they are. If it reads 'a   d u  ', I
know at a glance it's an alphabetic word found in the dictionary and written in
upper case.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-15T13:11:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303151311.3c70dd@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message 

> COBOL doesn't offer bit-sized variables. The smallest we get is a byte. We might
> as well use the eight bits to convey human-readable information.

PIC 1 Usage BIT.

Bit-sized variable from COBOL 2002 - already supported by numerous compilers.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-16T01:56:04
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73be51$1_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e7274a3.402689723@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[6 more quoted lines elided]…
> >represents the additive identity in ANY algebra. In a Boolean Algebra,
the
> >multiplicative identity represents universal truth; and the additive
> >identity represents the negation of this.
>
> Any non-zero value represents 'multiplicative identity' and 'universal
truth'..
> The value 1 has no special significance.
>
In a two valued logic system, using 0 and 1, what non-zero value (other than
1) could there be?  As the particular set of Boolean Algebras we deal with
in computing are all based on this particular two valued system, I rest my
case.

In Algebras that have more than two values your statement is axiomatically
false. ("any non-zero value" CAN NOT be used as multiplicative identity.)

And no, I am not threatened by your intellect <G>, neither do I care how you
represent universal truth.

My post is out of respect for George Boole...

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T07:37:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74260a.513656979@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <3e73be51$1_2@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[21 more quoted lines elided]…
>case.

Today's COBOL obliges us to use a 256-valued system, not a two valued system.

>In Algebras that have more than two values your statement is axiomatically
>false. ("any non-zero value" CAN NOT be used as multiplicative identity.)

Why is that? Educate me.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-16T10:08:11
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7431aa_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <3e73be51$1_2@text-west.newsgroups.com> <3e74260a.513656979@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e74260a.513656979@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[20 more quoted lines elided]…
> >In a two valued logic system, using 0 and 1, what non-zero value (other
than
> >1) could there be?  As the particular set of Boolean Algebras we deal
with
> >in computing are all based on this particular two valued system, I rest
my
> >case.
>
> Today's COBOL obliges us to use a 256-valued system, not a two valued
system.
>

Robert, I can't believe you wrote that. It is a two valued LOGIC system.

What it manipulates is a CHARACTER SET, that may indeed be 256 characters.
(Or not...what about Cyrillic, and Asian Character sets that use Double Byte
mode?)

We cannot have 256 outcomes from an IF; it is either TRUE or FALSE. Two
states.

But then you knew that... You were just scratching to refute a case that
can't be refuted. ANYTHING except agree that the case was made <G>...

> >In Algebras that have more than two values your statement is
axiomatically
> >false. ("any non-zero value" CAN NOT be used as multiplicative identity.)
>
> Why is that? Educate me.
>

OK, but don't encourage me to waste my time...If  I do this, I'll expect you
to acknowledge you have received and understood <G>.

In any Algebra, there are certain values that can be applied using the
operations defined in the Algebra, without actually changing whatever they
were used to operate on. (In fact, the system cannnot BE an "Algebra" unless
these values exist...).
Because they don't cause change, they are referred to as "identities" (the
result after using them is identical to the result BEFORE using them...)

For example, if we define the operation of "Multiplication", there exists a
value (1) such that any number "multiplied" by this value remains unchanged.
This is referred to as the "Multiplicative identity".

If we define the operation of "Addition", there exists a value (0) such that
any number "added" to this value remains unchanged. This is referred to as
the "Additive identity".

And so on, for other operations in other Algebras.

A good question might be "Why are these identities important? If they don't
change anything, why do we need them?"

The answer to this is way beyond the scope of what I'm writing here, but as
a general analogy, compare the Roman system of counting and arithmetic
(which had no zero) with the Arabic system that gave us Algebra. Systems
without identities are stunted in what they can do.

Given the definition of Multiplicative Identity explained above, you should
now see that ANY value simply won't cut it as a Multiplicative Identity (it
has to be 1).

In a Boolean Algebra, the Operation of "AND" (which corresponds loosely to
the operation of "Multiplication"  in other systems) uses the Identity 1.
Anything ANDed with 1 remains unchanged. 1 is therefore referred to as the
Multiplicative Identity for any Boolean Algebra, and by extension,
represents a value of TRUE. (If you AND something with TRUE it remains
TRUE). Similarly, if you OR something with Zero, it remains unchanged. So
zero represents the Additive Identity in a Boolean Algebra (as it does in
most other Algebras).

That, in a nutshell, is why I use 1 and zero to represent TRUE and FALSE in
my programs (not just COBOL, but wherever I'm allowed to...)

However, I am not suggesting this is RIGHT or WRONG; only that it is MY
preference.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T17:56:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74b986.23608866@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <3e73be51$1_2@text-west.newsgroups.com> <3e74260a.513656979@news.optonline.net> <3e7431aa_2@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message

>> Today's COBOL obliges us to use a 256-valued system, not a two valued
>system.
…[9 more quoted lines elided]…
>states.

It is true that IF may have only two outcomes, but the indicator may have 255
different states of 'truth'. For example, in the code snippet I posted, a word
may be numeric-word, percent-word, punctuation-word, alphabetic-word, etc. 

>> >In Algebras that have more than two values your statement is
>axiomatically
…[47 more quoted lines elided]…
>my programs (not just COBOL, but wherever I'm allowed to...)

I did learn something -- the concept of _preserving_ identity rather than
changing it.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:10:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b54vhj$7fo$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <3e73be51$1_2@text-west.newsgroups.com> <3e74260a.513656979@news.optonline.net> <3e7431aa_2@text-west.newsgroups.com> <3e74b986.23608866@news.optonline.net>`

```

On 16-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> It is true that IF may have only two outcomes, but the indicator may have 255
> different states of 'truth'. For example, in the code snippet I posted, a word
> may be numeric-word, percent-word, punctuation-word, alphabetic-word, etc.

Why 255?   Because you use ASCII encoding in your code?   How does this
universal CoBOL truth apply to people who use EBCDIC, Double-Byte, and Unicode?

Why do I get the idea that there is only one Truth and that is how you code in
your environment and that the rest of us are all fools for thinking that we have
different needs and environments?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e768cb1.43216146@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <3e73be51$1_2@text-west.newsgroups.com> <3e74260a.513656979@news.optonline.net> <3e7431aa_2@text-west.newsgroups.com> <3e74b986.23608866@news.optonline.net> <b54vhj$7fo$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 16-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
>> It is true that IF may have only two outcomes, but the indicator may have 255
>> different states of 'truth'. For example, in the code snippet I posted, a
word
>> may be numeric-word, percent-word, punctuation-word, alphabetic-word, etc.
>
>Why 255?   Because you use ASCII encoding in your code?   How does this
>universal CoBOL truth apply to people who use EBCDIC, Double-Byte, and Unicode?

Because my compiler and machine use ASCII. EBCDIC is the same. I don't know
double-byte and Unicode. 

>Why do I get the idea that there is only one Truth and that is how you code in
>your environment and that the rest of us are all fools for thinking that we
have
>different needs and environments?

I'm trying to share wisdom gleaned over 40 years of very active practice, so
that neophytes don't have to learn the hard way (trial and error) as we did.
What's wrong with that? I thought that's why newsgroups were formed.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-18T00:46:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303180046.1e6d2902@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3e709310_1@text-west.newsgroups.com> <3e71366b.321213406@news.optonline.net> <3e71b1e6_2@text-west.newsgroups.com> <3e7274a3.402689723@news.optonline.net> <3e73be51$1_2@text-west.newsgroups.com> <3e74260a.513656979@news.optonline.net> <3e7431aa_2@text-west.newsgroups.com> <3e74b986.23608866@news.optonline.net> <b54vhj$7fo$1@peabody.colorado.edu> <3e768cb1.43216146@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> I'm trying to share wisdom gleaned over 40 years of very active practice, 

Unfortunately your 'wisdom' is often not very wise at all.  

> so that neophytes don't have to learn the hard way (trial and error) 

Your 'trial and error' learning is most of the problem, you frequently
don't come out with appropriate conclusions.  You _always_ think that
you _are_ correct, even when you parade what you mis-understood 30
years ago and never bothered to fix.

> What's wrong with that? I thought that's why newsgroups were formed.

It is, but neophytes mostly need protecting _from_ you.
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-13T11:56:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E70E27C.5EF5D883@attglobal.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net>`

```
Robert,
I'm sure where you say "forget the rules of COBOL", you mean that you are adding
to them.  Since we're talking about COBOL code, we cannot "forget the rules".
Colin

>
> Forget the 'rules of COBOL'. Parentheses should always be written when a
> statement contains a mixture of AND and OR, or +/- and multiply or divide.
>
> Robert

I would have to assume you have a reason for saying so, and that it stems directly
from the rules you say to forget.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-14T03:54:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e714520.324978942@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3E70E27C.5EF5D883@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:

>Robert,
>I'm sure where you say "forget the rules of COBOL", you mean that you are
adding
>to them.  Since we're talking about COBOL code, we cannot "forget the rules".
>Colin

I'm saying your programmers will 'forget the rules of COBOL', so don't make
remembrance a precept of the Standard. 

>> Forget the 'rules of COBOL'. Parentheses should always be written when a
>> statement contains a mixture of AND and OR, or +/- and multiply or divide.

You didn't point out the logcal error in the above sentence. If you can't see
it, neither can your programmers.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-14T03:54:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7146ad.325376162@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7005d6.243228562@news.optonline.net> <3E70E27C.5EF5D883@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:

>I would have to assume you have a reason for saying so, and that it stems
directly
>from the rules you say to forget.

This is one of the most error-prone, bug-prone avenues of COBOL. Writing
explicit parentheses solves the problem completely.
```

#### ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-13T06:07:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4psam$jmu$1@slb3.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net>`

```
Colin,
   As usual an excellent document, BUT ... you know me.  A few comments and
suggestions below.
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-13T12:01:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E70E3A0.BC9941A7@attglobal.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net>`

```
As usual, you have something to say, and I agree with just about all of it (and
I don't even mind the three line version of SOURCE-COMPUTER).  You certainly
pointed out some things I forgot to say, like DATA DIVISION phrase alignment.
Maybe this practice is so nearly universal that I forgot it!  Still, it will go
into the revision.
Colin

"William M. Klein" wrote:

> Colin,
>    As usual an excellent document, BUT ... you know me.  A few comments and
…[195 more quoted lines elided]…
> http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/3.2.1.4
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-13T12:54:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303131254.692afc66@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net>`

```
I'm just going to make a comment on one of two of Bill's comments below...

> 
> >
…[13 more quoted lines elided]…
> 

Use caution if they are EC- however.

> 
> - The INITIALIZE statement is your friend.  However, you need to understand
> what it does and does not do (such as the fact that it does NOT change items
> defined as FILLER).
> 

Lest anyone thing that the non initialization of filler is "wrong" - it's not.

It's to allow one to do this:

01  SOCIAL-SEC-NUM.
    03  FIRST-3      pic 999.
    03  FILLER       PIC X VALUE "-".
    03  SECOND-2     PIC 99.
    03  FILLER       PIC X VALUE "-".
    03  LAST-3       PIC 999.

Then when you INITIALIZE SOCIAL-SEC-NUM you don't lose your "-" characters.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-14T03:54:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e714988.326106989@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>> - The INITIALIZE statement is your friend.  However, you need to understand
>> what it does and does not do (such as the fact that it does NOT change items
…[3 more quoted lines elided]…
>Lest anyone thing that the non initialization of filler is "wrong" - it's not.

Yes, it is wrong. It doesn't initialize FILLERs nor pointers.
>It's to allow one to do this:
>
…[7 more quoted lines elided]…
>Then when you INITIALIZE SOCIAL-SEC-NUM you don't lose your "-" characters.

WMK thinks INITIALIZE should restore initial values. That's plausible. It would
address your objection. But lacking an initial value, it should restore pointers
to null and fillers to spaces (pic x)  or zeros (pic 9 display) or low-values
(any other pic).  I'll write 'move low-values to ...' until they get it right.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-14T06:05:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303140605.353d34c6@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e714988.326106989@news.optonline.net>...
> thaneh@softwaresimple.com (Thane Hubbell) wrote:
> 
…[22 more quoted lines elided]…
> (any other pic).  I'll write 'move low-values to ...' until they get it right.


I hate to jump on the Robert you are wrong bandwagon, but Robert - you
are wrong.

The non initialization of filler is Correct in '85 COBOL and not
broken.  (We were not talking abotu COBOL 2002 features which I will
get into).  I have no clue where your comment on pointers came from,
since there is no usage Pointer in 85 COBOL - whatever an implementor
does with his special values is up to him.

Now with COBOL 2002 you CAN INITIALIZE filler and you can INITIALIZE
to the initial value, so I have no clue where your WMK comments came
from either.  COBOL 85 doesn't - it's not broken.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-14T13:19:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4ta0d$gqt$1@slb5.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com>`

```
Just to be clear, WMK never claimed that he thought that (with an '85
Standard compiler) INITIALIZE *should* change FILLER values.  Apparently Mr.
Wagner (whose notes I am now not even seeing) decided it was safe to ignore
what I wrote and put (incorrect) words in my mouth.

I did, however, point out that users of the INITIALIZE statement need to
know exactly what it does and does not do and I gave the fact that it does
not initialize FILLER items as an example.

As Thane and I are both well aware, there are BUNCHES of enhancements to the
INITIALIZE statement in the 2002 Standard including the option (not default)
to initialize filler items as well as the ability to initialize items to the
original VALUE clause.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T01:56:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7283c2.406561089@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <b4ta0d$gqt$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Just to be clear, WMK never claimed that he thought that (with an '85
>Standard compiler) INITIALIZE *should* change FILLER values.  Apparently Mr.
>Wagner (whose notes I am now not even seeing) decided it was safe to ignore
>what I wrote and put (incorrect) words in my mouth.

I was referring to discussions about how the 2002 standard should work, not what
the 85 standard specified.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T01:56:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e727713.403314021@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e714988.326106989@news.optonline.net>...
>> thaneh@softwaresimple.com (Thane Hubbell) wrote:
>> 
>> >> - The INITIALIZE statement is your friend.  However, you need to
understand
>> >> what it does and does not do (such as the fact that it does NOT change
items
>> >> defined as FILLER).
>> >> 
>> >
>> >Lest anyone thing that the non initialization of filler is "wrong" - it's
not.
>> 
>> Yes, it is wrong. It doesn't initialize FILLERs nor pointers.
…[10 more quoted lines elided]…
>> 

>I hate to jump on the Robert you are wrong bandwagon, but Robert - you
>are wrong.
…[5 more quoted lines elided]…
>does with his special values is up to him.

I don't dispute that compilers follow the 85 standard. I'm talking about about
how INITITIALIZE 'should' work. 

>Now with COBOL 2002 you CAN INITIALIZE filler and you can INITIALIZE
>to the initial value, so I have no clue where your WMK comments came
>from either.  COBOL 85 doesn't - it's not broken.

The 2002 solution is a political compromise. INITIALIZE should clear everything
without needing to add special syntax for FILLERs and initial values
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T05:16:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4u9g6$i9t$2@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net>`

```
Robert Wagner wrote:

> INITIALIZE should clear
> everything without needing to add special syntax for FILLERs and initial
> values

You _can_ make it do that, just put names on the fields instead of FILLER.

The use of 'FILLER' is like saying (in '59 thru '85) 'Don't change this 
field when doing an INITIALIZE'.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-14T22:33:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4uaej$3gt$1@slb9.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz>`

```
I do miss so much <G> when I don't see Robert's original messages.  Now, I
see that he has decided how COBOL statements should work - even though what
he "wants" is simply NOT the way it was designed or is currently implemented
by any conforming compiler.

Let's see what I can say similar to what he said about what INITIALIZE
should do:

A) Move CORRESPONDING should move FILLER items - when I want them copied to
the receiving field

B) CALL should look thru the entire computer for subprograms - even if they
aren't in the "PATH" (PC), STEPLIB/JOBLIB (IBM mainframe) etc

C) Reference modification should allow you to find a specified string of
characters

D) Logic errors in my programs should get compiler errors

  ***

Anyone else have ideas of how the COBOL language "should" work - that would
simply break all the existing  code that relies on compilers that actually
DO follow the Standard language definitions?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T11:21:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7307ff.440419424@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>I do miss so much <G> when I don't see Robert's original messages. 

If you're not listening, there is little point in responding. Someone please
quote this so WMK will see it. 

>A) Move CORRESPONDING should move FILLER items - when I want them copied to
>the receiving field

Nonsense. There is no way to establish correspondence between FILLERs. 

>B) CALL should look thru the entire computer for subprograms - even if they
>aren't in the "PATH" (PC), STEPLIB/JOBLIB (IBM mainframe) etc

Just plain silly. I never said that. 

>C) Reference modification should allow you to find a specified string of
>characters

I never wrote about reference modifiers. I don't like them and never use them. 

>D) Logic errors in my programs should get compiler errors

For the fourth time, you're putting words in my mouth that I never said.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T19:50:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4vsq5$cla$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net>`

```
Robert Wagner wrote:

> "William M. Klein" <wmklein@ix.netcom.com> wrote:
> 
…[3 more quoted lines elided]…
> please quote this so WMK will see it.

He'w not responding to you, he is writing to us.  Let me explain: the <G> 
stands for <grin>, that indicates that he is enjoying missing out.

>>A) Move CORRESPONDING should move FILLER items - when I want them copied
>>to the receiving field
> 
> Nonsense. There is no way to establish correspondence between FILLERs.

Exactly, specifying a field as FILLER means: don't do this one, just as it 
is in INITIALIZE.
 
>>B) CALL should look thru the entire computer for subprograms - even if
>>they aren't in the "PATH" (PC), STEPLIB/JOBLIB (IBM mainframe) etc
…[7 more quoted lines elided]…
> them.

Are they another thing that you tried without reading the manual and didn't 
work the way they _should_ ?
 
>>D) Logic errors in my programs should get compiler errors
> 
> For the fourth time, you're putting words in my mouth that I never said.

Of course you never said them, but they are quite similar to things that 
you _have_ said.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-15T14:23:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5023e$c70$1@slb1.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz>`

```
I see that Robert (in his usual "weird" way) simply SNIPPED (without
indicating it, the sentence that came before my list, i.e.

"Let's see what I can say similar to what he said about what INITIALIZE
should do:"

He never even noticed that I made NO claims that what I listed was what he
said.  I simply said that these "should work like" were SIMILAR to his
absurd statement about how INITIALIZE "should work".
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T21:47:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73966b.476885252@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:


>>>C) Reference modification should allow you to find a specified string of
>>>characters
…[5 more quoted lines elided]…
>work the way they _should_ ?

They are for lazy programmers. They obscure meaning. If you want to subdivide a
string, write a structure and give the substrings meaningful names.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-15T17:24:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yrCdna_1qYd1KO6jXTWchw@giganews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e73966b.476885252@news.optonline.net...
> Richard Plinston <riplin@Azonic.co.nz> wrote:
>
>
> >>>C) Reference modification should allow you to find a specified string
of
> >>>characters
> >>
> >> I never wrote about reference modifiers. I don't like them and never
use
> >> them.
> >
> >Are they another thing that you tried without reading the manual and
didn't
> >work the way they _should_ ?
>
> They are for lazy programmers. They obscure meaning. If you want to
subdivide a
> string, write a structure and give the substrings meaningful names.

Reference modification is like an indoor toilet: once you use one, you'll
wonder how you ever lived without it. Trust me on this.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T01:50:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73cdb8.491044323@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net> <yrCdna_1qYd1KO6jXTWchw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>Reference modification is like an indoor toilet: once you use one, you'll
>wonder how you ever lived without it. Trust me on this.

The real reason I shun reference modification is because it reminds me of Basic.
What a horrid language.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-16T12:18:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5588A7C48F207854.1E9F47EA9E57FEC1.F011A60AC900323E@lp.airnews.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net> <yrCdna_1qYd1KO6jXTWchw@giganews.com> <3e73cdb8.491044323@news.optonline.net>`

```
On Sun, 16 Mar 2003 01:50:23 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"JerryMouse" <nospam@bisusa.com> wrote:
>
…[4 more quoted lines elided]…
>What a horrid language. 

No RPG is a horrid language.  Basic is a very nice language which I've
done a lot with over the years.  But then beauty is in the eye of
beholder.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #109

Program aborting:
Close all that you have worked on.
You ask far too much.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:23:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5509v$7qo$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net> <yrCdna_1qYd1KO6jXTWchw@giganews.com> <3e73cdb8.491044323@news.optonline.net>`

```

On 15-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> >Reference modification is like an indoor toilet: once you use one, you'll
> >wonder how you ever lived without it. Trust me on this.
>
> The real reason I shun reference modification is because it reminds me of
> Basic.   What a horrid language.

What interesting logic!   If it reminds you of Basic, it must be shunned.

And you shun periods because they remind you of English.

I guess we can't argue with logic such as this.   Because we're idiots who don't
learn to accept being put in our place by the real genius.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T23:49:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b50ap0$is4$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net>`

```
Robert Wagner wrote:

> They are for lazy programmers. They obscure meaning. If you want to
> subdivide a string, write a structure and give the substrings meaningful
> names.

No. They are useful for the purpose they were designed to fulfill.  I do a 
fair amount of templating where a text file is the template of an HTML, 
XML, print form, postscript or EDIFAC output with tags marking the 
positions where substitutions are made.

These may start at any point in the line and be any length.  What would you 
suggest as a mechanism for using variable names: a million redefines and 
two levels of GO TO DEPENDING ON to select the correct name for start point 
and length ?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T00:58:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73bd6b.486870771@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net> <b50ap0$is4$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[12 more quoted lines elided]…
>and length ?


Based on incomplete knowledge of the problem (read: I might be wrong), I'd
suggest parsing the input record into words rather than operating on them 'in
situ'. By doing so you've elevated the system from trying to do everything at
one layer to a two-layer approach -- a parser and a syntax analyzer.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-17T07:05:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b514ac$tlq$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net> <b50ap0$is4$1@aklobs.kc.net.nz> <3e73bd6b.486870771@news.optonline.net>`

```
Robert Wagner wrote:

> Based on incomplete knowledge of the problem (read: I might be wrong), I'd

Yes, you might be.

> suggest parsing the input record into words rather than operating on them
> 'in situ'.  By doing so you've elevated the system from trying to do
> everything at one layer to a two-layer approach -- a parser and a syntax
> analyzer.

Yes, you are.

Given that you have no idea how the code is developed or how many 'layers' 
that I have in the actual code, then it presumptuous of you to assert that 
it could be 'elevated' by writing it in some other way.

I don't 'operate in situ', the lines may require repitition and/or packing. 
The template file _is_ parsed, but not into 'words', that woould be quite 
inappropriate, but creates a table of field positions, including start 
point and lengths, which the output 'layer' uses as substitution points.

Also when processing print format templates that will be output as text it 
is important to maintain the columnar relationships.  That is the positions 
in the line are significant, parsing to words will lose that.  HTML, XML, 
and EDIFACT gats packed tightly so 'in situ' doesn't work.  Not that the 
template processor knows what it is working on, there are control lines in 
the template that can charge how it operates.

In most case the tags aren't 'words', the templates aren't like, for 
example, source code.

Reference notation makes it work well and fast.  The alternate that you 
suggested of millions of redefines to cover all possible fields is just a 
non-starter.  UNSTRING/STRING requires control over positions and lengths 
that is just too complicated.  Using PERFORM loops to move character by 
character would work but would be really tedious.

As a solution reference notation is a good fit to the the problem.  So far 
you have suggested two really bad fits.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:19:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5502i$7ki$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net>`

```

On 15-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> >> I never wrote about reference modifiers. I don't like them and never use
> >> them.
…[5 more quoted lines elided]…
> a string, write a structure and give the substrings meaningful names.

There are other uses for reference modifiers.   They are quick and clear ways of
searching for the last space in a string.  They are useful when you are given
copy members or data dictionary members that were designed by someone else but
don't quite fit your current needs - and which copy members are used all over
the place.   (I know you can move the copy members to your own hard coded copy -
but that's getting around the whole object of having copy members - and won't
make your standards committee happy).

Do you object to this code?:
DISPLAY 'SIPR702 ENDS  ' FUNCTION CURRENT-DATE (05:2)
                                      '/' FUNCTION CURRENT-DATE (07:2)
                                      '/' FUNCTION CURRENT-DATE (01:4)
                                      ' ' FUNCTION CURRENT-DATE (09:2)
                                      ':' FUNCTION CURRENT-DATE (11:2)
                                      ':' FUNCTION CURRENT-DATE (13:2)
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e768906.42277795@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <3e7307ff.440419424@news.optonline.net> <b4vsq5$cla$1@aklobs.kc.net.nz> <3e73966b.476885252@news.optonline.net> <b5502i$7ki$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>There are other uses for reference modifiers.   They are quick and clear ways
of
>searching for the last space in a string.  They are useful when you are given
>copy members or data dictionary members that were designed by someone else but
>don't quite fit your current needs - and which copy members are used all over
>the place.   (I know you can move the copy members to your own hard coded copy
-
>but that's getting around the whole object of having copy members - and won't
>make your standards committee happy).
…[7 more quoted lines elided]…
>                                      ':' FUNCTION CURRENT-DATE (13:2)

Yes, I do. Call function current-date ONCE and do your magic on its output. If
you called it a millisecond before midnight, you'd get one date and another
time. Calling it multiple times is simply a waste of cpu time. 

Its output could easily be defined as year, month, day, hour and minute.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T05:40:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4uav1$ipi$2@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:

> Anyone else have ideas of how the COBOL language "should" work - that
> would
> simply break all the existing  code that relies on compilers that actually
> DO follow the Standard language definitions?

The compiler should follow indentation instead of stepping in or out of 
levels using IFs and ELSEs.  Oh no, that was one of Robert Wagner's too.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-15T13:04:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31FB0E1774E0C56B.2B0EAD86989E59F1.42F563963811ED20@lp.airnews.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net>`

```
On Fri, 14 Mar 2003 22:33:21 -0600, "William M. Klein"
<wmklein@ix.netcom.com> enlightened us:

>I do miss so much <G> when I don't see Robert's original messages.  Now, I
>see that he has decided how COBOL statements should work - even though what
…[21 more quoted lines elided]…
>DO follow the Standard language definitions?

Yes, I'd like it to take my poorly written problem statement because I
refuse to follow a "best practise" and write a self linking,
self-running program that will reside in whatever source management
system I have, generate its own JCL (because I'm a mainframe kind of
guy), and do this while I'm out to lunch and not whine when I get the
credit for a brilliant solution.  You think we can get that in the
2004 Standard?

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #109

Program aborting:
Close all that you have worked on.
You ask far too much.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-15T13:39:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qKca.9368$VT.1134868@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <31FB0E1774E0C56B.2B0EAD86989E59F1.42F563963811ED20@lp.airnews.net>`

```

"SkippyPB" <swiegand@neo.NOSPAM.rr.com> wrote in message
>
> Yes, I'd like it to take my poorly written problem statement because I
…[6 more quoted lines elided]…
>
With the new OOP stuff, you can make the source part of the object, then do
a search replacing on paragrapgh names.  Next you invoke the compiler,
recompile "self", invoke the os-object "copy", and do a chain back into
yourself iteratively.  This entirely eliminates the need for the old
fashioned ALTER statement.

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T21:47:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e739873.477404650@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <31FB0E1774E0C56B.2B0EAD86989E59F1.42F563963811ED20@lp.airnews.net> <9qKca.9368$VT.1134868@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:

>"SkippyPB" <swiegand@neo.NOSPAM.rr.com> wrote in message
>>
…[12 more quoted lines elided]…
>fashioned ALTER statement.

Editing source is too crude. The modern way to write self-modifying code is
called 'introspection', which enables a program to look at itself (and others),
then modify its behavior 'in situ'. For compilers that doesn't support
introspection (or reflection), there's always operator overloading. Be sure to
destroy the method after you use it so someone else doesn't inadvertently
stumble into it.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T21:47:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7397a6.477200335@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <31FB0E1774E0C56B.2B0EAD86989E59F1.42F563963811ED20@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>Yes, I'd like it to take my poorly written problem statement because I
>refuse to follow a "best practise" and write a self linking,
…[4 more quoted lines elided]…
>2004 Standard?

Synergy promises all that and more. What's your boss's email? :)
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-16T02:09:38
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73c17f_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b4uaej$3gt$1@slb9.atl.mindspring.net> <31FB0E1774E0C56B.2B0EAD86989E59F1.42F563963811ED20@lp.airnews.net>`

```

"SkippyPB" <swiegand@neo.NOSPAM.rr.com> wrote in message
news:31FB0E1774E0C56B.2B0EAD86989E59F1.42F563963811ED20@lp.airnews.net...
> On Fri, 14 Mar 2003 22:33:21 -0600, "William M. Klein"
> <wmklein@ix.netcom.com> enlightened us:
>
> >I do miss so much <G> when I don't see Robert's original messages.  Now,
I
> >see that he has decided how COBOL statements should work - even though
what
> >he "wants" is simply NOT the way it was designed or is currently
implemented
> >by any conforming compiler.
> >
…[3 more quoted lines elided]…
> >A) Move CORRESPONDING should move FILLER items - when I want them copied
to
> >the receiving field
> >
> >B) CALL should look thru the entire computer for subprograms - even if
they
> >aren't in the "PATH" (PC), STEPLIB/JOBLIB (IBM mainframe) etc
> >
…[7 more quoted lines elided]…
> >Anyone else have ideas of how the COBOL language "should" work - that
would
> >simply break all the existing  code that relies on compilers that
actually
> >DO follow the Standard language definitions?
>
…[7 more quoted lines elided]…
>

Definitely. When it's released in 2050...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:11:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b54vkr$7k6$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz>`

```

On 15-Mar-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > INITIALIZE should clear
> > everything without needing to add special syntax for FILLERs and initial
…[5 more quoted lines elided]…
> field when doing an INITIALIZE'.

Since it no longer costs anything significant in naming a field, this seems to
be a useful difference between FILLER and named fields.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e765c8c.30889871@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <b4u9g6$i9t$2@aklobs.kc.net.nz> <b54vkr$7k6$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 15-Mar-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:
…[11 more quoted lines elided]…
>be a useful difference between FILLER and named fields.

What about indicators? I deliberately avoid giving them a name so that all
access will be through 88 names. So that some buffo doesn't say 'move 'e' to
end-of-file-ind' followed by 'if end-of-file'. The purpose of name omission is
not to avoid initialization, it is to avoid two names for the same indicator.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-15T13:06:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303151306.5e1ea5ac@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e727713.403314021@news.optonline.net>...
> 
> I don't dispute that compilers follow the 85 standard. I'm talking about about
…[7 more quoted lines elided]…
> without needing to add special syntax for FILLERs and initial values

What?  You don't want it backward compatible?  

Maybe this example won't get lost this time.

01  SSN.
    03  First-3 pic 999.
    03  filler pic x value "-".
    03  second-2 pic 99.
    03  filler pic x value "-".
    03  third-part pic 9999.

Initialize SSN 

Gives you the DESIRED result of 000-00-0000

This is a FEATURE not a bug.  This is something that has been widely
used - because it is a FEATURE - intentional.  The news standard keeps
this compatibility so as not to break programs - and allows those who
WANT filler initialized to have it so.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T23:22:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e73aa8d.482039187@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e727713.403314021@news.optonline.net>...
>> 
>> I don't dispute that compilers follow the 85 standard. I'm talking about
about
>> how INITITIALIZE 'should' work. 
>> 
…[4 more quoted lines elided]…
>> The 2002 solution is a political compromise. INITIALIZE should clear
everything
>> without needing to add special syntax for FILLERs and initial values
>
…[18 more quoted lines elided]…
>WANT filler initialized to have it so.

I'll concede backward compatibility is a plausible reason to keep the old rules.


Rather than burdening us with extra syntax, a better solution would be a
compiler option to make it work 'the right way' or 'the old way'. Initial
values, as in the example, should always be set. They were there INITIALly, when
the program was loaded.

I see a dichotomy in the word INITIALIZE. It seems reasonable that INITIALIZE
set everything to its initial state. On most operating systems, that's binary
zeros unless you say VALUE. When a program starts, pic x fields don't have
spaces; they have binary zeros. First-3 doesn't have zeros; it has low-values.

The word "initialize" looks like a misnomer. If I was on the committee, I would
have argued for a new verb: "clear". 

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-17T01:45:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b50hij$ln5$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net>`

```
Robert Wagner wrote:

> Rather than burdening us with extra syntax, a better solution would be a
> compiler option to make it work 'the right way' or 'the old way'. 

It is only your opinion that 'the right way' is not the same as 'the old 
way'.

But using compiler options doesn't avoid any 'burden', it only hides it in 
the compiler configuration file.  

> Initial
> values, as in the example, should always be set. They were there
> INITIALly, when the program was loaded.

> I see a dichotomy in the word INITIALIZE. 

You seem to see a lot of things which don't exist.

Working-Storage may be set with initial values on loading  with a VALUE 
clause or some initial values may be set with the INITIALIZE statement. 

They should be considered as alternatives for W-S. Local storage and file 
section only have initialize.

> It seems reasonable that
> INITIALIZE set everything to its initial state. On most operating systems,
> that's binary zeros unless you say VALUE. 

Yet another of your fundemental lack of understanding of Cobol.

If there are no VALUE clauses, or it is Local-Storage or file section, then 
then there is _NO_ defined default setting.  It is entirely at the whim of 
the vendor what these are set to and no particular value can be relied on.

With MF the compiler options allow the undefined bytes to any specific 
character.  Relying on this is seriously flawed.

> When a program starts, pic x
> fields don't have spaces; they have binary zeros. First-3 doesn't have
> zeros; it has low-values.

No they don't, they have no specific value.  They may be null or spaces or 
whatever was previously in those bytes or some value chosen by the vendor.

This is especially true of local storage and file section.

Your arguments are remarkably shallow.

> The word "initialize" looks like a misnomer. If I was on the committee, I
> would have argued for a new verb: "clear".

If you were on the committee there never would have been any release of the 
standards.  You would still be arguing instead of understanding _why_ 
particular choices were made.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T07:37:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7413e2.509008840@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[4 more quoted lines elided]…
>way'.

All rules in the standard are someone's opinion. There is no 'universal truth'.

>> Initial
>> values, as in the example, should always be set. They were there
…[4 more quoted lines elided]…
>You seem to see a lot of things which don't exist.

Life would be simpler if I had your certitude. I'm burdened with thinking about
the meanings of words.

>> It seems reasonable that
>> INITIALIZE set everything to its initial state. On most operating systems,
>> that's binary zeros unless you say VALUE. 
>
>Yet another of your fundemental lack of understanding of Cobol.

You'd think I'd know COBOL after 40 years and millions of lines of code.  But
no, I need to be told I know nothing. Thank you for the valuable revalation. 

>If there are no VALUE clauses, or it is Local-Storage or file section, then 
>then there is _NO_ defined default setting.  It is entirely at the whim of 
>the vendor what these are set to and no particular value can be relied on.

You use the word 'vendor' as governmental agencies do, as a term of
disparagement.  The vendors in question are Microsoft and IBM, two of the
largest companies in the world. They are not starving waifs scratching at the
door. 

>> When a program starts, pic x
>> fields don't have spaces; they have binary zeros. First-3 doesn't have
…[5 more quoted lines elided]…
>This is especially true of local storage and file section.

I start with the same assumption. But I know they contain binary zeros. I don't
want to depend on it least Mr. Peabody sends me through the time machine to the
Bad Old Days, when one couldn't depend on initial values. 

>> The word "initialize" looks like a misnomer. If I was on the committee, I
>> would have argued for a new verb: "clear".
…[3 more quoted lines elided]…
>particular choices were made.

Your mama wears combat boots.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-16T07:29:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5_ca.8$sK6.8719@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e7413e2.509008840@news.optonline.net...
> Richard Plinston <riplin@Azonic.co.nz> wrote:
>
> >Robert Wagner wrote:
> >
> >> Rather than burdening us with extra syntax, a better solution would be
a
> >> compiler option to make it work 'the right way' or 'the old way'.
> >
…[3 more quoted lines elided]…
> All rules in the standard are someone's opinion. There is no 'universal
truth'.
>

No.  All words in the standard define the language.

Deviations from the standard are opinion.  If you want to understand basic
language theory at all, you have to start realizing that it takes two people
agreeing on a common meaning to define a "language".  All people in the
world deciding that a word has a private meaning is the antithesis of
language.

I'd suggest that you read about the tower of babel in the bible, and start
upgrading your theories from there.  We have come a long way in the last
3000 years or so.

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T17:57:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74b95d.23567896@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e7413e2.509008840@news.optonline.net...
…[21 more quoted lines elided]…
>language.

You make an excellent point. But languages evolve as people agree on 'common
usage' meaning of new words. For instance, we all agree that comp-3 means packed
decimal, even though it doesn't say so in the '85 standard. Commonly used words
are usually adopted in the next standard, just as commonly used English words
find their way into the dictionary. 

Because COBOL uses English words, it has some obligation to define meanings
close to the English meanings. In my opinion, INITIALIZE isn't close enough. It
should set _every_ field in the referenced structure to an initial value. 

Robert
"Hit Enter to exit"
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-16T15:10:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8R4da.364$lQ4.94208@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e74b95d.23567896@news.optonline.net...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
…[6 more quoted lines elided]…
> >> >> Rather than burdening us with extra syntax, a better solution would
be
> >a
> >> >> compiler option to make it work 'the right way' or 'the old way'.
> >> >
> >> >It is only your opinion that 'the right way' is not the same as 'the
old
> >> >way'.
> >>
…[6 more quoted lines elided]…
> >Deviations from the standard are opinion.  If you want to understand
basic
> >language theory at all, you have to start realizing that it takes two
people
> >agreeing on a common meaning to define a "language".  All people in the
> >world deciding that a word has a private meaning is the antithesis of
> >language.
>
> You make an excellent point. But languages evolve as people agree on
'common
> usage' meaning of new words. For instance, we all agree that comp-3 means
packed
> decimal, even though it doesn't say so in the '85 standard. Commonly used
words
> are usually adopted in the next standard, just as commonly used English
words
> find their way into the dictionary.
>
> Because COBOL uses English words, it has some obligation to define
meanings
> close to the English meanings. In my opinion, INITIALIZE isn't close
enough. It
> should set _every_ field in the referenced structure to an initial value.
>

You have stated your opinion ... to late to do any good, as the time to have
done it was when the new standard was being developed.  You have not had a
single person agree with your opinion, and had about a dozen disagree, with
lots of good reasons stated.

Your absolute refusal to acknowlege that, combined with your last hundred
posts or so, leads me to believe that you either do not understand the basic
nature of language, or that you are not really interested in communicating
at all. That is, you are not interested in what the words spoken, written,
or compiled actually DO mean, by common assent.  Instead, you wish to spew
out strings of letters in some private language, that you and you only
understand, then claim the rest of us are rather dumb because we obviously
do not see your point.

When you wish to adopt a common language, for the sake of communication, if
nothing else, then maybe you will be qualified to write a book.  Until then,
the rest of us are going to assume you are making a noise because you like
to hear the sound of your own voice.

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-17T01:36:52
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e750b51_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <8R4da.364$lQ4.94208@news20.bellglobal.com>`

```

"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:8R4da.364$lQ4.94208@news20.bellglobal.com...
>
>  Instead, you wish to spew
…[3 more quoted lines elided]…
>
Ah, now it has dawned on me...

Has anyone ever seen Robert Wagner and Tony Dilworth at the same time <G>?

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-17T14:36:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b53cfe$se9$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e74b95d.23567896@news.optonline.net> <8R4da.364$lQ4.94208@news20.bellglobal.com> <3e750b51_2@text-west.newsgroups.com>`

```
Peter E.C. Dashwood wrote:


> Ah, now it has dawned on me...
> 
> Has anyone ever seen Robert Wagner and Tony Dilworth at the same time <G>?

Much the same in style, but opposite in content.  Put the two in one room 
and sell tickets.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-16T21:29:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%oada.2279$544.131007@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <8R4da.364$lQ4.94208@news20.bellglobal.com> <3e750b51_2@text-west.newsgroups.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3e750b51_2@text-west.newsgroups.com...
>
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
…[4 more quoted lines elided]…
> > understand, then claim the rest of us are rather dumb because we
obviously
> > do not see your point.
> >
…[4 more quoted lines elided]…
> Pete.

I am finding some of the "new age" language theory rather fascinating.  I
wish I had had some of those insights thirty years ago, when I was
developing my "thinking modes".

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-17T19:51:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b52h62$gli$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net>`

```
Robert Wagner wrote:

> For instance, we all agree that comp-3 means packed decimal, 

No we certainly do not.  We can all agree that PACKED DECIMAL means Binary 
Coded Decinal, but the _reason_ that PACKED was introduced into the the 
standard was for the very reason that COMP-3 meant different things in 
different vendors compilers, and especially BCD may have been some other 
COMP-~, or not available at all.

> In my opinion, INITIALIZE isn't
> close enough. It should set _every_ field in the referenced structure to
> an initial value.

Yes, we do know what your opinion is.  However, it seems that no one agrees 
with you at all.

>  languages evolve as people agree on 'common usage'

Either you are going to agree with the standard and everyone else, or you 
are going to 'evolve' your own private language that is not Cobol.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:28:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b550kg$7sg$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net>`

```

On 16-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> For instance, we all agree that comp-3 means packed
> decimal, even though it doesn't say so in the '85 standard.

Then why did they feel a need to add PACKED-DECIMAL to later standards?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-17T14:54:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55cmd$aub$1@slb6.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu>`

```
Because all the compiler vendors who forgot to ask Mr. Wagner first and did
NOT use the IBM (and IBM emulation) syntax COMP-3 convention decided that
providing a TRULY "standard" (and well defined) USAGE was a better idea than
assuming "we all" would agree with Mr. Wagner.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e76606d.31882415@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Because all the compiler vendors who forgot to ask Mr. Wagner first and did
>NOT use the IBM (and IBM emulation) syntax COMP-3 convention decided that
>providing a TRULY "standard" (and well defined) USAGE was a better idea than
>assuming "we all" would agree with Mr. Wagner.

I write in Best Practices, posted to CLC: 

"Packed is an obsolete format where each digit and the sign occupy half a byte,
called a nybble (cute, huh?). On machines designed years ago, operations on
packed numbers were faster than on display because machines offered hardware
support. Modern machines do not, so there is no reason to use packed numbers.
Don't write these to a file because non-COBOL languages do not natively support
this format."

I'm not going to defend a format or nomenclature I said was obsolete.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-18T15:35:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57eb8$i9d$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net>`

```

On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> "Packed is an obsolete format where each digit and the sign occupy half a
> byte,
…[5 more quoted lines elided]…
> this format."

Some modern machines do not offer hardware support to packed numbers.  Other
modern machines do offer hardware support to packed numbers.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77becb.10529796@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 17-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
…[11 more quoted lines elided]…
>modern machines do offer hardware support to packed numbers.

The only 'modern' machines offering support are mainframes .. from IBM, Unisys,
Cray and the like. They're not really modern because of backward compatibility
issues. Intel 16-bit offered some lukewarm support which was dropped (slowed
down) in Intel 32-bit.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 17)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-19T17:12:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b58uck$9nv$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net>`

```
Robert Wagner wrote:


> The only 'modern' machines offering support are mainframes .. from IBM,
> Unisys, Cray and the like. They're not really modern because of backward
> compatibility issues. Intel 16-bit offered some lukewarm support which was
> dropped (slowed down) in Intel 32-bit.

Intel does support BCD, it was not 'dropped' in 32bit, the latest Pentiums 
are fully backwards compatible, it was not 'slowed down', later CPUs 
process BCD faster than older ones.  It may be that FP and Integer have 
been improved more than BCD.

Motorola 680x0 supports BCD, as does derivitives such as DragonBall.  Also 
the Power series and PowerPC, and StongARM and XScale.
```

###### ↳ ↳ ↳ Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 18)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-03-19T15:23:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E78C3B3.446F7290@istar.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b58uck$9nv$1@aklobs.kc.net.nz>`

```
According to www2.hursley.ibm.com/decimal the only current architecture
that has full support for even fixed decimal arithmetic is the z series
from IBM.  Even the i series (AS400) does it through software since the
POWER chip doesn't support decimal other than for decimal adjustment
and/or conversion according to IBM Fellow Mike Cowlishaw (Inventor of
Rexx) who is responsible for the decimal site at IBM.  He may have
overlooked current Unisys machines since I don't know if their decimal
capabilities are in native hardware.  I have seen reports that there is
no support for decimal in the Itanium (64 bit) Intel chip.  

Richard Plinston wrote:
> 
> Robert Wagner wrote:
…[12 more quoted lines elided]…
> the Power series and PowerPC, and StongARM and XScale.
```

###### ↳ ↳ ↳ Re: Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 19)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-19T16:49:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303191649.3918ffd2@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b58uck$9nv$1@aklobs.kc.net.nz> <3E78C3B3.446F7290@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote 

> According to www2.hursley.ibm.com/decimal the only current architecture
> that has full support for even fixed decimal arithmetic is the z series
> from IBM.  

From that site in the FAQ:

"""Most computer architectures other than ?pure RISC? machines do, in
fact, provide some form of decimal arithmetic instructions or support.
These include the Intel x86 architecture (used in PCs), the Motorola
68x architecture and its derivatives (used in Apple?s earlier machines
and the Palm Pilot), the IBM zSeries, the IBM Power PC (iSeries and
pSeries), the HP PA-RISC architecture, and most general-purpose
microprocessors."""

Of course it hinges on your word 'full'. As I said, these CPUs do
_support_ BCD in at least having these as native data types, having
instructions, and catering for nibble overflow. It wasn't 'dropped' or
'made slower' in Intel 32bit CPUs.

> I have seen reports that there is
> no support for decimal in the Itanium (64 bit) Intel chip.  

Itanium is not backwards compatible to Pentium, while the AMD 64bit
CPU is allegedly backwards compatible to their 32bit Athlon/Duron
Pentium compatibles.
```

###### ↳ ↳ ↳ Re: Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-20T09:43:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e798a41.65511034@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b58uck$9nv$1@aklobs.kc.net.nz> <3E78C3B3.446F7290@istar.ca> <217e491a.0303191649.3918ffd2@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote 
>
…[17 more quoted lines elided]…
>'made slower' in Intel 32bit CPUs.

When the 386 was introduced, the number of clocks per decimal instruction went
up significantly whereas others went down.  Since clocks were going off more
rapidly, the decimal instructions were executing faster than earlier machines.
But there was no longer any speed advantage of packed over, say, software
emulation. That's why I said the instructions were 'dropped'. If there's no
speed advantage, there is no reason to use decimal.
```

###### ↳ ↳ ↳ Re: Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 21)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-20T11:29:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303201129.134be8b2@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b58uck$9nv$1@aklobs.kc.net.nz> <3E78C3B3.446F7290@istar.ca> <217e491a.0303191649.3918ffd2@posting.google.com> <3e798a41.65511034@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> But there was no longer any speed advantage of packed over, say, software
> emulation. 

I very much doubt that software emulation would get even close to poor
hardware support.

Frome the Hursley FAQ:

""" Surely software emulation of decimal arithmetic is fast enough?

    No, it is not. The performance of existing software libraries for
decimal arithmetic is very poor compared to hardware speeds. In some
applications, the cost of decimal calculations can exceed even the
costs of input and output and can form as much as 90% of the workload.
See ?The ?telco? benchmark? for an example and measurements on several
implementations."""

> That's why I said the instructions were 'dropped'. If there's no
> speed advantage, there is no reason to use decimal.

The reasons for using decimal have little to do with speed.  In any
case once binary exceeds the hardware size there is significant change
in performance which means that it may not be much faster.

For example I just did a simple check using PIC S9(10)V9(3) with
usages of COMP-5, BINARY, PACKED-DECIMAL and DISPLAY (decimal) doing
an add, a move, a multiply and a divide.

The results were within a few percent and PACKED-DECIMAL was the
_fastest_.

        PACKED-DECIMAL    .45
        BINARY            .50
        DISPLAY           .53
        COMP-5            .53

MS Cobol 5 using OPTSPEED.
```

###### ↳ ↳ ↳ Re: Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-21T01:08:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7a6409.121271300@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b58uck$9nv$1@aklobs.kc.net.nz> <3E78C3B3.446F7290@istar.ca> <217e491a.0303191649.3918ffd2@posting.google.com> <3e798a41.65511034@news.optonline.net> <217e491a.0303201129.134be8b2@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[36 more quoted lines elided]…
>MS Cobol 5 using OPTSPEED.

Not much difference. BINARY and COMP-5 should have been much faster. You cannot
do S9(10V9(3) with integer BINARY and COMP-5. Something is missing here. Please
post source code so we can attempt to duplicate your results.
```

###### ↳ ↳ ↳ Re: Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 23)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-21T13:34:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5dqav$q4s$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e798a41.65511034@news.optonline.net> <217e491a.0303201129.134be8b2@posting.google.com> <3e7a6409.121271300@news.optonline.net>`

```
Robert Wagner wrote:

> Not much difference. BINARY and COMP-5 should have been much faster. 

Why 'should' they be faster.  In fact with Fujitsu these are faster, or 
specifically, the BCD and DISPLAY were slower, but that is probably because 
Fujitsu's emulation software is not as good as MF's use of BCD support in 
Intel processors.

> You cannot do S9(10V9(3) with integer BINARY and COMP-5. 

Can't I just ?  Well you _are_ the authority on these matters, so I must 
have imagined that I compiled and ran these programs and got the result 
values as expected.

> Something is missing here. 

Yes.   ;-)

> Please post source code so we can attempt to duplicate your results.

It's not particularly complicated code, a few PIC S9(10)V9(3) of various 
usages and a handfull of perform loops.

An exercise for the reader.
```

###### ↳ ↳ ↳ Re: Hardware support for decimal was Re: What's Missing in a COBOL Style Guide?

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-22T00:50:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7ba2ac.202854941@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e798a41.65511034@news.optonline.net> <217e491a.0303201129.134be8b2@posting.google.com> <3e7a6409.121271300@news.optonline.net> <b5dqav$q4s$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[4 more quoted lines elided]…
>values as expected.

>> Please post source code so we can attempt to duplicate your results.
>
…[3 more quoted lines elided]…
>An exercise for the reader.

I'll try it this weekend and respond within two days. Picture V on integers is
outside my experience.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-20T17:01:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5cs4o$dsg$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b58uck$9nv$1@aklobs.kc.net.nz>`

```

On 18-Mar-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> Intel does support BCD, it was not 'dropped' in 32bit, the latest Pentiums
> are fully backwards compatible, it was not 'slowed down', later CPUs
> process BCD faster than older ones.  It may be that FP and Integer have
> been improved more than BCD.

I remember the controversy when Intel decided to drop decimal support.  Did
Intel back down?   Or did I miss what the proposal actually was about?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 17)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-20T16:59:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5cs1g$dkp$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net>`

```

On 18-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> >Some modern machines do not offer hardware support to packed numbers.  Other
> >modern machines do offer hardware support to packed numbers.
…[5 more quoted lines elided]…
> down) in Intel 32-bit.

So what is your definition of "modern machines"?   Computers that are not
backwards compatible?

Computers that can't optimize Packed-Decimal code?   If this is your definition,
then your statement that "Modern computers do not" is kind of meaningless.   So
I am looking for a definition that ads some meaning to our conversation.

I am aware that Intel dropped support for packed-decimal.   But this is one chip
design.  Does Sun or Apple offer such support?   (I don't know).
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-21T01:08:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7a5e65.119827177@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 18-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
…[6 more quoted lines elided]…
>> Cray and the like. They're not really modern because of backward
compatibility
>> issues. Intel 16-bit offered some lukewarm support which was dropped (slowed
>> down) in Intel 32-bit.
>
>So what is your definition of "modern machines"?   Computers that are not
>backwards compatible?

Released with the last 3-5 years. 

>Computers that can't optimize Packed-Decimal code?   If this is your
definition,
>then your statement that "Modern computers do not" is kind of meaningless.   So
>I am looking for a definition that ads some meaning to our conversation.
>
>I am aware that Intel dropped support for packed-decimal.   But this is one
chip
>design.  Does Sun or Apple offer such support?   (I don't know).

Timing tests on my Sun SPARC show packed exactly the same as display. 

Apple doesn't support COBOL, so who cares?

Intel support was 'lukewarm' because it was one byte at a time. You had the
overhead of loop control. Since they slowed it down relative to other
instructions, it might as well be gone. I'm fairly sure it's still there on
Pentium. The talk about dropping it must have in reference to the 64-bit
machine.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 19)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-03-20T21:46:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-B60BC2.21465420032003@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net>`

```
In article <3e7a5e65.119827177@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:
>
> Apple doesn't support COBOL, so who cares?
> 

That is really starting to bug me.   I think I'm going to devote some 
serious time to one of the open source Cobols.

I know of three in various states of (dis)repair -- OpenCobol, 
CobolForGCC and TinyCobol.  Has anyone had any experience with any of 
the projects?

Could you give an opinion on which one would or would not be worth some 
porting effort?
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 20)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-21T15:50:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5e29p$tgr$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <joe_zitzelberger-B60BC2.21465420032003@corp.supernews.com>`

```
Joe Zitzelberger wrote:

>> Apple doesn't support COBOL, so who cares?
>> 
 
> That is really starting to bug me.ï¿œï¿œï¿œIï¿œthinkï¿œI'mï¿œgoingï¿œtoï¿œdevoteï¿œsome
> serious time to one of the open source Cobols.

I think there was a note about TheKompany was working on Kobol for Apple 
OS-X.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-21T04:48:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7a8f38.132327930@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <joe_zitzelberger-B60BC2.21465420032003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <3e7a5e65.119827177@news.optonline.net>,
> robert@wagner.net (Robert Wagner) wrote:
…[9 more quoted lines elided]…
>the projects?

I have no direct experience with any of them. Based on reading about them, the
most well developed seems to be Kobol. It isn't really open source, the company
sells it for $50, but it came from that genre so the company would probably
cooperate with porting it to Apple. It's written in C.

It appears to produce real machine language, so 98% of your work would be in the
back-end, generating code for the Power PC. That's tedious business.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 21)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-21T17:18:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5e7g4$vlt$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7a5e65.119827177@news.optonline.net> <joe_zitzelberger-B60BC2.21465420032003@corp.supernews.com> <3e7a8f38.132327930@news.optonline.net>`

```
Robert Wagner wrote:

> It appears to produce real machine language, so 98% of your work would be
> in the back-end, generating code for the Power PC. That's tedious
> business.

No.  Kobol produces C via its cob2c program (bit of a givaway to the 
observant that) which then goes into gcc.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-21T12:23:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7af9fb.159663817@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7a5e65.119827177@news.optonline.net> <joe_zitzelberger-B60BC2.21465420032003@corp.supernews.com> <3e7a8f38.132327930@news.optonline.net> <b5e7g4$vlt$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[5 more quoted lines elided]…
>observant that) which then goes into gcc.

My face is red. (note to self: wake up before writing at midnight)

http://www.thekompany.com/products/kobol/ says it will run on Mac OS X Real
Soon. Meanwhile, Yellow Dog is shipping Linux for Mac. Combining the two
products might mean COBOL on Mac is available today. 

Kobol has a fancy IDE but does not support free-format. Nor does it support
pointers. Cross-compiling pointers to C would be a no-brainer. The Kompany said,
in private correspondence, they'll support both when they release the
2002-compliant version. Don't hold your breath.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 23)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-22T07:17:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5fokm$kj3$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7a8f38.132327930@news.optonline.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net>`

```
Robert Wagner wrote:

> http://www.thekompany.com/products/kobol/ says it will run on Mac OS X
> Real Soon. Meanwhile, Yellow Dog is shipping Linux for Mac. Combining the
> two products might mean COBOL on Mac is available today.

Invalid conclusion.

While Kobol _generates_ C code, it has been compiled to execute using Intel 
instruction set and so will not run on Yellow Dog.

Yellow Dog has been recompiled for the PowerPC and modified as required for 
the Mac environment, this doesn't maen that random Intel based code can be 
loaded and run.
 
> Kobol has a fancy IDE but does not support free-format. Nor does it
> support pointers. 

Kobol is '85 standard (mostly). It may surprise you to discover ...

> Cross-compiling pointers to C would be a no-brainer. The
> Kompany said, in private correspondence, they'll support both when they
> release the 2002-compliant version. Don't hold your breath.

Exactly. When they have a '02 compliant compiler it will support '02 
features - presumably using BASED pointers and not MF usage.

They do say they already have '02 OO syntax working in 1.3.2, but the 
documentation for the product is out of date (1.0).
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-22T00:50:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7b9735.199919629@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7a8f38.132327930@news.optonline.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[7 more quoted lines elided]…
>instruction set and so will not run on Yellow Dog.

The Kobol Web page talks about operating systems, not processors. I assumed
Linux meant all processors that run Linux.

Why couldn't the Kompany simply recompile their Linux compiler to run on
PowerPC? The Linux API should work without modification.

>> Kobol has a fancy IDE but does not support free-format. Nor does it
>> support pointers. 
…[7 more quoted lines elided]…
>documentation for the product is out of date (1.0).

By including OO, they've shown they are not standard purists. It seems odd for
them to include difficult features while showing no interest in easy ones which
have been widely available as extensions for 20 years. 

I speculate they don't know that because they're not COBOL programmers. They
think free-form is new because the first time _they_ saw it was in the 2002
standard. 

It's hard to picture OO COBOL written between card columns 8 and 72. What a
paradigm clash!
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 25)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-22T14:04:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5gggb$uuh$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net>`

```
Robert Wagner wrote:

> Richard Plinston <riplin@Azonic.co.nz> wrote:
> 
> Why couldn't the Kompany simply recompile their Linux compiler to run on
> PowerPC? The Linux API should work without modification.

There is also the issue of the _libraries_. The C code generated from the 
gcc2c processor will rely rather heavily of routines which will actually do 
the grunt work.  But TheKompany are not particularly interested in getting 
Kobol onto other machines, they want to sell the IDE which is their _real_ 
product.

From the web site:

"""System Requirements

   KOBOL supports the following operating systems:

      * Linux
      Any Linux distribution for Intel computers (PowerPC support coming    
      soon)
""""

It does take time to bring out a professional and tested product.

> By including OO, they've shown they are not standard purists. 

Actually it only shows that they can't do it all at once.  They have made 
Kobol as much '85 compliant as they can, and they are introducing '02 
features.

Would you have them wait until they have everything in for '02 and then 
start getting it tested ?

> It seems odd
> for them to include difficult features while showing no interest in easy
> ones which have been widely available as extensions for 20 years.

But they probably won't be doing the 'widely available' ones, only the 
_standard_ ones.  While it may 'seem odd' to you, it probably doesn't to 
them.  After all how many actually use pointers in Cobol ?
 
> They think free-form is new because the first time _they_ saw it was in
> the 2002 standard.

It's irrelevant whether it is 'new' or not.  They were writing an '85 
compiler, not a grab-bag of non-standard features.  I can imagine that 
given a priority list, non-'85 bits would be at the bottom.
 
> It's hard to picture OO COBOL written between card columns 8 and 72. What
> a paradigm clash!

<shrug> I don't like stuff off the screen to the right, it can be easily 
missed.  I write my C, Python and other to fit within all the edit screens 
that I use.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 26)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-21T20:47:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5gir7$pe3$1@slb4.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz>`

```
ROFLOL

 "By including OO, they've shown they are not standard purists."
    and
 "It seems odd for them to include difficult features while showing no
interest in easy ones which have been widely available as extensions for 20
years."

Extensions from WHICH compiler vendor?  (Only the ones that RW thinks are
important - or those that many programmers have used over the past 20 years
and still do, e.g. Tandem, HP, Dec, Unisys, etc - not to mention Fujitsu
extensions that RW "doesn't like" such as Based-Storage and FUNCTION ADDR)

What it APPEARS that Kobol has been doing is

  A) implement the full (???) '85 Standard (the portable definition of COBOL
for *all* programmers and environments - not just those favored by "some"
programmers)

 B) start implementing features from the 2002 Standard (supporting "future"
portability)
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-22T03:10:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E7BC5FB.86DDEAB7@shaw.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net>`

```


"William M. Klein" wrote:

> ROFLOL
>
…[19 more quoted lines elided]…
>

AND :-

> > It's hard to picture OO COBOL written between card columns 8 and 72.
What
> > a paradigm clash!
>

Now if he was to look carefully at recently posted  examples, which did *not*
have a directive set to use 'freeformat'  :-

Starts at Column 8 and  finishes at Column 72 !!!
*>--------------------------------------------------------------
Method-id. "closeFile".
*>--------------------------------------------------------------
Linkage section.
copy "sqlreslt.cpy" replacing ==(tag)== by ==01 lnk==.

Procedure Division returning lnk-SqlResult.

  set ResultOK to true

  if FileOpened
     close Data-file

     if    ws-fileStatus = "00"
           set FileClosed to true

     else  set FileError to true
           invoke super "showFileError" using ws-ErrorParams
     End-if
  End-if

End Method "closeFile".
*>--------------------------------------------------------------

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-22T11:09:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7c408a.243275097@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>ROFLOL
>
…[9 more quoted lines elided]…
>extensions that RW "doesn't like" such as Based-Storage and FUNCTION ADDR)

Extensions from vendors shipping >95% of compilers in use. Does Real World have
any standing here?

>What it APPEARS that Kobol has been doing is
>
…[5 more quoted lines elided]…
>portability)

The appearance I see is a bunch of C++ programmers implementing features they
feel comfortable with, and relying on the '85 standard for all the rest. They
don't understand the COBOL market as it developed over the last 20 years. 

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-23T07:45:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5iel8$toh$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net>`

```
Robert Wagner wrote:

>> "It seems odd for them to include difficult features while showing no
>>interest in easy ones which have been widely available as extensions for
>>20 years."

They haven't been 'for 20 years'.  Pointers and SET ADDRESS OF came in with 
MF version 2.4, IIRC, so that it could be used for Windows programming, 
just over a dozen years ago.

Fujitsu version 3 was still a beta product around 6 years ago (I have some 
betas), the first usable version (4.0) was April 1998.  Of course it 
doesn't actually _support_ what you want, even though it may compile and 
execute it.

> Extensions from vendors shipping >95% of compilers in use. 

What surveys have you done to establish this figure ?  What percetage of 
the market does ACCU and RM have ?

I suspect that in terms of _shipments_ Tiny_Cobol, Open_Cobol and Kobol 
together probably exceeds all commercial versions on a weekly basis.

> The appearance I see is a bunch of C++ programmers implementing features
> they feel comfortable with, and relying on the '85 standard for all the
> rest. They don't understand the COBOL market as it developed over the last
> 20 years.

Then they will fail in the market place.  If you don't like it then don't 
use it.

If you have such a good feel for which features are demanded by users then 
please do write your own compiler and sell it, you should make a fortune, 
or get involved in Open_cobol or Tiny-Cobol (geeez, that would slow them 
down).
```

###### ↳ ↳ ↳ Common compilers (was: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-22T14:11:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5ig21$gvs$1@slb0.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b5iel8$toh$1@aklobs.kc.net.nz...
> Robert Wagner wrote:
>
<snip>
>
> > Extensions from vendors shipping >95% of compilers in use.
…[3 more quoted lines elided]…
>

Pretty soon I am going to need to stop reading even REPLIES to RW - if I
want to avoid an ulcer <G>.

The number of compilers "shipping" (even if a RELIABLE source provided it)
would provide some sort of information, but certainly NOT a "definitive"
answer to which COBOL compilers are in the "most common" usage.

Consider, for example the comparison between an IBM mainframe compiler (with
possibly up to multiple hundreds of users - and thousands and thousands of
"simultaneous" users of its produced object code) with a single Micro Focus
Windows compiler (only licensed for a single PC and requiring separate
run-time licenses for each computer running its produced object code).  What
possible "information" is gained by comparing the number of COMPILERS
shipped by each vendor?

Now consider the case of Fujitsu's *EDUCATIONAL USE ONLY* V3 "free
compiler".  If there are "lots" of these compilers "shipped" - but most (say
at least half) of its users actually do follow the documented restriction
that its object code may NOT be used for commercial purposes (assuming the
V3 compiler was acquired after this rule came into effect), what difference
does it make if MILLIONS of those compilers have been shipped?

When I worked for Micro Focus (before MERANT days - so probably my
information is QUITE out-of-date), both AcuCOBOL and RM/COBOL were as common
(if not more common) for the creation of applications INTENDED for
cross-platform uses (especially if one or more was a UNIX-type environment).
As far as I know, both IBM and Fujitsu which *do* offer UNIX-type systems
today are still relatively "small players" in these environments.

When it comes to the world of NON-IBM mainframes, RW has (as I recall)
admitted his ignorance of current uses of COBOL on such O/S's.   To claim
that anything LIKE only 5% of today's production COBOL code is running on
these environments seems silly even if he does admit that he doesn't know
these environments - and just counting how many compilers is shipped doesn't
mean a thing.  COMPAQ (via its acquisitions/mergers with Dec, Tandem, and
HP) offers a VARIETY of COBOL solutions which are actively used today to
deploy many, MANY production applications.  Similarly Unisys (both of its
"historical sides) has a large percentage of today's production COBOL code.

Bottom-Line:
  As usual (as far as I can tell), RW simply thinks that if he doesn't know
about or hasn't worked (recently) in an environment, it must not be
  - modern (?)
 - commonly used
 - important
 - worth looking at

In fact, the 2002 COBOL Standard *does* include many enhancements that were
first introduced as vendor extensions, e.g. GoBACK (from IBM) and USAGE
POINTER (first from Micro Focus, I think), and Accept/Display Screen Section
(I can't remember its first implementation, but it wasn't Micro Focus or IBM
or Fujitsu).  Furthermore, the 2002 Standard provides FUNCTIONALITY that has
been available (in NON-portable ways) from many vendors, e.g. USAGE
FLOAT-xxxx and BINARY-xxxx, BASED data items, FREE/ALLOCATE statements.

And back to the origin of the original thread, KOBOL seems to be targeting
PORTABLE (by definition - not de facto) COBOL and *not* simply those used to
the extensions common in RW's *limited* experience.
```

###### ↳ ↳ ↳ Re: Common compilers (was: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-22T22:06:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303222206.7e94f911@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <b5ig21$gvs$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote 

> POINTER (first from Micro Focus, I think), 

I can track POINTER back as far as 1991 in MF when it was needed to
handle OS/2 PM stuff.

> and Accept/Display Screen Section
> (I can't remember its first implementation, but it wasn't Micro Focus or IBM
> or Fujitsu). 

There are two different things here: extended ACCEPT/DISPLAY (eg
DISPLAY AT) and Screen SECTION.

MS Cobol 1.x, MF CIS Cobol and RM Cobol all had some sort of extended
ACCEPT/DISPLAY back in the days of CP/M and MP/M. Around 1978.  These,
however were all different.

X/Open produced a standard for this and also for file locking, ISAM
formats (C-ISAM) and several other things which seemed to be primarily
based on MF Level II Cobol.

I don't know exactly where SCREEN SECTION came from but it also was in
X-Open and was implemented by MF Cobol/2
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-23T02:24:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7cfc71.291384925@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[6 more quoted lines elided]…
>just over a dozen years ago.

Realia version 1, ca. 1984, had pointers and free-format. Setting a pointer to
the memory-mapped screen at B000 made screen painting ultra-fast. To get time of
day or check the keyboard buffer, set a pointer to the BIOS data segment at
x'40' and read it directly. No need for time-consuming API calls. Those were the
days ...

>> Extensions from vendors shipping >95% of compilers in use. 
>
…[4 more quoted lines elided]…
>together probably exceeds all commercial versions on a weekly basis.

I'm judging popularity from US employment ads. Outside the mainframe world,
nearly all are for Micro Focus. I've never seen an ad asking for ACCU or RM
skills, and only a few for Fujitsu or VisualAge. 

Do hobbiests use COBOL much? Postings to CLC do not so indicate.
Non-professionals all seem to be students. When a compiler is free or nearly
free, many will download it. How many will actually use it?

>If you have such a good feel for which features are demanded by users then 
>please do write your own compiler and sell it, you should make a fortune, 

I've considered it. A compiler that produced dot-NETcode and sold for less than
$1K would have a chance at success. Its libraries, optimizer and code generator
have already been written by Microsoft. My Demo Program, written in one day,
contained a parser and list structures reasonable for syntax analysis. A full
compiler might take 2-3 months. 

In another life, I wrote a DIBOL-to-COBOL cross-compiler in one month, then
spent another month solving one seemingly insignificant problem -- translating
DIBOL's out-of-line arithmetic error handling to COBOL's in-line ON SIZE ERROR.
That requires tracing all possible flows of control in order to know which error
handler, if any, is enabled when a calculation is executed. This, in turn,
requires back-tracking tree structures to avoid infinite looping when the
program is recursing or simply contains bugs. In retrospect, I shouldn't have
bothered. Ninety-nine percent of DIBOL programs had a single error handler which
reported 'something's wrong' and aborted. But hypothetically, there could have
been multiple handlers, so I wasted a month supporting an unused feature. 

>or get involved in Open_cobol or Tiny-Cobol (geeez, that would slow them 
>down).

That would be a culture clash.  I picture them spending a lot of time debating
abstractions such as LALR(k) regularity as though it meant something other than
"look, Ma, I'm a Real Computer Scientist" rather than cranking code.

TinyCOBOL appears to have started with COBOL 650. After realizing the parser was
inadequate, they switched to yacc. Imagine all the time they wasted writing BNR
definitions of COBOL in an attempt to avoid actual programming. I would have had
the thing done while they were still cursing noise words for making the language
difficult to parse. Slow them down ... yeah, right. 

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-23T07:46:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303230746.37cc246f@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net>`

```
On correction...

robert@wagner.net (Robert Wagner) wrote in message 

> TinyCOBOL appears to have started with COBOL 650. After realizing the parser was
> inadequate, they switched to yacc. Imagine all the time they wasted writing BNR
> definitions of COBOL in an attempt to avoid actual programming. I would have had
> the thing done while they were still cursing noise words for making the language
> difficult to parse. Slow them down ... yeah, right. 


Your facts are in error.  See: http://tiny-cobol.sourceforge.net/history.html
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 31)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-23T18:02:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7df067.21532664@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net> <bfdfc3e8.0303230746.37cc246f@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>On correction...
>
>robert@wagner.net (Robert Wagner) wrote in message 
>
>> TinyCOBOL appears to have started with COBOL 650. After realizing the parser
was
>> inadequate, they switched to yacc. Imagine all the time they wasted writing
BNR
>> definitions of COBOL in an attempt to avoid actual programming. 

>Your facts are in error.  See: http://tiny-cobol.sourceforge.net/history.html

I see. But another page on the site says 

"Effective with version 0.56, the TinyCOBOL compiler default parser is Bison.

 Berkeley's YACC (byacc) version 1.9.3 is now an option.

 Version 1.9.3 of YACC (byacc), which is available on this web page (see below),
has been modified to handle huge grammars such as COBOL. 

 Using previous versions of Berkeley's YACC on the TinyCOBOL grammar, will
result in an abort on a table overflow error"

http://tiny-cobol.sourceforge.net/snapshots.html
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 32)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-23T21:43:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303232143.250f4249@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net> <bfdfc3e8.0303230746.37cc246f@posting.google.com> <3e7df067.21532664@news.optonline.net>`

```
You obviously didn't check my reference.  It mentions nothing about
YACC -- I was simply correcting you on the COBOL 650 origin.  It was
not of COBOL 650 origin.


robert@wagner.net (Robert Wagner) wrote in message news:<3e7df067.21532664@news.optonline.net>...
> thaneh@softwaresimple.com (Thane Hubbell) wrote:
> 
…[24 more quoted lines elided]…
> http://tiny-cobol.sourceforge.net/snapshots.html
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** David Essex <dessex@eol.ca>
- **Date:** 2003-03-24T06:11:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7ee934_2@news.eol.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net>`

```
Robert Wagner wrote:
  > Richard Plinston wrote:
  > ...
…[12 more quoted lines elided]…
  > to parse.

As a TC contributor, who has been involved with the project since early
in it's beginnings (late 1999), I can say that your assumptions and
criticisms are incorrect.

TC was not derived from COBOL650 (nor COBOL7x).

TC is derived from RPCOBOL a DOS based compiler which generated x86
assembler.

It was written by Rildo Pragana, who later released the source code
under the GPL.

It used LEX/YACC from the beginnings.

There were no ' ... BNR definitions', as you claim.

As far as 'debating abstractions such as LALR(k)', yes that has been a
topic of discussion from time to time.

But then again, any one faced with the task of writing a COBOL
scanner/parser will have to deal with the language size and complexity
issues, sooner or later.

In short, LEX/YACC does NOT deal with COBOL very well. Yes there are
some work around, but it isn't pretty nor guaranteed to work all the time.

For a detailed look at some of the issues involved, see BTYACC(1)
(Berkeley's BackTracking YACC), an enhanced version of Berkeley's YACC
(byacc).

As far OC is concerned, it source was derived from TC. It has been
re-written most of it by a single individual. It now has a much cleaner
and leaner parser.

Anyway, given the scope of the TC project, there isn't much for whining.
Just some volunteers with limited time, tools and resources slowly
chewing on an elephant.

So if you would like to contribute some code, I'm sure any open source
COBOL project would be willing to accommodate.


  > ...
  > Using previous versions of Berkeley's YACC on the TinyCOBOL grammar,
  > will result in an abort on a table overflow error"

I'm not sure what you are trying to say.

You can verify the problem using the TC sources.

$make -f Makefile.mingw
flex -oscan.c scan.l
byacc -dv -b htcobol htcobol.y
byacc: 751 shift/reduce conflicts.
byacc: f - maximum table size exceeded

This is due to the fact that BYACC uses short integer types, which
limits the table size to 32K.


1)
BtYacc: Berkeley's BackTracking Yacc
http://www.siber.com/btyacc/
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 31)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-25T02:24:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7fa6cf.43392294@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net> <3e7ee934_2@news.eol.ca>`

```
David Essex <dessex@eol.ca> wrote:

>Robert Wagner wrote:
>  > Richard Plinston wrote:
…[25 more quoted lines elided]…
>under the GPL.

I had read elsewhere it was based on a home-grown compiler. I incorrectly
concluded that might have been COBOL650. Thank you for the correction. Thane
offered essentially the same by pointing me to the TinyCOBOL history page. 

Rildo said his objective was COBOL TSRs (multi-tasking under DOS). FWIW, my TSR
manager enabled Realia programs to be TSRs under DOS. I didn't have to write a
compiler. They weren't reentrant because I didn't think that was necessary on a
single-user machine. 

>It used LEX/YACC from the beginnings.

That I do find surprising. It compiled on Unix but generated code for DOS? 

>There were no ' ... BNR definitions', as you claim.

Sure there are. The yacc Rules are written in BNR. 

>As far as 'debating abstractions such as LALR(k)', yes that has been a
>topic of discussion from time to time.

I knew it. 

>But then again, any one faced with the task of writing a COBOL
>scanner/parser will have to deal with the language size and complexity
…[3 more quoted lines elided]…
>some work around, but it isn't pretty nor guaranteed to work all the time.

How ironic. The tool seeks to eliminate ambiguity, yet the tool (and add ons)
amplifies it. 

>As far OC is concerned, it source was derived from TC. It has been
>re-written most of it by a single individual. It now has a much cleaner
>and leaner parser.

Thanks for the info. I didn't realize they shared a common origin. 

>Anyway, given the scope of the TC project, there isn't much for whining.
>Just some volunteers with limited time, tools and resources slowly
…[3 more quoted lines elided]…
>COBOL project would be willing to accommodate.

I have plenty of spare time, witnessed by my postings to CLC. As I said, it
would be a culture clash. I'd want to write the compiler in COBOL .. the old
fashioned way .. and have its output run under dot-NET.  It would take two
months. Those aren't the goals or methodologies of TC/OC, so  I respectfully
decline. 

>  > ...
>  > Using previous versions of Berkeley's YACC on the TinyCOBOL grammar,
>  > will result in an abort on a table overflow error"
>
>I'm not sure what you are trying to say.

I was quoting a larger passage on the TinyCOBOL Web site. Those weren't my
words, they were the Web site's. The gist was that yacc was the parser. 

>This is due to the fact that BYACC uses short integer types, which
>limits the table size to 32K.

They said Microsoft/IBM were shortsighted by limiting the 16-bit PC to 640K. 32K
is a lot smaller. I'm guessing Berkeley increased the limit to 500,000 entries
(16-bt) rather than 2G (32-bit).  Some things never change.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 32)_

- **From:** David Essex <dessex@eol.ca>
- **Date:** 2003-03-25T01:00:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7ff1e3$1_1@news.eol.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net> <3e7ee934_2@news.eol.ca> <3e7fa6cf.43392294@news.optonline.net>`

```
Robert Wagner wrote:

  > David Essex wrote:
  >
…[3 more quoted lines elided]…
  > It compiled on UN*X but generated code for DOS?

Since it was written using LEX, YACC and C, getting it to compile under
UN*X was not very difficult.

It originally generated Int*l x86 assembler. Alan Cox did the original
port to generate i386 GNU assembler.

So with the aid of GCC, you could create an executable basically from
the project's start.


  >> There were no ' ... BNR definitions', as you claim.
  >
  > Sure there are. The YACC Rules are written in BNR.

I misunderstood what you meant.

BTW, you can find the full COBOL grammar(s) at the following links.

COBOL grammar Version 0.1.1:
http://www.cs.vu.nl/grammars/browsable/cobol/

VS COBOL II grammar Version 1.0.3:
http://www.cs.vu.nl/grammars/browsable/vs-cobol-ii/

  > ...
  > I'd want to write the compiler in COBOL .. the old fashioned way
  > .. and have its output run under dot-NET.
  > It would take two months.

Two months sounds rather optimistic.

There was an open source COBOL parser written in COBOL by Ken Foskey
(http://www.zipworld.com.au/~waratah/).

I do not know how (in)complete it is, or if it is still available.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 33)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-25T10:14:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8025dc.75921994@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <b5gir7$pe3$1@slb4.atl.mindspring.net> <3e7c408a.243275097@news.optonline.net> <b5iel8$toh$1@aklobs.kc.net.nz> <3e7cfc71.291384925@news.optonline.net> <3e7ee934_2@news.eol.ca> <3e7fa6cf.43392294@news.optonline.net> <3e7ff1e3$1_1@news.eol.ca>`

```
David Essex <dessex@eol.ca> wrote:

>Robert Wagner wrote:

>BTW, you can find the full COBOL grammar(s) at the following links.
>
>VS COBOL II grammar Version 1.0.3:
>http://www.cs.vu.nl/grammars/browsable/vs-cobol-ii/

Thank you. My searches didn't find this. 

>There was an open source COBOL parser written in COBOL by Ken Foskey
>(http://www.zipworld.com.au/~waratah/).
>
>I do not know how (in)complete it is, or if it is still available.

It has been deleted. In 2000, Ken wrote in this newsgroup:
"I have one that handles the data division pretty well completely, in
cobol. I creates a cobol array of the definitions so that you can use
the information gained."
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-22T19:39:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7c8c9a.262749649@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[7 more quoted lines elided]…
>the grunt work. 

I take that to mean libraries are written in Intel assembly language. 

>> It seems odd
>> for them to include difficult features while showing no interest in easy
…[4 more quoted lines elided]…
>them.  After all how many actually use pointers in Cobol ?

Free-form _would_ be widely used if it was available from IBM. 

Pointers are required to write systems software and compilers. Omitting them
relegates COBOL to business applications only. Ten years ago I rewrote XCOPY in
16-bit Realia, just to demonstrate the general-purpose capability of COBOL to
another newsgroup. By omitting pointers, Kobol is a step backward.  

I recently worked at Merrill Lynch, where I had access to thousands of source
programs. Out of curiosity, I ran a search for "pointer". It found less than
five hits, all in CICS programs where there was no alternative. 

>> They think free-form is new because the first time _they_ saw it was in
>> the 2002 standard.
…[3 more quoted lines elided]…
>given a priority list, non-'85 bits would be at the bottom.

Micro Focus et al. will be unhappy to hear they've developed "a grab-bag of
non-standard features".

>> It's hard to picture OO COBOL written between card columns 8 and 72. What
>> a paradigm clash!
…[3 more quoted lines elided]…
>that I use.

I agree there, but my editors were designed for screens rather than punched
cards. Viewable lines can be wider than 80 columns.

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-22T15:45:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303221545.4da22f5c@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <3e7c8c9a.262749649@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> I take that to mean libraries are written in Intel assembly language. 

Regardless of whether they are in assembly or C, they need to be made
to work on the Mac, your claim was rather simplistic in that they only
needed to get cob2c to run on the PowerPC.  Most of the Cobol data
types don't map directly to C types and so code is going to be
manipulating the bytes directly, and possibly differently on the two
CPUs.
 
> >But they probably won't be doing the 'widely available' ones, only the 
> >_standard_ ones.  While it may 'seem odd' to you, it probably doesn't to 
> >them.  After all how many actually use pointers in Cobol ?
> 
> Free-form _would_ be widely used if it was available from IBM. 

But it isn't, so it ain't.
 
> Pointers are required to write systems software and compilers. 

I haven't seen anyone wanting to write a compiler in Tiny-Cobol.  In
any case MF wrote their compilers in Cobol from the old CIS Cobol
days.  Certainly no pointers in CIS Cobol, Level II Cobol or Cobol/2
until around 2.4.

> Omitting them relegates COBOL to business applications only.

Your point being ?

> Ten years ago I rewrote XCOPY in
> 16-bit Realia, just to demonstrate the general-purpose capability of COBOL to
> another newsgroup. 

And did they all rush out and buy Cobol compilers ?  I thought not. 
Did they show you more respect ? I thought not.

> By omitting pointers, Kobol is a step backward.  

I doubt that they intended it to be a great leap forward, they are
still trying to catch up to '85.

If you want to use pointers then use C.

As they implement '02 features they will eventually put in pointers
(in the '02' way) one hopes.

> I recently worked at Merrill Lynch, where I had access to thousands of source
> programs. Out of curiosity, I ran a search for "pointer". It found less than
> five hits, all in CICS programs where there was no alternative. 

There you go.  Nobody _wants_ to use them, sometimes it is necessary
to pass an address or even to dereference one.  This can be done
without support from the compiler if it is essential.

I don't think that Kobol is seen as being part of the CICS market.

> Micro Focus et al. will be unhappy to hear they've developed "a grab-bag of
> non-standard features".

Some of these are becoming standard, some are not. MF is obviously
going to be unhappy that their OO was not the one adopted, So too is
Fujitsu and IBM. But now that we know what will be standard it seems
pointless to implement non-standard precursors.

This is why Fujitsu does not support the non-standard MF way of
pointer usage.  They obviously coded it because it _might_ have become
the standard, but now they will drop that way (or: have dropped).
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-22T19:06:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5j1b5$3ms$1@slb1.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <3e7c8c9a.262749649@news.optonline.net> <217e491a.0303221545.4da22f5c@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0303221545.4da22f5c@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote
>
<snip>
> > Micro Focus et al. will be unhappy to hear they've developed "a grab-bag
of
> > non-standard features".
>

I won't say that it is true today (as it may or may not be) but about a
decade ago, when I worked for Micro Focus, it was a STRATEGIC part of their
business plan that programmers could migrate source code *TO* a Micro Focus
compiler - but once they started using many of its "features", it would be
almost impossible to migrate AWAY from it - exactly BECAUSE of its "grab-bag
of non-standard features".

If one looks at several of the Fujitsu "features" - my guess is that they
have a similar "business plan".

There is one (and ONLY one) way to insure (if it is important to you) that
your source code is immediately portable from one ANSI/ISO conforming
compiler to another - and that is to turn on their standard conformance
checking and REQUIRE that no extensions are used.  There are other
approaches for "isolating" extensions - or using extensions that are also
available in other compilers that you CURRENTLY think you may want to port
to.  However, saying that a "new" compiler (e.g. Kobol or PerCOBOL or any of
the "open COBOL" projects) need to implement all the "common" (to you)
extensions in their early releases and to "skip" ANSI/ISO conformance, seems
counter-intuitive to me.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-23T05:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7d21ca.300947582@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5e7g4$vlt$1@aklobs.kc.net.nz> <3e7af9fb.159663817@news.optonline.net> <b5fokm$kj3$1@aklobs.kc.net.nz> <3e7b9735.199919629@news.optonline.net> <b5gggb$uuh$1@aklobs.kc.net.nz> <3e7c8c9a.262749649@news.optonline.net> <217e491a.0303221545.4da22f5c@posting.google.com> <b5j1b5$3ms$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Richard" <riplin@Azonic.co.nz> wrote in message
>news:217e491a.0303221545.4da22f5c@posting.google.com...
…[16 more quoted lines elided]…
>have a similar "business plan".

Excellent point. Adobe .pdf format springs to mind. One can easily convert *TO*
pdf, but it's exceedingly difficult to convert *FROM* pdf to anything else.
That's not an accident; that's a strategic plan. 

>There is one (and ONLY one) way to insure (if it is important to you) that
>your source code is immediately portable from one ANSI/ISO conforming
…[7 more quoted lines elided]…
>counter-intuitive to me.

The only extensions I advocate are pointers and free-form. Pointers use
IDENTICAL syntax on IBM, Micro Focus and Fujitsu. To me, that's a de-facto
standard. Both will be supported by the 2002 standard, although pointers will be
slightly different (gotta move the structures from linkage to based, otherwise
syntax is the same). I'm pleased to see IBM will finally have to capitulate to
free-form. Some septagenarian in Hursley will retire out of contempt.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 20)_

- **From:** David Essex <dessex@eol.ca>
- **Date:** 2003-03-21T06:03:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7af2d3$1_2@news.eol.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <joe_zitzelberger-B60BC2.21465420032003@corp.supernews.com>`

```
Joe Zitzelberger wrote:

   > Robert Wagner wrote:
   >
…[11 more quoted lines elided]…
   > be worth some porting effort?

TC is fairly functional and is available for Linux, BSD, Win32, BeOS.
TC generates i386 assembler, and uses GCC to create a binary.

CobolForGCC is a front end for GCC, but is still in the early stages of
development.

OpenCobol fairly functional and according to the SF project page (1) is
available for Linux, Win32 and the MacOS X.
OC generates C code, and uses GCC to create a binary.

So OC would probably be your best choice, assuming you can get the
auxiliary libraries.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-21T13:56:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5f5m4$lst$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net>`

```

On 20-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> >So what is your definition of "modern machines"?   Computers that are not
> >backwards compatible?
>
> Released with the last 3-5 years.

A new computer design in released in the last 3-5 years?  An upgraded chip
and/or OS?

Seeing that you said:

> Apple doesn't support COBOL, so who cares?

I figure you aren't interested in computers that don't support CoBOL.   Are
there any new computers released in the last 3-5 years that support CoBOL?    I
don't know of any.   Which leaves an upgraded chip and/or OS, which hardly
excludes anybody.    Which platforms are excluded by this definition?

I use a computer with hardware support for packed decimal arithmetic.    You say
modern computers don't have hardware support for packed decimal arithmetic.  
You say that "modern" means "released in the last 3-5 years.   You discount
computers that don't have CoBOL support.   That leads me to infer that there is
some quality in your computer that has been released in the last 3-5 years that
doesn't apply to my computer.  But I am not quite getting a handle on what this
is.  We both have had OS upgrades, so that's not it.  We both have had chip
upgrades, so that's not it.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-22T00:50:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7ba3eb.203174231@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 20-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[6 more quoted lines elided]…
>and/or OS?

Upgraded is good enough. As Richard argued correctly, chronology does not
necessarily indicate modernism. 

>Seeing that you said:
>
…[5 more quoted lines elided]…
>excludes anybody.    Which platforms are excluded by this definition?

The context of the question was packed decimal. COBOL is the only language which
directly supports packed decimal format. Other languages do it through the black
box of class.Currency or class.Decimal, where there's no telling what the
internal format is. 

If the Apple platform doesn't support COBOL, the question of packed decimal
support is moot. 

>I use a computer with hardware support for packed decimal arithmetic.    You
say
>modern computers don't have hardware support for packed decimal arithmetic.  
>You say that "modern" means "released in the last 3-5 years.   You discount
…[4 more quoted lines elided]…
>upgrades, so that's not it. 

The difference between 'modern' machines and yours is (bang/buck).

IBM mainframes running VSE (especially) or MVS (not so bad) have a hard time
delivering performance scaled to cpu speed because of inefficiencies
deliberately designed into the OS during the Glory Years, when IBM made money by
selling hardware upgrades. It shows up most predominantly in (mis-) management
of disk space and access speed. SMS has alleviated that handicap to a large
degree.

Did you know that VSE is the most popular IBM mainframe OS worldwide? It is
seldom used in the US, but is very popular in first, second and third-world
countries outside the US for the simple reason, it's cheap. 

Cheap compared to MVS, but not to a Unix box. I've ported literally thousands of
programs from mainframe to Unix or NT with narry a glitch. Unless they do some
wierd stuff or call the OS, they compile the first time and run as before .. for
a small fraction of the cost. I've also worked on systems where someone before
me did the port. In those cases, new development was in Java or C++, with COBOL
relegated to maintenance (legacy) status. 

Tomorrow, you could move those mainframe batch jobs to HP-UX or Solaris or NT,
and cut hardware costs 90%. The prospect of your manager reading this thread
should scare you. 

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-24T17:02:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5ndmv$rk6$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net>`

```

On 21-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> The context of the question was packed decimal. COBOL is the only language
> which
…[3 more quoted lines elided]…
> internal format is.

So the people who wrote the PL/I, EasyTrieve, and other compilers for mainframe
environments decided to go to the extra work of emulating what they could have
done quickly and safely by using assembly language calls - for what purpose?  
To make the programs run more slowly?

Someone in marketing must have intercepted their documentation and inserted lies
- so that we wouldn't know about this Truth that you have revealed to us.

It must be some type of conspiracy to keep us in the dark.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-25T02:24:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7f8953.35842817@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 21-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
…[10 more quoted lines elided]…
>done quickly and safely by using assembly language calls - for what purpose?  

Whoops, I forgot about PL/I. 

EasyTrieve can be compiled or interpreted. In my experience it is usually run in
interpreted mode. There goes the speed. 

Its competitor, VISION:results (formerly QUICKJOB, before that DYL-280) can also
be compiled or interpreted, but is usually interpreted. DYL-280 could only be
interpreted. DYL-240, the first in the series, was a JIT compiler. It read the
input language, emitted machine language directly into memory, and then branched
to the program it had just compiled. It was lightning fast.  I know because I
wrote it. 

Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-25T15:04:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5pr6b$7br$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net>`

```

On 24-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> Whoops, I forgot about PL/I.
>
…[11 more quoted lines elided]…
> wrote it.

Another competitor is SAS.  It can do more than EasyTrieve, but it is much
harder for a contractor to do a few SAS programs and learn the language from the
manuals available.   I suspect it handles packed decimal natively.

Even interpreted languages can be faster using hardware packed decimal routines
than using software decimal routines.    Especially interpreted languages!
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-25T17:32:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e809141.19545365@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <b5pr6b$7br$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>Another competitor is SAS.  It can do more than EasyTrieve, but it is much
>harder for a contractor to do a few SAS programs and learn the language from
the
>manuals available.   I suspect it handles packed decimal natively.

I suspect it does, too. That's another language I forgot about 

>Even interpreted languages can be faster using hardware packed decimal routines
>than using software decimal routines.    Especially interpreted languages!

If one is concerned about speed, (s)he doesn't use an interpreter in the first
place.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 25)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-03-27T13:15:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5vpld$24o0$1@si05.rsvl.unisys.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <b5pr6b$7br$1@peabody.colorado.edu> <3e809141.19545365@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e809141.19545365@news.optonline.net...

> If one is concerned about speed, (s)he doesn't use an interpreter in the
first place.

Not necessarily; only for programs that are processor-bound.   And although
"processor-bound" COBOL programs do exist, I would contend based on my
experience that they're in the distinct minority, that what takes up elapsed
time on most COBOL programs is I/O or waiting for other events (like data
base activity).

If an interpreted program spends, say, 5% of its time "processing" and the
other 95% waiting for something else to happen, I find it difficult to
believe that a compiled program might offer more than a 5% advantage in
elapsed time over the interpreted version.

Thus, one can be "concerned about" speed without having it be the overriding
criterion in every single case, and it might be much more cost-effective to
"optimize" a handful of processor-hog programs (or even to buy a bigger
hammer!) while still retaining an interpreter-based implementation than it
would be to to convert the entire shop to a different compiler.  Not
everyone who is "concerned about speed" will necessarily eschew
interpretation as a viable approach in every instance.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-26T02:15:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e810c21.19037031@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <b5pr6b$7br$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>Another competitor is SAS.  It can do more than EasyTrieve, but it is much
>harder for a contractor to do a few SAS programs and learn the language from
the
>manuals available.   I suspect it handles packed decimal natively.

I suspect it does, too. That's another language I forgot about. But neither PL/I
nor SAS are supported on Apple, so the question of packed decimal on Apple is
still moot. 

>Even interpreted languages can be faster using hardware packed decimal routines
>than using software decimal routines.    Especially interpreted languages!

If one is concerned about speed, (s)he doesn't use an interpreter in the first
place.  'Fast intrpreter' is an oxymoron.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-26T14:48:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5seju$e9k$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net>`

```

On 25-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> >Even interpreted languages can be faster using hardware packed decimal
> >routines
…[3 more quoted lines elided]…
> place.  'Fast intrpreter' is an oxymoron.

We evaluate our different needs and make our choices.    But once we decide that
SAS is the best tool for a particular job, do we then decide that "since SAS is
an interpreter, we shouldn't be concerned with efficient code"?   We should only
code efficiently with efficient languages?

I think it is the other way around.   With a highly optimized compiled language,
efficient coding is less important than with slower languages.


An analogy:

You are riding a bicycle to work.   Since you chose not to drive a car, should
you eschew shortcuts?   After all, if you were in a hurry, you wouldn't have
taken a bicycle in the first place.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 26)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-27T02:07:13
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e825cd9_2@127.0.0.1>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <b5seju$e9k$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b5seju$e9k$1@peabody.colorado.edu...
>
>
> An analogy:
>
> You are riding a bicycle to work.   Since you chose not to drive a car,
should
> you eschew shortcuts?   After all, if you were in a hurry, you wouldn't
have
> taken a bicycle in the first place.

It's a VERY good analogy Howard.

There may still be a case for avoiding inefficiency (like interpreters)
where speed is of the essence, though.

If you were REALLY in a hurry, you would've taken the car,  bicycle short
cuts or no bicycle short cuts (always assuming you COULD get there faster by
car...).

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-27T01:20:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303270120.51cbb7d5@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <b5seju$e9k$1@peabody.colorado.edu> <3e825cd9_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote 

> If you were REALLY in a hurry, you would've taken the car,  bicycle short
> cuts or no bicycle short cuts (always assuming you COULD get there faster by
> car...).

When I worked in York I used a bicycle and mostly got to work or home
faster than if I had a car. It was a folding bike so that I could fold
it up and catch a bus.  The only problem was little kids with "Mummy,
look at the funny bike".
Here, I can get down to the Bay as fast as a car, but getting home is
somewhat slower.  You would understand as you know Browns Bay.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-27T14:25:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8309e2_1@127.0.0.1>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <b5seju$e9k$1@peabody.colorado.edu> <3e825cd9_2@127.0.0.1> <217e491a.0303270120.51cbb7d5@posting.google.com>`

```
You are fortunate to be in such a beautiful part of Auckland, Richard.

I am now smiling at the image of a man on a folding bike coping with the
hillside at Brown's bay...<G>

Your point is taken, though.

Pete.

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0303270120.51cbb7d5@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> > If you were REALLY in a hurry, you would've taken the car,  bicycle
short
> > cuts or no bicycle short cuts (always assuming you COULD get there
faster by
> > car...).
>
…[5 more quoted lines elided]…
> somewhat slower.  You would understand as you know Browns Bay.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-28T19:35:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5vjq0$iqa$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5seju$e9k$1@peabody.colorado.edu> <3e825cd9_2@127.0.0.1> <217e491a.0303270120.51cbb7d5@posting.google.com> <3e8309e2_1@127.0.0.1>`

```
Peter E.C. Dashwood wrote:

> You are fortunate to be in such a beautiful part of Auckland, Richard.

And its another shitty day in Paradise, looks like it will rain all day, 
I'll use the car   ;-)
 
> I am now smiling at the image of a man on a folding bike coping with the
> hillside at Brown's bay...<G>
 
Something more practical is used here - a 12 speed.

The folding bike is still in Yorkshire at present, the wife is trying to 
get me to look for more work in UK, now that it is starting into Spring 
there, so that she can have another extended holiday.
```

###### ↳ ↳ ↳ OT weather and travel - was:Re: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-28T00:17:39
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8394ac_2@127.0.0.1>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b5seju$e9k$1@peabody.colorado.edu> <3e825cd9_2@127.0.0.1> <217e491a.0303270120.51cbb7d5@posting.google.com> <3e8309e2_1@127.0.0.1> <b5vjq0$iqa$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b5vjq0$iqa$1@aklobs.kc.net.nz...
> Peter E.C. Dashwood wrote:
>
…[13 more quoted lines elided]…
>
I have to say the weather here in the Midlands is really good at the moment.
We are having sunshine and temperatures around 17 during the day, though
falling seriously at night.

On the work front things are picking up a little. With your diverse
background and high skill levels I don't think you'll have too much trouble.
There is a Northern jobs board (in addition to the famous Jobserve) which
has a number of jobs throughout the Midlands and the North...check out:
http://www.theitjobboard.com/r.php?t=3_813_312605_153

I have completed my latest contract and am returning to New Zealand, passing
through L.A and Fiji, next month, so it's possible our paths will cross <G>.
I want to pursue  various personal projects throughout the Kiwi Winter
(which is pretty mild in the Bay). My plan is to take the Summer off, get
some time on the beach at the Mount, recharge the batteries, and then look
at what happens next, around April 2004 (by which time the War MIGHT be over
<G>).

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-27T15:54:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5v6sc$1bd$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1>`

```

On 26-Mar-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> > An analogy:
> >
…[13 more quoted lines elided]…
> car...).

Occasionally the bicycle is quicker than the car, allowing you to zoom across
the bike path across the river or freeway.
And occasionally you need a Q&D report, and the tool that gets it done soonest
is an interpreted tool.   The more efficient the interpreted tool, the more
useful it is.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-27T17:37:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E8337AC.87CD4009@shaw.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> On 26-Mar-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[21 more quoted lines elided]…
> useful it is.

True the bike can be quicker. However it was only late last year that I spoke to
somebody who used to cycle down the bicycle paths provided by the city along the
Bow River to the downtown core. Attractive enough, but not like the continuous
shades of green that you see along the River Thames heading west from Heathrow.
(Currently we are in our 'brown' season with the back lawn grass just showing the
first signs of a green tint).

However our intrepid cyclist threw in the towel when he got a speeding ticket !
Needless to say one of Calgary's 'finest' was part of their dozen or so bicycle
cops <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 29)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-28T00:34:54
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8398b7_2@127.0.0.1>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu> <3E8337AC.87CD4009@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E8337AC.87CD4009@shaw.ca...
>
>
> Howard Brazee wrote:
>
> However our intrepid cyclist threw in the towel when he got a speeding
ticket !
> Needless to say one of Calgary's 'finest' was part of their dozen or so
bicycle
> cops <G>.
>

ROFL!

Is that for real? I heard about cops on bikes being deployed in congested
urban areas, but it was an experiment. Sounds like Calgary found it worked
<G>.

So how long before they have radar traps for skateboards...<G>?

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-28T02:40:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E83B032.AF58B4EC@shaw.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu> <3E8337AC.87CD4009@shaw.ca> <3e8398b7_2@127.0.0.1>`

```


"Peter E.C. Dashwood" wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3E8337AC.87CD4009@shaw.ca...
…[19 more quoted lines elided]…
> Pete.

I wont swear to it, but I think it is verboten to have skateboards on those
pedestrian/bicycle paths <G>

As for our cyclist friend - not to be outdone - he's a DIYourselfer - and at Mom's
request, (he's a Canuck and wife is from Devon)  - he is building Mom's coffin.
Roughly about $1,200 for the home made product as opposed to $3,000 AND upwards from
the 'cemetery sharks'. It's a family affair - got his wife selecting lace etc. to do
the lining !

The 'police bicycle brigade' were used quite successfully to calm mild protesters  in
Calgary during the G8 meeting in Kananaskis country attended by George Dubya Bush and
Tony Blair, and of course the slippery Chirac.

Enjoy your time back in N.Z. How many sheep, one..., two..., three....?   <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 31)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-28T12:13:46
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e843c84_2@127.0.0.1>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu> <3E8337AC.87CD4009@shaw.ca> <3e8398b7_2@127.0.0.1> <3E83B032.AF58B4EC@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E83B032.AF58B4EC@shaw.ca...
>
>
…[6 more quoted lines elided]…
> Enjoy your time back in N.Z. How many sheep, one..., two..., three....?
<G>.
>

Well, the official figure is around 40,000,000 (down from 60,000,000 a few
years back...and 80,000,000 in 1967).

Every time I try and verify this figure I fall asleep.

(As our population is still under 4,000,000, if the sheep ever get organised
we will be in serious trouble....)

Many families in NZ have a lamb as a pet. The kids love bottle feeding them,
and, as they get older, the sheep are more effective than a lawnmower. A
friend of mine told me the following story many years ago and he swears it
is true. (If it isn't, it bloody well OUGHT to be...<G>)

Seems the family pet lamb had grown, as lambs inevitably do, and as it was
getting pretty wild and woolly, they decided to get it shorn.

The Yellow Pages were duly consulted to obtain a sheep shearing service, and
the conversation went something like this:

"G'day, do you guys shear sheep?"
"Yes Sir, we certainly do."
"OK, what's it cost?"
"For 10,000 we charge 90c each, for 50,000 we charge 70c each, and for
75,000 upwards we do 'em for 50c. How many yer got?"
"Er...one."
Hushed silence on the phone line, then...
"Yeah?! So what's his bloody name then....?"

I like the picure of the sheep shearer guy making an appointment in his
Diary and noting whether shampoo and set was also required...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 30)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-03-28T08:42:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2lYga.6653$062.973703@news20.bellglobal.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu> <3E8337AC.87CD4009@shaw.ca> <3e8398b7_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3e8398b7_2@127.0.0.1...
>
> ROFL!
…[8 more quoted lines elided]…
>

All our "park patrol" cops here are on bicycles.  I hear they are so old
fashioned that they still use Cobol for their payroll ... I was quite
startled when when cruised up beside me as I was walking last week to
chastise me for smoking in the park.  I assured him it was a dooby and not
nicotine, and he toddled off quite happily ...

Donald
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-27T12:55:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303271255.7fc01587@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b5v6sc$1bd$1@peabody.colorado.edu>...
> On 26-Mar-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> 
…[21 more quoted lines elided]…
> useful it is.

And let's not forget that interpreted languages provide for faster
development than the compile and execute cycle...
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 28)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-28T00:31:52
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e839801_2@127.0.0.1>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net> <b5ndmv$rk6$1@peabody.colorado.edu> <3e7f8953.35842817@news.optonline.net> <3e810c21.19037031@news.optonline.net> <3e825cd9_2@127.0.0.1> <b5v6sc$1bd$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b5v6sc$1bd$1@peabody.colorado.edu...
>
> On 26-Mar-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > If you were REALLY in a hurry, you would've taken the car,  bicycle
short
> > cuts or no bicycle short cuts (always assuming you COULD get there
faster by
> > car...).
>
> Occasionally the bicycle is quicker than the car, allowing you to zoom
across
> the bike path across the river or freeway.

Howard, please re-read the parenthetical part of  my last statement.
(I just KNEW that somebody would raise the point you have...<G>)

> And occasionally you need a Q&D report, and the tool that gets it done
soonest
> is an interpreted tool.   The more efficient the interpreted tool, the
more
> useful it is.

In which case, speed  (of execution) was not really the essential factor.
Rather, it was speed of development.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 21)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-03-25T07:35:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E803EF8.20883A5B@istar.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net> <b5f5m4$lst$1@peabody.colorado.edu> <3e7ba3eb.203174231@news.optonline.net>`

```
See comments below.
Robert Wagner wrote:
> 
> "Howard Brazee" <howard@brazee.net> wrote:
…[26 more quoted lines elided]…
> internal format is.

PL/1 has always supported packed decimal natively.  I suspect that Rexx
supports it but it may only support display format decimal (to 999
digits I think).  

> 
> If the Apple platform doesn't support COBOL, the question of packed decimal
…[34 more quoted lines elided]…
> should scare you.

Depends on the complexity and the volume.  I have seen successful ports
and have read about ports they had to give up on.  I doubt that the
successful shops saved 90 percent. If they did, either they had low
volume or didn't negotiate their mainframe contracts well.  They may
also have kept older boxes where the environmentals (heat, electricity,
etc.) were more expensive than newer mainframes with their much reduced
environmental load.  Shops also tend to bleed in any conversion. 

> 
> Robert
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 19)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-22T07:25:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5fp4s$kqg$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu> <3e7a5e65.119827177@news.optonline.net>`

```
Robert Wagner wrote:

>>So what is your definition of "modern machines"?  
> 
> Released with the last 3-5 years.

That describes 'recent' machines, not 'modern'.

New variants of the 680x0, Dragonball, have been released in the last 
couple of years (they are used in PDAs and phones), as have new Z80 
derivitives (used in Game Boy and drink machines).  These aren't 'modern'

StrongARM is as modern as one would wish, yet it first came out nearly 20 
years ago,
 
> Timing tests on my Sun SPARC show packed exactly the same as display.

SPARC does not have BCD support.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 18)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-03-20T21:59:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-4F9386.21593920032003@corp.supernews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <b55cmd$aub$1@slb6.atl.mindspring.net> <3e76606d.31882415@news.optonline.net> <b57eb8$i9d$1@peabody.colorado.edu> <3e77becb.10529796@news.optonline.net> <b5cs1g$dkp$1@peabody.colorado.edu>`

```
In article <b5cs1g$dkp$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:
<snip> 
> I am aware that Intel dropped support for packed-decimal.   But this is one 
> chip design.  Does Sun or Apple offer such support?   (I don't know).

Speaking for the Apple/PowerPC line they don't have BCD support in the 
consumer line of chips (601/604/620/740/etc) that I have seen.  It has 
been a few years since I did any PPC assembler, but I just refreshed my 
memory looking through the instruction set and I couldn't find a thing 
related to decimal instructions.

Unless they consider good bit shifting ops 'support' for BCD then it 
just isn't in Power.

Disclaimer:  When BCD instructions were available, like on the 68k 
machines, I never used them.  I could well be overlooking very obvious 
support.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e765e1d.31291149@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 16-Mar-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[3 more quoted lines elided]…
>Then why did they feel a need to add PACKED-DECIMAL to later standards?

You'd have to ask someone on the committee. My guess would be turf battle
between the committee and IBM. In this particular case, IBM won. Comp-3 is used
widely; I cannot recall ever seeing PACKED-DECIMAL except in manuals. 

Rule of thumb: the shorter word will win, because programmers are afraid of
'having to type too much'. The committee might have won if it had chosen PACKED
or PD.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-18T01:47:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303180147.1bf6bc71@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <3e765e1d.31291149@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >> For instance, we all agree that comp-3 means packed
> >> decimal, even though it doesn't say so in the '85 standard.
…[3 more quoted lines elided]…
> You'd have to ask someone on the committee. My guess would be 

You do tend to completely miss the subtleties of irony.

> turf battle
> between the committee and IBM. In this particular case, IBM won. Comp-3 is used
> widely; I cannot recall ever seeing PACKED-DECIMAL except in manuals. 

No. Wrong.  The felt the need to add PACKED-DECIMAL because COMP-3
does _not_ mean packed decimal.  Comp-3 can mean whatever the vendor
wants. Different vendors use COMP-3 for different representations.

Your response does not even make sense in a chronological way.  COMP-3
as BCD existed in IBM from the initial implementation. It is used
widely _in_IBM_circles, possibly some others.

PACKED-DECIMAL came in with '85.  When do you hypothesise the 'turf
war' took place ?  1960 ? 1985 ?

> Rule of thumb: the shorter word will win, because programmers are afraid of
> 'having to type too much'. The committee might have won if it had chosen PACKED
> or PD.

It is all about 'winning' or 'losing' with you isn't it.  To hell with
'truth' and 'knowledge', just make a guess.

> widely; I cannot recall ever seeing PACKED-DECIMAL except in manuals. 
Programmers who care about portability and understand what is, and is
not, standard use PACKED-DECIMAL when required.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77bfe7.10813528@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <3e7413e2.509008840@news.optonline.net> <i5_ca.8$sK6.8719@news20.bellglobal.com> <3e74b95d.23567896@news.optonline.net> <b550kg$7sg$1@peabody.colorado.edu> <3e765e1d.31291149@news.optonline.net> <217e491a.0303180147.1bf6bc71@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[7 more quoted lines elided]…
>You do tend to completely miss the subtleties of irony.

So stop using irony. 

>> turf battle
>> between the committee and IBM. In this particular case, IBM won. Comp-3 is
used
>> widely; I cannot recall ever seeing PACKED-DECIMAL except in manuals. 
>
…[6 more quoted lines elided]…
>widely _in_IBM_circles, possibly some others.

I didn't say anything about chronology. I didn't say PACKED-DECIMAL came
_before_  comp-3. 

>PACKED-DECIMAL came in with '85.  When do you hypothesise the 'turf
>war' took place ?  1960 ? 1985 ?

It came in 1985. 

>> Rule of thumb: the shorter word will win, because programmers are afraid of
>> 'having to type too much'. The committee might have won if it had chosen
PACKED
>> or PD.
>
>It is all about 'winning' or 'losing' with you isn't it.  To hell with
>'truth' and 'knowledge', just make a guess.

I don't make the rules; I just play the game. The real world thinks its about
winning and losing. Checking the market value of your dot-coms and mutual funds
will confirm this. 

>> widely; I cannot recall ever seeing PACKED-DECIMAL except in manuals. 
>Programmers who care about portability and understand what is, and is
>not, standard use PACKED-DECIMAL when required.

As I said in a response to WMK, I knew comp-3 wasn't in the standard but I
didn't know PACKED-DECIMAL was. Had I known that, I would have advocated
PACKED-DECIMAL. There is no point in deviating from the standard unless there is
a significant benefit.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 16)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-19T16:37:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b58sb2$8o0$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e765e1d.31291149@news.optonline.net> <217e491a.0303180147.1bf6bc71@posting.google.com> <3e77bfe7.10813528@news.optonline.net>`

```
Robert Wagner wrote:

>>> turf battle
>>> between the committee and IBM. In this particular case, IBM won. Comp-3
>>> is
> used
>>> widely; I cannot recall ever seeing PACKED-DECIMAL except in manuals.
 
>>PACKED-DECIMAL came in with '85.  When do you hypothesise the 'turf
>>war' took place ?  1960 ? 1985 ?
> 
> It came in 1985.

Has your guess now evolved into being some new historical 'fact' that you 
have invented.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:26:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b550fi$7s8$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz>`

```

On 16-Mar-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> If there are no VALUE clauses, or it is Local-Storage or file section, then
> then there is _NO_ defined default setting.  It is entirely at the whim of
> the vendor what these are set to and no particular value can be relied on.

Local-storage and linkage sections should, IMHO accept Value clauses now that we
have the INITIALIZE command.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-18T06:47:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b555ce$ko8$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>> If there are no VALUE clauses, or it is Local-Storage or file section,
>> then
…[5 more quoted lines elided]…
> that we have the INITIALIZE command.

Another of your little techniques for protecting your ego: instead of 
admitting that you didn't know this was the case, and thus your previous 
assertions were wrong and pointless, you try to switch the argument to some 
other irrelevant issue.

Your demands are extremely shallow.  If you want to establish a particular 
pattern of values in Linkage, local-storage or file section then the tools 
are there, just establish it in W-S (which is what it is there for) and do 
a MOVE.

Any novice with two clues could solve the issue without asking for a change 
in the language, are you too lazy to write a move statement ?

In fact for those areas, if there was a requiremt to do as you opine then 
it would be done with a )hidden) W-S block and a move due to _technical_ 
issues which seem beyond your intellect.

I think that you will be happier with a different language entirely, you 
certainly seem to be unhappy with Cobol, so take your trolls to some other 
group.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T19:22:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5578t$b8o$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b555ce$ko8$1@aklobs.kc.net.nz>`

```

On 17-Mar-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > Local-storage and linkage sections should, IMHO accept Value clauses now
> > that we have the INITIALIZE command.
…[6 more quoted lines elided]…
> Your demands are extremely shallow.

Obviously you don't know the difference between a demand and a statement that
includes "IMHO".   If you review your posts and mine, the answer should be
apparent.

> If you want to establish a particular
> pattern of values in Linkage, local-storage or file section then the tools
> are there, just establish it in W-S (which is what it is there for) and do
> a MOVE.

Which is what I do, obviously.   But we could always do moves instead of
INITIALIZE.  20 years ago, I had INIT records to be moved into fields I wanted
to initialize.   But the initialize is a better way - I just wish we could use
it properly everywhere.

> Any novice with two clues could solve the issue without asking for a change
> in the language, are you too lazy to write a move statement ?

Is it less work to write Value clauses and an INIT command than a MOVE?   It
doesn't seem so to me.   Maybe I'm not lazy enough.   Or maybe I'm thinking
about the maintenance programmers to follow me.

> In fact for those areas, if there was a requiremt to do as you opine then
> it would be done with a )hidden) W-S block and a move due to _technical_
> issues which seem beyond your intellect.

Yes, everything you write about is beyond my intellect, not to mention beyond
all of the other people who have been using this newsgroup for years.  Heck, we
can't even spell the way you do.  You've made it patently obvious how dumb the
world for not doing things your way.

> I think that you will be happier with a different language entirely, you
> certainly seem to be unhappy with Cobol, so take your trolls to some other
> group.

CoBOL is my favorite computer language.  You're the person who has repeatedly
told us how it should be.      I am gratified to learn that you believe that
people who prefer change in the language should switch to another newsgroup.   
It should be extremely easy for you to get one such off of it, leaving it for us
idiots.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-17T17:42:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303171742.6b24cbff@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b555ce$ko8$1@aklobs.kc.net.nz> <b5578t$b8o$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> Obviously you don't know the difference between a demand and a statement that
> includes "IMHO".   If you review your posts and mine, the answer should be
> apparent.

Oops, sorry, I was once again in RW response mode.

I will write 100 lines "I must check messages headers before sounding off.".

(actually I will hit 'dup line' 99 times).
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7663f1.32782985@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b555ce$ko8$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Howard Brazee wrote:
>
…[28 more quoted lines elided]…
>group.

What a comedy. You think you're flaming me when, in fact, you're responding to
Howard Brazee. 

ROTFL.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-17T14:51:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55ch4$n5c$1@slb4.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu>`

```
What an interesting request <G>

Do you think that this is EXACTLY *why* the 2002 Standard *does* allow VALUE
clauses for Linkage and Local-Storage (and file) section  items?  These
value clauses are "ignored" during "initial state" - but are exactly what
are used when the

   INITIALIZE to VALUE  (new with 2002 Standard)

functionality is used.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T21:21:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55e84$ecu$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b55ch4$n5c$1@slb4.atl.mindspring.net>`

```

On 17-Mar-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> What an interesting request <G>
>
…[7 more quoted lines elided]…
> functionality is used.

If I had been more up to date on the new standards, I wouldn't have suggested
that it would be nice to do what the language is going to do anyway, and could
have avoided being abused by Robert Wagner for being so patently idiotic and
demanding.

It's nice to have it confirmed that we are not alone in being idiots, but that
the standards committee is as ignorant and stupid as we apparently are.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-18T10:01:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55go3$pnj$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b55ch4$n5c$1@slb4.atl.mindspring.net> <b55e84$ecu$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

> It's nice to have it confirmed that we are not alone in being idiots, but
> that the standards committee is as ignorant and stupid as we apparently
> are.

RW has demonstrated several times that he completely misses such subtleties 
as irony and sarcasm, so he might see this as being said literally.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-18T13:38:49
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e770606_2@text-west.newsgroups.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b55ch4$n5c$1@slb4.atl.mindspring.net> <b55e84$ecu$1@peabody.colorado.edu> <b55go3$pnj$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b55go3$pnj$1@aklobs.kc.net.nz...
> Howard Brazee wrote:
>
> > It's nice to have it confirmed that we are not alone in being idiots,
but
> > that the standards committee is as ignorant and stupid as we apparently
> > are.
>
> RW has demonstrated several times that he completely misses such
subtleties
> as irony and sarcasm, so he might see this as being said literally.
>
Y' mean it isn't <G>? See, no matter what I may think, I would never make so
bold....

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-17T15:56:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55ga9$c6f$1@slb6.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b55ch4$n5c$1@slb4.atl.mindspring.net>`

```
ERROR - Will Robinson <G>

I just noticed (he said speaking to himself) that I made a dumb mistake in
replying to this thread.

The VALUE clause in Local-Storage section is allowed (as far as I know) in
all existing implementations with the Local-Storage extension.  Furthermore,
this has the EXACT same impact as it does in Working-Storage Section (i.e.
when the program is in "initial state" the item is assigned the specified
value.  Furthermore, in "recursive" programming, each instance of a
Local-Storage gets items with a VALUE clause assigned that value when first
instantiated.  The VALUE of such items are "popped" as one recurses OUT of a
series of instances.

It is only File Section and Linkage Section where it is ignored in "initial
state" - but used in INITIALIZE TO VALUE.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-17T23:57:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E76607E.B390E98D@shaw.ca>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu> <b55ch4$n5c$1@slb4.atl.mindspring.net> <b55ga9$c6f$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:

> ERROR - Will Robinson <G>
>
…[14 more quoted lines elided]…
>

You did qualify that with, "as far as I know".  And so far as I know, I don't
think it will work <G>.

I *know* I can use Level 78s (CONSTANTS) in Net Express methods under
Local-Storage Section - they work. But if I want a table of errors with constant
values then I have to use the M/F extension, (or perhaps 'old style' might be
preferable) - Working-Storage Section in the method. (Hence my pitch for
CONSTANT at the 01 Level to replace above 'extension' which is not COBOL 2002).

Not using Local-Storage in non-OO I'm not sure if the following is valid or
correct usage, but just to try it :-

Program-id. ValueClause.
Local-storage section.
78 Hello1                 value "Hello 1".
01 Hello2       pic x(08) value "Hello 2".
Procedure Division.
display Hello1
display Hello2
STOP RUN.

Hello1 displayed correctly, as I anticipated. The second didn't and from the
animator showed a Hex value of 6C 0D 0E 60 00 00 00 00.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7662c9.32486576@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <b50hij$ln5$1@aklobs.kc.net.nz> <b550fi$7s8$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 16-Mar-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:
…[5 more quoted lines elided]…
>Local-storage and linkage sections should, IMHO accept Value clauses now that
we
>have the INITIALIZE command.

COBOL 2002's ALLOCATE command makes it easier:

ALLOCATE data-name-1 INITIALIZED

7) If both the INITIALIZED phrase and data-name-1 are specified, the allocated
storage is initialized as if an INITIALIZE data-name-1 WITH FILLER ALL TO VALUE
THEN TO DEFAULT statement were executed.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 8)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-16T06:12:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303160612.4d0982cf@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message 

> Rather than burdening us with extra syntax, a better solution would be a
> compiler option to make it work 'the right way' or 'the old way'. Initial
> values, as in the example, should always be set. They were there INITIALly, when
> the program was loaded.

The problem with this solution is that it means that you have to have
the same behavior for the entire program.  That's not desireable -
sometimes I might want the filler initialized, other times I might
not.

> 
> I see a dichotomy in the word INITIALIZE. It seems reasonable that INITIALIZE
…[6 more quoted lines elided]…
> 

Intersting, and I can see why you might think that.... however, don't
consider the "INITIAL" value to be that value that the operating
environment assigns at startup, consider it from the point of view of
the programmer --- it's the Initial value *I* want - and that could be
any number of things considering the need at the time.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T17:57:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e74b6f5.22951937@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>robert@wagner.net (Robert Wagner) wrote in message 
>
>> Rather than burdening us with extra syntax, a better solution would be a
>> compiler option to make it work 'the right way' or 'the old way'. Initial
>> values, as in the example, should always be set. They were there INITIALly,
when
>> the program was loaded.
>
…[3 more quoted lines elided]…
>not.

When a language feature is unpredictable, I avoid using it, preferring to do it
myself. I used to think 'move low-values ..' was predictable. Now I'll have to
write 'move all x'00' ..'

>> I see a dichotomy in the word INITIALIZE. It seems reasonable that INITIALIZE
>> set everything to its initial state. On most operating systems, that's binary
>> zeros unless you say VALUE. When a program starts, pic x fields don't have
>> spaces; they have binary zeros. First-3 doesn't have zeros; it has
low-values.
>> 
>> The word "initialize" looks like a misnomer. If I was on the committee, I
would
>> have argued for a new verb: "clear". 
>> 
…[5 more quoted lines elided]…
>any number of things considering the need at the time.

I can live with that. I think of it in OO terms, as the value set by a
constructor. Whatever NEW does, INITIALIZE should do the same.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-16T14:29:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303161429.271058d@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <3e74b6f5.22951937@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e74b6f5.22951937@news.optonline.net>...
> >
> >The problem with this solution is that it means that you have to have
…[7 more quoted lines elided]…
> 

Huh?  Which part of INITIALIZE is unpredictable?  

> >
> >Intersting, and I can see why you might think that.... however, don't
…[6 more quoted lines elided]…
> constructor. Whatever NEW does, INITIALIZE should do the same.

That's why I sometimes override "NEW" with my own method - to do
something different.  I suppose that makes "NEW" unpredictable as well
and maybe you shouldn't use it.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-16T16:58:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b52vig$61n$1@slb6.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com>`

```
Thane,
  Don't you understand?  According to Mr. Wagner, that which doesn't work
the way that he thinks it SHOULD work is "unpredictable" - that which
differs from what he thinks is "best" is WRONG - that which didn't work the
way he wanted it to at least once in the past 40 years must be dangerous.

If nothing else, he really is quite consistent <G>
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-17T09:34:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e752529.51168182@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e74b6f5.22951937@news.optonline.net>...
>> >
>> >The problem with this solution is that it means that you have to have
…[4 more quoted lines elided]…
>> When a language feature is unpredictable, I avoid using it, preferring to do
it
>> myself. I used to think 'move low-values ..' was predictable. Now I'll have
to
>> write 'move all x'00' ..'
>> 
>
>Huh?  Which part of INITIALIZE is unpredictable?  

The unpredictability comes in maintenance. Consider: 

*> copybook payroll-master
 01  payroll-master.
      ....
*>    05  ytd-earnings                          pic  x9(05)v9(02).
*> ytd-earnings has been replaced by new-ytd-earnings 
*> changed 12/31/1989 by Robert Wagner per change notice 1234 
       05  filler                                     pic s9(05)v9(02).

The field now contains random values aka 'garbage'. 

>> I can live with that. I think of it in OO terms, as the value set by a
>> constructor. Whatever NEW does, INITIALIZE should do the same.
…[3 more quoted lines elided]…
>and maybe you shouldn't use it.

The beauty of OO is putting _you_  in charge of your own destiny, rather than a
standards committee. If you don't like the way NEW works, overload it with your
own method. 

Too bad we cannot overload INITIALIZE as conveniently.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-18T06:56:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b555rn$kvh$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net>`

```
Robert Wagner wrote:

 
> *> copybook payroll-master
>  01  payroll-master.
…[3 more quoted lines elided]…
> *> changed 12/31/1989 by Robert Wagner per change notice 1234
                        ^^^^^^^^^^^^^^^^
>        05  filler                                     pic s9(05)v9(02).
> 
> The field now contains random values aka 'garbage'.

Of course, if you have incompetent maintainers who don't have two clues 
about how the language works then you will get junk.

Anyone who _understood_ Cobol would not have set that to a word that means 
'don't initialise me', and would have changed it to, eg, 'old-ytd-earnings'.

Don't blame the language for your failures.  Learn it and learn how to make 
it work the way that is required.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-17T14:58:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b55ctm$3lc$1@slb6.atl.mindspring.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net> <b555rn$kvh$1@aklobs.kc.net.nz>`

```
Which brings me back to the origin of this discussion where I said that
"INITIALIZE is your friend - but you need to understand exactly what it does
and doesn't do".

Of course Mr. Wagner's rather "odd" example leads one to an interesting
question:  Exactly what difference would it make whether that field was or
was not initialized?  As it was changed to FILLER it could not be explicitly
referenced anywhere in the Procedure Division.  I assume that his "..."
indicated that there were other elementary items in the same record, so it
wouldn't be a problem when the group was referenced.

Seems like this example actually shows how the current (correct) '85
Standard definition of INITIALIZE works in an "intelligent" manner - by ONLY
initializing fields that may be explicitly referenced elsewhere within the
Procedure Division.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e766703.33569129@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net> <b555rn$kvh$1@aklobs.kc.net.nz> <b55ctm$3lc$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Which brings me back to the origin of this discussion where I said that
>"INITIALIZE is your friend - but you need to understand exactly what it does
…[12 more quoted lines elided]…
>Procedure Division.

This is not an "odd" example. It happens every day in the world of maintenance
programming. 

While it is true that the obsolete field cannot be referenced (assuming everyone
uses the copybook, which is not always the case), the file contains garbage in
these byte positions. I'm uncomfortable with garbage in my files. 

I once sent a file to the IRS defined by an IRS-supplied copybook containing
fillers. They rejected it because the fillers has not been 'properly'
initialized to spaces. 

In another article I talked about indicators defined as filler amd referenced
via 88 levels -- SET 88-level to true, if 88-level. There's an instance of
fillers being referenced. 


>
>--
…[16 more quoted lines elided]…
>> > The field now contains random values aka 'garbage'.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-18T02:03:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303180203.51a290fd@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net> <b555rn$kvh$1@aklobs.kc.net.nz> <b55ctm$3lc$1@slb6.atl.mindspring.net> <3e766703.33569129@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >initializing fields that may be explicitly referenced elsewhere within the
                                   ^^^^^^^^^^
> >Procedure Division.

> In another article I talked about indicators defined as filler amd referenced
> via 88 levels -- SET 88-level to true, if 88-level. There's an instance of
> fillers being referenced. 

I'll add 'explicitly' to the growing list of things that RW doesn't understand.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-18T10:27:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A7AD3B50106FA615.C6C52910482D02DE.AB7B5F5E1725CA03@lp.airnews.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net> <b555rn$kvh$1@aklobs.kc.net.nz> <b55ctm$3lc$1@slb6.atl.mindspring.net> <3e766703.33569129@news.optonline.net>`

```
On Tue, 18 Mar 2003 03:17:54 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[50 more quoted lines elided]…
>>> > The field now contains random values aka 'garbage'.

Your example is way past being "odd".  It is ridiculous.  No one in
their right mind would change a field that has wide ranging
implications like ytd-earnings to filler and leave the definition as
you have.

If the field were to be come obsolete, then the proper thing to do
would be to change it to filler and define it as pic x(7).  You could
write a conversion program to clear the field before a first night of
production use if you so desired and that would most likely be
preferred. 

And you complained that the collating sequence options given in this
newsgroup were not "real world".  I can't imagine the above being
"real world" either.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #110

With searching comes loss
And the presence of absence:
"My Novel" not found.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 15)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-03-19T02:54:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030318215434.18805.00000056@mb-ct.aol.com>`
- **References:** `<3e766703.33569129@news.optonline.net>`

```
>From: robert@wagner.net  (Robert Wagner)
>Date: 3/17/03 10:17 PM Eastern Standard Time

>
>I once sent a file to the IRS defined by an IRS-supplied copybook containing
>fillers. They rejected it because the fillers has not been 'properly'
>initialized to spaces. 

Didn't read the specs huh.  When working with any government file the reading
of the specs is an imperative.  There is the right way, the wrong way, and the
government's way (learned from many years of creating 1099's and Medicare
files).
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-17T19:12:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303171912.7979e47d@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >Huh?  Which part of INITIALIZE is unpredictable?  
> 
> The unpredictability comes in maintenance. Consider: 

The action of INITIALIZE is entirely predicatable by following the
rules as laid out in the manual.
 
> The field now contains random values aka 'garbage'. 

No. If an initialise is done on the record then the value of the
FILLER item will be left unchanged from whatever it currently holds. 
This is _NOT_ random and is entirely predictable.  It may be that the
value is from some previous record that had been read, or it may be it
is the system default byte if no record has been read, but the
_action_ of INITIALIZE can be predicted 100%.

> Too bad we cannot overload INITIALIZE as conveniently.

Well, you _can_, in a particualr way, by changing the values that are
output using the REPLACING clause of INITIALISE.

You don't see the conflict in your arguments, obviously.

First you complain that INITIALIZE is unpredictable (when actually the
fault is your inability to accurately predict something that is
deterministic).

Then you wish to have it overloaded.

Now with NEW there is not really an issue with overloading, it is
accepted that it needs to be done for each object and the exact action
can be observed in the class.

If INITIALIZE were 'overloaded' then it _would_ become more difficult
to predict as it would be neccessary to find out which 'version' of
INITIALIZE was being used.
I think that it is 'too bad' that you can't learn to predict the
action of INITIALIZE and want to change the world to match your flawed
expectations.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 12)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-17T21:09:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303172109.512e1314@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e752529.51168182@news.optonline.net>...
> thaneh@softwaresimple.com (Thane Hubbell) wrote:
> 
…[28 more quoted lines elided]…
> 

Just how, pray tell does this have anything at ALL to do with
INITIALIZE.  This is true whether you use initialize or not.  Leftover
data is leftover data.  And it's never "random" values.  It might be
implementor defined what the FILLER is initialized to -- if anything
-- but this is certainly not the fault of initialize, and there is
NOTHING unpredictable.  It's entirely predictable.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-19T03:29:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e77c433.11914427@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <3e74b6f5.22951937@news.optonline.net> <bfdfc3e8.0303161429.271058d@posting.google.com> <3e752529.51168182@news.optonline.net> <bfdfc3e8.0303172109.512e1314@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e752529.51168182@news.optonline.net>...
>> thaneh@softwaresimple.com (Thane Hubbell) wrote:
>> 
…[8 more quoted lines elided]…
>> >> When a language feature is unpredictable, I avoid using it, preferring to
do
>>  it
>> >> myself. I used to think 'move low-values ..' was predictable. Now I'll
have
>>  to
>> >> write 'move all x'00' ..'
…[22 more quoted lines elided]…
>NOTHING unpredictable.  It's entirely predictable.

Because, when you setup a new employee and INITIALIZE his/her record, you get
random values in the obsolete field. If you're a batch program, you might get
the previous employee's year-to-date earnings.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 14)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-19T17:16:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b58uk0$9nv$2@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e752529.51168182@news.optonline.net> <bfdfc3e8.0303172109.512e1314@posting.google.com> <3e77c433.11914427@news.optonline.net>`

```
Robert Wagner wrote:

>>-- but this is certainly not the fault of initialize, and there is
>>NOTHING unpredictable.  It's entirely predictable.
…[3 more quoted lines elided]…
> might get the previous employee's year-to-date earnings.

What part of 'predictable' do you not understand ?

You have been told how to make INITIALIZE do what you require.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-17T17:32:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b550qo$847$1@peabody.colorado.edu>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com>`

```

On 16-Mar-2003, thaneh@softwaresimple.com (Thane Hubbell) wrote:

> > Rather than burdening us with extra syntax, a better solution would be a
> > compiler option to make it work 'the right way' or 'the old way'. Initial
…[7 more quoted lines elided]…
> not.

Another problem is that many shops standardize on one set of compiler options. 
Such standardization is very nice when you are compiling a fix to an existing
program in the middle of the night and might not know what that program's
compiler options were.  (Endevor doesn't keep the options that we stick in the
front of the source code).
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-18T03:17:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e766a70.34446463@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <b550qo$847$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 16-Mar-2003, thaneh@softwaresimple.com (Thane Hubbell) wrote:
…[16 more quoted lines elided]…
>front of the source code).    

Good point. You'd want 'the right way' for new programs and 'the old way' for
legacy programs (pending review of INITIALIZE commands therein). Endevor isn't
smart enough to distinguish between legacy and new. Actually, it is, but
administrators can't be bothered to maintain the tables. So you're stuck with a
Procristian one-size-fits-all set of compiler options. 

That's yet another price you pay for lazy use of CM software.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-18T00:28:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303180028.186ace93@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <bfdfc3e8.0303151306.5e1ea5ac@posting.google.com> <3e73aa8d.482039187@news.optonline.net> <bfdfc3e8.0303160612.4d0982cf@posting.google.com> <b550qo$847$1@peabody.colorado.edu> <3e766a70.34446463@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> Good point. You'd want 'the right way' for new programs and 'the old way' for
> legacy programs (pending review of INITIALIZE commands therein). 

Given that 'the old way' _is_ 'the right way' (in spite of you not
understanding this) then there is no problem at all.

> That's yet another price you pay for lazy use of CM software.

Price ?  What price ?  Oh, you mean not being able to use RW-BOL ? 
That is a _benefit_ not a price.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-15T17:34:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MrmcnYg1aa-CKu6jXTWcjg@giganews.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net>
>
> The 2002 solution is a political compromise. INITIALIZE should clear
everything
> without needing to add special syntax for FILLERs and initial values
>

Uh, what does 'clear' mean?

01 XXX COMP-3.
  02  XXX-A  PIC 9(3).
  02  FILLER PIC X(650).
  02  XXX-B  PIC 9(7).

So what should INITIALIZE put in the above FILLER to "clear" it?

How about:
01  MASTER.
  02  MASTER-MONTHS.
     05  MASTER-MONTH OCCURS 12 PIC 9(5).
  02  MASTER-DAYS.
     05  MASTER-DAY OCCURS 365 PIC 9(5).

01 MASTER-MONTH-ONLY REDEFINES MASTER.
   02 MASTER-MONTH-CLEAR OCCURS 12 PIC 9(5).
   02 FILLER PIC X(4380).

01 MASTER-DAYS-ONLY REDEFINES MASTER.
  02  FILLER OCCURS 12 PIC 9(5).
  02  MASTER-DAY-CLEAR OCCURS 365 PIC 9(5).


Compare the actions of:
INITIALIZE MASTER
INITIALIZE MASTER-MONTH-ONLY
and
INITIALIZE MASTER-DAYS-ONLY
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-16T07:37:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e741285.508659139@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <bfdfc3e8.0303140605.353d34c6@posting.google.com> <3e727713.403314021@news.optonline.net> <MrmcnYg1aa-CKu6jXTWcjg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>
>"Robert Wagner" <robert@wagner.net>
…[13 more quoted lines elided]…
>So what should INITIALIZE put in the above FILLER to "clear" it?

It puts spaces. 

>How about:
>01  MASTER.
…[18 more quoted lines elided]…
>INITIALIZE MASTER-DAYS-ONLY

It puts zeros into cases 1 and 3, spaces into the filler in case 2.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-14T13:12:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303141312.171e287f@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> - The INITIALIZE statement is your friend.  However, you need to understand
> >> what it does and does not do (such as the fact that it does NOT change items
> >> defined as FILLER).

> Yes, it is wrong. It doesn't initialize FILLERs nor pointers.

The qualification above indicates that you need to _understand_
INITIALISE. As you have demonstrated many times before your
understanding is not of Cobol but of some stuff that you invented
decades ago without reading the manual.

INITIALISE is _not_ wrong.  It may not match what your opinion of what
it might do, but that simply indicates that it is your understanding
that is wrong.

> >01  SOCIAL-SEC-NUM.
> >    03  FIRST-3      pic 999.
…[3 more quoted lines elided]…
> >    03  LAST-3       PIC 999.
 
> WMK thinks INITIALIZE should restore initial values. That's plausible. 

WMK is aware of every nuance of INITIALISE.  It will be able to
restore initial values in the '2002 standard.

>  It would address your objection. 

It wasn't an 'objection' it was an 'explanation', a 'clarification'. 
You obviously didn't understand that, but then _anything_ that doesn't
agree with you is 'quibbling' even when it is intended to educate you
to as to how and why it actually works.

> But lacking an initial value, it should restore pointers
> to null and fillers to spaces (pic x)  or zeros (pic 9 display) or low-values
> (any other pic).  

No it _shouldn't_, not in the current standard, it should work exactly
as it is _defined_ to work.  It may well be able to work differently
when told to in some future compilers.

If you want 'filler' to be set to spaces or zero all that is required
is that you give them a name, that is how the INITIALISE knows whether
you want the field set to some initial value or not.

Learn how the language can be instructed to bahave as you want it to
and stop complaining that it doesn't work some other way.

> I'll write 'move low-values to ...' 

It might be very poor practice to move low-values to display numeric
fields, they should be set to all zero, other values _may_ give
incorrect results or may not pass a NUMERIC test.

It is very poor practice to set fields to low-values if they will be
written to a terminal or printer as the behaviour of these is
different from spaces - they will be ignored while a space will move
the output one character to the right.

> until they get it right.

Why don't you get your understanding of Cobol 'right' and then you
will stop making these stupid assertions about how ignorant you are.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-15T01:56:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e72850c.406891435@news.optonline.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <b4psam$jmu$1@slb3.atl.mindspring.net> <bfdfc3e8.0303131254.692afc66@posting.google.com> <3e714988.326106989@news.optonline.net> <217e491a.0303141312.171e287f@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> >> - The INITIALIZE statement is your friend.  However, you need to
understand
>> >> what it does and does not do (such as the fact that it does NOT change
items
>> >> defined as FILLER).
>
…[5 more quoted lines elided]…
>decades ago without reading the manual.

Forgive my ignorance, m'lord, I'm just a COBOL programmer. You said yourself I'm
stupid. Don't now chastise me for failing to underatand INITIALIZE. You can't
have it both ways. 

>If you want 'filler' to be set to spaces or zero all that is required
>is that you give them a name, that is how the INITIALISE knows whether
>you want the field set to some initial value or not.

Bull. I want the structure initialized, whether fields are FILLER or not. 

>It might be very poor practice to move low-values to display numeric
>fields, they should be set to all zero, other values _may_ give
>incorrect results or may not pass a NUMERIC test.

Agreed. I'll initialize them separately if necessary.
```

###### ↳ ↳ ↳ Re: What's Missing in a COBOL Style Guide?

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-16T05:11:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4u97j$i9t$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <3e714988.326106989@news.optonline.net> <217e491a.0303141312.171e287f@posting.google.com> <3e72850c.406891435@news.optonline.net>`

```
Robert Wagner wrote:

>>The qualification above indicates that you need to _understand_
>>INITIALISE. As you have demonstrated many times before your
…[5 more quoted lines elided]…
> INITIALIZE. You can't have it both ways.

I was not chastising you for not understanding initialise, that is 
something that might be cured over time, I was chastising you for arguing 
with people who _do_ understand how it works.
 
>>If you want 'filler' to be set to spaces or zero all that is required
>>is that you give them a name, that is how the INITIALISE knows whether
>>you want the field set to some initial value or not.
 
> Bull. I want the structure initialized, whether fields are FILLER or not.

Then you don't understand why the word FILLER is used.  It is so that the 
field cannot be directly referenced and _doesn't_ take part in certain 
operations, such as initialise (and also DISPLAY UPON CRT).

Perhaps you should write your own language rather than claiming that Cobol 
is 'wrong' when it follows its definition correctly.

>>It might be very poor practice to move low-values to display numeric
>>fields, they should be set to all zero, other values _may_ give
>>incorrect results or may not pass a NUMERIC test.
> 
> Agreed. I'll initialize them separately if necessary.
```

#### ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-13T08:30:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303130830.74d67747@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net>`

```
>  Very short names are desirable for use as subscripts and
>  indexes, but make them at least  two characters long, to
>  simplify finding them when editing a program.  (Think how
>  difficult it would be to find the occurrences of the words 'I'
>  or 'X' as opposed to the word 'IX'!)

In ISPF you can use 'f I word' or 'f X word all'
and find only the single char subscripts.


>3.Using NOT:
>  If you've ever coded 'NOT >' or 'NOT <' relational operators,
…[5 more quoted lines elided]…
>                    Procedure Division Ideas


In the case of Cobol relation operators there is one screwy 
thing that makes me a bit edgy, trying to pronounce the 
operators comes out as:

   <=   -- Less or equal
   =	-- Equal
   >=	-- Greater or equal (huh?!?)

In my well ordered, though often misunderstood, mind this 
ought to be '=>', as one would speak it, 'equal or greater'.

Now I realize that there are many different dialects and
opinions -- some people might actually say 'greater or
equal'.  My personal opinion is that "NOT <" is an easier
read than ">=".  Since I automatically, initially, type
it as "=>", using "NOT <" saves me an extra compile.
												 
Also, as Cobol does not allow '<>' a programmer still needs to
write 'NOT ='.

Anyway, I'm not sure how a programmer can understand any
relational operator without also understanding its
compliment.  They define each other.

<rant>

Not specifically related to relation operators, but to
the general 'NOT is hard to read' idea...

In its most perverted form this rule can actually reduce
readability by requiring odd-looking constructs like:

     IF A=B
	    CONTINUE
     ELSE
	    STATEMENTS WHEN A NOT = B
	 END-IF

The boolean condition of an IF statement can only resolve to 
two states.  It doesn't make much sense to me that a programmer
can understand one state without understanding the other state
completely.  If you can grasp the true condition then the 
not-true is equally graspable as 'everything else'.

</rant>



Finally, I would suggest another comment -- 'Whitespace
and indentation are your friends'.

Grouping lines that are logically executed together,
such as the body of an IF or PERFORM and visually
setting them off from the surrounding statements
is a great assist to readability.
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-13T12:11:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E70E5EC.4E34CE03@attglobal.net>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <16e2f010.0303130830.74d67747@posting.google.com>`

```
Joe,
Thanks for your input.  With respect to your comment about ISPF Editor
"Find", let me point out the following:

I just added the following two statements to a COBOL program:
77 I   BINARY PIC S9(4) VALUE ZERO.
77 I-X BINARY PIC S9(4) VALUE ZERO.

Then, I typed "f i word all".

Result:
Both of the lines I added were highlighted, because the Editor doesn't
treat the hyphen correctly.

(And, by the way, typing "F all 'x' word" results in highlighting the
I-X entry.)

This is precisely the problem that my advice attempts to address.
Colin

Joe Zitzelberger wrote:

> >  Very short names are desirable for use as subscripts and
> >  indexes, but make them at least  two characters long, to
…[5 more quoted lines elided]…
> and find only the single char subscripts.
```

##### ↳ ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-14T20:36:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4qj62$vk8$1@aklobs.kc.net.nz>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net> <16e2f010.0303130830.74d67747@posting.google.com>`

```
Joe Zitzelberger wrote:

> Now I realize that there are many different dialects and
> opinions -- some people might actually say 'greater or
> equal'.  

They do.

If fact if you wanted to use the long form of Cobol it would be:

    IF variable-1 IS GREATER THAN OR EQUAL TO variable-2
    THEN ...

However, NOT < is OK too.
```

#### ↳ Re: What's Missing in a COBOL Style Guide?

- **From:** bdhobbs18@acm.org (Bill Hobbs)
- **Date:** 2003-03-19T10:37:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ca5032.0303191037.35b2d2df@posting.google.com>`
- **References:** `<3E6FC7EC.8EF66036@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote in message news:<3E6FC7EC.8EF66036@attglobal.net>...
> Folks,
> You provided lots of great input when I posted a proposed COBOL
> Programming Standard a few days ago.  One thing that came up repeatedly,
> both in this newsgroup and within my company was "show us examples of
> how to code, not just the prohibitions about what we cannot code".

I've been following these style threads off and on, and I thought that
I would muddy the waters once again.  :-)

If an experienced programmer already has a style that is fairly
consistent and generally easy to work with, why mess with their head
by imposing a possibly incompatible style on them?

Look at the threads we have about periods, if not, internal/external
sort, etc..  If I dictate to others what is acceptable and
unacceptable coding practices, might I be responsible if the quality
of their code decreases because they're having to deal with style
changes?  What's that saying ... "if it works, don't fix it".

Back in the early 1990s, the colonel I worked for sent a memo to the
directorate stating that from now on the only word processor that
would be used would be WordPerfect.  I asked him why he directed this
change, he said that he was tried of receiving documents that he
couldn't open.  I told him that this would cost quite a bit as there
were several hundred PCs that I was aware of, and there were probably
many more that I wasn't aware of.  He showed me the Army's site
license for WordPerfect.  (It was refreshing to see that someone had
done their homework for a change.)  Then I asked him about training. 
They already know a word processor, they won't need training, he said.
 I pointed out that he had just completed training in a new messaging
system, he had known the old one, so he probably wasted a bunch of
taxpayer dollars.  Uh, that's different, said he.  I went for the
jugular - his own secretary had told me that they would never find my
body if I messed with her copy of MultiMate (I think it was called
MultiMate, it's been awhile).

He sighed, we may have a problem.  Seems she had been there since dirt
was new, and he was pretty sure he was going to lose that argument. 
And she wasn't alone - I think she was the shop steward for the Cranky
Old Secretaries Union 205.  He asked me if there were other options. 
I showed him a conversion utility, SoftwareBridge I think, that
converted between a bunch of word processor formats.  I suggested that
we get a site license, I could train users in about ten minutes, and
we wouldn't have to fear for our lives or careers.

The next memo rescinded the previous, gave directions how to get the
utility, and *suggested* that anyone who doesn't already know a word
processor get and use WordPerfect under the Army's site license.

The point that I'm trying to make is that some folk may have invested
quite a bit in making their style consistent and maintainable - don't
throw that effort away, forcing them to learn a new style.  If other
programmers have a problem with someone's style, then they should talk
about it.  A rank newbie could use the style guide to develop their
own style, but they could also absorb style points from program
listings, mentors, and colleagues.  You could ask the experienced
programmers to document their style, it could be an interesting
exercise.

You probably have a large amount of pre-style-guide code - will
resources be expended to bring that code into compliance with the
style guide?  I doubt it.  So you'll have a number of styles anyway. 
I can deal with any coding style - I'm a maintenance programmer, it's
part of the job description.  If I'm changing an existing program, I
try to conform with the style of that program.  I've seen multiple
styles within one program which I find jarring: a block of all upper
case code within a lower case program, a block of indent six within an
indent two program, etc..  To me, the tracks of a poor programmer.

Comments?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
