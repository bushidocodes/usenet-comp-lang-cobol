[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/DB2 Date edit question

_98 messages · 16 participants · 2007-08_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Date and calendar processing`](../topics.md#dates)

---

### COBOL/DB2 Date edit question

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-08-11T13:51:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com>`

```
Help please.
The following code fails - think I've missed something simple.
Table and column exist, database is connected.
I thought I could get a field off screen and edit it via the
SQL below but I get a compile error. I get the same error for
Time and Timestamp fields.
Might there be an 'industry standard' for dealing with these
types of fields?
My docs give little guidance on this and since I work in 
isolation there's no-one to ask.
Environment is Visualage Cobol 2.2, DB2 V7.2

           02   MP1ZADATEI                       PIC X(00010).

      *------------------------------
       E1-ADATE.
      *------------------------------
           IF MP1ZADATEL NOT = ZERO
              EXEC SQL DATE(MP1ZADATEI) END-EXEC
              IF SQLCODE = -180
                 ..ETC

--------------------------------------------------------------------
        SQL0060W  The "COBOL" precompiler is in progress.
   83   SQL0062W  Starting INCLUDE of file
                  "E:\conrad\edi1\THEBOOK.cbl".
   83   SQL0063W  Completed INCLUDE of file "THEBOOK.cbl".
 1057   SQL0104N  An unexpected token "DATE" was found following
                  "BEGIN-OF-STATEMENT".  Expected tokens may include:
                  "SELECT".  SQLSTATE=42601

Any help or code examples appreciated. please, thanks.
```

#### ↳ Re: COBOL/DB2 Date edit question

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-08-11T20:14:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4Novi.49125$YL5.33744@newssvr29.news.prodigy.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com>`

```
> SQL below but I get a compile error
>           02   MP1ZADATEI                       PIC X(00010).
…[18 more quoted lines elided]…
> Any help or code examples appreciated. please, thanks.

"DATE (anything)"   is not a valid SQL statement. (what's between "EXEC SQL" 
and "END-EXEC")

I can't tell what would make sense here What are you trying to get, some 
kind of date from the character string 'MP1ZADATEI' ?

MCM










>
```

#### ↳ Re: COBOL/DB2 Date edit question

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2007-08-11T13:28:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1186864103.244289.269570@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com>`

```
On Aug 11, 6:51 pm, Graham Hobbs <gho...@cdpwise.net> wrote:
> Help please.
> The following code fails - think I've missed something simple.
…[32 more quoted lines elided]…
> Posted via a free Usenet account fromhttp://www.teranews.com

I think you should invoke an SQL function along the following lines
according to the V9 DB2 for z/OS programmer's guide

EXEC SQL
 SELECT RAND(:hvrand) INTO :hvrandval FROM SYSIBM.SYSDUMMY1
END-EXEC

Note also that it is at least recommended that host variables be
enclosed within a DECLARE BEGIN .. END block and be prefixed by a
colon when they are referenced by SQL statements.

I haven't looked up the meaning of SQLCODE -180, but you may find that
SQLSTATE provides aore detailed explanation of any errors found, again
I haven't actually looked at the relevant manual for that either.
```

#### ↳ Re: COBOL/DB2 Date edit question

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-12T13:37:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5i76i7F3mgdc6U1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com>`

```


"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
news:pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com...
> Help please.
> The following code fails - think I've missed something simple.
…[30 more quoted lines elided]…
>

Your problem here is that you are not referencing a host variable to the SQL 
DATE  function.

As long as your RDBMS supports the function, it is OK to use it in COBOL, 
but you need to be clear about what is a field on your database and what is 
a field in your program.(Michael was not quite right about that.)

This is addressed by using Host Variables. Host variables must be declared 
with an SQL DECLARE statement, and prefixed with a symbol whenever they are 
referenced in EXEC SQL statements. (Often the symbol is a colon, but it 
varies on different systems.)

It would also be very helpful if, when posting here, you told us what COBOL 
and what RDBMS you are using. Believe it or not, but  despite 
standardization of both COBOL and SQL, there are actually differences 
between different systems! (Shock! Horror!)

Consult your documentation regarding the use of Host Variables and all will 
be revealed.

Robert Jones has posted a code example.

HTH,

Pete.
```

##### ↳ ↳ Re: COBOL/DB2 Date edit question

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-08-12T01:45:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net>`

```
Gentlemen,
Thanks - will work on what you've said.
MP!ZADATEI is a field on a CICS screen, populated from a column in a
row from a DB2 table. The user changes it and now it needs editing. I
thought my EXEC SQL was a winner - clearly not. 
Peter - I did say it was VisualAge COBOL 2.2, DB2 V7.2 - didnt mention
the word 'IBM':-). Sorry. 
graham

On Sun, 12 Aug 2007 13:37:06 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[60 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-13T00:59:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5i8ehiF3lkrtaU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com>`

```


"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
news:506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com...
> Gentlemen,
> Thanks - will work on what you've said.
…[4 more quoted lines elided]…
> the word 'IBM':-). Sorry.

No, I'm sorry, I missed that :-) (Too busy examining your code... :-))

You might not be able to support the ! in the name in Visual Age COBOL 
(which is actually MicroSoft rebadged)

Your EXEC SQL may yet be a winner, just give it a host variable... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-08-12T14:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5i8ehiF3lkrtaU1@mid.individual.net...
> "Graham Hobbs" <ghobbs@cdpwise.net> wrote in message
>>MP!ZADATEI is a field on a CICS screen, populated from a column in a
>>row from a DB2 table. The user changes it and now it needs editing


> Your EXEC SQL may yet be a winner, just give it a host variable... :-)
.
Isn't using EXEC SQL .... END-EXEC kind of an obtuse way to validate a date 
entered upon the screen?

Not that it can't be made to work, but generally you'd have some kind of 
library routine around to handle that.

Besides, at some point it's possible (probable?) you are going to have to 
reformat it anyway to do the UPDATE


MCM
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 5)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2007-08-12T17:47:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jgvub35e1pahgvi467v85db20119s42cub@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net>`

```
I hear what you say Michael. Might I scenario something (and if you
get bored with the subject I will understand) ..

My 'almost all common data types DB2 table' has 14 columns, one is a
key and in particular, three of the others are DB2 datatypes DATE,
TIME, TIMESTAMP. I populate the CICS screen from this table, any field
may be user changed, I need to edit all changes before they go back
into the table - typical CICS scenario.

My problem is to find the easiest/clearest way to edit these three
data types before update occurs. I suspect three ways are available:

1) my 'neat?' EXEC SQL.'s.
2) inline code like 'if month < 00 or >12 then error, etc'.
3) exec cics link 'editdate' with suitable commarea (and othe pgms for
TIME and TIMESTAMP) and test a return code. (your library routine)
4) some other way??
5) there is no especially favoured method.

But being out of the workforce for a few years now, on my laptop with
older IBM Cobol, CICS, DB2 and  btrieve VSAM software, developing a
software package (I am one of these BT/I's), am looking for help as to
how modern installations might handle DATE, TIME, TIMESTAMP edits.
You've already given me clues. Other insights?
Anyway, thanks to date.
graham 

On Sun, 12 Aug 2007 14:17:41 GMT, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
>news:5i8ehiF3lkrtaU1@mid.individual.net...
…[22 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-12T16:59:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com>`
- **In-Reply-To:** `<jgvub35e1pahgvi467v85db20119s42cub@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com>`

```
Graham Hobbs wrote:
> 
> My problem is to find the easiest/clearest way to edit these three
…[5 more quoted lines elided]…
> TIME and TIMESTAMP) and test a return code. (your library routine)

I can vouch for option 2 being very, very efficient.  We had a copybook 
that did date manipulation and validation.  It was 3,000+ lines, and I 
was just sure that it could be made much, much more efficient.

Well, when we had some analysis done on our source code, the results 
came out with the paragraphs sorted from longest run time to shortest 
run time.  For every program, the date/time routine's paragraphs filled 
the bottom of each list!

I had been working on a "convert" paragraph to convert time zones, using 
the database.  After we got those results, I abandoned that.  :)  The 
one tweak I did make to it after that was to "cache" the time zone 
information (we tracked when offsets were changed, so we could convert 
times as they were configured at a given point in time).  Caching those 
in working-storage allowed us to convert a lot of dates without plowing 
through the time change records every time.  It really helped on one 
batch program in particular.

Just my $.02.  (Also, I don't think "DATE()" by itself is a valid 
statement - though I've never used DB2.  We used "SELECT 
[date-expression] INTO :host-variable FROM [table-with-one-row]".)
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-13T12:22:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5i9mipF3nvs03U1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com>`

```

```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 8)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-12T20:59:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com>`
- **In-Reply-To:** `<5i9mipF3nvs03U1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net>`

```
Pete Dashwood wrote:

(When you have your "--" and the sig block at the top of the message, my 
reader truncates everything - that's why there's nothing quoted here...)

There are benefits to stored procedures - but the RDBMS runtime would 
still have been charged to our program, as the thread that started the 
whole mess would have been part of the program's charged time.  :) 
There's another school of thought that stored procedures tie one to a 
particular database, and that a program-based solution is preferable to 
obtain DB independence.  Of course, we've had enough debate in here as 
of late...  ;)

Personally, I believe that call has to be made for each system, by 
analyzing what it's going to do.  On our Unisys mainframe-based COBOL 
system, putting stored procedures in their proprietary RDMS format would 
probably make sense.  If it gets ported to another architecture, they're 
likely going to have different ways of validating dates.  On the other 
hand, on my websites I'm working on now with PHP 5, I'm using PHP Data 
Objects (PDO), which should allow me to extract the data access from the 
underlying database.  (Not that I plan on running it on anything but 
MySQL; but, I'll have the option.)

<ot>
Then, in my next set of college classes is .NET.  I'll be having fun 
with Mono, I'm sure - I may just finally get the knack of that.  (Part 
of it is I'm not getting paid for either - it's hard to justify sitting 
on the couch with a laptop in my lap when the kids want folks to bounce 
them on the trampoline, maintain their bikes, etc...  ;>  )

And then, I've been "selected" to "voluntarily" retrain into a different 
career field (not programming).  They want 20, and I'm #45 on the list, 
so I should be safe.  (If 20 don't volunteer, then everyone on the list 
has to pick what they want, and risk being involuntarily retrained.) 
So, I have to decide whether to a) not play this game and get out when 
this enlistment's up (with 13+ years at that point, that seems foolish); 
b) risk being involuntarily retrained to some combat career field; or c) 
choose my own path (there are current openings in safety, radio/TV, and 
as a chaplain's assistant).

Even if I switch career fields, though, I'll still pursue my bachelor's 
degree in Computer Science - especially when I can breeze through so 
many classes.
</ot>
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-13T22:39:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iaqn2F3oqi9dU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com>`

```


"LX-i" <lxi0007@netscape.net> wrote in message 
news:oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com...
> Pete Dashwood wrote:
>
> (When you have your "--" and the sig block at the top of the message, my 
> reader truncates everything - that's why there's nothing quoted here...)

Sorry, it was an oversight)
>
> There are benefits to stored procedures - but the RDBMS runtime would 
> still have been charged to our program, as the thread that started the 
> whole mess would have been part of the program's charged time.  :)


(Which is right and proper, of course... )

> There's another school of thought that stored procedures tie one to a 
> particular database, and that a program-based solution is preferable to 
> obtain DB independence.  Of course, we've had enough debate in here as of 
> late...  ;)

Uh, huh, and what about the program independence? :-)

I have transferred stored procedure code from MySQL (my personally preferred 
DB, although now that DB2 is "free"I may return to that and bring the wheel 
full circle) and ACCESS and SQL Server, the ones required by the client, 
without problem. (ACCESS is a bit limited in that procedures can only have 
ONE SQL statement, but that's no less than you might expect from ACCESS... 
:-)

>
> Personally, I believe that call has to be made for each system, by 
…[14 more quoted lines elided]…
> the trampoline, maintain their bikes, etc...  ;>  )

Play with the kids. They grow quickly. ;-)
>
> And then, I've been "selected" to "voluntarily" retrain into a different 
…[13 more quoted lines elided]…
>

I have absolutely no doubt that you will succeed at whatever is asked of 
you, Daniel.  You are very capable, and your attitude has never been in 
doubt.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-14T19:51:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PcWdnSETTNiDwV_bnZ2dnUVZ_vKunZ2d@comcast.com>`
- **In-Reply-To:** `<5iaqn2F3oqi9dU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <5iaqn2F3oqi9dU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com...
…[6 more quoted lines elided]…
> Uh, huh, and what about the program independence? :-)

Depends on which one you want.  Can't have both, sadly...

> I have transferred stored procedure code from MySQL (my personally preferred 
> DB, although now that DB2 is "free"I may return to that and bring the wheel 
…[3 more quoted lines elided]…
> :-)

I didn't even know Access supported stored procedures.  I haven't messed 
with MySQL stored procedures either.  That's interesting to know, though.
```

###### ↳ ↳ ↳ field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 9)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-13T11:26:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C03FC9.6F0F.0085.0@efirstbank.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com>`

```
>>> On 8/12/2007 at 8:59 PM, in message
<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com>, LX-i<lxi0007@netscape.net>
wrote:
> 
> There are benefits to stored procedures - but the RDBMS runtime would 
…[18 more quoted lines elided]…
> MySQL; but, I'll have the option.)

This brings to mind an interesting issue that we've been struggling with for
years at our shop.  This issue being, where does input validation belong?

Prior to the mid-1990s all of our data input to the mainframe was your good
ol' 3270 green screens.  For better or for worse, presentation logic and
business logic were implemented in the same CICS program.  Data validation
was hard coded directly in to the same CICS program.

We then started utilizing some distributed (Windows) applications to perform
some of these functions.  The same (if slightly modified) CICS programs
still existed on the back end and were utilized by the distributed
applications to actually get the data from there to here (the mainframe). 
All of the existing data validation remained in the CICS programs, but much
of the same logic was also put in to the distributed application.

One of the main reasons this was done was because the distributed
application has all those wonderful modern things such as drop-down lists,
radio buttons, etc.  In order to present the proper widgets (or whatever
they're called) to the end user the distributed application must, of course,
know what those valid values are.  Additionally, with those types of
applications the users are used to knowing pretty much immediately of they
have selected a valid option.  They don't want to go through all of the
effort of entering data, then at the end pressing enter and finally getting
back a message "such and such a value is invalid for this account type".

Just this year we implemented a project to 'web enable' a lot of our CSR
screens.  Again we ended up duplicating a lot of the
edits/validations/whatever you want to call them.  In some situations where
the logic is fairly complex and the relevant data resides on the mainframe
we will let things 'pass through' to be edited on the mainframe, but that's
fairly rare.

Another issue we come upon, even if we wanted to pass the edits through to
the mainframe, is that different applications sometimes allow for different
edits.  Here's a real example...  If an ATM card is ordered for a customer
who is a minor (under 18) there is a requirement that the order be approved
by an officer.  So the order is put in to a 'pending approval' queue.  If,
however, the card is ordered as part of setting up a new account through the
new accounts system (a distributed application) then the approval is *not*
required.  So I had to add logic to my CICS program to be able to
distinguish between the transaction being initiated directly (via a regular
3270 terminal session) and same transaction being initiated via a
distributed application (which actually still uses a regular 3270 terminal
session, but a 'psuedo signon' process is done by the distributed
application that lets the CICS program know that it's, well, a distributed
application).

Anyway, there are other cases where the 'end' application is more likely to
know what edits need to be in place, and to 'end' applications may not have
the same edits.  So putting the edits on the mainframe just makes things
worse.

Then again, most of the 'end' applications would have the *same* edits, and
so we end up with a lot of duplicate logic.  Even if the logic is somehow
combined, in, say, a Java object, that object cannot be utilized by a
regular Windows application, and certainly not by a mainframe application
(or mainframe OS does not support Java).

In the end we do what we have to do to make things work.  But no one is
really happy with it.

I don't know that we're going to change our direction at this point, but I
am curious about other's experiences.

Frank
```

###### ↳ ↳ ↳ field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 10)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-13T11:35:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C04207.6F0F.0085.0@efirstbank.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com>`

```
>>> On 8/13/2007 at 11:26 AM, in message
<46C03FC9.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick<Frank.Swarbrick@efirstbank.com> wrote:
> 
> This brings to mind an interesting issue that we've been struggling with 
…[91 more quoted lines elided]…
> am curious about other's experiences.

I didn't even finish my thoughts!  What made me think of this is the
possible use of the database for validation.  Most (all?) RDBMS allow for
fields to be validated at the database level.  This is all fine and dandy,
but is it really the best way to go?  Again, if you do this you allow the
user to input all of their fields into your application.  You then go to the
database to INSERT (or UPDATE) the record.  The database then decides that
one (or more!) of the values is invalid for their respective fields
(columns; whatever).  It just seems to me to be a lot of extra round trips
back and forth to the database to finally get valid data inserted.  Do
people really use the database for this?  Or to they code the data
validation in to their applications?

We're only now, from the mainframe side, starting to utilize a relational
database, so I have no real world experience when it comes to these things.

Thanks!

Frank
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 10)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-08-13T17:03:04-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q5e1c3dfemm1rrgrtahacviachdce8dmn4@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com>`

```
On Mon, 13 Aug 2007 11:26:01 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>>>> On 8/12/2007 at 8:59 PM, in message
><oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com>, LX-i<lxi0007@netscape.net>
…[79 more quoted lines elided]…
>(or mainframe OS does not support Java).

Java exists for both z/OS (unfortunately for you, probably not for
z/VSE) and Windows.
>
>In the end we do what we have to do to make things work.  But no one is
…[5 more quoted lines elided]…
>Frank
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-13T16:13:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C08338.6F0F.0085.0@efirstbank.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <q5e1c3dfemm1rrgrtahacviachdce8dmn4@4ax.com>`

```
>>> On 8/13/2007 at 2:03 PM, in message
<q5e1c3dfemm1rrgrtahacviachdce8dmn4@4ax.com>, Clark F
Morris<cfmpublic@ns.sympatico.ca> wrote:
> On Mon, 13 Aug 2007 11:26:01 -0600, "Frank Swarbrick"
> <Frank.Swarbrick@efirstbank.com> wrote:
…[8 more quoted lines elided]…
> z/VSE) and Windows.

Sorry, that was a typo.  I mean "our mainframe OS" (which is VSE and does
not support Java), not "or mainframe OS".

I know Windows (of course!) supports Java.  I have no idea if the Windows
guys would want to call Java routines.  As a one off thing, maybe.  As a
general rule?  I'm guessing not.

Frank
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-14T21:03:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5id9fsF3o9j5lU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <q5e1c3dfemm1rrgrtahacviachdce8dmn4@4ax.com> <46C08338.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:46C08338.6F0F.0085.0@efirstbank.com...
>>>> On 8/13/2007 at 2:03 PM, in message
> <q5e1c3dfemm1rrgrtahacviachdce8dmn4@4ax.com>, Clark F
…[19 more quoted lines elided]…
>

I wouldn't hesitate to call Java if the function I needed was available in a 
Java bean. (It can be easily brokered through CORBA.)

The way the question is formulated shows the difference in concepts.

You are still thinking in languages and source code; I think in functions 
needed, and simply don't care what it's written in. (that's why I have less 
resistance to stored DB procedures and triggers; it is just another 
language. To me the encapsulation of data and the validation of it, makes it 
worth the effort.)

This comes down to component based solutions as a general approach. I have 
applications with components written in VB, OO COBOL,  PowerCOBOL, and even 
one or two subroutines written in Standard (Fujitsu NetCOBOL) COBOL, and C#, 
some of which I wrote and some of which I didn't, (some of which I don't 
even have source code for, and don't need it) all playing nicely together 
(sometimes even in the same user window) to give a single, seamless, user 
experience.

Under Windows this was good, but under DotNET it is superb.

Interop services lets me call unmanaged code into my C# solution, and so I 
get to use all of the legacy components I need to, while re-wrapping them 
for a modern desktop (or Web) look and feel.

All new development is in C# as it lets stuff run on Windows or Linux  (or 
anywhere else that supports DotNET or Mono) without requiring a different 
compiler. (A bit like Java really... :-), but, having used both Java and C#, 
I have come to prefer C#)

Fortunately, I adopted an n-tier layered approach many years ago so there is 
no problem with different looking windows or themes. (Legacy presentation 
layer components are simply re-written in C#) This is about 20% of my 
legacy, so the remaining 80% that has no visual interface, can be easily 
re-used. I COULD re-use some of the Windows (PowerCOBOL, especially) stuff, 
but it just looks old-fashioned and dated.)

I'm currently revisiting an application I wrote 7 years ago for converting 
ISAM and VSAM/KSDS datasets into RDB. It is being enhanced to generate DDL 
for various RDBMS, and the whole thing is being re-wrapped into a single 
"Management Console" that lets you control the whole process from a single 
point. After refactoring PowerCOBOL and OO COBOL I was amazed to have the 
main function (analyzes COBOL source SELECT statements and FD/01 record 
definitions, then generates an ACCESS DB (really for documentation, but also 
for quick initial testing) and DDL for the RDB of your choice), run 
perfectly on the first attempt in the new DotNET environment, using the C# 
environment handling, control, and user interface.

When I first wrote this system from scratch it took 5 months; the upgrade 
and migration to DotNET will take 3/4 weeks with many original components 
being re-used without change, just "glued" together differently...New 
facilities are also being added. There is a possibility I may be asked to 
write some tools to automate the exisiting COBOL code conversion to RDB 
also. Any of you who have manually converted code and data to RDB will know 
that this is not to be undertaken lightly. It isn't just a matter of 
converting ISAM verbs to SQL; these are different paradigms, and OCCURS, 
REDEFINES, and group fields in the ISAM definitions have no place on the new 
RDB. It all has to be handled.

Once the RDB has been defined and normalized, it needs to be loaded. I can 
generate COBOL modules to do that (the client is a COBOL shop) and that was 
what led to my question regarding Batch Compiling Fujitsu COBOL (see 
different thread here in CLC)

I'm now thinking about NOT generating COBOL but simply generating DDL to 
load the data instead. (Of course I still have to read it  somehow, and it 
is in the ISAM system which is not readily open to tools other than COBOL.)

The point is that component based systems pay off in ways you can't even 
imagine when you build them. I had no idea 7 years ago that I would need to 
upgrade and enhance this system in some major ways, 7 years down the track. 
Now I'm being paid to do so, and thanking my lucky stars it is not a 
complete rewrite...in fact, I can focus on the new facilities rather than 
having to worry about complete redesigns and rebuilds of the old ones.

Encapsulation rules; objects are what matters; procedural source is as 
relevant as Latin.

(Of course there are enclaves where Latin is still important... Vatican City 
springs to mind... :-))

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-14T00:45:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9qtvl$sdd$1@reader1.panix.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com>`

```
In article <46C03FC9.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:

[snip]

>This brings to mind an interesting issue that we've been struggling with for
>years at our shop.  This issue being, where does input validation belong?

The users may say 'Data validation belongs where it causes response-time 
to be fastest.'

The programmers may say 'Data validation belongs where it causes changing 
code to be the easiest.'

Both of these may be considered as vectors; data validation, then belongs 
at the point where these two vectors intersect with a third one, said 
third vector being voiced by the one who says 'I sign the checks for the 
system; data validation belongs where it makes me smile the most.'

DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-08-14T05:43:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1gwi.873$924.548@newssvr23.news.prodigy.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <f9qtvl$sdd$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:f9qtvl$sdd$1@reader1.panix.com...
>
>>This brings to mind an interesting issue that we've been struggling with 
…[7 more quoted lines elided]…
> code to be the easiest.'

Striking a balance between features, performance and maitainability is a 
long-running  battle; rightly so, and rightly should and will continue.

I think there's also some kind of aphorism on this, something like "speed, 
features, maintainability: pick two" or something like that.

MCM
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-14T15:24:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9shf9$c3f$1@reader1.panix.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <f9qtvl$sdd$1@reader1.panix.com> <h1gwi.873$924.548@newssvr23.news.prodigy.net>`

```
In article <h1gwi.873$924.548@newssvr23.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:f9qtvl$sdd$1@reader1.panix.com...
>>
…[11 more quoted lines elided]…
>long-running  battle; rightly so, and rightly should and will continue.

I was trying to be even less specific than that, Mr Mattias, and 
attempting to liken the difficulty to that age-old question of 'what 
constitutes a Logical Unit of Work?'

Where something 'belongs', I'd say, depends on the criteria one uses to 
judge 'belonging'... and, as you point out, different groups have 
differing values that they use to weight criteria.

DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-14T10:40:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C1869C.6F0F.0085.0@efirstbank.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <f9qtvl$sdd$1@reader1.panix.com>`

```
>>> On 8/13/2007 at 6:45 PM, in message <f9qtvl$sdd$1@reader1.panix.com>,
<docdwarf@panix.com> wrote:
> In article <46C03FC9.6F0F.0085.0@efirstbank.com>,
> Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
…[19 more quoted lines elided]…
> system; data validation belongs where it makes me smile the most.'

In my shop the signers of checks often defer to the technical experts to
make these decisions.

Surprising, I know.

Frank
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-13T23:09:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iO2dnbe7vsZjpVzbnZ2dnUVZ_jydnZ2d@comcast.com>`
- **In-Reply-To:** `<46C03FC9.6F0F.0085.0@efirstbank.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
> 
> This brings to mind an interesting issue that we've been struggling with for
> years at our shop.  This issue being, where does input validation belong?

Our system had it in several places.  The date/time procedure I've 
mentioned before (P315) had validation on every routine in it.  We'd 
have programs that validated screen input, then passed it to a batch 
program that re-validates the same input.  While that may seem wasteful, 
it is of note that the batch program could be run without going through 
the screen.

When we put a GUI front-end, there were even more edits that happen on 
it, before the page is even submitted!  But, again, there are ways to 
script things that don't go through the GUI, so a program can't assume 
that the input has been validated before.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-14T21:30:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5idb0vF3n5b32U2@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <iO2dnbe7vsZjpVzbnZ2dnUVZ_jydnZ2d@comcast.com>`

```

```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-14T08:14:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13c3alhrifqq538@news.supernews.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <iO2dnbe7vsZjpVzbnZ2dnUVZ_jydnZ2d@comcast.com>`

```
LX-i wrote:
> Frank Swarbrick wrote:
>>
…[14 more quoted lines elided]…
> that the input has been validated before.

You can't have too much data validation. Even, as you say, when the data had 
presumbably already been validated.

One wonders how much code was recently written to check previously checked 
dates for Y2K...
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 10)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-08-14T16:57:43+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com>`

```
On Mon, 13 Aug 2007 11:26:01 -0600 "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

:>Prior to the mid-1990s all of our data input to the mainframe was your good
:>ol' 3270 green screens.  For better or for worse, presentation logic and
:>business logic were implemented in the same CICS program.  Data validation
:>was hard coded directly in to the same CICS program.

:>We then started utilizing some distributed (Windows) applications to perform
:>some of these functions.  The same (if slightly modified) CICS programs
:>still existed on the back end and were utilized by the distributed
:>applications to actually get the data from there to here (the mainframe). 
:>All of the existing data validation remained in the CICS programs, but much
:>of the same logic was also put in to the distributed application.

There are two kinds of validations, syntax and appropriateness.

An amount must be numeric (syntax) and be within a certain range
(appropriate).

February 30th fails on syntax, while Mar 23rd may fail due to being in the
wrong quarter, or wrong day of the week.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-14T08:42:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com>`

```
On Tue, 14 Aug 2007 16:57:43 +0300, Binyamin Dissen
<postingid@dissensoftware.com> wrote:

>There are two kinds of validations, syntax and appropriateness.
>
…[4 more quoted lines elided]…
>wrong quarter, or wrong day of the week.

Quite often I see syntax checking of a date that is really a waste of
resources - when it is followed by appropriateness checking that will
fail it anyway.

Part of this is our CoBOL background, where we check to see if a
denominator is zero before we do division, because that is easier than
handling the error if it is zero.  (Even if we expect that the number
isn't zero).     All the checking ahead of time every time uses up
resources that aren't needed with good exception handling.

An other edit is the inappropriate edit - when I enter my 9-digit zip
code on a web page and the program tells me to enter my zip code
correctly.    This is especially irritating when the database can
accept any sized postal code (handling foreign postal codes), but
notices that I'm from the U.S., so I must not know my 9-digit zip
code.

Why are they counting digits?    Because editing is Right and Proper?
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-15T03:22:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5idvmbF3p9c2pU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com...
> On Tue, 14 Aug 2007 16:57:43 +0300, Binyamin Dissen
> <postingid@dissensoftware.com> wrote:

>
> Why are they counting digits?    Because editing is Right and Proper?

No, Howard, editing string length for input fields on web pages is a 
valuable and accepted line of defence  against SQL inection attacks. (It is 
only one measure, but a very important one)

It is a pain (I hate writing it), but in today's world it is a necessary 
evil.

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-14T09:29:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com>`
- **References:** `<506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net>`

```
On Wed, 15 Aug 2007 03:22:49 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Why are they counting digits?    Because editing is Right and Proper?
>
…[5 more quoted lines elided]…
>evil.

Then allow me to enter my complete Zip code.   Are 9 digit postal
codes more dangerous to enter than are 5 digit postal codes?
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-15T11:45:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iet5aF3fmvltU1@mid.individual.net>`
- **References:** `<506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com...
> On Wed, 15 Aug 2007 03:22:49 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> codes more dangerous to enter than are 5 digit postal codes?

Allowing a longer input where a shorter one would do, is in principle, 
higher risk.

I don't know about your Zip codes, specifically, so I can't comment on that.

I do know that allowing excessive length ('excessive' being 'more than 
required') on a web input field is taking a risk that can be eliminated if 
you don't allow it. Certainly, I can't think of much I can do with 4 
characters of SQL, but there are smarter people than me out there (maybe 
tokenized...I dunno.) Why take the risk?

I would add that if you think the use of a web page is stupid, most Web 
Masters would be pleased to have your input (I like it when people complain 
about my pages because I fix them and the complaints diminish... Then the 
next site I build, I have all that user experience :-))

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 15)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-08-14T22:43:07-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6am4c3l84ammkrlt7rl1uijlvieum076jb@4ax.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net>`

```
On Wed, 15 Aug 2007 11:45:45 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[27 more quoted lines elided]…
>tokenized...I dunno.) Why take the risk?

Zip codes in the US were originally 5 digits.  They later added a 4
digit suffix to allow more precise sorting.  I thing that what Howard
is referring to is a an application where the 9 digit zip code or is
used by the back end of the application yet the person who designed
the application only allowed entry of the 5 digit code.  All fields
should be checked to be sure they fit (Old 3270 green screens did it
automatically) but fit should match overall reality. 
>
>I would add that if you think the use of a web page is stupid, most Web 
…[4 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 15)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-15T08:19:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net>`

```
On Wed, 15 Aug 2007 11:45:45 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I would add that if you think the use of a web page is stupid, most Web 
>Masters would be pleased to have your input (I like it when people complain 
>about my pages because I fix them and the complaints diminish... Then the 
>next site I build, I have all that user experience :-))

I have complained to Web masters, and the evidence is overwhelming
that your attitude is rare.

For instance, the way most common response to bugs found is that they
won't support anything except I.E.    They keep track, and people who
use their web page are overwhelming I.E.  (Because nothing else works,
and many browsers lie anyway).    Besides, more customers mean more
work.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-16T05:01:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5igrj7F3p3p7nU1@mid.individual.net>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com...
> On Wed, 15 Aug 2007 11:45:45 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> that your attitude is rare.

I'm sorry to hear that, Howard. Obviously, I talk to people who are like 
me... :-)
>
> For instance, the way most common response to bugs found is that they
> won't support anything except I.E.

Ah, now that's not quite the same thing.

I don't think people who don't build web sites realise how REALLY hard it is 
to make everything work across Browsers.

It is getting better with the advent of more server based code and dynamic 
generation of pages (servers are getting smart enough to generate the right 
code for whatever the Client Browser (given some encouragement from web 
developers)), but it is still a huge amount of work.

I'm currently working on a major site (although it's had to move to the 
"pending" queue while I complete the database migration tools I'm doing for 
a client.)

I was pretty thrilled with it, as it is the most ambitious thing I've done 
with web programming, so far. It is all ASP.NET and C# with themed headers 
and footers, alternate dynamic master pages and almost no JavaScript 
(everything is coded in C# on code-behind pages that run on the server. It 
looks pretty cool (I'm biased, of course...:-)) but imagine my horror when I 
found it rendered completely differently, not just on different Browsers, 
but on different versions of IE as well!

The "experience" on IE7 was a dream; on IE6, it was the occasional snore, 
IE5 it was more like restless sleep, and on Firefox it was a nightmare :-). 
I never would have known if I hadn't got people to try testing it, and they 
sent me some screen shots that showed themes not rendered, pages misaligned, 
text fonts that were simply ugly, colors not rendering correctly, and some 
minor logic bugs in processes for using the Web Service and various 
downloads.

I resolved to fix it (it isn't live yet, so it was more the challenge of it 
than any particular desire to meet customer demand...:-)) I spent three full 
days just finding out what I COULD do and getting it is close as possible 
across Browsers. I have tested it with FireFox, Netscape and IE5 thru IE7 
and it is much better (although it is still definitely best when seen with 
IE7). But this was several days of intensive work over long hours, and for 
very little real gain. It still looks exactly the same in IE7 as it did 
before; I might just as well have done nothing... :-)

Now, if someone was paying me to develop this site I simply couldn't spend 
that amount of time on the "Cross Browser" problem.. Server stats showed 
that for the brief time I let people access it, 93% were using IE. (Previous 
sites I've done have reported over 85%). It just isn't viable to develop for 
anything other than IE. It's a pity, and I wish it weren't so, but that is 
the reality of it. As long as the page renders in other Browsers, that's the 
best I can do...(If you see flat, lifeless, buttons and scraggly fonts in 
odd colours, and input fields that don't tab correctly, as long as the page 
is aligned correctly and is visible, that's all I can guarantee...)

> They keep track, and people who
> use their web page are overwhelming I.E.  (Because nothing else works,
> and many browsers lie anyway).    Besides, more customers mean more
> work.

Yes, IE has the market place pretty tied up. To be fair, it is much better 
than it was, but it is also more resource hungry (I'm running a 2GB notebook 
and I've seen IE7 using over 250MB...sometimes it freezes, although it has 
never crashed the system (so far...).

So, the bottom line is, Howard, that complaints about problems in other 
Browsers are just relegated to the bottom of the heap, unless they are 
really drastic; things like windows not floating properly, animations not 
activating, sound files refusing, video timing out, are all not going to get 
fixed because it just isn't economic. In three days I could add new, revenue 
generating, functionality that at least 85% of the traffic can enjoy without 
problem... the people who would be paying me want maximum bang for their 
buck.

I am using software and platforms that cost serious money and it STILL isn't 
easy to get Cross Browser compatibility. Between Visual Studio and 
Dreamweaver it is possible to emulate every type of Browser and screen size. 
I've done it. It makes no difference. Looks fine in emulation, look at it 
with the real thing, and it isn't...

So now I'm only guaranteeing support for IE...

And that was where we came in... :-)

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-15T12:45:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8i6c35aaghi828vpkegonh5d7mqqqim4d@4ax.com>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net>`

```
On Thu, 16 Aug 2007 05:01:42 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> For instance, the way most common response to bugs found is that they
>> won't support anything except I.E.
…[4 more quoted lines elided]…
>to make everything work across Browsers.

There are de jure and de facto standards.    If the web code was
designed to work with the de jure standards, it should work with
minimal changes with all of the browsers that claim to follow those
standards.   Which is every browser except one.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-15T12:53:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net>`

```
On Thu, 16 Aug 2007 05:01:42 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>So now I'm only guaranteeing support for IE...
>
>And that was where we came in... :-)

Good thing I don't need to be your customer.   You will find that your
stats will back up your assertion that those who can't use your web
site won't use your web site.

Now, I have used Opera with its default setting to say it is IE, and I
use Firefox and Safari.   But I won't use sites that demand Active-X
be enabled.   My wife's iMac doesn't even have it installed.

Being excluded from web sites isn't a matter of indifference to me and
for lots of people who don't use IE.   It's a matter of anger.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T02:06:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ij3vpF3q2meaU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com...
> On Thu, 16 Aug 2007 05:01:42 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> for lots of people who don't use IE.   It's a matter of anger.

It's a bit like shooting yourself in the foot... no-one is excluding you 
except yourself.

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-16T09:10:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net>`

```
On Fri, 17 Aug 2007 02:06:46 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Being excluded from web sites isn't a matter of indifference to me and
>> for lots of people who don't use IE.   It's a matter of anger.
>
>It's a bit like shooting yourself in the foot... no-one is excluding you 
>except yourself.

Ahh, blame the (non) customer.

But check around.   Lots of people are angry because web sites want us
to use Windows, I.E., and active-X.    I am reporting facts that I
have observed on newsgroups, and have observed in my workplace.

If a company doesn't mind prospective customers being angry and not
being able to use their sites - it doesn't matter whether the fault is
those prospective customers' failure to conform to Microsoft's failure
to conform.    They won't be customers.

In fact, they will be anti-customers - sharing their anger with
others.

Now companies are free to decide that IE is the de facto standard, and
those using de jure standard browsers aren't worthwhile.   That is
their right.    But designing around de jure standards isn't that
expensive and is more inclusive.   That's worth money.   (It may be
that you can't use MS designed tools though).
```

###### ↳ ↳ ↳ Browser standards was Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-08-16T13:17:36-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lut8c3lgf3rlf85gbfdmhfdgr1bvcrcmke@4ax.com>`
- **References:** `<46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com>`

```
On Thu, 16 Aug 2007 09:10:23 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Fri, 17 Aug 2007 02:06:46 +1200, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[25 more quoted lines elided]…
>that you can't use MS designed tools though).

Just to add fuel to the fire, if your web-site is commercial or
government, in some countries including the United States the site is
required to be able to handle a person who has one of the following
disabilities: vision, hearing, motion (unable to use a mouse, has no
hands, etc.).  The site does not have to be able to handle someone
like the late Helen Keller who was both blind and deaf.
```

###### ↳ ↳ ↳ Re: Browser standards was Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-16T11:54:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187290476.205601.102540@a39g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<lut8c3lgf3rlf85gbfdmhfdgr1bvcrcmke@4ax.com>`
- **References:** `<46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <lut8c3lgf3rlf85gbfdmhfdgr1bvcrcmke@4ax.com>`

```
On 16 Aug, 17:17, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Thu, 16 Aug 2007 09:10:23 -0600, Howard Brazee <how...@brazee.net>
> wrote:
…[41 more quoted lines elided]…
> - Show quoted text -

Which part of BLIND does not encompass VISION?

Blind people are able to use one of a number of audio browsers but
that wouldn't help Helen Keller. However, there is a screen reader
which converts text to Braille available. How it would manage with
Pete's fluff and eye-candy is anyones guess.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-16T15:26:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13c9cmei9ja2s1c@news.supernews.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com>`

```
Howard Brazee wrote:
>
> Now companies are free to decide that IE is the de facto standard, and
…[3 more quoted lines elided]…
> that you can't use MS designed tools though).

No, it's good public policy. FireFox, for example, is known to give your cat 
warts.

By insisting on IE, a responsible corporate entity is helping you do the 
right thing... insofar as your cat is concerned.

If you don't have a cat, you should be okay (unless you have a parrot or a 
gerbil).
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T18:52:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ikutnF3pqc6lU1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13c9cmei9ja2s1c@news.supernews.com>`

```

```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 22)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-17T03:09:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187345364.445022.294760@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<5ikutnF3pqc6lU1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13c9cmei9ja2s1c@news.supernews.com> <5ikutnF3pqc6lU1@mid.individual.net>`

```
On 17 Aug, 07:52, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> --
> "I used to write COBOL...now I can do anything.""HeyBub" <heybubNOS...@gmail.com> wrote in message
…[25 more quoted lines elided]…
> his balls, well, it was just heart-rending.

I don't think that you can catch warts from a parrot. Warts originated
in sheep and are spread by human-to-human contact. Perhaps your ex-
wife, UPPERCASE, had the warts and spread them to Waldo? or maybe you
are just getting confused with nomenclature and instead of warts you
mean psillicosis?

>
> Then Schroedinger pounced on Waldo,

Are you sure?

 who was distracted by the wart
> developing on his nose, and devoured him while I was out of the house.
> Schroedinger left me Waldo's feet and the nose wart as a trophy, never
…[6 more quoted lines elided]…
> ccccoollllllllld!!"

Definitely psillicosis.

> or "So, what're YOU looking at?!"   if visitors
> arrived. This was disappointing for me as I had spent hours teaching her
…[12 more quoted lines elided]…
>

I find it more convenient, and productive, to switch Bonzo off. That
office assistant is too annoying.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-18T13:47:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5in1e2F3oc2odU1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13c9cmei9ja2s1c@news.supernews.com> <5ikutnF3pqc6lU1@mid.individual.net> <1187345364.445022.294760@g4g2000hsf.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1187345364.445022.294760@g4g2000hsf.googlegroups.com...
> On 17 Aug, 07:52, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[42 more quoted lines elided]…
> Are you sure?

Well, he did, and he didn't...

>
> who was distracted by the wart
…[13 more quoted lines elided]…
> Definitely psillicosis.

Don't be psilli... she had psittacososis, caused by the wart virus on 
Schroedinger mutating into an airborne bacterium.
>
>> or "So, what're YOU looking at?!"   if visitors
…[19 more quoted lines elided]…
>

Oh, Bonzo ate that annoying puppy as a snack a long time ago... I had Dr 
Einstein there for a while, but he went off somewhere relatively obscure. 
Since then, I've disabled the Office Assistants too. Eye candy is one thing, 
but this is more like eye brussels sprouts...

Pete
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 24)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-18T03:40:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187433657.816642.205450@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5in1e2F3oc2odU1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13c9cmei9ja2s1c@news.supernews.com> <5ikutnF3pqc6lU1@mid.individual.net> <1187345364.445022.294760@g4g2000hsf.googlegroups.com> <5in1e2F3oc2odU1@mid.individual.net>`

```
On 18 Aug, 02:47, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
>
> > Definitely psillicosis.
>
> Don't be psilli... she had psittacososis, caused by the wart virus on
> Schroedinger mutating into an airborne bacterium.


Sorry, we both got the spelling wrong: psittacosis (apparently related
to fave-rave-disease-of-the-moment Chlamydia, so popular in the
media).
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-18T23:13:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5io2j9F3q4c7sU1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13c9cmei9ja2s1c@news.supernews.com> <5ikutnF3pqc6lU1@mid.individual.net> <1187345364.445022.294760@g4g2000hsf.googlegroups.com> <5in1e2F3oc2odU1@mid.individual.net> <1187433657.816642.205450@50g2000hsm.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1187433657.816642.205450@50g2000hsm.googlegroups.com...
> On 18 Aug, 02:47, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[11 more quoted lines elided]…
>

Mine was a typo; I'm actually quite good at speeling :-)....

Pete
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-17T16:22:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13cc4bfd5k4kre9@news.supernews.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com>`

```
Howard Brazee wrote:
>
> Ahh, blame the (non) customer.
…[17 more quoted lines elided]…
> that you can't use MS designed tools though).

WHY FIREFOX IS BLOCKED website(!)

"The Mozilla Foundation and its Commercial arm, the Mozilla Corporation, has 
allowed and endorsed Ad Block Plus, a plug-in that blocks advertisement on 
web sites and also prevents site owners from blocking people using it."

http://whyfirefoxisblocked.com/
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-18T15:55:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R-mdnXhcca5y91rbnZ2dnUVZ_gSdnZ2d@comcast.com>`
- **In-Reply-To:** `<13cc4bfd5k4kre9@news.supernews.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13cc4bfd5k4kre9@news.supernews.com>`

```
HeyBub wrote:
> Howard Brazee wrote:
>> Ahh, blame the (non) customer.
…[23 more quoted lines elided]…
> web sites and also prevents site owners from blocking people using it."

Yeah - heaven forbid *we* control the content *we* display on *our* 
computers...  This arrogance infuriates me.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 22)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-20T10:58:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13cjeh2pcgefa71@news.supernews.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13cc4bfd5k4kre9@news.supernews.com> <R-mdnXhcca5y91rbnZ2dnUVZ_gSdnZ2d@comcast.com>`

```
LX-i wrote:
>> WHY FIREFOX IS BLOCKED website(!)
>>
…[6 more quoted lines elided]…
> computers...  This arrogance infuriates me.

I dunno. If one wants to get warts by using Fx, then, sure, it's his choice. 
But since Fx causes the cat to develop warts, I'm not sure whether using Fx 
could be construed as animal cruelty...

Of course, if you don't have a cat, you should be okay.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 23)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-20T18:03:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XY6dnVymO4pEtlfbnZ2dnUVZ_qfinZ2d@comcast.com>`
- **In-Reply-To:** `<13cjeh2pcgefa71@news.supernews.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net> <gep8c3dipshvvv56mv63qckf4a1ogvfrlr@4ax.com> <13cc4bfd5k4kre9@news.supernews.com> <R-mdnXhcca5y91rbnZ2dnUVZ_gSdnZ2d@comcast.com> <13cjeh2pcgefa71@news.supernews.com>`

```
HeyBub wrote:
> LX-i wrote:
>>> WHY FIREFOX IS BLOCKED website(!)
…[12 more quoted lines elided]…
> Of course, if you don't have a cat, you should be okay. 

No cats, no dogs, no gerbils...  And if the ants that won't go away get 
warts, then that's fine with me.  :)
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-16T20:54:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e_GdnWN9vPR1kFjbnZ2dnUVZ_rXinZ2d@comcast.com>`
- **In-Reply-To:** `<5ij3vpF3q2meaU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com> <5ij3vpF3q2meaU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:8fi6c39v6ltegtd71t8ekjpasocgbpnhbg@4ax.com...
…[5 more quoted lines elided]…
> except yourself.

Are you serious?  :)  IE is a big security hole.  Sure, there's not a 
problem if you only use it on trusted web sites, but it's a pain to 
change browsers just to view another site.  Should they lower their 
security just to use a web site?
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 17)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-08-15T11:55:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187204145.654608.51560@j4g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5igrj7F3p3p7nU1@mid.individual.net>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net>`

```
On Aug 16, 5:01 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> I don't think people who don't build web sites realise how REALLY hard it is
> to make everything work across Browsers.

It is really easy to do so, just follow the standards that are set by
W3. Oh, wait, then IE fails.

Of course if you try to use all the Windows specific cruft that can be
exploited by spyware and such then, yes, it is really hard.

> The "experience" on IE7 was a dream; on IE6, it was the occasional snore,
> IE5 it was more like restless sleep, and on Firefox it was a nightmare :-).

That is most likely because you were using IEisms and Windowsisms,
just like a good Microsoftee should.

> Now, if someone was paying me to develop this site I simply couldn't spend
> that amount of time on the "Cross Browser" problem.. Server stats showed
> that for the brief time I let people access it, 93% were using IE. (Previous
> sites I've done have reported over 85%).

That depends on what you are measuring, it may be because anyone using
another browser sees the first page as crap and wanders off without
making a couple of dozen hits.

> So, the bottom line is, Howard, that complaints about problems in other
> Browsers are just relegated to the bottom of the heap, unless they are
> really drastic; things like windows not floating properly, animations not
> activating, sound files refusing, video timing out, are all not going to get
> fixed because it just isn't economic.

I have Firefox with add-ons that block flash, kill animations, refuse
sound, block pop-ups and advertising sites, and won't run scripts
(unless I specifically allow). Naturally Active-X is completely out.

You may design sites that look like flash adverts on TV, but I won't
watch those. Animations and flash are distracting, 'arty' backgrounds
and colours can make sites unreadable.

I also have an addon 'Web Developer', with one click I can turn off
'all styles' and get the information content as black text on white
background that I can read comfortably.

> In three days I could add new, revenue
> generating, functionality that at least 85% of the traffic can enjoy without
> problem... the people who would be paying me want maximum bang for their
> buck.

You say 'revenue generating'. That usually means adverts flashing at
me. Am I supposed to 'enjoy' those ?

Some sites are made like the DVDs that won't skip the trailers, or TV
recorders that won't skip over adverts. Just don't go there/buy them,
or get a browser/player that bypasses the crap.


> I am using software and platforms that cost serious money and it STILL isn't
> easy to get Cross Browser compatibility. Between Visual Studio and
> Dreamweaver it is possible to emulate every type of Browser and screen size.
> I've done it. It makes no difference. Looks fine in emulation, look at it
> with the real thing, and it isn't...

That may be deliberate, especially the 'Visual Studio'.

> So now I'm only guaranteeing support for IE...

If it is advertising, pop-ups, flash, animations, sound then that is
excellent, please ensure that _nothing_ shows for Firefox.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 17)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-15T21:09:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com>`
- **In-Reply-To:** `<5igrj7F3p3p7nU1@mid.individual.net>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com...
…[6 more quoted lines elided]…
> to make everything work across Browsers.

It is actually easier now - especially now that IE 7 supports more of 
the W3's standards.  :)

> It is getting better with the advent of more server based code and dynamic 
> generation of pages (servers are getting smart enough to generate the right 
> code for whatever the Client Browser (given some encouragement from web 
> developers)), but it is still a huge amount of work.

I don't think that's the answer.  With the separation of content and 
style, the style should be constant, and the content dynamic.

> I was pretty thrilled with it, as it is the most ambitious thing I've done 
> with web programming, so far. It is all ASP.NET and C# with themed headers 
…[4 more quoted lines elided]…
> but on different versions of IE as well!

What are you using to make the client side dynamic?  AJAX?  Or does it 
post-back for things that would normally be done in JavaScript?

> The "experience" on IE7 was a dream; on IE6, it was the occasional snore, 
> IE5 it was more like restless sleep, and on Firefox it was a nightmare :-).

IE 7 is pretty good - it's the best IE I've ever seen.  IE 6, well - 
that's what we're mandated to use at work.  At least until this fall, 
when the Air Force's Standard Desktop Configuration (SDC) 2.0 drops - 
Vista, IE 7, and Office 2007 for all!

IE 5?  Who cares?  :)  Since Ford started producing the Thunderbird and 
the Mustang, do they still produce Model T's?

Firefox is not too bad.  Of course, I write my code by hand, and develop 
in Firefox.  I've had similar experiences developing on Firefox and then 
looking at the site in IE!

> I resolved to fix it (it isn't live yet, so it was more the challenge of it 
> than any particular desire to meet customer demand...:-)) I spent three full 
…[5 more quoted lines elided]…
> before; I might just as well have done nothing... :-)

No - bringing your site within standards isn't useless.  :)  Think of it 
as future-proofing.  Lots of sites that worked great with IE 6 simply 
didn't work with IE 7 - and that's the same browser, just different 
versions!  I foresee better support for W3 standards coming in future 
versions of browsers, not worse; developing to a given standard can help 
alleviate surprises.

> I am using software and platforms that cost serious money and it STILL isn't 
> easy to get Cross Browser compatibility. Between Visual Studio and 
> Dreamweaver it is possible to emulate every type of Browser and screen size. 
> I've done it. It makes no difference. Looks fine in emulation, look at it 
> with the real thing, and it isn't...

Sometimes Notepad can be your friend!  :)  heh...

I'm not knocking what you've done.  I've done the same thing (mostly in 
reverse, but I know where you're coming from).  What I found really 
helped was looking up the CSS stuff on the W3C's web site, and putting 
most of my styles in CSS.  I know in the .NET environment, it's not 
quite as easy (although I think most of the controls have CssClass as 
one of their properties) or "automatic", but I've found that if I do it 
that way, it usually doesn't take much to make it work in both Firefox 
and IE.

I'd be happy to take a quick gander at some of the more problematic 
areas if you'd like.  :)  You know where to find me...
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T03:15:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ij7voF3pimneU1@mid.individual.net>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com>`

```


"LX-i" <lxi0007@netscape.net> wrote in message 
news:UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com...
> Pete Dashwood wrote:
>> "Howard Brazee" <howard@brazee.net> wrote in message 
…[18 more quoted lines elided]…
> style, the style should be constant, and the content dynamic.

Hmmm... yes and no. If I can serve dynamic content, why shouldn't I do so 
with dynamic style? (I can, of course, as long as I get themes and CSS 
right... ;-))
>
>> I was pretty thrilled with it, as it is the most ambitious thing I've 
…[8 more quoted lines elided]…
> post-back for things that would normally be done in JavaScript?

It just missed AJAX. I have downloaded the AJAX tutorials and am about 40% 
through them. I simply haven't got time (or inclination) to go back and 
change it.  There is some posting back as nearly all code is running on the 
server. Fortunately it doesn't seem to make much impact. The data 
transferred is minimal and it is no longer necessary to load a full page in 
order to update it. (AJAX achieves this by using client JavaScript I think? 
But you can do it in other ways as well.)
>
>> The "experience" on IE7 was a dream; on IE6, it was the occasional snore, 
…[13 more quoted lines elided]…
> looking at the site in IE!

I coded my first web site entirely in Notepad using frames and all kinds of 
stuff that is now 'deprecated'.  VS 2005 is better. And Dreamweaver Studio 8 
is great for keeping it honest.

I became quite facile in JavaScript but I prefer C# and I like the added 
security of running compiled code on the server.
>
>> I resolved to fix it (it isn't live yet, so it was more the challenge of 
…[14 more quoted lines elided]…
> alleviate surprises.

Again, yes and no... From a theoretical point of view it is certainly more 
professional and better practice to do that. But the Web is not about being 
professional... I want the most fun sites I can build. I DON'T look at stuff 
in B&W as Richard does, and I can't imagine running without ActiveX. I LIKE 
fluff and eye-candy and I enjoy looking at other people's sites and enjoying 
the features they have incorporated into them. It is fun. There is a lot of 
satisfaction in having talking heads or unexpected sound effects ... I 
accept cookies and I do allow ActiveX. But I'm not stupid about it... :-)

If a standard prevents me running Flash for example, then the Hell with the 
standard. If  15 percent of people can't see my site because they won't run 
a MS Browser on principle, then I see that as their loss. (I don't hesitate 
to open Firefox if I want a different perspective; it is just crazy to get 
emotional about this stuff and I am always amazed by the heat it engenders.) 
Howard, a normally very reasonable man, gets angry about being "excluded" 
and is thankful he isn't a customer of mine. (Actually, I take customer 
service VERY seriously and have the referrals to prove it...) Richard gets 
scathing and calls me a "good little MicroSoftee..."  as if I was guilty of 
some heinous crime.

All I'm doing is building some web sites and having some fun. I tried to 
explain honestly and unemotionally why certain Web Masters (self included) 
can't drop everything because some effect doesn't render in a non-MS 
Browser, and why the support has to go into IE, but I might as well have not 
bothered. The only rational response was yours, Daniel. Thank you for that.



>> I am using software and platforms that cost serious money and it STILL 
>> isn't easy to get Cross Browser compatibility. Between Visual Studio and 
…[4 more quoted lines elided]…
> Sometimes Notepad can be your friend!  :)  heh...

Yes, I know, but I like to think I have made some progress in 15 years... 
:-)

Actually the tools ARE very useful and most of mine have paid for themselves 
many times over. Therer are SO many options and possibilities that it just 
isn't realistic to be reading all the working papers coming out of W3C...

Besides, the development tools should keep track of it for me (they do up to 
a point...)

The three days I spent was well spent and I have learned a good deal. The 
process (and hopefully, the growth, goes on...) The site is now on a back 
burner anyway, and I am up to my ears in desktop C# and COBOL at the moment. 
I have to write a tool that I have re-designed 5 times and am still not 
happy with, so writing this is a welcome break... Maybe on the 6th time, 
after a break, it will fall into place...the problem is that a Normalized DB 
has no repeating groups ( My software creates linked tables as required by 
2NF, when it encounters OCCURS in the ISAM definition). Now, I need to load 
the data from the original files onto the DB tables. Pretty easy, you'd 
think; just read ISAM and "write" RDB...And it would be, if not for OCCURS 
and REDEFINES...:-)  Never mind, it is keeping me off the streets...:-)
>
> I'm not knocking what you've done.  I've done the same thing (mostly in 
> reverse, but I know where you're coming from).  What I found really helped 
> was looking up the CSS stuff on the W3C's web site, and putting most of my 
> styles in CSS.

I use CSS extensively and have done for a few years now.

> I know in the .NET environment, it's not quite as easy (although I think 
> most of the controls have CssClass as one of their properties) or 
> "automatic", but I've found that if I do it that way, it usually doesn't 
> take much to make it work in both Firefox and IE.

Yes, CSS certainly helps in that regard
>
> I'd be happy to take a quick gander at some of the more problematic areas 
> if you'd like.  :)  You know where to find me...

That's very kind, Daniel. Thanks, I appreciate it. At the moment, I have no 
problems with the Web Site. (Apart from not being able to work on it and get 
it live... it is almost there but not quite.) There are some quite sexy 
downloads where I have deployed with OneClick... and I need to test this 
stuff in other Browsers. BTW, you might be interested to know that adding a 
Web Service to your site really improves rankings. I haven't even begun to 
promote the site or registered it with any SEs, or even added bot 
encouragement, links, or even meta keywords to it, but the web site is 
already ranked (and it isn't even live yet) because the Web Service was 
picked up almost instantly.

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-16T09:43:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d0s8c3la8f8rfrf3rmlf6ekpjgek1c0dch@4ax.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net>`

```
On Fri, 17 Aug 2007 03:15:01 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>If a standard prevents me running Flash for example, then the Hell with the 
…[5 more quoted lines elided]…
>and is thankful he isn't a customer of mine. 

I didn't mention my own emotional state.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T04:21:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ijbs4F3oisb3U1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <d0s8c3la8f8rfrf3rmlf6ekpjgek1c0dch@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:d0s8c3la8f8rfrf3rmlf6ekpjgek1c0dch@4ax.com...
> On Fri, 17 Aug 2007 03:15:01 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> I didn't mention my own emotional state.

<post from Howard>

"Being excluded from web sites isn't a matter of indifference to me and
for lots of people who don't use IE.   It's a matter of anger."

</post from Howard>

(You were probably so angry you didn't realise you'd said it :-))

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-16T12:21:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l659c3tphga28932ps62r7qdkf1i7jgkee@4ax.com>`
- **References:** `<p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <d0s8c3la8f8rfrf3rmlf6ekpjgek1c0dch@4ax.com> <5ijbs4F3oisb3U1@mid.individual.net>`

```
On Fri, 17 Aug 2007 04:21:18 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> I didn't mention my own emotional state.
>
…[3 more quoted lines elided]…
>for lots of people who don't use IE.   It's a matter of anger."

I tried to make it about people in general - I guess I failed.

></post from Howard>
>
>(You were probably so angry you didn't realise you'd said it :-))

Possibly 8^).

My own shop doesn't test with Safari, despite being a university with
lots of Apple users.    Maybe that's because they don't believe
students will stop paying tuition because the scheduling might not
work with their computers.   But the whole reason we went to the web
was to save money - computers are cheaper than employees.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-16T09:27:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187281620.024182.304160@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5ij7voF3pimneU1@mid.individual.net>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net>`

```
On 16 Aug, 16:15, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:

>
> > IE 5?  Who cares?  :)  Since Ford started producing the Thunderbird and
> > the Mustang, do they still produce Model T's?

A little while ago I came across the information that the most common
installed browser was IE3 and that the most rapidly improving in
numbers browser was IE6. The reasoning went along the lines that IE3
was so popular because a lot of people had old machines and did not do
any browser upgrades (eg my dad) and IE6 was the new rave flavour,
having just been released. I suppose IE7 will replace IE6 in those
stats now.

>
>
…[3 more quoted lines elided]…
>

Ditto with me.

>
> >> I resolved to fix it (it isn't live yet, so it was more the challenge of
…[7 more quoted lines elided]…
> >> :-)

What about IE, IE2, IE3, IE4, Netscape Navigator...... Opera et al?
At what point does one decide to junk support for old or minority
browsers and go, instead, for the majority browser(s)?

Or should one hust code for the W3 standards and to hell with IE's
idiosyncracies?

>
> I DON'T look at stuff
> in B&W as Richard does, and I can't imagine running without ActiveX.

I prize security above fluff and eye-candy. Just say NO to activex.

As for fluff and eye-candy: It takes forever to download a megabyte of
fluff at 56 kpbs (and a lot of people have slower modems than that).
But this brings us back to whether one should design/build for the
latest whizz-bang pc or aim to be more inclusive.

> I LIKE
> fluff and eye-candy and I enjoy looking at other people's sites and enjoying
…[6 more quoted lines elided]…
> a MS Browser on principle, then I see that as their loss.

I said much the same to a guy who used some text based browser
(opera?). He went super-nova! People can get heated about these sorts
of things (it beats the old paragraph v. section argument).
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-16T12:23:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<od59c3dsj04jkaf1ihj439b7g9cg1jd8gs@4ax.com>`
- **References:** `<46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com>`

```
On Thu, 16 Aug 2007 09:27:00 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>I said much the same to a guy who used some text based browser
>(opera?). He went super-nova! People can get heated about these sorts
>of things (it beats the old paragraph v. section argument).

That has been my experience - I've seen lots of people who get quite
angry over such slights.

I'm too intellectual in my emotional responses - my daughter says I
must be bottling it in, because she believes anger is natural.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-16T21:25:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com>`
- **In-Reply-To:** `<1187281620.024182.304160@50g2000hsm.googlegroups.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com>`

```
Alistair wrote:
> On 16 Aug, 16:15, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[10 more quoted lines elided]…
> stats now.

Yikes.  IE 3 sucked!  (Even when it was new, Netscape Navigator 2 blew 
it away...)

> What about IE, IE2, IE3, IE4, Netscape Navigator...... Opera et al?
> At what point does one decide to junk support for old or minority
…[3 more quoted lines elided]…
> idiosyncracies?

It doesn't have to be either/or.  :)  I've found that everything that 
works with Firefox also works with Konqueror - the fonts are rendered at 
a different size, but the boxes and lines are the same.

I don't have any qualms at all about not supporting IE 6.  Even though, 
in my previous post, I called IE a security hole, IE 7 is much better 
than IE 6.  I know IE 7 can be installed on XP and Vista, and I think 
it'll go on W2K as well.  98/ME?  Heck, if Microsoft isn't supporting 
one of its own OS's, why should I?  :)

>> If a standard prevents me running Flash for example, then the Hell with the
>> standard. If  15 percent of people can't see my site because they won't run
…[4 more quoted lines elided]…
> of things (it beats the old paragraph v. section argument).

That was probably lynx.  True, there can be some heated debate on this. 
  My biggest gripe with Flash is that they won't make a 64-bit Flash 
plug-in.  I have to maintain 2 versions of Firefox, just so I can see 
YouTube or other active content (Java, etc.).

(Of course, normally, not having all those flashing animations is fine 
with me.  Between running the AdBlock Plus plug-in and a 64-bit browser, 
I don't really have many annoyances at all in my journeys through the web.)

I'm probably dating myself now - does anyone remember the 7-bit versus 
8-bit debates on FidoNet?  heh heh heh...
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-17T02:53:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187344380.421127.8560@a39g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com> <bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com>`

```
On 17 Aug, 04:25, LX-i <lxi0...@netscape.net> wrote:
> Alistair wrote:
> > On 16 Aug, 16:15, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
…[11 more quoted lines elided]…
> it away...)

Strangely, I don't think I was being judgemental. IE3 did what I
needed it to do on Win95 back in ye olden dayse.

>
> I'm probably dating myself now - does anyone remember the 7-bit versus
> 8-bit debates on FidoNet?  heh heh heh...

I was probably still in nappies (diapers in the US).
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-17T12:09:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa436i$9oo$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com> <bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com> <1187344380.421127.8560@a39g2000hsc.googlegroups.com>`

```
In article <1187344380.421127.8560@a39g2000hsc.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>I was probably still in nappies (diapers in the US).

Let's see... 'nappies' are 'basic garments for infants consisting of a 
folded cloth or other absorbent material drawn up between the legs and 
fastened about the waist' (http://www.m-w.com) and not periods of 
'sleeping briefly (especially during the day)'.

'Walkies' are 'acts or instances of going on foot especially for exercise 
or pleasure' and not... some other item of clothing.

Amazing what damage some folks have done to the King's English, eh?

DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 23)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-17T09:33:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187368432.007049.131010@57g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<fa436i$9oo$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com> <bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com> <1187344380.421127.8560@a39g2000hsc.googlegroups.com> <fa436i$9oo$1@reader1.panix.com>`

```
On 17 Aug, 13:09, docdw...@panix.com () wrote:
> In article <1187344380.421127.8...@a39g2000hsc.googlegroups.com>,
>
…[16 more quoted lines elided]…
> DD

Aye, but then tis your fault for letting them abuse the language, yer
majesty. <touches forelock>
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-17T16:55:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa4ju2$lok$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187344380.421127.8560@a39g2000hsc.googlegroups.com> <fa436i$9oo$1@reader1.panix.com> <1187368432.007049.131010@57g2000hsv.googlegroups.com>`

```
In article <1187368432.007049.131010@57g2000hsv.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 17 Aug, 13:09, docdw...@panix.com () wrote:

[snip]

>> Amazing what damage some folks have done to the King's English, eh?
>
>Aye, but then tis your fault for letting them abuse the language, yer
>majesty. <touches forelock>

Perhaps We have allowed certain barbaric customs, established in the days 
of Our Ancestors, to continue past the time when such customs are of good 
use, habit or benefit; We shall consider alternate recommendations, as 
befits Our station, and make Our decision known when We deem it 
appropriate.

Until such a making-known is done We will trust, as We have previously, in 
the good sense of Our subjects; to do otherwise might well seem 
ungenerous, a condition which is not suited to Our nature.

DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 25)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-18T03:35:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187433346.820841.76550@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<fa4ju2$lok$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187344380.421127.8560@a39g2000hsc.googlegroups.com> <fa436i$9oo$1@reader1.panix.com> <1187368432.007049.131010@57g2000hsv.googlegroups.com> <fa4ju2$lok$1@reader1.panix.com>`

```
On 17 Aug, 17:55, docdw...@panix.com () wrote:
> In article <1187368432.007049.131...@57g2000hsv.googlegroups.com>,
>
…[20 more quoted lines elided]…
> DD

You could have said it quicker with:

WE are not amused.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 26)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-19T04:43:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa8hp6$psm$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187368432.007049.131010@57g2000hsv.googlegroups.com> <fa4ju2$lok$1@reader1.panix.com> <1187433346.820841.76550@d55g2000hsg.googlegroups.com>`

```
In article <1187433346.820841.76550@d55g2000hsg.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 17 Aug, 17:55, docdw...@panix.com () wrote:

[snip]

>> Until such a making-known is done We will trust, as We have previously, in
>> the good sense of Our subjects; to do otherwise might well seem
…[4 more quoted lines elided]…
>WE are not amused.

We are not presumptuous in Our nature; We would prefer to have a 
making-known at least commence before We find Ourselves musing, a- or be-.

DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 23)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-17T11:29:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lembc3lcf92s7uibk1etqha5ghm7k9hl92@4ax.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com> <bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com> <1187344380.421127.8560@a39g2000hsc.googlegroups.com> <fa436i$9oo$1@reader1.panix.com>`

```
On Fri, 17 Aug 2007 12:09:54 +0000 (UTC), docdwarf@panix.com () wrote:

>Let's see... 'nappies' are 'basic garments for infants consisting of a 
>folded cloth or other absorbent material drawn up between the legs and 
…[4 more quoted lines elided]…
>or pleasure' and not... some other item of clothing.

It's funny what becomes natural.   For instance, we don't think about
that baked item "cookie" as being a baby name.  

Biscuits on both sides of the pond are different.   But more than
language, culture makes a difference.   I was watching the mini-series
(on DVD) _The Singing Detective_, and saw how cruel they treated
people in the man's boyhood.   Beating is OK - but letting someone
miss tea is not.   Tea being a bit of something covered with a
sickening amount of jam.   I'm not sure that I wouldn't prefer the
beating.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 23)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-18T03:34:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187433265.930630.85450@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<fa436i$9oo$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187281620.024182.304160@50g2000hsm.googlegroups.com> <bJednd0t6MXfiFjbnZ2dnUVZ_oCvnZ2d@comcast.com> <1187344380.421127.8560@a39g2000hsc.googlegroups.com> <fa436i$9oo$1@reader1.panix.com>`

```
On 17 Aug, 13:09, docdw...@panix.com () wrote:
> In article <1187344380.421127.8...@a39g2000hsc.googlegroups.com>,
>
…[9 more quoted lines elided]…
> 'sleeping briefly (especially during the day)'.

No, that is cat-napping. Something that Pete's cat Schroedinger
probably does or did.

>
> 'Walkies' are 'acts or instances of going on foot especially for exercise
…[4 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-19T04:45:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa8hu5$8or$1@reader1.panix.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <1187344380.421127.8560@a39g2000hsc.googlegroups.com> <fa436i$9oo$1@reader1.panix.com> <1187433265.930630.85450@g4g2000hsf.googlegroups.com>`

```
In article <1187433265.930630.85450@g4g2000hsf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 17 Aug, 13:09, docdw...@panix.com () wrote:
>> In article <1187344380.421127.8...@a39g2000hsc.googlegroups.com>,
…[12 more quoted lines elided]…
>No, that is cat-napping.

Really?  That appears to lead to absurdity; were one to abscond with a 
feline which was indulging in a period of sleeping briefly (especially 
during the day) then one might be catnapping a cat, napping.

DD
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-16T22:36:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tuudneIIV4pSuFjbnZ2dnUVZ_jednZ2d@comcast.com>`
- **In-Reply-To:** `<5ij7voF3pimneU1@mid.individual.net>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com...
…[5 more quoted lines elided]…
> right... ;-))

Right - but, generally, you're going to change the classes of what 
you're generating.  Instead of

<tr>
     <td>Status</td>
     <td style="font-weight:bold;color:white;background-color:red;">SOLD 
OUT</td>
</tr>

you'd do something like

<tr>
     <td>Status</td>
     <td class="soldout">SOLD OUT</td>
</tr>

Then, for each stylesheet (theme), you'd define "soldout" to appear 
however you wanted.  I wouldn't want to shovel all that inline style 
stuff around.  :)

>> What are you using to make the client side dynamic?  AJAX?  Or does it 
>> post-back for things that would normally be done in JavaScript?
…[7 more quoted lines elided]…
> But you can do it in other ways as well.)

Well, AJAX stands for Asynchronous JavaScript And XML, so I think it's 
pretty much JavaScript.  :)

> I coded my first web site entirely in Notepad using frames and all kinds of 
> stuff that is now 'deprecated'.  VS 2005 is better. And Dreamweaver Studio 8 
> is great for keeping it honest.

Frames were so cool...  back in the day, anyway...

>> No - bringing your site within standards isn't useless.  :)  Think of it 
>> as future-proofing.  Lots of sites that worked great with IE 6 simply 
…[12 more quoted lines elided]…
> accept cookies and I do allow ActiveX. But I'm not stupid about it... :-)

I really haven't used IE 7 enough to know how it handles ActiveX.  (I 
can't on this laptop now - there isn't IE for Ubuntu, and even then, I'm 
sure there wouldn't be a 64-bit version!)

> If a standard prevents me running Flash for example, then the Hell with the 
> standard. If  15 percent of people can't see my site because they won't run 
> a MS Browser on principle, then I see that as their loss.

For some, it's principle.  For others, it may be a restriction on their 
hardware (Apple) or operating system (Linux).  Yes, they chose to buy or 
run something other than Wintel, but "just opening IE" isn't even an option.

(I did notice while I was going through my logs yesterday that Safari, 
the Mac browser, seemed to come in a solid 3rd behind IE and Firefox.)

> (I don't hesitate 
> to open Firefox if I want a different perspective; it is just crazy to get 
…[5 more quoted lines elided]…
> some heinous crime.

On Howard's point, I see it.  Repeated annoyances can become 
frustrating, and when webmaster blow him off because "it works fine on 
IE", I can understand anger.  And, you really can't be surprised by 
Richard's take on it, can you?  You've stated your choices, and his 
views on MicroSoft are widely known.  :)  (I still think it's funny that 
two *guys* named a company a combination of "micro" and "soft"...  I 
think MacroHard would have been a better name.)

I also saw your comments on ActiveX as a security risk.  I think for a 
lot of us, it's "once bitten, twice shy" (except replace "once" with 
some much larger number).

> All I'm doing is building some web sites and having some fun. I tried to 
> explain honestly and unemotionally why certain Web Masters (self included) 
> can't drop everything because some effect doesn't render in a non-MS 
> Browser, and why the support has to go into IE, but I might as well have not 
> bothered. The only rational response was yours, Daniel. Thank you for that.

I didn't see as much irrationality in their posts as you did - but, it 
wasn't directed at me, either.

>> Sometimes Notepad can be your friend!  :)  heh...
> 
…[5 more quoted lines elided]…
> isn't realistic to be reading all the working papers coming out of W3C...

Heh - I don't have that kind of time either.  I just set my doctype, and 
look up what I don't know.  I also regularly validate the pages that I 
can (if they're not password-protected, for example) with their 
validation services.  Once it's valid, I see how it looks in IE.  If I 
tweak it, I'll revalidate.  I'll also remember what I had to do, so in 
theory, next time my code will be more portable.

You want an interesting experience?  Turn off images.  It's amazing the 
difference in the web when images are turned off.  :)  I had to do that 
while I was deployed last year.  That deployment also gave me a renewed 
hatred for ad sites - the US ad sites aren't very responsive from the 
other side of the globe.

> Besides, the development tools should keep track of it for me (they do up to 
> a point...)

heh - "should" and "to a point" - I think that's the level of compliance 
most browser have with the W3C's standards!  ;)

> The three days I spent was well spent and I have learned a good deal. The 
> process (and hopefully, the growth, goes on...)

cool...

> Pretty easy, you'd 
> think; just read ISAM and "write" RDB...And it would be, if not for OCCURS 
> and REDEFINES...:-)  Never mind, it is keeping me off the streets...:-)

heh - best of luck.  I've had a heck of a week.  I get pulled away from 
my desk doing all this extra stuff, then people want to know why I'm 
behind in my work from what I had scheduled.  Gee, I wonder...

>> I'd be happy to take a quick gander at some of the more problematic areas 
>> if you'd like.  :)  You know where to find me...
> 
> That's very kind, Daniel. Thanks, I appreciate it. At the moment, I have no 
> problems with the Web Site.

That's good.  The offer still stands, though, if something comes up in 
the future.  I actually enjoy that sort of thing.  :)
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-17T03:01:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187344894.350775.61570@w3g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<tuudneIIV4pSuFjbnZ2dnUVZ_jednZ2d@comcast.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <tuudneIIV4pSuFjbnZ2dnUVZ_jednZ2d@comcast.com>`

```
On 17 Aug, 05:36, LX-i <lxi0...@netscape.net> wrote:
> Pete Dashwood wrote:
>
…[18 more quoted lines elided]…
> stuff around.  :)

It can be fun  :-(

However, when you're down at the lowest level in a nested-nested-
nested-nested table having all that font stuff around just becomes
obstructive. What really beefs me is that if you correct (in DESIGN
mode) a spelling error in the paragraph text both Visual Studio and
Dreamweaver wrap </font>....<font> </font>....<font>   around your
correction, puffing up the size of the download. aNdd whu amung os
duesn@t macke spllng mishteaks?

>
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-18T08:23:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<noCdnd85iYF1nVrbnZ2dnUVZ_o7inZ2d@comcast.com>`
- **In-Reply-To:** `<1187344894.350775.61570@w3g2000hsg.googlegroups.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <tuudneIIV4pSuFjbnZ2dnUVZ_jednZ2d@comcast.com> <1187344894.350775.61570@w3g2000hsg.googlegroups.com>`

```
Alistair wrote:
> However, when you're down at the lowest level in a nested-nested-
> nested-nested table having all that font stuff around just becomes
…[4 more quoted lines elided]…
> duesn@t macke spllng mishteaks?

That's my biggest gripe with most generated HTML.  Sure, it works - but 
most of the time, it generates way, way, WAY more code than necessary. 
(Ever tried to save a Word document as HTML?)
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 22)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-19T06:28:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187530111.231627.110840@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<noCdnd85iYF1nVrbnZ2dnUVZ_o7inZ2d@comcast.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <UfCdnQBwRflDIl7bnZ2dnUVZ_o2vnZ2d@comcast.com> <5ij7voF3pimneU1@mid.individual.net> <tuudneIIV4pSuFjbnZ2dnUVZ_jednZ2d@comcast.com> <1187344894.350775.61570@w3g2000hsg.googlegroups.com> <noCdnd85iYF1nVrbnZ2dnUVZ_o7inZ2d@comcast.com>`

```
On 18 Aug, 15:23, LX-i <lxi0...@netscape.net> wrote:
> Alistair wrote:
> > However, when you're down at the lowest level in a nested-nested-
…[10 more quoted lines elided]…
>

Yes. Atrocious code.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 17)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-08-16T12:16:14-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net>`

```
On Thu, 16 Aug 2007 05:01:42 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[67 more quoted lines elided]…
>is aligned correctly and is visible, that's all I can guarantee...)

Here the job would have been made simpler if your development tool had
the option to force compliance with the appropriate level of the W3
standards.  I also agree with others who replied that your web-site
should not depend on ActiveX because of the integrity holes it opens
for the viewer and because Microsoft in their infinite LACK OF wisdom
refuse to have an option where I can enable it by web-site on first
visit either for the session or always.  It is a ROYAL pain running
Windows Update for this reason.  I also would count any web-site (like
Micro-focus at least used to be) that requires FLASH to even try to
use the site.  While flash is useful for some things, most things on a
site should be available (like manuals) without any need for FLASH.
Unrequested pop-ups also are a royal pain.  I am happy with my
subscription to the online Wall Street Journal but find their pop-ups
very aggravating.  
>
>> They keep track, and people who
…[28 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 18)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-16T09:29:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187281747.388722.205560@57g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com>`

```
On 16 Aug, 16:16, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Thu, 16 Aug 2007 05:01:42 +1200, "Pete Dashwood"
>
…[90 more quoted lines elided]…
>

I believe that you can switch Flash off. Or perhaps you are referring
to Splash screens which don't display anything when Flash is switched
off?
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T04:50:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ijdpuF3q0evmU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com>`

```


"Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
news:83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com...
> On Thu, 16 Aug 2007 05:01:42 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[88 more quoted lines elided]…
> standards.

Yes, I agree. It's actually worse than that, because Dreamweaver can monitor 
the standard and tell you where you've used non-standard tags, but it still 
is non-compliant even after you've checked it. It seems there is a fair bit 
of latitude in interpreting the standards.

>I also agree with others who replied that your web-site
> should not depend on ActiveX because of the integrity holes it opens
> for the viewer and because Microsoft in their infinite LACK OF wisdom
> refuse to have an option where I can enable it by web-site on first
> visit either for the session or always.

My web site neither depends on nor uses ActiveX that would be downloaded to 
a Client (I certainly use COM and ActiveX on the server). I'm pretty bored 
with hearing about the "holes" it opens up. Been hearing this same old song 
for years now, usually from people who don't know what COM even stands for, 
have never written a COM component, ignore the fact that there have been 3 
releases of COM+, each one steadily improving the product, plus a multitude 
of security patches, but heard or read somewhere that it is a security 
breach. Well, I've been implementing COM+ and DTS systems with RPCs on 
networks (public and private) for nearly 10 years now and have never had a 
machine infected because it had COM or ActiveX components on it. (I've had 
them subjected to other attacks, none of which proved serious.) When I look 
at COM, all I see is good. It lets me refactor OO COBOL code into new 
environments and has saved me large amounts of time and money in the move 
from COBOL to C#. HTML is more dangerous in my opinion, and you don't hear 
people going on about that...

> It is a ROYAL pain running
> Windows Update for this reason.  I also would count any web-site (like
> Micro-focus at least used to be) that requires FLASH to even try to
> use the site.

I don't like sites where they make me download documents in .PDF, with the 
concomitant nagging from bloody Adobe and insistence I upgrade and get a 
toolbar I neither need nor want. But I still go and get documents. Flash is 
very nice for some effects, but I woudn't make a site depend on it.



>While flash is useful for some things, most things on a
> site should be available (like manuals) without any need for FLASH.
> Unrequested pop-ups also are a royal pain.  I am happy with my
> subscription to the online Wall Street Journal but find their pop-ups
> very aggravating.

Turn them off.

I never put pop-ups on web sites and agree wholeheartedly. They spoil the 
experience rather than enhancing it, and most Browsers suppress them anyway.

>>
>>> They keep track, and people who
…[30 more quoted lines elided]…
>>So now I'm only guaranteeing support for IE...

That doesn't mean I won't try and get Cross Browser compliance, or that I 
would never change site code because of different Browsers. It just means I 
develop with IE, use MS oriented tools (for the most part) and so, will only 
guarantee the site when viewed in an MS Browser.

I would've thought that people would appreciate that position even if they 
don't agree with it.

Never mind. Web stuff is off topic here anyway...:-)

Pete.

>>
>>And that was where we came in... :-)
>>
>>Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-16T12:28:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vi59c3dvt24dlaugmod5uleqn639g6a7jj@4ax.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net>`

```
On Fri, 17 Aug 2007 04:50:11 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>My web site neither depends on nor uses ActiveX that would be downloaded to 
>a Client (I certainly use COM and ActiveX on the server). I'm pretty bored 
…[5 more quoted lines elided]…
>breach. 

It really doesn't matter if prospective customers avoid Active-X for
reasons that are invalid.    If you want those customers, you let them
work with the browser of their choice, on the computer of their
choice.

>That doesn't mean I won't try and get Cross Browser compliance, or that I 
>would never change site code because of different Browsers. It just means I 
…[4 more quoted lines elided]…
>don't agree with it.

And you should accept that positions like that get responses from
people who don't agree - this isn't the first argument about style on
this forum.

>Never mind. Web stuff is off topic here anyway...:-)

The concept of whether we should program to satisfy our customers is
always on-topic.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T18:27:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iktf8F3pd5a4U1@mid.individual.net>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <vi59c3dvt24dlaugmod5uleqn639g6a7jj@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:vi59c3dvt24dlaugmod5uleqn639g6a7jj@4ax.com...
> On Fri, 17 Aug 2007 04:50:11 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[36 more quoted lines elided]…
> always on-topic.

Read that last sentence again and engage your "pompous bullshit" filter :-)

 None of my customers has suffered due to the policies I adopt. (They 
certainly would if I adopted the policies you are suggesting.)

I see my customers as associates. Just like people who come to my house; 
you're welcome, but you take me as you find me. Don't grizzle because I 
haven't got a special room where you can face East and do the chicken dance. 
Amazingly, most of my visitors have no such requirement, and are perfectly 
happy to share a JD in the lounge. :-)

(Last post on this stupidity...)

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-17T10:07:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2khbc3ppcqtgkcvqp8l6c9uor1velk2t98@4ax.com>`
- **References:** `<p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <vi59c3dvt24dlaugmod5uleqn639g6a7jj@4ax.com> <5iktf8F3pd5a4U1@mid.individual.net>`

```
On Fri, 17 Aug 2007 18:27:52 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> The concept of whether we should program to satisfy our customers is
>> always on-topic.
>
>Read that last sentence again and engage your "pompous bullshit" filter :-)

I know my communication skills are lacking.   My big issue is
consideration for others.

> None of my customers has suffered due to the policies I adopt. (They 
>certainly would if I adopted the policies you are suggesting.)

Because you automatically exclude people from being your customers.

>I see my customers as associates. Just like people who come to my house; 
>you're welcome, but you take me as you find me. Don't grizzle because I 
>haven't got a special room where you can face East and do the chicken dance. 
>Amazingly, most of my visitors have no such requirement, and are perfectly 
>happy to share a JD in the lounge. :-)

So if you live up a flight of stairs, you may welcome wheelchair bound
friends to your house - but don't be surprised about their response.

>(Last post on this stupidity...)

OK.    I don't think the proper word is "stupidity" though.  

(This is an issue which I have strong feelings about)
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-17T16:25:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13cc4gt86q5ei67@news.supernews.com>`
- **References:** `<oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <vi59c3dvt24dlaugmod5uleqn639g6a7jj@4ax.com>`

```
Howard Brazee wrote:
>
> It really doesn't matter if prospective customers avoid Active-X for
…[3 more quoted lines elided]…
>

I follow the programming rule: "Since I can't please everybody, I decided to 
please me."
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-08-16T15:58:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kU2xi.5526$7e6.539@bignews4.bellsouth.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>
> ... I'm pretty bored with hearing about the "holes" it opens up. ...

> ... plus a multitude of security patches, ...

Security patches for something without security holes to patch?  ;-)
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 19)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-08-16T15:38:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187303899.451981.309060@q3g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5ijdpuF3q0evmU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net>`

```
On Aug 17, 4:50 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> >>Now, if someone was paying me to develop this site I simply couldn't spend
> >>that amount of time on the "Cross Browser" problem.. Server stats showed
> >>that for the brief time I let people access it, 93% were using IE.

In a hypothetical city one company ran all the car parking buildings.
All the cars that were not Ford's were being defaced: tires let down,
grease smeared on the windscreens, mud on the headlights, etc. When
complaints were made the company said that "95% of the cars parking in
the buildings were Fords, so they didn't care about the tiny numbers
of other cars that existed. If you want to have a great parking
experience then go buy a Ford. Later the Fords that were not XP or
Vista models were getting defaced."

> >I also agree with others who replied that your web-site
> > should not depend on ActiveX because of the integrity holes it opens
…[5 more quoted lines elided]…
> a Client (I certainly use COM and ActiveX on the server).

When people talk about a web site 'using' ActiveX they understand this
to mean client side ActiveX loaded into the client. They neither know
nor care what happens on the server.

> I'm pretty bored
> with hearing about the "holes" it opens up. Been hearing this same old song
…[4 more quoted lines elided]…
> breach. Well, I've been implementing COM+ and DTS systems with RPCs ...

You are talking at cross purposes. Client ActiveX does have "holes"
and is unfixable.

> HTML is more dangerous in my opinion, and you don't hear
> people going on about that...

Then you have a very strange opinion. It may be that IE can be broken
in some ways, for example some 16bit characters in a URL will cause
the rest of the URL to be hidden, but this is a Windows failure not
HTML.


> I don't like sites where they make me download documents in .PDF, with the
> concomitant nagging from bloody Adobe and insistence I upgrade and get a
> toolbar I neither need nor want. But I still go and get documents.

You don't have to put up with that. You can make the web behave the
way that _you_ want to just as I make it the way that _I_ want. In
particular you can have an add-on the Firefox such as 'PDF Download'
and have it displayed as HTML or downlaod, or load it into another
reader such as xpdf (even on Windows) or kpdf (KDE runs on Windows).

> I never put pop-ups on web sites and agree wholeheartedly. They spoil the
> experience rather than enhancing it, and most Browsers suppress them anyway.

IE7 has caught up in some respects. yes.

> That doesn't mean I won't try and get Cross Browser compliance, or that I
> would never change site code because of different Browsers. It just means I
…[4 more quoted lines elided]…
> don't agree with it.

I can appreciate that position as long as the exclusion is not from
ignorance, which it obviously isn't.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-17T18:33:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iktq7F3phqhiU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <1187303899.451981.309060@q3g2000prf.googlegroups.com>`

```


"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1187303899.451981.309060@q3g2000prf.googlegroups.com...
> On Aug 17, 4:50 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[84 more quoted lines elided]…
>
Thank you Richard. I know you don't like MS so I thought your post was 
"restrained" :-)

There is far too much heat in this subject and I have all the heat I can 
handle at the moment so no more on this...

Thanks for a balanced response.

Pete.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-17T02:48:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187344122.640791.131770@r34g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<1187303899.451981.309060@q3g2000prf.googlegroups.com>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <1187303899.451981.309060@q3g2000prf.googlegroups.com>`

```
On 16 Aug, 23:38, Richard <rip...@Azonic.co.nz> wrote:
> On Aug 17, 4:50 am, "Pete Dashwood"
>
…[8 more quoted lines elided]…
>

Browsers do have certain in-built restrictions which prevent HTML (and
Javascript) from doing some dodgy acts. But it doesn't stop people
from putting Javascript code in to web pages which are potentially
dangerous.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-18T13:56:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5in1u2F3r4vlkU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <1187303899.451981.309060@q3g2000prf.googlegroups.com> <1187344122.640791.131770@r34g2000hsd.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1187344122.640791.131770@r34g2000hsd.googlegroups.com...
> On 16 Aug, 23:38, Richard <rip...@Azonic.co.nz> wrote:
>> On Aug 17, 4:50 am, "Pete Dashwood"
…[16 more quoted lines elided]…
>
Just for the record, and not that it matters, I was thinking more about HTML 
mail when I made that satement. Neverteless, I use HTML mail, find it very 
useful for keeping track of responses and posting links to people, and 
filter and virus/script check all mail before allowing it onto my system.

Pete
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 22)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-08-21T13:31:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187728286.002059.256550@q3g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5in1u2F3r4vlkU1@mid.individual.net>`
- **References:** `<9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <1187303899.451981.309060@q3g2000prf.googlegroups.com> <1187344122.640791.131770@r34g2000hsd.googlegroups.com> <5in1u2F3r4vlkU1@mid.individual.net>`

```
On Aug 18, 1:56 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[17 more quoted lines elided]…
> > dangerous.

Javascript is not HTML, granted it is another language supported by
browsers.

> Just for the record, and not that it matters, I was thinking more about HTML
> mail when I made that satement. Neverteless, I use HTML mail, find it very
> useful for keeping track of responses and posting links to people, and
> filter and virus/script check all mail before allowing it onto my system.

There is nothing wrong with HTML, there is nothing wrong with email
using HTML, what is wrong is what Microsoft Outlook does with HTML
mail.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 20)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-17T10:10:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<21ibc3dganiflon2qf0knuejdeifdofe8r@4ax.com>`
- **References:** `<46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com> <5igrj7F3p3p7nU1@mid.individual.net> <83q8c3l9p90900l4oe9lcjhuabmoa4o0ll@4ax.com> <5ijdpuF3q0evmU1@mid.individual.net> <1187303899.451981.309060@q3g2000prf.googlegroups.com>`

```
On Thu, 16 Aug 2007 15:38:19 -0700, Richard <riplin@Azonic.co.nz>
wrote:

>I can appreciate that position as long as the exclusion is not from
>ignorance, which it obviously isn't.

I'm the opposite.   When someone accidentally is exclusionary, I can
understand.   When someone chooses to be exclusionary, I take that as
an insult.

The end result is the same though.
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 16)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-15T20:50:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YpGdnTHg9Zj7Jl7bnZ2dnUVZ_uOmnZ2d@comcast.com>`
- **In-Reply-To:** `<1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com>`
- **References:** `<9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com> <v9f3c3pksoedvbjlg8st6ve52o6b7o1bov@4ax.com> <5idvmbF3p9c2pU1@mid.individual.net> <kgi3c3hhkvnto090oq9tsa97509uunq5g2@4ax.com> <5iet5aF3fmvltU1@mid.individual.net> <1k26c3lntms024jrmj85omqui0ii5a1n91@4ax.com>`

```
Howard Brazee wrote:
> 
> For instance, the way most common response to bugs found is that they
…[3 more quoted lines elided]…
> work.

This made me curious.  Below, F = Firefox, IE = IE, NC = "Netscape 
(compatible)" (not quite sure what agent that is), M = Mozilla, K = 
Konqueror, and O = Opera.

For my root domain (which includes my Linux blog and other Linux 
resources)...

F  - 40.8%
IE - 19.8%
NC - 11.3%
M  -  3.2%
K  -  3.1%
O  -  1.7%

OK - that makes sense.  Now how about some of my subdomains?  My 
personal blog...

NC - 31.9%
F  - 31.2%
IE - 18.3%
M  -  2.1%
K  -  0.1%
O  - not in top 20

Emerald Mountain Christian School...

IE - 71.3%
F  -  9.7%
NC -  6.2%
K  -  0.7%
M  -  0.3%
O  -  0.2%

Photography by Michelle...

IE - 56.3%
F  - 41.8%
NC -  1.1%
M, O - less than .1%
K - none

I really don't see the need to support IE exclusively.  :)
```

###### ↳ ↳ ↳ Re: field validation (was Re: COBOL/DB2 Date edit question)

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-14T20:14:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KJGdnRIbYpLk_F_bnZ2dnUVZ_oqhnZ2d@comcast.com>`
- **In-Reply-To:** `<p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <9NydnexmCdlzDSLbnZ2dnUVZ_rGrnZ2d@comcast.com> <5i9mipF3nvs03U1@mid.individual.net> <oMednRMwtNq6VCLbnZ2dnUVZ_qmlnZ2d@comcast.com> <46C03FC9.6F0F.0085.0@efirstbank.com> <p1d3c3dn76d112rurl48apfij7pumrj6d5@4ax.com>`

```
Binyamin Dissen wrote:
> 
> February 30th fails on syntax,

Interestingly enough, February 30th actually passes in JavaScript!  (At 
least in IE 6...)

if (isNaN(parseInt(Date.parse("2007-02-30")))) {
     alert("Invalid Date!");
}
else {
     alert("You may proceed...");
}

"Date.parse" creates a date from a string, "parseInt" creates an integer 
from its argument, and "isNaN" means "is Not a Number".  This is how I 
used to validate dates, but once I figured out it let this through, I 
had to write a different routine.  (Never underestimate the 
bone-headedness of the user.)
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-13T12:17:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5i9m8uF3lvl7qU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com>`

```


"Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
news:jgvub35e1pahgvi467v85db20119s42cub@4ax.com...
>I hear what you say Michael. Might I scenario something (and if you
> get bored with the subject I will understand) ..
…[16 more quoted lines elided]…
>

You are suffering from the same problem many have encountered when moving to 
RDB; incompatibilities between language data types and RDB data types. For 
the most part, embedded SQL in COBOL does some very good data conversions 
uder the covers and ensures that the data presented from the DB to the 
program is in a format that the program can use, and vice versa.

However, more and more installations are moving away from embedded SQL for a 
number of reasons:

1. It is still tied back into procedural programming.
2. It is not as powerful as some of the emerging methods for data 
manipulation which can utilise multiprocessors and deferred execution. 
(Query Expressions, Lambda functions, etc.)

Obviously, most places are not going to move overnight into new database 
technology. (And it requires using a language that supports the new 
functions; COBOL doesn't.)

The modern trend is to place the editing and validation into stored 
procedures that are triggered automatically when the data is updated.

This makes sense insofar as the validations are stored with the data, and 
are independent of the language being used. It doesn't matter if you move to 
Basic, or C++ or C# or whatever, your data still gets validated by the RDBMS 
back end. (It is also easier to progress from this into the new technology, 
should you decide to, now or later.)

You were close to this solution when you decided to validate the date using 
an RDB DATE function. All of the solutions you have outlined are workable, 
it is just a question of what you prefer. Michael thinks it is "obtuse"; I 
disagree. I think it is perfectly sensible. (However, I understand Michael's 
objection. To a programmer, using program code to do things is the solution. 
Michael is a very experienced and excellent programmer, so to him this looks 
like a "sledgehammer to crack a nut'')

In fact, there is nothing wrong with using RDB functions to validate data 
that is being stored on a RDB, the only difference is WHERE you use the 
function. If you use it from COBOL with embedded SQL, then there is a good 
argument to be made for simply using program code instead. If, on the other 
hand, you stored a procedure to do it, and triggered that procedure whenever 
the date was updated, you have removed the whole business from your program. 
You get a return saying it worked or it didn't and you can do whatever you 
want from there.  You can also retrieve it, secure in the knowledge that it 
is "valid" in the wider sense of not just format validation..

An important point to note here is that this "back end" validation can go 
way beyond what you could easily do in program code. You can check the new 
date against other, previously validated dates now stored on the database, 
without having to retrieve them into a program. You have all of the 
extensive SQL DATE manipulation functions immediately available, with no 
program call overheads. For example, you can check whether the new date, 
plus a number of days is greater, less, or equal to an existing date, which 
is, in turn, so many days away from another date which it must exceed, and 
so on. And that is all before you even start to include data which is NOT a 
date in the validation.

Stored procedures are becoming a way of life on many sites, and embedded SQL 
is showing a consequent decline.

> But being out of the workforce for a few years now, on my laptop with
> older IBM Cobol, CICS, DB2 and  btrieve VSAM software, developing a
> software package (I am one of these BT/I's), am looking for help as to
> how modern installations might handle DATE, TIME, TIMESTAMP edits.

My comments above apply to all of these.

> You've already given me clues. Other insights?
> Anyway, thanks to date.
…[16 more quoted lines elided]…
>>entered upon the screen?

No, it isn't. It is just different from how we have done it traditionally. 
There is little difference between calling a data validation routine in 
program code and simply calling SQL to place the date on the RDB 
immediately. Both incur call overheads. But there is a case to be made for 
storing validations with data and getting it out of program code (see 
above).

In the old days, before RDBMS, we had no option other than to validate in 
program code. Now we do :-)

>>
>>Not that it can't be made to work, but generally you'd have some kind of
>>library routine around to handle that.

Maybe you might consider a stored procedure to be a "library routine"? It 
serves many of the same functions and can be shared amongst multiple fields.
>>
>>Besides, at some point it's possible (probable?) you are going to have to
>>reformat it anyway to do the UPDATE

Nope. Most RDBMS will accept anything that looks like a date. (It is one of 
the beautiful things about OO programming, called "overloading".)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-12T23:16:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13bvjgvie7psk69@corp.supernews.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <5i9m8uF3lvl7qU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5i9m8uF3lvl7qU1@mid.individual.net...
[snip]
> Nope. Most RDBMS will accept anything that looks like a date. (It is one
of
> the beautiful things about OO programming, called "overloading".)

Mr Dashwood, with all due respect, I think you are
letting your OO fanaticism get the better of you. <g>
In OO, "overloading" refers to a method accepting
different types; not different values. More likely is
that RDBMSs use some form of what might be called
format matching. For example, DB2 (9.1) apparently
has six formats: DEF, EUR, ISO, JIS, LOC, and USA.
For Microsoft Access 97 date literals, "Valid formats
include the date format specified by the locale settings
for your code or the universal date format." (However,
dates in SQL must be in US format.) This suggests
that formats; not "overloading", have been used for
some time and by different vendors.
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-13T22:42:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iaqt1F3nao79U1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <5i9m8uF3lvl7qU1@mid.individual.net> <13bvjgvie7psk69@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13bvjgvie7psk69@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[19 more quoted lines elided]…
>
OK, I stand corrected.

All I know is I can throw anything that looks like a date at a RDB and it 
works.

But you are right, the type is a DATE so it isn't overloaded.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-13T11:52:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C045ED.6F0F.0085.0@efirstbank.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <5i9m8uF3lvl7qU1@mid.individual.net>`

```
>>> On 8/12/2007 at 6:17 PM, in message
<5i9m8uF3lvl7qU1@mid.individual.net>,
Pete Dashwood<dashwood@removethis.enternet.co.nz> wrote:
> 
> "Graham Hobbs" <ghobbs@cdpwise.net> wrote in message 
…[19 more quoted lines elided]…
>>
 
> You are suffering from the same problem many have encountered when 
> moving to 
…[5 more quoted lines elided]…
> program is in a format that the program can use, and vice versa.

Looks like I started my previous thread too soon!  :-)
 
> However, more and more installations are moving away from embedded SQL 
> for a 
…[77 more quoted lines elided]…
> is showing a consequent decline.

I still have the issue I mentioned in my other message.  Personally, I am
not so much concerned as to *where* the business logic / validations exist. 
If it's in a stored procedure, that's fine (as long as I have access to look
at it!).  My concern is that this appears (from my, granted, limited point
of view) to require a lot of 'back and forth' between the user, the
application, and the database.  Is this not the case?

One piece of logic that we have in many of our user update type programs is
the "Do you really mean this" type screen.  Here's how it works...

The user enters various fields on various screens.  Secondary screens may or
may not be present depending on data entered on previous screens.  At the
end of all of the input the user is presented with a screen detailing all of
the input he has entered, with a button to "Submit" or "Cancel".  When he
submits then the data is actually sent to the database (or to the
mainframe!).

Within all of this a lot of validation has been going on.  Dates have been
checked, fields have been validated to make sure they are allowed in
combination with other fields, etc.  The final "Submit/Cancel" page will not
even be presented to the user until such time as all of the input has been
validated as being allowed.

Can this still be done with stored procedures and what have you?  I'm not
trying to be argumentative.  I simply see problems and I don't know the
solutions.

Thanks!

Frank
```

###### ↳ ↳ ↳ Re: COBOL/DB2 Date edit question

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-14T20:01:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5id5rkF3o6u19U1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <9EEvi.1690$3x.873@newssvr25.news.prodigy.net> <jgvub35e1pahgvi467v85db20119s42cub@4ax.com> <5i9m8uF3lvl7qU1@mid.individual.net> <46C045ED.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:46C045ED.6F0F.0085.0@efirstbank.com...
>>>> On 8/12/2007 at 6:17 PM, in message
> <5i9m8uF3lvl7qU1@mid.individual.net>,
> Pete Dashwood<dashwood@removethis.enternet.co.nz> wrote:
>>
<snipped conceptual level explanation>.
>>
>> Stored procedures are becoming a way of life on many sites, and embedded
…[10 more quoted lines elided]…
> application, and the database.  Is this not the case?

Yes and no.

There is switching between the entities you mention, but if it doesn't incur 
heavy overheads, why would you care?

The concepts are as oulined in my previous mail; You can have the validation 
processes stored with the actual data and removed from the presentation 
layer (user interface) entirely. Some people will like this idea, others 
won't. (I do :-))

For me, it isn't just the logical tidiness, it is a step towards the future. 
(I think this may be influencing several of the places I know where they are 
moving to this model, too.)  Banging away at databases with primitive SQL is 
not in the same league as running query expressions. This technology hasn't 
made it's way onto mainframes yet (as far as I know... if anyone is using 
Query Expressions or Lambda functions for DB access on a mainframe, please 
post here...), but I am picking it will within the next few years. It is 
probably fair to say that multiple processors are in the future for most 
commercial sites and this, combined with new storage technologies that are 
just around the corner, is going to require different and more powerful 
techniques of data manipulation if we are to reap the benefits of parallel 
processing and improved storage hardware.

After the first RDBMS call, the overheads in subsequent calls are virtually 
nonexistent. Not only that, but the DB subsystem is self monitoring and self 
optimizing.  (Program logic usually is not.) The system will optimize itself 
to the most frequent access paths.
( this is an area where expert software is getting smarter and less fallible 
than people...)

>
> One piece of logic that we have in many of our user update type programs 
…[19 more quoted lines elided]…
> Can this still be done with stored procedures and what have you?

Definitely, and probably even more efficiently than currently. As fields are 
entered they can be passed to the RDBMS, which triggers a validation. If the 
field passes, it is already stored and doesn't need to be, later. (it is 
still available to the program code, but now it is known to be valid). Cross 
field validations can be done in the same way. Collect the fields required 
and submit them together to an UPDATE that triggers the cross validation. 
If it fails, the user is requested to correct the data. No SUBMIT has been 
issued so the updates are not applied, and, anyway, triggers can operate 
immediately BEFORE or AFTER the function they are triggered by. (You always 
have the option to ROLLBACK if you wanted to approach this differently...)

As you can see, validations can be quite complex and there are facilities to 
support anything you need to do.

Everything you describe in the penultimate paragraph above can be easily 
accomplished with stored procedures and triggers. It moves this validation 
out of program code, and, at least in my opinion, that is a "consummation 
devoutly to be wished" (Sorry, MacBeth...) . Should you remove any existing 
fields from the DB, no program changes are required, and if/when new RDBMS 
technology is implemented, conversion to it is likely to be automatic.

However, you DO need to learn full SQL and write the procedures and 
triggers.

It's just another language ... :-)

(While you're at it, why not learn Query Expression syntax; (it looks like 
SQL, but is immensely more powerful)?)



> I'm not
> trying to be argumentative.

A refreshing change for CLC...:-)

>I simply see problems and I don't know the
> solutions.

Well, this is a good place to gather thoughts and ideas, if not 
solutions...:-)

Pete.
```

###### ↳ ↳ ↳ VisualAge COBOL (was: COBOL/DB2 Date edit question

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-13T05:20:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ySRvi.426019$LL7.61210@fe08.news.easynews.com>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5i8ehiF3lkrtaU1@mid.individual.net...
>
<snip>
>
> You might not be able to support the ! in the name in Visual Age COBOL (which 
> is actually MicroSoft rebadged)
>

IBM's VisualAge COBOL has *nothing* to do with any Microsoft *or* Micro Focus 
product products.  IBM's original "IBM COBOL/2" product was a rebadged (slightly 
modified) version of Micro Focus' COBOL/2 product (as was Microsoft's COBOL V4 - 
as I recall its name).  However, all the VisualAge (and later) IBM products are 
ports (sort-of) of IBM's mainframe compilers.  (The original PC and AIX 
front-ends were identical to the then-current IBM mainframe compiler -- with a 
separate back-end.  Since then there have been some divergencies.)
```

###### ↳ ↳ ↳ Re: VisualAge COBOL (was: COBOL/DB2 Date edit question

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-13T22:52:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iarg8F3odm61U1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <ySRvi.426019$LL7.61210@fe08.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:ySRvi.426019$LL7.61210@fe08.news.easynews.com...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:5i8ehiF3lkrtaU1@mid.individual.net...
…[19 more quoted lines elided]…
>

OK, I said MicroSoft and I meant MicroFocus.  I worked on introducing 
MicroFocus into the IBM software house at North Harbour (Southampton, UK) in 
the early 90s. Visual Age was released shortly after that and it was a port, 
not of a mainframe compiler, but simply rebadged MicroFocus in its initial 
release. (It even had the same compiler options). Later they may well have 
done something else with it, but at the time it smacked of MicroFocus. (and 
was a good product...).

I know you are usually right on these things, Bill, but in this case my 
memory tells it differently. However, I don't see it as important enough to 
argue about and will withdraw my comment if it offends you. (And it was 
definitely wrong,as written, anyway... :-))

Pete.
```

###### ↳ ↳ ↳ Re: VisualAge COBOL (was: COBOL/DB2 Date edit question

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-14T12:26:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5icb5jF3mb65gU1@mid.individual.net>`
- **References:** `<pltrb3hf2o0ujn52tqnd8tk5nsn5ars8uj@4ax.com> <5i76i7F3mgdc6U1@mid.individual.net> <506tb3pa4ka91dltlacjif853pqn9lefga@4ax.com> <5i8ehiF3lkrtaU1@mid.individual.net> <ySRvi.426019$LL7.61210@fe08.news.easynews.com> <5iarg8F3odm61U1@mid.individual.net>`

```
Hey Bill,

I just re-read this and note that I stated "Southampton". It was, of course, 
Portsmouth.

I think I need a holiday :-) (Fortunately the orchids in my garden are 
starting to bloom and I have just picked the first stem. Gorgeous. Deep 
orange tinged with red and yellow; it means that Summer is just around the 
corner and I can get out of the house and back to the beach... there's 
something relaxing about crashing surf :-))

Pete.
```

###### ↳ ↳ ↳ Re: VisualAge COBOL (was: COBOL/DB2 Date edit question

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-08-14T19:15:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187144105.403579.251910@x35g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5iarg8F3odm61U1@mid.individual.net>`
- **References:** `<5iarg8F3odm61U1@mid.individual.net>`

```
On Aug 13, 10:52 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
>
> OK, I said MicroSoft and I meant MicroFocus.  I worked on introducing
…[10 more quoted lines elided]…
> definitely wrong,as written, anyway... :-))

In the 90s I received stuff from IBM Developer Connection, I still
have piles of CDs here. In set 10 disk 4 there is Visualage Cobol
version 1.00. I had this installed for a while just to test it and see
what code changes I needed. It is definitely not a version of
MicroFocus.

In fact I just now put the disk into a drive and looked at the docs to
refresh _my_ memory.

There certainly were IBM rebadged versions of Microfocus, inluding IBM
Cobol/2, but Visualage version 1.00 (or later) is not one of them.
```

###### ↳ ↳ ↳ Re: VisualAge COBOL (was: COBOL/DB2 Date edit question

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-16T05:31:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5igrj9F3p3p7nU2@mid.individual.net>`
- **References:** `<5iarg8F3odm61U1@mid.individual.net> <1187144105.403579.251910@x35g2000prf.googlegroups.com>`

```


"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1187144105.403579.251910@x35g2000prf.googlegroups.com...
> On Aug 13, 10:52 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[31 more quoted lines elided]…
>
OK, thanks. Guess I was confused.  It may have been Cobol/2 but I really 
thought it wasn't.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
