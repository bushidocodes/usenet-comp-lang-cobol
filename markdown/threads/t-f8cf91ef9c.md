[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Procedure name not unique--huh?

_34 messages · 20 participants · 1998-02 → 1998-03_

---

### Procedure name not unique--huh?

- **From:** "timo suave" <ua-author-9101468@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34E5E4A0.985715BB@concentric.net>`

```

Can anyone help me out on this one?

I'm using Personal Cobol, and I got the message "Procedure Name Not
Unique". I have no idea what this means, because the procedure name is
only used once, and is called two or three times.

Any help appreciated.

   #######  #
   #  #  #
      #    ##  # ### ###    ###
####  #     #   #   #   #  #   #
      #     #   #   #   #  #   #
     ###   ### ### ### ###  ###

"STUPID, STUPID RAT CREATURES!!"
                    -Fone Bone

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ http://www.concentric.net/~tsuave/quagmire.htm ~
~ ```` email: tsu··.@con··c.net ```` ~
~ ```````````````` AIM: tsuave2 ```````````````` ~
~ `````````````` 70 posts to AGFF `````````````` ~
~ `````````` over 250 posts to ACE93! `````````` ~
~ ```````` winner of a DEELEY-BOB award ```````` ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

#### ↳ Re: Procedure name not unique--huh?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34E5E4A0.985715BB@concentric.net>`
- **References:** `<34E5E4A0.985715BB@concentric.net>`

```

timo suave wrote in message <34E··.@con··c.net>...
› Can anyone help me out on this one?
› 
…[24 more quoted lines elided]…
› ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Somewhere within your procedure division, you have two paragraphs or two
sections with the same name. (If it is two paragraphs with the same name,
then they are either in the same section or you don't have any sections.)

+ + + + + + + + + + + + + +
+   Bill Klein -
+       If COBOL were a drug, then I would be a long time addict refusing
treatment or recovery
+               or
 +        "C" is a nice letter to START the name of your programming
language with
 + + + + + + + + + + + + + +
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-02-17T09:31:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p2@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p2@usenetarchives.gap>`

```

In article ,
sit··.@di··c.com (Sitaram Chamarty) wrote:
› On Sat, 14 Feb 1998 16:00:00 -0800, William M. Klein
› wrote:
…[16 more quoted lines elided]…
› silently truncating at 30...

What compiler does that?

If the compiler silently truncates at 30, without issuing a diagnostic
complaining that the name is too long, then the compiler is broken.
Besides, he didn't have any paragraph names that long, and in any
event, as several others have already pointed out, the error is
obvious.
```

#### ↳ Re: Procedure name not unique--huh?

- **From:** "timorath suave" <ua-author-9395718@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34E5E4A0.985715BB@concentric.net>`
- **References:** `<34E5E4A0.985715BB@concentric.net>`

```
Here's the source code. And if you don't like the length of my .sig,
snip it when you reply. There's no need to leave it in when you reply
if it bugs you so much.
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p4@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap>`

```

In article <34E··.@con··c.net>,
timorath suave wrote:
Hi Timorath,

Take a look at the line marked below. See a problem?

BTW, if you want to do programming, decide now to start using meaningful data
and paragraph names. If this was a "real" program in my shop, I have you
killed - slowly.
(snip)
221-two-hundred-21.
perform 233-two-hundred-33.
300-three-hundred.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(snip)
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p4@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap>`

```

timorath suave wrote:

[asking why the compiler complains of a duplicate procedure name]

[snip -- source code, through part of procedure division]

›        221-two-hundred-21.
›            perform 233-two-hundred-33.
›                    300-three-hundred.
 
› Above, the compiler sees a paragraph header for 300-three-hundred.
 
›            write outone-rec from val-1 before advancing 1 line.
›            perform 222-two-hundred-22.
…[8 more quoted lines elided]…
›            perform 300-three-hundred.
 
› [snip -- a couple more paragraphs]
 
 
›        300-three-hundred.

Now the compiler sees a paragraph header with the same name as a
paragraph defined previously, namely 300-three-hundred. Just like
the error message said.

›            compute stugpa = stugpa + gpa.
›            compute stuctr = stuctr + 1.
…[3 more quoted lines elided]…
›            stop run.

Incidentally, your paragraph names are absolutely dreadful. Give
them names that mean something, like 900-end-job. If you read
a big block of code performing a dozen paragraphs whose names give
no clue as to what they do, you can't possibly figure out what's
going on without looking at the inside of each performed paragraph.
If they perform other mysterious paragraphs, you have to look at
them too, and so forth.

(Comments would help, too. Maybe you deleted them to save bandwidth.)

In a tiny homework assignment like this it may not seem to make
much difference. In the real world, where programs typically go
on for thousands of lines, a naming convention like this might cost
you your job, and should.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1998-02-14T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p4@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap>`

```

In article <34E··.@con··c.net>,
timorath suave wrote:
›
› And if you don't like the length of my .sig, snip it when you reply.
› There's no need to leave it in when you reply if it bugs you so much.

It is generally considered rude to _post_ a .sig longer than 4 x 79 in
the Big 8 and most, but not all, of alt.*. See "Rules for Posting to
Usenet" in news.announce.newusers at your site.

I do not usually bother to complain about rude people and I am not doing
so now. It is a waste of time because one of the defining
characteristics of rudeness is the inability to take a hint. Case in
point: others grumbled about your _posting_ such a rude .sig, yet you
talk above about _quoting_ .sigs. Free clue: your .sig was quoted in a
followup (not a "reply") to make fun of you. It makes no difference
whether a dumb .sig is quoted or not; the rudeness inheres in the
_posting_ of it.


[...]
› 221-two-hundred-21.
› perform 233-two-hundred-33.
› 300-three-hundred.

Here you have started a new paragraph named 300-three-hundred. You
should have gotten a diagnostic about procedure-name not in area "A".


[...]
› 300-three-hundred.
› compute stugpa = stugpa + gpa.
› compute stuctr = stuctr + 1.

Here you have another paragraph named 300-three-hundred.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-02-15T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p4@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap>`

```

On Sat, 14 Feb 1998 20:43:07 -0500, timorath suave
wrote:

› Here's the source code. And if you don't like the length of my .sig,
› snip it when you reply. There's no need to leave it in when you reply
› if it bugs you so much.

I see someone has already pointed out your flaw. I have two
suggestions:
1. when a compiler tells you it's a duplicate, assume it's true and
find it, not assume it's wrong and ask us to do the homework.
2. a tip for your success: STOP USING PERIODS at the end of
statements. a period is to be used at the end of a PARAGRAPH only. Had
you been practicing this simple technique, you would have avoided the
problem -- and avoidance is where it's at. periods at end of
statements violates all we know about structured programming and
design.

and I still don't like the sig file...... :-)
david

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1998-02-16T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p8@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap>`

```

On Mon, 16 Feb 1998 18:34:30 GMT, d.s··.@ix.··m.com (David)
wrote:

› 2. a tip for your success:  STOP USING PERIODS at the end of
› statements. a period is to be used at the end of a PARAGRAPH only. Had
…[7 more quoted lines elided]…
› 
David,

The above is an opinion that is hotly contested for and against in
this group. Please don't give newbies the opinion that everyone
thinks that way.

I am not expressing an opinion for and against BTW.

Thanks
Ken
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 4)_

- **From:** "timo suave" <ua-author-9101468@usenetarchives.gap>
- **Date:** 1998-02-16T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p9@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap>`

```

Ken Foskey wrote:
› 
› On Mon, 16 Feb 1998 18:34:30 GMT, d.s··.@ix.··m.com (David)
…[18 more quoted lines elided]…
› I am not expressing an opinion for and against BTW.

I have a question then: are you saying that the only place a period is
required is at the end of a paragraph? I was taught that you needed one
in every location that I had one, and was never told that they were
optional. Given, I had a _very_ bad teacher, so it is possible she
didn't know what she was talking about.

Is that right?

--timo
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 5)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-16T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p10@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap>`

```

timo suave wrote in message <34E··.@con··c.net>...
› Ken Foskey wrote:
›› 
…[29 more quoted lines elided]…
› --timo

Yes, we are saying that the only place that you need (are required) to have
a period is at the end of one paragraph and before the next paragraph
header. For all other "conditional" statements, you can end them with an
END-statement scope delimiter - and you can have as many imperative
statements and scope-terminated statements in a row without having any
periods.

The use of a period versus a scope terminator requires that you understand
the difference between the COBOL statement "CONTINUE" and the "NEXT
SENTENCE" phrase. The former goes to the next logical statement while the
latter goes to the next period. (This is a slight simplification - but is
basically the rules)
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 5)_

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p10@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap>`

```

On Tue, 17 Feb 1998 21:15:41 -0500, timo suave
wrote:

› Ken Foskey wrote:
›› 
…[29 more quoted lines elided]…
› --timo

Hi, Timo,
I'm glad we're spending this time with you -- because you're obviously
listening and concerned. I've seem a bunch of excellent posts of
advice and clarification -- hard to beat that.... :-)

YES, the period was initially intended to end a logic flow that was
written in normal sentences. That predated the concept of structured
programming. It was wrong. It was a concept in mid 1960's..

With structured programming and design, never place a syntax element
(such as a period) where one isn't needed. It forces a logic structure
that isn't needed. Prior to ANSI85 constructs, there was a need to
place periods occasionally, My advice is to treat a period as a
verb, i.e., place on a separate line -- it emphasizes its function.

In today's COBOL, the better compilers can implicitly insert a period
at the end of paragraphs for you -- that means you NEVER need to write
one yourself. Avoid them. If it doesn't add to functionality, DON'T
use it....

I advised a major cobol book publisher to stop putting periods at the
end of statements -- his reply was that "He had heard that it improved
compile time efficiency...." that is *NOT* where the money is,
folks...

In summary, the period is a logic element, not a grammatical element
or a 'neatness' element. It has the power of an END-IF, END-READ,
END-COMPUTE, etc.....

So, Timo, my advice is to write a program witn *NO* periods -- odds
are it will compile and work fine. Yes, you may receive a few warning
messages that a paragraph was missing a period.... but you'll learn
far more than your class.

I'm pursuing getting my book back in print -- it has much info on
this.... if I succeed, I'll let you know... :-)
david

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 6)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-19T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap>`

```

David wrote in message <34e··.@nnt··m.com>...
› On Tue, 17 Feb 1998 21:15:41 -0500, timo suave
› wrote:
…[74 more quoted lines elided]…
› 
I strongly disagree with the advice of leaving out the period at the end of
each paragraph (and expecting the compiler to do it for you). With the next
Standard, the old A-margin/B-margin distinction goes away (as it already has
with a number of existing compilers - a an extension.) Once this happens,
you REALLY need to put that period in -or the following paragraph-name may
well NOT be treated as a new paragraph.
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 6)_

- **From:** "news" <ua-author-13363@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap>`

```

I'm a novice and have found 2 things in my maintenance assignments.
1) Too many d-mn periods; they are worthless. When I ask, the experts, say
thats the way they learned, and thats the way they'll do it. Luckily my
boss, says make the changes necessary as I want them. One key trick to
never lose the paragraph period is to code the paragraph name
100-init-rtn.

. <<<<< see that period sitting there all neat undisturbed. I leave it
alone, and at compile time, it leaves me alone. Let it see there, it wont
be lonely. Trust me.
100-exit. exit.

2) Use scope delimiters!!!!!!!!!!!!!!!!!! They work and encapsulate
sentences quite neatly.
The END-IF & END-PERFORM are not the only ones. Theres even an
END-COMPUTE, END_READ,
END-DIVIDE. They add readability to your program.

I have read and maintained garbage code and neat code written by experts.
The legacy experts are the ones who learn that maybe there is another way
to write and arent stuck in their holier than thou attitudes. Just
because youve been around along time doesnt mean youre that good.

Continually striving for the best,
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 7)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p14@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p14@usenetarchives.gap>`

```

news wrote:
› 
› [snippage]
…[3 more quoted lines elided]…
› to write and arent stuck in their holier than thou attitudes.  

Well... yes 'n no. At the heart of it is the change in the language and
compiler (IKFCBL00 to IGYCRCTL) and, of course, changes in hardware.
One who has spent a few decades *knowing* that neglecting a period's
placement will generate a 3:AM Production Problem has caused more than
one Olde-Tymer to be rather... insistent on those funky little dots; as
my first COBOL instructor, Mr Mullen, wrote on the back of his shovel
with a piece of coal before the fireplace way back when:

A SENTENCE EXPRESSES A COMPLETE THOUGHT.
A SENTENCE ENDS WITH A PERIOD.
PERIOD.

You spend a few years pumping out code like that (and finding a few
dificulties caused by misplaced periods) and you might get a bit...
insistent about such things.

Likewise, one trained entirely in COBOL-85 might have learned

A PARAGRAPH CONTAINS LOGIC WHICH ACCOMPLISHES A FUNCTION
A PARAGRAPH MUST BE RE-USEABLE IN ANY PART OF THE PROGRAM
A PARAGRAPH ENDS WITH A PERIOD
.

... and hey, it works... Life is Good.

The Greatest Danger, I would say, lies in the careless combining of the
styles... turgid, hoary, blocked-out code (all TOs 'n THRUs in col 44,
for example) with bits of the more free-flowing stuff interspersed as
maintenance/enhancement demands it... randomly, as it were. Part of
troubleshooting/modifying code is 'covering yourself with the smell' of
it, getting the *feel* of it... 'Oh, I've seen this before... there
should be an EXAMINE coming up, that's how he usually does this'... and
mixing the styles can lead to a wee bit of confusion, especially in
those lovely mid-window, pre-dawn hours.

In short, two conclusions:

1) All things in Moderation... *including* Moderation.

2) IF PROGRAM-RUNS
PERFORM NEXT-ASSIGNMENT
ELSE
PERFORM CODE-LIKE-HELL UNTIL DAMNED-THING-WORKS. (<==
period!)

DD
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 7)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p14@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p14@usenetarchives.gap>`

```

news wrote:
(snip)

› 2)   Use scope delimiters!!!!!!!!!!!!!!!!!!   They work and encapsulate
› sentences quite neatly.
› The END-IF & END-PERFORM are not the only ones.  Theres even an
› END-COMPUTE, END_READ,
› END-DIVIDE.  They add readability to your program.

Right, also END-CALL (which I like a lot, like END-EXEC in CICS & SQL
commands), END-ADD, END-MULTIPLY, etc. We have the ability, with the COBOL-85
compilers and later, to write nice blocks of code.

Bill Lynch

(snip)
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 7)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-02-21T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p14@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p14@usenetarchives.gap>`

```

news wrote:
›
› Just because youve been around along time doesnt mean youre that good.

Than again, it might. ;-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 6)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap>`

```

David wrote:
(snip)

› So, Timo, my advice is to write a program witn *NO* periods -- odds
› are it will compile and work fine. Yes, you may receive a few warning
› messages that a paragraph was missing a period.... but you'll learn
› far more than your class.
› 

I'm in complete agreement with the notion of using periods (full stops) only
when necessary, they are COBOL verbs and should be regarded as such. I do want
to caution against writing your program with no periods if your platform is
IBM mainframe, periods are still required after each Data Division statement
and before each paragraph name. If you leave them out you don't get warnings
(you get error messages which carry higher return codes, e.g., 8 instead of 4
for a warning) and you don't get a load module.

Bill Lynch


› I'm pursuing getting my book back in print -- it has much info on
› this....   if I succeed, I'll let you know...   :-)
› david
› 
› David        d.s··.@ix.··m.com
 
› Good luck, David, on getting your book back in print.
 
› ____________________________________
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 7)_

- **From:** "huib klink" <ua-author-17074371@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p18@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p18@usenetarchives.gap>`

```



Bill Lynch wrote:

› I'm in complete agreement with the notion of using periods (full stops) only
› when necessary, they are COBOL verbs and should be regarded as such. I do want
…[4 more quoted lines elided]…
› for a warning) and you don't get a load module.

I do much agree with Bill. After having programmed in Cobol for almast 18 years, I
learned one thing :

Never accept compiles with warnings, let alone with errors.

Exceptions there are. I believe. I personally know none. Letting warnings sit is
giving in to quality. Too lazy to change? Silly arguments of compiler nog good
enough? ROFL.

Since Cobol '85, as a programmer I use and as a coach/trainer to my students /
trainee's I tell to use a period (in the PROC DIV):
- after a procedure name.
- as the last element in a paragraph (I prefer on a line of its own for easy
editable extension of the paragraph)
- nowhere else

In the PROC DIV the period has a SEMANTICal meaning as well as a syntactical
meaning. Cobol '85 has made the semantic use op periods superfluous, by giving us
the scope delimiters. (Thats why one says that "structures programming" has been
added to the language). So get rid of the semantic periods, use only the
syntactically needed ones, in the way I mentioned above.

In the first three divisions, the period has only syntactical meaning, so use it
there whenever the language definition says it is needed. One exception: the
period as picture character has of course semantic meaning).

Because a compiler may at least get syntactically correct sources from us. We do
have problems enough making programs that work correct. It's so easy to make them
compile correct, don't mess. You'll need the energy for the algorithm

Just an opinion.

Huib
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 6)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-02-21T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap>`

```

David wrote:

› I advised a major cobol book publisher to stop putting periods at the
› end of statements -- his reply was that "He had heard that it improved
› compile time efficiency...."   that is *NOT* where the money is,
› folks...

First, you are right that compile time efficiency is not where the money
is.

But second, adding an extra period should not make the compiler more
efficient. It's an extra token to handle; under most circumstances that
will add to compile time (not in amounts worth measuring). If anything,
the period is particularly inefficient because the compiler has to look
back to find what conditional statements need to be terminated, while
running into the next verb just ends one statement.

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ The puzzle too hard for human beings:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 6)_

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1998-02-22T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap>`

```

On Sat, 21 Feb 1998 02:26:35 GMT, d.s··.@ix.··m.com (David)
wrote:

David,

I stick to my original comments that these are disputed discussions.
Having said this I am now far more in favour of using a single period
based upon these discussions.

I have added some comments after some of your statements
(substantially trimmed).

› 
› In today's COBOL, the better compilers can implicitly insert a period
› at the end of paragraphs for you -- that means you NEVER need to write
› one yourself.  Avoid them.  If it doesn't add to functionality, DON'T
› use it....
Under OS/390 the cobol compiler issues a warning. I strongly
recommend zero warnings in a compile. I was amazed that I picked up 2
faults in production code running for three years by checking the
warnings (four character literal compared to a three character field
for example). IF you choose to code this way I recommend that you do
use the period, I agree with the comment that it should be on a
separate line but this is to do with programmer taste more than
anything else.

› 
› I advised a major cobol book publisher to stop putting periods at the
› end of statements -- his reply was that "He had heard that it improved
› compile time efficiency...."   that is *NOT* where the money is,
› folks...   
Yes - My compiler runs while I am doing something else. PC code may
be different but I doubt that you could measure the difference on a
stop watch for a huge program.

›
› In summary, the period is a logic element, not a grammatical element
› or a 'neatness' element. It has the power of an END-IF, END-READ,
› END-COMPUTE, etc.....

Strongly agree. Use END-IF's and align them to the IF eg:

IF xyz
MOVE ...
END-IF

See a separate thread discussing the use thereof. Has any one seen a
cobol code reformatter that puts the END-IF's into code for you?

Good luck with your book
Ken
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 7)_

- **From:** "pa..." <ua-author-6589140@usenetarchives.gap>
- **Date:** 1998-02-23T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p21@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p21@usenetarchives.gap>`

```

Ken Foskey (kfo··.@tig··m.au) wrote:

: Strongly agree. Use END-IF's and align them to the IF eg:

: IF xyz
: MOVE ...
: END-IF


Well, I agree except my taste is to indent the END's with the
code section they are bracketing. :)

IF it-needs-doing
PERFORM DoSomething-One
PERFORM DoSomething-Two
END-IF.

I would REALLY prefer it if the language was consistant with the
use of periods. For example, the above code has one period at the
end of the section, but to MY eyes it would look better
if the IF was ended soley by the END-IF and not the period.
Then you could have periods behind each sentance. :)

Of course, this comes from being used to other languages
where statement terminators are not used to define blocks of
code. :)


-Paul
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 6)_

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1998-02-22T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p12@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap>`

```

David wrote:

[snip -- part of one of several posts along the same lines]

› YES, the period was initially intended to end a logic flow that was
› written in normal sentences.  That predated the concept of structured
…[6 more quoted lines elided]…
› verb, i.e., place on a separate line -- it emphasizes its function.

There is a curious double standard being applied here.

"Never place a syntax element where one isn't needed." Therefore
we should never use a period if we don't have to. However, the same
rule does not seem to apply to equally unnecessary trains of END-IFs
and their kindred. Where a single character can do the work of six
or eight lines of code -- and it may take several minutes to figure
out just how many -- we are supposed to favor the six or eight lines
over the single character.

Equally tenuous is the argument -- or rather unsupported assertion --
that periods violate the principles of structured programming. One
might as well argue that GO TOs violate the law of gravity. The
two have absolutely nothing to do with each other. You can have
well-structured code with lots of periods, and you can have
unstructured or poorly structured code with minimal periods.

As I have always understood the basic principles of structured
programming, they amount to:

1. One exit point and one exit point per module. "Module" means
different things to different people, or in different contexts.
Without trying to be too precise I'll define it here as a procedure
or function invoked by name.

2. Restriction of control structures to three:

a. Sequential execution of instructions;

b. Selection -- i.e. IF, IF...ELSE, and perhaps some form of
case structure such as EVALUATE in COBOL;

c. Iteration -- i.e. PERFORM UNTIL, do...while, and the like.
Ideally the one entry/one exit rule applies to a loop as well.

(These rules are sometimes improperly summarized as "Don't use GO TO.")

Structured programming is often associated with other notions which
are logically distinct -- modular programming, top-down development,
abstract data types, and so forth. Traditional structured analysis
and design involves the use of data flow diagrams, structure charts,
and functional decomposition.

I fail utterly to see what any of these constellations of ideas have
to do with the choice of periods vs. scope terminators in COBOL --
a narrow stylistic issue confined to a single language.

There are sound arguments for avoiding periods, and other sound
reasons not to. Reasonable people may disagree, or have different
tastes. The issues are not so clear-cut as to justify a lot
of intemperate, tub-thumping pronouncements about right and wrong.

Most of the posts in this thread have at least agreed on the evils
of periods. Just to be contrary, I'll take the opposing view:

1. A lot of currently-running applications were originally written
before scope terminators like END-IF were available. Converting all
this code to eliminate unnecessary periods would cost time and money,
and would needlessly create opportunities for errors, while providing
no benefit in functionality or performance. Converting it piecemeal
would create disconcerting inconsistencies over an extended period
of time. (Of course if the conversion were automated through some
kind of code-mangling program, these arguments would not apply.)

2. Long trains of END-IFs snaking across the page are bulky, hard to
read, and slow to type. They crowd meaningful code off the screen, or
off the page, in a language already notorious for verbosity.

3. If blocks of conditional code are terminated only by END-THIS and
END-THAT, it is difficult to tell which code is *not* conditional.
You have to pick your way backward through the code, matching up
all the END-IFs with their ELSEs and IFs, hoping not to be misled by
some careless indentation.

None of these arguments is compelling. Neither are the arguments
against periods. By avoiding periods you may simply trade one
category of mistakes for another.

>From experience I know that I am more likely to misplace an END-IF
than to misplace a period. As a result I use scope terminators when
they come in handy, and I am happy to have them, but I also use
periods in roughly the traditional fashion.

Others have different collections of weaknesses, and different tastes,
and they are welcome to them. The only thing I can't stand is
intolerance.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 7)_

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1998-02-25T19:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p23@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p23@usenetarchives.gap>`

```

On Mon, 23 Feb 1998 23:03:42 -0600, "Michael C. Kasten"
wrote:

... a subset from a private mail from Michael ....

› Many have posted unsupported assertions that a period-free style is
› cleaner, less error-prone, and on and on.  However *nobody* -- with the
› notable exception of your posting of a few weeks ago -- has ever posted
› a coherent explanation of where the advantages come from.
› 

Michael

Can't claim this one. To the original author I would attribute but
alas your message is no more, victim of the purge routine. If the
original author is out there, can could you set up a link for the
rest of us to point at as a description of the style (please feel free
mail me if you need any help).

Michael, I think exactly the same thing as you. The first reasonable
argument was posted here and I now do not dismiss the style, it has
merit.

No I do not code this way. I am unlikely to change the way I code but
if the shop standard was period free I would no longer think it
totally daft. I originally stated that the statement was not widely
supported and I was backing up some of the sytlistic issues that I do
like.

That description would make a great link for your style guide. Which
I still highly recommend to everyone as worth looking at.

http://home.swbell.net/mck9/cobol/cobol.html

Ken
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 8)_

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1998-02-25T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p24@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p23@usenetarchives.gap> <gap-f8cf91ef9c-p24@usenetarchives.gap>`

```

Ken Foskey wrote:
› 
› On Mon, 23 Feb 1998 23:03:42 -0600, "Michael C. Kasten"
…[16 more quoted lines elided]…
› mail me if you need any help).

[snip]

I slightly mis-remembered your article (dated Nov. 9, 1997). You
were promoting the use of scope terminators such as END-IF. The use
of periods was tangential to your article, but in my mind the two
issues are closely related, since a no-period policy all but
guarantees a liberal use of END-IF and its kindred.

Your argument for scope terminators can be extended without too much
strain to an argument against periods. The text follows, with minor
deletions at the beginning and end:

[begin quote]

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
MOVE ÂJOEÂ TO WORKER (1)
MOVE ÂPAULÂ TO WORKER (1).
MOVE ÂKENÂ TO WORKER (2).

Most code reviews will pick up the subscripting error but not the
extra period.

If the code is written as follows then the first compile will pick up
the error.
IF FRED-88
MOVE ÂJOEÂ TO WORKER (1)
MOVE ÂPAULÂ TO WORKER (1).
MOVE ÂKENÂ TO WORKER (2)
END-IF.

[end quotation]

My thanks to http://www.dejanews.com for enabling me to dredge up
this expired article.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 9)_

- **From:** "paul keirnan" <ua-author-17074680@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p25@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p23@usenetarchives.gap> <gap-f8cf91ef9c-p24@usenetarchives.gap> <gap-f8cf91ef9c-p25@usenetarchives.gap>`

```

I also agree with the coding of COBOL without fullstops
after every statement.

However, where the paragraph must be terminated by a fullstop,
I strongly disagree with using a fullstop on a line by itself.

What I would advocate is the use of 'Continue.' as the last line
of a paragraph. This is far more visible than the sole fullstop.

Regards,
Paul
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 10)_

- **From:** "huib cobol frog klink" <ua-author-17074505@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p26@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap> <gap-f8cf91ef9c-p10@usenetarchives.gap> <gap-f8cf91ef9c-p12@usenetarchives.gap> <gap-f8cf91ef9c-p23@usenetarchives.gap> <gap-f8cf91ef9c-p24@usenetarchives.gap> <gap-f8cf91ef9c-p25@usenetarchives.gap> <gap-f8cf91ef9c-p26@usenetarchives.gap>`

```

Paul Keirnan wrote:

› What I would advocate is the use of 'Continue.' as the last line
› of a paragraph. This is far more visible than the sole fullstop.

Which I find a good idea!!!. Thanks, Paul. Never thought about that!

Huib
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

_(reply depth: 4)_

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p9@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p4@usenetarchives.gap> <gap-f8cf91ef9c-p8@usenetarchives.gap> <gap-f8cf91ef9c-p9@usenetarchives.gap>`

```

On Tue, 17 Feb 1998 08:37:44 GMT, kfo··.@tig··m.au (Ken Foskey)
wrote:

› On Mon, 16 Feb 1998 18:34:30 GMT, d.s··.@ix.··m.com (David)
› wrote:
…[20 more quoted lines elided]…
› Ken

Ken, then you're not helping us if you have no opinion. If this is
hotly contested, then let the debates begin. We are here to further
COBOL, and structure and design is where the future is. 90% of all
COBOL problems I've seen relate to periods 'in the way'. It was a
'nice idea' in early 60's to write procedural code much as you'd write
a letter to mom.... but it never worked. The PERIOD is a piece of
cobol syntax and deserves to be treated the same as we treat a verb,
i.e., on a line by itself. ALso, since it brings all logic to a halt,
it violates the structured programming design concept. I should be
able to insert a line of text within a paragraph and be unencumbered
by periods.... the language offers all we need to manage this
structure and the elementary problem brought to this August NG was due
to an abundance of periods in the source code.

Reading the code was like following someone on a thruway who kept
pressing the brake pedal every 10 seconds -- just in case.... let's
get beyond this... if we can't make headway on structure,
decomposition, language syntax, --- then we'll end up the GWBASIC of
the 90's.... LOL

Yes, I'm serious. We must somewhere make a stand. I dropped out of the
GOTO debates as they GO nowhere (pardon the pun...)

david

David d.s··.@ix.··m.com
____________________________________
```

#### ↳ Re: Procedure name not unique--huh?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p29@usenetarchives.gap>`
- **In-Reply-To:** `<34E5E4A0.985715BB@concentric.net>`
- **References:** `<34E5E4A0.985715BB@concentric.net>`

```

timo suave wrote:
› 
› Can anyone help me out on this one?
…[3 more quoted lines elided]…
› only used once, and is called two or three times.

Hmmmm, this sounds like homework... but what the heck, post the code and
let's have a look-see.

DD
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "randy van de loo" <ua-author-6589188@usenetarchives.gap>
- **Date:** 1998-02-15T19:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p29@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p29@usenetarchives.gap>`

```

› timo suave wrote:
›› Can anyone help me out on this one?
›› I'm using Personal Cobol, and I got the message "Procedure Name Not
›› Unique".  I have no idea what this means, because the procedure name is
›› only used once, and is called two or three times.
 
› Hmmmm, this sounds like homework... but what the heck, post the code and
› let's have a look-see.
› 
› DD

Going soft on us Goobers???

---------------------------------------------
> Randy  Van de Loo  -  PRO/teus Technology <
> remove NOSPAM from E-mail address before  <
> replying.                                 <
---------------------------------------------
Bait for spammers (With credit to E. Needham):
root@localhost
postmaster@localhost
admin@localhost
abuse@localhost
pos··.@127··0.1
```

###### ↳ ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-02-15T19:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p30@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p29@usenetarchives.gap> <gap-f8cf91ef9c-p30@usenetarchives.gap>`

```

Randy Van de Loo wrote:
› 
›› timo suave wrote:
…[10 more quoted lines elided]…
› Going soft on us Goobers???

Hee hee hee... a foolish consistency is the petty hobgoblin of small
minds, or so Thoreau said.

DD
```

#### ↳ Re: Procedure name not unique--huh?

- **From:** "timorath suave" <ua-author-9395718@usenetarchives.gap>
- **Date:** 1998-02-14T19:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p32@usenetarchives.gap>`
- **In-Reply-To:** `<34E5E4A0.985715BB@concentric.net>`
- **References:** `<34E5E4A0.985715BB@concentric.net>`

```

Thanks to everyone for the help.

And just so you know, I don't usually name my procedures that poorly.
When I was writing them, I wasn't sure what was going to go into each
one, so I named them generically. I'll change them before I'm done.

- timo
```

##### ↳ ↳ Re: Procedure name not unique--huh?

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1998-02-14T19:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f8cf91ef9c-p32@usenetarchives.gap>`
- **References:** `<34E5E4A0.985715BB@concentric.net> <gap-f8cf91ef9c-p32@usenetarchives.gap>`

```

On Sun, 15 Feb 1998 03:51:05 -0500, timorath suave
wrote:

› Thanks to everyone for the help.
› 
…[4 more quoted lines elided]…
› - timo

Just an opininion but you should have a concept of what they contain.
This concept may grow and therefore teh name may need to be altered to
accurately reflect the purpose but start out clean. This will save
you time in the long run.

Ken
```

#### ↳ Re: Procedure name not unique--huh?

- **From:** "dk..." <ua-author-17084214@usenetarchives.gap>
- **Date:** 1998-02-14T19:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f8cf91ef9c-p34@usenetarchives.gap>`
- **In-Reply-To:** `<34E5E4A0.985715BB@concentric.net>`
- **References:** `<34E5E4A0.985715BB@concentric.net>`

```

timo suave (tsu··.@con··c.net) wrote:
: Can anyone help me out on this one?

: I'm using Personal Cobol, and I got the message "Procedure Name Not
: Unique". I have no idea what this means, because the procedure name is
: only used once, and is called two or three times.

: Any help appreciated.

: --
: ####### #
: # # #
: # ## # ### ### ###
: #### # # # # # # #
: # # # # # # #
: ### ### ### ### ### ###

: "STUPID, STUPID RAT CREATURES!!"
: -Fone Bone

: ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
: ‾ http://www.concentric.net/‾tsuave/quagmire.htm ‾
: ‾ ```` email: tsu··.@con··c.net ```` ‾
: ‾ ```````````````` AIM: tsuave2 ```````````````` ‾
: ‾ `````````````` 70 posts to AGFF `````````````` ‾
: ‾ `````````` over 250 posts to ACE93! `````````` ‾
: ‾ ```````` winner of a DEELEY-BOB award ```````` ‾
: ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

why not show us the source? Clearly , the compiler is not wrong, but
you're not seeing the error. and do we need to see sig files longer than
the post itself? (grumble, grumble...)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
