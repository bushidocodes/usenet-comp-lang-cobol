[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RDB limitations: from Jimmy Gavan

_2 messages · 2 participants · 2008-10_

---

### RDB limitations: from Jimmy Gavan

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-10-13T12:25:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_wLIk.2023$sI6.1334@newsfe09.iad>`

```
Jimmy is having infinite amounts of trouble with his pc and has asked me to
post this for him.

PL
____________________________________________________
Your DBI QUESTION :

Bearing in mind no compiler to reference or even test my thoughts, some
of what I originally wrote was guesswork. Having now read your solution,
I see you have answered some of my queries.

The message I prepared, and I'll make an effort to post it if you are
interested :-

<Edit Customers> <....> <<Customer DBI..........>  <Customer Table>
DBI = Database <...........
Interface>

Not mentioned in Will's book, (I think he was perhaps on a deadline for
publishing), he did provide me with a white paper on COBOL file
handling. I adapted his thoughts as above and when switching to MS
Access  followed a parallel route. Any technique developed is a
compliment and an enhancement of a previous idea.

Three classes above - 'Edit' needs a Listbox of customers to select from
for editing/deleting and the dialog also allows you to 'Add'. Edit
invokes Customer DBI, (an intermediary) which in turn invokes the Table
containing a 'Cursor' method.  The DBI sends its own object reference
and a specific method name to the Table through Linkage.

Note that the DBI contains two distinct methods :-

(a) Tell the Table to 'fetch' and when finished this method in the DBI
finishes by checking the returned status for zero (covers 'Good' and 'No
more Rows'), otherwise the result is a TableError.

(b) method 'returned info' from the Table, i.e. each row

In the Table Class - A typical cursor routine and as each row is
retrieved, as appropriate it is returned to the DBI (using the
Link-ObjectReference and the Lnk-MethodName) - this is (b) above. This
cycle in the SQL statement continues until no more rows or an error
result - then goes back to (a) above.

Now in my case all I'm doing in the DBI (b) method is formatting entries
to go into a collection for the Dialog Listbox. In your situation my
method (b) could be extended to do conditional checks and the method
could quite easily invoke many methods from other classes and
create/write rows even in other tables. There is only a return to the
Cursor method in the Table AFTER I reach End Method (b); back in the
Table the cursor is still positioned for the next fetch.

You hit on the idea of two instances - given that you proved you can
have two cursors against the same table. I think my approach might let
you get away with one instance. Bearing in mind the DBI (intermediary)
is making the decisions and the Table Class is limited basically to gets
and puts.

The above is the design in a nutshell.

Robert's comments above SQL performance. I'll take it as read; again
back to a certain amount of specialization in products. My volumes are
extremely small and you are only going to realize poor performance when
you have huge databases - COBOL files or DBs.

---------------------------------------------------------

Your comments in the Fujitsu SQL thread, that's what I do - connecting.

I have two sets of Tables, call them Group 1 and Group 2. Group 1 is a
set of tables applicable to all clients (oil/gas companies). Group 2 is
specific to data for a particular production facility. For each
location there is a separate set for Group 2 - NDT we are talking about
again - the Inspection company may get the contract for Petro Canada,
Jumping Pound Creek this year, new inspectors for next five years, and
the original contractor might get lucky again in the sixth year. So no
point in Petro Canada data being in an omnibus DB which may be used
again or may never be used again.

Then you mentioned somewhere your beloved 'FACTORY' for storing
constants. Still can't buy that without seeing code. Not suggesting it
doesn't work, but why that approach ?

The Group 1 and Group 2 tables above. In the Object/Instance code is a
fixed constant:-

pic 9(01) value 1 for Group 1 Classes and pic 9(01) value 2 for Group 2
Classes.

Never changes and is applicable to all instances of a class. Each method
in a class referencing SQL starts with an invoke to check Class
'Connector' to see which is currently active, Group 1 or Group 2, using
the Table's constant. If it's Group 1 and the 'Connector' shows 2 as
being active then I change it to 1 and connect to Group 1.

----------------------------------------------------------------------------
---

Will's books :- He's actually written around some 40 books; some I know
dealt with Pascal. His COBOL books :-

1. Elements of OO COBOL - first and second editions. It's the second
edition that you have hidden away somewhere.

2. Elements of COBOL Web Programming - Very N/E specific and two major
topics were (1) Webbing and (2) SQL and how to use the M/F ESQL Assistant.

3. N/E with dotNet and as xxx pointed out N/E V5 comes as N/E plain and
N/E dotNet.

If just for nostalgia you want a copy of the 2nd Edition of #1, I can
snail-mail it to you if you give me your postal address. Will sent me
two copies. Got a deal on pricing from some printer up here in Edmonton
and they provided print number 1. Bloody awful with smudged pages, but
readable. As he put it in the attached yellow sticker, "Jimmy, Stand
back from this book it  will self-destruct in 30 days. Will". Then he
sent me the copy, printed in the States, which is what you had.

Haven't been in contact with him for years. He last told me he was
moving from California to Utah taking up snowboarding. (Bear in mind he
is a bare six months older than me). I made some comment like "Watch it,
you could do yourself some damage. And what about your kids ?". He
replied along the lines, "My kids. If they want to keep up with me, they
had better get moving !" :-)

--------------------------------------------------------------------------

*** I stopped at this point as Eileen had just come back from her
Anglican church for Thanksgiving - just now got back to this draft and
out of curiosity got into e-mail and I can read ALL the bloody messages
! See what I mean about the machine being 'iffy' ?

-------------------------------------------------------------------------

I read Jerry's 'Oremus' = 'Let us Pray" in Latin. Didn't read right, so
I googled on both 'Oremus' which is correct and 'Oreamus' which I
thought - latter is incorrect. But Google gives you umpteen references
to 'Americanus Oreamus', mountain goat, with constant references to them
being in the federal Jasper National Park. Quite some years since I've
been up there; must check 'em out next time I go. S'amzin what trivia
you pick up googling :-)

Jimmy, Calgary AB
```

#### ↳ Re: RDB limitations: from Jimmy Gavan

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-14T12:40:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6li4inFcetqbU1@mid.individual.net>`
- **References:** `<_wLIk.2023$sI6.1334@newsfe09.iad>`

```


"tlmfru" <lacey@mts.net> wrote in message 
news:_wLIk.2023$sI6.1334@newsfe09.iad...
> Jimmy is having infinite amounts of trouble with his pc and has asked me 
> to
…[8 more quoted lines elided]…
> I see you have answered some of my queries.

Not sure if the "you" referenced here is "me" (my question was about DB 
cursors and maintenance, not about Database interfacing), but, in case it 
is, I have some quick responses below... Pete.

>
> The message I prepared, and I'll make an effort to post it if you are
…[10 more quoted lines elided]…
> compliment and an enhancement of a previous idea.

You keep mentioning Wil's book (his name is Wilson, not William...) but I'm 
not sure WHICH of his books you are referring to.
>
> Three classes above - 'Edit' needs a Listbox of customers to select from
…[3 more quoted lines elided]…
> and a specific method name to the Table through Linkage.

Why would you not simply bind the table to the DB as a datasource?

>
> Note that the DBI contains two distinct methods :-
…[5 more quoted lines elided]…
> (b) method 'returned info' from the Table, i.e. each row

OK.

>
> In the Table Class - A typical cursor routine and as each row is
…[3 more quoted lines elided]…
> result - then goes back to (a) above.

But there is no updating of the the cursor... My post was about that.

>
> Now in my case all I'm doing in the DBI (b) method is formatting entries
…[5 more quoted lines elided]…
> Table the cursor is still positioned for the next fetch.

Yes, that works as expected.
>
> You hit on the idea of two instances - given that you proved you can
> have two cursors against the same table.

I never mentioned two cursors and I think you may have misunderstood the 
solution.


>I think my approach might let
> you get away with one instance.

Jimmy, I don't WANT to "get way with" anything. Two instances provides far 
better performance than one instance, where updating is required, and allows 
multithreading in the RDB itself.

The tool software will decide whether to generate one or two threads, based 
on the access pattern encountered in the application program. I am currently 
looking at a pre-generation pass to assess how much PUT access is in the 
application code and whether it is likely to conflict with the GET 
application code. The result of this will decide whether two instances are 
generated into the application or just a single one. For example, if the 
application is doing mainly skip-sequential processing and the odd random 
fetch of associated rows, there is no need for two threads.


> Bearing in mind the DBI (intermediary)
> is making the decisions and the Table Class is limited basically to gets
…[24 more quoted lines elided]…
> constants.

I have no particular affection for FACTORY any more than any other section 
of software and I don't use it for "storing constants". Do you make this 
stuff up :-)?

The FACTORY is REQUIRED so that a unique identifer can be stamped on each 
instance generated by it. The unique Id is used as a DB connection 
identifier so that each instance of the MOST handler can have its own unique 
DB connection. Each instance SETs the CONNECTION to its own connection when 
it does DB activity and so the threads are separated.

That's what FACTORY is for... at least, that is one of the things it is for.

>Still can't buy that without seeing code. Not suggesting it
> doesn't work, but why that approach ?

Because you can't get a unique instance identifier easily any other way. I 
COULD use the object reference itself and reference SELF, but then I would 
need a dummy property or method for SELF to reference. Besides, it is an 
acknowledged function of FACTORY to do this.

Perhaps a code snippet will help...

 working-storage section.
* Factory data items go here...
 01  instance-stamp.
     12 filler pic x(8) value "ARPMF0MT".   *> %stem%MT
     12 is-count pic 9999 value zero.
/
 PROCEDURE DIVISION.
* Factory Methods go here...
*
 IDENTIFICATION DIVISION.
 METHOD-ID. GETInstanceStamp.
 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 DATA DIVISION.
 FILE SECTION.
 WORKING-STORAGE SECTION.
 Linkage section.
 01 MOST-instance-stamp pic x(15).   *> DB connection name length is max 15 
chars
 PROCEDURE DIVISION returning MOST-instance-stamp.
 P1.
     add 1 to is-count
     move instance-stamp to MOST-instance-stamp

     .
 END METHOD GETInstanceStamp.
 END FACTORY.
*
* Object definition starts here...


Then...

* -----------------------------------------------------------------
* Object Methods go here...
 PROCEDURE DIVISION.  *> for object methods...
*=================================================================
* START OF METHOD - ARPMF0MTinit
*
* This initialises and returns the interface block.
*
 IDENTIFICATION DIVISION.
 METHOD-ID. ARPMF0MTinit AS "ARPMF0MTinit".
 ENVIRONMENT     DIVISION.
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01  DBaction pic x(8).
 LINKAGE SECTION.
 01  datablock pic x(8192).
 PROCEDURE       DIVISION using datablock.
 main section.
 main-start.

     initialize MOST-Interface-Block
     move zero to MOST-SQLSTATE
     move
     "%stem%MT MOST COM server interface initialized OK..."
     to MOST-SQLMsg
     invoke ARPMF0MT "GETInstanceStamp"     <==  Sets the instance stamp one 
time.
            returning MOST-instance-stamp              <==  after that, this 
instance can be
     end-invoke                                                     <== 
uniquely identified, every time
                                                                           <== 
it is used.
     set MOST-cursor-NOT-active to TRUE
     set MOST-init to TRUE
     set MOST-logging-inactive to TRUE
     move 'init' to DBaction
     invoke SELF "HandleDB"
            using DBaction
     end-invoke
     invoke SELF "TranslateFileStatus"
     end-invoke

     move MOST-interface-block to datablock
     .
 main-end.
     exit method
     .
 END METHOD ARPMF0MTinit.
*=============================================================

... and finally....

*=============================================================
*
* START OF METHOD - HandleDB
*
*  This method handles all the SQL actions that are required by
*  MOST. Because of Method encapsulation I could find no way
*  to share an SQL cursor across methods, so finally opted
*  to put everything here.
*
*  This method must be passed an action, which it then carries
*  out.
*
*  If the action is successful the passed action is blanked,
*  otherwise SQLSTATE and SQLMSG are set with information
*  about the problem.
*
 IDENTIFICATION DIVISION.
 METHOD-ID. HandleDB AS "HandleDB".
 ENVIRONMENT     DIVISION.
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01  saved-SQLSTATE   pic x(5).
 01  saved-SQLMSG     pic x(512).
 LINKAGE SECTION.
 01  DBaction    pic x(8).
 PROCEDURE DIVISION using DBAction.
 MAIN SECTION.
 P001.
     if DBaction NOT = 'init'
        move MOST-instance-stamp to HV-DB
        EXEC SQL
           SET CONNECTION :HV-DB   *> ensure we are using the right 
connection...
        END-EXEC
        move SQLSTATE to MOST-SQLSTATE
        MOVE SQLMSG   to MOST-SQLMSG
        if SQLSTATE NOT = '00000'
           go to p001-end
        end-if
     end-if

     evaluate DBaction
        when 'init    '
           perform SQLInit
        when 'start   '
           perform SQLStart
        when 'getnext '
           perform SQLGetNext
        when 'close   '
           perform SQLClose
        when 'finish  '
           perform SQLFinish
        when 'random  '
           perform SQLRandom
        when 'write   '
           perform SQLWrite
        when 'update  '
           perform SQLUpdate
        when 'delete  '
           perform SQLDelete
        when other
           move '99999' to SQLSTATE
           move 'Invalid action passed to HandleDB...' to SQLMsg
     end-evaluate
     if SQLSTATE = '00000'
        move space to DBaction
     end-if
     .
 p001-end.
     exit method.
*---------------------------------------------------
 SQLInit section.
 si001.
*
* Get a DB connection...
*
* CONNECT TO DATABASE ON %DBDSN% SERVER
     move MOST-instance-stamp to HV-DB  *> uniquely identify connection for 
this stream
     EXEC SQL
*  DSN, User and password must be set in the ODBC info file
*  which is external to the MOST handler.
       CONNECT TO 'TestDB' AS :HV-DB
     END-EXEC
* CHECK CONNECTION RESULT
     IF SQLSTATE = "00000"
      move "Connection to %DBDSN% server through ODBC OK..."
      to SQLMsg
         Log-Message
     else
        move SQLMsg to Log-message
     END-IF
     move SQLSTATE to MOST-SQLSTATE
     MOVE SQLMSG   to MOST-SQLMSG
     invoke SELF "LogIt"
     end-invoke
     .
 si999.
     exit.
*---------------------------------------------------
 SQLStart section.
 ss001.

...and so on...

You can see the factory instance stamp provides a unique DB connection 
identifier. The GET stream uses one connection, the PUT stream uses another, 
and there is no possibility of conflict. The downside (as for all COBOL 
ESQL) is that these connections are held for the life of the object. That is 
why DB set processing is so superior; a connection is held long enough to 
return a result set, then immediately released back to the connection pool. 
It's life is milliseconds. Later, when the result set needs to be 
replaced/updated/whatever, connection is re-established and the action 
completes, again , usually in a few milliseconds.   Classes in .NET automate 
most of this and the reconnection and update activity can be automatic. 
COBOL is really primitive by comparison. Nevertheless, it does get the job 
done, and it is very stable :-)

>
> The Group 1 and Group 2 tables above. In the Object/Instance code is a
…[9 more quoted lines elided]…
> being active then I change it to 1 and connect to Group 1.

You swap to a different table?

A DB connection swap would be many times faster...

>
> ----------------------------------------------------------------------------
…[6 more quoted lines elided]…
> edition that you have hidden away somewhere.

It isn't hidden away; it stands proudly on my bookshelf. Although I haven't 
referenced it for many years.

>
> 2. Elements of COBOL Web Programming - Very N/E specific and two major
…[6 more quoted lines elided]…
> snail-mail it to you if you give me your postal address.

I appreciate the offer, but, as you noted yourself above, I already have a 
copy of the second edition which Wil mailed to me at the time it was 
published.

>Will sent me
> two copies. Got a deal on pricing from some printer up here in Edmonton
…[17 more quoted lines elided]…
> ! See what I mean about the machine being 'iffy' ?

I see what you mean about the user being 'iffy'... :-)

Seriously, If you are getting mail from a number of sources, or web mail, it 
can take a while. I have it all centralised to Outlook so Outlook goes and 
checks various ISPs and mail servers and presents it all in one place. The 
point is that it can take time. For example, if you create mail, send it, 
then close down your system, mail may still be in your out box. Next time 
you login, this has to be sent so it may be a while before mail appears in 
your in box. It's easy to believe you are being prevented from seeing it or 
it isn't working.

The fact that you hadn't been in email for a while may have given background 
processes time to complete.

Check for disk activity if you have an LED that shows it. If it is on 
solidly, your system may appear to have hung, when, in fact, it is simply 
working.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
