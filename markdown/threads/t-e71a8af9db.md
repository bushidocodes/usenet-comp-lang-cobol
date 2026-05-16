[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Embedded SQL, PL/SQL in Cobol

_12 messages · 4 participants · 2005-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Embedded SQL, PL/SQL in Cobol

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-28T10:11:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com>`

```
I am new to SQL and PL/SQL and my company is considering cutting out
some middleware software we have that talks to Oracle. Does anyone know
of any "real World" examples of embedded SQL or PL/SQL?
```

#### ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-04-28T10:27:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114709249.290132.75750@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com>`

```
Jeff,

Here is a very basic sample that will connect to an Oracle database.
You can always expand the EVALUATE statement to include other various
SQLCODEs so that you can incorporate your own error messages if
desired. Also, you'll need to run this with the Oracle run-time
(rtsora) or build a shared library that you make an initial call to in
order to load the Oracle functions.

Good luck.

Chris



       identification division.
       program-id. dbconnect.

       data division.

       working-storage section.

           exec sql include sqlca end-exec.

           exec sql declare dbname database end-exec.

           exec sql begin declare section end-exec.

       01  db-user                     pic  x(10).
       01  db-passwd                   pic  x(10).

           exec sql end declare section end-exec.

       procedure division.

           move "myLogin" to db-user
           move "myPassword" to db-password

           exec sql
             connect
               :db-user
             identified by
               :db-passwd
             at
               dbname
           end-exec

           evaluate  sqlcode
               when  0
                   display "You are connected!" end-display
               when  other
                   display "Error: "  sqlerrmc(1:sqlerrml - 1)
end-display
           end-evaluate

           goback returning 0
           .
```

##### ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-28T10:35:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114709720.966871.107470@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1114709249.290132.75750@o13g2000cwo.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <1114709249.290132.75750@o13g2000cwo.googlegroups.com>`

```
Chris,

How well do you know SQL? I was wondering if I could email you a
program that uses our middleware and see if you could just point to
where I need changes etc.
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-04-28T18:59:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eu82719at3hd4ooeuv0ifel3n0apbf8d0a@4ax.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <1114709249.290132.75750@o13g2000cwo.googlegroups.com> <1114709720.966871.107470@o13g2000cwo.googlegroups.com>`

```
On 28 Apr 2005 10:35:21 -0700, "Jeff" <jmoore207@hotmail.com> wrote:

>Chris,
>
>How well do you know SQL? I was wondering if I could email you a
>program that uses our middleware and see if you could just point to
>where I need changes etc.

Jeff,

If you start something on a newsgroup it is all so correct that you
keep it within the group unless you reach a point where it is better
to, while a solution is found, proceed to private email.
If dealing with a technical problem you should then return with the
solution.

You have not yet reached the mentioned point here as you have not
given anyone the opportunity of helping you.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

_(reply depth: 4)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-28T11:28:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114712929.503556.67210@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<eu82719at3hd4ooeuv0ifel3n0apbf8d0a@4ax.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <1114709249.290132.75750@o13g2000cwo.googlegroups.com> <1114709720.966871.107470@o13g2000cwo.googlegroups.com> <eu82719at3hd4ooeuv0ifel3n0apbf8d0a@4ax.com>`

```
Sorry about my newsgroup ettiquette. I will wait until the mentioned
point on a solution.
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

_(reply depth: 5)_

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-04-28T12:26:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114716412.728181.294590@z14g2000cwz.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <1114709249.290132.75750@o13g2000cwo.googlegroups.com> <1114709720.966871.107470@o13g2000cwo.googlegroups.com> <eu82719at3hd4ooeuv0ifel3n0apbf8d0a@4ax.com> <1114712929.503556.67210@z14g2000cwz.googlegroups.com>`

```
Jeff,

As Frederico points out - its best to keep this on the newsgroup for
now.

While I have extensive experience with Emdedded SQL in COBOL (as
pertaining to Oracle), by no means am I the end all autority on the
subject. By limiting your resources to just myself, you'd be losing out
on a multitude of other valuable opinions and insight here in the
group.

Perhaps if you would post a chunk of the code using the middleware, as
well as a short explanation of its context, you will get more than one
possible solution for your problem. If no one is able to help out via
your post, then by all means you may e-mail me your code and I'll have
a look. But, if form holds true as I suspect it will, you will get
numerous offerings to your post.

What is it that your doing with the middleware? Here is a simple SELECT
statement for you to look at:

EXEC SQL
  SELECT
    <column name>
  INTO
    :host-variable
  FROM
    <table name>
  WHERE
    <column name> = ( numeric value, quoted literal(') or
:host-variable )
END-EXEC

As I said, with a look at a piece of your code, and some understanding
of its context, I'm sure you'll get the assistance you need.

Chris
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-04-28T19:10:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oyace.1608$6z3.1506@newssvr33.news.prodigy.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <1114709249.290132.75750@o13g2000cwo.googlegroups.com> <1114709720.966871.107470@o13g2000cwo.googlegroups.com>`

```
"Jeff" <jmoore207@hotmail.com> wrote in message
news:1114709720.966871.107470@o13g2000cwo.googlegroups.com...
> Chris,
>
> How well do you know SQL? I was wondering if I could email you a
> program that uses our middleware and see if you could just point to
> where I need changes etc.

???

What happened to ...
"I  am new to SQL and PL/SQL and my company is considering cutting out some
middleware software we have that talks to Oracle.."

What do you want to do... cut out the middleware (replacing with ESQL), or
fine-tune your SQL? Those are two totally different things.

If you are talking about doing some maintenance on this software because of
performance... sure, everyone's SQL can probably use a little tuning (mine
sure could!)... but I have to believe that eliminating the "middleware"
MIGHT  solve any such problems, quickly.

If that "middleware" is a complete extra external program which starts and
ends each time you want to access the database, for sure that overhead is a
killer. If it's a linked library, then you should probably be looking at
tuning the SQL, since you probably will not be gaining a whole lot by
changing from one library (current) to another (the library linked when you
use embedded SQL) (unless it's a pretty crummy library).

Lastly (or maybe even firstly!), you should look at the overall database
access in your program. Sometimes seemingly 'little' things like PREPAREing
statements and executing with parameters instead of doing an EXECUTE DIRECT,
or using a cursor instead of  doing multiple SELECTs can make a world of
difference.
```

#### ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-04-28T22:33:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5hl271tq9llhku6b8pegv75ooeehevbg2m@4ax.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com>`

```
On 28 Apr 2005 10:11:12 -0700, "Jeff" <jmoore207@hotmail.com> wrote:

>I am new to SQL and PL/SQL and my company is considering cutting out
>some middleware software we have that talks to Oracle. Does anyone know
>of any "real World" examples of embedded SQL or PL/SQL?


As others have mentioned, and also myself on another forum, you really
have to give us some code examples of what you are trying to achieve
with the change.

I work with Oracle and COBOL(obviously), and I have created interfaces
between COBOL and Oracle (and DB2 and Sybase and Informix), and I
along with others on this group will be able to give you some
pointers/ideas AFTER we see your examples. Not before.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-29T04:09:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114772945.578105.250250@g14g2000cwa.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <5hl271tq9llhku6b8pegv75ooeehevbg2m@4ax.com>`

```
The middleware is Open turbo. I will paste the calls to the database.
The program is not very big, I am starting with a small report program
that does a few seperate gets(call).
The middleware uses modes to go "get records"


005900 77  BASE        PIC X(24)    VALUE "  CONSDB.DATABASE;".
006000 77  PASS        PIC X(8)     VALUE "INQUIRY;".
006100 01  PROCID      PIC X(8)     VALUE "ALASTSUV".

020200     CALL "DBOPEN" USING BASE, PASS, MODE5, DB-STATUS.
020300     IF C-W NOT = 0
020400         PERFORM DB-ERROR.

022100     MOVE ZERO TO TAPE-REC.
022200     CALL "DBGET" USING BASE, DMBRDETL, MODE2, DB-STATUS,
022300         DALLITEM, MEMBERDETL, DB-ARG-SEP.
* Base is path to database, MEMBERDETL is the memberdetl table, mode2
reads next record serially, DB-ARG-SEP is variable passed.
022400     IF C-W = 11
022500         GO TO RRS-9999-EXIT.
C-W i- 11 is end of file
022600     IF C-W NOT = 0
022700         PERFORM DB-ERROR.
C-W = 0 means found record
022800     MOVE MBRSEP OF MEMBERDETL TO DB-ARG-SEP.
022900
023000 RRS-0200.
023100     CALL "DBGET" USING BASE, DMSMSTR, MODE7, DB-STATUS,
023200         DALLITEM, MBRSEPMSTR, DB-ARG-SEP.
Mode7 reads master record given a search value
023300     IF C-W NOT = 0
023400         PERFORM DB-ERROR.
023500     IF ACCTSTATUS OF MBRSEPMSTR(1) NOT = "A"
023600         GO TO RRS-0100.
023700     PERFORM MOVE-FIELDS THRU MOVE-FIELDS-EXIT.
023800
023900     MOVE RATE OF MEMBERDETL TO WSCR-RATE-CODE OF TAPE-REC.
024000     MOVE CLASX OF MEMBERDETL TO WSCR-SRVC-CODE OF TAPE-REC.
024100
024200     MOVE 0 TO CHECK-FLAG, I, HISTORY-COUNT.
024210     MOVE CLASX OF MEMBERDETL TO WW-CLASS.
024300     PERFORM CHECK-CLASS THRU CHECK-CLASS-EXIT.
024400     IF CHECK-FLAG = 1
024500         GO TO RRS-0100.
024700     MOVE MBRSEP OF MEMBERDETL TO DB-ARG-SEP.
024800     CALL "DBFIND" USING BASE, DMBRHIST, MODE1, DB-STATUS,
024900         SRCH-SEP, DB-ARG-SEP.
Find= sets up chain read
025000     IF C-W = 17
025100         GO TO RRS-0100.
C-W = 17 is no master entry
025200     IF C-W NOT = 0
025300         PERFORM DB-ERROR.
025400     MOVE 0 TO I.
025500 GET-NEXT-HISTORY.
025600     IF I > 11 GO TO RRS-0500.
025700     CALL "DBGET" USING BASE, DMBRHIST, MODE6, DB-STATUS,
025800         DALLITEM, MBRHISTDETL, DB-ARG-SEP.
Mbrhistdetl table,  Mode6  reads previous record in chain
025900     IF C-W = 14
026000         GO TO RRS-0500.
C-w = 14 beginning of file
026100     IF C-W NOT = 0
026200         PERFORM DB-ERROR.
026300     IF BILLTYPE OF MBRHISTDETL = 9
026400         GO TO GET-NEXT-HISTORY.
026410     CALL "DATE2Y2K" USING READDATE OF MBRHISTDETL, Y2K-DATE1.
99025037
026420     CALL "DATE2Y2K" USING TDUEDATE, Y2K-DATE2.
99025037
026500*Y2K IF READDATE OF MBRHISTDETL > TDUEDATE
99025037
026510     IF Y2K-DATE1               > Y2K-DATE2
99025037
026600         GO TO GET-NEXT-HISTORY.
026610     CALL "DATE2Y2K" USING READDATE OF MBRHISTDETL, Y2K-DATE1.
99025037
026620     CALL "DATE2Y2K" USING FDUEDATE, Y2K-DATE2.
99025037
026700*Y2K IF READDATE OF MBRHISTDETL < FDUEDATE
99025037
026710     IF Y2K-DATE1               < Y2K-DATE2
99025037
026800         GO TO RRS-0500.
026900     IF READDATE OF MBRHISTDETL NOT = HOLD-READDATE
027000        ADD 1 TO I
027100        MOVE READDATE OF MBRHISTDETL TO HOLD-READDATE
027200                      WSCR-DATE(I)
027300        MOVE KWH OF MBRHISTDETL TO WSCR-KWH(I)
027400        MOVE ENERGY OF MBRHISTDETL TO WSCR-REVENUE(I)
027500        ADD FUEL OF MBRHISTDETL TO WSCR-REVENUE(I)
027600     ELSE
027700        ADD KWH OF MBRHISTDETL TO WSCR-KWH(I)
027800        ADD ENERGY OF MBRHISTDETL TO WSCR-REVENUE(I)
027900        ADD FUEL OF MBRHISTDETL TO WSCR-REVENUE(I).
028000     GO TO GET-NEXT-HISTORY.
028100

I am trying to figure out where to start, do I use embedded SQL or
PL/SQL. I have very little knowledge, only what I have been reading in
the Oracle manuals. If I had an idea of where to start and what the
code looks like, I would feel much better about it. I appreciate
everyone's help and sorry of I came across as a smarta$$. I am very
anxious to get one program under my belt. Thank you again and I look
forward to your responses.
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-29T05:04:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114776246.808287.16990@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1114772945.578105.250250@g14g2000cwa.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <5hl271tq9llhku6b8pegv75ooeehevbg2m@4ax.com> <1114772945.578105.250250@g14g2000cwa.googlegroups.com>`

```
Also, not sure if I should use host tables to hold info?
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-04-29T07:57:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114786659.901760.181470@f14g2000cwb.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <5hl271tq9llhku6b8pegv75ooeehevbg2m@4ax.com> <1114772945.578105.250250@g14g2000cwa.googlegroups.com>`

```
Jeff,

Looking at this quickly, I'd say it's a prime candidate for Embedded
SQL.

The call to "DBOPEN" would be replaced by a SQL connect statement.

The call to "DBREAD" would be replaced by a SQL select statement.

The call to "DBFIND" would be replaced by a SQL cursor declaration and
open statement.

The call to "DBNEXT" would be replaced by a SQL fetch statement (from
your previously established cursor).


The only area you will run into a snag is your call to DBGET with
mode6. There is no "read previous" function in Oracle (not 100% sure
about other databases). What I would do in this circumstance is simply
sort the cursor in the proper decending sequence (time, transactions
nbr, etc) so the history comes out in sequence when simply using "read
next" (FETCH) logic.

I hope this helps point you in the right direction.

Chris
```

###### ↳ ↳ ↳ Re: Embedded SQL, PL/SQL in Cobol

_(reply depth: 4)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-29T08:04:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114787064.095129.248970@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1114786659.901760.181470@f14g2000cwb.googlegroups.com>`
- **References:** `<1114708272.300758.160650@l41g2000cwc.googlegroups.com> <5hl271tq9llhku6b8pegv75ooeehevbg2m@4ax.com> <1114772945.578105.250250@g14g2000cwa.googlegroups.com> <1114786659.901760.181470@f14g2000cwb.googlegroups.com>`

```
Thank you Chris!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
