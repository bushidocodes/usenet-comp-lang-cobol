[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/390 COBOL Programmers

_21 messages · 10 participants · 2000-03 → 2000-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### OS/390 COBOL Programmers

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000313095137.22475.00000615@ng-cn1.aol.com>`

```
Hi,

Just got back from SHARE. An excellent week.

I attended a lot of sessions on COBOL, PL/I, and LE. One thing that struck me
was a session where the compiler developers were saying they don't have many
new compiler capabilities on their agenda because programmers weren't coming up
with stated needs for them. At that same session, two programmers came up with
new needs (primarily for very large tables) that would not require waiting for
the new standard to come out.

A related point was that there are so many shops out there not using what's
already there that it's hard to make a business case for adding new
functionality.

So it got me to thinking. Perhaps we've been a little lazy, a little
non-creative. I would like to challenge each COBOL programmer on OS/390 class
systems to think a little bit about what enhancements to existing applications,
or new applications, they would make if the compiler supported them. Can we
come up with practical features that we can ask IBM to implement? And
furthermore, what would it take to get companies to move off of the old COBOL
technology? They made it clear they can't use a "stick" (and besides, IBM has
been steadily discontinuing support for various compiler versions and there are
still a lot of companies this hasn't motivated to move). What would give us all
a jump start?

One reason Java and related technologies get all the hype is that they are
glitzy (if not always the best tool for the task at hand). COBOL is not
particularly glitzy, it just gets lots of jobs done in a repeatable,
maintainable, sustainable way. Do we want to raise the level of perception /
appreciation for COBOL? How can we take charge of our careers and our [portion
of the] industry?

Just some thoughts.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: OS/390 COBOL Programmers

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD263D.6D9B44A2@cusys.edu>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com>`

```
I would like to see some compiler options hard coded into the
Environment or ID divisions.  I would especially like to see one which
caused a compile failure if it was possible to drop through paragraphs
and/or sections.
```

##### ↳ ↳ Re: OS/390 COBOL Programmers

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ajofh$h8u$1@slb1.atl.mindspring.net>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <38CD263D.6D9B44A2@cusys.edu>`

```
Howard,
  Interestingly enough such a requirement (for fall thru logic analysis) was
submitted to GUIDE about 15 years ago.  The original version(s) of VS COBOL
II included a "diagnostic" tool.  ($RNDMP) which did flow analysis (under
certain circumstances).  There was a requirement to make this a "public
interface" and to provide diagnostics when such flow occurred.

I would suggest that you (or Steve Comstock - or someone) submit this as a
(revised) SHARE requirement and/or via your normal IBM support channel.  My
guess (and it is ONLY a guess) is that much of the "flow analysis" is still
in the compiler's optimizing phase - but you would need to submit that to IBM
for an official response.
```

#### ↳ Re: OS/390 COBOL Programmers

- **From:** joarmc@linux2.johnmckown.net (John McKown)
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn8cs298.2dq.joarmc@linux2.johnmckown.net>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com>`

```

Well, one thing that I could use is a tighter integration with the new
OS/390 UNIX System Services. An easy way to get at the UNIX command
line parameters and environment variables would be nice. I know how
to do it using "pure" COBOL, but it involves using POINTER variables.
POINTERs are not greatly used by most COBOL programmers!

Also, it would be helpful if I could do "terminal" I/O via the DISPLAY and
ACCEPT verbs (or something similiar). In batch, for diagnostic messages,
I often use something like:

DISPLAY 'THE VALUE OF VAR IS' VAR UPON SYSOUT.

It would be nice to be able to use an UPON STDERR or UPON STDOUT to
direct the message to either UNIX's "stderr" or "stdout". Also, to
be able to do something like:

ACCEPT VARIABLE FROM STDIN.

The ability to use an HFS (UNIX) file specification in an ASSIGN clause
would be helpful also. At present, I need a DD statement. This is not
very UNIX-like. And is very difficult if I want to run a command from
the UNIX shell prompt. I end up wrapping the command in a "shell script"
which does the ALLOCATE. This is similiar to the way I do it in TSO.
But it is not very "UNIX-like". I.e. If I'm going to write UNIX programs
in COBOL for OS/390, then I want it to be "UNIX-like", not some half-assed
mixture of UNIX and "normal" OS/390 batch processing.

Unfortunately, I am not familiar with UNIX COBOL compilers, so I don't
know how they do this on, say a SUN system or AIX system.

Another thought is in the area of being able to have a "named constant"
which has a self-defining length. I'm thinking of something like an 88
level. For example:

99 MESSAGE1 VALUE IS 'MESSAGE NUMBER 1'.

I could then use a LENGTH OF to get the "compiled" length. This would allow
me to do something similiar to:

	CALL SUBROUTINE USING MESSAGE1, LENGTH OF MESSAGE1.

This way, I don't need to count the number of characters in the VALUE
clause and update the PIC X(nn) every time I change it. The use that I
have for this is in calling UNIX subroutines where I want to pass a
message and it's length for output. Actually, if the DISPLAY verb were
enhanced, then I wouldn't really need this. Well, maybe I would, I'm just
not sure. There are a lot of places in OS/390 UNIX where I need to pass
the "ADDRESS OF" a variable instead of the variable itself. I.e.

	CALL UNIX USING ADDRESS OF MESSAGE1, LENGTH OF MESSAGE1.

Also, I would like to be able to do an "ADDRESS OF" for variables in
Working-Storage. Granted, I can easily cheat to get this by writing
a subroutine similiar to:

PROGRAM ID. GETADDR.
LINKAGE SECTION.
01 LS-DATA PIC X.
01 LS-ADDR POINTER.
PROCEDURE DIVISION USING LS-DATA, LS-ADDR.
SET LS-ADDR TO ADDRESS OF LS-DATA.
GOBACK.

CALL 'GETADDR' VARNAME, ADDRESS-OF-VARNAME.

But I think it would be better to be able to say:
SET ADDRESS-OF-VARNAME TO ADDRESS OF VARNAME.

Again, I could use this function when I need to call UNIX-related subroutines
from COBOL.

In case you're wondering why I'm using COBOL and UNIX, it's because I don't
have a C compiler. We aren't going to get a C compiler. And that's the
end of that discussion! I need to use COBOL to write "CGI" programs for
the OS/390 Web Server. I can use assembler, but it is not a shop standard,
and it is more difficult to write (in general). Actually, I would prefer
to use assembler myself, but then I'd be stuck with supporting the bloody
thing forever since we have very few assembler programmers in our applications
group. I'm not in applications, I'm an OS/390 SysProg. And an assembler
"bigot" <grin>

Just some thoughts,
John
```

##### ↳ ↳ Re: OS/390 COBOL Programmers

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8alm02$j0f$1@slb7.atl.mindspring.net>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <slrn8cs298.2dq.joarmc@linux2.johnmckown.net>`

```
Comments "inter-laced" (about availability in next Standard).  You *should*
communicate to IBM if you think these items are worth implementing BEFORE
they provide a "full" next-Standard compiler.
```

#### ↳ COBOL "Requirements" for vendors (slightly IBM-centric) Re: OS/390 COBOL Programmers

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8alomc$blb$1@slb7.atl.mindspring.net>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com>`

```
One of the things that working on Standards and for COBOL software-type
vendors has taught me is that MOST "real users" don't understand that they
really, REALLY, need to submit their "enhancement" requests to the provider.
(They always think that SOMEONE ELSE is doing this and that they don't have
time to do it.) Furthermore, that the more users who ask for something, the
more likely it is to get "implemented".  Unfortunately, most users also don't
understand that (just like in your real world programming environments) there
are COSTS and LEAD-TIMES involved in moving from an initial "enhancement
request" to a provided "functionality".  (When you ask for something, tell
the vendor what you will be willing to pay for it - and how soon you need
it - and why.)

Having said that,  after Steve's original comment below, I have listed
several (well more than just several) items that I think IBM COBOL (and LE)
users should ask IBM for *now* in order to see them delivered before 2005.
If you don't think it is worth requesting them now if you won't see them
delivered for a few years, then PLEASE stop complaining about not getting
what you want with 2 or 3 months warning !!! <G>

Although targeted at the IBM (mainframe) COBOL environment, I think that many
of these "enhancement requests" should be submitted to a NUMBER of other
vendors represented in this newsgroup.
```

##### ↳ ↳ Re: COBOL "Requirements" for vendors (slightly IBM-centric) Re: OS/390 COBOL Programmers

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.133cc08a13fcf7c398998a@news.mersinet.co.uk>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <8alomc$blb$1@slb7.atl.mindspring.net>`

```
I noticed that William M. Klein as wmklein@nospam.netcom.com said...
> One of the things that working on Standards and for COBOL software-type
> vendors has taught me is that MOST "real users" don't understand that they
> really, REALLY, need to submit their "enhancement" requests to the provider.
> (They always think that SOMEONE ELSE is doing this and that they don't have
> time to do it.)

Most users don't have the contact route obviously available to them - 
that certainly goes for mainframe programmers where the compiler 
responsibility is with the systems programmers (and applications people 
all know that they speak in tongues).

> Furthermore, that the more users who ask for something, the
> more likely it is to get "implemented".

I always make that point but most people genuinely feel that they are far 
removed from the process.

[snipped suggestions]
> I probably can/will come up with some others, but I think that this is MORE
> than enough to get the conversation "going".

I'd say so.  Now how do we get in touch with these people?  Not so daft a 
question as I don't know any IBM UK contact for this sort of deal, and 
I'm not even working on an IBM COBOL site right now.
```

###### ↳ ↳ ↳ Re: COBOL "Requirements" for vendors (slightly IBM-centric) Re: OS/390 COBOL Programmers

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aurbf$i8$1@slb1.atl.mindspring.net>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <8alomc$blb$1@slb7.atl.mindspring.net> <MPG.133cc08a13fcf7c398998a@news.mersinet.co.uk>`

```
Charles F Hankel <charles@hankel.mersinet.co.uk> wrote in message
>
> I'd say so.  Now how do we get in touch with these people?  Not so daft a
> question as I don't know any IBM UK contact for this sort of deal, and
> I'm not even working on an IBM COBOL site right now.
>

IBM mainframe requirements may be submitted thru SHARE (or SHARE or GUIDE
Europe).  In addition (and this does require that you be at a "licensed" IBM
shop) you may submit them thru the "REQUEST" process (handled via IBM
support).  I don't have a contact for European GUIDE/SHARE at the moment -
but think that if you ask in IBM-MAIN, they could probably provide one.  If
this is a problem for you, let me know and I will post your question for you.
```

###### ↳ ↳ ↳ Re: COBOL "Requirements" for vendors (slightly IBM-centric) Re: OS/390 COBOL Programmers

_(reply depth: 4)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.133eac39f218a00798999b@news.mersinet.co.uk>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <8alomc$blb$1@slb7.atl.mindspring.net> <MPG.133cc08a13fcf7c398998a@news.mersinet.co.uk> <8aurbf$i8$1@slb1.atl.mindspring.net>`

```
I noticed that William M. Klein as wmklein@nospam.netcom.com said...
> Charles F Hankel <charles@hankel.mersinet.co.uk> wrote in message
> >
…[10 more quoted lines elided]…
> this is a problem for you, let me know and I will post your question for you.

That's OK, I'm a subscriber to IBM-MAIN though at the moment I do tend to 
skip through a lot of it, probably because it isn't directly relevant to 
current work.
```

#### ↳ Re: OS/390 COBOL Programmers

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u1BdzOej$GA.248@cpmsnbbsa03>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com>`

```
I would like to see support for reading, and writing comma, or tab delimited
files.

In other words, make the transformation transparent to the programmer.
The write operation would be required to use the FROM option.

The FD might look something like:

FD OUTPUT-FILE
      RECORDING MODE DELIMITED BY [COMMA or TAB or '?']
      REPLACING =="== BY ==' '==
                              ==~== BY ==-==.

FD INPUT-FILE
      RECORDING MODE DELIMITED BY [COMMA or TAB or '?']
      REPLACING ==' '== BY =="==
      ON ALPHANUMERIC OVERFLOW [TRUNCATE or ABORT]
      ON NUMERIC OVERFLOW [TRUNCATE or ABORT].
```

##### ↳ ↳ Re: OS/390 COBOL Programmers

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE9F95.94E18225@cusys.edu>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03>`

```
I have wanted one for some time, but I'm not so sure now that this is
the best way to go.  It might be better to go through a JDBC/ODBC
interface, not even knowing nor caring what the data look like.  Your
spreadsheet or database or whatever then reads the data in from this
more universal standard.

Basically, we both want to be able to pass data (and maybe meta data)
between COBOL and a universal interface.

DennisHarley wrote:
> 
> I would like to see support for reading, and writing comma, or tab delimited
…[16 more quoted lines elided]…
>       ON NUMERIC OVERFLOW [TRUNCATE or ABORT].
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udXzEDgj$GA.250@cpmsnbbsa05>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu>`

```

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:38CE9F95.94E18225@cusys.edu...
> I have wanted one for some time, but I'm not so sure now that this is
> the best way to go.  It might be better to go through a JDBC/ODBC
…[5 more quoted lines elided]…
> between COBOL and a universal interface.

Actually between mainframe and desktop applications.
Sometimes we get data from a user in the form of an Excel Spreadsheet or
Access database.
It ain't brain surgery to reformat the data, it is just time consuming.

Since delimited files have been around for awhile, it wouldn't hurt to have
a less time consuming method to parse them built into the language.

I am not that familiar with ODBC, and I'll have to do research on JDBC
(thanks Howard),
but I understand that everything is not ODBC compliant. That is, you
sometimes have to disable the ODBC interception of SQL, and pass it through
unaltered.
>
> DennisHarley wrote:
> >
> > I would like to see support for reading, and writing comma, or tab
delimited
> > files.
> >
…[14 more quoted lines elided]…
> >       ON NUMERIC OVERFLOW [TRUNCATE or ABORT].
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CF87A1.AD07B1F2@zip.com.au>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05>`

```
DennisHarley wrote:
> 
> Since delimited files have been around for awhile, it wouldn't hurt
…[6 more quoted lines elided]…
> interception of SQL, and pass it through unaltered.

Is now a good time to point out that ODBC is a Microsoft interface and
we are talking about mainframe in this thread.

I 100% agree with handling delimited files directly.  we can use
unstring most of the time though.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CF9EC1.3B8D2971@cusys.edu>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05> <38CF87A1.AD07B1F2@zip.com.au>`

```
Ken Foskey wrote:
> 
> Is now a good time to point out that ODBC is a Microsoft interface and
…[3 more quoted lines elided]…
> unstring most of the time though.

We're talking about files which are used to pass data between mainframes
and PCs.

The problem with unstring is in your "most of the time though".  When
your data have unpredictable characters including commas, quotes, and
apostrophes, we have to make our code jump through hoops.  We also have
to explicitly define our numeric data with sign separate or whatever
standard.  This is all bits and bytes stuff, not business rules.

An interfacing standard which handles all of these - and maybe allows
for metadata would be very appreciated - not only by the IS staff, but
by the users who will be offered this interface more often (too often a
programmer provides the printed report which was asked for instead of
the PC data which was wanted).
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

_(reply depth: 6)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OUszudrj$GA.259@cpmsnbbsa04>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05> <38CF87A1.AD07B1F2@zip.com.au> <38CF9EC1.3B8D2971@cusys.edu>`

```

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:38CF9EC1.3B8D2971@cusys.edu...
> Ken Foskey wrote:
> >
> > I 100% agree with handling delimited files directly.  we can use
> > unstring most of the time though.
>
Howard Brazee <howard.brazee@cusys.edu> wrote in message

> We're talking about files which are used to pass data between mainframes
> and PCs.
…[5 more quoted lines elided]…
> standard.  This is all bits and bytes stuff, not business rules.

I have learned something from this thread.
I think that most of the problems we encounter come from using COMMA as the
delimiter.
TAB would be a better choice, since (last I heard) the user cannot enter it
in a text field.

> An interfacing standard which handles all of these - and maybe allows
> for metadata would be very appreciated - not only by the IS staff, but
> by the users who will be offered this interface more often (too often a
> programmer provides the printed report which was asked for instead of
> the PC data which was wanted).

Maybe the FD is the wrong place for this.
Maybe we just need a COBOL Language method for handling standard PC format
delimited strings. Something that does the conversion for us, especially
decimal alignment in numeric input fields.

The metadata issue can be handled by the programmer.
Intentionally format it and write it for output.
Test for it, and either bypass or process it in input.
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D01513.3808198D@home.com>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05> <38CF87A1.AD07B1F2@zip.com.au> <38CF9EC1.3B8D2971@cusys.edu> <OUszudrj$GA.259@cpmsnbbsa04>`

```


DennisHarley wrote:
> 
> Howard Brazee <howard.brazee@cusys.edu> wrote in message
…[21 more quoted lines elided]…
> in a text field.

Not a bad suggestion - but lurking in the back of my mind is the
difference between reading sequential and line sequential if you have
that difference in your compiler. And as very often the user and myself
want to look at the records visually, will the tab spread the display
out into a LONgggggg record  I don't know I've never tried. Certainly a
neutral character is required, if you can hit on one, say colon(:) or
tilde(~). 

But even that doesn't resolve the problem; if you take the approach 
  
	unstring input record
	   my accountnumber delimited by tilde
	   my abc           delimited by tilde etc
           into ....
	End-unstring

You will still go belly-up if you try to move a non-numeric to a
numeric.

'Alien' data, I find I have to check that quotes (") are paired off. And
even where I have generated an ascii delimited to a fixed format, where
the user edits and then resubmits - I don't trust him - he can
inadvertently cause me grief.

Regrettably, I find myself testing (a) for paired quotes and (b) every
incoming 'numeric' field for validity and (c) then moving values field
by field - a real pain in the derriere !

It's a while since I've dabbled with 'alien' formats - but I should also
mention those variations on a theme that come from the PC DB
packages/spreadsheets - the variety of ways a date is expressed - those
damned slashes/obliques (/) don't even give me the chance to use compute
function current-date !

Jimmy
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

_(reply depth: 8)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7BGeKuj$GA.247@cpmsnbbsa03>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05> <38CF87A1.AD07B1F2@zip.com.au> <38CF9EC1.3B8D2971@cusys.edu> <OUszudrj$GA.259@cpmsnbbsa04> <38D01513.3808198D@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:38D01513.3808198D@home.com...
>
>
> DennisHarley wrote:
> >
> > I think that most of the problems we encounter come from using COMMA as
the
> > delimiter.
> > TAB would be a better choice, since (last I heard) the user cannot enter
it
> > in a text field.
>
…[6 more quoted lines elided]…
> tilde(~).

I think that loading the data into a spreadsheet will resolve the tab
problem.
Provided the records are terminated by CRLF, and the volume doesn't exceed
the Spreadsheet maximum row capability.
The other option is to load the data into an empty Access database, and
create a new table.
Just specify TAB delimited, and let the DB figure out the columns.

When doing file transfers from the mainframe to the PC, the most frequently
used option is to create line sequential (insert CRLF at the end of each
line) at the PC end.
When going from the PC to the mainframe the CRLF option will create a
variable length record file on the mainframe end.

The problem with the tilde and colon is that we frequently have old data
which was never filtered, so there may be colons or tildes in the data
itself.

When I create a file on the mainframe to send to the PC, I ALWAYS use a 2
step approach.
1) Create the extract in mainframe format, so I can use File-Aid to review
the data.
2) Convert the extract file to delimited format in a stand alone program.

> But even that doesn't resolve the problem; if you take the approach
>
…[7 more quoted lines elided]…
> numeric.

I find that I use reference modification (n:n?) more often than STRING,
UNSTRING.

> 'Alien' data, I find I have to check that quotes (") are paired off. And
> even where I have generated an ascii delimited to a fixed format, where
> the user edits and then resubmits - I don't trust him - he can
> inadvertently cause me grief.

This is where I think using the TAB may benefit us.
The String is terminated by "TAB or "CRLF , not the " alone.

> Regrettably, I find myself testing (a) for paired quotes and (b) every
> incoming 'numeric' field for validity and (c) then moving values field
> by field - a real pain in the derriere !

This is why I would like to see this whole operation automated.

> It's a while since I've dabbled with 'alien' formats - but I should also
> mention those variations on a theme that come from the PC DB
…[3 more quoted lines elided]…
>
From what I understand tilde presents a problem to Oracle.
I can always reformat a date,
I would just like the tedious part of using delimited files simplified.

Besides files, there is also the possibility of using the format for TCP/IP
communication between mainframe CICS, and desktop GUI user presentations.
```

###### ↳ ↳ ↳ OS/390 COBOL/PC tools communication

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D0E9C6.E4DF3707@cusys.edu>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05> <38CF87A1.AD07B1F2@zip.com.au> <38CF9EC1.3B8D2971@cusys.edu> <OUszudrj$GA.259@cpmsnbbsa04> <38D01513.3808198D@home.com> <e7BGeKuj$GA.247@cpmsnbbsa03>`

```
DennisHarley wrote:
> 
> > Regrettably, I find myself testing (a) for paired quotes and (b) every
…[4 more quoted lines elided]…
> 

Ideally, there should be a small-computer database interface built into
Cobol for communicating with PC tools.  But another solution would be to
create a general-purpose called program or object.  (maybe one for
reading a PC file and the other for writing it (forget the FTP for
now)).

Has anybody created or used such an interface?
```

###### ↳ ↳ ↳ Re: OS/390 COBOL Programmers

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d06183.609935717@news.cox-internet.com>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <u1BdzOej$GA.248@cpmsnbbsa03> <38CE9F95.94E18225@cusys.edu> <udXzEDgj$GA.250@cpmsnbbsa05> <38CF87A1.AD07B1F2@zip.com.au> <38CF9EC1.3B8D2971@cusys.edu> <OUszudrj$GA.259@cpmsnbbsa04> <38D01513.3808198D@home.com>`

```
On Wed, 15 Mar 2000 23:04:15 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Not a bad suggestion - but lurking in the back of my mind is the
>difference between reading sequential and line sequential if you have
…[5 more quoted lines elided]…
>

All of the imports I have looked at can handle embedded comma within
the fields if the non numeric fields are enclosed in quotation marks.


Here's how I handle it.

String Quote Field1 X"FFFFFF" field2 X"FFFFFF" field3 X"FFFFFF" field4
X"FFFFFF" field5 quote delimited by size into string-destination

Inspect string-destination replacing all X"FFFFFF" by '","'

You end up with a nice little output.

Now the only other thing you could do is to determine the significant
lenght of each of the fields and use that in counters with reference
mod for the string ot give you that "trimmed" look.

For the reverse I always replace the '","' with high-values, unstring
delimited by high values, then kill the leading quote from the first
field and the trailing quote from the last.

If there are embedded numeric fields without quotes you have a problem
-- but even this can be coded for with relative ease-- but most
packages will make a "comma/quote" delimited file that has quotes
around all fields.
```

#### ↳ Re: OS/390 COBOL Programmers

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FF8AB8.BB1FACEC@istar.ca>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com>`

```
I suspect that many of the COBOL programmers are doing it a way station
on the corporate ladder, not as a career.  Further the management
attitude is that they should work with what they have and no provision
is made for them to influence the vendor or the standard.  My belief is
that if companies had put minimal effort into defining what they needed
in a business language and working to get it, we would not have the
proliferation of proprietary languages such as DYL280.  

In terms of getting improvements and the business case for those
improvements, my belief is that one of the priorities is anything that
allows us to use existing tools written in other languages.  That means
data types recognized by C/C++ programs along with the calling
conventions for them, object oriented syntax that allows
interoperability with standard class libraries written in other
languages and more generalization of existing structures.  We will have
to be able to handle the double byte character sets, especially Unicode
and the multi-byte superset ISO 10646, XML, and locale sensitive field
comparisons.  This last will be a performance hog even for English let
alone some of the Latin and Germanic languages where there are two
different ways of representing the same accented letter of the alphabet
(see the Unicode standard for mind numbing details).

In addition I would like to see the FD interface enhanced such that the
same select statement and FD can be used to access a true flat file, an
indexed file where the sequence is assumed to be that of the primary
keys, a relational database view where the sequence is implied in the
view or any other data entity where records could be logically read or
written using the information in the SELECT and FD.  This could include
accessing a screen where the glue that connects the file to the screen
also takes care of any data transformations.  The Guide/SHARE Language
Futures Task Force implicitly asked for this in their final report
published in 1984.  

Lastly, I believe that packages are becoming more important because of
the large cost of designing and maintaining systems.  Thus the software
developers will have to make known their needs to the various vendors in
a way that conveys to those vendors the fact that this also affects many
customers of that vendor besides the developer.  

Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.ca        

S Comstock wrote:
> 
> Hi,
…[42 more quoted lines elided]…
> USA
```

##### ↳ ↳ Re: OS/390 COBOL Programmers

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FFD5F2.274D9BFF@home.com>`
- **References:** `<20000313095137.22475.00000615@ng-cn1.aol.com> <38FF8AB8.BB1FACEC@istar.ca>`

```


"Clark F. Morris, Jr." wrote:
> 
> I suspect that many of the COBOL programmers are doing it a way station
…[20 more quoted lines elided]…
>
Clark,
 
I can appreciate the Unicode bit is a real problem. But as to accessing
classes from other languages - now that's real intriguing. Look what we
would eventually get from the 'Open' Linux classes concept.

> In addition I would like to see the FD interface enhanced such that the
> same select statement and FD can be used to access a true flat file, an
…[7 more quoted lines elided]…
> published in 1984.

I take it what you are after here is a 'common COBOL handle' to any DB -
possibly a class or sub-routine per DB package - that makes sense to me.
(Not using them I don't know what difficulties people run into, but at
the PC level I see so many queries relating to 'talking' to DBs).

> 
> Lastly, I believe that packages are becoming more important because of
…[3 more quoted lines elided]…
> customers of that vendor besides the developer.

Your last statement, you are echoing a theme - pass you thoughts on to
Ed Arranga at cobolreport.com., ( 74651.2630@compuserve.com) - and see
him jump up and down !!!

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
