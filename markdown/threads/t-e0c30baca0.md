[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SQL Expressions in Access, using Fujitsu COBOL

_10 messages · 5 participants · 2008-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### SQL Expressions in Access, using Fujitsu COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-22T15:40:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6h6qotFjca0jU1@mid.individual.net>`

```
I have been working intensely with MS Access  and Fujitsu COBOL over the 
last few weeks. (Actually I haven't been able to work too intensely because 
I have been recovering from illness, but on the occasions when I have been 
able to sit down and do some work, it has been intense... :-))

Most of the time it is perfectly satisfactory, and I have actually been 
surprised at how much SQL Language MS Access actually supports.

For the purposes for which it is required on this occasion, it is fine, but 
I have noticed some limitations when using it from COBOL.

1. There are some expressions in ANSI SQL which are not implemented in 
Access. COALESCE is one such.  You can get the same effect using an Access 
function called "Nz" (and there are also a couple of less elegant ways of 
dealing with returned nulls, including the old bog standard, indicator 
variables (ugly, but effective...)), but Nz doesn't work when invoked 
through ODBC from COBOL (using Fujitsu, which has an external ODBC.info 
file...). If I run a query in Access 2003 which uses the Nz function, it 
works perfectly. If I connect via OLEDB in C# and issue SQL containing it, 
it works perfectly. Write an ESQL query in COBOL and it crashes, returning 
SQLSTATE 37000 (normally a syntax error) and a message saying that an 
unknown function was found. Remove the Nz function and it works... (but, of 
course it doesn't help me detect nulls.)

2.  Access has always suffered from a bad reputation, which, since Access 
2000, has been thoroughly undeserved. The versions from then on used the 
same engine as SQL Server and are very effective RDB repositories if you use 
them as such and don't start trying to mix in Access "programming". However, 
it is annoying that functions which work perfectly well with Access and 
other languages, simply don't, with Fujitsu COBOL.

I'm curious as to whether this is a Fujitsu limitation or whether other 
people using Access from other versions of COBOL, via ODBC, have the same 
problems?

Pete.
```

#### ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-21T23:44:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1sgsa498oinq0teaeeqmig41b05kiqvcir@4ax.com>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net>`

```
On Fri, 22 Aug 2008 15:40:11 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>I have been working intensely with MS Access  and Fujitsu COBOL over the 
>last few weeks. (Actually I haven't been able to work too intensely because 
…[31 more quoted lines elided]…
>problems?

Nz is not a SQL function. Try 

IsNull(column_name, "")

If that does not work, try

IIF(Not IsNull(column_name), column_name, "")
```

##### ↳ ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-22T22:57:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6h7kciFjqlikU1@mid.individual.net>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net> <1sgsa498oinq0teaeeqmig41b05kiqvcir@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:1sgsa498oinq0teaeeqmig41b05kiqvcir@4ax.com...
> On Fri, 22 Aug 2008 15:40:11 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[48 more quoted lines elided]…
> IIF(Not IsNull(column_name), column_name, "")

Thanks Robert.

This time I did the homework and have already considered all of the above.

COALESCE is obviously the best, but not available.

I know Nz is not an SQL function; it is a VBA function that is accessible 
through Access.

I have a pretty good handle on what will work and what won't, and what I can 
generate easily and what is trickier to build and emit using C#. I'm more 
interested at the moment in the fact that Fujitsu COBOL doesn't work with 
these functions and wondered whether it is limited to Fujitsu...

Pete.
```

#### ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-22T09:20:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g8m0di$had$1@reader1.panix.com>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net>`

```
In article <6h6qotFjca0jU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>I have been working intensely with MS Access  and Fujitsu COBOL over the 
>last few weeks. (Actually I haven't been able to work too intensely because 
>I have been recovering from illness, but on the occasions when I have been 
>able to sit down and do some work, it has been intense... :-))

Best wishes for a rapid and complete recovery, Mr Dashwood.

DD
```

##### ↳ ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-22T23:08:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6h7l0mFjrf10U1@mid.individual.net>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net> <g8m0di$had$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:g8m0di$had$1@reader1.panix.com...
> In article <6h6qotFjca0jU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
>
Thank you Doc. :-)

I had viral pneumonia. It is very debilitating and has left me weak and 
tired. (I'm much better now, but still not 100%)
There's no treatment apart from rest and fluids and letting the immune 
system do it's stuff... (I imagine that most of my blood is alcohol anyway, 
so I really don't know how the pesky virus  survived... :-)) I normally keep 
very good health and this is the first time I remember being sick for a 
number of years.

It takes 4 to 7 weeks to recover (or not... :-)) In my case, 27 days before 
I could say I felt better.

I seriously recommend avoiding it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-22T12:25:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g8mb70$kbm$1@reader1.panix.com>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net> <g8m0di$had$1@reader1.panix.com> <6h7l0mFjrf10U1@mid.individual.net>`

```
In article <6h7l0mFjrf10U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[11 more quoted lines elided]…
>Thank you Doc. :-)

You're quite welcome, Mr Dashwood.

>I had viral pneumonia. It is very debilitating and has left me weak and 
>tired. (I'm much better now, but still not 100%)
>There's no treatment apart from rest and fluids and letting the immune 
>system do it's stuff... (I imagine that most of my blood is alcohol anyway, 
>so I really don't know how the pesky virus  survived... :-))

My memory is, admittedly, porous... and the World of Known Things - if 
such a thing exists - may have changed in the interim, as well... but I 
recall being taught that alcohol's antiseptic properties were primarily 
antibacterial and that some viruses could be crystallised in alcohol and 
yet still retain virulence.

(a curious, horrid thought... a 'virus crystal', like a bit of quartz but 
made of ebola or smallpox)

DD
```

#### ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2008-08-23T16:37:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hgb0b4hec89t6dcejia33ckbaberhkimvp@4ax.com>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net>`

```
On Fri, 22 Aug 2008 15:40:11 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I have been working intensely with MS Access  and Fujitsu COBOL over the 
>last few weeks. (Actually I haven't been able to work too intensely because 
…[33 more quoted lines elided]…
>Pete.
This is a ACCESS limitation
NZ is a user defined function internal to Access, so the JET engine
does not know about it and fails. All other such functions will fail
also, so do not be surprised if you find other failures.

to do what you need, you need to do as follows.
IIf(IsNull(my_field),my_value_if_null,my_field)

This works with Access, but may not work with other databases. Be sure
to make your code a portable as possible, or at least in a way you can
have the SQL statement easily replaceble.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-24T14:22:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hbuv8Fkek8qU1@mid.individual.net>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net> <hgb0b4hec89t6dcejia33ckbaberhkimvp@4ax.com>`

```


"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message 
news:hgb0b4hec89t6dcejia33ckbaberhkimvp@4ax.com...
> On Fri, 22 Aug 2008 15:40:11 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[44 more quoted lines elided]…
> does not know about it and fails.

Not quite. It is a VBA function which gets handled by the expression handler 
function in Jet (or not :-)). Certainly, Nz is a "special case". I have 
actually written VB functions and had them processed by SQL as part of Jet, 
until stored procedures became available...

>All other such functions will fail
> also, so do not be surprised if you find other failures.

No, they don't. But in this case I'm not using other functions. I only 
trtied that one because it was a recommended alternative to COALESCE.

I believe it probably WOULD work if all updates (like SP8) were applied to 
Jet 4. This was not the case on the machine Iused to test it and is being 
remedied as I write this. Anyway, Nz is not  what I want to use.
>
> to do what you need, you need to do as follows.
> IIf(IsNull(my_field),my_value_if_null,my_field)

Sure, that is one way, and a good one. I was hoping to avoid using IIF which 
is pretty much tied to Access, but I've come to the realization that  I 
cant.

IsNull (which, in the above, is also a VBA function just like Nz; the SQL 
function for IsNull takes 2 parameters...) is probably marginally better 
than using indicator variables.


>
> This works with Access, but may not work with other databases. Be sure
> to make your code a portable as possible, or at least in a way you can
> have the SQL statement easily replaceble.

That is very high on my list :-)

This code will be generated from the Migration Toolset (written in C#) so I 
need for it to be simple and consistent. It must also be easily possible to 
generate a different construct if a different RDBMS than Access is used, and 
it needs to generate differently for ALPHA, NUMERIC, and DATE types.

Currently  the rules for code generation are as follows:

For each column on the database (DBCOL):

if NOT a DATE type
          if NOT a CHAR type
                 if using ACCESS
                        generate:  IIF (NOT IsNull ([DBCOL]), [DBCOL], 0)
                else
                        generate:  COALESCE(DBCOL, 0)

          else
                 if using ACCESS
                       generate:  IIF (NOT IsNull ([DBCOL]), [DBCOL], "  ")
                 else
                        generate: COALESCE(DBCOL," ")
else
     if using ACCESS
            generate: IIF (NOT IsNull (CStr([DBCOL])), CStr([DBCOL]), 
"01/01/1900")
    else
            generate: COALESCE (CONVERT (datetime, convert(char(10), DBCOL, 
103)) , "01/01/1900")

I have some testing to do, but I think this will be fine. I'm looking 
forward to writing the C# that builds it :-)   (Can't do that until I have 
finalised on the COBOL template code. This is still under test but looking 
very good)

The exercise involved in researching this has been a very fruitful one.

Contributions here were very useful and I thank all concerned.

Pete.
```

###### ↳ ↳ ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-24T09:15:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<02esk.37719$ZE5.8596@nlpi061.nbdc.sbc.com>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net> <hgb0b4hec89t6dcejia33ckbaberhkimvp@4ax.com> <6hbuv8Fkek8qU1@mid.individual.net>`

```
Using ODBC, you can query the datasource for its support (or lack thereof) 
for specific functions... and/or get a list of non-ODBC keywords reserved by 
the specific data source.   (SqlGetInfo function)

I have to believe you can do the same thing using other interfaces.

MCM
```

###### ↳ ↳ ↳ Re: SQL Expressions in Access, using Fujitsu COBOL

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-25T10:38:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6he67iFkrajjU1@mid.individual.net>`
- **References:** `<6h6qotFjca0jU1@mid.individual.net> <hgb0b4hec89t6dcejia33ckbaberhkimvp@4ax.com> <6hbuv8Fkek8qU1@mid.individual.net> <02esk.37719$ZE5.8596@nlpi061.nbdc.sbc.com>`

```
"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:02esk.37719$ZE5.8596@nlpi061.nbdc.sbc.com...
> Using ODBC, you can query the datasource for its support (or lack thereof) 
> for specific functions... and/or get a list of non-ODBC keywords reserved 
> by the specific data source.   (SqlGetInfo function)

That's very interesting, Michael. Thanks, I didn't know that.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
