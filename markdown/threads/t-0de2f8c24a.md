[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Student needs help with reference modification

_15 messages · 12 participants · 2000-01_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Student needs help with reference modification

- **From:** "Pat" <patp@cpinternet.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
Hi,

Our COBOL teacher gave us work over the holiday break (sigh...).  It's a
validation program.  I'm trying to use reference modification to move part
of a field (looks like a social security type number).  I get the error
message "reserved word missing or incorrectly used".  I've got this typed in
as our book shows, but the book is sometimes wrong.  We're using MF Personal
COBOL 2.0, and at times the book has shown some compiler specific things for
RM (for example, EBCDIC vs. ASCII embedded negative signs).  I wouldn't
think this is a compiler thing, but for the life of me I can't see what I've
missed.  I'm sure it's one of those "Duh!" things (they usually are!).

Here's the code:

(working-storage)
 05  IR-EMPLOYEE-NUMBER          PIC 9(9).

10   DL-EMPLOYEE-NUMBER.
   15 DL-EMPLOYEE-NUMBER-1     PIC 9(3).
   15                          PIC X(1)    VALUE "-".
   15 DL-EMPLOYEE-NUMBER-2     PIC 9(2).
   15                          PIC X(1)    VALUE "-".
   15 DL-EMPLOYEE-NUMBER-3     PIC 9(4).

(procedure)
MOVE IR-EMPLOYEE-NUMBER:1:3 TO DL-EMPLOYEE-NUMBER-1
MOVE IR-EMPLOYEE-NUMBER:4:2 TO DL-EMPLOYEE-NUMBER-2
MOVE IR-EMPLOYEE-NUMBER:6 TO DL-EMPLOYEE-NUMBER-3

I want to move the first 3 digits of IR-EMPLOYEE-NUMBER  to
DL-EMPLOYEE-NUMBER-1, the 4th and 5th to DL-EMPLOYEE-NUMBER-3, and the rest
to the last.

Any help would be greatly appreciated!!

Thanks,
Pat
```

#### ↳ Re: Student needs help with reference modification

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<854lof$qho$1@nntp9.atl.mindspring.net>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
You need parenthesis around your starting point and length:

Change ===>

MOVE IR-EMPLOYEE-NUMBER:1:3 TO DL-EMPLOYEE-NUMBER-1

To ===>

MOVE IR-EMPLOYEE-NUMBER (1:3) TO DL-EMPLOYEE-NUMBER-1

HTH....

WOB

Pat <patp@cpinternet.com> wrote in message
news:rlfd4.639$i9.4083@newsfeed.slurp.net...
> Hi,
>
> Our COBOL teacher gave us work over the holiday break (sigh...).  It's a

< Rest Snipped>
```

#### ↳ Re: Student needs help with reference modification

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-xeGShJq8nsie@localhost>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
On Thu, 1 Jan 1970 00:59:59, "Pat" <patp@cpinternet.com> wrote:

Pat - I can't see where anyone has answered you yet (or my news server
has not yet received the responses - I just today received your Jan 1 
posting).

> Here's the code:
> MOVE IR-EMPLOYEE-NUMBER:1:3 TO DL-EMPLOYEE-NUMBER-1

Change to: Move IR-EMPLOYEE-NUMBER (1:3) to DL-EMPLOYEE-NUMBER-1.

That should fix you up.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Student needs help with reference modification

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85543c$jd1$1@news.igs.net>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
You need to use parenthesis around your address modification.
IE: MOVE IR-EMPLOYEE-NUMBER(1:3) TO ...

Pat wrote in message ...
>Hi,
>
…[3 more quoted lines elided]…
>message "reserved word missing or incorrectly used".  I've got this typed
in
>as our book shows, but the book is sometimes wrong.  We're using MF
Personal
>COBOL 2.0, and at times the book has shown some compiler specific things
for
>RM (for example, EBCDIC vs. ASCII embedded negative signs).  I wouldn't
>think this is a compiler thing, but for the life of me I can't see what
I've
>missed.  I'm sure it's one of those "Duh!" things (they usually are!).
>
…[26 more quoted lines elided]…
>
```

#### ↳ Re: Student needs help with reference modification

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38763948.CFF0732A@home.com>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```


Pat wrote:
> 
> Hi,
…[10 more quoted lines elided]…
> 

Sure it's one of those "Duh" things - but we've all been there, and
using Debuggers/Animators we 'seasoned' people find we've done it over
and over again. Anyway nice try, and you were so-oooooo close.

Not to confuse you, because you are ASSUMING input data is legit - Ken's 
suggestion of pic 999-99-9999 will work PROVIDING the incoming data is
numeric. Same applies of course to your reference modification moves.
It will go belly-up either route if you attempt to move non-numeric to a
numeric field.

In this case I'm guessing the instructor was wanting to test you on
Reference Modification - without doubt a very powerful feature.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Student needs help with reference modification

- **From:** Clark Morris <cfmtech@istar.ca>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3877D933.4667829A@istar.ca>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net> <38763948.CFF0732A@home.com>`

```
Since the hyphen is the sign character, I doubt that PIC 999-99-9999
is valid. I don't have a COBOL compiler or manual easily available to
verify my belief so could someone confirm or refute my contention?

Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.ca   

"James J. Gavan" wrote:
> 
> 
…[11 more quoted lines elided]…
> Jimmy, Calgary AB
```

#### ↳ Re:Ref modification _ thanks!!

- **From:** "Pat" <patp@cpinternet.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y_td4.1350$Mp.1224@newsfeed.slurp.net>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
Hi,

Thanks to all you folks who answered my post.  I did need to put ( ) around
the numbers (IR-EMPLOYEENUMBER (1:3)) .  But the book didn't have show it
that way - really!!!  Really really!!

Anyway, I was wondering, too, about a numeric edited pic of 999-99-9999.
Wasn't sure if it would work, our book names blank, slash, etc...as editing
symbols, but not a - (dash).  Other than using it as a negative sign......
Good to know in the future, thanks so much!!

Have a wonderful weekend, all!

Pat
```

##### ↳ ↳ Re: Re:Ref modification _ thanks!!

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<855tqs$ck98$1@newssvr03-int.news.prodigy.com>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net> <Y_td4.1350$Mp.1224@newsfeed.slurp.net>`

```

Pat <patp@cpinternet.com> wrote in message
news:Y_td4.1350$Mp.1224@newsfeed.slurp.net...
> Hi,
>
> Thanks to all you folks who answered my post.  I did need to put ( )
around
> the numbers (IR-EMPLOYEENUMBER (1:3)) .  But the book didn't have show it
> that way - really!!!  Really really!!
>
> Anyway, I was wondering, too, about a numeric edited pic of 999-99-9999.
> Wasn't sure if it would work, our book names blank, slash, etc...as
editing
> symbols, but not a - (dash).  Other than using it as a negative sign......
> Good to know in the future, thanks so much!!
…[3 more quoted lines elided]…
> Pat

I believe you're right about 999-99-9999 not being a valid picture clause.
Unless there's been a new feature of COBOL I'm not aware of, the hyphen can
only be used as a leading, trailing, or floating minus sign.  I would
accomplish that particular result by coding the following:
01  EMPL-NO                     PIC  999B99B9999.
01  FILLER REDEFINES EMPL-NO.
       05  FILLER                                      PIC  999.
       05  DASH-1                                     PIC  X.
       05  FILLER                                      PIC  99.
       05  DASH-2                                     PIC  X.
       05  FILLER                                      PIC  9999.
MOVE 123456789                                TO EMPL-NO
MOVE '-'                                                  TO DASH-1
MOVE '-'                                                  TO DASH-2
..
```

##### ↳ ↳ Re: Re:Ref modification _ thanks!!

- **From:** "Gumbo" <a@a.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fVOd4.789$%%6.5646@typhoon.columbus.rr.com>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net> <Y_td4.1350$Mp.1224@newsfeed.slurp.net>`

```
>Thanks to all you folks who answered my post.  I did need to put ( ) around
>the numbers (IR-EMPLOYEENUMBER (1:3)) .  But the book didn't have show it
>that way - really!!!  Really really!!


Your BOOK you are using for your COBOL class is NOT a reference manual. It
IS a book used to present things the author thinks you need to know. In the
majority of these instances, save some of the books published by readers of
this newsgroup, these books have many errors.

When something in a manual causes an error, ALWAYS refer to the manual which
is specific to your compiler.

A REFERENCE MANUAL specifically describes the syntax used by a particular
compiler. Thus it "should" be more acurate than a book for a class, not
necessarily written for one particular compiler. Further, these books are
not always written by one author, these authors may also not be using the
same compiler.

Books for college courses are created by corporations in most cases.
Sometimes even by the professors teaching the course. In both instances this
is a conflict of interest because of the money involved. The truth about a
course is then not the most important factor in writing the book. Making
money is. Therefore to meet deadlines the books are not thoroughly revied
for errors. Thus the sad state of college books.
```

###### ↳ ↳ ↳ Re: Ref modification _ thanks!!

- **From:** georgekorz@cs.com (George K)
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000112000125.24451.00000090@nso-cj.news.cs.com>`
- **References:** `<fVOd4.789$%%6.5646@typhoon.columbus.rr.com>`

```
And paying $75 for a paperback bound book of 120 error laden pages really ticks
me off!
GK (A student in his final semester.)

George K
```

#### ↳ Re: Student needs help with reference modification

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3876B118.3F41D4BA@worldnet.att.net>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
Pat wrote:
> 
> Hi,
…[30 more quoted lines elided]…
> to the last.

Could also be done with the ever handy STRING verb:

STRING  IR-EMPLOYEE-NUMBER (1:3) '-'
	IR-EMPLOYEE-NUMBER (4:2) '-'
	IR-EMPLOYEE-NUMBER (6:)
    DELIMITED BY SIZE INTO DL-EMPLOYEE-NUMBER
END-STRING

This approach still uses reference modification. I'm not 100% certain
it's legal to use reference modification on a numeric field, but that's
easily handled if it isn't.

Bill Lynch
```

##### ↳ ↳ Re: Student needs help with reference modification

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<856eso$bcus$1@newssvr03-int.news.prodigy.com>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net> <3876B118.3F41D4BA@worldnet.att.net>`

```

> This approach still uses reference modification. I'm not 100% certain
> it's legal to use reference modification on a numeric field, but that's
> easily handled if it isn't.
>
> Bill Lynch

Reference modification works on any field whose usage is display.
```

##### ↳ ↳ Re: Student needs help with reference modification

- **From:** "Pat" <patp@cpinternet.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QzHd4.1917$Mp.7647@newsfeed.slurp.net>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net> <3876B118.3F41D4BA@worldnet.att.net>`

```
Bill Lynch wrote in response to my question:

>Could also be done with the ever handy STRING verb:

>STRING  IR-EMPLOYEE-NUMBER (1:3) '-'
>IR-EMPLOYEE-NUMBER (4:2) '-'
>IR-EMPLOYEE-NUMBER (6:)
>   DELIMITED BY SIZE INTO DL-EMPLOYEE-NUMBER
>END-STRING


Ooh, a new one on this student (most things are....;-)  )

I'll have to look this up and keep it in mind for future reference.
Thanks!

Pat
```

#### ↳ Re: Student needs help with reference modification

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8542ln$r6m$2@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net>`

```
    You forgot the ( ) around the reference mod, ie ABCD (2:3)  for chars 2,
3, and 4 of ABCD.



Pat <patp@cpinternet.com> wrote in message
news:rlfd4.639$i9.4083@newsfeed.slurp.net...
> Hi,
>
…[3 more quoted lines elided]…
> message "reserved word missing or incorrectly used".  I've got this typed
in
> as our book shows, but the book is sometimes wrong.  We're using MF
Personal
> COBOL 2.0, and at times the book has shown some compiler specific things
for
> RM (for example, EBCDIC vs. ASCII embedded negative signs).  I wouldn't
> think this is a compiler thing, but for the life of me I can't see what
I've
> missed.  I'm sure it's one of those "Duh!" things (they usually are!).
>
…[18 more quoted lines elided]…
> DL-EMPLOYEE-NUMBER-1, the 4th and 5th to DL-EMPLOYEE-NUMBER-3, and the
rest
> to the last.
>
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Student needs help with reference modification

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3875D235.11FF3827@zip.com.au>`
- **References:** `<rlfd4.639$i9.4083@newsfeed.slurp.net> <8542ln$r6m$2@ssauraaa-i-1.production.compuserve.com>`

```
Russell Styles wrote:
> 
>     You forgot the ( ) around the reference mod, ie ABCD (2:3)  for chars 2,
…[47 more quoted lines elided]…
> >


Can't you use a simple picture field 999-99-9999?

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
