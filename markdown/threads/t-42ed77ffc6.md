[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Embedded SQL and MS ACCESS Dates

_15 messages · 8 participants · 2007-11_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Embedded SQL and MS ACCESS Dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T00:53:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
Is anybody using PC COBOLs to access a MS Access database ?

I haven't done it for quite some time now and the last time I did was Access 
97.

I am trying to INSERT records as part of a load, into an ACCESS 2003 DB, 
from COBOL.

The fields defined as DateTime on the database are causing an SQLSTATE 
22005 -
"[Microsoft][ODBC Microsoft Access Driver]Invalid character value for cast 
specification (null)"

With Access 97 I remember using floating point to update Date fields (the 
field contained the date as 8 digits on the left of the point , and the time 
as 4 digits on the right of the point) and this worked fine; it doesn't with 
ACCESS 2003.

The irony is that I can do it easily with C# as I can ensure the field being 
inserted is a Date type, but COBOL doesn't have a picture DATE as far as I 
know...

Anyway, it is necessary to do it from COBOL.

So far I have tried the following, all to no avail:

1. Set the Host Variable to be pic x(26) and used every date string you can 
imagine...
        YYYYMMDD
        YYYY/MM/DD
         DDMMYYYY
         DD/MM/YYYY

2. Used hyphens as separators instead of slashes.

3. Added times as strings  HH:MM:SS after the date string.

4. Tried using the SQL DATE function in the VALUES of the INSERT...

INSERT INTO  (a,b,c...) VALUES (:a, :b, Date(:c)...)

No joy. (Same result every time, so at least the syntax is OK... :-))

I'm sure this should be simple, but a search of the web finds thousands of 
people having similar problems with inserting Date data onto Access DBs.

Please don't tell me to use a third party Load system (many of them have the 
same problem, apparently... and anyway, I need for this to work from 
COBOL. )

Any assistance greatly appreciated.

I will solve this, but it would take less time if I had some help... :-)

Pete.
```

#### ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "me" <null@null.com>
- **Date:** 2007-11-04T12:52:05
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u9adndYmJL7mXbDanZ2dnUVZ8q2dnZ2d@bt.com>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5p5q5cFpdk59U1@mid.individual.net...
> Is anybody using PC COBOLs to access a MS Access database ?
>
Peter,

Does any of this help...

http://supportline.microfocus.com/documentation/books/nx40/nx40indx.htm
```

#### ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "me" <null@null.com>
- **Date:** 2007-11-04T12:54:41
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
Bugger, it didn't show what I wanted...

Database Access > 3. Data Types

Date and Time Data Types
COBOL does not have date/time data types so SQL date/time columns are 
converted to character representations.

If a COBOL output host variable is defined as PIC X(n), for a SQL timestamp 
value, where n is greater than or equal to 19, the date and time are 
specified in the format yyyy-mm-dd hh:mm:ss.ff..., where the number of 
fractional digits is driver-defined.

For example:

1994-05-24 12:34:00.000OpenESQL
Because OpenESQL can access any relational database and each database has 
different ways of specifying dates and times, a standard way is provided of 
specifying dates and times in input host variables. If you are using this 
method, you must use the option DETECTDATE in the SQL directive when 
compiling your program.

  a.. To specify a date, move the date into the host variable in the form 
{dyyyy-mm-dd}.

  b.. To specify a time, move the time into the host variable in the form 
{thh:mm:ss}.

  c.. To specify a date and time, move the date and time into the host 
variable in the form {tsyyyy-mm-dd hh:mm:ss}.

For example:

$set sql(dbman=odbc, detectdate)
 01 Hire-Date pic x(26).
 move "{d'1965-11-02'} to Hire-Date
 exec sql
     insert into emp (HireDate) values (:Hire-Date)
 end-exec
```

##### ↳ ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T02:01:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p5u5kFpnd78U1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com>`

```

```

##### ↳ ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T02:06:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p5ue7Fpf7pkU1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com>`

```
Sorry about accidental blank post... :-)

I found this stuff from the link you posted. Thanks.

Unfortunately, it isn't useful for me although I read it with interest, in 
case I'm ever using MicroFocus COBOL.

In this instance I need a solution for Fujitsu, but sometimes looking at 
other stuff can jog an idea.

Thanls for the link and for your comments. I appreciate someone actually 
trying to help :-)

Pete.

TOP POST NO MORE BELOW FROM ME...

"me" <null@null.com> wrote in message 
news:Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com...
> Bugger, it didn't show what I wanted...
>
…[37 more quoted lines elided]…
>
```

##### ↳ ↳ [O/T] Re: Embedded SQL and MS ACCESS Dates

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-11-04T11:45:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7HmXi.4$Eu6.99426@news.sisna.com>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com>`

```

"me" <null@null.com> wrote in message 
news:Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com...

[skipped]
> Because OpenESQL can access any relational database and each database has

I "like" those b.rds to name some pure commercial products starting with 
"Open".
Did anybody had an idea to patent/trademark the word "Open" for opensource 
community ?
i.e. if some product name is started from "Open" they should provide all 
souces under GPL or something like that :-)))

Really the question is if anybody knows opensource SQL precompiler for Cobol 
(even not finished / non-working, even just parser) ?
I have my own but I'm afraid to publish it because it's garbage. It's very 
limited, I'm not parsing SQL statements, indicator variables never been 
implemented etc. I took a look at mysql/postgres ESQL but it's tied to C/C++ 
recognizing C/C++ datatypes in parser so it's not easy to take it as a 
"base"...

Regards,
Sergey
```

###### ↳ ↳ ↳ Re: [O/T] Re: Embedded SQL and MS ACCESS Dates

- **From:** Waldek Hebisch <hebisch@math.uni.wroc.pl>
- **Date:** 2007-11-08T18:54:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgvm1b$t0n$2@z-news.pwr.wroc.pl>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <Y6KdnSziwauKXLDanZ2dneKdnZydnZ2d@bt.com> <7HmXi.4$Eu6.99426@news.sisna.com>`

```
Sergey Kashyrin <ska@resqnet.com> wrote:
> Really the question is if anybody knows opensource SQL precompiler for Cobol 
> (even not finished / non-working, even just parser) ?
…[4 more quoted lines elided]…
> "base"...

Look at Firebird.  I looked at older version and it contained
embedded SQL precompiler for 6 different languages including Cobol.
```

#### ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-11-04T05:10:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194181803.514565.249040@e9g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5p5q5cFpdk59U1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
On Nov 4, 3:53 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Is anybody using PC COBOLs to access a MS Access database ?
>
…[54 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

I not really sure about Fujitsu Cobol, but on Microfocus NetExpress
the formatis as follows;

03  SQLdatefield         SQL type is timestamp.

03  wSQLdate             pic x(29).

with proper SQL date values formatted as: "yyyy-mm-dd hh:mm:ssss"
```

##### ↳ ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T03:20:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p62p1FpkttrU1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <1194181803.514565.249040@e9g2000prf.googlegroups.com>`

```


"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1194181803.514565.249040@e9g2000prf.googlegroups.com...
> On Nov 4, 3:53 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[75 more quoted lines elided]…
>

Thanks Rene. Doesn't help unfortunately... :-)

Pete.
```

#### ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-04T15:06:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8glXi.150$3Z2.100@nlpi069.nbdc.sbc.com>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
In article <5p5q5cFpdk59U1@mid.individual.net>, "Pete Dashwood" 
<dashwood@removethis.enternet.co.nz> wrote:
>Is anybody using PC COBOLs to access a MS Access database ?
>
…[9 more quoted lines elided]…
>specification (null)"

Is this of any help?

http://www.devnewsgroups.net/group/microsoft.public.sqlserver.xml/topic14659.
aspx
```

##### ↳ ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T13:17:30+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p75opFpsn2cU1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <8glXi.150$3Z2.100@nlpi069.nbdc.sbc.com>`

```


"Doug Miller" <spambait@milmac.com> wrote in message 
news:8glXi.150$3Z2.100@nlpi069.nbdc.sbc.com...
> In article <5p5q5cFpdk59U1@mid.individual.net>, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[18 more quoted lines elided]…
>

I dunno... it returns a 404 when I access it :-)

Thanks anyway, Doug. Problem is now solved (see separate thread) but it took 
me about 13 hours to run it down... (I guess I'm getting old :-))

Pete.
```

###### ↳ ↳ ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-05T01:05:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e%tXi.2754$yV6.2445@newssvr25.news.prodigy.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <8glXi.150$3Z2.100@nlpi069.nbdc.sbc.com> <5p75opFpsn2cU1@mid.individual.net>`

```
In article <5p75opFpsn2cU1@mid.individual.net>, "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[24 more quoted lines elided]…
>I dunno... it returns a 404 when I access it :-)

Works for me. Did you observe that it had wrapped to a second line?
>
>Thanks anyway, Doug. Problem is now solved (see separate thread) but it took 
>me about 13 hours to run it down... (I guess I'm getting old :-))

Hmmm... for some reason, I'm not seeing that separate thread. What did the 
issue turn out to be?
```

#### ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2007-11-04T18:23:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194225389_2857@sp12lax.superfeed.net>`
- **In-Reply-To:** `<5p5q5cFpdk59U1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
Pete Dashwood wrote:
> Is anybody using PC COBOLs to access a MS Access database ?
> 
…[52 more quoted lines elided]…
> Pete.

Have a look at

    <http://www.codefixer.com/codesnippets/insert_date_access_sql.asp>

    <http://www.hotscripts.com/Detailed/55202.html>

Both show format as YYYY-MM-DD.

The second makes a point of using the hash mark delimiters.

HTH,

Jeff




----== Posted via Newsfeeds.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

#### ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** Robert <no@e.mail>
- **Date:** 2007-11-04T19:53:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnssi39tr1p69naln9liaf2agpt5so74td@4ax.com>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net>`

```
On Mon, 5 Nov 2007 00:53:14 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:


>1. Set the Host Variable to be pic x(26) and used every date string you can 
>imagine...
…[13 more quoted lines elided]…
>No joy. (Same result every time, so at least the syntax is OK... :-))

The Date() function returns today's date. It should have ignored :c and inserted today's
date. Try changing the column type from DateTime to Date. If that works, the next step is
inserting your dates rather than the system date. Functions DateValue() and CDate() take a
string as input and output a date type (not datetime). The string format depends on your
regional settings. 

To go the other way, convert date to string, use the Format() function.
```

##### ↳ ↳ Re: Embedded SQL and MS ACCESS Dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T15:28:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p7deuFpomquU1@mid.individual.net>`
- **References:** `<5p5q5cFpdk59U1@mid.individual.net> <gnssi39tr1p69naln9liaf2agpt5so74td@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:gnssi39tr1p69naln9liaf2agpt5so74td@4ax.com...
> On Mon, 5 Nov 2007 00:53:14 +1300, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[21 more quoted lines elided]…
> The Date() function returns today's date.

I should have checked it before trying it :-) Just tired.

>It should have ignored :c and inserted today's
> date. Try changing the column type from DateTime to Date.

Changing the DB format was going to be my next avenue of investigation. 
Obviously, as a last ditch I could simply load date strings and convert them 
to DATE types later, but I didn't really want to do that...

The problem is now solved (see separate thread)


>If that works, the next step is
> inserting your dates rather than the system date. Functions DateValue() 
…[3 more quoted lines elided]…
> regional settings.

Yes, I found out about all this during a number of hours browsing the Web... 
:-)

>
> To go the other way, convert date to string, use the Format() function.
>

Yep, read about that too.

Thanks for your post, Robert. What I was really looking for with this post 
was someone who is actually using Fujitsu COBOL to access an ACCESS database 
and who could simply give me a copy of the Host Variables used.

Nevertheless, despite the time (which I can ill afford right now) it has 
been an edifying exercise and I am grateful to all who contributed.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
