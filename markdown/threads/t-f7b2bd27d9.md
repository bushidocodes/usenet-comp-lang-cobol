[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] My, How Things Have Changed

_15 messages · 5 participants · 2010-11_

---

### [OT] My, How Things Have Changed

- **From:** docdwarf@panix.com ()
- **Date:** 2010-11-03T00:08:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iaq967$5hl$1@reader1.panix.com>`

```

I learned something that tickled my my mind and thought that others, even 
less well-schooled than I - if such a thing is possible! - might 
appreciate this treasure-in-a-pebble.

The concept of 'SQL injection' is not foreign to me but it existed only as 
that... a concept; when I code screens they're invoked by EXEC CICS and 
followed by a last-to-first check of fields for edit failures.  As anyone 
with a few decades' of experience might know name-checking (both for 
people and addresses) is its own Art.

I ran across the example of 'Little Bobby Tables' for the first time (the 
name appears in a UseNet posting of 2003 and the earliest 'explanation' of 
it I can find is http://xkcd.com/327/ (which appears to be from 2007)) and 
was amused, enlightened, stunned and horrified, all simultaneously.  That 
*anyone* would allow an interface which permitted user input to slip below 
the application interface and fall into (for lack of better terminology) 
the command-interpreter gave me Great Pause; my first response was 'how 
could such a thing ever pass a QA review?'...

... and the answer came back, out of the abyss, as it were, of 'They don't 
do those much any more.'  And in a way... they do and they don't, 
depending on who 'they' is.  I've seen websites that are, to my 
steam-powered way of thinking, a delight... the equivalent of a mechanic's 
manual for an automobile where one moves the cursor over an area and an 
expanded view comes up, and expansions within those views, and without 
remembering X1AB-7725-6A315-44817 one can order a replacement bracket, 
fixture, bit of trim or individual screw.

On the other hand... I can easily imagine a small school district (or even 
an individual school not open to general admission, called 'private' in 
the United States of America and 'public' in BritSpeak-land) where someone 
who knows a bit of computer-manipulation puts together a... something to 
keep track of people/stuff/events... and Someone Important glances over a 
shoulder or at a print-out and says 'That might be helpful if only we 
could... '... and it grows, organically, into a collection of patches and 
kludges like the Systems of Old did...

... but without the initial rigor required by the Systems of Old, with 
their Glass Houses and High Priests and folks who would actually approach 
the task with the discipline of people at least pretending to do Science.  
This is not to denigrate their inventiveness, creativity or 
problem-solving ability but just as a species changes to reflect its 
environment so might solutions to a problem - the same problem - be 
different when their formulators or audiences are The Homebrew Computer 
Society instead of The Association for Computing Machinery.

This and a (coin of small value) will get me (a minute container of a 
beverage)... but as goes the aphorism to which I passingly referred in the 
opening paragraph, 'Blessed is he who finds treasures in pebbles; he will 
always be surrounded by riches.'

DD
```

#### ↳ SQL injection vulnerability was Re: [OT] My, How Things Have Changed

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2010-11-03T12:16:10-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<glu2d6pfjv58e7jv5na14h1uvgjcsrbdou@4ax.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com>`

```
In reading the posting below and the cartoon that it pointed to I
became confused and worried.  Does this mean that a CICS transaction
with static SQL is vulnerable to SQL injection?  Does it mean that
once something gets on a database it could become SQL code at some
future point?  As someone who gave up trying to validate names because
of the variation (O'Henry for example), this has me concerned.  The
validation checking for this might be esoteric to say the least.  Is a
right parenthesis invalid in a person's name or a place name, for
example?  

Clark Morris

On Wed, 3 Nov 2010 00:08:39 +0000 (UTC), docdwarf@panix.com () wrote:

>
>I learned something that tickled my my mind and thought that others, even 
…[50 more quoted lines elided]…
>DD
```

##### ↳ ↳ Re: SQL injection vulnerability was Re: [OT] My, How Things Have Changed

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2010-11-03T12:16:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<857b8bcb-3d86-436f-aa44-a5ab6afc0707@c16g2000vbp.googlegroups.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <glu2d6pfjv58e7jv5na14h1uvgjcsrbdou@4ax.com>`

```
On Nov 3, 10:16 am, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> In reading the posting below and the cartoon that it pointed to I
> became confused and worried.  Does this mean that a CICS transaction
…[6 more quoted lines elided]…
> example?  


SQL injection is principally an issue with dynamically constructed SQL
queries that use in-line values for parameters.  Static SQL statements
are usually not vulnerable, nor are dynamic ones where all the values
are either pre-defined or come from variables outside the SQL
statement (“?” place holders or  “@” variables in stored procedures,
for example).

See:  http://www.owasp.org/index.php/SQL_Injection
```

##### ↳ ↳ Re: SQL injection vulnerability was Re: [OT] My, How Things Have Changed

- **From:** docdwarf@panix.com ()
- **Date:** 2010-11-04T14:55:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iauhhi$31i$1@reader1.panix.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <glu2d6pfjv58e7jv5na14h1uvgjcsrbdou@4ax.com>`

```
In article <glu2d6pfjv58e7jv5na14h1uvgjcsrbdou@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>In reading the posting below and the cartoon that it pointed to I
>became confused and worried.  Does this mean that a CICS transaction
>with static SQL is vulnerable to SQL injection?

To the best of my knowledge, Mr Morris, no.

>Does it mean that
>once something gets on a database it could become SQL code at some
>future point?

To the best of my knowledge, Mr Morris, that is the concept behind 'stored 
procedures', chunks of SQL that get stored in a dataset/table and then 
invoked.

>As someone who gave up trying to validate names because
>of the variation (O'Henry for example), this has me concerned.

It is good to know one's own limits, aye... although how one learns one's 
limits without exceeding them might be left for another lesson.

>The
>validation checking for this might be esoteric to say the least.  Is a
>right parenthesis invalid in a person's name or a place name, for
>example?  

I do not believe that the Little Bobby Tables scenario would appear in Ye 
Olde Style of coding, where CICS maps and COBOL work-areas are. for the 
most part, rather well delineated.  If one is working with a lower-level 
language and system then the borders might become fuzzier and the 
possibility for injection increases.

DD
```

#### ↳ Re: My, How Things Have Changed

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-03T13:43:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com>`

```
On Nov 3, 12:08 am, docdw...@panix.com () wrote:
> I learned something that tickled my my mind and thought that others, even
> less well-schooled than I - if such a thing is possible! - might
…[49 more quoted lines elided]…
> DD

For your information there are freely available documents on the
internet which detail how such attacks may be made in detail. The
number and variety of attacks beggars belief.
```

##### ↳ ↳ Re: My, How Things Have Changed

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-04T12:23:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8je98cFnbeU1@mid.individual.net>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com>`

```
Alistair Maclean wrote:
> On Nov 3, 12:08 am, docdw...@panix.com () wrote:
>> I learned something that tickled my my mind and thought that others,
…[57 more quoted lines elided]…
> number and variety of attacks beggars belief.

And 3 or 4 basic and fundamental checks eliminate 99% of them.

In this day and age the only way an injection attack can work is by 
negligence on the part of a developer.

But if it worries you, get off SQL.

LINQ is an infintely better solution and injection attacks are "not 
applicable" if it is written properly. (User input is converted to 
parameters and cannot be part of the directly executed string.)

Pete.
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2010-11-03T16:49:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<441c50e0-a27d-4dcc-8969-c5a185005225@g25g2000yqn.googlegroups.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com> <8je98cFnbeU1@mid.individual.net>`

```
On Nov 3, 6:23 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Alistair Maclean wrote:
> > On Nov 3, 12:08 am, docdw...@panix.com () wrote:
…[69 more quoted lines elided]…
> parameters and cannot be part of the directly executed string.)


Whether LINQ is "infinitely better" is perhaps debatable, but that
solution to injection attacks is exactly the same one correctly
written SQL uses.  The syntax varies from language to language, and
the follow Java example is modified from the OWASP site:

// Unsafe
 String query = "SELECT account_balance FROM user_data WHERE user_name
= '" + custname + "'";
 ResultSet results = statement.executeQuery( query );

// Safe:
 String query = "SELECT account_balance FROM user_data WHERE user_name
= ? ";
 PreparedStatement pstmt = connection.prepareStatement( query );
 pstmt.setString( 1, custname);
 ResultSet results = pstmt.executeQuery( );

There are other solutions as well, but proper parameterization is
generally the best solution.
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-04T13:46:05+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jee2fFgceU1@mid.individual.net>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com> <8je98cFnbeU1@mid.individual.net> <441c50e0-a27d-4dcc-8969-c5a185005225@g25g2000yqn.googlegroups.com>`

```
robertwessel2@yahoo.com wrote:
> On Nov 3, 6:23 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[93 more quoted lines elided]…
> generally the best solution.

I use checks at the front end for things like "--" and ";" AND parameterize, 
when using dynamic SQL.

I still find LINQ an overall better solution.

Pete.
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

- **From:** docdwarf@panix.com ()
- **Date:** 2010-11-04T15:05:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iaui3e$31i$3@reader1.panix.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com> <8je98cFnbeU1@mid.individual.net>`

```
In article <8je98cFnbeU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>But if it worries you, get off SQL.
>
>LINQ is an infintely better solution and injection attacks are "not 
>applicable" if it is written properly.

Of *course*.... 'all ya gotta do is' get off SQL, get into LINQ and write 
it properly'.  

DD
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-05T14:11:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jh3uaFsn3U1@mid.individual.net>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com> <8je98cFnbeU1@mid.individual.net> <iaui3e$31i$3@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8je98cFnbeU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> DD

Sure.

How hard is that? :-)

Pete.
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-11-05T12:26:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ib0t5g$svj$1@reader1.panix.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <8je98cFnbeU1@mid.individual.net> <iaui3e$31i$3@reader1.panix.com> <8jh3uaFsn3U1@mid.individual.net>`

```
In article <8jh3uaFsn3U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8je98cFnbeU1@mid.individual.net>,
…[14 more quoted lines elided]…
>How hard is that? :-)

Perhaps as easy as any other solution to a technical problem which is 
prefaced by an 'all ya gotta do is'.

DD
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-05T05:35:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ad5303a-ce9c-4bee-9ab6-bba80fe78df6@j18g2000yqd.googlegroups.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com> <8je98cFnbeU1@mid.individual.net> <iaui3e$31i$3@reader1.panix.com> <8jh3uaFsn3U1@mid.individual.net>`

```
On Nov 5, 1:11 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article <8je98cFnb...@mid.individual.net>,
…[17 more quoted lines elided]…
>

Does DB2 support LINQ? (he asked innocently)....
```

###### ↳ ↳ ↳ Re: My, How Things Have Changed

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-07T11:58:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jm4s8FgjvU1@mid.individual.net>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com> <8je98cFnbeU1@mid.individual.net> <iaui3e$31i$3@reader1.panix.com> <8jh3uaFsn3U1@mid.individual.net> <8ad5303a-ce9c-4bee-9ab6-bba80fe78df6@j18g2000yqd.googlegroups.com>`

```
Alistair Maclean wrote:
> On Nov 5, 1:11 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[21 more quoted lines elided]…
> Does DB2 support LINQ? (he asked innocently)....

I've only used it with SQL Server, but it is designed for use with any data 
repository. I should think it is possible through ODBC but you would need to 
write the query in C# or call/invoke a Class written in C#, as LINQ is 
"Language INtegrated".

Let the man who invented it explain it: 
http://blogs.msdn.com/b/charlie/archive/2007/01/26/anders-hejlsberg-on-linq-and-functional-programming.aspx

(Click the "stream it" link on the page to see an excellent video.)

By the way, I'm not so stupid that I seriously think that all the mainframe 
sites using SQL COULD move to LINQ (without a great deal of effort) and some 
of this conversation was with tongue in cheek.

I DO believe that LINQ (and the functional programming that supports it) IS 
better than SQL for manipulating data, but at the moment it is largely 
academic. The syntax is worth investigating, but, currently you would need a 
free download of C# and Visual Studio in order to do so.

Probably some people who wish to teach themselves C# will do that anyway and 
it then becomes an option for them.

Pete.
```

##### ↳ ↳ Re: My, How Things Have Changed

- **From:** docdwarf@panix.com ()
- **Date:** 2010-11-04T15:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iauhpq$31i$2@reader1.panix.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com> <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com>`

```
In article <6ab29326-da36-4782-ac27-8c6fd0ffffd1@v16g2000yqn.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@googlemail.com> wrote:
>On Nov 3, 12:08?am, docdw...@panix.com () wrote:

[snip]

>> ?That
>> *anyone* would allow an interface which permitted user input to slip below
…[5 more quoted lines elided]…
>> do those much any more.'

[snip]

>For your information there are freely available documents on the
>internet which detail how such attacks may be made in detail. The
>number and variety of attacks beggars belief.

I'm sure there are, Mr Maclean; what man can make, man can break.

DD
```

#### ↳ Re: My, How Things Have Changed

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-08T07:45:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1e18acf1-7741-4b10-b037-71a18c3d8fd3@z22g2000pri.googlegroups.com>`
- **References:** `<iaq967$5hl$1@reader1.panix.com>`

```
On Nov 3, 12:08 am, docdw...@panix.com () wrote:
> I learned something that tickled my my mind and thought that others, even
> less well-schooled than I - if such a thing is possible! - might
> appreciate this treasure-in-a-pebble.

For interest:

http://www.bbc.co.uk/news/technology-11711478

details a Romanian hacker using SQL injection to hack the Royal Navy
web site.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
