[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Revisiting an Old Prejudice: READ INTO/WRITE FROM

_105 messages · 25 participants · 2004-08 → 2004-09_

---

### Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T09:42:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetdfp$mnk$1@panix5.panix.com>`

```

So... I was being consulted on a program's design and mention was made of 
the FD; reflexively I responded that the record layout in the FD should be 
as simple as possible, e.g.

 FD  INFILE
     BLOCK CONTAINS 0 RECORDS
                            .
 01  INFILE-REC        PIC X(160).

... and that everything should be dealt with in WORKING-STORAGE using READ 
INTO and WRITE FROM.

This, of course, is what was taught to me lo, those many decades back; the 
specific of 'Thou shalt not perform arithmetic manipulations in file 
buffers' was expanded into the zero-tolerance rule of 'Thou shalt not 
touch file buffers; all will be done in WORKING-STORAGE via READ INTO and 
WRITE FROM.'

A few years back... not too long ago, maybe 1988, 1989, I was called in to 
help a coder who was getting some whacky results... and sure enough, he 
was doing arithmetice manipulations on the FDand the numbers were coming 
out screwy. Granted, the platform was WANG VS... but the Ancient Teaching 
was proven right.

Things have changed since then, of course, and the Thou Shalt/Shalt Nots 
dating back to ENIAC may no longer be applicable... so I wonder:

Does anyone know of harm/damage/bad stuff (outside of that which can be 
chalked up to sloppiness, e.g. changing a key's position/length and not 
updating the WORKING-STORAGE layout to match) which might happen due to 
continuing to adhere to this?  What is more likely to Go Wrong by holding 
to this 'standard'?

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Pat Hall <phall@notsospam.certcoinc.com>
- **Date:** 2004-08-05T08:55:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10h4f1gnb8gv9eb@corp.supernews.com>`
- **In-Reply-To:** `<cetdfp$mnk$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
I still adhere to it.  If there is a problem I haven't seen it but then 
old habits,  especially ones with historical merit, die hard.  Besides 
if I always do it the same way it sure is easier to debug.

PatH

docdwarf@panix.com wrote:

> So... I was being consulted on a program's design and mention was made of 
> the FD; reflexively I responded that the record layout in the FD should be 
…[32 more quoted lines elided]…
>
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-05T14:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41124383.391260382@news.optonline.net>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>So... I was being consulted on a program's design and mention was made of 
>the FD; reflexively I responded that the record layout in the FD should be 
…[8 more quoted lines elided]…
>INTO and WRITE FROM.

That's not as simple as possible. This is:

FD  INFILE.
01  PIC X(160).
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T10:54:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cethnv$6eg$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <41124383.391260382@news.optonline.net>`

```
In article <41124383.391260382@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[15 more quoted lines elided]…
>01  PIC X(160).

Do tell, Mr Wagner... how is your record layout of X(160) simpler than any 
other record layout of X(160)?

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-05T08:58:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetlfj$26th$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <41124383.391260382@news.optonline.net> <cethnv$6eg$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:cethnv$6eg$1@panix5.panix.com...
> In article <41124383.391260382@news.optonline.net>,
> >That's not as simple as possible. This is:
…[5 more quoted lines elided]…
> other record layout of X(160)?

I think he was commenting on the BLOCK CONTAINS clause.

But I'll go you one better:

    FD  INFILE.

is sufficient in 2002 COBOL; the record description is optional.  READ ...
INTO you already have had for decades.  What makes this possible is the new
WRITE FILE <filename> FROM <identifier>.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T12:39:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetnri$1hv$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <41124383.391260382@news.optonline.net> <cethnv$6eg$1@panix5.panix.com> <cetlfj$26th$1@si05.rsvl.unisys.com>`

```
In article <cetlfj$26th$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
><docdwarf@panix.com> wrote in message news:cethnv$6eg$1@panix5.panix.com...
>> In article <41124383.391260382@news.optonline.net>,
…[8 more quoted lines elided]…
>I think he was commenting on the BLOCK CONTAINS clause.

I think so, also... and I also think that the BLOCK CONTAINS clause is a 
part of the File Description, not the record layout.

>
>But I'll go you one better:
…[3 more quoted lines elided]…
>is sufficient in 2002 COBOL; the record description is optional.

Looks like I'll have something to implement, then, in another couple o' 
decades.  Speaking of which... I was talking with a lad about different 
approaches in coding and put together the following two examples:

Perform Until eof
    Read Infile Into wk-inrec
        At End 
            Set eof To True
        Not At End
            Evaluate wk-inrec(1:1)
                When 1
                When 6
                    Continue
                When 2
                    Perform Process-Typ2
                When 5
                    Perform Process-Typ5
            End-Evaluate
    End-Read
End-Perform

... and ...

    PERFORM MAINLINE THRU M-EX UNTIL EOF.

MAINLINE.
    PERFORM READ-INFILE THRU RI-EX.
    IF EOF
        GO TO M-EX.
    IF WK-INREC-CHAR1 = 1 OR 6
        GO TO ME-EX.
    IF WK-INREC-CHAR1 = 2
        PERFORM PROCESS-TYP2 THRU P-T2-EX.
    IF WK-INREC-CHAR1 = 5
        PERFORM PROCESS-TYP5 THRU P-T5-EX.

... and then I started laughing.  What caused me mirth is that when I 
started coding in 'OLDBOL' I dropped all uses of '85-or-above 
constructs... no reference-modification, no Evaluate... reflexively coding 
with '74 limitations.

It reminded me of folks I know who will, say, discuss matters of calculus 
in English... but when they are adding up the receipt in a restaurant will 
fall back into the language in which they first learned their numbers, 
German, Italian, Hindi or what-have-you.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-06T13:28:10-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf0bl5$qnm$1@news.eusc.inter.net>`
- **In-Reply-To:** `<cetlfj$26th$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <41124383.391260382@news.optonline.net> <cethnv$6eg$1@panix5.panix.com> <cetlfj$26th$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:

> <docdwarf@panix.com> wrote in message news:cethnv$6eg$1@panix5.panix.com...
> 
…[23 more quoted lines elided]…
> 
That extension makes the practice Doc referred to safe and not subject 
to problems when the length of the record changes and all of the 
corresponding records in the various FDs are not changed.  My personal 
preference is to have the record description in question used with all 
of the appropriate FD statements and put up with, in my controversial 
opinion, is the odious syntax for qualification.  That way I know that 
when the record description is changed, all places in the program that 
deal with the record are properly updated.

Incidentally, has IBM changed from defaulting to BLOCK 1 record when the 
description for a Non-VSAM file has "FD file-name."?  If it hasn't, in 
the environments Doc normally works in, "FD file-name BLOCK 0." is still 
needed for the non-VSAM data sets.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-08-07T04:04:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6xYQc.401165$Gx4.357662@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<cf0bl5$qnm$1@news.eusc.inter.net>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <41124383.391260382@news.optonline.net> <cethnv$6eg$1@panix5.panix.com> <cetlfj$26th$1@si05.rsvl.unisys.com> <cf0bl5$qnm$1@news.eusc.inter.net>`

```


Clark F. Morris, Jr. wrote:
> (snip) 
> Incidentally, has IBM changed from defaulting to BLOCK 1 record when the 
> description for a Non-VSAM file has "FD file-name."?  If it hasn't, in 
> the environments Doc normally works in, "FD file-name BLOCK 0." is still 
> needed for the non-VSAM data sets.

As far as I know IBM still defaults to BLOCK 1, even in Enterprise 
COBOL for z/OS.  I fixed a batch program within the last year or two 
that took 20 minutes to run, but with BLOCK CONTAINS 0 RECORDS the 
runtime was reduced to well under one minute.

With larger files the performance improvement is even more valuable.

And as to DocDwarf's original question, I was also taught to always 
READ INTO and WRITE FROM.  It might not always be necessary, but I 
don't see that it hurts anything to keep doing it that way.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-07T08:52:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf2jb1$fn8$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlfj$26th$1@si05.rsvl.unisys.com> <cf0bl5$qnm$1@news.eusc.inter.net> <6xYQc.401165$Gx4.357662@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <6xYQc.401165$Gx4.357662@bgtnsc04-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>And as to DocDwarf's original question, I was also taught to always 
>READ INTO and WRITE FROM.  It might not always be necessary, but I 
>don't see that it hurts anything to keep doing it that way.

zzzzZZZZzzzzz.... zzzzzaaaaAAAAWWWKKKHHHhhhhh... huh? whuh?  Dear me, did 
someone actually address the question?  Thanks much, Mr Trembley.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-25T00:11:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xOQWc.32745$9Y6.2697@newsread1.news.pas.earthlink.net>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <41124383.391260382@news.optonline.net> <cethnv$6eg$1@panix5.panix.com> <cetlfj$26th$1@si05.rsvl.unisys.com> <cf0bl5$qnm$1@news.eusc.inter.net> <6xYQc.401165$Gx4.357662@bgtnsc04-news.ops.worldnet.att.net>`

```
There is an existing SHARE requirement for IBM to use SMS for blocking when the
BLOCK CONTAINS clause isn't coded.  It hasn't been marked "available" yet - but
did receive a semi-positive reply.
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2004-08-05T08:03:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10h4j2ef43alcfd@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message:
> This, of course, is what was taught to me lo, those many decades back; the
> specific of 'Thou shalt not perform arithmetic manipulations in file
> buffers' was expanded into the zero-tolerance rule of 'Thou shalt not
> touch file buffers; all will be done in WORKING-STORAGE via READ INTO and
> WRITE FROM.'

I don't think I've heard this before--avoiding arithmetic manipulations in
file buffers.  Is it a performance thing with some compilers?  Could you
give an example of what needs to be avoided?

Walter
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T11:22:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetjbb$ci2$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com>`

```
In article <10h4j2ef43alcfd@corp.supernews.com>,
Walter Murray <wmurray@midtown.net> wrote:
><docdwarf@panix.com> wrote in message:
>> This, of course, is what was taught to me lo, those many decades back; the
…[6 more quoted lines elided]…
>file buffers.  Is it a performance thing with some compilers?

From the posting to which you responded, the paragraph immediately 
following the above:

--begin quoted text:

A few years back... not too long ago, maybe 1988, 1989, I was called in to
help a coder who was getting some whacky results... and sure enough, he
was doing arithmetice manipulations on the FDand the numbers were coming
out screwy. Granted, the platform was WANG VS... but the Ancient Teaching
was proven right.

--end quoted text

>Could you
>give an example of what needs to be avoided?

Arithmetic manipulations... things like ADD, SUBTRACT, MULTIPLY, DIVIDE 
and COMPUTE, for a start.

FD  INFILE.
01  INREC.
    05  INREC-NUMFLD1 PIC S9(5)V99 COMP-3.
    05  INREC-NUMFLD2 PIC S9(5)V99 COMP-3.
    05  INREC-NUMFLD3 PIC S9(5)V99 COMP-3.
    05  INREC-NUMFLD4 PIC S9(5)V99 COMP-3.

ADD INREC-NUMFLD1 TO INREC-NUMFLD2.
DIVIDE INREC-NUMFLD1 BY INREC-NUMFLD4.
SUBTRACT 3.14 FROM INREC-NUMFLD3.
MULTIPLY INREC-NUMFLD3 BY 5.

... and suchlike.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2004-08-05T14:32:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10h59rl1im2ob45@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote:
> Walter Murray <wmurray@midtown.net> wrote:
> >Could you
…[17 more quoted lines elided]…
> ... and suchlike.

That's what I thought you were saying.  But this is perfectly legal standard
COBOL, right?  (Well, except for the missing GIVING phrases on the DIVIDE
and the MULTIPLY, and the use of COMP-3, a common extension.)

Are you saying that some compilers are defective and give the wrong results
for the statements above?

Or, perhaps, are you referring to the unpredictable things that can happen
if you access a file's record area when it is not available, such as after
the file has been closed?

Walter
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T20:27:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ceuj9t$cn3$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com>`

```
In article <10h59rl1im2ob45@corp.supernews.com>,
Walter Murray <wmurray@midtown.net> wrote:
><docdwarf@panix.com> wrote:
>> Walter Murray <wmurray@midtown.net> wrote:
…[25 more quoted lines elided]…
>for the statements above?

I've said what I've said, sometimes twice now.  For the third and last 
time:

from 
<http://groups.google.com/groups?selm=cetdfp%24mnk%241%40panix5.panix.com&output=gplain>

--begin quoted text:

This, of course, is what was taught to me lo, those many decades back; the 
specific of 'Thou shalt not perform arithmetic manipulations in file 
buffers' was expanded into the zero-tolerance rule of 'Thou shalt not 
touch file buffers; all will be done in WORKING-STORAGE via READ INTO and 
WRITE FROM.'

A few years back... not too long ago, maybe 1988, 1989, I was called in to 
help a coder who was getting some whacky results... and sure enough, he 
was doing arithmetice manipulations on the FDand the numbers were coming 
out screwy. Granted, the platform was WANG VS... but the Ancient Teaching 
was proven right.

--end quoted text

from 
<http://groups.google.com/groups?selm=cetjbb%24ci2%241%40panix5.panix.com&output=gplain>

--begin quoted text:

From the posting to which you responded, the paragraph immediately 
following the above:

--begin quoted text:

A few years back... not too long ago, maybe 1988, 1989, I was called in to
help a coder who was getting some whacky results... and sure enough, he
was doing arithmetice manipulations on the FDand the numbers were coming
out screwy. Granted, the platform was WANG VS... but the Ancient Teaching
was proven right.

--end quoted text

--end quoted text

You've read all this previously, I hope... what do you find to be unclear?  
I told you what I was taught, I told you what I have experienced.

>
>Or, perhaps, are you referring to the unpredictable things that can happen
>if you access a file's record area when it is not available, such as after
>the file has been closed?

Read what I wrote, Mr Murray.  What I said, what I intended and what I 
referred to is all right there.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2004-08-05T22:04:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rfmdnUDvx-K-eo_cRVn-tQ@comcast.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com>`

```
Cripes, calm down.  I'm pretty sure he knew what you wrote, as do I.  But I
would have the same question - WHY?

OK, you said "I was taught..." and "I experienced...".  Didn't you want to
know WHY there was a problem?  It doesn't seem to me like there should be
any problem with it.

I've been programming Cobol for 18 years on Unix & Windows systems, and I've
never encountered problems doing math on fields in FD's with those
platforms/compilers.  Years ago, I did see code that insisted on moving
everything from FD fields into Working Storage after reads and vice versa
before writes/rewrites, but no one could ever give me a good reason why it
was done.  The only reason I ever came up with was the usage of SAME AREA,
which only seemed useful when memory was at a premium.

<docdwarf@panix.com> wrote in message news:ceuj9t$cn3$1@panix5.panix.com...
> In article <10h59rl1im2ob45@corp.supernews.com>,
> Walter Murray <wmurray@midtown.net> wrote:
…[22 more quoted lines elided]…
> >That's what I thought you were saying.  But this is perfectly legal
standard
> >COBOL, right?  (Well, except for the missing GIVING phrases on the DIVIDE
> >and the MULTIPLY, and the use of COMP-3, a common extension.)
> >
> >Are you saying that some compilers are defective and give the wrong
results
> >for the statements above?
>
…[4 more quoted lines elided]…
>
<http://groups.google.com/groups?selm=cetdfp%24mnk%241%40panix5.panix.com&ou
tput=gplain>
>
> --begin quoted text:
…[16 more quoted lines elided]…
>
<http://groups.google.com/groups?selm=cetjbb%24ci2%241%40panix5.panix.com&ou
tput=gplain>
>
> --begin quoted text:
…[20 more quoted lines elided]…
> >Or, perhaps, are you referring to the unpredictable things that can
happen
> >if you access a file's record area when it is not available, such as
after
> >the file has been closed?
>
…[3 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-05T23:13:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408052213.4f61da38@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com>`

```
"JJ" <jj@nospam.com> wrote

> I've been programming Cobol for 18 years on Unix & Windows systems, and I've
> never encountered problems doing math on fields in FD's with those
…[4 more quoted lines elided]…
> which only seemed useful when memory was at a premium.

Some versions of Fujitsu Cobol, such as on Linux, do not allow access
to record areas before an open or after a close.  It gives a
segmentation fault which presumably is because the record areas are
created dynamically upon OPEN.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 7)_

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-08-06T08:49:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pCHQc.2991$7l3.1812@newssvr23.news.prodigy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <217e491a.0408052213.4f61da38@posting.google.com>`

```

I wasn't aware that Cobol programming was done on ascii type
systems. At least not to any great degree.

Why would you use Cobol in these environments. I'm very curious.

Thanks,

Gary



"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0408052213.4f61da38@posting.google.com...
> "JJ" <jj@nospam.com> wrote
>
> > I've been programming Cobol for 18 years on Unix & Windows systems, and
I've
> > never encountered problems doing math on fields in FD's with those
> > platforms/compilers.  Years ago, I did see code that insisted on moving
> > everything from FD fields into Working Storage after reads and vice
versa
> > before writes/rewrites, but no one could ever give me a good reason why
it
> > was done.  The only reason I ever came up with was the usage of SAME
AREA,
> > which only seemed useful when memory was at a premium.
>
…[3 more quoted lines elided]…
> created dynamically upon OPEN.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 8)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-06T07:43:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vOadneNaTu-b4I7cRVn-sg@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <217e491a.0408052213.4f61da38@posting.google.com> <pCHQc.2991$7l3.1812@newssvr23.news.prodigy.com>`

```
The Family wrote:
> I wasn't aware that Cobol programming was done on ascii type
> systems. At least not to any great degree.
…[5 more quoted lines elided]…
> Gary

Because our customers can't afford a mainframe?
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-06T08:54:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cevv1h$j67$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <217e491a.0408052213.4f61da38@posting.google.com> <pCHQc.2991$7l3.1812@newssvr23.news.prodigy.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com>`

```
In article <vOadneNaTu-b4I7cRVn-sg@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>The Family wrote:
>> I wasn't aware that Cobol programming was done on ascii type
…[8 more quoted lines elided]…
>Because our customers can't afford a mainframe?

Ignoring, for the moment, that answering a question with a question is no 
answer at all... it might be that they cannot afford a mainframe... or 
perhaps because they don't need a mainframe... or perhaps because the 
problem at hand is best - or at least capably - addressed by using the 
tool of COBOL.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 10)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-06T15:33:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<srudnTMiTr2Sdo7cRVn-og@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <217e491a.0408052213.4f61da38@posting.google.com> <pCHQc.2991$7l3.1812@newssvr23.news.prodigy.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <vOadneNaTu-b4I7cRVn-sg@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[16 more quoted lines elided]…
> addressed by using the tool of COBOL.

My mistake. The response should have read:

"Because our customers can't afford a mainframe."
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-06T19:26:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf143d$bdj$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com>`

```
In article <srudnTMiTr2Sdo7cRVn-og@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>> In article <vOadneNaTu-b4I7cRVn-sg@giganews.com>,
…[19 more quoted lines elided]…
>"Because our customers can't afford a mainframe."

Well, now, that makes *all* the difference; my reply to your response 
would then have read:

'It might be that some cannot afford a mainframe... or perhaps because 
some don't need a mainframe... or perhaps because the problem at hand is 
best - or at least capably - addressed by using the tool of COBOL.'

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 12)_

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-08-07T01:21:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com>`

```

Well, I guess my question should have been....

"I would be interested in learning more about Cobol on a non-main-
frame environment. Where might I look to get more information"?

Thanks - Gary



<docdwarf@panix.com> wrote in message news:cf143d$bdj$1@panix5.panix.com...
> In article <srudnTMiTr2Sdo7cRVn-og@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[31 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 13)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-06T21:34:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9YmdnZ9MetZQooncRVn-pQ@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>`

```
The Family wrote:
> Well, I guess my question should have been....
>
…[3 more quoted lines elided]…
> Thanks - Gary

You can ask here - what would you like to know?

Bear in mind that COBOL worked fine on 64K 360-Mod30 back in the '60s.
Today's desktop PCs are magnitudes more powerful so there's no real
impediment to COBOL's use.

Here's the Fujitsu COBOL main page:

www.adtools.com
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 14)_

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-08-07T03:33:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4YQc.2440$L45.1002@newssvr24.news.prodigy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com> <9YmdnZ9MetZQooncRVn-pQ@giganews.com>`

```

Well, I wanted to know how Cobol handled screen management,
and a myriad of other things that I won't bother you with now.

I'll look at the site, and return with specific questions, if necessary.

Thanks, for the info,

Gary




"JerryMouse" <nospam@bisusa.com> wrote in message
news:9YmdnZ9MetZQooncRVn-pQ@giganews.com...
> The Family wrote:
> > Well, I guess my question should have been....
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-07T08:55:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf2jfn$g3j$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>`

```
In article <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>,
The Family <lgvwalk@swbell.net> wrote:
>
>Well, I guess my question should have been....
>
>"I would be interested in learning more about Cobol on a non-main-
>frame environment. Where might I look to get more information"?

You might start at the ever-popular 
http://www.cobolreport.com/faqs/cobolfaq.htm

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 14)_

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-08-07T14:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1P5Rc.3397$ZC7.2407@newssvr24.news.prodigy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com> <cf2jfn$g3j$1@panix5.panix.com>`

```

Thanks,


Gary



<docdwarf@panix.com> wrote in message news:cf2jfn$g3j$1@panix5.panix.com...
> In article <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>,
> The Family <lgvwalk@swbell.net> wrote:
…[9 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 13)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-08-07T15:02:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf2qta0scc@news3.newsguy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>`

```

In article <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>, "The Family" <lgvwalk@swbell.net> writes:
> 
> Well, I guess my question should have been....
> 
> "I would be interested in learning more about Cobol on a non-main-
> frame environment. Where might I look to get more information"?

Straight lines like that almost make me wish I were in sales...

There are a few odds and ends about COBOL on non-mainframe platforms
(and some mainframe ones) at http://www.microfocus.com.  We've been
selling COBOL for non-mainframe platforms for almost 30 years now.

COBOL is quite popular on Windows and Unix, for much the reason Doc
suggested - people want to get something done, and they have COBOL
developers available who can do it.  And, sometimes, for the reason
Jerry suggested: they believe they can do it cheaper on one of those
platforms than on a mainframe.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 14)_

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-08-08T03:22:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g0hRc.3511$QL3.1231@newssvr24.news.prodigy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com> <cf2qta0scc@news3.newsguy.com>`

```

Yes, I am quite familiar with Cobol, and with the fact that Micro-
Focus builds one for many platforms. However, I've never used
your product, but know others that have.

I just thought I might experiment with Cobol on a PC to see how
it works. I don't want to get into $1,000's just for experimentation.

After looking at the Fujitsu site, I can see that like most things on a
PC, 100's of decisions<g> have to be made concerning platform
(Win, .NET, etc).


Thanks - Gary




"Michael Wojcik" <mwojcik@newsguy.com> wrote in message
news:cf2qta0scc@news3.newsguy.com...
>
> In article <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com>, "The Family"
<lgvwalk@swbell.net> writes:
> >
> > Well, I guess my question should have been....
…[23 more quoted lines elided]…
>  -- Walt Kelly
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-08T18:32:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IkuRc.52368$J06.32462@pd7tw2no>`
- **In-Reply-To:** `<g0hRc.3511$QL3.1231@newssvr24.news.prodigy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com> <cf2qta0scc@news3.newsguy.com> <g0hRc.3511$QL3.1231@newssvr24.news.prodigy.com>`

```
The Family wrote:

Well Michael may be a superb programmer, (I don't know what his role 
is). For sure, he'd make a lousy salesman  :-)

Other vendors may have tutorial versions of their products, but the 
following extract is more specific :-

Begin quote << A new version of Net Express University Edition has
been released, Net Express with .NET University Edition.  That is Net
Express v4.0 plus the .NET add-on.  If you do not want to install the .NET
stuff you do not have to you can just install v4.0.  The product is the full
product with all functionalities of the GA product with only one
restriction, the maximum number of lines of code allowed per program.  That
limit is 2200.  And the price is $149 USD, http://www.microfocus.com/shop/.
Quite a bargain.  The product does not come with standard maintenance of
course but will be updated on a regular basis as the GA product is.

The product information for that version of Net Express University Edition
can be found here;
http://www.microfocus.com/shop/description.asp?productid=39

 end of quote >>

You're familiar with M/F already, and with above you are ahead of me in the game; I'm still using N/E V.3.1. The above limitation of 2,200 lines is not a serious restriction for experimentation, plus you'll also be familiar with the fact that using the "Ignore the red tape" features, you can leave out syntax you don't need. Of course if you are in the habit of using 'READ INTO ........" since Pontius was a Pilate - then that marginally increases your source line usage  :-) 

Not sure - but I think the University price is subtracted when you buy the full product.
As a University Edition user, you can go to M/F site and sign up for Answer Exchange, (freebie). You can post queries against the sub-heading "University Edition" - anyway you can also access the main Net Express thread for ideas.

Don't let's get delusional - the full price isn't cheap, (you would have to quiz M/F on prices). Plus there are runtime fees. But as a Fujitsu user just replied to me, "Their (F/J) prices are hitting the roof..." as well. F/J doesn't have runtime fees, but on the downside check out their Tech Support, or lack thereof (???)

Michael I'm getting awfully tired of pointing people at Answer Exchange - bitch at your sales people to give you a text extract one of you could post in response to this type of compiler query, plus of course 'suck-it-and-see' using the UE. Now if some "kind person' would give me the the upgrade to N/E 4.0 as a 'freebie' - I would happily post here whatever you want !

Jimmy, Calgary AB

Thanks.


>Thanks - Gary
>
…[44 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 16)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-08-09T13:48:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf7vau0117a@news3.newsguy.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com> <cevv1h$j67$1@panix5.panix.com> <srudnTMiTr2Sdo7cRVn-og@giganews.com> <cf143d$bdj$1@panix5.panix.com> <68WQc.2416$Af4.1696@newssvr24.news.prodigy.com> <cf2qta0scc@news3.newsguy.com> <g0hRc.3511$QL3.1231@newssvr24.news.prodigy.com> <IkuRc.52368$J06.32462@pd7tw2no>`

```

In article <IkuRc.52368$J06.32462@pd7tw2no>, "James J. Gavan" <jjgavan@shaw.ca> writes:
>
> Well Michael may be a superb programmer, (I don't know what his role 
> is).

These days, it's mostly the comms infrastructure for Enterprise
Server, and before that it was various MF middleware products.  It's
only recently that I've actually been using MF COBOL myself to any
significant extent.

> For sure, he'd make a lousy salesman  :-)

Ah well.  I shall continue to labor in the code pits.

> [snip helpful description of University Edition]
> Michael I'm getting awfully tired of pointing people at Answer
> Exchange - bitch at your sales people to give you a text extract one
> of you could post in response to this type of compiler query, plus of
> course 'suck-it-and-see' using the UE.

To be fair, I think they do provide product-description boilerplate
from time to time.  I just toss it in some email folder somewhere
and forget about it.  (I *would* make a lousy salesman.)  You're
right, though - I should dig it out for occasions like this.

Thanks for mentioning UE.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-06T12:46:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408061146.3d5b7e6d@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <217e491a.0408052213.4f61da38@posting.google.com> <pCHQc.2991$7l3.1812@newssvr23.news.prodigy.com> <vOadneNaTu-b4I7cRVn-sg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> > I wasn't aware that Cobol programming was done on ascii type
> > systems. At least not to any great degree.
> 
> Because our customers can't afford a mainframe?

That seems to make the assumption that all mainframes are 'EDCDIC type
systems'.

Many decades ago I worked on mainframes that, while not ASCII - they
weren't American, were 'ascii type'.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-06T05:14:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cevi5h$6p5$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com>`

```
In article <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com>, JJ <jj@nospam.com> wrote:
>Cripes, calm down.  I'm pretty sure he knew what you wrote, as do I.

This *is* calm, actually... 'so cold he burns, no wonder some think he is 
on fire', as Nietzsche put it.

>But I
>would have the same question - WHY?

I was not asked 'WHY', I was asked, repeatedly, 'are you saying that'... 
when what I said was, according to quotation, apparently clear.

>
>OK, you said "I was taught..." and "I experienced...".  Didn't you want to
>know WHY there was a problem?

Had I wanted to know this it just might be possible that I would have 
posted a thread which mentioned it in a forum of professionals who might 
be able to address the matter.

>It doesn't seem to me like there should be
>any problem with it.

It doesn't seem to me that there should be any reason for bodies to be 
attracted to each other with a force that is inversely proportional to the 
square of the distance between their centers, as well... what's Life 
without a bit of Mystery?

>
>I've been programming Cobol for 18 years on Unix & Windows systems, and I've
…[5 more quoted lines elided]…
>which only seemed useful when memory was at a premium.

Thrice now it has been posted what I was taught and thrice what I 
experienced... perhaps someone else might be able to say more, incessant 
repetition wearies me.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** Paul Knudsen <HughG@dodgeit.com>
- **Date:** 2004-08-21T06:20:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com>`

```
On Thu, 5 Aug 2004 22:04:20 -0400, "JJ" <jj@nospam.com> wrote:

>But I
>would have the same question - WHY?
…[3 more quoted lines elided]…
>any problem with it.

The way I heard it,  it was for dumps.  Apparently in the old days
they either didn't include the file area, or included the whole thing
and you had to count down to find the current record.  So if the CR
was in WS, you could find it much quicker.  Makes sense I suppose.

Me, I quit looking at dumps when debuggers came out.  Never needed
READ INTO since.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-24T17:10:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgfsqi$28v$1@peabody.colorado.edu>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com>`

```

On 21-Aug-2004, Paul Knudsen <HughG@dodgeit.com> wrote:

> The way I heard it,  it was for dumps.  Apparently in the old days
> they either didn't include the file area, or included the whole thing
> and you had to count down to find the current record.  So if the CR
> was in WS, you could find it much quicker.  Makes sense I suppose.

That's what I was told in 1980.   We put fillers in our Working Storage to make
it easier to find stuff.

> Me, I quit looking at dumps when debuggers came out.  Never needed
> READ INTO since.

Formatted dumps really made things easier.   I haven't found a debugger yet that
made mainframe batch CoBOL easier.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-25T09:25:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ijloi0d6fgr80p6t9hcokbnl68ef6ekeli@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <cgfsqi$28v$1@peabody.colorado.edu>`

```
On Tue, 24 Aug 2004 17:10:42 GMT, "Howard Brazee" <howard@brazee.net>
wrote:

>  I haven't found a debugger yet that made mainframe batch CoBOL easier.

The fastest debugger can read source and SEE what it does before it's
executed even once. Preemptive debugging. It doesn't cost anything
(extra) but it's seldom used.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-25T08:54:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-71F196.08541725082004@knology.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <cgfsqi$28v$1@peabody.colorado.edu>`

```
In article <cgfsqi$28v$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:

> On 21-Aug-2004, Paul Knudsen <HughG@dodgeit.com> wrote:
> 
…[7 more quoted lines elided]…
> it easier to find stuff.


There was/is a shop standard that says each programs should have, as the 
first and last item in working storage, an 01-level containing text like 
"Working Storage Starts Here".

It was a cute idea.

But about the same time the Endevor group turned on the OPTIMIZE option 
on the compiler.

So when looking at a dump of storage, you will often see something like:

WORKING STORAGE STARTS HERE><WORKING STORAGE ENDS HERE.OTHER UNALTERED 
CONSTANTS THAT WERE IN 01-LEVEL ITEMS.  BLAH.  BLAH. BLAH.

The compiler felt free to reorder the 01-items, making the practice 
somewhat humorous.



> > Me, I quit looking at dumps when debuggers came out.  Never needed
> > READ INTO since.
…[3 more quoted lines elided]…
> made mainframe batch CoBOL easier.

Have you seen IBM Debug Tool with distributed debugger?  It is 
wonderful.  You specify your IP address as an LE Test Parm, e.g:

         EXEC PGM=WHATEVER,PARM='something/TEST(10.10.10.10)'

And run the debugger client on your workstation.  When WHATEVER begins 
executing your workstations debugging client will have control.  It 
looks alot like any other PC-IDE debugger.  You can scroll through the 
entire source, view all working storage in the watch box, etc.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-25T14:33:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgi7v1$b0j$1@peabody.colorado.edu>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <cgfsqi$28v$1@peabody.colorado.edu> <joe_zitzelberger-71F196.08541725082004@knology.usenetserver.com>`

```

On 25-Aug-2004, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> Have you seen IBM Debug Tool with distributed debugger?  It is
> wonderful.  You specify your IP address as an LE Test Parm, e.g:
…[6 more quoted lines elided]…
> entire source, view all working storage in the watch box, etc.

I think I tried it once at a different shop.  It looks familiar.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 9)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-08-26T12:59:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2p6q8qFgu2g1U1@uni-berlin.de>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <cgfsqi$28v$1@peabody.colorado.edu> <joe_zitzelberger-71F196.08541725082004@knology.usenetserver.com>`

```
Wow, that looks great!  Too bad, once again, it's not (or does not appear to
be) availible for VSE.

How do you initiate it for CICS transactions?  

I've never actually used IBM Debug Tool, as it looked to me to not be very
user friendly or dynamically interactive, at least if used only on the
mainframe.  Does anyone agree with this?  Does anyone use IBM Debug Tool and
prefer it over, say, Intertest or Xpediter?



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> Joe Zitzelberger<joe_zitzelberger@nospam.com> 8/25/2004 6:54:17 AM >>>
In article <cgfsqi$28v$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:

> On 21-Aug-2004, Paul Knudsen <HughG@dodgeit.com> wrote:
> 
…[5 more quoted lines elided]…
> That's what I was told in 1980.   We put fillers in our Working Storage to

> make
> it easier to find stuff.


There was/is a shop standard that says each programs should have, as the 
first and last item in working storage, an 01-level containing text like 
"Working Storage Starts Here".

It was a cute idea.

But about the same time the Endevor group turned on the OPTIMIZE option 
on the compiler.

So when looking at a dump of storage, you will often see something like:

WORKING STORAGE STARTS HERE><WORKING STORAGE ENDS HERE.OTHER UNALTERED 
CONSTANTS THAT WERE IN 01-LEVEL ITEMS.  BLAH.  BLAH. BLAH.

The compiler felt free to reorder the 01-items, making the practice 
somewhat humorous.



> > Me, I quit looking at dumps when debuggers came out.  Never needed
> > READ INTO since.
> 
> Formatted dumps really made things easier.   I haven't found a debugger
yet 
> that
> made mainframe batch CoBOL easier.

Have you seen IBM Debug Tool with distributed debugger?  It is 
wonderful.  You specify your IP address as an LE Test Parm, e.g:

         EXEC PGM=WHATEVER,PARM='something/TEST(10.10.10.10)'

And run the debugger client on your workstation.  When WHATEVER begins 
executing your workstations debugging client will have control.  It 
looks alot like any other PC-IDE debugger.  You can scroll through the 
entire source, view all working storage in the watch box, etc.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 10)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-26T23:10:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-96A83A.23105226082004@knology.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <cgfsqi$28v$1@peabody.colorado.edu> <joe_zitzelberger-71F196.08541725082004@knology.usenetserver.com> <2p6q8qFgu2g1U1@uni-berlin.de>`

```
the same way... just put your IP or your NETNAME in the DBTC trans 
fields, with the program or tran you want to trap.  The screen will pop 
and you will be in control.

Very easy...

In article <2p6q8qFgu2g1U1@uni-berlin.de>,
 "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote:

> Wow, that looks great!  Too bad, once again, it's not (or does not appear to
> be) availible for VSE.
…[70 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 7)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-08-24T18:19:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R9PWc.19769$DG.793041@news20.bellglobal.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com>`

```

"Paul Knudsen" <HughG@dodgeit.com> wrote in message
news:05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com...
> On Thu, 5 Aug 2004 22:04:20 -0400, "JJ" <jj@nospam.com> wrote:
>
<SNIP>
> was in WS, you could find it much quicker.  Makes sense I suppose.
>
> Me, I quit looking at dumps when debuggers came out.  Never needed
> READ INTO since.
> -- 
So what do you do if you have a production abend?  Reproduce the problem
under the debugger?
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-25T09:25:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0kloi090sd7n4gvvb78pete8tfr5uffol0@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <R9PWc.19769$DG.793041@news20.bellglobal.com>`

```
On Tue, 24 Aug 2004 18:19:38 -0400, "Don Leahy"
<leahydon@nospamplease.netscape.net> wrote:

>
>"Paul Knudsen" <HughG@dodgeit.com> wrote in message
…[10 more quoted lines elided]…
>under the debugger?

The Micro Focus debugger (anim) can be run against a dump. It displays
source, same as normal debugging, and puts the cursor on the failing
line. You cannot step through code in that mode, of course, but you
can put the cursor on a data name -- either in procedure or data
division -- to see its value. 

Alternatively, they offer a formatted dump (FaultFinder) similar to
that found on mainframes. The debugger approach is the better of the
two.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 9)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-08-25T18:47:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JF8Xc.22299$DG.1091852@news20.bellglobal.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <R9PWc.19769$DG.793041@news20.bellglobal.com> <0kloi090sd7n4gvvb78pete8tfr5uffol0@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:0kloi090sd7n4gvvb78pete8tfr5uffol0@4ax.com...
> On Tue, 24 Aug 2004 18:19:38 -0400, "Don Leahy"
> <leahydon@nospamplease.netscape.net> wrote:
…[24 more quoted lines elided]…
>
Cool.  If that's true (sorry if that sounds skeptical), then it must be a
later release of anim than the one my current client is stuck with  (vintage
1997) which is of no use at all for debugging mainframe abends.

Our version is so old that, in frustration, some of the programmers are
clamouring to get rid of it, acquire a host debugger, and go back to
developing systems on the mainframe. .
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-26T01:35:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1jfqi0pvhcj3gd4igb1aqk2mv3ek4nj01h@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <ceuj9t$cn3$1@panix5.panix.com> <rfmdnUDvx-K-eo_cRVn-tQ@comcast.com> <05qdi0544d2t2rqvovjv3jl28h06egq5ef@4ax.com> <R9PWc.19769$DG.793041@news20.bellglobal.com> <0kloi090sd7n4gvvb78pete8tfr5uffol0@4ax.com> <JF8Xc.22299$DG.1091852@news20.bellglobal.com>`

```
On Wed, 25 Aug 2004 18:47:15 -0400, "Don Leahy"
<leahydon@nospamplease.netscape.net> wrote:

>
>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
…[34 more quoted lines elided]…
>developing systems on the mainframe. .

The Mainframe Express data sheet says nothing about reading dumps. 
I was describing Server Express, which runs on Unix. 

Have you tried running anim against a dump file? You might have to
copy the dump file to your PC. If the IDE doesn't offer that option,
just run it from the command line 'anim filename'. You might have to
copy the .idy to the current directory.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-14T18:08:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VXwTc.15861$5s3.11403@fe40.usenetserver.com>`
- **In-Reply-To:** `<10h59rl1im2ob45@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com>`

```
Walter Murray wrote:

> <docdwarf@panix.com> wrote:
> 
…[25 more quoted lines elided]…
> and the MULTIPLY, and the use of COMP-3, a common extension.)

Are you saying that the standard mandates GIVING for multiply and divide 
statements?  I'm not sure I concur with that...  In every COBOL I've 
ever used, giving was listed as [GIVING] (meaning it was optional).
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-14T22:21:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfmhbg$q2n$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com>`

```
In article <VXwTc.15861$5s3.11403@fe40.usenetserver.com>,
LX-i  <lxi0007@netscape.net> wrote:
>Walter Murray wrote:
>
…[31 more quoted lines elided]…
>ever used, giving was listed as [GIVING] (meaning it was optional).

I was wondering if someone else would notice that.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-14T23:23:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408142223.70cceb59@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com>`

```
LX-i <lxi0007@netscape.net> wrote

> >>ADD INREC-NUMFLD1 TO INREC-NUMFLD2.
> >>DIVIDE INREC-NUMFLD1 BY INREC-NUMFLD4.
> >>SUBTRACT 3.14 FROM INREC-NUMFLD3.
> >>MULTIPLY INREC-NUMFLD3 BY 5.

> Are you saying that the standard mandates GIVING for multiply and divide 
> statements?  I'm not sure I concur with that...  In every COBOL I've 
> ever used, giving was listed as [GIVING] (meaning it was optional).

The arithmetic operations in the original Cobol were designed such
that the result goes into the final operand, as it does for MOVE.  If
there is a GIVING then that is the final and the result goes there.

In statements without GIVING such as:

   ADD A TO B
   SUBTRACT A FROM B
   MULTIPLY A BY B
   DIVIDE A INTO B

The results go into B.

However, with DIVIDE A BY B logically the result should go into A, but
this would break the rule about final operand.  Thus with DIVIDE .. BY
.. the GIVING is _not_ optional.  It is optional with DIVIDE .. INTO
.. and the other operations.

The MULTIPLY requires a GIVING because the final operand is a literal
which is illegal for a receiving field.  If it had been MULTIPLY 5 BY
InRec-NumFld3 it would have been perfectly valid without a GIVING.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2004-08-15T16:48:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hvthv2lein84a@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com> <217e491a.0408142223.70cceb59@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> However, with DIVIDE A BY B logically the result should go into A, but
> this would break the rule about final operand.  Thus with DIVIDE .. BY
> .. the GIVING is _not_ optional.  It is optional with DIVIDE .. INTO
> .. and the other operations.

It is optional with DIVIDE ... INTO as long as the second operand is not a
numeric literal and the REMAINDER phrase is not specified.

Walter
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-15T23:38:20-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2oal3fF8i45sU1@uni-berlin.de>`
- **In-Reply-To:** `<217e491a.0408142223.70cceb59@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com> <217e491a.0408142223.70cceb59@posting.google.com>`

```
Richard wrote:

> LX-i <lxi0007@netscape.net> wrote
> 
…[32 more quoted lines elided]…
> InRec-NumFld3 it would have been perfectly valid without a GIVING.

According to my 1985 Draft Standard which I assume was carried over from 
previous standards, MULTIPLY A BY B does not require a GIVING clause. 
The result is in B.  This is contrary to the way many of us would read 
the clause and adding a GIVING clause to say MULTIPLY A BY B GIVING B 
would probably be clearer to the non-programmer.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-16T00:21:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408152321.2f857e16@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com> <217e491a.0408142223.70cceb59@posting.google.com> <2oal3fF8i45sU1@uni-berlin.de>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote 

> >>>>MULTIPLY INREC-NUMFLD3 BY 5.

> > In statements without GIVING such as:
> >    ... 
> >    MULTIPLY A BY B
> >    ...
> > The results go into B.
 
> According to my 1985 Draft Standard which I assume was carried over from 
> previous standards, MULTIPLY A BY B does not require a GIVING clause. 

You should note that I covered this.  However, the example above is
invalid because 'B' is a literal which cannot take a result.  Thus if
one wanted to have

    MULTIPLY variable BY literal 

then it _requires_ a GIVING (or reforming so the variale is last).

> The result is in B.  This is contrary to the way many of us would read 
> the clause and adding a GIVING clause to say MULTIPLY A BY B GIVING B 
> would probably be clearer to the non-programmer.

The way one reads such things is the result of what one is used to.  I
learned to recognise that the result went in the last operand - then
they brought in 'modern' innovations such as SET, COMPUTE which broke
this.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-16T11:32:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wk5Uc.23227$5s3.9606@fe40.usenetserver.com>`
- **In-Reply-To:** `<217e491a.0408142223.70cceb59@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com> <217e491a.0408142223.70cceb59@posting.google.com>`

```
Richard wrote:

> LX-i <lxi0007@netscape.net> wrote
> 
…[14 more quoted lines elided]…
> there is a GIVING then that is the final and the result goes there.

Do you know that this is the first time I've heard that?  It makes the 
seemingly backwards behavior, especially of Multiply and Divide, make 
more sense.

> In statements without GIVING such as:
> 
…[14 more quoted lines elided]…
> InRec-NumFld3 it would have been perfectly valid without a GIVING.

Thanks for the clarification - I see now why the original comment was made.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2004-08-15T16:41:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hvt538o7t4o1e@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10h4j2ef43alcfd@corp.supernews.com> <cetjbb$ci2$1@panix5.panix.com> <10h59rl1im2ob45@corp.supernews.com> <VXwTc.15861$5s3.11403@fe40.usenetserver.com>`

```
"LX-i" <lxi0007@netscape.net> wrote:
> Walter Murray wrote:
> > <docdwarf@panix.com> wrote:
…[3 more quoted lines elided]…
> >>MULTIPLY INREC-NUMFLD3 BY 5.

> > That's what I thought you were saying.  But this is perfectly legal
standard
> > COBOL, right?  (Well, except for the missing GIVING phrases on the
DIVIDE
> > and the MULTIPLY, and the use of COMP-3, a common extension.)
>
> Are you saying that the standard mandates GIVING for multiply and divide
> statements?  I'm not sure I concur with that...  In every COBOL I've
> ever used, giving was listed as [GIVING] (meaning it was optional).

Yes, for the example MULTIPLY and DIVIDE statements given, Standard COBOL
requires a GIVING phrase.

A DIVIDE ... BY always requires a GIVING phrase.  A DIVIDE ... INTO requires
a GIVING phrase if the second operand is a numeric literal or if a REMAINDER
phrase is specified.

A MULTIPLY statement requires a GIVING phrase if the second operand is a
numeric literal.

Walter
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-08-05T15:12:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9EGkAgI9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
.    Am  05.08.04
schrieb  docdwarf@panix.com
    auf  /COMP/LANG/COBOL
     in  cetdfp$mnk$1@panix5.panix.com
  ueber  Revisiting an Old Prejudice: READ INTO/WRITE FROM

d> ... and that everything should be dealt with in WORKING-STORAGE using
d> READ INTO and WRITE FROM.

  To me this doesn't make sense.

  If one takes into account the holy principle:
  Thou shalt not trust external data and check it before using it

  So, when you try to do calculations with an item from an imput file  
which is not a number, an error will occur.



Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

  "Nach meiner Ansicht besitzt die Presse _das_ _Recht_,
Schriftsteller, Politiker, Komï¿½dianten und andere ï¿½ffentliche
Charaktere zu _beleidigen_. Achtete ich [so einen Angriff gegen mich]
einer Notiz wert, so galt mir in solchen Fï¿½llen der Wahlspruch: ï¿½
corsaire, corsaire et demi [auf einen Schelmen anderthalben]."
                  - Karl Marx   17.11.1860  (Herr Vogt, Kapitel XI)
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-06T05:19:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cevif0$7mr$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <9EGkAgI9flB@jpberlin-l.willms.jpberlin.de>`

```
In article <9EGkAgI9flB@jpberlin-l.willms.jpberlin.de>,
Lueko Willms <l.willms@jpberlin.de> wrote:
>.    Am  05.08.04
>schrieb  docdwarf@panix.com
…[7 more quoted lines elided]…
>  To me this doesn't make sense.

Perhaps not... but it was not asked to make sense, it was asked if any 
harm/damage/Bad Stuff is known to happen by maintaining the practise.

>
>  If one takes into account the holy principle:
>  Thou shalt not trust external data and check it before using it

Another Teaching from the Oldene Dayse was 'All data are sacred, no datum 
is to be trusted', sure.

>
>  So, when you try to do calculations with an item from an imput file  
>which is not a number, an error will occur.

This can be said for that which is in the file buffer and that which is in 
WORKING-STORAGE, certainly.

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-05T09:02:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetlmc$272c$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cetdfp$mnk$1@panix5.panix.com...

> Does anyone know of harm/damage/bad stuff (outside of that which can be
> chalked up to sloppiness, e.g. changing a key's position/length and not
> updating the WORKING-STORAGE layout to match) which might happen due to
> continuing to adhere to this?  What is more likely to Go Wrong by holding
> to this 'standard'?

The COBOL standard does not require that the record have meaningful
information in it after a WRITE unless the file is specified in a SAME
RECORD AREA clause.  If you depend on the information hanging around after
that, you're in implementation-dependent territory.

    -Chuck Stevens
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-05T12:42:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ceto0r$23j$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlmc$272c$1@si05.rsvl.unisys.com>`

```
In article <cetlmc$272c$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message news:cetdfp$mnk$1@panix5.panix.com...
…[10 more quoted lines elided]…
>that, you're in implementation-dependent territory.

If by 'the record' you intend what lives in the FD, what I am calling the 
file buffer... then what I read you saying is that this is a reason for 
continuing the practises of READ INTO/WRITE FROM.  Did I get that right?

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-05T10:25:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cetqiq$2aa8$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlmc$272c$1@si05.rsvl.unisys.com> <ceto0r$23j$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:ceto0r$23j$1@panix5.panix.com...
> In article <cetlmc$272c$1@si05.rsvl.unisys.com>,
> Chuck Stevens <charles.stevens@unisys.com> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:cetdfp$mnk$1@panix5.panix.com...
> >
> >> Does anyone know of harm/damage/bad stuff (outside of that which can be
> >> chalked up to sloppiness, e.g. changing a key's position/length and not
> >> updating the WORKING-STORAGE layout to match) which might happen due to
> >> continuing to adhere to this?  What is more likely to Go Wrong by
holding
> >> to this 'standard'?
> >
> >The COBOL standard does not require that the record have meaningful
> >information in it after a WRITE unless the file is specified in a SAME
> >RECORD AREA clause.  If you depend on the information hanging around
after
> >that, you're in implementation-dependent territory.
>
> If by 'the record' you intend what lives in the FD, what I am calling the
> file buffer... then what I read you saying is that this is a reason for
> continuing the practises of READ INTO/WRITE FROM.  Did I get that right?

Yes.  Further, it seems to me that *encouragement* of that practice is what
led to making the record description optional in the FD and adding the WRITE
FILE syntax so that it could be optional.

In fact, I'd go so far as to say that if somebody wrote a proposal to make
WRITE <record-name> officially archaic, I would probably vote in favor of
it.   According to the standard, the record associated with a file is
unavailable before the file is opened, unavailable after the file is closed,
unavailable after a write or rewrite, and undefined after an unsuccessful
read or a successful open.

For me the "file buffer" is a different place from the FD's record
description; for me it's the job of the "operating environment" and not the
job of the compiler to deal with buffer management, so, for me, there's no
problem using a FD record or fields within it as if it were in
working-storage -- the space is always available, it's just space, and the
system transfers the information in the record into and out of the file
buffers.

The standard, however, has to account for implementations that don't handle
things that way, which is why it decrees the record unavailable; programs
that access such records outside of the execution-time contexts in which
they're defined as "available" are noncompliant.

Yeah, I think WRITE FILE and abandonment of the FD record, with the implicit
bizarrenesses about availability and defined content during execution, is a
good idea.   Whether the standard "archaizes" WRITE <record> or not, it
strikes me that WRITE FILE is better style overall.

Now, for those of you for whom the FD's record *is* the file buffer, and
WRITE FILE ends up doing an extra move that WRITE <record> didn't, well, I
just don't know what to say about implementations that would do that!
;-)

     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2004-08-05T12:27:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10h52hf50a7q0ec@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlmc$272c$1@si05.rsvl.unisys.com> <ceto0r$23j$1@panix5.panix.com> <cetqiq$2aa8$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

> The standard, however, has to account for implementations that don't
handle
> things that way, which is why it decrees the record unavailable; programs
> that access such records outside of the execution-time contexts in which
> they're defined as "available" are noncompliant.

I was looking for an explicit statement to that effect in the standard.  Can
you point me to it?

Walter
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-05T12:47:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ceu2s9$2frm$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlmc$272c$1@si05.rsvl.unisys.com> <ceto0r$23j$1@panix5.panix.com> <cetqiq$2aa8$1@si05.rsvl.unisys.com> <10h52hf50a7q0ec@corp.supernews.com>`

```
The problem is that the standard doesn't worry about *functional*
noncompliance, it worries about *syntactic* noncompliance.

Taking ANSI X3.23-1985 sequential I-O as an example, and ignoring "SAME
RECORD AREA":    CLOSE GR6 specifies that the record area is "no longer
available", READ GR12 specifies that the content of the record area is
"undefined", REWRITE GR5 specifies "not available", and WRITE GR2 specifies
"no longer available".   ISO/IEC 1989:2002 is similar.

Perhaps a more accurate way of describing this is that a program that
accesses a record in a FD when the file that the FD describes is closed or
has just been written to is dependent on behavior that is outside what is
permitted by the standard.   It's not the sort of thing the compiler could
flag as noncompliant, but the consequences of trying to do something the
standard says "you're not supposed to be able to do that" are undefined.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2004-08-06T12:49:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ni26sF143r8U1@uni-berlin.de>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlmc$272c$1@si05.rsvl.unisys.com> <ceto0r$23j$1@panix5.panix.com>`

```
I have several times run in to a situation where someone once had something
like:

WRITE MY-REC

and then changed it to

WRITE MY-REC
MOVE new-data-field to MY-REC-FIELD
WRITE MY-REC

Basically they were looking to write an addition record that was mostly the
same as the previous record, only with one field being different.

Unfortunately after the first WRITE the pointer for the file buffer moved to
the next record so that the next WRITE wrote either garbage (if the file
buffer had yet to 'loop' around to the beginning) or it wrote a totally
unrelated record (the one that existed in that part of the buffer the 'last
time through', if you will.  Never good.  

Not sure if this is the 'reason' you are looking for.

I would say that 'creating' a record in a file buffer, manipulating it
(optionally) and then writing it is probably safe.  But doing anything with
it once you've written it is not guarunteed to be safe.  It's most likely
not safe, at least in my environment, if there is more than one record per
block.  Don't know if it would be safe even if there was only one record per
block.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> <docdwarf@panix.com> 8/5/2004 10:42:03 AM >>>
In article <cetlmc$272c$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message
news:cetdfp$mnk$1@panix5.panix.com...
>
>> Does anyone know of harm/damage/bad stuff (outside of that which can be
>> chalked up to sloppiness, e.g. changing a key's position/length and not
>> updating the WORKING-STORAGE layout to match) which might happen due to
>> continuing to adhere to this?  What is more likely to Go Wrong by
holding
>> to this 'standard'?
>
…[3 more quoted lines elided]…
>that, you're in implementation-dependent territory.

If by 'the record' you intend what lives in the FD, what I am calling the 
file buffer... then what I read you saying is that this is a reason for 
continuing the practises of READ INTO/WRITE FROM.  Did I get that right?

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-08-06T20:54:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4113EFB6.4080201@optonline.net>`
- **In-Reply-To:** `<2ni26sF143r8U1@uni-berlin.de>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <cetlmc$272c$1@si05.rsvl.unisys.com> <ceto0r$23j$1@panix5.panix.com> <2ni26sF143r8U1@uni-berlin.de>`

```
This reminds me that our first Payroll program had a master record of
90 words. The hardware buffer was 60 words. Because we were all green
as grass (during the growing season), the Univac SE was assigned the
job of programming that file's part of the system.  As I recall his
solution was to allocate three memory buffers, and process ten words
at a time until the whole record was ready to write before reading
the next record into the buffer. What ever it was, updates to that
program required "his" maintenance for a long time. Payrolls have a
way of changing, and when necessary, he would be hired to do the change
instead of trying to let someone else learn how to do it.

If I remember correctly, and that's a big jump, I used that source
program to help teach a new bunch of programmers C-10. (Univac 1 machine
language.)

Warren Simmons


Frank Swarbrick wrote:
> I have several times run in to a situation where someone once had something
> like:
…[66 more quoted lines elided]…
>
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-05T18:50:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
The following applies ONLY to IBM's mainframe environment.

A little "history"

1) With pre '74 Standard OS/VS COBOL (and earlier, e.g. ANS V4 product) it was
possible to "access" the record (as described under an FD) before an OPEN and
after a CLOSE. (This was NOT documented as valid - but worked)  Therefore, it
was a "medium common" to have

   READ file-name
     AT END
          MOVE HIGH-VALUES TO record-name

  IF record-name NOT = HIGH-VALUES ....

Somewhere around "LANGLVL(2)" and/or VS COBOL II (I can't remember which), this
no longer worked and LOTS of programs "died" at run-time.   Therefore, the "new
Standard" of always doing a READ INTO and WRITE FROM became very common in IBM
shops.  (Even though the only "real" problem was accessing the record before an
OPEN and after a CLOSE.

2) When IBM (eventually) moved ACB's (VSAM) and DCB's (QSAM) "above the 16M
line", it became possible (and in come - not all cases) for the "block" to be
read into storage above the line, but for a copy of the record to be "moved"
below the line.  It was this below-the-line area that was accessed by the
program.  Therefore, previously "working" (but not documented as valid) programs
that did negative subscripting to get to a variable length record's LLZZ field -
or to try and get to "block" information from the record, would fail.  Again, to
avoid the "temptation" to use these techniques, the READ INTO and WRITE FROM
formats were made "shops standards".

    ***

Not for history (but current)
  I have checked both the Enterprise COBOL "Tuning" White Paper and the
"Programming Guides" and can find no indication that there is any performance
advantage/disadvantage of one technique over the other.  I am *not* an Assembler
programmer, but I believe that S/3x0 Assembler provides support for "locate" and
"move" modes for reads (writes).  I seem to recall discussions of which performs
better - and why doesn't COBOL use one over the other (in certain cases).
However, there doesn't seem to be any documented way for a COBOL programmer to
"insure" which is used - much less which will perform better.

Finally, if you are positioning IBM mainframe programs for "multi-threading" you
should read the section at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/4.4.4

which does explicitly mention "implicit serialization lock" with READ INTO and
WRITE FROM
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-05T14:33:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408051333.c347f30@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote

I suspect that the problem only occurred if it had:

>    READ file-name
>      AT END
>           MOVE HIGH-VALUES TO record-name
            CLOSE file-name
     .
> 
>   IF record-name NOT = HIGH-VALUES ....

It isn't the AT END that dumped the buffer, but the CLOSE.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-05T14:52:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ceua7c$2kt5$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <217e491a.0408051333.c347f30@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0408051333.c347f30@posting.google.com...
> "William M. Klein" <wmklein@nospam.netcom.com> wrote
>
…[10 more quoted lines elided]…
> It isn't the AT END that dumped the buffer, but the CLOSE.

The buffer is indeed still available after the READ but before execution of
the AT END clause, but its contents are undefined.  The AT END MOVE ...
should work, but then after the CLOSE the record you just MOVEd to is no
longer "available", so if you "avail" yourself of its contents there's no
telling what you'll get.  So far as the standard is concerned, as I see it,
you might get HIGH-VALUES, you might get a run-time error, you might get
rutabagas, you might get Thursday.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-05T19:09:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408051809.36b95d6b@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <217e491a.0408051333.c347f30@posting.google.com> <ceua7c$2kt5$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote 

> > I suspect that the problem only occurred if it had:
> >
…[12 more quoted lines elided]…
> should work, 

Exactly.  The original wasn't a problem.  Putting the CLOSE in the AT
END then creates the problem.

> but then after the CLOSE the record you just MOVEd to is no
> longer "available", 

Exactly.  If the CLOSE is left until just before STOP RUN (or
similar), or is left off, relying on the run-time to close the file,
then the buffer problem doesn't occur - well not _after_ a successful
OPEN anyway.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-06T03:30:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9XCQc.10490$9Y6.9366@newsread1.news.pas.earthlink.net>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <217e491a.0408051333.c347f30@posting.google.com> <ceua7c$2kt5$1@si05.rsvl.unisys.com> <217e491a.0408051809.36b95d6b@posting.google.com>`

```
From the '02 Standard (I think this matches what Chuck posted for the '85
Standard also)

From GR(21) of the READ statement,
    "When the at end condition exists, execution of the READ statement is
unsuccessful."

From GR(15)
     "Unless otherwise specified, at the completion of any unsuccessful
execution of a READ statement, the content of the associated record area is
undefined,"

I do NOT think this is just after the CLOSE.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-06T09:25:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf0be7$vm9$1@si05.rsvl.unisys.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <217e491a.0408051333.c347f30@posting.google.com> <ceua7c$2kt5$1@si05.rsvl.unisys.com> <217e491a.0408051809.36b95d6b@posting.google.com> <9XCQc.10490$9Y6.9366@newsread1.news.pas.earthlink.net>`

```
There are at least three different issues.

After a successful CLOSE the "record area" is unavailable.

After a WRITE or REWRITE, the "logical record" is unavailable.  .

After an unsuccessful READ, the contents of the record area are undefined.

    -Chuck Stevens

 record itself is unavailable; after a WRITE or REWRITE
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:9XCQc.10490$9Y6.9366@newsread1.news.pas.earthlink.net...
> From the '02 Standard (I think this matches what Chuck posted for the '85
> Standard also)
…[7 more quoted lines elided]…
> execution of a READ statement, the content of the associated record area
is
> undefined,"
>
…[21 more quoted lines elided]…
> > > The buffer is indeed still available after the READ but before
execution of
> > > the AT END clause, but its contents are undefined.  The AT END MOVE
...
> > > should work,
> >
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-06T20:11:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408061911.6d8293af@posting.google.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <217e491a.0408051333.c347f30@posting.google.com> <ceua7c$2kt5$1@si05.rsvl.unisys.com> <217e491a.0408051809.36b95d6b@posting.google.com> <9XCQc.10490$9Y6.9366@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote 

>      "Unless otherwise specified, at the completion of any unsuccessful
> execution of a READ statement, the content of the associated record area is
> undefined,"
> 
> I do NOT think this is just after the CLOSE.

There is a difference between 'the content of the record area is
undefined' and 'the record area is undefined (or unavailable)'.

Between a sucessful open and the close the record area is accessible
and may be referenced.  After an unsuccessful READ, or in many other
cases, the content is undefined, that is it may be rubbish, but if
something is moved there it may be tested later.

After a CLOSE the record area may disappear entirely, as it does in
Fujitsu NetCobol for Linux, and possibly other versions, but does not
in MicroFocus versions that I have used.  When the record area becomes
unavailable a reference to it causes an abend (segmentation fault).

That is, I know of no cases where moving data into a record area and
testing that area between an AT END and the CLOSE would be a problem.
If there is then the Cobol system is broken.  For example after an AT
END it is entirely possible to move a new value into a key and do a
START or a READ.
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-09T20:58:52-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf9a1p$288$1@news.eusc.inter.net>`
- **In-Reply-To:** `<kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net>`

```
William M. Klein wrote:

> The following applies ONLY to IBM's mainframe environment.
> 
…[28 more quoted lines elided]…
> 

As someone who coded varying flavors in varying flavors of IBM COBOL
from DOS COBOL from releases 18 - 26 of 360 DOS through COBOL for MVS
and VM, this is not the way it worked.  In COBOL VS and COBOL 68, the 
Get Locate mode of reading was used for sequential files other than VSAM 
ESDS data sets.  The AT END condition caused the record pointer to 
become indeterminate or 0.  System 0C4 abends - protection exceptions 
resulted if you attempted to address the record area for a file after 
the AT END condition occurred.  VS COBOL II at the release 1.4 level if 
not before changed this so that the record area for a file was 
addressable after the AT END condition occurred.  My guess is that this 
was done to be consistent with the detection of an AT END condition on a 
VSAM KSDS - Indexed file where you had to be able to move a key value to 
the record area to issue a START command.  This was confirmed by testing 
and by showing this I was able to persuade one shop to eliminate the 
standard of READ INTO since it had not been rigorously enforced anyway. 
  The advent of the Language Environment dumps for COBOL showing the 
record areas associated with the files clinched the argument for 
eliminating the sporadically enforced standard.  My personal preference 
has been for READ as opposed to READ INTO especially because of 
considerations for Keyed files.  Also it is inefficient for 
multi-format, multi-length record files.  Obviously there are a number 
of people who vehemently disagree with me.  The debate probably dates 
back to when READ INTO first became available.
>     ***
> 
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-09T22:06:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf9aja$5pr$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <cf9a1p$288$1@news.eusc.inter.net>`

```
In article <cf9a1p$288$1@news.eusc.inter.net>,
Clark F. Morris, Jr. <cfmtech@istar.ca> wrote:

[snip]

>My personal preference 
>has been for READ as opposed to READ INTO especially because of 
>considerations for Keyed files.  Also it is inefficient for 
>multi-format, multi-length record files.

Mr Morris, I know of no test the results would indicate such.  Might you 
be so kind as to point me towards one so that I could report my results to 
the group?

>Obviously there are a number 
>of people who vehemently disagree with me.

At this point I have insufficient information to agree or disagree, Mr 
Morris... hence my request.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-11T20:45:57-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2o56bjF70g4mU1@uni-berlin.de>`
- **In-Reply-To:** `<cf9aja$5pr$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <cf9a1p$288$1@news.eusc.inter.net> <cf9aja$5pr$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

> In article <cf9a1p$288$1@news.eusc.inter.net>,
> Clark F. Morris, Jr. <cfmtech@istar.ca> wrote:
…[20 more quoted lines elided]…
> Morris... hence my request.

I base this on the generated code for the READ followed by the implied 
MOVE.  In the case of a single or multi-format variable length record 
the move on a z series system would be to load the sending and receiving 
record addresses, the sending and receiving field lengths and the fill 
character into registers and then execute a MVCL - Move Character Long. 
  The sending field length would be 4 less than the value in the first 
two bytes of the record as seen by the system (the first four bytes of 
the record are not visible to the COBOL program except through 
contortions).  This will move the number of bytes actually in the input 
record and then space fill the rest of the record as required. The MVCL 
is not one of the most efficient instructions in the z series set and is 
interruptible.  Thus code is generated to handle the possibility of 
interruption.  Granted, any inefficiencies normally will be negligible 
compared to all of the other processing going on.  Note this problem 
exists for all variable length record files whether the file is composed 
of multiple record types with different fixed lengths or one record type 
that is true variable length.  WRITE FROM is more efficient than WRITE 
for Variable Length Record sequential files on z/OS because it allows 
the maximum number of records to be packed into the maximum block size 
allowed.

My personal belief is that you are open to fewer surprises if you 
process the records for keyed (VSAM on z/OS) files in the FD because of 
the rules for that kind of file handling.  I am sure other members on 
the list could make good cases for the READ INTO / WRITE FROM.
> 
> DD
>
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-09T21:23:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FLydnevrKqM4rIXcRVn-tQ@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <cf9a1p$288$1@news.eusc.inter.net>`

```
Clark F. Morris, Jr. wrote:
>  My personal
> preference
…[4 more quoted lines elided]…
> back to when READ INTO first became available.

I agree about the (modest?) inefficiency. In my view, though, the loss in
production inefficiency is more than made up for by avoiding catastrophe (of
the torches and pitchfork variety) by bothering the data in an FD.

READ INTO, like giving an enema to a dead man, can't hurt.

----
PS
I just finished a Carl Hiaasen book, "SKiNNY DiP." One of the minor
characters - a one man brute squad - has an interesting hobby: He steals
roadside crosses and re-erects them in his backyard. Has over 40. His
backyard looks like a miniature Arlington.



Another very minor character says, at one point to a main character:

"Understand that I'm not a well person. I'm muddling through a rough spell
at the moment, the man said. "For instance, I've got a hunch you don't even
marginally resemble H.R. Haldeman. Bob, they used to call him at the White
House."... "Anyway, that's who I'm hallucinating when I look at you - Bob
Haldeman. So keep that in mind. Plus, I've got a hideous duet running like a
freight train through my skull -- 'Hey, Jude,' as performed by Bobbie Gentry
and Placido Domingo. It's a fucking miracle I haven't disemboweled myself."

One of the less sane characters in the book.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-10T05:24:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfa480$6qc$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <kkvQc.10061$9Y6.4328@newsread1.news.pas.earthlink.net> <cf9a1p$288$1@news.eusc.inter.net> <FLydnevrKqM4rIXcRVn-tQ@giganews.com>`

```
In article <FLydnevrKqM4rIXcRVn-tQ@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>Clark F. Morris, Jr. wrote:
>>  My personal
…[7 more quoted lines elided]…
>I agree about the (modest?) inefficiency.

As mentioned to Mr Clark, I know of no test the results of which would 
indicate such.  Outside of each WRITE requiring a MOVE from 
WORKING-STORAGE to the DATA RECORD (accomplished nowadays on an IBM 
mainframe by the equivalent of an MVC) the efficiency should be 
identical... of course, this is not a world where 'should be' equals 'is', 
hence my request for the tests upon which the conclusions about 
inefficiencies are made.

>In my view, though, the loss in
>production inefficiency is more than made up for by avoiding catastrophe (of
            ^^
>the torches and pitchfork variety) by bothering the data in an FD.

Wow, I'm glad I've *never* done anything like that... and I'm glad I'm the 
King of England, too!

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-08-06T01:30:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4112DEDD.7040001@optonline.net>`
- **In-Reply-To:** `<cetdfp$mnk$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
As this is the fist message in this subject shown to me in my mail 
reader, I'd like to xpln one more time. COBOL was designed in the
late 1050's and early 1960's.  The short range group was made up of
almost all UNIVAC or former UNIVAC users.

The UNIVAC by todays standards was a simple system. Except for tape
drives, the ONLY memory was 1000 words of mercuray delay line except
for I/O buffers of 60 words each. Each word was 12 characters long
including the sign if one existed, and memory management was a 
programmer's responsibility.

Conscquently, a READ in 1960 COBOL was expected to dump the input
buffer into some sixty words of the 1000 words. If you had tape out
the output was built in the memory buffer, and when write occured,
the 60 words were moved to the output buffer and hence to the tape.
(In my mind, I'm not really sure that the I/O bufferes existed. They
probably were part of the 1000 words of memory.) At any rate, when
you had one input and one output, a minimum I/O situation, 120 words
were dedicated to I/O.  It was common to have two inputs and one or two 
or  more outputs which drastically reduced the availabe space for
program code. Once an input block was full, the program dealt with
parts of it depending upon the record size. Most common was 120 
characters, 10 words. Other versions could be word, or multiple word in
groups of two as machine instructions were used. Besides word records
instuction support supported two words, and ten words. There were  no
library routines to use, except the paper copies of the machine code
needed to do these things.

However, there were procedure one could use to build records in memory
from more than one tape drive at a time. So, for example, a two way
merge would use three 60 word buffers, and programs could read into
working storage a record from one file, and from another file, make
a decision, and write the output from the proper input buffer.

Our HSP only printed 120 characters per line, so no output would exceed 
that unless it would appear on two lines or more, or not at all. The 
output was writen to tape, carried to the printer, and the printer
had compatible buffers.

I would guess, but have no backup that computer design from the point
of COBOL 60 on considered ways to improve that initial condition. So
all of the talk about read into, and write from is grandfather spec.

I hope this helps some people understand that COBOL has changed with
the hardware (in part to do a better job, and capture more customers.)

I'm certainly for that kind of thing, and the way I look at it, there
were a lot of jobs created as a result.

Warren Simmons






docdwarf@panix.com wrote:
> So... I was being consulted on a program's design and mention was made of 
> the FD; reflexively I responded that the record layout in the FD should be 
…[32 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-06T05:31:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cevj57$aik$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <4112DEDD.7040001@optonline.net>`

```
In article <4112DEDD.7040001@optonline.net>,
Warren Simmons  <wsimmons5@optonline.net> wrote:

[snip]

>I would guess, but have no backup that computer design from the point
>of COBOL 60 on considered ways to improve that initial condition. So
…[6 more quoted lines elided]…
>were a lot of jobs created as a result.

Thanks greatly for the perspective, Mr Simmons, and yet...

... and yet the question of 'does it do harm?' still hangs.

[snip]

>> Things have changed since then, of course, and the Thou Shalt/Shalt Nots 
>> dating back to ENIAC may no longer be applicable... so I wonder:
…[5 more quoted lines elided]…
>> to this 'standard'?

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-07T13:40:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HICdnexYyKyIv4jcRVn-uQ@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> So... I was being consulted on a program's design and mention was
> made of the FD; reflexively I responded that the record layout in the
…[29 more quoted lines elided]…
> Go Wrong by holding to this 'standard'?

-------
During a performance in an early 1900s NY Yiddish theatre an actor collapsed
on the stage.

A doctor from the audience jumps to the stage and kneels beside the actor.

From the back of the balcony come a yiddishia-momma voice: "Give him an
enema!"

The doctor puts his ear to the actor's chest, listens for a moment, then
stands.

From the back of the balcony: "GIVE HIM AN ENEMA!"

The doctor faces the balcony and says: "Madame, the actor is DEAD."

From the back of the balcony: "So,... it can't hurt!"

I've often said the same about READ...INTO and WRITE...FROM.
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-07T19:27:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf3ohh$r08$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <HICdnexYyKyIv4jcRVn-uQ@giganews.com>`

```
In article <HICdnexYyKyIv4jcRVn-uQ@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Does anyone know of harm/damage/bad stuff (outside of that which can
>> be chalked up to sloppiness, e.g. changing a key's position/length
…[4 more quoted lines elided]…
>-------

[snip]

>From the back of the balcony: "GIVE HIM AN ENEMA!"
>
…[4 more quoted lines elided]…
>I've often said the same about READ...INTO and WRITE...FROM.

You've often said that READ INTO and WRITE FROM are like giving a dead 
actor an enema?

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-10T08:20:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-0847CD.08204410082004@knology.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <HICdnexYyKyIv4jcRVn-uQ@giganews.com> <cf3ohh$r08$1@panix5.panix.com>`

```
In article <cf3ohh$r08$1@panix5.panix.com>, docdwarf@panix.com wrote:

> In article <HICdnexYyKyIv4jcRVn-uQ@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[26 more quoted lines elided]…
> 

There are many programming standards that are similar in function to 
givng a corpse an enema...
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-10T08:46:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfag3b$dik$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <HICdnexYyKyIv4jcRVn-uQ@giganews.com> <cf3ohh$r08$1@panix5.panix.com> <joe_zitzelberger-0847CD.08204410082004@knology.usenetserver.com>`

```
In article <joe_zitzelberger-0847CD.08204410082004@knology.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <cf3ohh$r08$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
…[29 more quoted lines elided]…
>givng a corpse an enema...

I've had to adhere to a variety of programming standards in a variety of 
places, aye, but I've never attended to the latter task mentioned; I will 
yield, in this evaluation, to the Voice of Experience.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-10T07:54:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nPqdna-brYUHWIXcRVn-oA@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <HICdnexYyKyIv4jcRVn-uQ@giganews.com> <cf3ohh$r08$1@panix5.panix.com> <joe_zitzelberger-0847CD.08204410082004@knology.usenetserver.com> <cfag3b$dik$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
>>
>> There are many programming standards that are similar in function to
…[4 more quoted lines elided]…
> I will yield, in this evaluation, to the Voice of Experience.

Maybe not an enema, but a lot of programming projects are similar to putting
lipstick on a corpse.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-10T09:47:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfajl7$pdp$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <joe_zitzelberger-0847CD.08204410082004@knology.usenetserver.com> <cfag3b$dik$1@panix5.panix.com> <nPqdna-brYUHWIXcRVn-oA@giganews.com>`

```
In article <nPqdna-brYUHWIXcRVn-oA@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>>>
…[8 more quoted lines elided]…
>lipstick on a corpse.

I'm likewise and similarly inexperienced in such matters... but I can, at 
times, write code and Just for Laffs put together an experiment.

(Platform: IBM mainframe, compiler: IBM Enterprise COBOL for z/OS and 
OS/390 3.2.0)

Given a FILE-CONTROL of

SELECT IOFILE                             
       ASSIGN IOFIL                       
       ORGANIZATION IS INDEXED            
       ACCESS MODE IS DYNAMIC             
       FILE STATUS IS IO-STATUS           
       RECORD KEY IS IO-KEY-SSN OF IOFILE.

... and an FD of 

FD  IOFILE.                                
01  IOFILE-RECORD.                         
    03  FILLER                  PIC X(01). 
    03  IO-KEY-SSN              PIC X(09). 
    03  FILLER                  PIC X(238).

... and a PROCEDURE DIVISION of

    OPEN I-O IOFILE.                    
THE-READ.                               
    READ IOFILE NEXT.                   
THE-READ-INTO.                          
    READ IOFILE NEXT INTO IO-RECORD.    
THE-WRITE.                              
    WRITE IOFILE-RECORD.                
THE-WRITE-FROM.                         
    WRITE IOFILE-RECORD FROM IO-RECORD. 
THE-GOBACK.                             
    GOBACK.                             

... and the compiler invocation parameters of

PARM='SIZE(MAX),LIB,NUMPROC(MIG),MAP,DYNAM,   
 XREF,OPT,FLAG(I,I),NOSEQ,TEST(NONE,SYM),LIST'

(chosen for the Very Good Reason of... I just happened to have them 
hanging about)

... I found that the READ and the READ INTO were identical for the first 
fourteen instructions.  The READ terminated with (the MVI below is 
instruction number twelve)

         MVI   179(4),X'04'            FCB=1    
         MVC   0(2,3),169(10)          (BLW=0)+0
GN=16    EQU   *                                
GN=15    EQU   *                                

... while the READ INTO had (again, the MVI is the twelvth instruction):

         MVI   179(4),X'04'            FCB=1    
         MVC   0(2,3),169(10)          (BLW=0)+0
GN=18    EQU   *                                
         L     5,308(0,9)              BLF=0    
         MVC   8(248,3),0(5)           IO-RECORD
GN=17    EQU   *                                

Likewise, but reversed, the WRITE and the WRITE FROM were identical for 
the last eight instructions; the WRITE FROM was prefaced with:

     L     4,308(0,9)              BLF=0         
     MVC   0(248,4),8(3)           IOFILE-RECORD 

... and all that follows is more-or-less the same.

Granted that the example given is for a single-format, single-indexed 
file; I am still most interested in seeing the test which demonstrates 
that inefficiencies wrought by these two instructions are a quantifiable 
cause for concern.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-10T18:49:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v7idnRZLUtWRwoTcRVn-iQ@giganews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <joe_zitzelberger-0847CD.08204410082004@knology.usenetserver.com> <cfag3b$dik$1@panix5.panix.com> <nPqdna-brYUHWIXcRVn-oA@giganews.com> <cfajl7$pdp$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <nPqdna-brYUHWIXcRVn-oA@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[16 more quoted lines elided]…
> experiment.

I love experiments.

I agree that a piddly MVI instruction or two is sticking two fingers in the
dyke (dike?)* when one is sufficient. I've seen people force one finger in
the dike (dyke?) when no fingers were necessary at all. Usually the  same
people who go nuts over micro-efficiency have no problem with tape sorting.

-----
* Sorry, I don't speak Dutch so I'm not sure which word is correct. I have
the same problem reading the numbers on Mexican license plates.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-10T22:04:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfbus4$b20$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nPqdna-brYUHWIXcRVn-oA@giganews.com> <cfajl7$pdp$1@panix5.panix.com> <v7idnRZLUtWRwoTcRVn-iQ@giganews.com>`

```
In article <v7idnRZLUtWRwoTcRVn-iQ@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>> In article <nPqdna-brYUHWIXcRVn-oA@giganews.com>,
…[19 more quoted lines elided]…
>I love experiments.

I do also... especially when I don't know what the results are going to 
be!

>
>I agree that a piddly MVI instruction or two is sticking two fingers in the
>dyke (dike?)* when one is sufficient.

Gah... not MVI, MVC.  MVI is an SI-format instruction and MVC is an 
SS-format... I remember reading someplace (maybe in the back of a Murach 
CICS book?) that an SS-format takes about three times as long as an SI... 
but long before I read that I had been taught that, when possible, to make 
flags, switches, indicators, 88-levels and suchlike because 'it's faster'.

Wasn't until much later that I learned those single characters compiled to 
SI-format MVI and CLI, larger ones were MVC and CLC.

And... I am not Dutch, either, but I was taught that 'dike' is the 
flood-preventing berm and 'dyke' is an offensive colloquialism... but 
www.dictionary.com shows things which might be interpreted otherwise.

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-08-08T12:18:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hcklqqbkn8b78@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cetdfp$mnk$1@panix5.panix.com...
>
> So... I was being consulted on a program's design and mention was made of
…[30 more quoted lines elided]…
> to this 'standard'?

While I cannot identify that which 'is more likely to GoWrong',
I can suggest that the practice may violate the 'two-year programmer
rule'.

Standard COBOL, language reference manuals, and instructional texts
place those record description entries that are associated with files in the
FILE SECTION. From the texts I have read, this is what new progammers
are taught -- it is what some of us old programmers have retained.

Mr Dwarf, it seems to me that the 'standard' you described is contrary
to the tenor of COBOL, its teachings, and, while there may have been,
as you stated, reasons for following this 'standard' in the past, the
continuation of the practice seems unneccesary.

If the 'two-year programmer rule' is intended to prevent
'harm/damage/bad stuff ', then a practice contrary to what 'two-year
programmers' have been taught is suspect.
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-08T13:11:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf5mrl$c4p$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hcklqqbkn8b78@corp.supernews.com>`

```
In article <10hcklqqbkn8b78@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:cetdfp$mnk$1@panix5.panix.com...
…[36 more quoted lines elided]…
>rule'.

One step at a time, Mr Smith... are you saying, then, that a 'two-year 
programmer' is not expected to be conversant with the READ INTO and WRITE 
FROM constructs?

I ask this, rather incredulously, because the 'zero-tolerance rule' (and 
the associated syntaces for READ INTO and WRITE FROM) I mention above was 
taught in my first COBOL class; if the curriculum has changed that much 
(or my own experience was that disparate) then I might do well to revisit 
what I expect from a 'two-year programmer'.

>
>Standard COBOL, language reference manuals, and instructional texts
>place those record description entries that are associated with files in the
>FILE SECTION. From the texts I have read, this is what new progammers
>are taught -- it is what some of us old programmers have retained.

Sadly enough, the only text I have at hand is McCracken's 'A Simplified 
Guide to Structured COBOL Programming'... granted that it does not apply 
the Thou Shalt the instructor gave us but the syntaces are given and a 
reason for them.

(They are covered in Chapter Eight, 'Sequential File Processing (Part II) 
and Subroutines'; the sub-heading under which they appear is 'A simple 
merge program' (p.230).)

If what you say is true, and, generally, texts do not emphasise that Thou 
Shalt Not touch file buffers (etc)...' ... well, this might be seen as Yet 
Another Reason why one needs a text *and* an instructor, both.

>
>Mr Dwarf, it seems to me that the 'standard' you described is contrary
>to the tenor of COBOL, its teachings, and, while there may have been,
>as you stated, reasons for following this 'standard' in the past, the
>continuation of the practice seems unneccesary.

Mr Smith, I have no familiarity whatsoever with the 'tenor' of COBOL; 
while what 'seems' can be dependent on who is observing what I asked is a 
matter of fact:  'What is more likely to Go Wrong by holding to this 
'standard'?'

>
>If the 'two-year programmer rule' is intended to prevent
>'harm/damage/bad stuff ', then a practice contrary to what 'two-year
>programmers' have been taught is suspect.

There's the rub, Mr Smith... the only textbook I have available indicates 
that READ INTO and WRITE FROM are, clearly and unambiguously, a part of 
what is labelled 'A Simplified Guide' and are covered under the subheading 
of 'a simple merge program'.  If a two-year programmer is no longer 
expected to be familiar with such concepts then, indeed, something might 
Go Wrong when using them.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-08-08T16:26:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hd3528rjphtad@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hcklqqbkn8b78@corp.supernews.com> <cf5mrl$c4p$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cf5mrl$c4p$1@panix5.panix.com...
> In article <10hcklqqbkn8b78@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:cetdfp$mnk$1@panix5.panix.com...
> >>
> >> So... I was being consulted on a program's design and mention was made
of
> >> the FD; reflexively I responded that the record layout in the FD should
be
> >> as simple as possible, e.g.
> >>
…[5 more quoted lines elided]…
> >> ... and that everything should be dealt with in WORKING-STORAGE using
READ
> >> INTO and WRITE FROM.
> >>
> >> This, of course, is what was taught to me lo, those many decades back;
the
> >> specific of 'Thou shalt not perform arithmetic manipulations in file
> >> buffers' was expanded into the zero-tolerance rule of 'Thou shalt not
> >> touch file buffers; all will be done in WORKING-STORAGE via READ INTO
and
> >> WRITE FROM.'
> >>
> >> A few years back... not too long ago, maybe 1988, 1989, I was called in
to
> >> help a coder who was getting some whacky results... and sure enough, he
> >> was doing arithmetice manipulations on the FDand the numbers were
coming
> >> out screwy. Granted, the platform was WANG VS... but the Ancient
Teaching
> >> was proven right.
> >>
> >> Things have changed since then, of course, and the Thou Shalt/Shalt
Nots
> >> dating back to ENIAC may no longer be applicable... so I wonder:
> >>
…[3 more quoted lines elided]…
> >> continuing to adhere to this?  What is more likely to Go Wrong by
holding
> >> to this 'standard'?
> >
…[12 more quoted lines elided]…
> what I expect from a 'two-year programmer'.

Mr Dwarf, you wrote, above, 'I responded that the record layout in the
FD should be as simple as possible ...and that everything should be dealt
with in WORKING-STORAGE  using READ INTO and WRITE FROM'.
Clearly, one cannot 'deal with' the record layout using 'READ INTO and
WRITE FROM'. 'READ INTO and WRITE FROM' are incidental to
the placement of the record layout for the file. Thus, the first step is to
determine where best to place the record layout for the file. What I stated
below was 'Standard COBOL, language reference manuals, and
instructional texts place those record description entries that are
associated
with files in the FILE SECTION.' So, eventhough a 'two-year programmer'
may be conversant with 'READ INTO and WRITE FROM', that
programmer may be unfamiliar with describing and using a file's record
layout in the WORKING-STORAGE SECTION. I do not contend that
this is a major obstacle, only that it is an obstacle that must be overcome.

One potentional problem in describing storage is that the redefinition of
record descriptions is implicit in the FILE SECTION; but must be explicit
in the WORKING-STORAGE SECTION. A programmer taught to use
the FILE SECTION may need to learn from a 'bad' experience that things
are different.

Another is the processing of variable length records using COBOL 85
syntax. As I understand it, there are cases with ODO tables where the
actual record layout must be described in the FILE SECTION. But,
maybe such is not for the two-year programmer.

> >
> >Standard COBOL, language reference manuals, and instructional texts
> >place those record description entries that are associated with files in
the
> >FILE SECTION. From the texts I have read, this is what new progammers
> >are taught -- it is what some of us old programmers have retained.
…[12 more quoted lines elided]…
> Another Reason why one needs a text *and* an instructor, both.

I did a cursory review of six texts looking for the location of record
description entries for files and the use of READ and WRITE. All placed
record layouts for files in the FILE SECTION. In all, except one, READ
was used to describe processing. In all, the primary use for WRITE FROM
was for printed reports.

> >
> >Mr Dwarf, it seems to me that the 'standard' you described is contrary
…[7 more quoted lines elided]…
> 'standard'?'

Mr Dwarf, as I stated above, 'I cannot identify that which 'is more likely
to
GoWrong''. The reason being, in part, that I have no experience from which
to make such an identification. I have never used the practice you described
and I do not recall ever having seen it used. I do recall that an older
system
written for IBM COBOL F always used records with a key of
HIGH-VALUES on each indexed file and ended processing when the key
was encountered. I assume this was to prevent some problems that may have
occurred at end of file. But, this system still placed the record layout in
the
FILE SECTION.

Thus, I am left only to speculate that a 'two-year programmer' may be
confused why a practice not taught is followed and that this confusion may
cause problems.

> >
> >If the 'two-year programmer rule' is intended to prevent
…[8 more quoted lines elided]…
> Go Wrong when using them.

Three recent texts, based on COBOL 85, provide many examples
including the merging of files without using READ INTO and WRITE
FROM. Mr Dwarf, I do not always know my expectations until I find
something that offends my sensibilities; but if an employer expects a
two-year programmer to be familiar with concepts no longer taught
this may result in disappointment for both.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-08T18:06:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf684e$16l$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hcklqqbkn8b78@corp.supernews.com> <cf5mrl$c4p$1@panix5.panix.com> <10hd3528rjphtad@corp.supernews.com>`

```
In article <10hd3528rjphtad@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:cf5mrl$c4p$1@panix5.panix.com...

[snip]

>> Mr Smith, I have no familiarity whatsoever with the 'tenor' of COBOL;
>> while what 'seems' can be dependent on who is observing what I asked is a
…[5 more quoted lines elided]…
>GoWrong''.

Many thanks, Mr Smith, for addressing the question I asked in so direct a 
fashion.

>The reason being, in part, that I have no experience from which
>to make such an identification. I have never used the practice you described
>and I do not recall ever having seen it used.

Thanks again, Mr Smith, for being so forthright about the amount of 
familiarity you have with the subject about which I am inquiring; it is 
good to be able to know about the experiences one has had which go into a 
public pronouncement.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-08-08T23:42:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hdso774o5b150@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hcklqqbkn8b78@corp.supernews.com> <cf5mrl$c4p$1@panix5.panix.com> <10hd3528rjphtad@corp.supernews.com> <cf684e$16l$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cf684e$16l$1@panix5.panix.com...
> In article <10hd3528rjphtad@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:cf5mrl$c4p$1@panix5.panix.com...
>
> [snip]
>
> >> Mr Smith, I have no familiarity whatsoever with the 'tenor' of COBOL;
> >> while what 'seems' can be dependent on who is observing what I asked is
a
> >> matter of fact:  'What is more likely to Go Wrong by holding to this
> >> 'standard'?'
> >
> >Mr Dwarf, as I stated above, 'I cannot identify that which 'is more
likely
> >to
> >GoWrong''.
…[5 more quoted lines elided]…
> >to make such an identification. I have never used the practice you
described
> >and I do not recall ever having seen it used.
>
…[3 more quoted lines elided]…
> public pronouncement.

You are most welcome, Mr Dwarf. It is the comparative 'more likely'
and the condition 'by holding to this 'standard'' that provides the
difficulty.
To give an example of a 'What', one must have experience of both.
Effectively, one must have had a problem doing 'everything' in working
storage and needed to move the complete record layout to the file
description entry to correct the problem. By not adhering to the described
practice, I never experienced any of its potential problems. Hmm! I
suppose that I must admit that I am not sorry that I could not help more
than I may have.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-09T05:16:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf7fe1$h31$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hd3528rjphtad@corp.supernews.com> <cf684e$16l$1@panix5.panix.com> <10hdso774o5b150@corp.supernews.com>`

```
In article <10hdso774o5b150@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:cf684e$16l$1@panix5.panix.com...
…[31 more quoted lines elided]…
>difficulty.

Well, Mr Smith... if it were easy then I might not have felt the need to 
make this inquiry to so august a forum as this, no?

>To give an example of a 'What', one must have experience of both.

That could be why I structured the query as I did, Mr Smith; I related 
what I had been taught and (as a result of this teaching) practised, along 
with a half-remembered situation a few decades old on a platform which is 
not the most common... and asked what others had learned and experienced.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-08-15T02:19:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hu05vsh8rcr2f@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hd3528rjphtad@corp.supernews.com> <cf684e$16l$1@panix5.panix.com> <10hdso774o5b150@corp.supernews.com> <cf7fe1$h31$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cf7fe1$h31$1@panix5.panix.com...
> In article <10hdso774o5b150@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:cf684e$16l$1@panix5.panix.com...
> >> In article <10hd3528rjphtad@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[6 more quoted lines elided]…
> >> >> Mr Smith, I have no familiarity whatsoever with the 'tenor' of
COBOL;
> >> >> while what 'seems' can be dependent on who is observing what I asked
is a
> >> >> matter of fact:  'What is more likely to Go Wrong by holding to this
> >> >> 'standard'?'
> >> >
> >> >Mr Dwarf, as I stated above, 'I cannot identify that which 'is more
likely
> >> >to
> >> >GoWrong''.
> >>
> >> Many thanks, Mr Smith, for addressing the question I asked in so direct
a
> >> fashion.
> >>
> >> >The reason being, in part, that I have no experience from which
> >> >to make such an identification. I have never used the practice you
described
> >> >and I do not recall ever having seen it used.
> >>
> >> Thanks again, Mr Smith, for being so forthright about the amount of
> >> familiarity you have with the subject about which I am inquiring; it is
> >> good to be able to know about the experiences one has had which go into
a
> >> public pronouncement.
> >
…[12 more quoted lines elided]…
> not the most common... and asked what others had learned and experienced.

I am curious, Mr Dwarf, why did you include the restriction '(outside
of that which can be chalked up to sloppiness, e.g. changing a key's
position/length and not  updating the WORKING-STORAGE layout
to match) '? I ask because these types of errors appear to that which
'is more likely to Go Wrong'. In each of the cases that comes to mind,
the example you provided as, making 'the record layout in the FD ...
as simple as possible', prevents certain compile time checks, for such
'sloppiness', allowing this 'sloppiness' to become runtime errors and
anomalies.

Also, do I understand correctly that your making 'the record layout
in the FD ... as simple as possible' is intended to enforce the
'zero-tolerance rule' (which you mentioned as having been taught in
your first COBOL class)? I ask this because both GC28-6403-0,
"IBM System/360 Disk Operating System Subset American
National Standard COBOL" (aka COBOL E), and GC28-6396-5,
"IBM OS Full American National Standard COBOL" (aka
COBOL F) show nearly identical sample programs for "Random
retrieval and updating of an indexed file". These sample programs
use only the file buffers for processing. The only item in working
storage being the NOMINAL KEY for the indexed file. The
updating of the indexed file record was the instruction
'ADD CD-AMT TO DISK-AMT', followed by a REWRITE.
Thus, not only are file buffers touched but arithmetic is done on
an item in them. I wonder, Mr Dwarf, whether the instructors 'Thou
Shalts' were the result of working with a non-conforming compiler.
For example, if the instructor had problems with using, let's say, a
COBOL 74 compiler for Wang VS and developed his 'Thou
Shalts' based upon overcoming those problems; then was it
COBOL or something else that was taught?

I found that I had a similar experience ('sloppiness') when I updated
a system. Different record descriptions were used to descibe a
record, one a complete description in the FD, the other a PIC X(xxx)
in working storage, which was used to hold a copy of the record,
temporarily. When I modified some fields in the copy book for the
complete description. I failed to notice the copy of the record.
During testing the program failed. Needless to say, I was not happy
with discovering this 'sloppiness'.

I have one, personal, program in which I use READ INTO and
WRITE FROM, exclusively. There was, at one point, eight record
descriptions for the same record type. I chose to use COPY
REPLACING (partial text replacement) to create unique data
names for processing of the records in various procedures.

Mr Dwarf, I have carefully reviewed a lot of material, including my
experience, trying to find some rational basis for the general
applicability of the 'zero-tolerance rule', I found none.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-15T07:11:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfngcn$451$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hdso774o5b150@corp.supernews.com> <cf7fe1$h31$1@panix5.panix.com> <10hu05vsh8rcr2f@corp.supernews.com>`

```
In article <10hu05vsh8rcr2f@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:

[snip]

>I am curious, Mr Dwarf, why did you include the restriction '(outside
>of that which can be chalked up to sloppiness, e.g. changing a key's
>position/length and not  updating the WORKING-STORAGE layout
>to match) '?

Because sloppiness, Mr Smith, can be found anywhere; it has been said that 
'you can make something foolproof, but not damn-fool-proof'.

[snip]

>Also, do I understand correctly that your making 'the record layout
>in the FD ... as simple as possible' is intended to enforce the
>'zero-tolerance rule' (which you mentioned as having been taught in
>your first COBOL class)?

Quite right, Mr Smith... the less there is in the FD which is not defined 
as FILLER the less there is in the FD on which to perform any sort of 
manipulation.

>I ask this because both GC28-6403-0,
>"IBM System/360 Disk Operating System Subset American
…[14 more quoted lines elided]…
>COBOL or something else that was taught?

Mr Smith, I have absolutely no idea where or how my instructor arrived at 
this particular commandment; when he taught it to the class I was too busy 
trying to learn COBOL to question his resumee, pedigree or experience.  
From some of the comments seen here it appears that the practise of READ 
INTO/WRITE FROM was not limited to his classroom.

[snip]

>Mr Dwarf, I have carefully reviewed a lot of material, including my
>experience, trying to find some rational basis for the general
>applicability of the 'zero-tolerance rule', I found none.

That might be why, Mr Smith, that I did not ask for anyone to supply a 
'rational basis', I asked if anyone knew of things that might Go Wrong 
outside of the general sloppiness I exempted.

To the best of my recollection of this rather lengthy thread... nobody's 
reported doing so.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-08-15T13:03:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10hv5tff85rjmaf@corp.supernews.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hdso774o5b150@corp.supernews.com> <cf7fe1$h31$1@panix5.panix.com> <10hu05vsh8rcr2f@corp.supernews.com> <cfngcn$451$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cfngcn$451$1@panix5.panix.com...
> In article <10hu05vsh8rcr2f@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
…[9 more quoted lines elided]…
> 'you can make something foolproof, but not damn-fool-proof'.

Mr Dwarf, would not sloppiness include the teaching of a rule
that has the effect of introducing the potential for sloppiness?
A rule intended to address a problem of uncertain origin?
A rule that is unnecessary with conforming compilers?

> [snip]
>
…[31 more quoted lines elided]…
> INTO/WRITE FROM was not limited to his classroom.

Mr Dwarf, from the comments seen here, there is no evidence that
those using READ INTO and WRITE FROM also practice the
'zero-tolerance rule' you described.

> [snip]
>
…[6 more quoted lines elided]…
> outside of the general sloppiness I exempted.

Mr Dwarf, this is usenet and I am merely practicing something I
learned a long time ago, "Question the premises!" The requirement
for READ INTO and WRITE FROM is premised on the
'zero-tolerance rule'. That is, if the rule is irrational, then so may be
the aforementioned requirement. In effect, the rule is a problem -- it
is the rule that might make things Go Wrong.

> To the best of my recollection of this rather lengthy thread... nobody's
> reported doing so.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-15T13:44:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfo7e1$sa$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <10hu05vsh8rcr2f@corp.supernews.com> <cfngcn$451$1@panix5.panix.com> <10hv5tff85rjmaf@corp.supernews.com>`

```
In article <10hv5tff85rjmaf@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:cfngcn$451$1@panix5.panix.com...
…[14 more quoted lines elided]…
>that has the effect of introducing the potential for sloppiness?

Mr Smith, I do not know of anything that can be taught which cannot be 
applied sloppily.

>A rule intended to address a problem of uncertain origin?

Mr Smith, a problem is a problem, no matter what its origin.

>A rule that is unnecessary with conforming compilers?

Mr Smith, I do not understand what you are intending by 'necessity'; COBOL 
is applicable across a variety of compilers.

>
>> [snip]
…[36 more quoted lines elided]…
>'zero-tolerance rule' you described.

That just might be why, Mr Smith, I did not ask for the reason that people 
did such.

>
>> [snip]
…[10 more quoted lines elided]…
>learned a long time ago, "Question the premises!"

The premises given, Mr Smith, were:

1) I was taught this rule and this technique.

2) My experience includes a circumstance where neglecting this technique 
caused something to Go Wrong.

>The requirement
>for READ INTO and WRITE FROM is premised on the
>'zero-tolerance rule'. That is, if the rule is irrational, then so may be
>the aforementioned requirement. In effect, the rule is a problem -- it
>is the rule that might make things Go Wrong.

And in my experience, Mr Smith, I have run across a situation where 
something Went Wrong because the rule was not adhered to; this was a 
reinforcement of the teaching I had received.  I then inquired of the 
group whether someone had experience of the opposite, that being if 
something would Go Wrong if the rule *was* adhered to... and to the best 
of my recollection of this rather lengthy thread... nobody's reported 
doing so.

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-14T18:27:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JdxTc.15865$5s3.14148@fe40.usenetserver.com>`
- **In-Reply-To:** `<cetdfp$mnk$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

> Does anyone know of harm/damage/bad stuff (outside of that which can be 
> chalked up to sloppiness, e.g. changing a key's position/length and not 
> updating the WORKING-STORAGE layout to match) which might happen due to 
> continuing to adhere to this?  What is more likely to Go Wrong by holding 
> to this 'standard'?

In my opinion, Read Into / Write From are "safer," especially in a 
maintenance environment.  Sure, _you_ know what you're doing, but the 
next person to come along may not.  And, with the intricacies of when 
the contents of the FD are reliable and when they are not, it makes 
sense to use the aforementioned technique.  "Quick fixes" are more 
likely to work, especially if they're done (as they often are) without 
proper analysis first.  :)
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-08-15T00:11:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<411EA9C6.8000507@optonline.net>`
- **In-Reply-To:** `<JdxTc.15865$5s3.14148@fe40.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <JdxTc.15865$5s3.14148@fe40.usenetserver.com>`

```
It seems to me that for the benefit of all file users, the file should
contain some identity. For example, the serial number of the compiler
that produced it showing the release and date of writing. Then down the
line it would be possible to create a reference library of such 
"versions" by vendor that would identify the kinds of quirks that
existed with this file as it was created. Also, in a future extension
of the life of this file a chain of references could exist for the
possible need to decipher the data. Concerns over encryption could
be referenced and documented.  Some data is lots more critical than
others.  While this is just a balloon assent ion for me at this time,
more and more problems that are brought to light in this forum could
be planned for with some kind of system that addresses these kinds of
problems.

Warren Simmons
wsimmons5@optonline.net



LX-i wrote:
> docdwarf@panix.com wrote:
> 
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-14T22:23:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfmhfq$qj7$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <JdxTc.15865$5s3.14148@fe40.usenetserver.com>`

```
In article <JdxTc.15865$5s3.14148@fe40.usenetserver.com>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>
…[8 more quoted lines elided]…
>next person to come along may not.

... especially when I am both; have you ever looked at some years-old code 
and thought 'Who *wrote* this trash... oh, lookee there, I done it!'?

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-16T11:29:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kh5Uc.23226$5s3.2702@fe40.usenetserver.com>`
- **In-Reply-To:** `<cfmhfq$qj7$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <JdxTc.15865$5s3.14148@fe40.usenetserver.com> <cfmhfq$qj7$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

> In article <JdxTc.15865$5s3.14148@fe40.usenetserver.com>,
> LX-i  <lxi0007@netscape.net> wrote:
…[16 more quoted lines elided]…
> and thought 'Who *wrote* this trash... oh, lookee there, I done it!'?

:)  Quite recently, in fact.  There was a program I "rewrote" because it 
was structured quite horridly, and didn't do what it was supposed to do 
to boot.  I recently looked through the program again, and thought "My 
goodness - what was I thinking?"  (Coincidentally, it still isn't doing 
what it's supposed to be doing - but, the customer has accepted that 
it's a flaw in their requirements, and are planning to fix it in the 
next major release.)

In the mean time, responsibility for that program has now passed to 
someone else - so, I'm sure they'll rewrite my rewrite.  Maybe the 3rd 
time will be the charm.  ;)
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Paul Knudsen <HughG@dodgeit.com>
- **Date:** 2004-08-21T06:11:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dqpdi0hr3mg4fdh88p7t17j0dm0nkcj8tl@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
On 5 Aug 2004 09:42:17 -0400, docdwarf@panix.com wrote:

>Does anyone know of harm/damage/bad stuff (outside of that which can be 
>chalked up to sloppiness, e.g. changing a key's position/length and not 
>updating the WORKING-STORAGE layout to match) which might happen due to 
>continuing to adhere to this?  What is more likely to Go Wrong by holding 
>to this 'standard'?

Other than the small waste of space, there's nothing "wrong" with it I
suppose.
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-08-24T01:21:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgej86$9sf$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <dqpdi0hr3mg4fdh88p7t17j0dm0nkcj8tl@4ax.com>`

```
In article <dqpdi0hr3mg4fdh88p7t17j0dm0nkcj8tl@4ax.com>,
Paul Knudsen  <HughG@dodgeit.com> wrote:
>On 5 Aug 2004 09:42:17 -0400, docdwarf@panix.com wrote:
>
…[7 more quoted lines elided]…
>suppose.

Thanks much for the observation.

DD
```

#### ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Gerry Kroll <NO.keldine@SPAM.keldine.ca.FOR.ME>
- **Date:** 2004-09-05T22:21:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com>`

```
On 5 Aug 2004 09:42:17 -0400, docdwarf@panix.com wrote:

>
>So... I was being consulted on a program's design and mention was made of 
…[32 more quoted lines elided]…
>DD

Sorry to be so late jumping into this thread,....

The reason for using READ INTO and WRITE FROM is nothing more than
*efficiency*  ..... 

In the bad old days, before computers became so fast, programmers
worried about how long their programs ran, and they tried to produce
programs that did their thing as accurately and as quickly as
possible.  Believe me: It's a BIG deal when a program takes 20 minutes
as opposed to 15 minutes to run through a reel of tape when you're
dealing with 200+ reel datasets.  Been there, done that.

Now for the efficiency part: When you're working directly in a file's
record, each reference to a field in that record requires that the CPU
locates the record, loads an index register with the record location,
and then uses an indexed reference to the field.  This takes several
instructions (i.e., time).  If you're working with fields in Working
Storage, the location is static and the field can be referenced by the
CPU directly without involving any index registers or indexing.

The problem the original poster was asked to help resolve was probably
caused by referencing an output field after the record had been
written.

My credentials:
COBOL, FORTRAN,  & Assembler programmer, 1964 - 1980;
COBOL & FORTRAN compiler writing & debugging, Univac, IBM, and
Honeywell systems, 1971 - 1984
CODASYL COBOL language committee member, 1975 - 1978
ANSI COBOL language committee member, 1978

Regards, Gerry Kroll  
(Hi, Don Nelson & Jerome Garfunkel: long time no see)
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-06T18:39:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-798E9C.18391806092004@knology.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>`

```
In article <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>,
 Gerry Kroll <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:

<snip>
> The reason for using READ INTO and WRITE FROM is nothing more than
> *efficiency*  ..... 
…[14 more quoted lines elided]…
> CPU directly without involving any index registers or indexing.
<snip>

I'm going to have to totally disagree with you here -- at least in the 
case of IBM/z-OS machines.  The compiler loading a BLF into an index 
register takes the same number of instructions as it does to load a BLW 
into an index register.  Both are remote to the programs executing code 
and must be resolved at runtime.

It is possible that some implementation of a Cobol compiler once messed 
up file section field references without equally messing up working 
storage field references.  But that would only have made the case true 
for that specific compiler -- not as a broad, general, cross-platform 
rule.

I assume, when you say 'static', you are talking about the intermixed 
code and data.  Something that you could get with a NORENT, NOREUSE load 
module where declared variables are actually embedded as part of the 
executing code.

I'm not sure what the very old compilers did, but all of IBMs offerings, 
at least since VS-Cobol-II (perhaps older, anyone?) have generated 
separate working storage by default with an initial getmain for the 
working storage at runtime.  I'm not even sure you could get one to 
embed working storage in the load module if you tried.
 
You are right that it is an efficiency question, but that question is 
one of Move Mode I/O verses Locate Mode I/O.  Locate Mode is always 
faster, although with a record smaller than 256 bytes you would be very 
hard pressed to notice a difference.

Joe Z.




*** FWIW, the above only discusses specifics about IBM hardware/software 
with some generalities about Intel memory protection and division 
styles.  I know Unisys machines can locate records anywhere, but will 
also provide the programmer with a cup of coffee and a magizine if any 
waiting is involved.  However, since I've never seen one in the wild, 
I'm not really able to discuss how Unisys memory might be structured and 
protected...

;-)
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-09-07T04:47:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<413D3CF7.7000807@optonline.net>`
- **In-Reply-To:** `<joe_zitzelberger-798E9C.18391806092004@knology.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com> <joe_zitzelberger-798E9C.18391806092004@knology.usenetserver.com>`

```
Hi JOe,

I tried to point out previously why RI WF were in the COBOL system.
It was my take on it based upon the environmnet of the Univac I.
This system used a mercury delay line for memory, and there was a
totol of 1000 12 character words in which to store in and out data.
Typically, since the blocks of data were moved in batches of 60
words, a progam would assign addresses 940 to 999 as the I/O buffer
for input one. Blocks of 60 words were then assigned for any other
input or output. Soooooo
A read from tape (there was no other kind) loaded the first block
from a tape into 940. Also typically, programs were designed with
ten word records, but not always. The programmer would address the
data in 940 to 949 as the first record. If it was a tape copy, the
simplist thing one could do, that record would be memory transfered
to the output buffer's next ten words.
As it can be seen, if any relationship existed between the first
and second input record, etc. this could be done six times, and
then the whole input buffer would have to be transfered to the output
buffer.

Since very few programs were simple copy programs, some reference to
the seond etc. records might be necessary prior to the move to the
outpupt buffer, say such as a summary of like sorted data. As this
simple proceedure expanded it was possible to work programmatically
in both the input and output buffer, and that proved to be a frequent
problem, sooooo

Memory bufferes were set up in what COBOL calles Working Storage, out 
side of the I/O buffers.  I don't know that this was a problme in other
systems of that time, but as the short range committee all had 
experience with the Univac I, I believe they set the rule about
Read Into (Y00940 Z00820) as an example. The computers I/O system
at that time (and probably still is in most systems, not part of
the programmers direct responsiblility. Such that in the illustratiion
I'm trying to make, would have the I/O system step through six records,
and without additional help, refill the input buffer with the next
block of 60 words.

Now, to clarify as much as possible, the I/O was something a programmer
copied from paper into his program, and seldom considered it except
when the size of the record changed, and then only to plug in a 
different I/O program. Our early programmers had training but were
formerly tab people. It took a few years for them to grasp the 
relationship between the I/O portion of their code and the part they
did.

That's a lot of words, and it isn't KISS, but it's my expaination of
why when how and where this idea came up. New hardwre, and new compilers
made a difference.  I think of it as taking a record from thhe file,
working on it at my desk,then placing it in the output box. Best done
Read Into, Write From.

Forgive the verbage.

Warren Simmons



Joe Zitzelberger wrote:
> In article <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>,
>  Gerry Kroll <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:
…[65 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** docdwarf@panix.com
- **Date:** 2004-09-06T21:04:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chj1e0$dep$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>`

```
In article <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>,
Gerry Kroll  <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:
>On 5 Aug 2004 09:42:17 -0400, docdwarf@panix.com wrote:

[snip]

>>Does anyone know of harm/damage/bad stuff (outside of that which can be 
>>chalked up to sloppiness, e.g. changing a key's position/length and not 
…[5 more quoted lines elided]…
>Sorry to be so late jumping into this thread,....

Hey, old threads never die... they just smell that way.

>
>The reason for using READ INTO and WRITE FROM is nothing more than
>*efficiency*  ..... 

[snip]

>Now for the efficiency part: When you're working directly in a file's
>record, each reference to a field in that record requires that the CPU
>locates the record, loads an index register with the record location,
>and then uses an indexed reference to the field.

How very interesting... I am assuming that this behavior varies from 
compiler to compiler.  The test I posted (to be found at 
<http://groups.google.com/groups?selm=cfajl7%24pdp%241%40panix5.panix.com&output=gplain> )
was not constructed to test this (and was done with a more modern 
compiler, as well); the only other compiler to which I have access is a 
version of IKFCBL00 at work; I'll code something up and post what the PMAP 
shows.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

- **From:** Gerry Kroll <NO.keldine@SPAM.keldine.ca.FOR.ME>
- **Date:** 2004-09-07T10:32:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fgrj05hl2j34lbqj563h16bune2treaab@4ax.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com> <chj1e0$dep$1@panix5.panix.com>`

```
On 6 Sep 2004 21:04:00 -0400, docdwarf@panix.com wrote:

>In article <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>,
>Gerry Kroll  <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:
…[34 more quoted lines elided]…
>DD

My "efficiency" explanation was intended to be just that: an
"explanation".  Just because a given coding and programming (they're
different!) practice was considered to be more efficient back in the
olden days doesn't automatically mean that that's still the case.

I speak from experience on that "used to be efficient" thing.  I
worked on the innards of several Cobol compiler and run-time library
implementations, on wildly different hardware.  They ALL were much
more efficient in the generated object code when dealing with fields
in Working Storage as opposed to fields subordinate to an FD.  

This has nothing to do with procedure and data in the same code
segment.  In fact, none of the implementations I dealt with ever did
that. Rather, it had to do with being able to dedicate a pointer
register to the *static* location (i.e., never changes) of Working
Storage and then in all relevant procedures using the contents of that
pointer register to locate the data without ever having to load it.
Not so with file records, where the location changes as the result of
READ or WRITE statements.

On Intel CPUS, the equivalent would be to use the Data Segment
register (DS) to point to Working Storage, while loading the *very
dynamic* Extra Segment (ES) register with the current location of the
FD's record being worked on.  A procedure can depend on the DS
register not changing during its execution, but the ES register can't
be depended upon.  (Some implementations might use an Index Register
instead of the ES, but they all use DS to point to Working Storage.)

The "not changing" statements above do NOT prevent the OS from moving
the physical location of a data or code segment.

Regards,
Gerry Kroll.
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-09-07T11:06:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chkiq0$eai$1@panix5.panix.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com> <chj1e0$dep$1@panix5.panix.com> <1fgrj05hl2j34lbqj563h16bune2treaab@4ax.com>`

```
In article <1fgrj05hl2j34lbqj563h16bune2treaab@4ax.com>,
Gerry Kroll  <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:
>On 6 Sep 2004 21:04:00 -0400, docdwarf@panix.com wrote:
>
>>In article <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com>,
>>Gerry Kroll  <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:

[snip]

>>>The reason for using READ INTO and WRITE FROM is nothing more than
>>>*efficiency*  ..... 
…[20 more quoted lines elided]…
>olden days doesn't automatically mean that that's still the case.

Perfectly understood, Mr Kroll... but the Search for Knowledge can be a 
relentless taskmaster and you've given me something to take a look at... 
and take a look I've done, and more.

A PMAP generated by:

PP 5740-CB1 RELEASE 2.4  IBM OS/VS COBOL  JULY  1, 1982

(which, of course, gave me a listing-date of SEP  7,1904) shows that a 
MOVE of a PIC X(09) field in WORKING-STORAGE to a PIC X(09) field defined 
at the 05 level in an FD generates:

MOVE 000578  D2 08 7 001 6 100 MVC   001(9,7),100(6) DNM=1-143 DNM=3-362 

... while a MOVE of this same WORKING-STORAGE field to another PIC X(09) 
05 level field in WORKING-STORAGE generates:

MOVE 00057E  D2 08 6 009 6 100 MVC   009(9,6),100(6) DNM=1-237 DNM=3-362

... which indicates, at least to my eye, that the considerations you bring 
to bear were not considerations a scant two-decades-and-small-change back.

>
>I speak from experience on that "used to be efficient" thing.  I
…[3 more quoted lines elided]…
>in Working Storage as opposed to fields subordinate to an FD.  

That touches on the point of my question, Mr Kroll... after all, I used to 
be a lad with a full head of white-blond hair and a soprano singing-voice; 
what 'used to be' is not necessarily what 'is, now' and hence, my query.  
Some of the dicta given me during my training are now irrelevant - 'Want 
to fit an oversized program into core?  Code your SELECTs with a RESERVE 
NO ALTERNATE AREAS clause!' - but... hey, some people think that my entire 
existence is irrelevant, I can deal with that.  Trying to get me to wear a 
pair of courdory knickerbockers, however, might cause Bad Things to 
happen... and so I asked about Bad Things which might happen were one to 
force COBOL to assume the fashions of the Oldene Dayse.

DD
```

###### ↳ ↳ ↳ Re: Revisiting an Old Prejudice: READ INTO/WRITE FROM

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-09T06:06:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-98DF1C.06064509092004@knology.usenetserver.com>`
- **References:** `<cetdfp$mnk$1@panix5.panix.com> <nvgnj09rnukvvfmmpkhs7m899648okbvqh@4ax.com> <chj1e0$dep$1@panix5.panix.com> <1fgrj05hl2j34lbqj563h16bune2treaab@4ax.com>`

```
In article <1fgrj05hl2j34lbqj563h16bune2treaab@4ax.com>,
 Gerry Kroll <NO.keldine@SPAM.keldine.ca.FOR.ME> wrote:

> My "efficiency" explanation was intended to be just that: an
> "explanation".  Just because a given coding and programming (they're
…[30 more quoted lines elided]…
> Gerry Kroll.

You are trying to make me believe that a load of an address into a 
register is more expensive than a load of an address into a register AND 
a move of a large block of memory.

I can see the lack of an address register being a problem on the 
register poor Intels -- but they are an unusual case.  Certainly not on 
something like S/360 arch.  Consider the S/360...

Once you have the register loaded to refer to the record in the file 
system buffer (and you need that to do the move into working storage), 
you have everything you need to reference the fields directly in the 
file system buffer.  (assuming a <4k record)

There is no reason a register could not be designated to each file.  As 
the address of that record changes, the base/displacement of the fields 
do not change.  You get static location for your FD records.

Just for fun I compiled something with IBMs current offering -- this is 
how they behave, each open file is dedicated a base register, as is each 
4k of working storage.  References were resolved identically.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
