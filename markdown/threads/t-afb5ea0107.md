[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Closing END statements

_36 messages · 17 participants · 1997-11_

---

### Closing END statements

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3465d71a.1387021@news.tig.com.au>`

```

I am writing a style guide and I thought I would throw this open for
comment to the news group.

All statements should have a closing END statement (IF closes with
END-IF, EVALUATE with END-EVALUATE, etc). The only exception to this
is the simple statements such as a simple read.

The reason for this is to eliminate misplaced full stops (periods) at
compile time. If you are moving statements into an IF statement and
forget to remove a period from one of them a compile time error will
occur saving debug time. Should you not do this and indent the code
according to functionality it will be extremely locate the additional
period, in part due to the physical size of the period.

The END statement also makes the code readable with all statements
closed and indented back to ensure that the code is complete.

Example:
IF FRED-88
MOVE �JOE� TO WORKER (1)
MOVE �PAUL� TO WORKER (1).
MOVE �KEN� TO WORKER (2).

Most code reviews will pick up the subscripting error but not the
extra period.

If the code is written as follows then the first compile will pick up
the error.
IF FRED-88
MOVE �JOE� TO WORKER (1)
MOVE �PAUL� TO WORKER (1).
MOVE �KEN� TO WORKER (2)
END-IF.

Our standard code review consists of 3 programmers, this more than
three times the cost of picking up the compile time error and the very
small extra effort of coding cleanly.

OK comment.

TIA Ken
```

#### ↳ Re: Closing END statements

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3465d71a.1387021@news.tig.com.au>`
- **References:** `<3465d71a.1387021@news.tig.com.au>`

```

Ken Foskey wrote:
› 
› I am writing a style guide and I thought I would throw this open for
…[11 more quoted lines elided]…
› period, in part due to the physical size of the period.

[snip]

Period abuse has never been much of a problem for me. I am reluctant
to adopt a significantly different style to solve a non-problem,
especially when that style comes at a significant cost.

Unnecessary scope delimiters (END-IF and their kindred) take time to
type, they occupy space on the screen, they consume paper and ink in
the listing, and they generally clutter up the code, rendering it (to
my eyes at least) less readable. These costs are not prohibitive,
but they are not trivial either. Converting to a new style carries
additional costs.

If your shop has had problems with period abuse, the proposed policy
is a reasonable response. So is the suggestion made by Judson
McClendon elsewhere in this thread: use a code-checker to ensure that
the indentation is consistent with the punctuation.

You could combine these approaches: use a code-checker to enforce the
END-IF policy, together with whatever other policies are worth
enforcing. A good code-checker would not be trivial to write, though.
You could buy Judson McClendon's, I suppose, but his stylistic tastes
probably won't coincide with yours. Maybe it's configurable. (Judson,
this is an invitation for a shameless advertisement.)

Some people, whose tastes I otherwise respect, recommend an extended
version of your policy: one period per paragraph. This policy would
mandate a liberal use of scope delimiters. I won't raise my objections
to this policy (for now at least), but it might be a good subject for
another thread.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: Closing END statements

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap>`

```

In article <346··.@swb··l.net>,
Michael C. Kasten wrote:
› Ken Foskey wrote:
›› All statements should have a closing END statement (IF closes with
…[8 more quoted lines elided]…
›› period, in part due to the physical size of the period.

I would say this policy makes sense on a new code,
but with existing code your mileage may vary.

Dots are definitely hard to find visually -- much harder than END-IFs.
And the general premise of structured programming says that every
opening delimiter should have an explicit closing deleimiter.

Apparently dots that close sentence were invented when number of
characters punched on punch cards did matter a lot and a single
terminating dot seemed like a good solution.

However things have changed now -- the storage for code is cheap,
codes are bigger, and having them as structured programs has become
more important.


› If your shop has had problems with period abuse, the proposed policy 
› is a reasonable response.  So is the suggestion made by Judson
…[8 more quoted lines elided]…
› this is an invitation for a shameless advertisement.)

It's kinda hard for me to see how this code checker would work
for the manually written program. When live people write programs,
they follow rules to a degree, but they always sacrifice them in order to
make program more visually attractive, or avoid going to the next line
or something like this.

I would advocate approach, where you use automatic tool such as
CobolBeautifier to enforce a certain style in your program. The code
generation table in the CobolBeautifier are totally customizable, so
you can invent your own style, or take the existing shop style and
encode it into the CobolBeautifier code generaiton rules. Then by
letting all programs pass thru CobolBeautifier one time
you automatically enforce the preferred style.

The free demo of the CobolBeautifier available from
http://www.siber.com/sct/ does not let you change the code generation
tables -- you just have the 3 tables hard-wired into the program. The
full commercial version lets you put in any code generation table you
want.

The only problem with the current version of it is that it requires
some knowledge of C++ and compiler technology. I think, we'll be able
to make it more visual and completely detached from C++ or any other
language used internally in the implementation. It should happen in
the next major release.


Vadim Maslov
Siber Systems
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p3@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap>`

```

Vadim Maslov wrote:
› 
› In article <346··.@swb··l.net>,
…[7 more quoted lines elided]…
››› compile time.

I like this as a shop standard, but I think you're missing the mark on
the benefits. The principle benefit is in readability. Toward this
end, a shop standard should state that if old code is well written to a
different standard, maintain that standard. Too often I have seen
programs which were written to one standard and then patched according
to a different standard. There's nothing more baffling that a deeply
nested statement which shifts coding styles.

› Apparently dots that close sentence were invented when number of
› characters punched on punch cards did matter a lot and a single
› terminating dot seemed like a good solution.

Actually it was invented when nested statements were completely
verboten. I had a Cobol teacher tell me never to use ELSE, use GO
instead. As recently as 1978 I had to defend my use of nested IFs to
get my code past the change control committee. I got them to accept
this:

IF LAST-DEPT NOT = THIS-DEPT
PERFORM DEPT-BREAK
ELSE IF LAST-DIV NOT = THIS-DIV
PERFORM DIV-BREAK
ELSE IF LAST-SECT NOT = THIS-SECT
PERFORM SECT-BREAK
ELSE IF LAST-QUAL NOT = THIS-QUAL
PERFORM QUAL-BREAK.

But not this:

IF QUAL < 20
IF GRADE = "G"
MOVE "GOOD" TO FAB-TYPE
ELSE
MOVE "FAIR" TO FAB-TYPE
ELSE
IF GRADE = "G"
MOVE "SHORT/G" TO FAB-TYPE
ELSE
MOVE "SHORT" TO FAB-TYPE.

"Too complex." "No one will understand it." "Break it up." The
"better" way to write this was:

IF QUAL < 20
GO TO XYZ10-QUAL-LT-20.
IF GRADE = "G"
MOVE "SHORT/G" TO FAB-TYPE
ELSE
MOVE "SHORT" TO FAB-TYPE.
GO TO XYZ20-PAST-QUAL.
XYZ10-QUAL-LT-20.
IF GRADE = "G"
MOVE "GOOD" TO FAB-TYPE
ELSE
MOVE "FAIR" TO FAB-TYPE.
XYZ20-PAST-QUAL.

I  |\    Randall Bart                      mailto:Bar··.@usa··m.net
L  |/             @worldnet.att.net and @hotmail.com I am also Barticus
o  |\    1-818-985-3259                       Please reply without spam
v  | \   
e    |\  Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
Y    |/  
o    |\  Think You're Smart?
u    |/  Can you solve http://members.aol.com/PanicYr00/Sequence.html ?
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-11-09T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p4@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap> <gap-afb5ea0107-p4@usenetarchives.gap>`

```

In article <645smo$1.··.@bgt··t.net>,
RandallBart wrote:
› Vadim Maslov wrote:
› 
…[6 more quoted lines elided]…
› nested statement which shifts coding styles.

I would agree that there is a benefit in readability. I am a big fan
of structured programming and object-oriented programming and I do
believe that they make life of a professional programmer a lot easier.

But I do not think that I missed the mark on benefits, as you say.
My approach, as I said before, advocates the use of universal and
consistent style throughout the program.

I just go a step further and say that one can use automatic tools such
as CobolBeautifier and coding standards compliance checker (to be
given a name) to automatically ensure that selected style is strictly
followed. You just encode your style in a set of code generation
rules that converter/checker program can follow.

And, by the way, the prototype of mf2fsc converter, available at
http://www.siber.com/sct/ automatically adds END-IFs and other good
END-* statements to the Cobol program to make it structured.


Vadim Maslov
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "ed milne." <ua-author-6589438@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p3@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap>`

```


Vadim Maslov wrote in message <346··.@new··t.net>...
› Apparently dots that close sentence were invented when number of
› characters punched on punch cards did matter a lot and a single
› terminating dot seemed like a good solution.


Periods were part of COBOL because the language was designed to emulate the
English language. The idea (don't laugh) was that it would allow ordinary
mortals to write programs.

The addition of the END clauses is an admission that this is a language for
professional programmers only.

Ed Milne
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p6@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap> <gap-afb5ea0107-p6@usenetarchives.gap>`

```

Ed Milne. wrote:
› 
› Vadim Maslov wrote in message <346··.@new··t.net>...
…[12 more quoted lines elided]…
› Ed Milne

I'm sure you're right about that; but a bigger plus, IMHO, is that it
makes Cobol comparable to many (most?) other languages, e.g., Fortran
(which predates Cobol), PL/I, REXX, etc., etc. The PERFORM ..
END-PERFORM is along the same lines, finally gives us poor Cobol folk a
DO loop.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 5)_

- **From:** "han..." <ua-author-8441900@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p7@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap> <gap-afb5ea0107-p6@usenetarchives.gap> <gap-afb5ea0107-p7@usenetarchives.gap>`

```

On Sun, 09 Nov 1997 23:43:37 -0500, Bill Lynch
dreamed up a literary gem, but posted this
instead:

› Ed Milne. wrote:
›› 
…[17 more quoted lines elided]…
› DO loop.

I don't see that making COBOL look like a hundred other languages is a
plus. It's English-like qualities made it more readily understandable
to the beginner, especially back when Computer Science degrees were
not available. How many of us started in that way, without needing a
double first in mathematics to qualify us for the job?

I know many programmers who learned COBOL without the dubious benefits
of specialist education and went on to learn Assembler, and they could
make the systems sing. They didn't need it to look like Fortran ro
whatever, they needed it (and still do) to do a job - a job that it
has been doing rather well over the past thirty-odd years, witness all
the old code that we have to check out for Y2K.

Charles

----------------
Old and past it?
Not any more
----------------
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 6)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p8@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap> <gap-afb5ea0107-p6@usenetarchives.gap> <gap-afb5ea0107-p7@usenetarchives.gap> <gap-afb5ea0107-p8@usenetarchives.gap>`

```

Charles F Hankel wrote:
› 
› On Sun, 09 Nov 1997 23:43:37 -0500, Bill Lynch
…[42 more quoted lines elided]…
› ----------------

All I can say is that I am glad you became a programmer instead of a
physician or an auto mechanic - THEY are required to learn and practice
new things. I believe you are fortunate that you became a programmer,
too, because the industry is full of people who don't really understand
what they are doing, nor why.

Suppose you, or a parent, developed cataracts. You'd see a doctor.
Suppose, further, when discussing cataract surgery with the doctor he
describes immobilizing the patient's head with sand bags for 7-10 days
post-op. You might respond, I thought you used lasers now and there was
no need for the sand bags and immobilization. The doctor replies calmly,
this is the way I was trained 20 years ago and it works just fine. I
don't like these pointless new techniques which require me to change the
way I do things and you're obviously a cretin for bringing it up.

You and Judson must be the best of friends.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 7)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p9@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap> <gap-afb5ea0107-p6@usenetarchives.gap> <gap-afb5ea0107-p7@usenetarchives.gap> <gap-afb5ea0107-p8@usenetarchives.gap> <gap-afb5ea0107-p9@usenetarchives.gap>`

```

Bill Lynch wrote:
› 
› Charles F Hankel wrote:
…[22 more quoted lines elided]…
››› DO loop.

I agree that COBOL was desperately in need of inline loops, code blocks and
constants.

›› I don't see that making COBOL look like a hundred other languages is a
›› plus.  It's English-like qualities made it more readily understandable
›› to the beginner, especially back when Computer Science degrees were
›› not available.  How many of us started in that way, without needing a
›› double first in mathematics to qualify us for the job?

Well, COBOL was designed before some of the advantages of structured design
and block structured languages was known. I think the END-xxx constructs are
about as COBOL-like as they could have been made, and do the job. My only
complaint about the way constants were implemented is that you should be able
to declare a constant before even the file section, to take advantage of them
in record layouts and such. I do not feel that old programs should
necessarily be retro-fitted with END-xxx constructs, unless you can reliably
automate it.

›› I know many programmers who learned COBOL without the dubious benefits
›› of specialist education and went on to learn Assembler, and they could
…[3 more quoted lines elided]…
›› the old code that we have to check out for Y2K.

I agree. These people learned their profession on the job, and learned it
well. No matter what your educational background, you have to learn a lot
(maybe more) on the job to be effective. Actually, it has been more like
forty years.

› All I can say is that I am glad you became a programmer instead of a
› physician or an auto mechanic - THEY are required to learn and practice
› new things. I believe you are fortunate that you became a programmer,
› too, because the industry is full of people who don't really understand
› what they are doing, nor why.

You apparently equate formal education with ability. But education is an
enabler, not a creator. How do you think progress is made in any field? It
wasn't because somebody learned it in school, but because they saw further
than what they had been taught. They learned that in the field.

New things may be good; they may be bad. Nothing is good just because it is
new. Or bad just because it is old. There was a special on powered earth
moving machines recently on The History Channel. The latest powered cranes
made today look and work almost exactly the same way as the very first model.
The designer got it right the first time. No harm in that. No doubt other
designs have been proposed in the while, but were dropped or little used
because they weren't as good.

› Suppose you, or a parent, developed cataracts. You'd see a doctor.
› Suppose, further, when discussing cataract surgery with the doctor he
…[5 more quoted lines elided]…
› way I do things and you're obviously a cretin for bringing it up.

Perhaps you would want a doctor who insisted on using the latest techniques,
even if they were not best for your situation? What if he knew only the
latest techniques, and wasn't aware of an older one which was better in some
cases? What if the latest technique was no better, but cost 10 times as
much? What if he over treats you just to make more money? There is a
serious problem with these issues right now in the medical community.

I can assure you of one thing. If I was a doctor, or an auto mechanic, I
would be the best one that I could be. I studied physics and math in
college, not computers. I can't speak for anyone else, but I have absorbed
the contents of far more books since I left school than I did while in
school; most on computers, programming and electronics. I often write
extensive programs just to learn. I study theory as diligently as practice,
and my office looks like a library. People who come in for the first time
always comment. Of the almost 20 computer languages I have mastered over
some 29 years, only two or three of them were taught formally. The rest I
mastered by reading the book and doing it. Does the fact that I wasn't
sitting in a formal class make that knowledge any less real or less useful?
It certainly works well in practice.

I am happy to adopt any new programming tool which offers me advantage in
doing a better, faster, easier, cheaper job. What I don't do is dance to the
strings of the current 'politically correct' fad of programming, when there
is no advantage. I try new techniques all the time, and always have. And
when I have carefully monitored the value of some practice in actual use over
20 years, I'm quite able to judge for myself how well it works. And when
something new comes along, I spend the time to learn if it works well too.

› You and Judson must be the best of friends.

Sorry, I haven't had the pleasure.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 8)_

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p10@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p3@usenetarchives.gap> <gap-afb5ea0107-p6@usenetarchives.gap> <gap-afb5ea0107-p7@usenetarchives.gap> <gap-afb5ea0107-p8@usenetarchives.gap> <gap-afb5ea0107-p9@usenetarchives.gap> <gap-afb5ea0107-p10@usenetarchives.gap>`

```

In article <01bcf114$eb722ea0$5434b9ce@juddesk>,
"Judson D. McClendon" wrote:
›
› My only complaint about the way constants were implemented is that you
› should be able to declare a constant before even the file section, to
› take advantage of them in record layouts and such.

Most compilers today let you do this. Here's an example using a
compile-time constant in the PICTURE clause, the VALUE clause, and the
PROCEDURE DIVISION.

$ copy sys$input demo.cob
IDENTIFICATION DIVISION.
PROGRAM-ID. DEMO.
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT IN-FILE ASSIGN TO "DEMO.DAT".
REPLACE ==BUFSIZ== BY ==512==.

DATA DIVISION.
FILE SECTION.

FD IN-FILE
ACCESS MODE IS SEQUENTIAL.

01 IN-DAT.
05 IN-REC PIC X(BUFSIZ).

WORKING-STORAGE SECTION.
01 FILLER.
05 WS-BUFSIZ PIC 9(3) VALUE BUFSIZ.
05 WS-REC PIC X(BUFSIZ).

PROCEDURE DIVISION.
0000-MAIN.
DISPLAY "BUFFER SIZE IS " BUFSIZ.
STOP RUN.
^Z
$ cobol demo.cob
$ link demo.obj
$ run demo.exe
BUFFER SIZE IS 512
$


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

##### ↳ ↳ Re: Closing END statements

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap>`

```

Michael C. Kasten wrote:
› 
› You could combine these approaches: use a code-checker to enforce the
…[4 more quoted lines elided]…
› this is an invitation for a shameless advertisement.)

Thanks for the invitation, Michael. ;-) But you are correct that such
programs do depend somewhat on programming style. This is why I don't market
the program. I developed the programming standards which my clients use, so
this is not a problem for them. But if anyone is really interested, e-mail
me and I can supply the criteria the program uses. If changes are needed, I
can probably tailor a version for a reasonable fee. :-) You would need the
source code, because minor modifications to the environment division and so
forth would be needed for different compilers.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

##### ↳ ↳ Re: Closing END statements

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-11-09T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap>`

```

Michael C. Kasten wrote:
› 
› Ken Foskey wrote:
…[24 more quoted lines elided]…
› my eyes at least) less readable. 

WOW. I can't really follow that, IMHO, scope delimiters are a nice
language enhancement. I think it makes the code cleaner looking, easier
to read and I personally don't care how much extra ink it takes to
print!

Steve
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-09T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p13@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap>`

```

steve wolfe wrote:
› 
› Michael C. Kasten wrote:
…[33 more quoted lines elided]…
› Steve

Thank you, Steve!

Bill Lynch
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p13@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap>`

```

steve wolfe wrote:
› 
› Michael C. Kasten wrote:
…[10 more quoted lines elided]…
› print!

This is more of an 'Olde-Tymers'' concern... probably
ecologically-based, don't want to cut down too many greenbar-trees to
make the paper and all. It hearkens back to the old 'maintenance versus
space/efficiency' argument; for the most part anything which improves
readability (and improves ease-of-maintenance) takes up space and/or
decreases program efficiency. Some shops used to string together
imperatives into a single line, like:

IF FLDA = 'Q' MOVE FLDB TO FLDC ELSE MOVE FLDD TO FLDE GO TO THE-END.

in order to cut down on the amount of DASD thbe source would take up.
Old habits die hard.

DD
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p15@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap> <gap-afb5ea0107-p15@usenetarchives.gap>`

```

The Goobers wrote:
› 
› steve wolfe wrote:
…[27 more quoted lines elided]…
› DD

Wow, this is one I haven't seen before - worrying about the size of the
source.

BTW, I was involved in re-engineering (read restructuring) Cobol source
professionally back in 1989 - 1990. The magazine "Software Maintenence"
stated that often what a maint programmer needed most was clean,
reformatted source. They recommended that the programmer's workbench
include a good reformatter. I've never encountered a situation which
suggested this is not true.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p15@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap> <gap-afb5ea0107-p15@usenetarchives.gap>`

```

(posted and mailed)

The Goobers wrote:
› 
› [snip -- quoting in part from a post of mine]
…[12 more quoted lines elided]…
› Old habits die hard.

Your innuendo is baseless and defamatory as well as irrelevant.

Anyone who visits my website can judge whether I promote efficiency at
the expense of readability, or whether I am likely to stuff multiple
statements on a line.

Anyone who reads my original posting -- not just an excerpt quoted
out of context -- will find my argument to be roughly as follows:

The policy suggested by Ken Foskey, concerning the use of END-IF
and its kindred, has costs as well as benefits. It is arguable
whether the benefits outweigh the costs. Where the benefits are
slight, even minor costs may outweigh them.

The best argument for Mr. Foskey's suggestion is that it would reduce
errors caused by the misuse of periods. Since I have seldom suffered
from this kind of error, I wouldn't benefit much from his policy. I
wouldn't presume to make this call for someone else.

What remains is largely a matter of aesthetics and personal taste.
There is little point in debating taste, though there is some virtue
in consistency.

(I *do* use scope delimiters, and I am glad to have them. I just
don't feel compelled to code an END-IF for every single IF.)

If you have a counterargument to offer, let's hear it. If you don't,
you might as well go back to name-calling.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 5)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p17@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap> <gap-afb5ea0107-p15@usenetarchives.gap> <gap-afb5ea0107-p17@usenetarchives.gap>`

```

Michael C. Kasten wrote:
› 
› (posted and mailed)
…[18 more quoted lines elided]…
› Your innuendo is baseless and defamatory as well as irrelevant.

What innuendo?... thought I was rather direct, myself; if the sly remark
about 'greenbar-trees' is annoying then hey, grow some thicker skin. I
cannot see how my remarks were defamatory; I was trying to describe a
context which might be foreign to young'uns who've never had to
calculate blocksizes on one of them newfangled 3380s.

›
› Anyone who visits my website can judge whether I promote efficiency at
› the expense of readability, or whether I am likely to stuff multiple
› statements on a line.

I do not believe that I said you did this, I said that *anything*...
whether you did it or not... which improves readability takes up space
and/or decreases efficiency.

› 
› Anyone who reads my original posting -- not just an excerpt quoted
…[5 more quoted lines elided]…
›    slight, even minor costs may outweigh them.
 
› Anyone who reads what I included in my response will find:
›› Unnecessary scope delimiters (END-IF and their kindred) take time to
›› type, they occupy space on the screen, they consume paper and ink in
›› the listing, and they generally clutter up the code, rendering it (to
›› my eyes at least) less readable.

I do not believe this is out of context nor does it contradict the
assertion you made above.

› 
› The best argument for Mr. Foskey's suggestion is that it would reduce
› errors caused by the misuse of periods.  Since I have seldom suffered
› from this kind of error, I wouldn't benefit much from his policy.  I
› wouldn't presume to make this call for someone else.

How very *generous* of you to allow others to have different
experiences.

› 
› What remains is largely a matter of aesthetics and personal taste.
…[7 more quoted lines elided]…
› you might as well go back to name-calling.

Please tell me what name you or anyone else was called by me... you
poopie-head, you!

DD
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "don eakin" <ua-author-2567354@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p13@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap>`

```

The main purpose for scope delimiters is readability. Any of you folks
that think they take up space and use ink ever had to maintain a
program which had no periods for about 30-40 line with multiple i'fs and
or else's? I think not, if you object to a simple end- statement.
In the past 37 plus years, in my position as an industry specialist, I
have seen more COBOL programs which were like a plate of noodles than an
English language program, and as I said, give me scope terminators over
periods any day of the week.
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p19@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap> <gap-afb5ea0107-p19@usenetarchives.gap>`

```

Double "Hooray" for Don!

Bill Lynch

Don Eakin wrote:
› 
› The main purpose for scope delimiters is readability.  Any of you folks
…[6 more quoted lines elided]…
› periods any day of the week.
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 5)_

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-11-20T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p20@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap> <gap-afb5ea0107-p19@usenetarchives.gap> <gap-afb5ea0107-p20@usenetarchives.gap>`

```

Attention Netscape Communicator users:
I just found a neat command in Collabra under the Message pull-down called
Ignore Thread. Even better, there's a keyboard shortcut: Just press K
(presumably short for Kill) and you go to the next topic, never having to scroll
through all that useless junk nobody cares about anyway.
I just used it on this one!

Bill Lynch wrote:
› 
› Double "Hooray" for Don!
…[12 more quoted lines elided]…
›› periods any day of the week.

***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-19T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p19@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p13@usenetarchives.gap> <gap-afb5ea0107-p19@usenetarchives.gap>`

```

Don Eakin wrote:
›
› The main purpose for scope delimiters is readability.

The 'main' reason for adding the END-xxx scope terminators was to provide
capability which COBOL lacked. Specifically, a 'logical code block'
capability. I don't disagree with your other points, but being able to write
logical blocks of code embedded within IF and other statements is extremely
important for code structuring. Otherwise, you are stuck with splitting them
logical code blocks into separate paragraphs, using GO TO, and/or using
repetitive or convoluted IF logic. This is much more wide ranging and
significant than elimination of some ELSEs and periods, as nice as that may
be. Perhaps you were thinking of this as well?

In my opinion, COBOL 85 added the three most desperately needed capabilities
which COBOL lacked: logical code blocks, inline loops and constants.

Don, you must have started in computers around 1960, one of the few folks who
have been around longer than my 29+ years. :-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

##### ↳ ↳ Re: Closing END statements

- **From:** "loren g. foster, cdp" <ua-author-6588883@usenetarchives.gap>
- **Date:** 1997-11-09T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap>`

```


Michael C. Kasten wrote in message <346··.@swb··l.net>...
›
› Period abuse has never been much of a problem for me. I am reluctant
› to adopt a significantly different style to solve a non-problem,
› especially when that style comes at a significant cost.

That is wonderful, but for the rest of us that day in and day out have to
maintain code that the style is neo-old, it is a problem..

› Unnecessary scope delimiters (END-IF and their kindred) take time to
› type, they occupy space on the screen, they consume paper and ink in
…[5 more quoted lines elided]…
››› SNIP<<<<

Scope delimiters are not unnecessary. They add readability and clean up the
logic. I can only assume that GO TO is still in your bag of tricks.
Besides, have you never used COPY?? You will spend much more on paper
printing out abends due to errors introduced due to the lack of delimiters
and you will printing out a compile listing (for those that still do).
```

##### ↳ ↳ Re: Closing END statements

- **From:** "patrick finnegan" <ua-author-1889869@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap>`

```

You can ignore most of the previous advice. The best way to eliminate
periods is to code exit paragraph statements placing the period just
before the exit paragraph name. See example below. Anyone maintaining
the program knows immediately that that they only have to code one
period after the paragraph name(1000-initialize) and one period before
the paragraph exit(1000-exit).

I have major problems trying to explain to my novice programmers why
they can code periods after single level MOVE statements but not within
a multilevel IF, END-IF, or PERFORM,END-PERFORM. The paragraph EXIT
approach eliminates confusion and encourages the use of scope
terminators which tend to enforce structured code. It also fits in
neatly with the idea of scope terminators in that the EXIT denotes the
end of the paragraph while the paragraph name marks the beginning. This
makes the code more readable to the novice or the unfortunate who has to
maintain the code.

1000-INITIALIZE.
****************************************************************
* FUNCTION : INITIALIZE DATA AREA. *
* *
* PERFORMS : NONE *
* *
* PERFORMED BY : 0000-CONTROL *
****************************************************************

D DISPLAY '** 1000-INITIALIZE **'

INITIALIZE WFZ51CD-RETURN-DATA

W010-GENERAL-ITEMS

SQL-INIT-FLAG

SET WFZ51CD-OK TO TRUE

.
1000-EXIT.
EXIT.
EJECT




full stop gfull stops is to code oi



› 
› Ken Foskey wrote:
…[14 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p24@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p24@usenetarchives.gap>`

```

Patrick Finnegan wrote:
› 
› You can ignore most of the previous advice.  The best way to eliminate
…[5 more quoted lines elided]…
› 

[sample code snipped]

If you're looking for the best way to eliminate periods, this technique
will certainly come close. You can eliminate two more periods by
eliminating the EXIT paragraph.

It is not clear to me, however, whether this approach will reduce
errors or merely trade one kind of error for another.

Suppose I see the following code at the end of a long paragraph:

...
ELSE
PERFORM 3333-FOO
ELSE
PERFORM 4444-BAR
ELSE
ADD +1 TO FOOBAR-COUNT.

PERFORM 6000-REPORT-TOTALS.

In the absence of GO TO, I absolutely know that every time I execute
this paragraph, I will PERFORM 6000-REPORT-TOTALS.

Now consider an alternative version:

...
ELSE
PERFORM 3333-FOO
END-IF
ELSE
PERFORM 4444-BAR
END-IF
ELSE
ADD +1 TO FOOBAR-COUNT
END-IF
PERFORM 6000-REPORT-TOTALS
.

Do I always PERFORM 6000-REPORT-TOTALS, or not? Well, er, um,
probably -- if I can believe my indentation, and if I didn't
accidentally leave out an END-IF somewhere in some preceding code,
forty or fifty lines away. Until I carefully examine the entire
paragraph, I can't be sure.

I would rather terminate a complex sentence with a period, and know
that it's terminated, than forever be anxiously counting my END-IFs.
It is true that periods are subject to abuse. However, scope
delimiters like END-IF are not immune to abuse.

A lot depends on what you're used to. If I ever get around to playing
with my free Fujitsu compiler, I'm going to try out the period-free
style and see how I like it.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p25@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p24@usenetarchives.gap> <gap-afb5ea0107-p25@usenetarchives.gap>`

```

In article <346··.@swb··l.net> mc··.@swb··l.net "Michael C. Kasten" writes:
› I would rather terminate a complex sentence with a period, and know 
› that it's terminated, than forever be anxiously counting my END-IFs.
› It is true that periods are subject to abuse.  However, scope 
› delimiters like END-IF are not immune to abuse.

If you want to terminate a sentence, perhaps to end a paragraph or
to assert that all the conditionals have been closed by END-s, you
can try using the Continue statement like this:
PERFORM ab-item
END-IF
END-WHILE
END-IF
CONTINUE.
PERFORM ab-summary
CONTINUE.
next-para.

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 5)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-12T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p26@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p24@usenetarchives.gap> <gap-afb5ea0107-p25@usenetarchives.gap> <gap-afb5ea0107-p26@usenetarchives.gap>`

```

Richard Ross-Langley wrote:
› 
› In article <346··.@swb··l.net> mc··.@swb··l.net "Michael C. Kasten" writes:
…[16 more quoted lines elided]…
› 

Why bother with the "continue"? Just code the period (full-stop) - on
its own line, if you like.

Bill Lynch

› --
› Richard Ross-Langley        +44 1727 852 801
› Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
› * Independent Computer Consultancy    Established in 1977 *
```

###### ↳ ↳ ↳ Re: Closing END statements

_(reply depth: 4)_

- **From:** "han..." <ua-author-8441900@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p25@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p24@usenetarchives.gap> <gap-afb5ea0107-p25@usenetarchives.gap>`

```

All of this hostility towards a natural language element puzzles me.
When you write your native language in roman characters, you use a
full stop (or period or whatever you want to call it) at the end of
the sentence.

An IF statement, for instance, is not a complete sentence in itself,
is it? It's always followed by some imperative or other. So, why do
you have a problem with it in COBOL?

Personally, I have not seen a paper listing in years. I use a screen
exclusively either on a PC or a good old 327x. Some places that I
have worked use only 24x80 screens and that leaves only about 18 lines
for code.

I personally prefer to see as much meaningful code as possible and
find that the lines taken up with the various "END-" simply get in the
way of seeing the real code.

As to the use of END-EXEC in CICS calls and the like, that is not
COBOL, merely a precompiler delimiter.

Charles

----------------
Old and past it?
Not any more
----------------
```

##### ↳ ↳ Re: Closing END statements

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-11-15T19:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p2@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap>`

```

In article <01bcf21c$6d9ad140$4534b9ce@juddesk>,
"Judson D. McClendon" wrote:
›
› Well, REPLACE is actually a COBOL 85, Level II compiler source
› directive, rather than language syntax.

COPY and REPLACE appear under the rubric of source text manipulation
because they can appear in any SECTION. However, they are indeed CoBOL
statements, not compiler source directives (such as LIST and NOLIST,
which are implementation-defined and do not appear in the standard).

I find it most useful to view compile-time constants as existing in the
"environment" of the program, so I generally use a comment to create a
"CONSTANT SECTION" in the ENVIRONMENT DIVISION, like this:

IDENTIFICATION DIVISION.
PROGRAM-ID. DEMO.
ENVIRONMENT DIVISION.
*CONSTANT SECTION.
REPLACE
==SEND-MAX== BY ==1024==
==RECV-MAX== BY ==1024==
==RECV-TIMEOUT== BY ==0015==
==ALLOC-RETRIES== BY ==0010==
==DEVNAM-MAX== BY ==0255==
==STX== BY ==X'02'==
==ETX== BY ==X'03'==
.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT IN-FILE ASSIGN TO "DEMO.DAT".
DATA DIVISION.
FILE SECTION.

[etc.]


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-16T19:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p29@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p2@usenetarchives.gap> <gap-afb5ea0107-p29@usenetarchives.gap>`

```

Chris Westbury wrote:
› 
› Judson D. McClendon"  wrote:
…[7 more quoted lines elided]…
› which are implementation-defined and do not appear in the standard).

REPLACE and COPY are text manipulation operators because they manipulate the
source text. COBOL statements are PART of the program logic; source
manipulation commands work ON the program source itself. The fact that you
can use one or the other to accomplish a given thing doesn't change that. IF
you use:

REPLACE ==MOVE 1== BY ==XXXX==.

the compiler will happily replace all occurrences of 'MOVE 1' by XXXX. This
is decidedly NOT the operation of a constant declaration or any COBOL
statement! This is the operation of a compiler text processor command.

I don't question that you can use it in place of a constant declaration, but
it is not the same thing.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: Closing END statements

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p31@usenetarchives.gap>`
- **In-Reply-To:** `<3465d71a.1387021@news.tig.com.au>`
- **References:** `<3465d71a.1387021@news.tig.com.au>`

```

Ken Foskey wrote:
› 
› I am writing a style guide and I thought I would throw this open for
…[5 more quoted lines elided]…
› 
Not true with IBM's Cobol II, READ has an END-READ, DIVIDE has an
END-DIVIDE, etc. (I can't remember using an "END-WRITE", but I suspect
it exists).

BTW, I think your idea is a good one, esp. the END-IF. I do not think
there's a practical issue of how long it will take to code the
"END-..."s. Is someone going to argue that we should bill/sue IBM for
forcing us to code all the "END-EXEC"s?

Bill Lynch

(rest snipped)
```

##### ↳ ↳ Re: Closing END statements

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1997-11-09T19:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p31@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p31@usenetarchives.gap>`

```

Bill Lynch wrote:
› [snip] (I can't remember using an "END-WRITE", but I suspect
› it exists).

Sure it does. When you use the INVALID KEY phrase you have just
transformed the simple WRITE statement, an imperative statement, into a
conditional statement. There exists and END-* for each conditional
statement.

As I recall, there are about 19 END-* reserved words (not counting
END-OF-PAGE, which is not related to the current subject).

Best regards,
Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

##### ↳ ↳ Re: Closing END statements

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p31@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p31@usenetarchives.gap>`

```

On Sun, 09 Nov 1997 20:31:16 -0500, Bill Lynch
wrote:

› Not true with IBM's Cobol II, READ has an END-READ, DIVIDE has an
› END-DIVIDE, etc. (I can't remember using an "END-WRITE", but I suspect
› it exists).
›

Bill

You are 100% correct. My intention was that the end-read is not
required just good practice. I will work on the phrasing to correct
this.

I believe in standards that are useful most reads are simply that
reads. If you apply logic past the 'at end' set a flag then I would
recommend the use of it.

Wonder how many of us have picked up the COBOL manual and scanned it
to grow our understanding of the language for the latest release. I
started on COBOL I and change jobs to COBOL II and now on the latest
IBM COBOL with intrinsic functions. I looked up the manual and sent
out some teasers to all our programmers. I hope it had some effect.

Ken
```

#### ↳ Re: Closing END statements

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-08T19:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p34@usenetarchives.gap>`
- **In-Reply-To:** `<3465d71a.1387021@news.tig.com.au>`
- **References:** `<3465d71a.1387021@news.tig.com.au>`

```

In general, the method you suggest won't catch missing periods, which are
just as important. It's not too difficult to write a program to scan COBOL
source and flag missing or extra periods, along with incorrect indentation.
Once you have the program, it takes far, far less time to scan the source
file than it does to type those hundreds of END-IFs required for large
programs. And the program won't miss a single one. You can also take the
opportunity in the program to look for other 'easy to miss' errors which a
compiler won't catch. I wrote such a program for my own use many years ago,
and it has been an enormous boon. It works so well that all my clients have
purchased it for their own use, even though I don't market it. Perhaps you
could provide a listing of such a program in your book.

If COBOL were being created new today, I might agree with your suggestion.
But developing habits of coding consistently is very important in avoiding
coding errors and code reading errors. Changing a programming standard like
this should only be done when there is clear and significant benefit;
otherwise it is not worth dealing with the inconsistency between new and old
code in a maintenance environment. The idea is to develop programming
standards which are not only more reliable and maintainable, but that are
more time efficient as well.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

Ken Foskey  wrote:
> I am writing a style guide and I thought I would throw this open for
> comment to the news group.
…[10 more quoted lines elided]…
> period, in part due to the physical size of the period.
```

##### ↳ ↳ Re: Closing END statements

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p34@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p34@usenetarchives.gap>`

```

On 9 Nov 1997 18:25:21 GMT, "Judson D. McClendon"
wrote:

› In general, the method you suggest won't catch missing periods, which are
› just as important. It's not too difficult to write a program to scan COBOL
› source and flag missing or extra periods, along with incorrect indentation.
If it does not affect the logic flow I don't care.... I am looking
for a bug killer (aren't we all).

› Once you have the program, it takes far, far less time to scan the source
› file than it does to type those hundreds of END-IFs required for large
› programs. And the program won't miss a single one.
There is no intention to apply this to the entire (existing) program
that does not conform. If the program is not maintained then don't
touch it. If the program is being maintained then look at the area
you are changing and tidy that up, amazing what efficiencies can be
found this way.

›  You can also take the
› opportunity in the program to look for other 'easy to miss' errors which a
…[3 more quoted lines elided]…
› could provide a listing of such a program in your book.
I would love to use a code checker but we have a review process for
the logic anyway. People will check the cobol standards and pick it
up. In a maintenance role where a large program does not conform
then it will just become a task without additional value.

› 
› If COBOL were being created new today, I might agree with your suggestion. 
…[4 more quoted lines elided]…
› code in a maintenance environment. 
If I could add the END-IFs automatically to the legacy code I would.
Maybe if I just ....... To hard... It is easier and more beneficial
to change it by hand anyway, thinking about the order of evaluation.

One program I changed had fall through logic that went through a chain
of 20 IF's when 90% of the records coming in fell through. Changing
this and some other the logic changed the CPU count dramatically.

› The idea is to develop programming
› standards which are not only more reliable and maintainable, but that
› are more time efficient as well.

The time efficiency comes from not debugging stupid errors that I have
no doubt we have all made. That period placed where we did not want
it cost us 10 hours to debug instead of 3 minutes in a compile cycle.

That interesting statistic of walkthrough after clean compile 0.78
units(probably hours) per bug. Finding it in a debug cycle is 10
units.

For machine time efficiency there is a separate guide that I have
written for MVS. It covers the simple tricks for IBM MVS cobol. 99
times out of 100 people time is what is important for the maintenance
programmer. Besides it is surprising how efficient clean readable
code is, a bit of thought goes a long way. This could be a separate
thread all of it's own and has been.

PS: Does anyone know whether MVS cobol INSPECT is a very CPU hunger
command or not?

› -- 
› Judson McClendon          This is a faithful saying and worthy of all
…[18 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Closing END statements

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afb5ea0107-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afb5ea0107-p35@usenetarchives.gap>`
- **References:** `<3465d71a.1387021@news.tig.com.au> <gap-afb5ea0107-p34@usenetarchives.gap> <gap-afb5ea0107-p35@usenetarchives.gap>`

```

Ken Foskey wrote:
›
› [snippage]
› PS: Does anyone know whether MVS cobol INSPECT is a very CPU hunger
› command or not?
›

Depends on what is trying to 'digest' it... using IKFCBL00 both the
INSPECT and the STRING are major-league CPU-hogs, under IGYCRCTL they
aren't. Try slapping together a simple skeleton program and compile
using PMAP and LIST, respectively... you'll be amazed.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
