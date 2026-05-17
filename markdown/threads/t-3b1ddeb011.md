[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with an EVALUATE statement

_14 messages · 12 participants · 1996-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Problem with an EVALUATE statement

- **From:** "stephane bodart" <ua-author-17086396@usenetarchives.gap>
- **Date:** 1996-09-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3235FBFF.330B@info.fundp.ac.be>`

```

I have a problem with the following statement :

EVALUATE ET
WHEN "CUSTOMER" DISPLAY "Entity Customer"
WHEN "ORDER" DISPLAY "Entity Order"
END-EVALUATE.

If the variable ET has the value "CUSTOMER", then the instruction
DISPLAY "Entity Customer" is executed twice ???
If I read my reference manual, when the condition is verified, the first
instruction following the condition must be executed. After, we must go
out of the evaluate instruction !!!

Thanks for your reply.

Stephane.
```

#### ↳ Re: Problem with an EVALUATE statement

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-09-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3235FBFF.330B@info.fundp.ac.be>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be>`

```

Stephane Bodart wrote:
› 
› I have a problem with the following statement :
…[4 more quoted lines elided]…
›            END-EVALUATE.

The statement is syntactically correct (I would never put a period
after END-EVALUATE, however - but it is legal).

› If the variable ET has the value "CUSTOMER", then the instruction
› DISPLAY "Entity Customer" is executed twice ???
› If I read my reference manual, when the condition is verified, the first
› instruction following the condition must be executed. After, we must go
› out of the evaluate instruction !!!

You are right. It appears that you might have hit a bug or something
or somehow you are executing the statement twice due to something else
in the program. I can't imagine that a bug like that would get out
(the guy will probably come back and say it is my compiler - would be
just my luck).

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: Problem with an EVALUATE statement

- **From:** "william b. wilborn" <ua-author-15698000@usenetarchives.gap>
- **Date:** 1996-09-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3235FBFF.330B@info.fundp.ac.be>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be>`

```

Stephane Bodart wrote:
› 
› I have a problem with the following statement :
…[14 more quoted lines elided]…
›         Stephane.It is difficult to tell without seeing the rest of the code, but this 
type of problem is typically caused by falling through the code a second
time. It can easily be caused by a missing STOP RUN. If the program is
not too long, send the whole thing.

Bill Wilborn
```

##### ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "stephane bodart" <ua-author-17086396@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p3@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap>`

```

William B. Wilborn wrote:
› Stephane Bodart wrote:
›› 
…[20 more quoted lines elided]…
› Bill Wilborn

This is the interesting part of my program. The procedure TEST-READ is
only executed once.

TEST-READ.
IF OP-CODE IS EQUAL TO 3
THEN
PERFORM READ-FIRST
END-IF.

READ-FIRST.
EVALUATE ET
WHEN "CUSTOMER" DISPLAY "Entity Customer"
WHEN "ORDER" DISPLAY "Entity Order"
END-EVALUATE.

I've tested my program with the debugger. ET has the "CUSTOMER" value.
It displays "Entity
Customer". Then the cursor of the debugger is going to the END-EVALUATE
instruction.
No problem at his moment.
But after this, it re-executes directly the line :
WHEN "CUSTOMER" DISPLAY "Entity Customer".
I'm sure that the procedure READ-FIRST is not executed twice ???

Thanks.
Stephane.
```

###### ↳ ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "john keane" <ua-author-2851830@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p4@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap> <gap-3b1ddeb011-p4@usenetarchives.gap>`

```

› 
›        TEST-READ.
…[21 more quoted lines elided]…
›         Stephane.

IMHO, it appears as if your code is executing READ-FIRST the first time
from the PERFORM in TEST-READ and once as it falls through READ-FIRST
after returning to TEST-READ. In other words, the program is not
returning to its source after executing TEST-READ, but is falling through
to execute READ-FIRST a second time.

John Keane
```

###### ↳ ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p4@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap> <gap-3b1ddeb011-p4@usenetarchives.gap>`

```

: > Stephane Bodart wrote:
: > >
: > > I have a problem with the following statement :
: > >
: > > EVALUATE ET
: > > WHEN "CUSTOMER" DISPLAY "Entity Customer"
: > > WHEN "ORDER" DISPLAY "Entity Order"
: > > END-EVALUATE.
: > >


I'm not familiar with the EVALUATE statement, but should the WHEN
statement be terminated with a period?
```

###### ↳ ↳ ↳ Re: Problem with an EVALUATE statement

_(reply depth: 4)_

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-09-11T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p6@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap> <gap-3b1ddeb011-p4@usenetarchives.gap> <gap-3b1ddeb011-p6@usenetarchives.gap>`

```

jya··.@fre··h.us (Jack Yazel) wrote:
+: > Stephane Bodart wrote:
+: > >
+: > > I have a problem with the following statement :
+: > >
+: > > EVALUATE ET
+: > > WHEN "CUSTOMER" DISPLAY "Entity Customer"
+: > > WHEN "ORDER" DISPLAY "Entity Order"
+: > > END-EVALUATE.
+: > >
+
+
+ I'm not familiar with the EVALUATE statement, but should the WHEN
+statement be terminated with a period?
+
+
Nope.
```

###### ↳ ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p4@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap> <gap-3b1ddeb011-p4@usenetarchives.gap>`

```

In <323··.@inf··c.be>, Stephane Bodart writes:
› This is the interesting part of my program. The procedure TEST-READ is
› only executed once.
…[12 more quoted lines elided]…
› 
The Evaluate clause looks perfectly fine to me.
Suggestion: change your code to the following.
READ-FIRST.
DISPLAY "About do do Evaluate".
EVALUATE ET
WHEN "CUSTOMER" DISPLAY "Entity Customer"
WHEN "ORDER" DISPLAY "Entity Order"
END-EVALUATE.
When you run it, if you get two of "About to do Evaluate", you have
a logic bug in your program. If you get only one, but two displays,
of "Entity customer", it points to a compiler bug or some kind of
storage clobber.

Ron (rt at mfltd.co.uk)
address in this funny form to avoid automatic Email Spammers
```

###### ↳ ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-09-11T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p4@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap> <gap-3b1ddeb011-p4@usenetarchives.gap>`

```

How do you get to the paragraph TEST-READ? With a PERFORM,
or with a GO TO? If the latter, that's your problem -- you perform
READ-FIRST, then fall through and execute it again.

Stephane Bodart wrote:
+This is the interesting part of my program. The procedure TEST-READ is
+only executed once.
+
+ TEST-READ.
+ IF OP-CODE IS EQUAL TO 3
+ THEN
+ PERFORM READ-FIRST
+ END-IF.
+
+ READ-FIRST.
+ EVALUATE ET
+ WHEN "CUSTOMER" DISPLAY "Entity Customer"
+ WHEN "ORDER" DISPLAY "Entity Order"
+ END-EVALUATE.
+
+I've tested my program with the debugger. ET has the "CUSTOMER" value.
+It displays "Entity
+Customer". Then the cursor of the debugger is going to the END-EVALUATE
+instruction.
+No problem at his moment.
+But after this, it re-executes directly the line :
+ WHEN "CUSTOMER" DISPLAY "Entity Customer".
+I'm sure that the procedure READ-FIRST is not executed twice ???
+
+ Thanks.
+ Stephane.
```

##### ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "erlend moen" <ua-author-619162@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p3@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p3@usenetarchives.gap>`

```

William B. Wilborn wrote:
<< Stephane.It is difficult to tell without seeing the rest of > the
code, but this type of problem is typically caused by falling through
the code a second time. It can easily be caused by a missing STOP RUN.
If the program is not too long, send the whole thing.>>

Or insert som testpoints before the statement to examine if this really
happens!

<< Erlend Moen, Brushaneveien 19h, N-7082 Kattem, Norway             >>
<< e.mail: e.··.@bnb··k.no  URL: http://home.sn.no/home/bnmo        >>
<< Tel: +47 72 84 83 36 Fax: +47 73 89 20 79 Mobile: +47 92 82 24 64 >>
```

#### ↳ Re: Problem with an EVALUATE statement

- **From:** "fal..." <ua-author-15896936@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p11@usenetarchives.gap>`
- **In-Reply-To:** `<3235FBFF.330B@info.fundp.ac.be>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be>`

```

Stephane Bodart wrote:

› I have a problem with the following statement :
 
›           EVALUATE ET
›        WHEN "CUSTOMER"   DISPLAY "Entity Customer" 
›        WHEN "ORDER"      DISPLAY "Entity Order" 
›           END-EVALUATE.
 
› If the variable ET has the value "CUSTOMER", then the instruction
› DISPLAY "Entity Customer" is executed twice ???

I see nothing wrong with the EVALUATE try setting a breakpoint or
putting a display just before it -- it must be getting executed twice
somehow.

George Trudeau
```

#### ↳ Re: Problem with an EVALUATE statement

- **From:** "truh..." <ua-author-17086349@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p12@usenetarchives.gap>`
- **In-Reply-To:** `<3235FBFF.330B@info.fundp.ac.be>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be>`

```

In article <323··.@inf··c.be>, Stephane Bodart writes:
› I have a problem with the following statement :
› 
…[13 more quoted lines elided]…
› 	Stephane.

I would try to test it like this (add the def. of that w-time to w-s):

ACCEPT W-TIME FROM TIME.
EVALUATE ET
WHEN "CUSTOMER"
DISPLAY "Entity Customer " W-TIME
MOVE "SOMEONE" TO ET
WHEN "ORDER"
DISPLAY "Entity Order " W-TIME
MOVE "OTHERONE" TO ET
WHEN OTHER
DISPLAY ET " " W-TIME
END-EVALUATE.
DISPLAY "This should be between any other displays".


You have a bug in your program, if there is a line "This should..."
after every "Entity customer" line (and that second "Entity customer"
line still appears). That w-time can be used to search the problem,
if there is one (in your program). You have to (of course) accept that
w-time several times elsewhere also, but you got my point, I'm sure.

Hope this helps,

Vellu
```

##### ↳ ↳ Re: Problem with an EVALUATE statement

- **From:** "klei..." <ua-author-4538985@usenetarchives.gap>
- **Date:** 1996-09-12T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3b1ddeb011-p12@usenetarchives.gap>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be> <gap-3b1ddeb011-p12@usenetarchives.gap>`

```

In article <323··.@inf··c.be>, Stephane Bodart This is the interesting part of my program. The procedure TEST-READ is
› only executed once.

TEST-READ.
IF OP-CODE IS EQUAL TO 3
THEN
PERFORM READ-FIRST
END-IF.

READ-FIRST.
EVALUATE ET
WHEN "CUSTOMER" DISPLAY "Entity Customer"
WHEN "ORDER" DISPLAY "Entity Order"
END-EVALUATE.

I do not know how many times I have seen this: Its a fall thru to the
READ-FIRST paragraph. Add a DISPLAY to the TEST-READ paragraph after the
END-IF and then a GOBACK. That will show you the ERROR!!!

Programming 101 Watch for fall thru to other paragraphs.



Ken Leidner                     kle··.@ear··k.net
Systems Programmer                (personal account)
Toyota Motor Sales USA          Ken··.@toy··a.com
                                  (Work E-Mail address)
```

#### ↳ Re: Problem with an EVALUATE statement

- **From:** "timothy hayes" <ua-author-15649287@usenetarchives.gap>
- **Date:** 1996-09-10T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3b1ddeb011-p14@usenetarchives.gap>`
- **In-Reply-To:** `<3235FBFF.330B@info.fundp.ac.be>`
- **References:** `<3235FBFF.330B@info.fundp.ac.be>`

```

Stephane Bodart wrote:
› 
› I have a problem with the following statement :
…[14 more quoted lines elided]…
›         Stephane.

In the procedure that execute the TEST-READ routine, are you using a
THROUGH clause? This could cause the TEST-READ to execute the paragraph
that contains the evaluate and then execute the paragraph that contains
the evaluate again. Just a thought. Here is an example
PERFORM TEST-READ THROUGH EVAL-PARA
...
TEST-READ.
IF FIELD = 3
PERFORM EVAL-PARA
END-IF.

EVAL-PARA.
EVALUATE ET
WHEN 'Customer' DISPLAY 'Enter Customer'
WHEN 'Agent' DISPLAY 'Enter Agent'
END-EVALUATE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
