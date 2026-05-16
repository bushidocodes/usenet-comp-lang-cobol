[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SQL Commands

_11 messages · 5 participants · 2006-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### SQL Commands

- **From:** "Servizio Tecnico" <robertob68(nospam)@hotmail.com>
- **Date:** 2006-04-07T11:53:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it>`

```
Hi, I use Fujitsu v7 with Embedded SQL but when I write the command "DROP
TABLE" and "CREATE TABLE" return a error in compilation like this:
SQL STATEMENT IS INVALID - ODBC 7600E NOT EXECUTABLE SQL STATEMENT

Someone can helpme?

Thanks
Roberto
```

#### ↳ Re: SQL Commands

- **From:** "void * clvrmnky()" <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-04-07T12:19:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<siwZf.17427$43.324@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it>`

```
Servizio Tecnico wrote:
> Hi, I use Fujitsu v7 with Embedded SQL but when I write the command "DROP
> TABLE" and "CREATE TABLE" return a error in compilation like this:
> SQL STATEMENT IS INVALID - ODBC 7600E NOT EXECUTABLE SQL STATEMENT
> 
"CREATE TABLE" is not a valid SQL statement.  Are you creating a proper 
statement as defined by the SQL language?  You need a table name, at 
least.  Embedded SQL may have its own constraints and requirements for 
the CREATE keyword, as well.
```

##### ↳ ↳ Re: SQL Commands

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-04-07T18:48:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i09d325u0i2lu22p5ugatootgmugt9iupv@4ax.com>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <siwZf.17427$43.324@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```
On Fri, 07 Apr 2006 12:19:36 -0400, "void * clvrmnky()"
<clvrmnky.invalid@hotmail.com.invalid> wrote:

>Servizio Tecnico wrote:
>> Hi, I use Fujitsu v7 with Embedded SQL but when I write the command "DROP
…[6 more quoted lines elided]…
>the CREATE keyword, as well.
"Created table ... " IS a valid SQL statement.

Problem with ESQL from Fujitsu is that THEY have restricted the SQL
statements allowed.

Solutions, as previously stated within this group (and that would show
up if the OP have bothered to search the group postings), can pass
through the use of

1- Dynamic SQL
2- Use of ADO CODE (not the ADO control supplied by Fujitsu (DO NOT
USE IT!!)) (or eventually DAO/RDO)




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: SQL Commands

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-04-08T17:44:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49p0ugFpp6k0U1@individual.net>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <siwZf.17427$43.324@nnrp.ca.mci.com!nnrp1.uunet.ca> <i09d325u0i2lu22p5ugatootgmugt9iupv@4ax.com>`

```

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message 
news:i09d325u0i2lu22p5ugatootgmugt9iupv@4ax.com...
> On Fri, 07 Apr 2006 12:19:36 -0400, "void * clvrmnky()"
> <clvrmnky.invalid@hotmail.com.invalid> wrote:
…[23 more quoted lines elided]…
>
I have used the Fujitsu control without problem, but generally don't because 
I prefer to have total control. It works very well with PowerCOBOL.

I'm interested to know what problems you found with it, Frederico, that 
would make you want to shout this advice?

Dynamic SQL is not a good solution from the performance point of view, but 
it does, as you say, allow you to do things which Fujitsu do not support 
through ESQL.

Pete.
```

#### ↳ Re: SQL Commands

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-04-07T19:23:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d0bf0$44370268$45491d7a$6510@KNOLOGY.NET>`
- **In-Reply-To:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it>`

```
Servizio Tecnico wrote:
> Hi, I use Fujitsu v7 with Embedded SQL but when I write the command "DROP
> TABLE" and "CREATE TABLE" return a error in compilation like this:
> SQL STATEMENT IS INVALID - ODBC 7600E NOT EXECUTABLE SQL STATEMENT

Notice the word "executable" statement.  There are two types of SQL 
statements - CREATE and DROP are both considered Data Definition 
Language (DDL) statements.  My guess would be that FJ7 doesn't like DDL 
through ESQL.  You may be able to get around this by using dynamic SQL - 
check your manual for that term if you're not familiar with it.  :)
```

##### ↳ ↳ Re: SQL Commands

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-04-08T14:43:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YZPZf.501$Lm5.30@newssvr12.news.prodigy.com>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <d0bf0$44370268$45491d7a$6510@KNOLOGY.NET>`

```
"LX-i" <lxi0007@netscape.net> wrote in message
news:d0bf0$44370268$45491d7a$6510@KNOLOGY.NET...
> Servizio Tecnico wrote:
> > Hi, I use Fujitsu v7 with Embedded SQL but when I write the command
"DROP
> > TABLE" and "CREATE TABLE" return a error in compilation like this:
> > SQL STATEMENT IS INVALID - ODBC 7600E NOT EXECUTABLE SQL STATEMENT
…[5 more quoted lines elided]…
> check your manual for that term if you're not familiar with it.  :)

I've used CREATE *TEMPORARY* TABLE via ESQL... not with FJ but with IBM M/F
and some 'nix COBOL (MF?) I worked on.. maybe that's a solution ...

Then again, I still use CREATE TABLE thru the Windows ODBC API and that
works just fine.

Then again, maybe all this speculation is a waste of time until we see what
happens using a syntactically correct CREATE TABLE statement.... after all,
the ESQL compiler has to call the DBMS's PREPARE statement during
compilation, and that will surely fail if the statement is syntactically
incorrect.

MCM
```

###### ↳ ↳ ↳ Re: SQL Commands

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-04-08T16:26:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <d0bf0$44370268$45491d7a$6510@KNOLOGY.NET> <YZPZf.501$Lm5.30@newssvr12.news.prodigy.com>`

```
On Sat, 08 Apr 2006 14:43:04 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>"LX-i" <lxi0007@netscape.net> wrote in message
>news:d0bf0$44370268$45491d7a$6510@KNOLOGY.NET...
…[22 more quoted lines elided]…
>incorrect.
Sorry but no. As I stated previsously Fujitsu ESQL does NOT SUPPORT
some sql statements, and CREATE table is one of them, not matter how
correct the statement is.

So if using ESQL the only way is to use a dynamic statement. (with FJ
COBOL).




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: SQL Commands

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-04-08T15:35:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2LQZf.56505$F_3.27176@newssvr29.news.prodigy.net>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <d0bf0$44370268$45491d7a$6510@KNOLOGY.NET> <YZPZf.501$Lm5.30@newssvr12.news.prodigy.com> <jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com>`

```
"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com...
> On Sat, 08 Apr 2006 14:43:04 GMT, "Michael Mattias"
> <michael.mattias@gte.net> wrote:
…[12 more quoted lines elided]…
> >> through ESQL.  You may be able to get around this by using dynamic
SQL -
> >> check your manual for that term if you're not familiar with it.  :)
> >
> >Then again, maybe all this speculation is a waste of time until we see
what
> >happens using a syntactically correct CREATE TABLE statement.... after
all,
> >the ESQL compiler has to call the DBMS's PREPARE statement during
> >compilation, and that will surely fail if the statement is syntactically
> >incorrect.

> Sorry but no. As I stated previsously Fujitsu ESQL does NOT SUPPORT
> some sql statements, and CREATE table is one of them, not matter how
> correct the statement is.

I did see that, but I'm just stubborn enough to think that writing a
syntactically-correct CREATE TABLE statement is worth a try.

Since I call CREATE TABLE.... the same way I call SELECT... or INSERT... and
it's ho-hum in my programs, I figger it has to be worth a shot if I can't
find an explicit prohibition in the compiler vendor's manual. (Which of
course, may be saying more about the quality of the documentation than about
anything else).

MCM
```

###### ↳ ↳ ↳ Re: SQL Commands

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-04-09T13:57:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49r7vrFpgg5dU1@individual.net>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <d0bf0$44370268$45491d7a$6510@KNOLOGY.NET> <YZPZf.501$Lm5.30@newssvr12.news.prodigy.com> <jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com>`

```

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message 
news:jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com...
> On Sat, 08 Apr 2006 14:43:04 GMT, "Michael Mattias"
> <michael.mattias@gte.net> wrote:
…[35 more quoted lines elided]…
>
 I really HATE it when someone says "It's the ONLY way..." :-)

My experience (and it is extensive) is that when IT people say this, what 
they really mean, is: "It's the ONLY way I can think of or know of, and if 
there are other alternatives I can't be bothered exploring them..."

I have seen it many times throughout my career and  almost invariably, a 
little imagination or "thinking outside the square" provides a (usually 
better...) alternative.

I remember one famous case in Spain where I wanted to refresh multiple 3270 
screens when certain events occurred. IBM (Spain's) position on it was that 
it could not be done because conversational mode required the user to press 
ENTER. End of story. It can't be done. Three weeks later I demonstrated a 
number of 3270 screens all being simultaneously refreshed without user 
intervention. IBM Spain came along and saw it. "You could not have done this 
using standard code; you must have modified our system routines and we won't 
support it."  I assured them I had done no such thing and that everything 
was standard. It just required some lateral thinking. When I finally 
revealed how it was done (and I teased them for a while just for the fun of 
it :-)), the memorable comment was: "Oh Well, if you do it like THAT, of 
course it is possible..."

Frederico is absolutely correct when he says that the preferred way to 
manipulate DDL in Fujitsu COBOL is by dynamic SQL, and Fujitsu do not 
support ESQL CREATE.

However, dynamic SQL  is NOT "the ONLY way".

You can get an even richer experience if you simply create an ADOX object in 
your COBOL, and utilise the methods, properties, and events provided by 
MicroSoft. This will allow full acces to ALL DDL statements (NOT just CREATE 
TABLE) and it also allows cube access as well as flat tables.

And it is not limited to Fujitsu COBOL;  it will work with any COBOL that 
supports ActiveX or COM objects.

Pete.
```

###### ↳ ↳ ↳ Re: SQL Commands

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-04-09T10:56:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jllh32dusg0g8pnfoa59m2st6ckpsfe4l8@4ax.com>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <d0bf0$44370268$45491d7a$6510@KNOLOGY.NET> <YZPZf.501$Lm5.30@newssvr12.news.prodigy.com> <jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com> <49r7vrFpgg5dU1@individual.net>`

```
On Sun, 9 Apr 2006 13:57:09 +1200, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>
>"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message 
…[3 more quoted lines elided]…
>>
snip
>> So if using ESQL the only way is to use a dynamic statement. (with FJ
>> COBOL).
…[6 more quoted lines elided]…
>

snip
>
>Frederico is absolutely correct when he says that the preferred way to 
…[13 more quoted lines elided]…
>Pete. 

I also hate when someone does not read the full sentence.

I said " ... if using ESQL ...".
Now as far as I know ESQL standard is NOT ADOX or COM/ActivX.

Now if you do not use ESQL then you can use the others, which I also
mentioned on another reply.

And as you know I did bother looking for alternatives. (see my ADO
coding on this and other threads, and on the tek-tips faq I mention in
one of them). I could have also provided an example in DAO/RDO, but I
have choosen not to do it as its old technology.

As for ADOX, very similar to ADO in how it would work. my example with
ADO can be used as the basis for such code.
If someone is desesperate for ADOX code and cant do it on their own
then I may do a sample program.


Regarding ESQL, if you can find a way of doing the create table using
ONLY ESQL (AND NOT DYNAMIC SQL) with FJ cobol V7 or lower. (Not sure
V8 will allow it. havent tried it yet), then I am sure many
programmers will be happy with it. And this using the ESQL
pre-compiler supplied by FJ, as other venders will do things
differently.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: SQL Commands

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-04-11T00:39:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49v1vsFpgqmdU1@individual.net>`
- **References:** `<4436367c$0$36928$4fafbaef@reader3.news.tin.it> <d0bf0$44370268$45491d7a$6510@KNOLOGY.NET> <YZPZf.501$Lm5.30@newssvr12.news.prodigy.com> <jclf32h58f7qn008k25c28kh1f7cis53qv@4ax.com> <49r7vrFpgg5dU1@individual.net> <jllh32dusg0g8pnfoa59m2st6ckpsfe4l8@4ax.com>`

```
 

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message 
news:jllh32dusg0g8pnfoa59m2st6ckpsfe4l8@4ax.com...
> On Sun, 9 Apr 2006 13:57:09 +1200, "Pete Dashwood"
> <dashwood@enternet.co.nz> wrote:
…[63 more quoted lines elided]…
>
Sure... no problem :-)

Here's some code that meets the requirements you stated above:

...
EXEC SQL
    BEGIN DECLARE SECTION
END-EXEC
01 TableName PIC x(30)
EXEC SQL
    END DECLARE SECTION
END-EXEC

PROCEDURE DIVISION.

EXEC SQL
  CONNECT TO DEFAULT
END-EXEC

MOVE "Whatever" to TableName
EXEC SQL
   CALL CreateTable (:TableName)
END-EXEC

EXEC
    SQL COMMIT
END-EXEC

EXEC SQL
   DISCONNECT DEFAULT
END-EXEC
...

The above will work for any RDBMS that supports stored procedures, and where 
you have stored a general procedure that creates any table known to the 
database, given the table name. (A series of selectable CREATE TABLE 
statements. They might just as well be DROP or ALTER; it really doesn't 
matter...)

It is ESQL. And it works on Fujitsu V7.

The point I am trying to make is that just because the manual says you can't 
use ESQL to write DDL statements, doesn't mean that you 'can't'. It simply 
means the syntax for those statements is not directly supported. I think 
Michael was expressing the same idea in his mail to this thread.

And, BTW, my observations were not intended to be personal and I wouldn't 
suggest that you personally didn't bother to explore solutions. I have seen 
some of your posts in the Tek forum and I know you are giving good advice. 
(In fact I refrained from posting there because I saw you had it covered on 
a couple of occasions :-))

But all of us should be careful to qualify the statement "It's the ONLY 
way..." [I can think of...] or, better still, just don't use it... :-)

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
