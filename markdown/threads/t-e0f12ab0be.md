[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interesting code

_72 messages · 26 participants · 1999-11_

---

### Interesting code

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vtlff$gp5$1@news.igs.net>`

```
I was reading code (by people in my employ) when I ran across this snippet I
thought interesting. I have not been a proponent of the one period on a line
style in the past, but I thought this usage rather interesting. The fact
that two lines have been commented out but left in as comments is also
rather interesting, stylistically.  Any thoughts?


           MOVE SELECTOR-TOP TO SP2-WD-TITLE.
           CALL "SP2" USING SP2-OPEN-WINDOW SP2-WINDOW-DEF.
           IF SP2-WD-RET-CODE IS NOT EQUAL TO ZERO
               DISPLAY "SP2-WD-RET-CODE = ", SP2-WD-RET-CODE
      *         STOP RUN
           .
           MOVE LOW-VALUES TO SP2-PD-DATA.
      *     MOVE -1 TO SP2-PD-MENU-ROWS.
           MOVE SELECTOR-TOTAL-WIDTH TO SP2-PD-WIDTH.
```

#### ↳ Re: Interesting code

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822E900.80A19DE7@IMN.nl>`
- **References:** `<7vtlff$gp5$1@news.igs.net>`

```
donald tees wrote:
> 
> I was reading code (by people in my employ) when I ran across this snippet I
…[13 more quoted lines elided]…
>            MOVE SELECTOR-TOTAL-WIDTH TO SP2-PD-WIDTH.
The original code could have been:
             MOVE SELECTOR-TOP TO SP2-WD-TITLE.
             CALL "SP2" USING SP2-OPEN-WINDOW SP2-WINDOW-DEF.
             IF SP2-WD-RET-CODE IS NOT EQUAL TO ZERO
                 DISPLAY "SP2-WD-RET-CODE = ", SP2-WD-RET-CODE
                 STOP RUN.
             MOVE LOW-VALUES TO SP2-PD-DATA.
             MOVE -1 TO SP2-PD-MENU-ROWS.
             MOVE SELECTOR-TOTAL-WIDTH TO SP2-PD-WIDTH.
(I can see the commented statements shifted one position to the right due to an
insertion of the asterix, I presume that an PC-editor is used which most of the
time by default operate in insert mode)

Now, to prevent the logic structure, the code-modifying guy did put the dot
after stop run on a separate line and then comment the STOP RUN.
In the series of imperative statements (3 MOOVE's) no need to put the dot apart,
because the three MOVE's all have their own.

This kind of code has the posibility to make errors. Forgetting to put the
period after the STOP RUN on its own line would have made the first MOVE part of
the IF afterwards. If you (or someone else) insist on this coding style, give my
compliments to the one that made the change: he/she did a good job.

I strongly prefer to code:
             MOVE SELECTOR-TOP TO SP2-WD-TITLE
             CALL "SP2" USING SP2-OPEN-WINDOW SP2-WINDOW-DEF
             IF SP2-WD-RET-CODE IS NOT EQUAL TO ZERO
                 DISPLAY "SP2-WD-RET-CODE = ", SP2-WD-RET-CODE
                 STOP RUN
--->         END-IF 
             MOVE LOW-VALUES TO SP2-PD-DATA
             MOVE -1 TO SP2-PD-MENU-ROWS
             MOVE SELECTOR-TOTAL-WIDTH TO SP2-PD-WIDTH
             .
That last dot^because I assume the third MOVE to be the last one in the COBOL
paragraph.
Now the modification is just to put the starts in column 7 ...

This is going to some other very long thread about periods. period.

The Frog.
```

##### ↳ ↳ Re: Interesting code

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vvpir$qrc$1@news.igs.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <3822E900.80A19DE7@IMN.nl>`

```

The COBOL Frog wrote in message <

>the IF afterwards. If you (or someone else) insist on this coding style,
give my
>compliments to the one that made the change: he/she did a good job.
>
The interesting part about it is that the person that did the code had never
coded in Cobol until two weeks before.  Mind you, Dave is an old pro with
twenty years in numerous other languages.  He is one of the best toolmakers
I know, and was between contracts, which is why I asked him to help me do
some catch up.
```

##### ↳ ↳ Re: Interesting code

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3823057F.36ADCB74@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <3822E900.80A19DE7@IMN.nl>`

```
The COBOL Frog wrote:

> I strongly prefer to code:
>              MOVE SELECTOR-TOP TO SP2-WD-TITLE
…[11 more quoted lines elided]…
> Now the modification is just to put the starts in column 7 ...

But now that you put in the END-IF, your preferance of putting the
period at the end of the sentence no longer has an advantage.  Certainly
a standard of putting in END-IF is more valuable than a style of using a
single period.
```

#### ↳ Re: Interesting code

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822EF56.80BD5492@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net>`

```
The stand alone period here is useful - for old COBOLs which don't have
END-IF statements.  When you have scope terminators, the advantage you
show below goes away.

END-IF should be a standard.

donald tees wrote:
> 
> I was reading code (by people in my employ) when I ran across this snippet I
…[13 more quoted lines elided]…
>            MOVE SELECTOR-TOTAL-WIDTH TO SP2-PD-WIDTH.
```

##### ↳ ↳ Re: Interesting code

- **From:** DACatHome@aol.com
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vv9p0$3im$1@nnrp1.deja.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <3822EF56.80BD5492@NOSPAMhome.com>`

```
In article <3822EF56.80BD5492@NOSPAMhome.com>,
  Please, do, not, e-mail, replies, post, them!! wrote:
> The stand alone period here is useful - for old COBOLs which don't
have
> END-IF statements.  When you have scope terminators, the advantage you
> show below goes away.
…[5 more quoted lines elided]…
> > I was reading code (by people in my employ) when I ran across this
snippet I
> > thought interesting. I have not been a proponent of the one period
on a line
> > style in the past, but I thought this usage rather interesting. The
fact
> > that two lines have been commented out but left in as comments is
also
> > rather interesting, stylistically.  Any thoughts?
> >
…[9 more quoted lines elided]…
>

I've never seen a period on a line by itself. I have seen code were
there is an END-IF or END-PERFORM followed by a period. Also constructs
like this:
IF (condition)
    MOVE X TO Y
    IF (condition)
        MOVE A TO B
    ELSE
        MOVE B TO A
    END-IF
ELSE
    MOVE Y TO X.

The END-IF in this case is unnecessary. I guess people think this makes
the code clearer, or they don't know that periods and ELSE statements
are implicit scope terminators. In any case, I rather have an "extra"
scope terminator than a period by itself because it's easier to pick
out.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38234B91.6D90FC01@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <3822EF56.80BD5492@NOSPAMhome.com> <7vv9p0$3im$1@nnrp1.deja.com>`

```
DACatHome@aol.com wrote:

> I've never seen a period on a line by itself. I have seen code were
> there is an END-IF or END-PERFORM followed by a period. Also constructs
…[15 more quoted lines elided]…
> out.

You're right, it's not necessary, but if I were writing shop standards,
I would require two END-IFs in the above code.  And I would encourage
the second one to be terminated by a period.  The compiler doesn't care,
but I want maintenance to be quick and correct.
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3823a2c7.72008507@news1.attglobal.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <3822EF56.80BD5492@NOSPAMhome.com> <7vv9p0$3im$1@nnrp1.deja.com>`

```
On Fri, 05 Nov 1999 19:05:06 GMT, DACatHome@aol.com wrote:

>In article <3822EF56.80BD5492@NOSPAMhome.com>,
>  Please, do, not, e-mail, replies, post, them!! wrote:
…[47 more quoted lines elided]…
>out.

Personally, I prefer BOTH.  I WOULD use the END-IF, and the the lone
period on a line all by itself.  One period per paragraph.  If it were
not for backward compatibility, I would advocate eliminating the
period in the procedure division completely.

All that aside, I try to conform to whatever is ALREADY in a program.
I'm not a zealot on the issue, although it does tend to devolve into a
religious debate.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3826DD70.7ADFABD2@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <3822EF56.80BD5492@NOSPAMhome.com> <7vv9p0$3im$1@nnrp1.deja.com> <3823a2c7.72008507@news1.attglobal.net>`

```
Thane Hubbell wrote:

> Personally, I prefer BOTH.  I WOULD use the END-IF, and the the lone
> period on a line all by itself.  One period per paragraph.  If it were
> not for backward compatibility, I would advocate eliminating the
> period in the procedure division completely.

Not me.  I agree that END-IF is a good standard to me.  It makes your
intention more clear and puts a well defined ending to your IF logic. 
But eliminating periods does neither.  The only thing eliminating
periods does is make it easier to cut and paste code.  In my environment
periods are very useful (we have pre-compiler imbedded IF logic  which
should be terminated).  A solid, obvious termination point is useful in
analyzing how a program works.
 
> All that aside, I try to conform to whatever is ALREADY in a program.
> I'm not a zealot on the issue, although it does tend to devolve into a
> religious debate.

Have to, with different environments to work in.  (it's interesting when
a shop has strong standards and then buys programs with different
standards, especially from more than one source).
```

#### ↳ Re: Interesting code

- **From:** "bart higdon" <develop@intouchcomputers.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enDU3.31289$23.1632502@typ11.nn.bcandid.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net>`

```
not only do I comment out old code in first 6 spaces I put my initials and
date.

bh1105* example
```

##### ↳ ↳ Re: Interesting code

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38239F99.B9ABD7B3@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <enDU3.31289$23.1632502@typ11.nn.bcandid.com>`

```
bart higdon wrote:
> 
> not only do I comment out old code in first 6 spaces I put my initials and
> date.
> 
> bh1105* example

TILT - not Y2K compliant. Seriously, do you clean up stuff more than a
year old as you go along, or do people wonder if "WL1105" was 1998 or
1993?

Bill Lynch
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3826DC0C.36039B9B@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <enDU3.31289$23.1632502@typ11.nn.bcandid.com> <38239F99.B9ABD7B3@att.net>`

```
William Lynch wrote:
> 
> bart higdon wrote:
…[10 more quoted lines elided]…
> Bill Lynch

Certainly the day of the month isn't important here - so 1105 will be
May of 2011.  

I have found that it is better to document the name and date of the
maintenance in the REMARKS, and then put your maintenance request number
(or make up such a number) to reference this change to individual lines.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 4)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38279FB0.19DD1F38@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <enDU3.31289$23.1632502@typ11.nn.bcandid.com> <38239F99.B9ABD7B3@att.net> <3826DC0C.36039B9B@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> William Lynch wrote:
…[15 more quoted lines elided]…
> May of 2011.

Are you suggesting that Bart's example, "bh1105*", is a reference to
May, 2011 (or, of course, November, 2005)? He *really* works ahead,
doesn't he? Since moving to Endevor early this year I've gotten very
comfortable deleting the old code and making the program source reflect
what *this* program does *now*. That's exactly what I want to see if I
get a 3 AM call. I have no interest in what it did in 1993, 1994, etc.
Endevor conveniently shows me the changes from version to version, and I
can always retrieve the source without signout to do a Comparex against
my current version in my PDS. As always, YMMV.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38282EAB.C8E9D76@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <enDU3.31289$23.1632502@typ11.nn.bcandid.com> <38239F99.B9ABD7B3@att.net> <3826DC0C.36039B9B@NOSPAMhome.com> <38279FB0.19DD1F38@att.net>`

```
William Lynch wrote:

> > > TILT - not Y2K compliant. Seriously, do you clean up stuff more than a
> > > year old as you go along, or do people wonder if "WL1105" was 1998 or
…[17 more quoted lines elided]…
> Bill Lynch

Pretty much.  You rarely don't need this kind of comments over a year
old.  I can see arguments for keeping an audit trail of changes due to
tax law changes, etc.  But for debugging purposes, let the comments drop
out.  The standards should allow for common sense.   

My job requires a column 73-80 modid on all changes.  (we can delete
lines though)  That's a pain because we can't SEE those columns with a
SUPER-C.  Now that everybody is switching to TSO (to avoid the CICS
charge of SISD), this isn't automatic anymore.  It is ugly when you put
modid's over modid's.  We use Endeavor, and I hope after people use TSO
for a while, people will re-think this policy.

I am for common sense in using commented out code.

There is one place though where we have to be careful in a different
way.  We have some third party programs which get fixes which are
dependent upon line numbers not being moved.  Applying those fixes is a
pain - no programming, just typing and testing, and using their
comments.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991109114630.11319.00000052@ngol01.aol.com>`
- **References:** `<38282EAB.C8E9D76@NOSPAMhome.com>`

```
In article <38282EAB.C8E9D76@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes:

>
>My job requires a column 73-80 modid on all changes.  (we can delete
…[14 more quoted lines elided]…
>

How does one get a ModId put in 73-80 w/o having to constantly shift the 
screen right/left all the time?
I would prefer to use 73-80 as it fits a 'iiyymmdd' or 'iiitask#' format much
better than using the sequence number area with 'Rymmdd' or 'iiymdd'.

I have not seen where anyone has ever had to worry about changes more than
ten years ago.  Most of the time stuff has been modified over and over such
that
most lines that get maintained are changed again in less than 10 years.
Certainly there is static stuff that never gets changed, but even in the event
of
looking for 10 or 100  year old code, there should be a modifications log
either
in the front of the program or in some version control system to tie it all
together.

I kinda got spoiled with Multi-Edit on the PC that can automatically insert a 
change identifier using a combination of the user's initials and the PC system
date.

Too bad I haven't found a nifty macro to handle the same thing in ISPF.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38285570.C1040ECB@NOSPAMhome.com>`
- **References:** `<38282EAB.C8E9D76@NOSPAMhome.com> <19991109114630.11319.00000052@ngol01.aol.com>`

```
Sff5ky wrote:

> How does one get a ModId put in 73-80 w/o having to constantly shift the
> screen right/left all the time?

SISD had a command to do that.  I generally put my initials in columns
1-3 and then do some global changes when I am done with my work.

> I would prefer to use 73-80 as it fits a 'iiyymmdd' or 'iiitask#' format much
> better than using the sequence number area with 'Rymmdd' or 'iiymdd'.

We use our request number.  The log at the top (in the old REMARKS area)
tells what was done, when, and the request number.
 
> I have not seen where anyone has ever had to worry about changes more than
> ten years ago.  Most of the time stuff has been modified over and over such
…[7 more quoted lines elided]…
> together.

Agreed.
 
> I kinda got spoiled with Multi-Edit on the PC that can automatically insert a
> change identifier using a combination of the user's initials and the PC system
> date.

I like multi-edit, especially before they went GUI.  With the DOS
interface, I could enter ME FILE.BAT and it was smart enough to look in
C:/BELFRY to find FILE.BAT (or create it if it didn't exist).  With
Windows, I keep having to walk trees to put my file where I want it.  A
real pain.
 
> Too bad I haven't found a nifty macro to handle the same thing in ISPF.

Someone wrote one for us, but I haven't used it.  Basically, you change
a line and press an F key to put the code in columns 73-80.
```

#### ↳ Re: Interesting code

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382283d6.28044543@news1.attglobal.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net>`

```
On Thu, 4 Nov 1999 22:58:39 -0500, "donald tees" <donald@willmack.com>
wrote:

>I was reading code (by people in my employ) when I ran across this snippet I
>thought interesting. I have not been a proponent of the one period on a line
…[3 more quoted lines elided]…
>

Code snipped...

I do this quite often.  I might want to know what it did before or I
might want to put the commented code back.  I would have used fewer
periods also.

Another thing I do, that some might dislike, is code any new code in
all lower case.  It helps me know what I added vs what was there
before.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Commented code.

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822F002.486DDDC8@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net>`

```
Thane Hubbell wrote:

> The fact
> >that two lines have been commented out but left in as comments is also
…[11 more quoted lines elided]…
> before.

I work in a shop with pre-compilers which put in their own asterisks in
column 7.  So I am in the habit of putting a double asterisk in my
comments, to make it easier to see my comments.

How do people here generally document changed code within their
programs?
```

###### ↳ ↳ ↳ Re: Commented code.

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38239BE7.912B41AC@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
(snip)
> 
> How do people here generally document changed code within their
> programs?

Historically we left the commented out code in place and put dates
(MMDDYY, of course) in cols. 1-6. Now that we're using Endevor, I'm
pushing for tossing all that out and just making the vew version of
SCBR666 do what it's supposed to do. I can use the Changes option in
Endevor to see the changes (if I first Select the element, then I can
put the "C" on any level to see the changes). Endevor's pretty slick
when all's said & done.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3824310A.F27B87B5@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com> <38239BE7.912B41AC@att.net>`

```
William Lynch wrote:
> 
> Howard Brazee wrote:
…[14 more quoted lines elided]…
> Bill Lynch

In endevor the comments actually make this tool useless.  You see the
deleted code and then the inserted commented code.  Very confusing.
```

###### ↳ ↳ ↳ Re: Commented code.

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vuv90$4ln$1@starburst.uk.insnet.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com>`

```
We normally use multiple (more than 2) asterisks to differentiate commented
out code from real comments.

Rick

Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:3822F002.486DDDC8@NOSPAMhome.com...
> Thane Hubbell wrote:
>
…[20 more quoted lines elided]…
> programs?
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 4)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38239C91.E43214A9@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com> <7vuv90$4ln$1@starburst.uk.insnet.net>`

```
Rick Price wrote:
> 
> We normally use multiple (more than 2) asterisks to differentiate commented
> out code from real comments.

I prefer more than one "*" for coded comments (I've been using 5
asterisks for years) because just one is so easily missed (plus lots of
software, e.g., the CICS translator, puts a single "*" in col. 7 when it
expands the commands). As always, YMMV

Bill Lynch
```

###### ↳ ↳ ↳ Re: Commented code.

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KtDU3.30502$it.630230@news2.rdc1.on.home.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com>`

```
I prefer document how the program currently works and delete any comments
about how the code used to work. If I want to know how the code used to work
I can always sign out an earlier version from the version control system,
view revision comments or easily see the difference between versions.

FYI, we use cvs (http://www.cyclic.com/cvs/info.html) and have hooked it
into e-mail so any changes are broadcast via a subscriber list. It has the
added value of being freeware.

Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:3822F002.486DDDC8@NOSPAMhome.com...
> Thane Hubbell wrote:
>
…[20 more quoted lines elided]…
> programs?
```

###### ↳ ↳ ↳ Re: Commented code.

- **From:** "DENDEN" <DENDEN@prodigy.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vv17v$3sji$1@newssvr03-int.news.prodigy.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com>`

```
On 11/05/1999 Howard Brazee wrote:
<snip>
<How do people here generally document changed code within their
programs?>

Possibly due to my age and/or the number of projects I work on, sometimes I
comment out exisiting code just on the hunch that it has a reasonable chance
of returning at some point in the future.  I use mulitple asterisks, but put
the date in, i.e.

***** 11/05/1999  code from #nnnnnn thru #nnnnnn below commented out for xyz
reason *****

This, of course, assumes numbered code, not free form.  If it's free form, I
end the code with another line of

***** 11/05/1999  end commented code *****

If it's a single line, I use the same approach, continuing the remainin code
on another commented line if it overflows the line.
I use the same techinque for new code, only explaining a little about why
the code was added.  Periodically, I try to clean out older comments, but it
sure helps me remember my thought process at the time the code was
added/commented.  If there is any overhead involved other that the number of
lines involved, it's worth it to my organization, since I'm the only
programmer in my department.

Denny Brouse
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 4)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38239DB0.5444AEA9@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com> <7vv17v$3sji$1@newssvr03-int.news.prodigy.com>`

```
DENDEN wrote:
> 
(snip)
> 
> Possibly due to my age and/or the number of projects I work on, sometimes I
> comment out exisiting code just on the hunch that it has a reasonable chance
> of returning at some point in the future.  I use mulitple asterisks, but put
> the date in, i.e.

How long do you retain the commented out code? My area has programs with
dates in the '80's! (1980's, of course <g>). IMHO this is a prime way
source gets really cluttered and hard to read (even if you're not coding
GOTO's).

> ***** 11/05/1999  code from #nnnnnn thru #nnnnnn below commented out for xyz
> reason *****

Does "#nnnnnn" mean all source is numbered and these numbers don't
change, i.e., no RENUM? Using this style I'd put comment banners to show
the start & end of the mods. Not practical for 1 statement changes,
though.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 5)_

- **From:** "DENDEN" <DENDEN@prodigy.net>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80hvfe$2l5o$1@newssvr03-int.news.prodigy.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com> <7vv17v$3sji$1@newssvr03-int.news.prodigy.com> <38239DB0.5444AEA9@att.net>`

```
Bill,

I realize this may sound unprofessional, but the rule I use is based on what
the code does.  For example, I work for a bank, and every once in awhile, we
need a cross reference file to process the checks of an acquired bank.  We
normally don't reissue new checks to the customer until they run out.  So at
this point in time, the cross reference code is commented out and hasn't
been used for about 4 years.  I just have a hunch as soon as I delete it,
the next acquisition will need it.  Other one time stuff, I use the "home
closet" rule.  If I haven't worn it in a year or two, I pitch it.

Yes, all of our code is sequenced, with 100 as the increment.  If we need a
bunch of code within the 99 numbers, we perform a routine outside of that
range.  We use the scheme perform 100-DO-THIS, 102-DO-THAT, etc., where 100
is actually at line number 100nnn.  Sometimes the code gets a little
cluttered, but with the actual line number as a prefix to the routine, it
makes maintenance pretty easy.  On extremely large programs, we pull in
external libraries.  It's not perfect by any means, but I've certainly seen
worse!
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382D4BAD.89F1DEA@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com> <7vv17v$3sji$1@newssvr03-int.news.prodigy.com> <38239DB0.5444AEA9@att.net> <80hvfe$2l5o$1@newssvr03-int.news.prodigy.com>`

```
DENDEN wrote:
> 
> I realize this may sound unprofessional, but the rule I use is based
…[7 more quoted lines elided]…
> worn it in a year or two, I pitch it.

Put the code in a subroutine.  Comment out the call to a subroutine. 
One line as opposed to X.  The code in a subroutine is never commented
out just never linked and never called.

This cat is skinned another way.
Ken
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 7)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991113111322.25952.00000279@ngol03.aol.com>`
- **References:** `<382D4BAD.89F1DEA@zip.com.au>`

```
In article <382D4BAD.89F1DEA@zip.com.au>, Ken Foskey <waratah@zip.com.au>
writes:

>
>Put the code in a subroutine.  Comment out the call to a subroutine. 
…[5 more quoted lines elided]…
>

The only problem with this option is that with an optimizing compiler,
you are notified that code at lines x-y are never executed and so
some 'bright boy' comes in and whacks the procedure since it is 
never used.  :-)   Seen that happen more often than I care to re-count.
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382df646_3@news3.prserv.net>`
- **References:** `<382D4BAD.89F1DEA@zip.com.au> <19991113111322.25952.00000279@ngol03.aol.com>`

```
> The only problem with this option is that with an optimizing compiler,
> you are notified that code at lines x-y are never executed and so
> some 'bright boy' comes in and whacks the procedure since it is
> never used.  :-)   Seen that happen more often than I care to re-count.


have a variable that is set to 0:

move 1 to var
compute var = var - var

 then

if var = 1 call proc
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 9)_

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ssvt2s4q6mvi51f2thkrd6uerihp2f7v0v@4ax.com>`
- **References:** `<382D4BAD.89F1DEA@zip.com.au> <19991113111322.25952.00000279@ngol03.aol.com> <382df646_3@news3.prserv.net>`

```
On Sat, 13 Nov 1999 17:38:48 -0600 "Leif Svalgaard" <lsvalg@ibm.net> wrote:

:>> The only problem with this option is that with an optimizing compiler,
:>> you are notified that code at lines x-y are never executed and so
:>> some 'bright boy' comes in and whacks the procedure since it is
:>> never used.  :-)   Seen that happen more often than I care to re-count.

:>have a variable that is set to 0:

:>move 1 to var
:>compute var = var - var

:> then

:>if var = 1 call proc

Assuming that all this is in-line code it can be optimized away.

The move followed by the compute would be converted into 

    MOVE 0 TO var

And if the IF VAR is inline it can be optimized as well.
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382E92E6.37D85253@zip.com.au>`
- **References:** `<382D4BAD.89F1DEA@zip.com.au> <19991113111322.25952.00000279@ngol03.aol.com>`

```
Sff5ky wrote:
> 
> In article <382D4BAD.89F1DEA@zip.com.au>, Ken Foskey <waratah@zip.com.au>
…[14 more quoted lines elided]…
> never used.  :-)   Seen that happen more often than I care to re-count.

By my definition a subroutine is not a perform statement.  It is a
called procedure.

Ken
```

###### ↳ ↳ ↳ Re: Commented code.

- **From:** docdwarf@clark.net ()
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wjEU3.33601$oa2.79619@iad-read.news.verio.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com>`

```
In article <3822F002.486DDDC8@NOSPAMhome.com>,
Howard Brazee  <Please, do, not, e-mail, replies, post, them!!> wrote:

[snippolinio]

>How do people here generally document changed code within their
>programs?


Who documents?  Seriously, I usually use:

***myuserid MM/DD/YY MODS BEGIN
(code)
***myuserid MM/DD/YY MODS END

... in addition to whatever goes in at the top of the program.

DD
```

###### ↳ ↳ ↳ Re: Commented code.

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38242FAB.993D0B56@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <3822F002.486DDDC8@NOSPAMhome.com> <wjEU3.33601$oa2.79619@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 
> In article <3822F002.486DDDC8@NOSPAMhome.com>,
…[15 more quoted lines elided]…
> DD

When I (rarely) do this I remove them on the next cycle.  The start
and stops just clutter the code space.

Incidentally there was a great discussion about this and readable code
on news:comp.software-eng  'Comment before code, or comment after
code?'

Ken
```

##### ↳ ↳ Re: Interesting code

- **From:** "bart higdon" <develop@intouchcomputers.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xkDU3.31282$23.1632192@typ11.nn.bcandid.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net>`

```
I do the same but all new code I write is small case.
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38239E71.FFF57C62@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <xkDU3.31282$23.1632192@typ11.nn.bcandid.com>`

```
bart higdon wrote:
> 
> I do the same but all new code I write is small case.

This seems to be a life or death issue in MVS shops. Another guy and I
decided to leave the code in caps, but do the comments in mixed case.
IMHO, again, makes it easier to read. This is the same guy who convinced
me (by example) to update to using periods only where required in the
Procedure Division. 

Bill Lynch
```

##### ↳ ↳ Re: Interesting code

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vug59$68g$1@news.igs.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net>`

```
I have been using case to clarify code here and there as well.  I am not
sure if I like the practice, though.  While I found it handy to emphasize
certain things, after a while the code just starts to get cluttered looking.

Thane Hubbell wrote in message <382283d6.28044543@news1.attglobal.net>...
>On Thu, 4 Nov 1999 22:58:39 -0500, "donald tees" <donald@willmack.com>
>wrote:
>
>>I was reading code (by people in my employ) when I ran across this snippet
I
>>thought interesting. I have not been a proponent of the one period on a
line
>>style in the past, but I thought this usage rather interesting. The fact
>>that two lines have been commented out but left in as comments is also
…[15 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vupp9$cno$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <382283d6.28044543@news1.attglobal.net> <7vug59$68g$1@news.igs.net>`

```
    Once you decide that the code is cluttered enough, and you want to reset
it back
to all uppercase, you can use the DIFF utility that comes with 16 bit MF to
renumber cols 1-6,
 and uppercase all source code without disturbing comments or literals.


donald tees <donald@willmack.com> wrote in message
news:7vug59$68g$1@news.igs.net...
> I have been using case to clarify code here and there as well.  I am not
> sure if I like the practice, though.  While I found it handy to emphasize
> certain things, after a while the code just starts to get cluttered
looking.
>
    <snips>

> >Another thing I do, that some might dislike, is code any new code in
> >all lower case.  It helps me know what I added vs what was there
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Interesting code

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vu6a0$ppf$1@starburst.uk.insnet.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net>`

```
I would imagine the single period in this case is just to allow the STOP RUN
to be commented out (and uncommented later?).

We have a rule that changed code should be commented out so people can see
what was there before.   However we insist on multiple asterisks (***** STOP
RUN) to allow this to be easily identified when reading through code.   I've
had problems in the past trying to figure out a piece of code because I
didn't immediately spot that some lines were commented out.   I guess on
colour coded PC editors this wouldn't be such a problem. :-)

Rick

donald tees <donald@willmack.com> wrote in message
news:7vtlff$gp5$1@news.igs.net...
> I was reading code (by people in my employ) when I ran across this snippet
I
> thought interesting. I have not been a proponent of the one period on a
line
> style in the past, but I thought this usage rather interesting. The fact
> that two lines have been commented out but left in as comments is also
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Interesting code

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822DFB1.3F5A96D5@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net>`

```
Rick Price wrote:
> 
> I would imagine the single period in this case is just to allow the
…[10 more quoted lines elided]…
> Rick

MVS now colour codes as well (HILITE ON).

I hate commented code.  I have SCLM (free for MVS) or SCCS on the unix
and I can recover the old code and do a compare in the middle of the
night if need be.

The extra code just adds overhead to the process and instead of
focusing on what it does do we focus on what it does not.

2 cents
Ken
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38239EC4.DCF9319F@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au>`

```
Ken Foskey wrote:
> 
(snip)
> 
> MVS now colour codes as well (HILITE ON).
…[6 more quoted lines elided]…
> focusing on what it does do we focus on what it does not.

Here, here, Ken. We seem to be on the same wavelength here.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vuuvh$4jl$1@starburst.uk.insnet.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au> wrote in message
news:3822DFB1.3F5A96D5@zip.com.au...
> Rick Price wrote:
> >
…[23 more quoted lines elided]…
> Ken
Ken

Yeah, but you don't know there is anything worth looking for!  Commented
code on complex problems at least gives you the chance to see that something
has been tried before.   Although we clean up commented code, on a module
that hasn't been changed for some time, commented code gives you some kind
of  time perspective.

I dislike commented code that doesn't stand out, hence our standard for
multiple asterisks, but over the last 20 odd years we have found it very
useful.

I don't understand why commented code adds overhead to the process.  Surely
it just means the compiler has to read a few extra lines.  It certainly can
give you an historical perspective on problems.

Rick
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3824328A.CC742191@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net>`

```
Rick Price wrote:
> 
> I don't understand why commented code adds overhead to the process.
…[3 more quoted lines elided]…
> Rick

warning:  strong opinion follows

I agree but the cost of the extra code is the extra paging and
scanning code that does nothing. Maintenance programmers cost a lot of
money relative to everything else.

The historical perspective is overrated, someone made the decision to
strip the code out and you want to second guess them.  Focus on the
real problem (new function, bug fix, whatever) and leave history to
historians.

Not playing nice tonight :-}
Ken
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j2XU3.11939$B15.133756@news3.mia>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au>`

```
Ken Foskey wrote:
>
>... Maintenance programmers cost a lot of money relative to everything
…[5 more quoted lines elided]…
>historians.

Ken, you express my opinion *exactly*.  :-)
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3826DF9F.F6816A5F@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au>`

```
Ken Foskey wrote:
> 
> Rick Price wrote:
…[11 more quoted lines elided]…
> money relative to everything else.

Maintenance programmers cost money when they don't know what the
relevant "fix" did.  The quicker they understand the intent of the
program and especially of the changes to the program, the less they
cost.
 
The first place to look for a new problem is at recent maintenance. 
This doesn't mean the latest change (which usually is available via some
change control), but this means RECENT changes, which may be a few
generations back.  Besides, looking at the code is quicker than doing a
bunch of code comparisons.

Now I agree it would be nice to have a procedure to get rid of old
change documentation which was reviewed and determined to be unneeded. 
(Review is necessary), but what shop has the resources to do this?
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_0GV3.1002$VO5.11333@news3.mia>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com>`

```
Howard Brazee wrote:
>
>Maintenance programmers cost money when they don't know what the
>relevant "fix" did.  The quicker they understand the intent of the
>program and especially of the changes to the program, the less they
>cost.

How does wading through hundreds of lines of *obsolete* code, in
addition to thousands of lines of current code, help them understand
'quicker'?  If a person is new to the program, they could care less
about what it *used* do do, they're busy enough trying to determine
what it's doing now.  If they are familiar with the program, they
probably already know what it used to do, and what it's doing now.
In neither case are the old comments helpful.  I recently did some
Y2K remediation for a client.  Perhaps 25% of the systems included
obsolete code, commented out.  It seriously interfered with what I
was trying to do, and I hate the practice. :-)
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382748DE.C9E6D357@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[15 more quoted lines elided]…
> was trying to do, and I hate the practice. :-)

When a previously working program aborts, a good strategy is to look at
recent changes to see what has changed.

Commented out code has never interfered with my work, but I can see how
it may be irritating.  Still, maintenance costs are high, emergency
maintenance costs are highest.  Making it easy to find recent changes
(not just the last update) can be worth a great deal of time saved.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 7)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D6JV3.411$IE6.15427@typhoon01.swbell.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia>`

```

Judson McClendon <judmc123@bellsouth.net
> wrote in message news:_0GV3.1002$VO5.11333@news3.mia...

> How does wading through hundreds of lines of *obsolete* code, in
> addition to thousands of lines of current code, help them understand
…[8 more quoted lines elided]…
> --

"Find a need and fill it," I always say. For a modest honorarium,
I'll write a program for you that will strip out all comments in your
offensive source code.

For not much more, I can simultaneously strip out all vowels in
data names. I can even imagine a "Professional Programmer" edition
that replaces all data names with tokens ("A0000 - A9999,"
"B0000-B9999," etc.).
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<807qul$dfs$1@mail.pl.unisys.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <D6JV3.411$IE6.15427@typhoon01.swbell.net>`

```
Hmmmph.  Reminds me of a program I once had the misfortune to look at.  It
was a cross-reference-and-flowchart utility (in which the flowcharting
facilities had been disabled, but not entirely eliminated) for COBOL
programs, written in COBOL, that was obviously written by a Fortran
programmer who was using it as a test vehicle to school himself on all the
wondrous uses and possibilities for the ALTER verb while simultaneously
trying to absorb the barest rudiments of COBOL.   Never have I seen a
program less decipherable in my thirty-plus years in data processing.  And
I've seen some grim programs in my day (though to be fair most weren't
written in COBOL).

    -Chuck Stevens

Jerry P <bismail@bisusa.com> wrote in message
news:D6JV3.411$IE6.15427@typhoon01.swbell.net...
<history snipped>
>
> "Find a need and fill it," I always say. For a modest honorarium,
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 9)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8083qi$be6$1@nntp4.atl.mindspring.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <D6JV3.411$IE6.15427@typhoon01.swbell.net> <807qul$dfs$1@mail.pl.unisys.com>`

```
I have a simple rule about the verb ALTER -
IF YOU USE ALTER, I WILL KILL YOU.

No 3 strikes, no suspended sentence, no 2nd chances. I will devise a death
that
takes as long as it took me to figure out what effect the ALTER had.

On the subject of cols 1-6, They can be useful. If (on MF), working in a
controlled
development environment such as LCS, SCLM or my current one - Changeman,
you can put the package/release/etc ID no in cols 1-6, and put an ID in the
maintenance history.

But when it comes to removing code, packages like Changeman keep multiple
versions - so there's no need to keep redundant code  - rip it out, and take
out
any comments that refer to it too.

Chuck Stevens <charles.stevens@unisys.com> wrote in message
news:807qul$dfs$1@mail.pl.unisys.com...
> Hmmmph.  Reminds me of a program I once had the misfortune to look at.  It
> was a cross-reference-and-flowchart utility (in which the flowcharting
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 10)_

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<808rjd$p1i$1@starburst.uk.insnet.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <D6JV3.411$IE6.15427@typhoon01.swbell.net> <807qul$dfs$1@mail.pl.unisys.com> <8083qi$be6$1@nntp4.atl.mindspring.net>`

```

Unbeliever <popsider@ix.netcom.com> wrote in message
news:8083qi$be6$1@nntp4.atl.mindspring.net...
> I have a simple rule about the verb ALTER -
> IF YOU USE ALTER, I WILL KILL YOU.
…[3 more quoted lines elided]…
> takes as long as it took me to figure out what effect the ALTER had.
<snip>

I agree generally.  However, we once had a program which used ALTER.  It was
totally understandable and efficient and I couldn't see how to improve the
program by taking it out.  It was with us for many years and successfully
transferred to different platforms.

We finally got rid of it because the utility it was part of had to be
rewritten in C.

Mind you the C is a lot less easy to understand than the ALTER <G>.

Rick
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382766CD.1F27337E@worldnet.att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia>`

```


Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[17 more quoted lines elided]…
> Judson McClendon      judmc123@bellsouth.net  (remove numbers)

One of my former bosses hated it as well, and part of our code walkthru
process was to ensure that no commented-out code was left in the
program.  He argued that the source code manager should be used for that
purpose (we use Endevor).  I sometimes find myself running a SuperC
compare of the current version against a prior version to see if
anything unusual changed.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 8)_

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<808qcg$ok5$1@starburst.uk.insnet.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net>`

```
Yeah but how many versions back do you go?

And how do you decide what was replaced with what?

I like well commented programs.  As far as I'm concerned, commented out code
is comments.  Sure when it becomes redundant it can be removed but where's
the pain?

Rick

Arnold Trembley <arnold.trembley@worldnet.att.net> wrote in message
news:382766CD.1F27337E@worldnet.att.net...
>
>
…[31 more quoted lines elided]…
> http://home.att.net/~arnold.trembley/
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 9)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3827F2F1.AFD23964@worldnet.att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net>`

```
Rick Price wrote:
> 
> Yeah but how many versions back do you go?

Endevor supports 100 versions before you have to compress (I believe). 
We've only had it about six years, so that's more than enough so far.
> 
> And how do you decide what was replaced with what?

Endevor also has a "browse history" function, so you can view
added/deleted lines relative to the version you are looking at. 
Sometimes I use superc because I don't want to fire up another TSO app.

> 
> I like well commented programs.  As far as I'm concerned, commented out code
…[3 more quoted lines elided]…
> Rick

It's certainly a debatable subject.  Some people find interspersed
comments of any variety offensive.  My boss didn't like commented-out
code because he felt it made the programs harder to understand.  I
tended to agree with him, but he had felt very strongly about it so it
was best to stay on his good side.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 9)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3828153B.E5D82F7E@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net>`

```
Rick Price wrote:
> 
> I like well commented programs.  As far as I'm concerned, commented
> out code is comments.  Sure when it becomes redundant it can be
> removed but where's the pain?

I will mostly disown this opinion but it is interesting to consider...

Comments should not exist in code.  If the code requires a comment you
can either rename variables to should the true purpose or separate the
function into a separate called module (perform) this effectively
becomes your comment and eliminates it.

This has the benefit of extracting smaller functions that can be
easily reused in other sections and assists removing of duplicated
code.

....

I have paraphrased a comment from comp.object.  I kind of agree with
it. Comments should be restricted to the why.

I am currently reading refactoring by Martin Fowler.  He says
something similar to the above.  Once I have finished the book I will
attempt to give a summary.

Ken
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3828671B.8C57531B@home.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au>`

```


Ken Foskey wrote:
> 
> Rick Price wrote:
…[14 more quoted lines elided]…
> code.

Ken,

This kind of ties-in with your comments about small methods in OO
doesn't it. Generally speaking, I rarely use commenting - but sometimes
it can be useful to have a one or two-liner comment to remind me why I
coded in a particular way, so that I don't fall into the trap of coding
something that I found out previously didn't work.

And like Judson, I don't keep 'junk' to refer to, as to how the program
used to perform - I'm only interested how it works now with its current
function - and it's that I want to change, should the program fail, not
the history.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<809pq8$it$1@aklobs.kc.net.nz>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

: Comments should not exist in code.  If the code requires a comment you
: can either rename variables to should the true purpose or separate the
: function into a separate called module (perform) this effectively
: becomes your comment and eliminates it.
: ....

I entirely agree.  When maintenance is done the original comments
in a program are often overlooked and not changed to represent
how the program now works.  This may be because, for example, the
comment is at the PERFORM of a piece of code and when the paragraph
itself is changed the programmer does not see them to change them.

Out of date, or simply wrong, comments are worse than no comments
at all.  Clearly written code that concentrates on using
descriptive paragraph names and variable names means the same
to the computer and to the programmer.

Commented code tends to distract the reader and make them think
that the code follows the comment, making the reader less
attentive to what the code _actually_ does.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 11)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80a9ck$gg2$1@news.igs.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au> <809pq8$it$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote in message <809pq8
<BIG SNIPPAGE>

>Commented code tends to distract the reader and make them think
>that the code follows the comment, making the reader less
>attentive to what the code _actually_ does.
>
I agree. Recently I have learning OOP stuff, and I have been using the
examples from the Fujitsu 4.0 disk.  I was going nuts trying to understand
what was happening, until I got smart and removed all the comments.  Once I
had taken all the garbage out  (all rather fractured nonsense that said far
less about the code than the code, and made reading the code impossible), I
found the programs *much* easier to understand.  I could see more than a
couple of lines at once, for one thing.

Why anybody would think a list of data names is "documentary" when preceded
by an asterisk, while a record description with picture clauses and level
numbers that shows the inter-relationships and data type is not
"documentary", is beyond me.  I got the impression that the examples were
written by a C coder that did not like Cobol.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3828B026.1533E339@home.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au> <809pq8$it$1@aklobs.kc.net.nz> <80a9ck$gg2$1@news.igs.net>`

```


donald tees wrote:
> 
> Richard Plinston wrote in message <809pq8
…[8 more quoted lines elided]…
> what was happening, until I got smart and removed all the comments.  

Interesting comment Donald. Same applied to me looking at the N/E OO
examples.

Jimmy
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 10)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3828ccea.215104609@news1.attglobal.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au>`

```
On Tue, 09 Nov 1999 23:36:11 +1100, Ken Foskey <waratah@zip.com.au>
wrote:


>I have paraphrased a comment from comp.object.  I kind of agree with
>it. Comments should be restricted to the why.
>

Interesting.  Mostly I find myself leaving notes to myself.  "This
looks wrong, but it isn't", or "You did this on purpose".   In
particulary tricky code I comment what is being done and why and how.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 11)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3829411F.52FFAEE4@zip.com.au>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au> <3828ccea.215104609@news1.attglobal.net>`

```
Thane Hubbell wrote:
> 
> On Tue, 09 Nov 1999 23:36:11 +1100, Ken Foskey <waratah@zip.com.au>
…[8 more quoted lines elided]…
> particulary tricky code I comment what is being done and why and how.

A rare occasion where I kind of disagree.

If the code is obscure rewrite it to be clearer.  Unless there are
severe penalties on run time (Verified not opinion).  You are often
not optimizing the right thing.

I tend to leave comments in code I could not understand on my
understanding of the code with 'I THINK' in it.

Ken
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3829B691.3BC3A7DC@home.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au> <3828ccea.215104609@news1.attglobal.net> <3829411F.52FFAEE4@zip.com.au>`

```


Ken Foskey wrote:
> 
> Thane Hubbell wrote:
…[20 more quoted lines elided]…
> 

Sorry Ken, but I'll agree with Thane on this one. Not tricky code per
se, but if I have coded in a particular context, I may think back later
why did I code it that way, I could have done this. And my comment
reminds me exactly why I did it that way.

Jimmy
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0YdW3.4952$z26.57947@news4.mia>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au> <3828ccea.215104609@news1.attglobal.net> <3829411F.52FFAEE4@zip.com.au>`

```
Ken Foskey wrote:
>
>If the code is obscure rewrite it to be clearer.  Unless there are
>severe penalties on run time (Verified not opinion).  You are often
>not optimizing the right thing.

Not always possible. :-)  Sometimes code is based on an algorithm
that is complex or abstract to the point that you could not write
the code in a way as to be clear why you are doing what.  You don't
see this a lot in COBOL programs, but some algorithms can be really
obscure, unless commented.  Calculating the date of Easter, say for
a list of holidays in a payroll program, is not crystal clear. :-)
In such cases, I put a comment block describing the algorithm.  And
also write the code to be as clear as possible. :-)
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 12)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38297C9E.F0288EF@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net> <808qcg$ok5$1@starburst.uk.insnet.net> <3828153B.E5D82F7E@zip.com.au> <3828ccea.215104609@news1.attglobal.net> <3829411F.52FFAEE4@zip.com.au>`

```
Ken Foskey wrote:

> > Interesting.  Mostly I find myself leaving notes to myself.  "This
> > looks wrong, but it isn't", or "You did this on purpose".   In
…[6 more quoted lines elided]…
> not optimizing the right thing.

Sometimes the obscurity isn't in the code, it's in the business rules. 
A note to say that this is really what accounting, or purchasing, or the
CIO really wants can be helpful.

The right way, the wrong way, and the Army way...
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38282BE2.7AFB576@NOSPAMhome.com>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia> <382766CD.1F27337E@worldnet.att.net>`

```
Arnold Trembley wrote:

> One of my former bosses hated it as well, and part of our code walkthru
> process was to ensure that no commented-out code was left in the
…[3 more quoted lines elided]…
> anything unusual changed.

That works pretty well if the change you care about is in the very last
migration.  If you have to go though various previous changes, it
doesn't work as well.

I recommend that you have a standard that when code is migrated - all
commented code over, say 3 months old gets deleted UNLESS there is a
***  leave this *** statement.  Let the programmers decide to leave
comments where you have regular changes.

If you have three migrations of different changes within a month, all of
the changes will be easy to see, but more stable code no longer has the
commented code.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 9)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991109114631.11319.00000053@ngol01.aol.com>`
- **References:** `<38282BE2.7AFB576@NOSPAMhome.com>`

```
In article <38282BE2.7AFB576@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes:

>
>I recommend that you have a standard that when code is migrated - all
…[8 more quoted lines elided]…
>

I don't usually use a time period  for determining the removal of dead code.
In past exerience, I have used a rule of 3 major maintenance cycles before 
cleaning out dead stuff.  Although there have been exceptions, where a
particular
piece of code handled a unique function/feature that I might want to use as 
a reference at a later date, or where I found code being re-introduced on a 
alternating project cycle.   (delete the code this month, three months of
updates,
then OH BTW! re-instate that code from 4 months ago 'We need it again').

I am not fortunate enough to be working in a shop with any kind of version
control.
Any recovery that I have is done purely thru my own backup/recovery procedures.
Currently involves using IND$FILE to download every member that I have touched
today and PKZIPing the files into an archive that rolls by project or by date 
depending on the PDS that I am capturing from.
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38294226.A0F4BE4@zip.com.au>`
- **References:** `<38282BE2.7AFB576@NOSPAMhome.com> <19991109114631.11319.00000053@ngol01.aol.com>`

```
Sff5ky wrote:
> 
> I am not fortunate enough to be working in a shop with any kind of
> version control.

You mention IND$FILE so I am assuming MVS.  Look at SCLM (even if you
use it yourself and copy it over later) it is free with ISPF.

If you need help call :-}
Ken
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 11)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3829be8d.276973090@news1.attglobal.net>`
- **References:** `<38282BE2.7AFB576@NOSPAMhome.com> <19991109114631.11319.00000053@ngol01.aol.com> <38294226.A0F4BE4@zip.com.au>`

```
On Wed, 10 Nov 1999 21:00:06 +1100, Ken Foskey <waratah@zip.com.au>
wrote:

>Sff5ky wrote:
>> 
…[5 more quoted lines elided]…
>

It's been available for VSE for a long time too.  (Even back as far as
DOS).

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 7)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38279D66.2D48FFB9@att.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <7vu6a0$ppf$1@starburst.uk.insnet.net> <3822DFB1.3F5A96D5@zip.com.au> <7vuuvh$4jl$1@starburst.uk.insnet.net> <3824328A.CC742191@zip.com.au> <3826DF9F.F6816A5F@NOSPAMhome.com> <_0GV3.1002$VO5.11333@news3.mia>`

```
Judson McClendon wrote:
> 
(snip)
> 
> How does wading through hundreds of lines of *obsolete* code, in
…[8 more quoted lines elided]…
> was trying to do, and I hate the practice. :-)

There, there (that's an even stronger "here, here (sic)",

Bill Lynch :-)
```

#### ↳ Re: Interesting code

- **From:** "Don Pace" <donp@yahoo.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf3385$1137cdc0$4e9e99ce@ns.webzone.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net>`

```
I have been programming in Cobol for quite a number of years.  I see the
concept of putting the period on a line by itself as another one of those
bright ideas of some Professor Popoff that has never spent one day actually
programming in a real environment.  Just another nail on the Cobol coffin.

donald tees <donald@willmack.com> wrote in article
<7vtlff$gp5$1@news.igs.net>...
I was reading code (by people in my employ) when I ran across this snippet
I
thought interesting. I have not been a proponent of the one period on a
line
style in the past, but I thought this usage rather interesting. The fact
that two lines have been commented out but left in as comments is also
rather interesting, stylistically.  Any thoughts?


           MOVE SELECTOR-TOP TO SP2-WD-TITLE.
           CALL "SP2" USING SP2-OPEN-WINDOW SP2-WINDOW-DEF.
           IF SP2-WD-RET-CODE IS NOT EQUAL TO ZERO
               DISPLAY "SP2-WD-RET-CODE = ", SP2-WD-RET-CODE
      *         STOP RUN
           .
           MOVE LOW-VALUES TO SP2-PD-DATA.
      *     MOVE -1 TO SP2-PD-MENU-ROWS.
           MOVE SELECTOR-TOTAL-WIDTH TO SP2-PD-WIDTH.
```

##### ↳ ↳ Re: Interesting code

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383a323f.64365048@news.gw.total-web.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <01bf3385$1137cdc0$4e9e99ce@ns.webzone.net>`

```
Well it sounds like a good idea to me, so just call me "Prof".

On Sat, 20 Nov 1999 17:24:50 GMT, "Don Pace" <donp@yahoo.com> wrote:

>I have been programming in Cobol for quite a number of years.  I see the
>concept of putting the period on a line by itself as another one of those
>bright ideas of some Professor Popoff that has never spent one day actually
>programming in a real environment.  Just another nail on the Cobol coffin.
>

---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

###### ↳ ↳ ↳ Re: Interesting code

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3838948C.EEAEA2CA@nbnet.nb.ca>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <01bf3385$1137cdc0$4e9e99ce@ns.webzone.net> <383a323f.64365048@news.gw.total-web.net>`

```
As someone who has been coding in COBOL since 1963, I vote for the 2
periods per paragraph: 1 after the paragraph name and one at the end of
the paragraph on a line by itself.  It makes wok with the scope
terminators simpler and means that I can move things around in the
paragraph.

Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca 

Paul Knudsen wrote:
> 
> Well it sounds like a good idea to me, so just call me "Prof".
…[10 more quoted lines elided]…
> SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

###### ↳ ↳ ↳ Re: Interesting code

_(reply depth: 4)_

- **From:** "The COBOL Frog" <H.Klink@IMN.nl>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81chr7$2k$1@porthos.nl.uu.net>`
- **References:** `<7vtlff$gp5$1@news.igs.net> <01bf3385$1137cdc0$4e9e99ce@ns.webzone.net> <383a323f.64365048@news.gw.total-web.net> <3838948C.EEAEA2CA@nbnet.nb.ca>`

```
I code since 1974. No that long, but I vote the same.
Clark Morris <morrisc@nbnet.nb.ca> wrote in message news:3838948C.EEAEA2CA@nbnet.nb.ca...
> As someone who has been coding in COBOL since 1963, I vote for the 2
> periods per paragraph: 1 after the paragraph name and one at the end of
…[8 more quoted lines elided]…
> > Well it sounds like a good idea to me, so just call me "Prof".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
