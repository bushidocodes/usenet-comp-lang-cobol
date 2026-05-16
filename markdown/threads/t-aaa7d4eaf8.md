[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Structured versus the other way.

_6 messages · 6 participants · 2001-05 → 2001-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Structured versus the other way.

- **From:** foodman <nospam@newsranger.com>
- **Date:** 2001-05-31T12:07:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VtqR6.6788$rn5.317795@www.newsranger.com>`

```
Hi:

For anyone interested in making a fair, unbiased, unemotional, objective
look at Mr. Dashwood's structured code and my admittedly old-fashioned
code I have put a copy of my original post on my website.

When everything is lined up properly it makes it easy to compare
Mr. Dashwood's coded with mine.

Go to foodman123.com/post.htm

to see it as I composed it.

Thanks

Tony Dilworth
```

#### ↳ Re: Structured versus the other way.

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2001-05-31T09:39:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1657B7.E0A40775@certcoinc.com>`
- **References:** `<VtqR6.6788$rn5.317795@www.newsranger.com>`

```
Sorry Tony but for the same reason you are more comfortable with your
"simple" code I am more comfortable with the top down approach.  Probably
one is no better than the other but my personal preference is definitely top
down with out the go to's.  I guess beauty is in the eye of the beholder.<G>

PatH

foodman wrote:

> Hi:
>
…[13 more quoted lines elided]…
> Tony Dilworth
```

#### ↳ Re: Structured versus the other way.

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-05-31T15:10:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0105311410.35d6f677@posting.google.com>`
- **References:** `<VtqR6.6788$rn5.317795@www.newsranger.com>`

```
foodman <nospam@newsranger.com> wrote in message news:<VtqR6.6788$rn5.317795@www.newsranger.com>...
> Hi:
> 
…[12 more quoted lines elided]…
> 


This style ALWAYS looks simpler for short programs which have a single
function.  I have seen this kind of example used for years and years
to justify "Top-down with forward GO TO's".

The problems are with maintenance.  
SCENARIO:
Your program is in production.  The user now wants to add five more
fields, with their own edits and with cross edits. Six months later,
the user needs the inputs to be validated against an input file. A
while later, certain validated input data is to be used to create a
new file.  Then, some data will be used to create a file, and some
will be used to update 2 different files. A month later, the
validation and update criteria change.

By now, you KNOW it's a mess of spaghetti.  Not only that, it will be
a testing nightmare because logically related procedures may be in
very widely spaced locations in the code -- easy to miss.

I'll take Mr Dashwood's style any day!  It's mine, too! 

Stephen J Spiro
```

##### ↳ ↳ Re: Structured versus the other way.

- **From:** james.watts@unisys.com (Jim Watts)
- **Date:** 2001-06-04T14:30:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fg61f$a4r$2@mail.pl.unisys.com>`
- **References:** `<VtqR6.6788$rn5.317795@www.newsranger.com> <4145699b.0105311410.35d6f677@posting.google.com>`

```
Having written 1 million plus lines of Cobol code, I vote for the second 
method.  It is cleaner, easier to understand and most of all it is far easier 
to maintain.  If everyone would put more though in to teh maintainability of 
their code things would be better.  

I am also a fan of responsable use of the GOTO statement.  If used correctly, 
the code is cleaner, easier to understand and maintain.

In article <4145699b.0105311410.35d6f677@posting.google.com>, 
stephenjspiro@hotmail.com (Stephen J Spiro) wrote:
>foodman <nospam@newsranger.com> wrote in message
> news:<VtqR6.6788$rn5.317795@www.newsranger.com>...
…[37 more quoted lines elided]…
>Stephen J Spiro
```

#### ↳ Re: Structured versus the other way.

- **From:** "Joe Durnavich" <joejd@mcs.net>
- **Date:** 2001-06-04T19:02:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1XQS6.64912$4f7.4894927@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<VtqR6.6788$rn5.317795@www.newsranger.com>`

```

foodman writes:

> For anyone interested in making a fair, unbiased, unemotional, objective
> look at Mr. Dashwood's structured code and my admittedly old-fashioned
…[7 more quoted lines elided]…
> to see it as I composed it.

My own variation of Dashwood's code follows.  The advantage of
the structured approach is that the loop conditions are stated explicity.
You can easily tell that there is a loop, what the initial conditions are,
and
what it takes to stop it.  With your code, you have to read through
a whole paragraph and dig out that information.  For example, in
your version, you don't know that paragraph B is a loop until you
get to the GO TO at the end of it.

Also, in a large structured program, you can be sure the program
starts and stops in the main paragraph.  You don't have to hunt
through the code for GO TO END-PROGs.  These tend to introduce
bugs in which allocated resources are not freed because
somebody added an exit somewhere in the middle of the code.

       PROCEDURE DIVISION.

       MAIN-PARAGRAPH.
           ACCEPT INPUT-STRING.
           PERFORM
               UNTIL INPUT-STRING = SPACES
                   PERFORM REMOVE-SPACES
                   DISPLAY OUTPUT-STRING
                   ACCEPT INPUT-STRING
           END-PERFORM.
           STOP RUN.

       REMOVE-SPACES.
           MOVE SPACES TO OUTPUT-STRING.
           SET OUT-IX TO ZERO.
           PERFORM
               VARYING IN-IX FROM 1 BY 1
               UNTIL IN-IX > IN-LENGTH
               OR    OUT-IX = OUT-LENGTH
                   IF IS-CHAR(IN-IX) NOT = SPACE
                       SET OUT-IX UP BY 1
                       MOVE IS-CHAR(IN-IX) TO OUT-CHAR(OUT-IX)
                   END-IF
           END-PERFORM.

       END PROGRAM.
```

##### ↳ ↳ Re: Structured versus the other way.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-05T08:28:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1C8A25.53509C93@Azonic.co.nz>`
- **References:** `<VtqR6.6788$rn5.317795@www.newsranger.com> <1XQS6.64912$4f7.4894927@bgtnsc06-news.ops.worldnet.att.net>`

```
Joe Durnavich wrote:
> 
> foodman writes:
…[4 more quoted lines elided]…
> and

> what it takes to stop it.  With your code, you have to read through
                                             ^^^
> a whole paragraph and dig out that information.  For example, in
> your version, you don't know that paragraph B is a loop until you
                ^^^
> get to the GO TO at the end of it.

One of the problems with Foodman's perception on this is that _he_
DOESN'T "have to read through a whole paragraph" and _he_ DOES know the
paragraph B is a loop.

It appears that Foodman has used codes for his names in a consistent
(but secret) way, and has constructed loops in a specific manner, so
that when he sees the paragraph 'B' he _does_ know it is a loop and
cannot understand your objection.

Aside from the fact that he wrote the example (and thus has prior
knowledge of his), he has written in this style (in isolation
apparently) for decades.  When he sees other code he simply cannot
understand it as easily as his own, that must be the other person's
fault, or the other style's fault.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
