[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BIG: Cobol parser project

_31 messages · 15 participants · 1999-04_

---

### BIG: Cobol parser project

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3705EE1E.EF7AB4FA@zip.com.au>`

```
Here is my cobol parser project version 0.01.  It compiles (Fujitsu V3),
it appears to reliably pull out the working storage on my single test
program.

Zero testing, caveat emptor, work very much in progress.

This is a first on the PC for me, normally on the big iron.  How do I
actually assign files from outside the program?

Note that the program must compile in both MVS and PC so make the
answers close.  I am not happy with the file handling because it wont
compile on MVS.

Has anyone got a text list of reserved words?

Eventual purpose:

1.  Output obsolete words from the program.

2.  Parser to ensure adherence to standards.  No point doing what a
machine can do (Jump in here Donald :->)

2.  Automatically add end-if, etc.

3.  Code formatter base.
```

#### ↳ Re: Cobol parser project

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e54ko$fvd$1@news.igs.net>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au>`

```
Files are assigned in the select clause for Fujitsu:

SELECT FILE ASSIGN TO DATA-NAME.
move "C:\area\name.ext" to data-name.
open ...

Ken Foskey wrote in message <3705EE1E.EF7AB4FA@zip.com.au>...
>Here is my cobol parser project version 0.01.  It compiles (Fujitsu V3),
>it appears to reliably pull out the working storage on my single test
…[22 more quoted lines elided]…
>3.  Code formatter base.
```

#### ↳ Re: BIG: Cobol parser project

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990403091412.08111.00000732@ngol08.aol.com>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au>`

```
In article <3705EE1E.EF7AB4FA@zip.com.au>, Ken Foskey <waratah@zip.com.au>
writes:

>Here is my cobol parser project version 0.01.  It compiles (Fujitsu V3),
>it appears to reliably pull out the working storage on my single test
…[12 more quoted lines elided]…
>

This looks like a neat project to see the final result.
I'd like to follow along and possibly attempt to use the end product 
for standardized code review of the programmers that I support.

As for MVS/PC compatibility, you've already broken that rule with
permitting 255 char lines for the program source.
By placing the file name in the assign statement also breaks the 
MVS compatibility rule.
Code it as if you were on the MVS box using the implementor names,
the only PC specific that would have to be added is the 'line sequential'
organization. By using the 'MVS Implementor names', you will be forced
into using the 'Runtime Environment Variables' screen.  The 'Runtime
Environment' is where you would setup the equivalent of your JCL DD names.

Hope this gets you started towards bringing this to a 'near' single source
dual platform product.  
** As a note for code maintenance:  I'd keep all the code in a single file
   commenting out what is specific to the opposing environment and possibly
   add some kind of identifier tag in 73-80 [old style 80-column coder here].

Best of luck to you.
```

##### ↳ ↳ Re: BIG: Cobol parser project

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370624d0@news3.us.ibm.net>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au> <19990403091412.08111.00000732@ngol08.aol.com>`

```
Ken,
To circumvent all the problems with files do this:
Write another Cobol program to do the file I/O.
The call that with a control block containing an operation
code (open, get, close). That way, the main (and
difficult program can be completely portable and the
(trivial) I/O program can be made as non-portable as you need.

Sff5ky <sff5ky@aol.comxxx123> wrote in message
news:19990403091412.08111.00000732@ngol08.aol.com...
> In article <3705EE1E.EF7AB4FA@zip.com.au>, Ken Foskey <waratah@zip.com.au>
> writes:
…[34 more quoted lines elided]…
>    commenting out what is specific to the opposing environment and
possibly
>    add some kind of identifier tag in 73-80 [old style 80-column coder
here].
>
> Best of luck to you.
>
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37062E70.53355FDB@zip.com.au>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au> <19990403091412.08111.00000732@ngol08.aol.com> <370624d0@news3.us.ibm.net>`

```
Leif Svalgaard wrote:
> 
> Ken,
…[6 more quoted lines elided]…
> 

Great idea:  The reason I did not go this way is because I like to bury
my reads inside the loops.

I will use a driver and a subroutine.   The driver does the up front and
the subroutine actually reads the records in.

To the other one, I was going to try the record contains 0 characters
trick but Fujitsu would not have a bar of it.

The next problem I am getting is that the opy has to be:

  COPY 'TOKENS.CBL'.

When I go MVS it must be:

  COPY TOKENS.

So much for day two.  Time to go to sleep.

While the families away I get to actually do the project I have been
stewing on...

Ken

PS:  I missed the '=' sign.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37063684@news3.us.ibm.net>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au> <19990403091412.08111.00000732@ngol08.aol.com> <370624d0@news3.us.ibm.net> <37062E70.53355FDB@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote in message
news:37062E70.53355FDB@zip.com.au...
> Leif Svalgaard wrote:
> >
…[13 more quoted lines elided]…
> the subroutine actually reads the records in.

You can still do reads inside the loops; just replace the
read wil a call of the I/O program.

The main point is that the subroutine is the only one that knows
about the actual file.



>
> To the other one, I was going to try the record contains 0 characters
…[9 more quoted lines elided]…
>

COPY TOKENS will work anywhere also on Fujitsu. You may have
to set an environment variable to tell it where copy members are
and what their extension is, but you can ALWAYS use just
COPY TOKEN.




> So much for day two.  Time to go to sleep.
>
…[5 more quoted lines elided]…
> PS:  I missed the '=' sign.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990403123029.11047.00000759@ngol06.aol.com>`
- **References:** `<37062E70.53355FDB@zip.com.au>`

```
In article <37062E70.53355FDB@zip.com.au>, Ken Foskey <waratah@zip.com.au>
writes:

>
>The next problem I am getting is that the opy has to be:
…[8 more quoted lines elided]…
>

I am able to use copy syntax as 
   COPY 'LIBFIL'.
and this works on both FujiCOBOL and COBOL for MVS AD\Cycle370.
On the PC I have the copybooks in a \CPY directory with NO FILE EXT.
This has worked beautifully for the last year under v3 and v4.  It does pose
a little problem with editting the libraries, but these are 'supposed' to be 
copies of Mainframe libraries and I don't want to get them out of sync.
Any library maintenance is done on the mainframe and then downloaded back to
the PC development area.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370657fd@news3.us.ibm.net>`
- **References:** `<37062E70.53355FDB@zip.com.au> <19990403123029.11047.00000759@ngol06.aol.com>`

```
Sff5ky <sff5ky@aol.comxxx123> wrote in message
> In article <37062E70.53355FDB@zip.com.au>, Ken Foskey <waratah@zip.com.au>
> >The next problem I am getting is that the copy has to be:
> >  COPY 'TOKENS.CBL'.
> >When I go MVS it must be:
> >  COPY TOKENS.

> I am able to use copy syntax as
>    COPY 'LIBFIL'.
> and this works on both FujiCOBOL and COBOL for MVS AD\Cycle370.
> On the PC I have the copybooks in a \CPY directory with NO FILE EXT.
> This has worked beautifully for the last year under v3 and v4.  It does
pose
> a little problem with editting the libraries, but these are 'supposed' to
be
> copies of Mainframe libraries and I don't want to get them out of sync.
> Any library maintenance is done on the mainframe and then downloaded back
to
> the PC development area.

I don't see where the problem is. With Fujitsu
my Cobol programs have extension .COB
Copybooks have extension .CBL and I simply
write COPY LIBFIL in the program. This works
on PC and is the standard way on MVS and
on all other platforms as well.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990403160215.08023.00001025@ngol04.aol.com>`
- **References:** `<370657fd@news3.us.ibm.net>`

```
In article <370657fd@news3.us.ibm.net>, "Leif Svalgaard" <lsvalg@ibm.net>
writes:

>> the PC development area.
>
…[7 more quoted lines elided]…
>

I think that the point was that on the PC Kevin was coding 
COPY 'LIBFIL.CPY'
and on MVS
COPY LIBFIL.

My point was that enclosing the libfil name in quote/apost works in 
both environments and you should not have to all the extension to the
libfil name.  In my case, I choose to operate without extensions as it 
simplifies my download procedures.  I do place the copylib files in a 
specific directory that is referenced in the compiler options.

You indicated that there is compiler option to indicate what extension 
is used, where might I find this?  Would you be familiar enough with the 
editor to be able to tell how to adjust the options so I do not have to use
the CBL/COB extensions yet still follow the COBOL syntax highlighting rules???

Thanks in advance.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370683c6@news3.us.ibm.net>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com>`

```
Well, I really don't use the Fujitsu editor so I don't have the problem.
The compiler option is something you might find on some compilers
(my stuff compiles on about 20 different ones and some you have to
tell where/what copybooks are).
My point was simply that sticking with the fully portable COPY XXXX.
without extension or apost/quotes is always the 'best'.
Then you simply adjust to what your particular compiler wants.

If you have special wishes (like in your case, no extension) you
sometimes lose out.

Sff5ky <sff5ky@aol.comxxx123> wrote in message
news:19990403160215.08023.00001025@ngol04.aol.com...
> In article <370657fd@news3.us.ibm.net>, "Leif Svalgaard" <lsvalg@ibm.net>
> writes:
…[25 more quoted lines elided]…
> editor to be able to tell how to adjust the options so I do not have to
use
> the CBL/COB extensions yet still follow the COBOL syntax highlighting
rules???
>
> Thanks in advance.
>
>
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3706BD4E.D92E137B@zip.com.au>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net>`

```
Leif Svalgaard wrote:
> 
> Well, I really don't use the Fujitsu editor so I don't have the problem.
…[6 more quoted lines elided]…
> 

Leif,

I think you get the gernsey.  I will try calling my copybook .CBL and
omitting the quotes adn the extension.

General, 

By the way someone have some space to store some of this stuff to stop
flooding the news group?

start Day II

OK I will split the program into the following modules:

PARSEIO  - Simple reader routine
PARSER   - Simple start up
PARSPARM - Read in the token parameters (remove the 'special'
           parameters)
PARSTOKN - The basic stuff that I have done already.
PARSID   - Identification division
PARSENV  - Environment division
PARSDATA - Data division
PARSPROC - Procedure division

Back to actual coding.

Sign in later...
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 9)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e6v1h$9lr$2@bgtnsc02.worldnet.att.net>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au>`

```
Ken,  I got Parser to compile of V4 F, but I have not succeeded yet in
getting it to process a file.  I'll be tailing along following you guys as a
mental exercise. I'm learning some new stuff, too.

Thanks,

Warren Simmons
Ken Foskey wrote in message <3706BD4E.D92E137B@zip.com.au>...
>Leif Svalgaard wrote:
>>
…[35 more quoted lines elided]…
>Sign in later...
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37075024.E53F4038@zip.com.au>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net>`

```
Warren Simmons wrote:
> 
> Ken,  I got Parser to compile of V4 F, but I have not succeeded yet in
> getting it to process a file.  I'll be tailing along following you guys as a
> mental exercise. I'm learning some new stuff, too.
 
What makes you think there is a group.  I am just one person and when
the wife gets back it is back to the back burner.

Learning experience:

I use the attached copybook in linkage through multiple subprograms.
Notice that active-token-idx is defined COMP.  I originally defined it
as an index as in:

 05  TOKEN-buffer                      occurs 10000
                                       indexed by TOKEN-IDX
                                                  active-token-idx
                                                  last-token-idx.

And the actve-token-idx was not passed back.  Each subproggram defined
it's own local copy.  Debugging is wonderful.  (For example token-idx
happy clicks up in the tokeniser but all other programs think it is 1).

Is this correct?  Is it actually defined what will happen?

One for the standards gurus to chew on.

Question 2:  How do you define a copybook as a requirement on the
compiler.  I 'fixed' the problem but it did not go away in the build
because V3 did not sense the copybook change and automatically
recompile.

Hot dickity dog I just found a program in \fsc\pcobol32 f3bxe000.exe it
looks like an editor.  Is this the default editor that I somehow cleared
in my tinkering?
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e8rve$214@sjx-ixn1.ix.netcom.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au>`

```
Ken Foskey wrote in message <37075024.E53F4038@zip.com.au>...
   <snip>
>
>Learning experience:
…[15 more quoted lines elided]…
>
  <snip>

Yes, there are some "funny" rules about INDEX items - but the bottom-line is
that they are ALWAYS "local".  (there is an distinction as you see below
between index data-items and indices themselves.) The "solution" is to have

 05  TOKEN-buffer                      occurs 10000
                                       indexed by TOKEN-IDX
                                                  active-token-idx
                                                  last-token-idx.
 05  Save-Index-Table  Occurs 3 times.
      10  Each-Index   Usage Index.

Then you
   A) save the current index values into the table
   B) "pass" the table of indices as well as your buffer to the subprogram
   C) in the subprogram set your indices to the passed-saved values
   D) do your logic
   E) save the new indices values back into the table
   F) return to the calling program
   G) reset the calling program's indices value to whatever the subprogram
put in the table

*OR* alternatively, don't use indices - but use "subscripting" with another
defined data item (such as your COMP solution).

(Someone else may have a better way of using the same "index values" in
calling and called programs - but this is the approach that I think is
clearest.)
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 12)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3707f7f9@news3.us.ibm.net>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote
 > Ken Foskey wrote in message <37075024.E53F4038@zip.com.au>...
> >(snip) the actve-token-idx was not passed back.  Each subproggram defined
…[3 more quoted lines elided]…
> Yes, there are some "funny" rules about INDEX items - but the bottom-line
is
> that they are ALWAYS "local
>(snip)
> *OR* alternatively, don't use indices - but use "subscripting" with
another
> defined data item (such as your COMP solution).

Use subscripting instead of indexing. Compilers can optimize subscripts
to behave like indices. That is add 10 instead of 1 if the item indexed is
10 characters long. And in any case, the subscripting time if very small
anyway compared to the operation, e.g.
  02   TABLE-ITEM    PIC X(20) OCCURS 2000 TIMES.
  02   THE-SUB          PIC S9(5) COMP.

IF TABLE-ITEM (THE-SUB) = "QWERTYUIOPASD"
      do something
END-IF
```

###### ↳ ↳ ↳ Indexes are overused

_(reply depth: 12)_

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com>`

```
Indexes are way overused anyway. Seems like every client site has some
crazy standard that you have to use indexes all the time, even when they're
not appropriate, because someone a long time ago said they're more
efficient, even though that really depends on what you're doing.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 13)_

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370AC317.5656C981@ix.netcom.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com>`

```
What you would consider to be an inappropriate use of an index?  A standard you
do not necessarily agree with does not make it crazy. And yes, even today,
indexes are still the most efficient method for accessing table elements. Isn't
it strange that so many of the client sites where you have worked have also
employed that same anonymous person who implemented the rules for the use of
indexes. Is it really more difficult to code SET NDX TO 1 as opposed to MOVE 1
TO SUB. Have you tried a SEARCH of a table with a subscript recently?

"Robert M. Pritchett" wrote:

> Indexes are way overused anyway. Seems like every client site has some
> crazy standard that you have to use indexes all the time, even when they're
…[8 more quoted lines elided]…
> that same contract on a 1099 as a self-employed independent contractor!
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 14)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370aeb58.798827435@news1.ibm.net>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com>`

```
On Tue, 06 Apr 1999 22:29:44 -0400, John Trifon
<jtrifon@ix.netcom.com> wrote:

>What you would consider to be an inappropriate use of an index?  A standard you
>do not necessarily agree with does not make it crazy. And yes, even today,
…[4 more quoted lines elided]…
>TO SUB. Have you tried a SEARCH of a table with a subscript recently?

What I think is meant might be something like ... oh, where a number
that is input by the user refers DIRECTLY to a table element.  For
example, a table of Months.  The user enters 11 and you lookup
November.  Making the table of months reference ONLY by an index and
not via a subscript is silly.  You have to "jump through hoops" as it
were to get the entered value into the index.
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 15)_

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OvjMrkSg#GA.250@nih2naab.prod2.compuserve.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net>`

```
Exactly. Indexes are fine for sequential access, or via Search or Search
All, but for random access, subscripts are not only easier to read, they're
actually more efficient - even the compiler manual usually says so. Forcing
programmers to use indexes in these inappropriate cases not only obscures
and complicates the code, it's less efficient, or at least no better.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Thane Hubbell wrote in message <370aeb58.798827435@news1.ibm.net>...

>What I think is meant might be something like ... oh, where a number
>that is input by the user refers DIRECTLY to a table element.  For
…[3 more quoted lines elided]…
>were to get the entered value into the index.
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 16)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370BD7F1.5296@compaq.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net> <OvjMrkSg#GA.250@nih2naab.prod2.compuserve.com>`

```
Robert M. Pritchett wrote:
> 
> Exactly. Indexes are fine for sequential access, or via Search or Search
> All, but for random access, subscripts are not only easier to read, they're
> actually more efficient - even the compiler manual usually says so.

This depends entirely on the implementation and on what you are doing.  
In many, subscripts are never more efficient.  And, if the subscript 
is not some binary type it is never more efficient.  However, 
efficiency should not be that much of a concern.  One reason I have 
heard for using indexes is that they are associated with only one 
table and it prevents a class of problems where the user gets mixed up 
using the wrong subscript with some table.  However, to each his/her 
own.

> Forcing
> programmers to use indexes in these inappropriate cases not only obscures
> and complicates the code, it's less efficient, or at least no better.
> 
See above
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pX1P2.1801$HB5.460843@news3.mia>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net> <OvjMrkSg#GA.250@nih2naab.prod2.compuserve.com> <370BD7F1.5296@compaq.com>`

```
Don Nelson wrote:
> ...
>One reason I have heard for using indexes is that they are associated
>with only one table and it prevents a class of problems where the user
>gets mixed up using the wrong subscript with some table.
> ...

I agree with this reason, Don.  In fact, the reasoning is so strong to
my mind that I never use index data items.  They are accidents looking
for a place to happen.  I don't necessarily avoid subscripts, there are
cases when using them makes the code simpler or clearer than indexes,
and efficiency is not an issue.  In fact, the overall logic of using
indexes can be less efficient than subscripts, if you must frequently
convert between indexes and numeric values, or frequently compare
indexes with numeric data items or indexes of tables with different
element sizes.  An individual indexed reference should never be less
efficient than subscripting, of course. :-)
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 18)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370CFE7B.303C@compaq.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net> <OvjMrkSg#GA.250@nih2naab.prod2.compuserve.com> <370BD7F1.5296@compaq.com> <pX1P2.1801$HB5.460843@news3.mia>`

```
Judson McClendon wrote:
> 
> Don Nelson wrote:
…[7 more quoted lines elided]…
> my mind that I never use index data items.

I assume you mean "01 whatever USAGE INDEX".  As you say, they are 
really bad.

> They are accidents looking
> for a place to happen.  I don't necessarily avoid subscripts, there are
…[5 more quoted lines elided]…
> element sizes.

That is true in most cases.  If you are comparing against constants 
most compilers use the computed value in place of the constant so 
there is no loss.  The important thing is to make the code obvious and 
easy to maintain.  Unless something is in a tight look that is 
executed a zillion times small bits of efficiency should not be too 
important.

>An individual indexed reference should never be less
> efficient than subscripting, of course. :-)
 True
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 15)_

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370C1680.380CFD9@ix.netcom.com>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net>`

```
The "jump through hoops"  is an extreme  exaggeration. In the trivial month lookup
example, it still is only 1 line of code difference.
Ignoring any validation of the data, which really isn't a consideration here:

ACCEPT mm.
SET mm-ndx TO mm
DISPLAY month-name ( mm-ndx)
*-------------- vs ---------------------*
ACCEPT mm.
DISPLAY month-name ( mm)


Thane Hubbell wrote:

> On Tue, 06 Apr 1999 22:29:44 -0400, John Trifon
> <jtrifon@ix.netcom.com> wrote:
…[14 more quoted lines elided]…
> were to get the entered value into the index.
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 16)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N62P2.1820$HB5.466358@news3.mia>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net> <370C1680.380CFD9@ix.netcom.com>`

```
John Trifon wrote:
>The "jump through hoops"  is an extreme  exaggeration. In the trivial month
>lookup example, it still is only 1 line of code difference.
>Ignoring any validation of the data, which really isn't a consideration here:

There are situations when, for every use of a subscript/index to actually
reference a table, you must reference the subscript/index many times for
its occurrence number value.  In these cases, use of an index certainly
can complicate and obfuscate the code to some degree over the use of a
subscript, and can be less efficient, relatively speaking.  The specific
ratio depends on the machine architecture, the compiler, and the particular
requirements of the logic.
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 17)_

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<923579702.23618.0.nnrp-03.9e98b131@news.demon.co.uk>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au> <7e6v1h$9lr$2@bgtnsc02.worldnet.att.net> <37075024.E53F4038@zip.com.au> <7e8rve$214@sjx-ixn1.ix.netcom.com> <#9CaVbJg#GA.333@nih2naaf.prod2.compuserve.com> <370AC317.5656C981@ix.netcom.com> <370aeb58.798827435@news1.ibm.net> <370C1680.380CFD9@ix.netcom.com> <N62P2.1820$HB5.466358@news3.mia>`

```
I guess everyone's saying its horses for courses.

For some things indexes are much faster.  I vaguely remember that on the
WANG VS there was a study that showed a vast improvement (I can't remember
the figure) on indices over subscripts.

However it does depend on the compiler and hardware.  When we converted our
COBOL to run on AS400, I investigated and subscripts were actually faster
than indices.  This was partly because of the compiler and partly because of
the way AS400 described tables at the MI level.

E.g on a table of 6 byte long elements, the VS compiler would generate SET
index UP BY 5 as ADD 30 TO index whereas the AS400 would generate it as
MULTIPLY 5 BY 6 and ADD the result to index.  So the VS worked out literal
increments at compile time but the AS did it at run time.

Conversely the AS retained structure and array information at the MI level
and could use a subscript directly to pick up an element.

I checked out the AS back in 1990 and things have probably changed since
then.  Certainly everything's much faster and I've certainly stopped
worrying about things like this.

Regards
Rick

Judson McClendon wrote in message ...
>John Trifon wrote:
>>The "jump through hoops"  is an extreme  exaggeration. In the trivial
month
>>lookup example, it still is only 1 line of code difference.
>>Ignoring any validation of the data, which really isn't a consideration
here:
>
>There are situations when, for every use of a subscript/index to actually
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37078406@news3.us.ibm.net>`
- **References:** `<370657fd@news3.us.ibm.net> <19990403160215.08023.00001025@ngol04.aol.com> <370683c6@news3.us.ibm.net> <3706BD4E.D92E137B@zip.com.au>`

```
> By the way someone have some space to store some of this stuff to stop
> flooding the news group?

I could make a room at http://etk.com where you can upload the whole
project to. then people can go there and look at the current status
and download what they want.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eoQZYYJg#GA.122@nih2naaf.prod2.compuserve.com>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au> <19990403091412.08111.00000732@ngol08.aol.com> <370624d0@news3.us.ibm.net>`

```
There's a place for using I/O modules, I don't know for sure if this is it,
but I have seen places where these are sorely overused, like it's been
adopted as some kind of standard and is required even though in many cases
it's inappropriate and even harmful to software quality.

That may not apply here, I just wanted to mention the possibility.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Leif Svalgaard wrote in message <370624d0@news3.us.ibm.net>...
>Ken,
>To circumvent all the problems with files do this:
…[4 more quoted lines elided]…
>(trivial) I/O program can be made as non-portable as you need.
```

###### ↳ ↳ ↳ Re: BIG: Cobol parser project

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370B3071.D4EA31DB@zip.com.au>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au> <19990403091412.08111.00000732@ngol08.aol.com> <370624d0@news3.us.ibm.net> <eoQZYYJg#GA.122@nih2naaf.prod2.compuserve.com>`

```
Robert M. Pritchett wrote:
> 
> There's a place for using I/O modules, I don't know for sure if this is it,
> but I have seen places where these are sorely overused, like it's been
> adopted as some kind of standard and is required even though in many cases
> it's inappropriate and even harmful to software quality.

I think it is.  I can write an MVS version of the IO and keep the IO
problems separate from the real working (portable?) code.

Status check.

Who was it that said that this is difficult.

I re-engineered the general routines a couple of time already.  The
infrastructure takes a long time to create in these sorts of projects. 
I think it is getting mechanical now just defining the actual rules of
cobol.

I used Arnold's table to create a comprehensive list of tokens via
program and a complementary token copybook.  If I want to add extra word
I can automatically regen the copybook and the keywords table using a
bildtokn command.  Primitive, this is a project on it's own.

I will release a new work in progress once the code for the working
storage is complete.

Does anyone want to tackle the environment division for me?  I will send
latest code base on request by a volunteer.

Ken

PS:  Has Fujitsu corrected the VERY obscure messages when it has a
problem with the 'end-' stuff.  I missed an end-if and it said an
imperative was missing.  Took me a while to spot the missinf end-if
```

#### ↳ Re: Cobol parser project

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e5hjb$jjj$3@news-1.news.gte.net>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au>`

```
Automatically adding/inserting  "end-if"s can easily change the meaning of
the logic. Go slowly on this one.

MCM.

Ken Foskey wrote in message <3705EE1E.EF7AB4FA@zip.com.au>...
>Zero testing, caveat emptor, work very much in progress.
>
>Eventual purpose:
>2.  Automatically add end-if, etc.
```

#### ↳ COBOL Reserved Words

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37074D18.3EB0DF8F@worldnet.att.net>`
- **References:** `<3705EE1E.EF7AB4FA@zip.com.au>`

```
Ken Foskey wrote:
> 
> Has anyone got a text list of reserved words?

Yeah, I do.  I apologize for the length, I count 503 reserved words, but
then I include stuff like EXEC, END-EXEC, EJECT, SKIP, et cetera.  I'll
attach it at the end.

> 
> Eventual purpose:
…[4 more quoted lines elided]…
> machine can do (Jump in here Donald :->)

Standards?  How about making the program customizable.  In my limited
experience, standards vary quite a bit from one shop to another.
> 
> 2.  Automatically add end-if, etc.
> 
> 3.  Code formatter base.

The only reason I have this kind of data is that I wrote a program to
analyze code for compliance to my shop's standards.  Not to reformat
(which I consider to be a much more difficult project), but as an aid
for structured code walkthru's.  After several years of maintenance,
this program is around 8000 lines, but it also checks for dead data,
non-referenced paragraphs, uninitialized variables, comparisons between
numeric and non-numeric data, recursive calls, et cetera.

I would estimate the lexer portion of this monster to be roughly 2000
lines, including data definitions.

Here it is.  It's big:
```

##### ↳ ↳ Re: COBOL Reserved Words

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990405085730.21597.00003571@ng-fi1.aol.com>`
- **References:** `<37074D18.3EB0DF8F@worldnet.att.net>`

```
would you mind sending me a copy of this program?  I use could use this
"monster" in our shop.

Thanks,
Tom Wymer

twymer@hotmail.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
