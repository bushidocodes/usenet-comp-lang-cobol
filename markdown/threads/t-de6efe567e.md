[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Book Puzzlement

_13 messages · 9 participants · 1998-04_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### COBOL Book Puzzlement

- **From:** "cr..." <ua-author-11176@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<353ef9f8.155540123@news.mindspring.com>`

```


Been studying COBOL from the TY COBOL in 21 Days (much better than
the Dummies book, and the "Revolutionary" COBOL book had a corrupt
compiler file). I like COBOL as compared to C and VB; the language is
so much easier than C that it lets you concentrate on the puzzle-logic
part, which is what I like about programming, and it lets you see the
entire program easier than VB.
Now dig this passage from that book, though:

Here's the code:

Listing 5.8 from page 111:

003800 PERFORM CALCULATE-AND-DISPLAY
003900 UNTIL THE-MULTIPLIER > 12.
004000
004100 CALCULATE-AND-DISPLAY.
004200 ADD 1 TO THE-MULTIPLIER.
004300 COMPUTE THE-PRODUCT = THE-NUMBER* THE-MULTIPLIER.
004400 DISPLAY
004500 THE-NUMBER " * " THE-MULTIPLIER " = "

004600 THE-PRODUCT.

(line 46 added to beat newsreader wraparound)

Here's an explanation of the code (from the book) that I do not
understand:

" If you follow the path of the logic in listing 5.8, starting at
the top of CALCULATE-AND-DISPLAY when THE-MULTIPLIER equals 11, you'll
notice an error in the logic (a bug). The paragraph adds 1 to
THE-MULTIPLIER, making it 12, and displays the results for 12. The
program then returns to line 003900, falls through to line 004000,
where it jumps back to line 003800, and checks the condition again."

My comments: now the immediately previous sentence is what I don't
understand; the book does say, quite understandably, that in a PERFORM
UNTIL sentence, the condition is tested before the PERFORM is
executed; however, when THE-MULTIPLIER equals 12, and the program
returns to line 003900 (to check the condition), since the condtion is
false ( 12 is NOT >12), shouldn't the program then immediately
PERFORM the CALCULATE-AND-DISPLAY paragraph? Instead the book says it
"falls through the line 00400 where it jumps back to line 003800, and
checks the condition again."

Now, suppose there were some extraneous sentence there on line 004000
(a DISPLAY sentence, perhaps). You would then execute whatever is on
that line, and, logically, also excute whatever sentences you would
care to place between line 004000 and the beginning of the
CALCULATE-AND-DISPLAY paragraph before actually executing the
CALCULATE-AND-DISPLAY paragraph.

This doesn't make sense to me. After the condition of THE-MULTIPLIER
is evaluated, it would seem that the CALCULATE-AND-DISPLAY paragraph
would be executed, instead of falling through to line 004000, jumping
back to line 003800, and then checking the condition again!. Seems
strange to me! I don't actually have a compiler on line yet, but if I
did, it would seem that I could verify the book's proposed sequence of
events by inserting some test sentence, say a DISPLAY sentence, on
line 40, and see if that executed or not.

To continue on with the book:

"THE-MULTIPLIER equals 12 (so it is not greater than 12), however, and
the paragraph CALCULATE-AND-DISPLAY is performed one more time. The
first action in CALCULATE-AND-DISPLAY is to add 1 to THE-MULTIPLIER,
so the results will be displayed when THE-MULTIPLIER equals 13."

Comment: this is a "bug" because the program was supposed to display
results only up to 12. Very reasonably, they suggest moving the "ADD
ONE TO THE-MULTIPLIER" sentence to the end of the
CALCULATE-AND-DISPLAY paragraph. That is fine.

Can anyone explain that bit about the double check and the
falling-through?
Thanks, prof.
Randy
Cryonics: Gateway to the Future?
http://www.mindspring.com/cryon/
*********************************
```

#### ↳ Re: COBOL Book Puzzlement

- **From:** "cr..." <ua-author-11176@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<353ef9f8.155540123@news.mindspring.com>`
- **References:** `<353ef9f8.155540123@news.mindspring.com>`

```

On Wed, 22 Apr 1998 11:19:37 -0400, "Richard S. MacKnight"
wrote:

› 
› Randy Smith wrote in message <353··.@new··g.com>...
…[47 more quoted lines elided]…
› been satisfied.

Sorry if I seem overly pedantic or anal here, but are you confirming
my suspicion that the book is incorrect when they state that,
"The paragraph adds 1 to THE-MULTIPLIER, making it 12, and displays
the results for 12. The program then returns to line 003900, falls
through to line 004000, where it jumps back to line 003800, and checks
the condition again"?

To be more precise, when you say "AFTER the PERFORM-UNTIL logic has
been sataisfied," do you actually mean to say that line 004000 will
not be seen by the compiler until after the CALCULATE-AND-DISPLAY
paragraph has been performed X number of times (be that number 12 or
13 or whatever)?

›› Now, suppose there were some extraneous sentence there on line 004000
›› (a DISPLAY sentence, perhaps). You would then execute whatever is on
…[30 more quoted lines elided]…
› etc..

Yes, of course, but then that part of the "bug," or indeed, the "bug"
itself, as described in the book, is and was not my concern. I am
concerned only with the book's description of the program flow as i
pointed out in my reply to you above. I only wrote the rest of the
book's explanation for continuity purposes.

Thank you.

› 
›› 
…[7 more quoted lines elided]…
› 

Randy
Cryonics: Gateway to the Future?
http://www.mindspring.com/cryon/
*********************************
```

##### ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "richard s. macknight" <ua-author-17074119@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p2@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p2@usenetarchives.gap>`

```

› Sorry if I seem overly pedantic or anal here, but are you confirming
› my suspicion that the book is incorrect when they state that,
…[10 more quoted lines elided]…
› 
Lines 3800 and 3900 can be combiled to read.
3800 PERFORM CALULATE-AND-DISPLAY UNTIL THE-MULTIPLIER > 12.

This means that line 3800 will call the named subroutine until the
conditional statement has been satisfied. Program execution will NOT go
past this line (or line 3900 in your example) until THE-MULTIPLIER is > 12.
If you put a STOP RUN statement on line 4000, the program would halt after
the PERFORM condition has been completed.

Consider this:

3799 100-BEGIN-LOOP.
3800 PERFORM CALCULATE-AND DISPLAY.
3900 IF THE-MULTIPLIER > 12
3901 GO 100-END-LOOP
3902 ELSE
3903 GO 100-BEGIN-LOOP
3904 END-IF.
3905 100-END-LOOP.
4000 program continues....

It may help to see it this way.
```

#### ↳ Re: COBOL Book Puzzlement

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<353ef9f8.155540123@news.mindspring.com>`
- **References:** `<353ef9f8.155540123@news.mindspring.com>`

```

Randy Smith wrote in article
<353··.@new··g.com>...
› 
› Listing 5.8 from page 111:
…[20 more quoted lines elided]…
› where it jumps back to line 003800, and checks the condition again." 

Huh!? As it stands, the example would reenter line 4100, which is
probably an unwanted fall-through, but there's no way it can get to 3800.

› Comment: this is a "bug" because the program was supposed to display
› results only up to 12. Very reasonably, they suggest moving the "ADD
› ONE TO THE-MULTIPLIER" sentence to the end of the
› CALCULATE-AND-DISPLAY paragraph. That is fine.

I don't think that addresses the problem.
You're still going to get one extra result beyond what you were
probably hoping for. The only difference is a different starting point.

In the following three examples, I have changed your 12 to 4, for
brevity. THE-MULTIPLIER is intialized at 0.

NEXT+ ...1....*....2....*....3....*....4....*....5....*....6....*....7..
002200 PROCEDURE DIVISION.
002300 MAINLINE.
002400 MOVE 22 TO THE-NUMBER.
002500 PERFORM CALCULATE-AND-DISPLAY
002600 UNTIL THE-MULTIPLIER > 4.
002650 DISPLAY "OWARI".
002700 STOP RUN.
002800 CALCULATE-AND-DISPLAY.
002828 ADD 1 TO THE-MULTIPLIER.
003000 COMPUTE THE-PRODUCT = THE-NUMBER * THE-MULTIPLIER.
003100 DISPLAY THE-NUMBER " * " THE-MULTIPLIER
003200 " = " THE-PRODUCT.
E
#RUNNING 0851
#0851 DISPLAY:0000022 * 001 = 0000022.
#0851 DISPLAY:0000022 * 002 = 0000044.
#0851 DISPLAY:0000022 * 003 = 0000066.
#0851 DISPLAY:0000022 * 004 = 0000088.
#0851 DISPLAY:0000022 * 005 = 0000110.
#0851 DISPLAY:OWARI.
#ET=0.7 PT=0.1 IO=0.1

NEXT+ ...1....*....2....*....3....*....4....*....5....*....6....*....7..
002200 PROCEDURE DIVISION.
002300 MAINLINE.
002400 MOVE 22 TO THE-NUMBER.
002500 PERFORM CALCULATE-AND-DISPLAY
002600 UNTIL THE-MULTIPLIER > 4.
002650 DISPLAY "OWARI".
002700 STOP RUN.
002800 CALCULATE-AND-DISPLAY.
003000 COMPUTE THE-PRODUCT = THE-NUMBER * THE-MULTIPLIER.
003100 DISPLAY THE-NUMBER " * " THE-MULTIPLIER
003200 " = " THE-PRODUCT.
003233 ADD 1 TO THE-MULTIPLIER.
E
#RUNNING 0849
#0849 DISPLAY:0000022 * 000 = 0000000.
#0849 DISPLAY:0000022 * 001 = 0000022.
#0849 DISPLAY:0000022 * 002 = 0000044.
#0849 DISPLAY:0000022 * 003 = 0000066.
#0849 DISPLAY:0000022 * 004 = 0000088.
#0849 DISPLAY:OWARI.
#ET=0.5 PT=0.1 IO=0.0

Note that it would be much simpler to understand if you abandoned
the use of Communist code like "perform until" and stuck with good
old American "go to."

NEXT+ ...1....*....2....*....3....*....4....*....5....*....6....*....7..
002200 PROCEDURE DIVISION.
002300 MAINLINE.
002400 MOVE 22 TO THE-NUMBER.
002800 CALCULATE-AND-DISPLAY.
002828 ADD 1 TO THE-MULTIPLIER.
003000 COMPUTE THE-PRODUCT = THE-NUMBER * THE-MULTIPLIER.
003100 DISPLAY THE-NUMBER " * " THE-MULTIPLIER
003200 " = " THE-PRODUCT.
003300 IF THE-MULTIPLIER < 4
003400 GO TO CALCULATE-AND-DISPLAY
003500 .
003600 DISPLAY "OWARI".
003700 STOP RUN.
E
#RUNNING 0853
#0853 DISPLAY:0000022 * 001 = 0000022.
#0853 DISPLAY:0000022 * 002 = 0000044.
#0853 DISPLAY:0000022 * 003 = 0000066.
#0853 DISPLAY:0000022 * 004 = 0000088.
#0853 DISPLAY:OWARI.
#ET=0.5 PT=0.1 IO=0.1

If you insist on using inferior structures, you could also say
PERFORM CALCULATE-AND-DISPLAY UNTIL THE-MULTIPLIER = 4.



Ross

http://www.geocities.com/Hollywood/Set/7185/
```

##### ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "cr..." <ua-author-11176@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p4@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p4@usenetarchives.gap>`

```

On 22 Apr 1998 16:57:02 GMT, "Ross Klatte" wrote:

› Randy Smith  wrote in article
› <353··.@new··g.com>...
…[26 more quoted lines elided]…
› 

Thank you for your detailed correction of the bug (in your subsequent
paragraphs), and yes, I agree that is quite simply a prototypical
off-by-one type of problem easily fixed in a variety of ways.
My real concern is not with the "bug," but instead with their
description of the program flow, to wit:

››  " If you follow the path of the logic  in listing 5.8, starting at
›› the top of CALCULATE-AND-DISPLAY when THE-MULTIPLIER equals 11, you'll
…[3 more quoted lines elided]…
›› where it jumps back to line 003800, and checks the condition again." 

Would you say that this description (the immediately preceding
paragraph) of the program flow is incorrect? This was from the book.

›› Comment: this is a "bug" because the program was supposed to display
›› results only up to 12. Very reasonably, they suggest moving the "ADD
…[31 more quoted lines elided]…
› #ET=0.7 PT=0.1 IO=0.1

Rgarding the immediately preceding paragraph:

The fact that "OWARI" is displayed where it is proves that the program
flow as detailed by the book ("The program then returns to line
003900, falls through to line 004000, where it jumps back to line
003800, and checks the condition again." ) is indeed incorrect, if
indeed this is an actual output from an actual COBOL program.

However, on the other issue (certainly a peripheral one, as far as I
am concerned) regarding the off by one problem, I'll quote part of my
original post:

›› Comment: this is a "bug" because the program was supposed to display
›› results only up to 12. Very reasonably, they suggest moving the "ADD
›› ONE TO THE-MULTIPLIER" sentence to the end of the
›› CALCULATE-AND-DISPLAY paragraph. That is fine.
› 

In your fix, you did not move the ADD ONE TO THE-MULTIPLIER sentence
to the end of the CALCULATE-AND-DISPLAY paragraph. That is why the
fix did not work.
Thank you for responding to my query.




› NEXT+ ...1....*....2....*....3....*....4....*....5....*....6....*....7..
› 002200 PROCEDURE DIVISION.                                              
…[19 more quoted lines elided]…
› #ET=0.5 PT=0.1 IO=0.0                                                   
 
› Yes, this is correct.
 
 
› 
› Note that it would be much simpler to understand if you abandoned 
…[27 more quoted lines elided]…
› PERFORM CALCULATE-AND-DISPLAY UNTIL THE-MULTIPLIER  =  4.                  


Yes, there is still much for me to learn about COBOL. I think this
technique is on the next page. :-)


Randy
Cryonics: Gateway to the Future?
http://www.mindspring.com/cryon/
*********************************
```

##### ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-23T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p4@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p4@usenetarchives.gap>`

```

Ross Klatte wrote:

› E
› #RUNNING 0851
…[8 more quoted lines elided]…
› NEXT+ ...1....*....2....*....3....*....4....*....5....*....6....*....7..

Wow, it's CANDE!

I  |\   Randall Bart, Old Burroughs Guy
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \      Todd McCormick released after 12 day illegal incarceration
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/     http://www.marijuanamagazine.com/toc/articles/toddfree.htm
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "hank" <ua-author-88501@usenetarchives.gap>
- **Date:** 1998-04-26T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p6@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p4@usenetarchives.gap> <gap-de6efe567e-p6@usenetarchives.gap>`

```

andallBart wrote in article
<6hrul5$9.··.@bgt··t.net>...
› Ross Klatte wrote:
›  
…[13 more quoted lines elided]…
› Wow, it's CANDE!

Throw it in some WFL and see if it coughs up anything.
```

#### ↳ Re: COBOL Book Puzzlement

- **From:** "j.a...." <ua-author-17075620@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p8@usenetarchives.gap>`
- **In-Reply-To:** `<353ef9f8.155540123@news.mindspring.com>`
- **References:** `<353ef9f8.155540123@news.mindspring.com>`

```

In article <353··.@new··g.com>, cr··.@min··g.com says...
› 
› 
…[31 more quoted lines elided]…
› THE-MULTIPLIER, making it 12, and displays the results for 12. The
 
› Read 13 instead of 12 in the lines before this one and then it is OK
 
› program then returns to line 003900, falls through to line 004000,
› where it jumps back to line 003800, and checks the condition again." 
…[45 more quoted lines elided]…
› *********************************

When the perform is execute yhe last time, finishing whit THE-MULTIPLIER = 13
the condition is false, the program will continue with line 004000. This might be
a bug. However the final result will be that a calculation with THE-MULTIPLIER = 14
will be carried out.

Regards,

Johan
```

#### ↳ Re: COBOL Book Puzzlement

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p9@usenetarchives.gap>`
- **In-Reply-To:** `<353ef9f8.155540123@news.mindspring.com>`
- **References:** `<353ef9f8.155540123@news.mindspring.com>`

```

Randy Smith wrote:
›
› Been studying COBOL from the TY COBOL in 21 Days (much better than
› the Dummies book, and the "Revolutionary" COBOL book had a corrupt
› compiler file).

[snippage of that which has been addressed]

My compliments and congratulations, Mr/Ms Smith; *that* is how a
homework question should be researched, addressed and posted. I'll not
try to repeat the answers you've received... was it straightened out to
your satisfaction? In short, it relies on fall-through logic; a PERFORM
transfers execution of the program to the first imperative statement
following the specified section/paragraph label until another label is
met and the condition(s) associated with the PERFORM is/are satisfied
(unless TEST BEFORE is specified... but more on that another time).
Execution is then resumed with the next imperative statement which
follows the PERFORM... in this case this next statement was in the range
covered by the PERFORM so the code was repeated.

DD
```

##### ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "cr..." <ua-author-11176@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p9@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p9@usenetarchives.gap>`

```

On Thu, 23 Apr 1998 06:43:59 -0400, The Goobers
wrote:

› Randy Smith wrote:
›› 
…[18 more quoted lines elided]…
› DD

I can assure you, Mr/Mrs DD, that *that* was not a homework question.
It is true that I am studying COBOL, but as a self-study project only;
there are no COBOL classes in Houston. I hand out the assignments,
and I complete them to my own satisfaction.

Yes, I am satisfied that the book's explanation of the program flow is
incorrect. Your reply seems to confirm this somewhat.
Thank you for your reply.
Randy
Cryonics: Gateway to the Future?
http://www.mindspring.com/cryon/
*********************************
```

###### ↳ ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p10@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p9@usenetarchives.gap> <gap-de6efe567e-p10@usenetarchives.gap>`

```

In article <354··.@new··g.com>,
Randy Smith wrote:
› On Thu, 23 Apr 1998 06:43:59 -0400, The Goobers 
› wrote:
…[26 more quoted lines elided]…
› and I complete them to my own satisfaction. 
 
› What, then... are you saying that you are not assigning yourself homework?
 
› 
› Yes, I am satisfied that the book's explanation of the program flow is
› incorrect. Your reply seems to confirm this somewhat.

Truth be known I didn't read the book's commentary; I checked the code and
saw a problem which has bedeviled many a neophyte so I gave a Standard
Answer... nothing special, nothing hectic, it was free so it was worth at
least *double* what you paid for it.

DD
```

#### ↳ Re: COBOL Book Puzzlement

- **From:** "cr..." <ua-author-11176@usenetarchives.gap>
- **Date:** 1998-04-27T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p12@usenetarchives.gap>`
- **In-Reply-To:** `<353ef9f8.155540123@news.mindspring.com>`
- **References:** `<353ef9f8.155540123@news.mindspring.com>`

```

On Wed, 22 Apr 1998 15:15:59 GMT, cr··.@min··g.com (Randy Smith)
wrote:
I thank everyone for his/her replies.

I do, however, feel that I have to repeat myself here in that my
reason for posting was not because I didn't understand the control
structure or the typical "off-by-one" bug shown here, but because of
the book's incorrect explanation of the program flow (which I posted
in quotes).

Perhaps most did not fully read the post, and jumped on the off-by-one
bug and/or the control loop structure as the reason for my posting.
Curious...

Well, thanks anyway. I got my DOS MF COBOL compiler in the mail and
installed it and verified that the book's explanation of the program
flow is wrong.

Randy
Cryonics: Gateway to the Future?
http://www.mindspring.com/cryon/
*********************************
```

##### ↳ ↳ Re: COBOL Book Puzzlement

- **From:** "material fellow" <ua-author-501273@usenetarchives.gap>
- **Date:** 1998-04-28T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de6efe567e-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de6efe567e-p12@usenetarchives.gap>`
- **References:** `<353ef9f8.155540123@news.mindspring.com> <gap-de6efe567e-p12@usenetarchives.gap>`

```

Randy Smith wrote:
› 
› On Wed, 22 Apr 1998 15:15:59 GMT, cr··.@min··g.com (Randy Smith)
…[11 more quoted lines elided]…
› Curious...

Not curious at all.

In technical people, including scientific people, there is much value
placed on telling the other person that he/she is wrong, that the idea
won't work, that the data are wrong..............

In fact, in some newsgroups, what you find are those who delight in
skimming something for anything that seems wrong.

Then, like your hated elementary teacher, they circle it in red and
throw it back at you with a pithy comment.

E-mail with HTML allowing for colored text will allow this tendency to
be more visible.

Negativism...... technical types believe it can be the route to
knowledge and understanding.


I use stealth Java in my sig file.
It's there, but no one can detect it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
