[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interesting Date Routine

_41 messages · 27 participants · 2000-08 → 2000-09_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### Interesting Date Routine

- **From:** "Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com>
- **Date:** 2000-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
(although I don't believe it's still available)

Here is an interesting date routine that was found while changing legacy
systems
for the Year 2000.

             01  DATE1  PIC 9(6).
             01  DATE2  PIC 9(6).
             ...
             COMPUTE DATE2 = DATE1 * 100.0001.

What does it do?
It converts a date in the form YYMMDD to a date with the form MMDDYY. For
example, if DATE1 = 961204, then multiplying by 100.0001 gives
96120496.1204. By
moving this to a PIC 9(6) field, the first 2 bytes and the last four after
the
decimal are dropped, leaving 120496.
```

#### ↳ Re: Interesting Date Routine

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nahcm$2voq$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```

You mean like COMPUTE DATE1 = DATE2 * 10000.01?!

Lincoln Duncan <NotOnSite*NOSPAM*@Yahoo.com> wrote in message
news:sph8l3o8kn9102@corp.supernews.com...
> Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
> (although I don't believe it's still available)
…[18 more quoted lines elided]…
>
```

#### ↳ Re: Interesting Date Routine

- **From:** jacksleight@my-deja.com
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nbcdg$2g1$1@nnrp1.deja.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Very nice guys. Thanx.

Jack


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Interesting Date Routine

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39994046.F47ACE21@brazee.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
That code is interesting and fun.  But I would never use it in a COBOL program
today.  A primary aspect of COBOL is that it is supposed to be clear and
unambiguous, making maintenance easy.

I am such a proponent of COBOL, that I wouldn't even use it in C, trying to
make C maintainable as well.

I suppose it could be used within a hidden object, but only after showing that
it provided sufficient efficiency gains over more obvious code.  But does
anybody make code as simple as what this is supposed to do into an object?

Thanks though for sharing - as I said, it is fun code.

Lincoln Duncan wrote:

> Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
> (although I don't believe it's still available)
…[16 more quoted lines elided]…
> decimal are dropped, leaving 120496.
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ncvff$1vm8$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <39994046.F47ACE21@brazee.net>`

```

What is "unclear" about the following?
05  W-YYMMDD  PIC  9(6).
05  W-MMDDYY  PIC  9(6).
ACCEPT   W-YYMMDD  FROM DATE
MULTIPLY W-YYMMDD  BY 100.0001  GIVING W-MMDDYY
.

Howard Brazee <howard@brazee.net> wrote in message
news:39994046.F47ACE21@brazee.net...
> That code is interesting and fun.  But I would never use it in a COBOL
program
> today.  A primary aspect of COBOL is that it is supposed to be clear and
> unambiguous, making maintenance easy.
>
> I am such a proponent of COBOL, that I wouldn't even use it in C, trying
to
> make C maintainable as well.
>
> I suppose it could be used within a hidden object, but only after showing
that
> it provided sufficient efficiency gains over more obvious code.  But does
> anybody make code as simple as what this is supposed to do into an object?
>
> Thanks though for sharing - as I said, it is fun code.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399A9431.982F875E@brazee.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <39994046.F47ACE21@brazee.net> <8ncvff$1vm8$1@newssvr05-en0.news.prodigy.com>`

```

Terry Heinze wrote:

> What is "unclear" about the following?
> 05  W-YYMMDD  PIC  9(6).
…[3 more quoted lines elided]…
> .

Let's say one mess up - maybe putting in the wrong number of zeros.  (one of the
first responses in this thread questioned that).  This is not obvious to the
maintenance programmer who is accepting upon face value that this algorithm is
working.  He has to get out a pencil and paper to check to see if this works
correctly.  Or worse - maybe overflow to work differently when ported to a new
computer, compiler, or compiler switch .  It wouldn't be obvious or clear what
the problem is.

The INTENT is pretty obvious.  But the mechanism isn't so obvious.
```

#### ↳ Re: Interesting Date Routine

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3999482C.B83E5086@zip.com.au>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Lincoln Duncan wrote:
> 
> Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
…[14 more quoted lines elided]…
> last four after the decimal are dropped, leaving 120496.

This is clever code,  the problem is clever code is hard to work out.

In most systems three moves will out perform a multiplication so KISS.

Any one for obfuscated cobol contest (sorry COBOL!!!).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** "Erlend Moen" <erlend.moen@disys.no>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nbihu$3ak$1@oslo-nntp.eunet.no>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> skrev i news:3999482C.B83E5086@zip.com.au
>
> This is clever code,  the problem is clever code is hard to work out.
…[3 more quoted lines elided]…
> Any one for obfuscated cobol contest (sorry COBOL!!!).

How 'bout converting from yymmdd to ddmmyy? Anyone?

<-emo->
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

- **From:** einomoto@compuserve.com (Edmond J. Inomoto)
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00000715105525.OUI08.einomoto@compuserve.com>`
- **References:** `<3999482C.B83E5086@zip.com.au> <8nbihu$3ak$1@oslo-nntp.eunet.no>`

```
On August 15 2000, "Erlend Moen" <erlend.moen@disys.no> wrote:

>> Ken Foskey <waratah@zip.com.au> skrev i 
>> news:3999482C.B83E5086@zip.com.au
…[10 more quoted lines elided]…
> <-emo->

These should work:

COMPUTE DATE-YMD = DATE-MDY * 10000.01

COMPUTE DATE-MDY = DATE-YMD * 100.0001

where all dates are 6-digits. Although all my base dates are now
Y2K-compliant, I use these routines to format 6-digit report & screen
dates, e.g. 08/15/00. (These calculations are restricted to a single
subprogram, BTW).
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t4jm5.41$nj6.41538@nnrp3.sbc.net>`
- **References:** `<3999482C.B83E5086@zip.com.au> <8nbihu$3ak$1@oslo-nntp.eunet.no> <00000715105525.OUI08.einomoto@compuserve.com>`

```

"Edmond J. Inomoto" <
> >
> > How 'bout converting from yymmdd to ddmmyy? Anyone?

> These should work:
>
…[3 more quoted lines elided]…
>

Geeze!

How about DATE-YMD = FUNCTION REVERSE (DATE-DMY).
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ncf6q$efc$1@nntp9.atl.mindspring.net>`
- **References:** `<3999482C.B83E5086@zip.com.au> <8nbihu$3ak$1@oslo-nntp.eunet.no> <00000715105525.OUI08.einomoto@compuserve.com> <t4jm5.41$nj6.41538@nnrp3.sbc.net>`

```
Some how, I don't think that will work.  I really don't think that I want a
month of "05" reversed to "50" - much less a day of "31" changed to "13". <G>
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7kn5.72$Mg4.65884@nnrp1.sbc.net>`
- **References:** `<3999482C.B83E5086@zip.com.au> <8nbihu$3ak$1@oslo-nntp.eunet.no> <00000715105525.OUI08.einomoto@compuserve.com> <t4jm5.41$nj6.41538@nnrp3.sbc.net> <8ncf6q$efc$1@nntp9.atl.mindspring.net>`

```
This was just a hint. I left the details - which should be clear to
the most casual observer - as an exercise for the reader.

But, in the interest of clarity, the full code would be:

MOVE FUNCTION REVERSE(DATE-DMY) TO DATE-YMD.
MOVE FUNCTION REVERSE(DATE-YMD-YY) TO DATE-YMD-YY.
MOVE FUNCTION REVERSE(DATE-YMD-MM) TO DATE-YMD-MM.
MOVE FUNCTION REVERSE(DATE-YMD-DD) TO DATE-YMD-DD.

I thought I did pretty well, extricating myself from that pickle, all
things considered.



"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:8ncf6q$efc$1@nntp9.atl.mindspring.net...

> Some how, I don't think that will work.  I really don't think that I
want a
> month of "05" reversed to "50" - much less a day of "31" changed to
"13". <G>

> > Geeze!
> >
> > How about DATE-YMD = FUNCTION REVERSE (DATE-DMY).
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-08-16T04:31:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399A188D.5C1E24FC@worldnet.att.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au>`

```
Ken Foskey wrote:
> 
> Lincoln Duncan wrote:
…[16 more quoted lines elided]…
> > last four after the decimal are dropped, leaving 120496.

This technique was discussed in detail in comp.software.year-2000 two or
three years ago, and the general consensus was that it was "a bad
idea".  Any good Y2K scanner should flag arithmetic performed on a date
field, and this "Look at me! I'm a programmer!" code is difficult to
convert to 4-digit years.
 
> 
> This is clever code,  the problem is clever code is hard to work out.
…[3 more quoted lines elided]…
> Any one for obfuscated cobol contest (sorry COBOL!!!).

Listen to Ken.  He knows what he's talking about.

I compiled both methods for reformatting the date in a single VS COBOL
II program, and generated the disassembled code.  The calculation method
generated 28 bytes of instructions including PACK, MULTIPLY, and
UNPACK.  The MOVE version generated two six-byte MVC instructions,
because the optimizer was able to condense two moves of adjacent fields
into a single assembler instruction.  

I thought the performance penalty would be much higher.  I had assumed
the compiler would generate a call to a runtime library routine.

I saw several programs that subtracted 1 from year 00 and stored it in a
PIC 99 field, and the results might surprise you.

I've also seen this in a program: 

05  MY-YEAR   PIC 99  VALUE ZEROS.

IF MY-YEAR + 1 = ZERO
    do something because next year is 2000
ELSE
    don't worry, it's not Y2K yet
END-IF.

The above example FAILED in VS COBOL II, because the expression (MY-YEAR
+ 1) evaluted to an intermediate field that did NOT have a PIC 99
definition, and 100 is definitely NOT equal to zero!  That one took a
while to debug.

I've also seen division performed on a date, but the less said about
that, the better.
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** Fred Young <fred@perfectcircle.com>
- **Date:** 2000-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399C9CB3.C3E2FC43@perfectcircle.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au>`

```


Ken Foskey wrote:

> > example, if DATE1 = 961204, then multiplying by 100.0001 gives
> > 96120496.1204. By  moving this to a PIC 9(6) field, the first 2 bytes and the
> > last four after the decimal are dropped, leaving 120496.
>
> This is clever code,  the problem is clever code is hard to work out.

Ken is right on, Clear beats Clever every time.

>
>
…[9 more quoted lines elided]…
> http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

- **From:** Thomas <thomas@inorbit.com>
- **Date:** 2000-08-18T06:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nil57$tqo$1@nnrp1.deja.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com>`

```
In article <399C9CB3.C3E2FC43@perfectcircle.com>,
  Fred Young <fred@perfectcircle.com> wrote:
>
>
…[3 more quoted lines elided]…
> > > 96120496.1204. By  moving this to a PIC 9(6) field, the first 2
bytes and the
> > > last four after the decimal are dropped, leaving 120496.
> >
> > This is clever code,  the problem is clever code is hard to work
out.
>
> Ken is right on, Clear beats Clever every time.
>

Yow. As much of a fan as I am for Clear over Clever, I can't possibly
agree with "every time." Nit-picking, sure; but I'm not even sure of a
two-thirds majority.  :-)

A definite example might be an encryption scheme. There might be any
number of reasons why I'd choose Clever over Clear.

Just for the sake of discussion...

Tom Liotta

> >
> >
> > In most systems three moves will out perform a multiplication so
KISS.
> >
> > Any one for obfuscated cobol contest (sorry COBOL!!!).
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 4)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zPhn5.629$%O6.33852@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com> <8nil57$tqo$1@nnrp1.deja.com>`

```
So the obscure is better than clear .... sometimes in the minds of many.

You have hit upon one of the major reasons the CODASYL effort was formed.
Up until then, clever was restricted to methods of using UNIT
RECORD equipment by tricking the machines to do things not otherwise
possible.  Since many of the "responsible" people had worked with unit
record equipment, they did NOT feel concerned about the "techniques" in use
in the card shop.  After five years of converting this kind of operation to
a tape computer system, many people in management found that they no longer
understood what was being done, and were threatened by the outcome of their
decisions.  They made commitments to upper management based upon their own
experience which was outdated.  Some got hung out to dry, and decided there
needed to be some "clarification" to this new "programmer" job title.
COBOL was born largely from that decision to avoid making the same mistake
"next time."

Yet, even today, many of the people in responsible positions are unaware of
the consequences of their decisions to follow one path or another and rely
on the newbies who what to follow their own agenda.

Of course the above represents my own opinion, and does not reflect the
ideas or opinions of others unless they say so.

Keep it simple (stupid).

Warren Simmons

"Thomas" <thomas@inorbit.com> wrote in message
news:8nil57$tqo$1@nnrp1.deja.com...
> In article <399C9CB3.C3E2FC43@perfectcircle.com>,
>   Fred Young <fred@perfectcircle.com> wrote:
…[50 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-08-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FaQn5.120$p36.16264@news2.mia>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com> <8nil57$tqo$1@nnrp1.deja.com> <zPhn5.629$%O6.33852@bgtnsc05-news.ops.worldnet.att.net>`

```
"Warren Simmons" wrote:
> So the obscure is better than clear .... sometimes in the minds of many.
>  [snip]
> Keep it simple (stupid).

Warren, I think most of the experienced programmers here would agree
with you on KISS, I do.  Not very often, but occasionally I encounter
a situation where performance is more important than clarity, though
I still try to make it as clear as possible, within the performance
constraints.  This is not just in very high performance code, it can
also be found where the simple and clear solution runs for several
hours, but a clever and subtle solution runs for 10 minutes.  More
frequently, I encounter problems so complex, they simply cannot be
made 'simple'.  Years ago, one of my clients asked me to rewrite some
report programs.  The reports were very complex, each with a number of
different types of data reported in different sections of the report,
with varying control breaks, both across the page and down the page.
The old reports had been hard coded with fixed columns across the page
for each horizontal control break.  The problem was, the number of
possible horizontal columns, which varied day to day, was about to
exceed the page width.  They wanted the program to automatically
overflow the columns to additional pages, such that the entire
report would print the leftmost columns, followed by the entire report
again with the columns just to the right, and so forth.  Sometimes
there would be one pass, sometimes two or more, depending on the data.
There were perhaps 15 to 20 sections of the reports, some could
overflow and others didn't expand across the page.  My solution was
to create a table driven kernel that provided the above capability,
which was used by each report section that used the control break
across the page format.  The programs first made a 'preview pass'
through the data to 'simulate' the report, to see how many passes
would be required.  Then, on each pass, it was necessary to keep up
with how many lines would be printed on the leftmost pass, so the
horizontal columns would be adjacent when the report passes were
laid side by side.  Believe me, this kernel was extremely complex
and subtle.  However, by careful design, it should would perhaps
never need any modifications.  It was (and has been for 15+ years)
flexible enough to accommodate any changes necessary by changing the
tables, and modifying the data being passed to it, which is not
difficult.  Looking back, I still can't see a better approach, and
I have had reason to use a somewhat simplified version of that
approach in similar situations.  I believe that sometimes complex
and subtle is best, or even necessary, though not very often.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 6)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PJUn5.19508$4T.1177934@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com> <8nil57$tqo$1@nnrp1.deja.com> <zPhn5.629$%O6.33852@bgtnsc05-news.ops.worldnet.att.net> <FaQn5.120$p36.16264@news2.mia>`

```
It's true that generalization is sometimes over statement. KISS is NOT the
only way.  Certainly, there are applications or conditions that require
methods that confound most people. They may have a method to there madness.

When dealing with the Unit Record class of automation of procedures, many
seemingly unnecessary steps and methods are used.  Often these are
necessary to the solution.

In these times some firms are able to fund the "invention" of methods that
overcome some of the owcquired things people had to do to keep it simple.

With computer based systems, the key, in my experience is one thing, I-O
time. Most of the computing can be done concurrently with the I-O time.
Soooo..
Reading a file twice to avoid complicated procedures is not unheard of as
is doing more than one sort to create reports for one purpose.  If we spent
time reviewing all of the things people remember doing, and can think of
that they have heard about, we might come up with some new "functions" or
tool terms that would simplify our description of the process.
These terms crop up all of the time when new solutions based upon computer
application surface.

I'm still not sure I know everything my SPFPC program provides in function,
and I once taught others the SPF features.

When I try to use photographic type systems I'm hampered because of a lack
of background in the subject.

I feel that many solutions devised that are complex are that way because
the simple solution has not been devised or invented.  Which leads me to
the requirements of reports.

People who specify the output layout of the data they want to see, and how
it should be presented sometimes have little idea of the impact or for that
matter end use of the data.

Now days, it seems that a http page can do everything we need.  Who knew?

EOTOBS

Warren Simmons
"Judson McClendon" <judmc@bellsouth.net> wrote in message
news:FaQn5.120$p36.16264@news2.mia...
> "Warren Simmons" wrote:
> > So the obscure is better than clear .... sometimes in the minds of
many.
> >  [snip]
> > Keep it simple (stupid).
…[45 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-08-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FH9o5.1818$p36.428690@news2.mia>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com> <8nil57$tqo$1@nnrp1.deja.com> <zPhn5.629$%O6.33852@bgtnsc05-news.ops.worldnet.att.net> <FaQn5.120$p36.16264@news2.mia> <PJUn5.19508$4T.1177934@bgtnsc07-news.ops.worldnet.att.net>`

```
"Warren Simmons" <warren.simmons@worldnet.att.net> wrote:
>
> I feel that many solutions devised that are complex are that way because
> the simple solution has not been devised or invented.

I completely agree.  When I am designing or redesigning a system, one
of the things I always try to do is to back off from what the user is
specifically requesting, so that I, and hopefully they, can view the
actual requirements behind the requests.  Often it is difficult to get
a user to do this, particularly if they have used an old system for a
long time.  It helps if they can think 'out of the box', or can come
to trust you.  Very often users request some function that turns out
to be a policy set 'way back to accommodate some situation that no
longer exists, or can be made unnecessary by good design.  I always
try go get a grasp of the fundamental principles driving the system.
It is my experience that when you do this well, it results in a more
flexible, robust, and simpler, design.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 8)_

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-08-23T01:09:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39a32429.37329373@news1.frb.gov>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com> <8nil57$tqo$1@nnrp1.deja.com> <zPhn5.629$%O6.33852@bgtnsc05-news.ops.worldnet.att.net> <FaQn5.120$p36.16264@news2.mia> <PJUn5.19508$4T.1177934@bgtnsc07-news.ops.worldnet.att.net> <FH9o5.1818$p36.428690@news2.mia>`

```
On Mon, 21 Aug 2000 07:58:30 -0500, Judson McClendon wrote:

>When I am designing or redesigning a system, one
>of the things I always try to do is to back off from what the user is
>specifically requesting, so that I, and hopefully they, can view the
>actual requirements behind the requests.  
[...]
>It helps if they can think 'out of the box', or can come
>to trust you.  
[...]
>It is my experience that when you do this well, it results in a more
>flexible, robust, and simpler, design.

It may also result in a solution that meets the user's actual (as
opposed to stated) requirements.

It might even result in less finger-pointing ("You should have known
what I meant.") and in less doing things over again (and again).
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 6)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-09-07T23:23:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p9m4a0rpn@enews1.newsguy.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <3999482C.B83E5086@zip.com.au> <399C9CB3.C3E2FC43@perfectcircle.com> <8nil57$tqo$1@nnrp1.deja.com> <zPhn5.629$%O6.33852@bgtnsc05-news.ops.worldnet.att.net> <FaQn5.120$p36.16264@news2.mia>`

```
Yes, and Production Control folks don't want stuff sitting in their 
execution queue for hours either.

Clever is not mutually exclusive of Clear.  A Clever solution does not need
to be Complex.  I understand what you are saying about that report and
creating trick code is certainly satisying.  Sometimes little things, clever
things, can do a lot of good too, like changing a SEARCH to a SEARCH ALL for
a big table or putting buffers on a heavily accessed VSAM file.  There are
tons of other things that are Clever and Clear.

Good code should really never need to be modified.  This is sort of like
encapsulation.  The only 2 reasons why a program needs to be modified is
either there is a bug or it needs to be enhanced.

If that is true, then the only reason to modify a program is for
enhancement.

A very good programmer will write it bug free the first time.  A good
programmer may get a few calls or questions.  An average programmer will
need help or at least advice, and all other programmers wouldn't even have
gotten the task.

OK, time for bed.

Jeff



----------
In article <FaQn5.120$p36.16264@news2.mia>, "Judson McClendon"
<judmc@bellsouth.net> wrote:


> "Warren Simmons" wrote:
>> So the obscure is better than clear .... sometimes in the minds of many.
…[47 more quoted lines elided]…
>
```

#### ↳ Re: Interesting Date Routine

- **From:** Jonathan Ball <jonball_NS@earthlink.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<399968B6.86C45F2C@earthlink.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Lincoln Duncan wrote:
> 
> Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
…[17 more quoted lines elided]…
> decimal are dropped, leaving 120496.

This routine, and a related one - multiply a MMDDYY date by 10000.01 to
yield YYMMDD - have been around in RPG at least since the 1970s.  I
first encountered them on the System/38 in RPG II and RPG III in 1982. 
You still can find them all over in AS/400 shops.  I have never seen it
used in COBOL.

It is discouraged for one reason already mentioned in other replies to
the original post - lack of clarity (although the practice is so
widespread in the AS/400 world, you can't really be an AS/400 RPG
programmer and not know about it) - as well as for a minor bit of
runtime inefficiency:  the two leftmost digits and the four decimal
digits must be truncated, and the compiler generates some additional
code to do that...or so all the trade magazines say.
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** "Thomas Kine" <t.kine@computer.org>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net>`

```
Using this technique is one of the most processor-intensive tasks I have
seen.  It generates exceptions while running and will kill your machine if
you convert a large number of dates.

I would never, ever use this on an AS/400.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

- **From:** Thomas Hauber <thauber@my-deja.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<8nc5jk$f7p$1@nnrp1.deja.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net>`

```
I would challenge you to come up with hard provable numbers to support
your assertion that this wastes cycles.  Such a blanket statement is
a knee jerk reaction until proven.


In article <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net>,
  "Thomas Kine" <t.kine@computer.org> wrote:
> Using this technique is one of the most processor-intensive tasks I
have
> seen.  It generates exceptions while running and will kill your
machine if
> you convert a large number of dates.
>
…[6 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 4)_

- **From:** "Thomas Kine" <t.kine@computer.org>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<N5hm5.9526$4T.570883@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net> <8nc5jk$f7p$1@nnrp1.deja.com>`

```
Depends on the number of conversion you are doing and the load on the
AS/400.

I have killed a machine with this technique (back in the System 38 days) and
learned its problems the hard way.  Took the DBA a heckuva lot of research
to figure out what was slowing the machine down.

I don't have hard numbers, but I wouldn't encourage any programmers working
for me to use it.  Better and easier ways to handle this conversion.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

- **From:** Jonathan Ball <jonball_NS@earthlink.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<39999CF3.347E5CC8@earthlink.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net>`

```
Thomas Kine wrote:
> 
> Using this technique is one of the most processor-intensive tasks I have
…[3 more quoted lines elided]…
> I would never, ever use this on an AS/400.

I don't doubt that you are right, but how would you detect the
exceptions?  I wrote a quickie test program and ran it:


	.
	.
	Data Division.
	Working-Storage Section.
	77  date-ymd   pic 9(006) comp-3 value 991231.
	77  date-mdy   pic 9(006) comp-3.
	Procedure Division.
	    perform 10 times
	        compute date-mdy = date-ymd * 100.0001
	    end-perform.
	    goback.

At the conclusion, I checked my job log and there were no messages of
any kind.  Where do the exceptions appear?
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 4)_

- **From:** "Thomas Kine" <t.kine@computer.org>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<Wkhm5.9538$4T.572308@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net> <39999CF3.347E5CC8@earthlink.net>`

```
My understanding of the issue is that it generates some type of machine
exception because of the overflow condition you are forcing.  This technique
relies on the result not fitting into the defined variable, and OS/400
signals some kind of error on this condition - not into the job log, which
is why it can be very hard to find a performance problem related to this
technique.

Here's one reference to it from
http://www.as400network.com/TheRPGSource/199907-8/Art01Txt.htm

"Date conversions. Practically every RPG programmer knows the trick in which
you can change the format of a date represented by a number. For example, to
convert a date from ymd format to mdy format, multiply by 100.0001.

Although this method works, it's slow. You could do the same conversion at
least a hundred times faster with a couple of EVAL statements. In addition,
the trick isn't very flexible. For example, you can't use this technique for
mdy-to-dmy conversions. These days, the preferred way to handle dates is to
use the date data type.

If you really do need to truncate high-order digits from a number, you can
use overlapping zoned-decimal subfields. For example, in the program in
Figure 2, the value displayed is 12345."

Although the above excerpt doesn't talk about why it is hundreds of times
faster, it can slow down a program considerably if you are doing thousands
of conversions.
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 5)_

- **From:** "FXA Limited" <fxa@fxa-base.freeserve.co.uk>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<8nc9kl$7m3$1@newsg1.svr.pol.co.uk>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net> <39999CF3.347E5CC8@earthlink.net> <Wkhm5.9538$4T.572308@bgtnsc07-news.ops.worldnet.att.net>`

```
Mike Dawson, in his book, Performance Programming did bench mark tests on
the Mult method compared to moves using data structures. The move option was
reported as being 29% faster.

He also states that data exceptions occur ONLY as a result of a mathematical
operation where the true answer has more significant digits than the
variable specified. For example:

DATYMD   MULT  100.0001  DATMDY   60

910531      x           100.0001  = 91053191.0531

but the receiver is specified as 6,0 resulting in the data exception. He
says that a move of 4567 into a three digit field will NOT cause the data
exception.

It's also a great book if it's still in print:  ISBN: 1-884322-08-5
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 5)_

- **From:** Jonathan Ball <jonball_NS@earthlink.net>
- **Date:** 2000-08-16T06:23:51+00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<399A32B1.4D31D9AF@earthlink.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net> <39999CF3.347E5CC8@earthlink.net> <Wkhm5.9538$4T.572308@bgtnsc07-news.ops.worldnet.att.net>`

```
Thomas Kine wrote:
> 
> My understanding of the issue is that it generates some type of machine
…[17 more quoted lines elided]…
> of conversions.

Nowadays, of course, I would use the AS/400 ILE COBOL intrinsic function
CONVERT-DATE-TIME, or, if I ever get the opportunity to go back to RPG
(and learn RPG IV), whatever is the equivalent in RPG IV (there *is* an
equivalent, isn't there?  a quick perusal of the ILE RPG reference
didn't seem to reveal an exact equivalent.)
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 6)_

- **From:** myfirstname@mylastname.net.invalid (Paul Cunnane)
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<399a4e49.174288134@63.211.125.92>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net> <39999CF3.347E5CC8@earthlink.net> <Wkhm5.9538$4T.572308@bgtnsc07-news.ops.worldnet.att.net> <399A32B1.4D31D9AF@earthlink.net>`

```
On Wed, 16 Aug 2000 06:23:51 GMT, Jonathan Ball
<jonball_NS@earthlink.net> wrote:

>Nowadays, of course, I would use the AS/400 ILE COBOL intrinsic function
>CONVERT-DATE-TIME, or, if I ever get the opportunity to go back to RPG
>(and learn RPG IV), whatever is the equivalent in RPG IV (there *is* an
>equivalent, isn't there?  a quick perusal of the ILE RPG reference
>didn't seem to reveal an exact equivalent.)

Yup: MOVE

:)
```

###### ↳ ↳ ↳ Re: Interesting Date Routine

_(reply depth: 4)_

- **From:** Karl Hanson <kchanson@us.ibm.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<3999C3A2.F25B0F05@us.ibm.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net> <W6fm5.26277$gW5.1427810@bgtnsc04-news.ops.worldnet.att.net> <39999CF3.347E5CC8@earthlink.net>`

```
Jonathan Ball wrote:
> 
> Thomas Kine wrote:
…[23 more quoted lines elided]…
> any kind.  Where do the exceptions appear?

Exception messages can be suppressed from the job log... for example the
ILE C #pragma exception_handler has a "control action" of
_CTLA_HANDLE_NO_MSG which does this.  You could try getting a flow trace
using TRCJOB - I believe evidence of exceptions will show there
regardless of logging.

http://publib.boulder.ibm.com:80/cgi-bin/bookmgr/BOOKS/QB3AT602/8.12.11
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** "FXA Limited" <fxa@fxa-base.freeserve.co.uk>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.sys.ibm.as400.misc
- **Message-ID:** `<8nbvmr$iku$1@news6.svr.pol.co.uk>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <399968B6.86C45F2C@earthlink.net>`

```
And what's more it is not portable. Why would anyone in Europe want a date
in MMDDYY format? As much use as an ashtray on a motorcycle!

:-)

DG
```

#### ↳ Re: Interesting Date Routine

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Nsfm5.331$Ku3.100188@dfiatx1-snr1.gtei.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
That "trick" is in "Teach Yourself COBOL in 21 Days" published in 1994 by
SAMS Publishing.

Except in that book, they don't call it a "trick" they call it a
"technique;" which is why I do not recommend that book to anyone. (OK, so
they show some other stuff, too).

Using tricks and relying on PICTURE overflow is a bad habit to get into, and
I suggest any aspiring COBOL programmers learn to do date math using a
correct method. (Below)


01  DATE-YYMMDD    PIC 9(06).
01  DATE-MMDDYY    PIC 9(06).


     MOVE DATE-YYMMDD(1:2)  TO DATE-MMDDYY (5:2)
     MOVE DATE-YYMMDD(3:2)  TO DATE-MMDDYY (1:2)
     MOVE DATE-YYMMDD(5:2)  TO DATE-MMDDYY (3:2)
  or....
     STRING DATE-YYMMDD(1:2)  DELIMITED BY SIZE
                  DATE-YYMMDD(3:2)   DELIMITED BY SIZE
                  DATE-YYMMDD(5:2)   DELIMITED BY SIZE
          INTO DATE-MMDDYY
    END-STRING
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3999906C.60680A66@brazee.net>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <Nsfm5.331$Ku3.100188@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:

> That "trick" is in "Teach Yourself COBOL in 21 Days" published in 1994 by
> SAMS Publishing.
…[7 more quoted lines elided]…
> correct method. (Below)

Agreed, but...

> 01  DATE-YYMMDD    PIC 9(06).
> 01  DATE-MMDDYY    PIC 9(06).
…[9 more quoted lines elided]…
>     END-STRING

1.  Why are your dates numeric?  Are you going to do arithmetic with
DATE-MMDDYY?
2.  Why use reference modification?  It seems to me that 05 levels are more
clear and easier to find while doing maintenance.    It is also less likely to
be messed up by bad maintenance (for instance someone changing DATE-YYMMDD to
PIC 9(8) to accept a century).

Certainly 05 levels will eliminate the need of a STRING statement.
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399af27a.8264968@207.126.101.100>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <Nsfm5.331$Ku3.100188@dfiatx1-snr1.gtei.net>`

```
I still like this:

01  Date-YYMMDD.
     03  D-YY Pic 99.
     03  D-MM Pic 99.
     03  D-DD Pic 99.

01  Date-MMDDYY.
     03  D-MM Pic 99.
     03  D-DD  Pic 99.
     03  D-YY Pic 99.

Move Corresponding Date-YYMMDD to Date-MMDDYY.


On Tue, 15 Aug 2000 17:53:49 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>That "trick" is in "Teach Yourself COBOL in 21 Days" published in 1994 by
>SAMS Publishing.
…[56 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Interesting Date Routine

- **From:** "Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spj8g8uskn976@corp.supernews.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Okay, okay....I said it was interesting, not useful or recommended.
I know I've never used it or even considered using it.

Arghhhhhhhh !
LD



Lincoln Duncan <NotOnSite*NOSPAM*@Yahoo.com> wrote in message
news:sph8l3o8kn9102@corp.supernews.com...
> Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
> (although I don't believe it's still available)
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Interesting Date Routine

- **From:** thomaskine@my-deja.com
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nevoe$nul$1@nnrp1.deja.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com> <spj8g8uskn976@corp.supernews.com>`

```
Yeah, I agree.  I feel partly responsible because of my reaction to
your posting.

It was just that I had been burned by this in the past and it is a
pretty clever technique...

My apologies for any part I played in this red herring.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Interesting Date Routine

- **From:** "Tim Hillock" <timhillock@home.com>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%Ijm5.29117$c5.1060569@news2.rdc1.on.home.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
It could/may have been very useful on a  small machine in the late 60's to
early 70's where/when RAM was at a price.
```

#### ↳ Re: Interesting Date Routine

- **From:** jacksleight@my-deja.com
- **Date:** 2000-08-16T02:22:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ncttc$bg4$1@nnrp1.deja.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Well Linc, I guess that'll learn ya.
A good deed never goes unpunished. Sheesh!


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Interesting Date Routine

- **From:** David Bretz <DBretz@mescoma.com>
- **Date:** 2000-08-31T12:06:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39AE8299.E3127C7B@mescoma.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
Make it even simpler........


COMPUTE DATE1 = DATE1 * 100.0001
```

#### ↳ Re: Interesting Date Routine

- **From:** "Dave Begley" <dbegley@houston.rr.com>
- **Date:** 2000-08-31T17:40:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%Lwr5.23323$C5.449082@typhoon.austin.rr.com>`
- **References:** `<sph8l3o8kn9102@corp.supernews.com>`

```
This was common on an AS/400 computer system that I worked on.  It works
okay, except if the date field is a packed numeric field and is also part of
the key to the file.  On the packed numeric fields, there is an extra byte
(or bit, whatever) preceeding the 6 digits that you 'see'.  Sometimes this
calculation would leave something in that hidden part of the field and this
would cause the data to appear to be out of sequence.  It was very strannge
looking when I first saw the problem.



"Lincoln Duncan" <NotOnSite*NOSPAM*@Yahoo.com> wrote in message
news:sph8l3o8kn9102@corp.supernews.com...
> Found at:  http://www.software.ibm.com/year2000/tips3.html#levsedr
> (although I don't believe it's still available)
…[18 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
