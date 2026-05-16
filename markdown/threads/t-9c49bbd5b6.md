[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL - compile-time messages and documentation

_9 messages · 8 participants · 1999-04 → 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL - compile-time messages and documentation

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
There have been some comments about compile-time messages in the IBM-MAIN
list server recently.  I put out the following post there - but would also
be interested in input from comp.lang.cobol people as well.

NOTE WELL:
    This is intended as an IBM compiler "survey" only.  There are very
different (but related?) issues for other compilers and their messages - and
documentation.

   ***

There have been comments in several threads recently about the lack of an
<IBM> COBOL compile-time "messages and codes" manual.  I now understand (but
didn't originally) that what people WANT is a manual that says,

  "If you receive message xyz, then the probable causes are 1, 2, and 3, -
and the best way to resolve these are to take steps a, b, can c."

As has also been pointed out IBM's stated (public) position is that ALL
compile-time messages are "self documenting" and that there is nothing more
that they can/should put into a separate manual.

Now for my question(s) - to better understand the issue(s):

1) Do you think there is a difference between the current COBOLs (either VS
COBOL II or COBOL for this-and-that) versus the older OS/VS COBOL or DOS/VS
COBOL compilers?  In other words, do you think there ever was such a
manual - or do you think that the old messages were clearer than the new
ones?  OR do you think that this isn't a new problem - but just one that is
still aggravating and seems to be more visible because your programmers
aren't used to the new COBOL compilers?

2) When your programmers have problems with some of the messages, do these
same programmers have access to the LRM (Language Reference Manual) - but
still can't figure out the message(s)?  If they have access, is it to the
hard-copy or soft-copy versions of the manuals?

If it is hard-copy, is this their own "personal" copy of the LRM - or one
that is shared with others in their group or from a common library?

3)  Can you give me (private email is OK - or public if you prefer - but I
don't know how much of IBM-MAIN is interested in this) some examples of the
messages that cause your programmers problems?  Particularly, if there are
specific messages that seem to come up frequently - I would be interested in
them.  (I will probably share these with IBM - but if you don't want me to,
please let me know.)

  ***

Thanks in advance. I hope that if this "problem" gets clearer, a better
solution may be made possible.
```

#### ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370BA562.4674421E@NOSPAMhome.com>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
> As has also been pointed out IBM's stated (public) position is that ALL
> compile-time messages are "self documenting" and that there is nothing more
> that they can/should put into a separate manual.

I have often found that I get a message with a one line message, so I
look it up in a big manual and significantly no more information.
```

#### ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ega0c$l0c$1@news.igs.net>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
William M. Klein wrote in message <7eg2ra$84s@sjx-ixn9.ix.netcom.com>...
<Large snippage regarding error messages>

I have though for a long time that *all* the compiler writers need to do a
lot of catch up.

I very typical situation:  The compile gives out cryptic and short error
messages, with an error number. This is to save memory/disk space.  The
manual writer takes all the references from paper and converts them to a
machine readable a lookup table. If you are lucky, they are in the help
system, but they probably get printed from a web site. They in turn refer to
the *big* manual to save in memory and disk.  The writer of the big manual
converts everything to machine readable, and cross references the paper
table (that does not exist any more) to that reference manual.

To correct this huge mess, a new help system is written, and a separate
scanning program is written to read the manual.  So.  I get an error.  I go
into the help system to see what the error message means. After that, I then
go into the reference system to find out what to do about it, using yet a
third piece of software.

Integrating the error messages, the error lookup tables, the online help
manuals, and the manuals would probably do more for the language than all
the GUI work done so far.
```

#### ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eVgnj8Sg#GA.266@nih2naab.prod2.compuserve.com>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
I thought there was such a manual, or at least a chapter in most user
guides or programmer's guides or somewhere. Anyway, I often find that
making intelligent use of compiler options produces enough information to
understand the problem, especially if information available before was too
short or cryptic.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

#### ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370C8FFD.A2EF3D44@zip.com.au>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
I have just moved companies and in my old company I had a personal copy
of the CD's from IBM.  In my new one they have set up an MVS web server
and put on the CICS and DB2 manuals but no Cobol manual (despite
repeated requests).

For compile time the messages are self explanitory (mostly) the
unreachable code does still occur but only under optimise. Quite handy
to check for these occasionally.

The run time, these messages are sometimes a little obscure.  Once you
have seen the first they are easy to work out though.  The problem here
is that they abend with a USER code 4038.  This leads programmers to
look for user errors in the code.

Ken
```

#### ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370C63E3.235AC743@worldnet.att.net>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
William M. Klein wrote:  (some snipping here)
> 
> Now for my question(s) - to better understand the issue(s):
…[7 more quoted lines elided]…
> aren't used to the new COBOL compilers?

I've never seen an IBM manual that explains what action the programmer
should take for a specific compiler diagnostic message in the way you
described.  In general, I believe those messages are self-documenting,
with a few exceptions.  The messages are different for compilers prior
to COBOL II.  I don't think this is a new problem, but I would agree
that some programmers just aren't used to the newer IBM COBOL compilers.

> 
> 2) When your programmers have problems with some of the messages, do these
…[5 more quoted lines elided]…
> that is shared with others in their group or from a common library?

Access to manuals is a problem.  We have some COBOL II LRM's.  I
jealously guard mine, but some programmers have no access, or there may
be one or two per development team.
Where I work, programmers also have access to TSO Book-Mangler and
Library Reader for Windows but don't seem to be able to use these
reference materials effectively.

We have COBOL for MVS and VM, and we're starting to use it, but we have
no hardcopy LRM, and Book-Mangler/Library Reader for Windows is the only
source of information.
 
> 
> 3)  Can you give me (private email is OK - or public if you prefer - but I
…[4 more quoted lines elided]…
> please let me know.)

There was one message in COBOL II that threw me for a loop when I first
saw it.  Within the last six months I received a panicky call about the
very same message from a programmer just learning COBOL II.  I don't
have the exact text with me, but the message was a warning generated by
the optimizer.  It tried to explain that a subroutine had been moved
inline, but then contained dead code which was removed.  The dead code
was a conditional statement where a path could not be taken based on the
data values in the inline context.  That's hard to explain on one line. 
The exact phrase that panicked the programmer was something about "code
that could not be reached".

I'm still a little irritated that COBOL II and higher will not link if a
period is missing, in a context where it OS/VS COBOL simply issued a
warning and moved on.

In my experience, programmers just now starting to use COBOL II or COBOL
for MVS and VM have the most problems with subprograms, or mixing NORES
OS/VS COBOL with RES COBOL II, or with options related to NUMPROC and
AMODE/RMODE considerations.  If they're trying out intrinsic functions
they don't have the LRM and don't know when COMPUTE is required or MOVE
is allowed.  They don't seem to have many problems with the compiler
diagnostic messages.
```

#### ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gt7er$864$1@news.ses.cio.eds.com>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com>`

```
For new programmers, such a book would be an invaluable resource,
saving weeks of wasted time trying to figure out what all the error
messages are.

They are not, in any way, self-documenting (except to those who
already know what they mean), since many errors are often caused by
problems unrelated to the line on which the error occurs.  "Code on
line xxx can never be executed and was therefore discarded," really
means that the data-items on the IF statement surrounding the code
cannot be properly compared.  But to read that message you would think
there is a problem right there, not back up in the Data Division.

I've figured out what the majority of the error messages mean, and
because I'm familiar and comfortable with them, I can figure out new
ones without too much difficulty.  My question is, why should there be
any difficult at all?  I've started a Word document that contains a
list of all ABENDs codes my programs take, and why, and how I solved
it.  This way, I never have to reinvent the wheel of discovery a year
down the road.  I haven't thought to put compiler error messages in
it, but after this I will.  I regularly email this document to a
circle of friends much newer to programming than I, they like it and
say it saves them time.  I doubt it will go farther then that, as I'm
not technical enough with some of it, and a get the feeling a couple
of my conclusion may have been wrong, but I just don't have enough
information.  Why don't I?  Because there is no decent compiler/abend
diagnostic manual.

There was a book written about this subject several years ago, going
by the title Application Program Debugging under MVS: COBOL and COBOL
II.  It's out of print though, and I haven't been able to find it.


William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7eg2ra$84s@sjx-ixn9.ix.netcom.com...
> There have been some comments about compile-time messages in the
IBM-MAIN
> list server recently.  I put out the following post there - but
would also
> be interested in input from comp.lang.cobol people as well.
>
> NOTE WELL:
>     This is intended as an IBM compiler "survey" only.  There are
very
> different (but related?) issues for other compilers and their
messages - and
> documentation.
>
>    ***
>
> There have been comments in several threads recently about the lack
of an
> <IBM> COBOL compile-time "messages and codes" manual.  I now
understand (but
> didn't originally) that what people WANT is a manual that says,
>
>   "If you receive message xyz, then the probable causes are 1, 2,
and 3, -
> and the best way to resolve these are to take steps a, b, can c."
>
> As has also been pointed out IBM's stated (public) position is that
ALL
> compile-time messages are "self documenting" and that there is
nothing more
> that they can/should put into a separate manual.
>
> Now for my question(s) - to better understand the issue(s):
>
> 1) Do you think there is a difference between the current COBOLs
(either VS
> COBOL II or COBOL for this-and-that) versus the older OS/VS COBOL or
DOS/VS
> COBOL compilers?  In other words, do you think there ever was such a
> manual - or do you think that the old messages were clearer than the
new
> ones?  OR do you think that this isn't a new problem - but just one
that is
> still aggravating and seems to be more visible because your
programmers
> aren't used to the new COBOL compilers?
>
> 2) When your programmers have problems with some of the messages, do
these
> same programmers have access to the LRM (Language Reference
Manual) - but
> still can't figure out the message(s)?  If they have access, is it
to the
> hard-copy or soft-copy versions of the manuals?
>
> If it is hard-copy, is this their own "personal" copy of the LRM -
or one
> that is shared with others in their group or from a common library?
>
> 3)  Can you give me (private email is OK - or public if you prefer -
but I
> don't know how much of IBM-MAIN is interested in this) some examples
of the
> messages that cause your programmers problems?  Particularly, if
there are
> specific messages that seem to come up frequently - I would be
interested in
> them.  (I will probably share these with IBM - but if you don't want
me to,
> please let me know.)
>
>   ***
>
> Thanks in advance. I hope that if this "problem" gets clearer, a
better
> solution may be made possible.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-05-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gtrv2$g27@dfw-ixnews12.ix.netcom.com>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com> <7gt7er$864$1@news.ses.cio.eds.com>`

```
Chris,
  I thought that this thread had died out.  I am interested in your
comments - but will admit that they seem to be a "bit" in the minority (but
certainly not unique).  Personally, I would prefer to teach a "new"
programmer HOW to resolve the messages they are getting - rather than giving
them a cookbook that probably is misleading (in at least some cases).  For
example, I think that the message that you mentioned (about code being
discarded) can teach a programmer a couple of things:

1) Learn the differences between I- and W-level messages - versus more
severe ones. (This is a W-level message as I recall.)

2) I wouldn't agree with you that it is usually a data division problem, but
then again it DOES take looking at your specific code for ANY message that
you get.

I am CC'ing my IBM contacts on this note (to convey your input) but
personally, I am not yet convinced that any manual would really help in most
cases (and certainly not in the one you mention).
```

###### ↳ ↳ ↳ Re: IBM COBOL - compile-time messages and documentation

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gutho$88t$1@news.ses.cio.eds.com>`
- **References:** `<7eg2ra$84s@sjx-ixn9.ix.netcom.com> <7gt7er$864$1@news.ses.cio.eds.com> <7gtrv2$g27@dfw-ixnews12.ix.netcom.com>`

```
William,

Yes, I saw the month old date, but I was having trouble with my news
server and couldn't always review old messages or post responses to
them.  There were several other old threads I didn't post to, but this
one I couldn't resist.

All right, I'll admit it, having to figure out what every error
message meant with no help at all (no one to ask, in my case), did
help me.  But it also took, in some cases, a day or two to figure out
what they meant (when your inexperienced, sometimes more than one
thing can be affecting what you're doing, causing some problems to
become harder to solve).

I'm forced to concede that compiler errors are easier to solve than
logic errors, and for that there is no fixed set of information
available to solve problems, only general techniques.


Sincerely,
    Chris Osborne



William M. Klein <wmklein@inospam.netcom.com> wrote in message
news:7gtrv2$g27@dfw-ixnews12.ix.netcom.com...
> Chris,
>   I thought that this thread had died out.  I am interested in your
> comments - but will admit that they seem to be a "bit" in the
minority (but
> certainly not unique).  Personally, I would prefer to teach a "new"
> programmer HOW to resolve the messages they are getting - rather
than giving
> them a cookbook that probably is misleading (in at least some
cases).  For
> example, I think that the message that you mentioned (about code
being
> discarded) can teach a programmer a couple of things:
>
> 1) Learn the differences between I- and W-level messages - versus
more
> severe ones. (This is a W-level message as I recall.)
>
> 2) I wouldn't agree with you that it is usually a data division
problem, but
> then again it DOES take looking at your specific code for ANY
message that
> you get.
>
> I am CC'ing my IBM contacts on this note (to convey your input) but
> personally, I am not yet convinced that any manual would really help
in most
> cases (and certainly not in the one you mention).
>
> --
> Bill Klein (wmklein at ix dot netcom dot com)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
