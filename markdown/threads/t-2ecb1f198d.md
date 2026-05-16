[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GO TO and THROUGH

_21 messages · 15 participants · 2000-09 → 2000-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### GO TO and THROUGH

- **From:** "Floyd Johnson" <floydj@netins.net>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
I suspect that this question may be one that may start a religious war, but
I want to ask.  I am using Thane Hubbell's book.  In chaptes 10 and 11 he
introduces the GO TO and THROUGH keywords.  Though my training in COBOL goes
back to 1966/67  when I first used COBOL as a high school student in an
Explorer Post sponsored by IBM, my professional exposure has been minimal.
I am currently teaching a "File Processing with COBOL" course for sophomore
CS students  where COBOL is their second language (there first was one year
of JAVA and data structures).

Having said that, it would seem to me that these two keywords (GO TO and
THROUGH) lend themselves to unstructured and potentially difficult to debug
programs.  My gut feeling (given my strong background in structured
programming) would be to discourage their use in new programs, but to make
sure that students understood their use so they can read and maintain
program that contain these constructs.

I would stop there and not even ask the question - except I trust the text
and the fact that the author has chosen to include these topics in the midst
of other important concepts would give them greater significance than I
would in the classroom.  I want to make sure that I am not missing
something.

Thanks for any advice or comments.

Floyd Johnson
```

#### ↳ Re: GO TO and THROUGH

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<npRA5.232$Rd6.65229@nnrp3.sbc.net>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```

"Floyd Johnson" <floydj@netins.net

> I am currently teaching a "File Processing with COBOL" course for
sophomore.....

You illustrate the difference between a book an a teacher. In a book,
everything is in the same size (usually) type and, to the reader, all
things look equally important.

A teacher, on the other hand, can emphasize or diminsh topics
according to their real-world significance.

In a book on COBOL, the author just has to mention GO TO and THRU (and
maybe even ALTER) because they are a part of the language. You job, as
a teacher, is to assign relative values to these topics. You are
correct in your initial impression that GO TO (et al) sucks big time.
Please inform your students accordingly.
```

#### ↳ Re: GO TO and THROUGH

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8r0o7c02adu@enews2.newsguy.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
I would say that Shop Standards are the key in the workplace.  Use whatever
constructs you'd like, just don't go too far outside the box.  PERFORM THRU
EXIT (which we shall now call PTE, or the PTE Instruction) is the better
choice if that will better comply with shop standards.

Just as with internal sort, the PTE and GOTO verbs can be used very
effectively, but usually it's better to stay a little cleaner if it won't
compromise the system too much.

I also work in PowerBuilder.  It does not have a GO TO verb.  That fact does
not inherently promise, or deliver, better code.

There are situations where different contructs work better.  I could build
you a small system using VSAM, internal sorts, GO TOs, PTEs, workfiles
galore, etc.  and it would fly and be very efficient.  But I'd rather have
it as a flat filed, externally sorted program without GO TOs or PTE.

It just depends.

Jeff

----------
In article <8qvg1d$mr9$1@ins21.netins.net>, "Floyd Johnson"
<floydj@netins.net> wrote:


> I suspect that this question may be one that may start a religious war, but
> I want to ask.  I am using Thane Hubbell's book.  In chaptes 10 and 11 he
…[24 more quoted lines elided]…
>
```

#### ↳ Re: GO TO and THROUGH

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D34C6D.6C731CE6@brazee.net>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
Floyd Johnson wrote:
> 
> I suspect that this question may be one that may start a religious war, but
…[13 more quoted lines elided]…
> program that contain these constructs.

I hate GO TO and THROUGH constructs.  But I have to work with programs
which were written using both constructs.   So I agree with you
completely.

There are people who are advocates of both commands, but only to allow
for a GO TO THIS-PARAGRAPH-EXIT which is a dummy paragraph at the end of
a THRU.  They want a way to exit a paragraph without switches.   With
the next version of COBOL, this will no longer be necessary, as there
will be commands to exit paragraphs, sections, and performs.

And there is one person on this newsgroup who likes GO TO in standard
in-line code.  I wouldn't be surprised if there is another person out in
the industry who agrees with him.   He is a developer who doesn't have
to maintain other people's code, which makes a big difference in which
standards work best.
```

#### ↳ Re: GO TO and THROUGH

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%tIA5.9005$bD5.57423@news3.atl>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
"Floyd Johnson" <floydj@netins.net> wrote:
>
> Having said that, it would seem to me that these two keywords (GO TO and
…[10 more quoted lines elided]…
> something.

You will find most of the experienced programmers around here in close
agreement with you on those points, including Thane Hubbell, who will
probably respond himself.  However, there are some programmers here who
advocate PERFORM THRU for various reasons.  Personally, there is only
one reason why I use either construct in COBOL.  In some of the systems
I write, there is a need for paragraphs containing long series of 'IF'
statements, any of which, if true, should exit the paragraph.  If COBOL
had the EXIT PARAGRAPH construct proposed in the draft standard, it
would be perfect for this purpose (most structured languages provide
an 'exit block' statement).  Also, two of my largest clients still use
COBOL 74, so the END-xxx constructs aren't available.  For this reason,
on these systems I use PERFORM xxx THRU xxx-EXIT and GO TO xxx-EXIT.
As you note, this can be a dangerous practice, so I use a code checker
program that enforces the PERFORM and THRU paragraphs match, there are
no intermediate paragraph names, and it flags any GO TO outside the
paragraph.  But my situation is certainly not typical, I don't use GOTO
in any other language, and will drop PERFORM THRU and GO TO as soon as
EXIT PARAGRAPH is available. :-)
```

##### ↳ ↳ Re: GO TO and THROUGH

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D3A3A2.C611D90B@home.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <%tIA5.9005$bD5.57423@news3.atl>`

```


Judson McClendon wrote:
> 
> But my situation is certainly not typical, I don't use GOTO in any > other language, and will drop PERFORM THRU and GO TO as  soon as  EXIT > PARAGRAPH is available. :-)

Judson,

Bite the bullet - switch to OO in NetExpress and you can IMMEDIATELY use
EXIT METHOD <G>

Jimmy
```

###### ↳ ↳ ↳ Re: GO TO and THROUGH

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3GNA5.44386$dZ2.15987772@news3.rdc1.on.home.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <%tIA5.9005$bD5.57423@news3.atl> <39D3A3A2.C611D90B@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:39D3A3A2.C611D90B@home.com...
>
>
> Judson McClendon wrote:
> >
> > But my situation is certainly not typical, I don't use GOTO in any >
other language, and will drop PERFORM THRU and GO TO as  soon as  EXIT >
PARAGRAPH is available. :-)
>
> Judson,
…[4 more quoted lines elided]…
> Jimmy

Neato! I didn't know Merant had ported NetExpress to the mainframe. Where
can I get a copy? ;-)
```

#### ↳ Re: GO TO and THROUGH

- **From:** Herwig Huener <Herwig.Huener@fujitsu-siemens.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D36FE9.EE8BA39C@fujitsu-siemens.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
2000-09-28 17:17:17 MESZ

Floyd Johnson schrieb:

...

I hate GOTOs in every language. But now and
then on encounters a Situation where there
is a need to use it.

For instance, recently I wrote a routine
which inserts some hundred words into a search
tree. The words were alphabethically  ordered,
and inserting them in this order would create
a degenerated tree - functional but not
good for performance. On the other hand,
I did not want to reorder these insertions
for the sake of maintenace.

So I built a GOTO-structure which made
sure that all those insertions are executed
exactly once, but not in the order in which
they are written down. Now the tree
looks fine and is nearly balanced.

That was the only case in which a GOTO was
justified, in my eyes, in 20 years of
programming.

Herwig
```

#### ↳ Re: GO TO and THROUGH

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D39BA1.8D5FF53@neo.rr.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
Floyd Johnson wrote:
> 
> I suspect that this question may be one that may start a religious war, but
…[6 more quoted lines elided]…
> of JAVA and data structures).
<snip>

You are absolutely right, this will start a religious war.

Here is the problem - If the only tool you have is a hammer, then
all problems appear to be nails.  Sometimes management takes away
a tool (yeah, think out of the box) and that causes some
problems.  Let me give some examples:

I have worked in many different environments -- some that
prevented [artificially] any one from using GO TO.  All
paragraphs had to be performed (top down structured).  I finally
won an exception for my code, because I was doing CICS work. 
Once I showed them that I could be very structured using GO TO,
and that my code used much less of CICS' resources that way (read
that, ran much faster, paged less), they allowed the use of GO TO
in CICS programs.  They even accepted the idea of "Fall Through"
code -- NO PERFORMS ALLOWED (except for a search of a table or
something similar).  It ultimately bought them 20% of their CPU
and PAGE delays in their CICS regions which delayed a CPU
upgrade.

I have also seen shops that did not allow Report Writer, because
their management didn't understand it.  Same was true of
DECLARATIVES!  Get them to accept R/W, and they are amazed at how
much productivity you can get from your programmers.  Establish a
base program and use it to create your reports.  4 hours from
specs to production (almost as fast as I can do it w/ RPG!).  

Now, enter some third party software that you have to interface
with (CICS, DL/I, DL/1, IMS, IDMS, etc.), and suddenly, you have
to allow for all kinds of interesting constructs.  Why?  Because
the implementation of the product you are interfacing with forces
it upon you.

How would you like to be called by some routine, that requires
you to call it back?  Why?  Because you can't have multiple entry
points in your code.  So to fix this, you have to call the caller
back so you can pass it the function and paragraph name within
your code so it can call you back directly!  Now, go ahead, do a
perform and try to figure out where you come down on this one! 
Granted, what I'm talking about is rather dated (COBOL '74 and
IMS/DC), but, these are some of the things that dictate how you
must write a program. 

Now, let's take the "THRU" (or "through") construct and examine
it.  In the days of yore, we had sections within the procedure
division and optionally they were numbered (back in the REAL or
CORE based machine days, you had the system build you overlays
for really large programs...).  If you did not specify the THRU
in one place and did in another, well, in ye old IBM terminology,
"the results are unpredictable", particularly when you had GO
TO's embedded.  [I think this is what got the "GO TO" -less code
tirade started.]  So, some shops made it mandatory that you must
always use a "THRU" and you must always use "******-EXIT.  EXIT."
constructs so it was obvious where you ended execution.

So back to where I started.  If the only tool you have is a
hammer, all problems look like nails.

Now with pointers, EVALUATE, END-IF, and the other niceties that
we currently have in COBOL, I don't write code the way I use to
when we were told we had to use the 68 or 74 standards.  But I
still, to this day, use THRU and GO TO to make it obvious where a
paragraph and/or block of code end.  But then, my language of
choice is S/3x0 ALC, and using Priv-Ops (ok, so I'm the wacky sys
prog who writes in RPG, COBOL, and other H/L Languages -- I try
to pick the tool that matches the job).
```

##### ↳ ↳ Re: GO TO and THROUGH

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g1mm3r0.pminews@news.wanadoo.es>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D39BA1.8D5FF53@neo.rr.com>`

```
On Thu, 28 Sep 2000 19:28:20 GMT, Steve Thompson wrote:

>Now with pointers, EVALUATE, END-IF, and the other niceties that
>we currently have in COBOL, I don't write code the way I use to
…[8 more quoted lines elided]…
>
Steve,

You are not the only sysprog who uses COBOL, I once wrote a VSAM Listcat
replacement and a VSAM undelete program in COBOL For moving data up and down
it's still the easiest language available)

Willem Clements
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

#### ↳ Re: GO TO and THROUGH

- **From:** David Bretz <DBretz@mescoma.com>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D461C9.7B57D5D6@mescoma.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
Actually, I use GO TO and THRU to create very structured programs
(actually, modular programs).  For Example:


Procedure Division.

0000-MAIN-PARAGRAPH.
     PERFORM 1000-PARAGRAPH THRU 1000-EXIT.
     PERFORM 2000-PARAGRAPH THRU 2000-EXIT.
     PERFORM 3000-PARAGRAPH THRU 3000-EXIT.
     STOP RUN.
0000-EXIT.  EXIT.

1000-PARAGRAPH.
     PERFORM 1100-PARAGRAPH THRU 1100-EXIT.
     PERFORM 1200-PARAGRAPH THRU 1200-EXIT.
 
     IF SOME CONDITION
        GO TO 1000-EXIT.
  
      PERFORM 1300-PARAGRAPH THRU 1300-EXIT.
1000-EXIT.  EXIT.

1100-PARAGRAPH.
1100-EXIT.  EXIT.

ETC

ETC


I think you get the idea.  I always use PERFORM THRU and never GO TO
outside a performed paragraph.  Each paragraph in one of my programs
does one function, and I mearly combine the functions to make a complete
program.

Dave Bretz


Dave Bretz

Floyd Johnson wrote:
> 
> I suspect that this question may be one that may start a religious war, but
…[23 more quoted lines elided]…
> Floyd Johnson
```

##### ↳ ↳ Re: GO TO and THROUGH

- **From:** "Cliff Peterson" <cliff.peterson@spamcop.net>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hA5B5.41720$A4.1314587@news1.giganews.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com>`

```
Procedure Division.

0000-MAIN-PARAGRAPH.
     PERFORM 1000-PARAGRAPH.
     PERFORM 2000-PARAGRAPH.
     PERFORM 3000-PARAGRAPH.
     STOP RUN.

1000-PARAGRAPH.
     PERFORM 1100-PARAGRAPH.
     PERFORM 1200-PARAGRAPH.
     IF SOME CONDITION
         PERFORM 1300-PARAGRAPH
     END-IF.

1100-PARAGRAPH.

My style, such as it is...
I don't use GO TO, but I don't think about it much.

I feel that THROUGH implies that there's an intermediate way out of the
performed routine, as does SECTION.  By avoiding GO TO, there's no need for
either THROUGH or SECTION, simplifying the code.

Many times, you see a paragraph that has 600 lines of code, peppered with a
few routines that make a decision, then jump past the rest of the code to
the end.  My way is to attempt to isolate the decisions, then PERFORM
straight-line routines as a result of each decision.

But... as a reformed spaghetti programmer (started in FORTRAN), I'm always
on the lookout for better ideas ;-)

Cliff

----------------------------------------
> Procedure Division.
>
…[18 more quoted lines elided]…
> 1100-EXIT.  EXIT.
```

##### ↳ ↳ Re: GO TO and THROUGH

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g1nr1z0.pminews@news.wanadoo.es>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com>`

```
On Fri, 29 Sep 2000 05:32:57 -0400, David Bretz wrote:

>Actually, I use GO TO and THRU to create very structured programs
>(actually, modular programs).  For Example:
…[28 more quoted lines elided]…
>
I do  more or less the same, but using SECTION istead of PERFORM THRU
Your program would look like this

MAIN SECTION.
MAIN-10..
     PERFORM SECT-1000.
     PERFORM SECT-2000.
     PERFORM SECT-3000.
     STOP RUN.
MAIN-EXIT.  EXIT.

SECT-1000 SECTION.
SECT-1000-10.
     PERFORM SECT-1100.
     PERFORM SECT-1200.
 
     IF SOME CONDITION
        GO TO SECT-1000-EXIT.
  
      PERFORM SECT-1300.
SECT-1000-EXIT.  EXIT.

SECT-1100 SECTION.
SECT-1100-EXIT.  EXIT.

The result is exactly the same, but I like the implicit hierarchy.

Of course, using this style PERFORM should only target SECTION and GO TO only
jumps to paragraphs. A cross-reference of the compilation also gives you an
easy tool to do some logic checking as well.

As always, just my opinion




Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

##### ↳ ↳ Re: GO TO and THROUGH

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D4944C.8E9D155C@brazee.net>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com>`

```


David Bretz wrote:
> 
> Actually, I use GO TO and THRU to create very structured programs
…[33 more quoted lines elided]…
> Dave Bretz

That's perfectly structured.  Some shops have syntax checkers to make
sure there are no typos, but I have actually seen a job working
(incorrectly) in production where someone cut and pasted a GO TO
1100-EXIT, and forgot to change it to GO TO 1200-EXIT.
```

###### ↳ ↳ ↳ Re: GO TO and THROUGH

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QV1B5.11071$bD5.69303@news3.atl>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com> <39D4944C.8E9D155C@brazee.net>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> That's perfectly structured.  Some shops have syntax checkers to make
> sure there are no typos, but I have actually seen a job working
> (incorrectly) in production where someone cut and pasted a GO TO
> 1100-EXIT, and forgot to change it to GO TO 1200-EXIT.

This is why I believe a program to check for this type of error is
essential if you are using PERFORM THRU and/or GO TO.  When I run my
checker on programs where my clients have been lax in using it, it
almost invariably finds PERFORM THRU the wrong exit, or GO TO outside
the paragraph, caused by exactly what you describe, or mistyping.
```

###### ↳ ↳ ↳ Re: GO TO and THROUGH

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-30T01:10:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8r3tq8$7ju$2@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com> <39D4944C.8E9D155C@brazee.net> <QV1B5.11071$bD5.69303@news3.atl>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:QV1B5.11071$bD5.69303@news3.atl...
> "Howard Brazee" <howard@brazee.net> wrote:
> >
> > That's perfectly structured.  Some shops have syntax checkers
to make
> > sure there are no typos, but I have actually seen a job
working
> > (incorrectly) in production where someone cut and pasted a GO
TO
> > 1100-EXIT, and forgot to change it to GO TO 1200-EXIT.
>
> This is why I believe a program to check for this type of error
is
> essential if you are using PERFORM THRU and/or GO TO.  When I
run my
> checker on programs where my clients have been lax in using it,
it
> almost invariably finds PERFORM THRU the wrong exit, or GO TO
outside
> the paragraph, caused by exactly what you describe, or
mistyping.
> --

    What checker?  Can we get one?




> Judson McClendon      judmc@bellsouth.net
> Sun Valley Systems    http://www.sunvaley.com
> "For God so loved the world that He gave His only begotten Son,
that
> whoever believes in Him should not perish but have everlasting
life."
>
>
>
```

###### ↳ ↳ ↳ Re: GO TO and THROUGH

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s54C5.2667$2Q4.15249@news1.atl>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com> <39D4944C.8E9D155C@brazee.net> <QV1B5.11071$bD5.69303@news3.atl> <8r3tq8$7ju$2@sshuraab-i-1.production.compuserve.com>`

```
"Russell Styles" <RWSTYLES@COMPUSERVE.COM> wrote:
> Judson McClendon <judmc@bellsouth.net> wrote:
> > "Howard Brazee" <howard@brazee.net> wrote:
…[12 more quoted lines elided]…
>     What checker?  Can we get one?

I wrote mine (they're not that hard to write), but it is so tailored
to my own coding style that it would be of limited or no value with
other coding styles.  For example, I use PERFORM THRU <exit> with
paragraph numbers.  The paragraph numbers are always ascending front
to back in the source, the numbers of a paragraph and its matching
exit paragraph are equal, and there can be no paragraphs between the
two (no duplicate numbers).  The exit paragraphs must end with -EXIT.
 Unlike some others here, I use periods after each sentence instead
of one period at the end of a paragraph.  My checker verifies that
any code line that follows a period must begin in column 12, but
other code must begin in column 16 or greater.  In this way, I can
catch missing and extra periods as well.  Any GO TO can only be to
the paragraph or exit it is within.  My clients, who all adopted my
coding style in their programming standards, purchased my checker,
but I don't sell it to anyone else.  I have added a few other little
features, such as flagging paragraph names over 30 characters long,
etc.

If you don't use a similar paragraph numbering scheme, you may need
to make two passes, one to build a paragraph table and the other to
check for overlapping performs, and GOTO outside the paragraph if
you permit GOTO.  If you use periods after each sentence, and follow
standard indentation rules, implementing the missing/extra period
test should be easy.  You really need COBOL 85 to avoid periods
after each sentence, and my two largest clients still use COBOL 74
because their COBOL 85 compiler is far slower.
```

###### ↳ ↳ ↳ Re: GO TO and THROUGH

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-30T01:09:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8r3tq1$7ju$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39D461C9.7B57D5D6@mescoma.com> <39D4944C.8E9D155C@brazee.net>`

```
> > I think you get the idea.  I always use PERFORM THRU and
never GO TO
> > outside a performed paragraph.  Each paragraph in one of my
programs
> > does one function, and I mearly combine the functions to make
a complete
> > program.
> >
> > Dave Bretz
>
> That's perfectly structured.  Some shops have syntax checkers
to make
> sure there are no typos, but I have actually seen a job working
> (incorrectly) in production where someone cut and pasted a GO
TO
> 1100-EXIT, and forgot to change it to GO TO 1200-EXIT.


    This is quite easy to do when the guilty go to is performed
only
after an error.  In that case, the incorrect go to could go
unused
for a long time.
```

#### ↳ Re: GO TO and THROUGH

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-09-29T00:26:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39d3df9e.88744447@news.transport.com>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
The "correct" standard is the one your shop enforces.  We need
programmers that know how to follow shop rules and how to maintain
both styles.

Students need to be exposed to both standards.  My shops code is about
80% PERFORM-THRU/GOTO-EXIT style, and 20% is coded without THRU and
without GOTO.  (We outlawed THRU/GOTO about 8 years ago.)

I've seen it mentioned already in this thread, but some times GO TO is
still justified for pure performance reasons, primarily in mainframe
online transaction systems where every fraction of a second is
considered important, and can slow down other users on the same
system.

Pete


On Thu, 28 Sep 2000 09:11:10 -0400, "Floyd Johnson"
<floydj@netins.net> wrote:

>I suspect that this question may be one that may start a religious war, but
>I want to ask.  I am using Thane Hubbell's book.  In chaptes 10 and 11 he
…[24 more quoted lines elided]…
>
```

#### ↳ Re: GO TO and THROUGH

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-29T03:52:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39d41084.4876211@207.126.101.100>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net>`

```
At great risk of continuing yet ANOTHER useless GO TO war, here are MY
comments quoted from Page 163 of Sams Teach Yourself COBOL in 24
Hours.  

------
COBOL, like most other programming languages, has a GO TO statement.
The Go To causes the program to jump to the Paragraph title or Section
header specified in the Go To statement.  As with Perfrom ... Thru,
the advances in the COBOL language with the 1985 standard have
eliminated any need to use Go To.  However, it seems to be the "easy
way out" for many programmers, and I think it is worthwhile to spend
some time explaining its use and abuse.
------

I'm back again.  I wanted to give the reader a complete picture - I go
on to illustrate the use of GO TO and to talk about falling through
code and the like.

Now a personal opinion - as if the above wasn't enough -

If I am writing a NEW program I will not use GO TO.  I don't code to
avoid it -- my style just doesn't require it's use -- I'm not even
tempted.  I will try to use OO if the environment supports it.  That
is my latest style.

However, if I am maintaining code, I will stick with the existing
style of the code.  If Perform ... Thru is used, or GO TO and exit is
used, I will conform to that "standard".  Mixing styles never does the
programmer that follows you any good.

On Thu, 28 Sep 2000 09:11:10 -0400, "Floyd Johnson"
<floydj@netins.net> wrote:

>I suspect that this question may be one that may start a religious war, but
>I want to ask.  I am using Thane Hubbell's book.  In chaptes 10 and 11 he
…[24 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: GO TO and THROUGH

- **From:** Floyd Johnson <floydj@netins.net>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39D485CE.97BDD198@netins.net>`
- **References:** `<8qvg1d$mr9$1@ins21.netins.net> <39d41084.4876211@207.126.101.100>`

```
Thane:

     Oops - I missed the paragraph or mis-understood it.  

Everybody Else:

     Thanks to everybody for their responses.  It helped 
     put my thoughts into perspective.

Floyd Johnson

Thane Hubbell wrote:
> 
> At great risk of continuing yet ANOTHER useless GO TO war, here are MY
…[62 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
