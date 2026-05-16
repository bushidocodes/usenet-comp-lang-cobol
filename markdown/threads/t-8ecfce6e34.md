[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ELIF Proposal

_91 messages · 29 participants · 1998-11 → 1998-12_

---

### ELIF Proposal

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
Barticus@att.spam.net (Randall Bart)
Date: 29 Nov 1998 06:47:11 GMT
Was kind enough to commented within an ongoing discussion of possibilty of
having an ELIF construct in the COBOL language:

<<
..., most of the modern languages have it.  In Fortran there's an explicit
ELSIF (I think that's how it's spelled), in COBOL-85 it's implemented by
the slightly obtuse EVALUTATE statement, and in C, Algol, and Pascal
there's no need for a special construct, because ELSE followed immediately
by IF is semantically identical to an ELSE-IF.

Judson (McClendon) mentions he's strung so many ELSE IFs together that the
compiler
blew it's stack.  In COBOL-85 this is just a fact of life, because the
compiler has to know how many END-IFs can follow (though a really cleaver
compiler could just have a counter of nested ELSEs); but in a competently
written COBOL-74 compiler, ELSE IF should not increase the nesting level.
>>

His posting was, in part, a response to one of my own. His surveying is
probably more complete than my own, and probably he is right that most
languages have an ELSE IF construct than do not. But the view to the effect
that in COBOL, "...there's no need for a special construct, because ELSE
followed immediately by IF is semantically identical to an ELSE-IF.", deserves
further interaction if you don't mind.

ELSE followed immediately by IF is not _syntactically_ identical to an ELSE-IF.
This creates a weaknesses in COBOL.  

As a standalone statement a long IF-ELSE-IF sequence tends to be indented
further and further in COBOL programs. In many cases that indentation is not
representing anything semantically. In other words, IF-ELSE-IF constructs are
really just sequential cascades of prioritized mutually exclusive tests.  These
sequences bear no more  structural relationship than do sequences of imperative
statements.

Furthermore, IF-ELSE-IF expressions are frequently followed by abusive END-IF
sequences.  In a standalone statement these END-IF dragons are useless. When an
IF-ELSE-IF is imbedded within some other conditional expression, the nesting
becomes compounded, and the denesting END-IFs frequently get confused.
_Syntactically_ ELSE IF constructs are a generator of END-IF tokens,
_syntactically, ELIFs are not. This difference has a dramatic impact on the
human machine interface.

The END-IF dragon consumes valuable vertical realestate. As some generous
commentors have indicated there is a strong tendency for people to place the
ELSE and IF on two separate lines, further removing related code from a coders
focal point. An ELIF could not be placed upon two lines. There would be no
END-IF dragon on an ELIF sequence, just one little puppy, END-IF.

ELIF expressions could easily be nested inside of other conditionals. This is
actually a double benefit. Relatively simple IF-THEN-ELSE expressions are
sometimes broken into pieces because one of the branches has a IF-ELSE-IF
sequence that causes the over all structure to be hard to undersand as a result
of indentation.  An ELIF construct would actually make some of these
salvagable, reducing by a _small amount_ the need to break conditional
expressions into separate paragraphs simply because of abuse of the horizontal
attribute of the visual interface with excessive indentation.

In many cases EVALUATE is an answer to this.  But EVALUATE has serious
problems.  To begin with it is verbose, somewhat more prone to typing errors
then smaller constructs. But more importantly EVALUATE is structurally rigid. 
Your WHEN tests most have the same topology as that announced in the EVALUATE,
unless you code EVALUATE TRUE, at which point the header of the EVALUATE
dissolves to superfluidity that takes a chunk of vertical realestate and helps
reveal that the header itself always necessitates a needless increment of
indentation. 

EVALUATE is very useful. It has helped a lot.  If you agree with what it has
helped us do, why would you resist another construct that offers further help. 

EVALUATE has as its greatest strength the feature that it implies a subject for
a sequence of tests. The need for the alternative EVALAUTE TRUE syntax shows
that it is somewhat dubious when used outside of its strongest area.

There are a number of situations in which the subject or object of tests vary a
lot through a sequence. It is not rare that early test in a sequence are just
short circuit triggers. For example, if the subject is not there or not
testable as a numeric, then don't do the following tests.  Same for the object.
 Today to use EVALUATE in these situations, we have IF-ELSE-IF sequences
indenting further and further, until by the time we get to the core EVALUATE
with its extra indentation the real tests in the WHEN clauses are frequently
severely indented.  I believe ELIF would relief many of these situations of
their artificial horizontal pressure.

Also, I must add, that EVALUATE statements start simple, and get complex late
in life. They are very hard to maintain if there is a need to change the
topology of the conditionals on just one branch of many. This is especailly
true if you are committed to an early naive coding form that tries to express
the subject in the EVALUATE phrase (in contrast to the WHEN clauses). In
comparison, an individual branch of an ELIF sequence is highly modifiable,
having all the flexibility of an IF statement.

A WHEN clause is usually constrained to the shape of the world projected by the
EVALUATE phrase. 

It is not that EVALUATE is bad. We just need more.

Also I would argue that ELSE-IF is easier to teach than EVALUATE. And indeed,
that the EVALUATE construct actually trains people to think in
non-combinatorial fashion, leading to code that is broken out into many pieces
far removed from one another.

In the easiest case it is better, as in faster and more clear, to make combined
test where relevant.  In the cases that are more difficult to understand I
think we get conjunction of tests when it is irrelevant and dangerous to
combine because the EVALUATE topology makes it hard to combine in the subset
where appropriate. Thus we have patch code that starts out, AM I HERE, BUT I
SHOULDN'T BE, THEN GO TO MY-FAVORITE-EXIT. (But this latter point is involved).

In parting, let me add as an important aside, concerning stacks in the compiler
program, ELIFs would not have to be stacked as ELSE IF sequences are.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: ELIF Proposal

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3662de01.0@news1.ibm.net>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
RKRayhawk wrote in message <19981130123924.16775.00000169@ng131.aol.com>...
>>ELSE followed immediately by IF is not _syntactically_ identical to an
ELSE-IF.
>This creates a weaknesses in COBOL.
>ELIF expressions could easily be nested inside of other conditionals.

The ELIF is a good suggestion, although I would prefer the more readable
ELSE-IF

Adding to the standard now may not be a good idea because of the ensuing
delays.
But and ELSE-IF would be a welcome construct.
```

##### ↳ ↳ Re: ELIF Proposal

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981130142756.20613.00000236@ng21.aol.com>`
- **References:** `<3662de01.0@news1.ibm.net>`

```

From: "Leif Svalgaard" <leif@ibm.net>
Date: Mon, 30 Nov 1998 12:03:32 -0600
posted

<<
The ELIF is a good suggestion, although I would prefer the more readable
ELSE-IF

Adding to the standard now may not be a good idea because of the ensuing
delays.
But an ELSE-IF would be a welcome construct.
>>


Thanks for your generous comment.  There is no hurry.  COBOL's future is a
long.  

Your suggestion of ELSE-IF _is_ more readable and has the attractive feature
that it is graphically distinct, in contrast to ELIF which looks a lot like
ELSE. The tag 'ELIF' may be useful for NG discussions,being tight.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: ELIF Proposal

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eYnV4ndH#GA.123@upnetnews05>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com>`

```

RKRayhawk wrote in message <19981130142756.20613.00000236@ng21.aol.com>...
>
>From: "Leif Svalgaard" <leif@ibm.net>
…[16 more quoted lines elided]…
>Your suggestion of ELSE-IF _is_ more readable and has the attractive
feature
>that it is graphically distinct, in contrast to ELIF which looks a lot like
>ELSE. The tag 'ELIF' may be useful for NG discussions,being tight.


ELF would be even tighter, and being shorter (and more spritely), ELF would
be less likely to be confused with ELSE.  BTW, I agree that the ELSE-IF
construct should definitely be seriously investigated and favorably
considered by the COBOL Standards group, but only _after_ if finally
launches the COBOL 02000? edition.  Based on current progress and practices
of the  COBOL Standards group, I project that the follow-on standard would
come in somewhere after the year 02020.  I guess that means I view this
ELSE-IF proposal with 20/20 vision?

(The content of this response is certified  to satisfy all Y10K
requirements.)
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36652831.0@news1.ibm.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05>`

```
Dennis J. Minette wrote in message ...
>RKRayhawk wrote in message <19981130142756.20613.00000236@ng21.aol.com>...
>>From: "Leif Svalgaard" <leif@ibm.net>
…[8 more quoted lines elided]…
>>that it is graphically distinct, in contrast to ELIF which looks a lot
like
>>ELSE. The tag 'ELIF' may be useful for NG discussions,being tight.
>
…[4 more quoted lines elided]…
>launches the COBOL 02000? edition

shorter yet would be EF and it has the virtue of having the same length as
IF so that the conditions now would start in the same column:
IF cond1
    ....
EF cond2
    ...
EF cond3
    ...
.
Note, that the period here is a natural end for all the EFs.
Use of EF, ELF, or ELIF does, however, go against the
general readability (and verbosity) of Cobol.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 5)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366601BD.506E@sprynet.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
> 
> shorter yet would be EF and it has the virtue of having the same length as
…[10 more quoted lines elided]…
> general readability (and verbosity) of Cobol.

All this talk of ELSE-IF etc. is vaguely interesting, but can someone
explain to me the advantage of the above structure over the following?

EVALUATE TRUE
  WHEN cond1
        ....
  WHEN cond2
        ....
  WHEN cond3
        ....
END-EVALUATE

(other than the IF/EF taking one less line, that is...)
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 6)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3666A495.D0CF0E6E@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <366601BD.506E@sprynet.com>`

```
> All this talk of ELSE-IF etc. is vaguely interesting, but can someone
> explain to me the advantage of the above structure over the following?
…[10 more quoted lines elided]…
> (other than the IF/EF taking one less line, that is...)

Try this:

IF      A = B
    PRINT LINE-1
ELSE-IF D > E
    PRINT LINE-2
ELSE-IF D < E
    PRINT LINE-3
END-IF
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<746fqu$3jq@dfw-ixnews4.ix.netcom.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <366601BD.506E@sprynet.com> <3666A495.D0CF0E6E@home.com>`

```

Howard Brazee wrote in message <3666A495.D0CF0E6E@home.com>...
>> All this talk of ELSE-IF etc. is vaguely interesting, but can someone
>> explain to me the advantage of the above structure over the following?
…[20 more quoted lines elided]…
>END-IF

That is why the original sample used the "EVALUATE TRUE" form.  As I
indicated in an earlier note, when I code this, I often feel it is a "cop
out" - but your sample could easily be coded as:

 Evaluate True
      When   A = B
        PRINT LINE-1
      When  D > E
        PRINT LINE-2
      When  D < E
        PRINT LINE-3
END-Evaluate

Note: I intentionally did NOT make the last when a "WHEN OTHER" because of
the way the original IF was worded.  Personally, I almost never code an
EVALUATE without a WHEN OTHER - even if it is only a
   Display "You should never get here"
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 8)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3666F34E.D784D87C@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <366601BD.506E@sprynet.com> <3666A495.D0CF0E6E@home.com> <746fqu$3jq@dfw-ixnews4.ix.netcom.com>`

```
I guess it is an attempt to fix something which no longer needs fixing.

> That is why the original sample used the "EVALUATE TRUE" form.  As I
> indicated in an earlier note, when I code this, I often feel it is a "cop
…[14 more quoted lines elided]…
>    Display "You should never get here"
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 8)_

- **From:** as999@torfree.net (Adrian Boldan)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F3GCK3.HG1.0.bloor@torfree.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <366601BD.506E@sprynet.com> <3666A495.D0CF0E6E@home.com> <746fqu$3jq@dfw-ixnews4.ix.netcom.com>`

```
William M. Klein (wmklein@ix.netcom.com) wrote:

: Note: I intentionally did NOT make the last when a "WHEN OTHER" because of
: the way the original IF was worded.  Personally, I almost never code an
: EVALUATE without a WHEN OTHER - even if it is only a
:    Display "You should never get here"

I am assuming that you don't display just "You, stupid!", but also what 
the contents of the evaluated variable are...
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<743hbg$i4b$1@news.igs.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net>`

```
Leif Svalgaard wrote in message <36652831.0@news1.ibm.net>...
>EF cond2
>Note, that the period here is a natural end for all the EFs.
>Use of EF, ELF, or ELIF does, however, go against the
>general readability (and verbosity) of Cobol.


Yes, but it does go well with that classic debugging phrase ...
You know ...
WHAT? THE EF IS WRONG!
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 5)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36655262.8314FA6A@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net>`

```
> Note, that the period here is a natural end for all the EFs.
> Use of EF, ELF, or ELIF does, however, go against the
> general readability (and verbosity) of Cobol.

Amen.  We don't need to turn COBOL into C.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 6)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36660597.776C@sprynet.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <36655262.8314FA6A@home.com>`

```
Howard Brazee wrote:
> 
> > Note, that the period here is a natural end for all the EFs.
…[3 more quoted lines elided]…
> Amen.  We don't need to turn COBOL into C.

Unless my memory is really shot, C does not even have ELSE-IF or similar
construct.

Something I find interesting about C is you can do the following;

  if condition-1
      printf("condition 1 is true");
  if condition-2 && condition-3
  {
      printf("condition 1 is true");
      printf("condition 2 is true");
  }

In other words, if you only need to perform one statement when a certain
condition is true then you can do it without the beginning and ending braces.
If you want to perform multiple statements you must start with a beginning
brace and end with a closing brace.  This way you can save lines if you're
only wanting to one small thing.  A somewhat analogous example in COBOL 
would be

  if condition-1
      display "condition 1 is true".
  if condition-2 and condition-3
      display "condition 2 is true"
      display "condition 3 is true"
  end-if

But I do not do this, because I'm a "one dot per paragraph" kind of guy.

I guess the thing is, the ';' in C seems to be more like a "terminate
the statement but not the structure" kind of thing, while the '.' in COBOL
is a "terminate the statement *and* the structure."  Or something.  I guess
what I'm trying to say is, with the C example you could add another
statement to the first conditional by changing it to the following:

  if condition-1                      /* old line */
  {                                   /* new line */
      printf("condition 1 is true");  /* old line */
      dosomething();                  /* new line */
  }                                   /* new line */

You've not changed any lines, you've only added new ones.  But with the
COBOL one you have to remove the period after the display statement
and then put one after the new statement (or use and END-IF, which is
what I'd do).

Now I do realize I'm being picky, but there you have it.  

By the way, I haven't coded in C in at least five years, so I apologize
if I've screwed something up in my examples.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 7)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uDHAa3xH#GA.180@upnetnews05>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <36655262.8314FA6A@home.com> <36660597.776C@sprynet.com>`

```

Frank Swarbrick wrote in message <36660597.776C@sprynet.com>...
>Howard Brazee wrote:
>>
…[20 more quoted lines elided]…
>condition is true then you can do it without the beginning and ending
braces.
>If you want to perform multiple statements you must start with a beginning
>brace and end with a closing brace.  This way you can save lines if you're
…[27 more quoted lines elided]…
>what I'd do).

If your personal coding standards are to place _all_ periods on a separate
line you would not have any period adjustment to perform.  Some programmers
code that way because IF constructs do have a tendency to need changes as
business rules and practices change (BTW, this practice is an antecedant of
the END-whatever terminator constructs.)

>Now I do realize I'm being picky, but there you have it.
>
…[5 more quoted lines elided]…
>work: frank.swarbrick@1stbank.com
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 5)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#USW42eH#GA.214@upnetnews05>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <36652831.0@news1.ibm.net>...
>Dennis J. Minette wrote in message ...
>>RKRayhawk wrote in message <19981130142756.20613.00000236@ng21.aol.com>...
…[13 more quoted lines elided]…
>>ELF would be even tighter, and being shorter (and more spritely), ELF
would
>>be less likely to be confused with ELSE.  BTW, I agree that the ELSE-IF
>>construct should definitely be seriously investigated and favorably
…[15 more quoted lines elided]…
>


I too consider the shortening of ELSE-IF to EF, but just as ELIF is too
similar in form and length to ELSE, EF is too similar to IF in form and
length.  :-)

As you say, COBOL has thrived on (or in spite of?) verbosity, so why don't
we all just compromise on the originally proposed ELSE-IF construct?  As
some guy in L.A. once said on TV "Can't we all just get along?"
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 6)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366616E1.578F@swbell.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05>`

```
Dennis J. Minette wrote:

[snip] 

> I too consider the shortening of ELSE-IF to EF, but just as ELIF is too
> similar in form and length to ELSE, EF is too similar to IF in form and
…[4 more quoted lines elided]…
> some guy in L.A. once said on TV "Can't we all just get along?"

The spelling "ELSE-IF" is a standing invitation to bugs.  Consider
the following snippet:

    IF FOOBAR = "A"
       PERFORM A-ROUTINE
    ELSE-IF FOOBAR = "B"
       PERFORM B-ROUTINE
    END-IF
    PERFORM DO-SOMETHING-ELSE
    .

In this case the last PERFORM occurs unconditionally, no matter
what FOOBAR is.  But if my fingers misbehave I get:

    IF FOOBAR = "A"
       PERFORM A-ROUTINE
    ELSE IF FOOBAR = "B"
       PERFORM B-ROUTINE
    END-IF
    PERFORM DO-SOMETHING-ELSE
    .

All I did was leave out the hyphen.  The compiler won't complain,
and my eyeballs probably won't complain either, but the logic is
completely different.  The last PERFORM will occur only if FOOBAR
is not "A".

The spelling "ELSIF" would be much less error-prone because it 
would take two typos instead of one to keep the compiler from
complaining.  Unlike "ELIF" it is visually distinct, by reason of 
its length, from "ELSE".

This argument assumes that the scope terminator would be END-IF.
If ELSE-IF had to be terminated by (for instance) END-ELSE-IF,
then the second version would be a syntax error.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 6)_

- **From:** cadams@acucorp.com (Chris Adams)
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36657d96.168710913@news.acucorp.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05>`

```
On Wed, 2 Dec 1998 07:15:50 -0500, "Dennis J. Minette"
<dennis_minette@email.msn.com> wrote:

>As you say, COBOL has thrived on (or in spite of?) verbosity, so why don't
>we all just compromise on the originally proposed ELSE-IF construct?  As

The other nice thing about this is that it makes life easier when switching
versions. If you use an older compiler primarily and suddenly switch to the New
& Improved version, you aren't going to have to wonder just what the keyword for
"ELSE-IF" is. Contrast this with the minor insanity that can creep in if you're
regularly working with C, C++ and Java (or Java and JavaScript) where some
things look very similar but can behave slightly differently at times. The
language can be terse enough that you won't always be reminded of the
difference. COBOL has enough verbosity to keep this from happening anywhere near
as often.

Unless someone is an unusually slow typist, I can't see the verbosity costing
much extra time since the keyboard is rarely the bottleneck. Besides, most
people in this group probably have COBOL keywords memorized at the reflex level
anyway...


# Chris Adams <cadams@acucorp.com> <adamsc@ibm.net>
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 7)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ewBuzUvH#GA.161@upnetnews05>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com>`

```

Chris Adams wrote in message <36657d96.168710913@news.acucorp.com>...
>On Wed, 2 Dec 1998 07:15:50 -0500, "Dennis J. Minette"
><dennis_minette@email.msn.com> wrote:
…[5 more quoted lines elided]…
>versions. If you use an older compiler primarily and suddenly switch to the
New
>& Improved version, you aren't going to have to wonder just what the
keyword for
>"ELSE-IF" is. Contrast this with the minor insanity that can creep in if
you're
>regularly working with C, C++ and Java (or Java and JavaScript) where some
>things look very similar but can behave slightly differently at times. The
>language can be terse enough that you won't always be reminded of the
>difference. COBOL has enough verbosity to keep this from happening anywhere
near
>as often.
>
>Unless someone is an unusually slow typist, I can't see the verbosity
costing
>much extra time since the keyboard is rarely the bottleneck. Besides, most
>people in this group probably have COBOL keywords memorized at the reflex
level
>anyway...
>
>
># Chris Adams <cadams@acucorp.com> <adamsc@ibm.net>

I agree that too many synonyms, as well as an excess of "allowed but not
required" COBOL reserved words is not necessarily "a good thing."

I've actually seen (heard?) heated arguments among COBOL programmers as to
whether the figurative constant ZERO or ZEROS or ZEROES is the 'preferred'
term for elegant usage.  But the correct answer here seems to be 'whatever
floats your boat.'
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 8)_

- **From:** cadams@acucorp.com (Chris Adams)
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36672074.275940471@news.acucorp.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05>`

```
On Wed, 2 Dec 1998 19:46:32 -0500, "Dennis J. Minette"
<dennis_minette@email.msn.com> wrote:

>I've actually seen (heard?) heated arguments among COBOL programmers as to
>whether the figurative constant ZERO or ZEROS or ZEROES is the 'preferred'
>term for elegant usage.  But the correct answer here seems to be 'whatever
>floats your boat.'

How about the wars over whether = is preferable to EQUAL? Or whether you should
include the optional parts like IS. Some people have *way* too much spare time!

# Chris Adams <cadams@acucorp.com> <adamsc@ibm.net>
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 9)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uh6nY3xH#GA.123@upnetnews05>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com>`

```

Chris Adams wrote in message <36672074.275940471@news.acucorp.com>...
>On Wed, 2 Dec 1998 19:46:32 -0500, "Dennis J. Minette"
><dennis_minette@email.msn.com> wrote:
…[6 more quoted lines elided]…
>How about the wars over whether = is preferable to EQUAL? Or whether you
should
>include the optional parts like IS. Some people have *way* too much spare
time!
>
># Chris Adams <cadams@acucorp.com> <adamsc@ibm.net>

I personally prefer to use = instead of EQUAL so an argument of using IS
with it is wasted on me.  But, to some people, IS _is_ important, "depending
on what your definition of IS is."  You might recognize the quote - it is
from the Chief Semanticist of the United States.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 10)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-LyZ8rUzS01SF@Dwight_Miller.iix.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <uh6nY3xH#GA.123@upnetnews05>`

```
On Fri, 4 Dec 1998 00:22:19, "Dennis J. Minette" 
<dennis_minette@email.msn.com> wrote:


> I personally prefer to use = instead of EQUAL so an argument of using IS
> with it is wasted on me.  But, to some people, IS _is_ important, "depending
…[3 more quoted lines elided]…
> 

At my prior place of employment they used EQUAL instead of = ... why? 
Because the print band did not have an = on it and when you printed 
the listing.......



-------------------------
Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 11)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3668B000.3064D173@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <uh6nY3xH#GA.123@upnetnews05> <Jl0PnHJ5PvPd-pn2-LyZ8rUzS01SF@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
(snip)
> 
> At my prior place of employment they used EQUAL instead of = ... why?
> Because the print band did not have an = on it and when you printed
> the listing.......

But how long ago was this? And what kind of shop (my IBM mainframe
background may be peeking thru here, again. This hasn't been an issue in
IBM mainframe shops since the late 60's)?

FWIW, I'm voting for "=", "<", ">", "<=", ">=", etc.

Bill Lynch
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 12)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#ISSlQBI#GA.328@upnetnews03>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <uh6nY3xH#GA.123@upnetnews05> <Jl0PnHJ5PvPd-pn2-LyZ8rUzS01SF@Dwight_Miller.iix.com> <3668B000.3064D173@att.net>`

```

William Lynch wrote in message <3668B000.3064D173@att.net>...
>Thane Hubbell wrote:
>>
…[12 more quoted lines elided]…
>Bill Lynch

I'm voting with you on that, Bill. Spelling out EQUAL or LESS or GREATER is
just sooo much extra work for no extra benefit. <g>
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 13)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981206181800.29937.00001121@ngol08.aol.com>`
- **References:** `<#ISSlQBI#GA.328@upnetnews03>`

```

>>FWIW, I'm voting for "=", "<", ">", "<=", ">=", etc.

On one print train on our 3203 printer we did not have the < or > characters,
which meant that either one had to go back to the cards (yes, we did all our
programming on cards in those days, as did our students), or not use < or >
characters. This was awkward in particular with BASIC programs.

When we got our 3203-5 printer, instead of having the characterset repeated 5
times, we got one where the characterset was repeated only 4 times, but had
more characters, including < and >. That made quite an improvement helping
BASIC students!

Mark A. Young
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 13)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366A5453.DF31A324@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <uh6nY3xH#GA.123@upnetnews05> <Jl0PnHJ5PvPd-pn2-LyZ8rUzS01SF@Dwight_Miller.iix.com> <3668B000.3064D173@att.net> <#ISSlQBI#GA.328@upnetnews03>`

```
"Dennis J. Minette" wrote:
> 
(snip)
> >FWIW, I'm voting for "=", "<", ">", "<=", ">=", etc.
> >
…[3 more quoted lines elided]…
> just sooo much extra work for no extra benefit. <g>

What's all this I hear about COBOL's being verbose?

Bill Lynch <G>
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 13)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366BE9ED.D45A44F5@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <uh6nY3xH#GA.123@upnetnews05> <Jl0PnHJ5PvPd-pn2-LyZ8rUzS01SF@Dwight_Miller.iix.com> <3668B000.3064D173@att.net> <#ISSlQBI#GA.328@upnetnews03>`

```
> >But how long ago was this? And what kind of shop (my IBM mainframe
> >background may be peeking thru here, again. This hasn't been an issue in
> >IBM mainframe shops since the late 60's)?

I worked in a shop with multiple IBM printers in 1980, one of the
printers had problems with this.

Another reason is that if you were a bit sloppy in your coding sheets,
the key punch operators might not get what you wanted.  Words were
clearer.

> >FWIW, I'm voting for "=", "<", ">", "<=", ">=", etc.
> >
…[3 more quoted lines elided]…
> just sooo much extra work for no extra benefit. <g>

The trouble is, if you aren't a good typist EVERYTHING is more work now
that we all use keyboards.  And if you are a good typest, spelling out
words is easier than using symbols which might be in different places on
different keyboards.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 14)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3670a2ab.171710983@netnews>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <uh6nY3xH#GA.123@upnetnews05> <Jl0PnHJ5PvPd-pn2-LyZ8rUzS01SF@Dwight_Miller.iix.com> <3668B000.3064D173@att.net> <#ISSlQBI#GA.328@upnetnews03> <366BE9ED.D45A44F5@home.com>`

```
'Twas Mon, 07 Dec 1998 07:45:01 -0700, when Howard Brazee
<NOSPAMbrazee@home.com> illuminated comp.lang.cobol thusly:

>> >FWIW, I'm voting for "=", "<", ">", "<=", ">=", etc.
>> >
…[8 more quoted lines elided]…
>different keyboards.

On a Dvorak keyboard most of the letters are in different locations from a
QWERTY keyboard, so let's not use any of those letters.

<, >, and = are pretty consistantly located.
```

###### ↳ ↳ ↳ Syntax wars

_(reply depth: 9)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667F2A9.3A8B3647@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com>`

```
> How about the wars over whether = is preferable to EQUAL? Or whether you should
> include the optional parts like IS. Some people have *way* too much spare time!

I once was in a shop which had a printer which couldn't print ">".  So
the shop standard was to spell it out.  I was glad I wasn't using ALGOL!
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 10)_

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367D00E0.37DA@bellsouth.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com>`

```
Howard Brazee wrote:
> 
> > How about the wars over whether = is preferable to EQUAL? Or whether you should
…[3 more quoted lines elided]…
> the shop standard was to spell it out.  I was glad I wasn't using ALGOL!

Our printer also doesn't print =, >, or <.  It's become such an
ingrained habit to write out these words, I'm afraid I'd be struck by
lightening if I didn't.
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 11)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367D7B19.6BF930D9@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net>`

```
Kitty Carr wrote:
> 
> Howard Brazee wrote:
…[9 more quoted lines elided]…
> lightening if I didn't.

Even in 1998? I'm truly amazed. BTW, what sort of printer do you have /
what else doesn't your printer have?

Bill Lynch
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 12)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75khns$7vm$1@news.igs.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net>`

```
She's a fed, Bill.  Her printer only gets a CPU on Tuesdays,
Thursdays, and every other Sunday afternoon ...

William Lynch wrote in message <367D7B19.6BF930D9@att.net>...
>Kitty Carr wrote:
>>
>> Howard Brazee wrote:
>> >
>> > > How about the wars over whether = is preferable to EQUAL? Or whether
you should
>> > > include the optional parts like IS. Some people have *way* too much
spare time!
>> >
>> > I once was in a shop which had a printer which couldn't print ">".  So
>> > the shop standard was to spell it out.  I was glad I wasn't using
ALGOL!
>>
>> Our printer also doesn't print =, >, or <.  It's become such an
…[6 more quoted lines elided]…
>Bill Lynch
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 13)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367F1097.147A09C9@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net>`

```
Donald Tees wrote:
> 
> She's a fed, Bill.  Her printer only gets a CPU on Tuesdays,
> Thursdays, and every other Sunday afternoon ...
> 
One word: OY

Bill Lynch L-)
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 13)_

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3680473E.693D@bellsouth.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net>`

```
Donald Tees wrote:
> 
> She's a fed, Bill.  Her printer only gets a CPU on Tuesdays,
…[23 more quoted lines elided]…
> >Bill Lynch

We have two IBM printers, a 3203 and 4245, at least that's what's
faintly etched on their fronts.  What?  They're old?  But I'm sure they
were manufactured during my lifetime.  I don't know what other
characters they don't print, but I do know they give off invisible rays
that cause all male programmers to slink away when it's time to change
the paper.  Now THAT'S amazing!
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 14)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36806AA2.E7D0AEDD@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net>`

```
Kitty Carr wrote:
> 
(snip)
> > >Even in 1998? I'm truly amazed. BTW, what sort of printer do you have /
> > >what else doesn't your printer have?
…[4 more quoted lines elided]…
> faintly etched on their fronts.

3203 & 4245, right. I think my grandpa had stories about those beasts.

Bill Lynch <g>
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 14)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36806d6c.51560091@news1.ibm.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net>`

```
On Wed, 23 Dec 1998 01:38:04 GMT, Kitty Carr <kcarr1@bellsouth.net>
wrote:


>
>We have two IBM printers, a 3203 and 4245, at least that's what's
…[4 more quoted lines elided]…
>the paper.  Now THAT'S amazing!

I like the note about programmers changing the paper.  

BTW:  I'll be the second highest paid tape drive operator next year.
I think the financial "Crunch" that will/is occuring is going to
impact operations the most.
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 15)_

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-b0jkENtUygeh@dsm4merlin.iix.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net> <36806d6c.51560091@news1.ibm.net>`

```
On Wed, 23 Dec 1998 04:12:48, redsky@ibm.net (Thane Hubbell) wrote:

> I like the note about programmers changing the paper.  
>  
Yep, that was cute - I'll have to pass it on to Mom, if you haven't 
already.

> BTW:  I'll be the second highest paid tape drive operator next year.
> I think the financial "Crunch" that will/is occuring is going to
> impact operations the most.
> 
With me being the first, I suppose?

It is going to be a real bear the first time Frozen Dave wants an SPL 
set mailed somewhere! (YHWH help us when we need a backup!)
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 14)_

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16E3CD41C4A29C70.3BDD9195997E68BC.4B907D33DC95B755@library-proxy.airnews.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net>`

```
Kitty Carr wrote:
(snip) 
> I do know they give off invisible rays
> that cause all male programmers to slink away when it's time to change
> the paper.  Now THAT'S amazing!

Kitty,

This is not a new phenomenon.  The same rays are emitted at our office
by all sorts of devices:  The copier, the coffee pot, and the ice cube
trays in the freezer to name a few.   :)
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 15)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3681044a.4799015@news.enter.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net> <16E3CD41C4A29C70.3BDD9195997E68BC.4B907D33DC95B755@library-proxy.airnews.net>`

```
"David W. Furin" <dfurin@larich.com> wrote:

>Kitty Carr wrote:
>(snip) 
…[13 more quoted lines elided]…
>LaRich Distributors, Inc.     | web:    http://www.larich.com


David:

You forgot to mention the most concentrated sterilization rays which
are emitted when one lowers the toilet seat.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 14)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36812957.0@news3.uswest.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net>`

```
Kitty Carr wrote in message <3680473E.693D@bellsouth.net>...
>Donald Tees wrote:
>>
…[8 more quoted lines elided]…
>> >> > > How about the wars over whether = is preferable to EQUAL? Or
whether
>> you should
>> >> > > include the optional parts like IS. Some people have *way* too
much
>> spare time!
>> >> >
>> >> > I once was in a shop which had a printer which couldn't print ">".
So
>> >> > the shop standard was to spell it out.  I was glad I wasn't using
>> ALGOL!
…[15 more quoted lines elided]…
>the paper.  Now THAT'S amazing!


Programmers?  Change paper?  That's an operator's job!
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 15)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3681D945.64498600@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <75khns$7vm$1@news.igs.net> <3680473E.693D@bellsouth.net> <36812957.0@news3.uswest.net>`

```
Chris Osborne wrote:
> 
(snip)
> We have two IBM printers, a 3203 and 4245, at least that's what's
> >faintly etched on their fronts.  What?  They're old?  But I'm sure they
…[5 more quoted lines elided]…
> Programmers?  Change paper?  That's an operator's job!

Not if the printers are on the same floor as the programmers, e.g.,
15-East, and the computer operators are on the 3rd floor. Programmers
don't change paper, programmers don't get their printed output (not
always a bad thing, BTW).

Bill Lynch
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 12)_

- **From:** Clifton Ivy <clif@purdue.edu>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36812321.11E044D9@purdue.edu>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net>`

```
Hm-m-m...

This is almost like why nearly all of the mainframe systems in our shop
are set up to allow **only** upper-case data in them.  They do this by
setting a CICS option to automatically convert all data from "terminals"
from lower case to upper case.

The reason was that our **printers** used a physical chain (train, loop)
of type characters that whirled around in front of the paper.  There
were individual "hammers" for each print column; when the proper
character came by, the hammer whacked it (as it flew past -- this
boggles the mind!).

At any rate, the "upper case only" print chain had more repeats of the
letters than the "upper / lowe case" print chain, so the "proper
character" came by more often.  Therefore, upper case output printed
faster than mixed case output!

This difference was significant, especially when you were printing
gazillions of pages per month.

Now, of course, with laser printers, it doesn't matter.  But people are
still afraid of mixed-case systems -- they just don't remember why!

William Lynch wrote:
> 
> Kitty Carr wrote:
snip...
> > Our printer also doesn't print =, >, or <.  It's become such an
> > ingrained habit to write out these words, I'm afraid I'd be struck by
…[5 more quoted lines elided]…
> Bill Lynch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
They're just my opinions...
Clifton Ivy, Mgmt Info, Purdue University
clif@purdue.edu
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 13)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36816F7D.3AC20289@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <36812321.11E044D9@purdue.edu>`

```
> This difference was significant, especially when you were printing
> gazillions of pages per month.
> 
> Now, of course, with laser printers, it doesn't matter.  But people are
> still afraid of mixed-case systems -- they just don't remember why!

I remember those days.  But I am still afraid of mixed-case systems
because there is a huge pool of programs which were not written with
mixed case data in mind.

There are several ways to handle the following:
      IF INPUT-LAST-NAME = MIXED-CASE-LAST-NAME PERFORM FOUND-ONE.
But I would love to have one or more COBOL enhancement to make this
easier.

At any rate, lots of programs will break by careless allowing data entry
of mixed case.
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 14)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3681c5b4.74426615@netnews>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <36812321.11E044D9@purdue.edu> <36816F7D.3AC20289@home.com>`

```
'Twas Wed, 23 Dec 1998 15:32:29 -0700, when Howard Brazee
<NOSPAMbrazee@home.com> illuminated comp.lang.cobol thusly:

>I remember those days.  But I am still afraid of mixed-case systems
>because there is a huge pool of programs which were not written with
…[5 more quoted lines elided]…
>easier.

IF  FUNCTION UPPER-CASE (INPUT-LAST-NAME) = 
        FUNCTION UPPER-CASE (MIXED-CASE-LAST-NAME)
    PERFORM FOUND-ONE.

Standard Cobol since 1989.
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 15)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36823461.2B535CA3@IMN.nl>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <36812321.11E044D9@purdue.edu> <36816F7D.3AC20289@home.com> <3681c5b4.74426615@netnews>`

```
Randall Bart wrote:
8<

> IF  FUNCTION UPPER-CASE (INPUT-LAST-NAME) =
>         FUNCTION UPPER-CASE (MIXED-CASE-LAST-NAME)
>     PERFORM FOUND-ONE.

or
IF FUNCTION LOWER-CASE (INPUT-LAST-NAME) =
        FUNCTION LOWER-CASE (MIXED-CASE-LAST-NAME)

> Standard Cobol since 1989.

The Frog
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 15)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36824B3E.A7C8D693@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <36812321.11E044D9@purdue.edu> <36816F7D.3AC20289@home.com> <3681c5b4.74426615@netnews>`

```
Randall Bart wrote:
> 
> 'Twas Wed, 23 Dec 1998 15:32:29 -0700, when Howard Brazee
…[15 more quoted lines elided]…
> Standard Cobol since 1989.

Standard Cobol since 1989 doesn't mean that most Cobol programs
programmed since 1989 use that standard compiler.  So when we allow data
entry of mixed case, lots of programs need to be changed to have that
function placed in their comparisons.

When I said "easier", I was thinking more in the lines of something I
could put in a compiler or a copylib   LNAME PIC X(25) USAGE IS
UPPER-CASE, and recompile.

That's why most shops simply convert your input to upper case - they
don't want to go through Y2K type analysis through all the code.
```

###### ↳ ↳ ↳ Re: Syntax wars

_(reply depth: 14)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3681DA8F.B4D4121D@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <36672074.275940471@news.acucorp.com> <3667F2A9.3A8B3647@home.com> <367D00E0.37DA@bellsouth.net> <367D7B19.6BF930D9@att.net> <36812321.11E044D9@purdue.edu> <36816F7D.3AC20289@home.com>`

```
Howard Brazee wrote:
> 
(snip)
> 
> At any rate, lots of programs will break by careless allowing data entry
> of mixed case.

While this is certainly true, it's not the issue here. We started by
discussing the pros & cons of coding ">", "<", "=", etc., vs. "(IS)
GREATER (THAN)", "(IS) LESS (THAN)", "(IS) EQUAL (TO)", etc. Our most
recent standard for application screens is for the map (BMS) legends (or
text fields) to be mixed case, while the data supplied by the software
is upper case, e.g.:

	Security Description: IBM COMMON STOCK

Bill Lynch
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 8)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74781b$o5k$1@news.igs.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05>`

```
Dennis J. Minette wrote in message ...

>I've actually seen (heard?) heated arguments among COBOL programmers as to
>whether the figurative constant ZERO or ZEROS or ZEROES is the 'preferred'
>term for elegant usage.  But the correct answer here seems to be 'whatever
>floats your boat.'


Don't be silly.  Everybody knows that you move ZERO
to a PICTURE 9 field, and ZEROS to anything larger.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 9)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-TdzHObMud8Pe@Dwight_Miller.iix.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net>`

```
On Thu, 3 Dec 1998 23:55:08, "Donald Tees" <donald@willmack.com> 
wrote:

> Dennis J. Minette wrote in message ...
> 
…[7 more quoted lines elided]…
> to a PICTURE 9 field, and ZEROS to anything larger.

I don't have a problem with that, but when should one use ZEROES?
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 10)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<749f1n$4dm$1@news.igs.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-TdzHObMud8Pe@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Thu, 3 Dec 1998 23:55:08, "Donald Tees" <donald@willmack.com>
>wrote:
…[3 more quoted lines elided]…
>> >I've actually seen (heard?) heated arguments among COBOL programmers as
to
>> >whether the figurative constant ZERO or ZEROS or ZEROES is the
'preferred'
>> >term for elegant usage.  But the correct answer here seems to be
'whatever
>> >floats your boat.'
>>
…[4 more quoted lines elided]…
>I don't have a problem with that, but when should one use ZEROES?

When you visit Britain.


>
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 10)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981205004831.06806.00001138@ngol06.aol.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-TdzHObMud8Pe@Dwight_Miller.iix.com>`

```

In article <Jl0PnHJ5PvPd-pn2-TdzHObMud8Pe@Dwight_Miller.iix.com>,
redsky@ibm.net (Thane Hubbell) writes:

>I don't have a problem with that, but when should one use ZEROES?

I use ZERO for moving to a single-digit/single byte position, and ZEROES for
moving to multi-digit or multi-byte positions.

I never use ZEROS.

Mark A. Young
```

###### ↳ ↳ ↳ ZERO or ZEROS or ZEROES

_(reply depth: 9)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667d1bb.180873407@netnews>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net>`

```
'Twas Thu, 3 Dec 1998 18:55:08 -0500, when "Donald Tees"
<donald@willmack.com> illuminated comp.lang.cobol thusly:

>Dennis J. Minette wrote in message ...
>
…[7 more quoted lines elided]…
>to a PICTURE 9 field, and ZEROS to anything larger.

For PIC 9 or PIC X use ZERO
For PIC 9(n) use ZEROS
For PIC X(n) use ZEROES
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 10)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<748ou1$mjs$1@news.igs.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews>`

```
Randall Bart wrote in message <3667d1bb.180873407@netnews>...
>
>For PIC 9 or PIC X use ZERO
>For PIC 9(n) use ZEROS
>For PIC X(n) use ZEROES


Naw, for PIC X(n) (PICTURE X(n) that is), use ALL "0".
;<)
Funny how everybody has their idiosynchracies.  I hate seeing
PIC.  To me, it falls right beside using X as a data name ... I
hear old data processing pro's nagging me about lazy typing
habits, meaningful names, and shortcuts making long delays.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 11)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667FD03.9F81F22A@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net>`

```
> Naw, for PIC X(n) (PICTURE X(n) that is), use ALL "0".
> ;<)
…[3 more quoted lines elided]…
> habits, meaningful names, and shortcuts making long delays.


I converted some small Burroughs code to run on a large Burroughs
machine once.  One change was to change PC  to PIC .   And then check to
make sure we didn't move a period to column 73.   What a rediculous
keystroke saver PC ?!?!?!
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mAwb2.10706$Jl.3836679@news3.mia>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com>`

```
Howard Brazee wrote:
>
>I converted some small Burroughs code to run on a large Burroughs
>machine once.  One change was to change PC  to PIC .   And then check to
>make sure we didn't move a period to column 73.   What a rediculous
>keystroke saver PC ?!?!?!

Wow, that must have been a long time ago, Howard.  IIRC, PC was removed
in the Burroughs COBOL 68 compilers.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 13)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3670a359.171884986@netnews>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia>`

```
'Twas Wed, 09 Dec 1998 15:21:54 GMT, when "Judson McClendon"
<judmc123@bellsouth.net> illuminated comp.lang.cobol thusly:

>Howard Brazee wrote:
>>
…[6 more quoted lines elided]…
>in the Burroughs COBOL 68 compilers.

All the Burroughs Medium System Cobol 68 compilers accepted PC for
PICTURE, VA for VALUE and OC for OCCURS.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wt8c2.2810$CE2.1126222@news4.mia>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews>`

```
Randall Bart wrote:
>
>All the Burroughs Medium System Cobol 68 compilers accepted PC for
>PICTURE, VA for VALUE and OC for OCCURS.

I don't think so.  I was in the Air Force from May 1968 to May 1972 and I
very clearly and distinctly remember having to convert many programs which
used PC to PIC and OC to OCCURS, because the new compiler would not accept
it.  Since I left in 1972, there is no way this was for COBOL 74; it must
have been for COBOL 68.  I suppose it is possible that the Air Force had a
special version of COBOL 68, since they bought 150 B2500/B3500 computers,
but I doubt it.  I kept the MCP listings for our section, and it was the
standard MCP.  U.S. Steel had a modified MCP which I did some debugging on,
but not the USAF, at least for normal base level processing.  No telling
what they had for specialized stuff. :-)

Thinking about the B3500 MCP reminds me of an old anecdote. :-)  When I
was a Burroughs systems tech, my major account had a B3500, which was core
memory.  They had a couple of long jobs running that had been in the mix
for several hours and would be running for several more, and the engineers
needed to take the system down for a few minutes.  Since core memory is
non volatile, I tool down the online, stopped the long running programs so
the MCP would go into its interrupt wait loop, took down all the CPU data
from the console and powered down the system.  The engineers did their
thing, I powered up the system, restored the CPU state, restarted the MCP
in the wait loop, did a GO on the stopped programs.  We restarted the
online system and loaded up the system again.  It ran until all the long
jobs had completed, and we rebooted.  That incident is still a legend
around here. :-)
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74rkea$39j$1@mail.pl.unisys.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <Wt8c2.2810$CE2.1126222@news4.mia>`

```
There were several "flavors" of Medium System COBOL(68) compilers (COBOL,
COBOLL, COBOLV all come to mind).  Perhaps this was a migration from one to
another (most likely to COBOLV, which,. if I recall, was the last of the
three).

    -Chuck Stevens


Judson McClendon wrote in message ...
>Randall Bart wrote:
>>
…[34 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 15)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3673392c.36868680@netnews>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <Wt8c2.2810$CE2.1126222@news4.mia>`

```
'Twas Fri, 11 Dec 1998 12:45:42 GMT, when "Judson McClendon"
<judmc123@bellsouth.net> illuminated comp.lang.cobol thusly:

>Randall Bart wrote:
>>
…[12 more quoted lines elided]…
>what they had for specialized stuff. :-)

Let me just say all I know and then some.  Originally there were two
compilers which ran on Medium Systems:  COBOL and LCOBOL.  COBOL produced
native code, while LCOBOL produced B700 code.  They were very similar
dialects of COBOL, and they were not compliant with ANSI X3.23-1968.  They
included PC as an abbreviation for PICTURE, which saved four keystrokes
(not one, as some have insinuated).  Then they wrote COBOLL which was
supposed to be ANSI 68, so it included PIC as an abbreviation for PICTURE,
and judging by your story did not include PC.  Typically Burroughs wrote
ANSI compliant compilers to get government contracts, and you may have
been one of the early users of that compiler.  Then in a later release
they added PC to make it easier for users to migrate from COBOL to COBOLL.
COBOLV supported all the same syuntax as COBOLL.  There was a later
compiler called COBOL which was written to ANSI X3.23-1974, and didn't
support all those Burrousghs extensions.  AFAIK, PC, VA, and OC never made
it into any Burroughs Cobol-74 compilers.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 16)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AwRc2.5476$xx1.997608@news3.mia>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <Wt8c2.2810$CE2.1126222@news4.mia> <3673392c.36868680@netnews>`

```
Randall Bart wrote:
>
>Let me just say all I know and then some.  Originally there were two
…[13 more quoted lines elided]…
>it into any Burroughs Cobol-74 compilers.

Sounds plausible to me. :-)
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 16)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36769352.32677CE1@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <Wt8c2.2810$CE2.1126222@news4.mia> <3673392c.36868680@netnews>`

```
They
> included PC as an abbreviation for PICTURE, which saved four keystrokes
> (not one, as some have insinuated). 

Four?  I don't see it.  PC saves 1 over the standard PIC, and saves 5
over the spelled out PICTURE.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 17)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367744fa.6320494@netnews>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <Wt8c2.2810$CE2.1126222@news4.mia> <3673392c.36868680@netnews> <36769352.32677CE1@home.com>`

```
'Twas Tue, 15 Dec 1998 09:50:26 -0700, when Howard Brazee
<NOSPAMbrazee@home.com> illuminated comp.lang.cobol thusly:

>>They
>> included PC as an abbreviation for PICTURE, which saved four keystrokes
…[3 more quoted lines elided]…
>over the spelled out PICTURE.

Sorry, I cain't count.  PC saves 5 over PICTURE.  How many PC saves over
PIC wasn't an issue, the early Cobols had only PICTURE.  Some compilers
started offering abbrevs for PICTURE, Burroughs happened to pick PC, but
ANSI adopted PIC.  That was why Judson was stuck changing PC to PIC in
1972.  But trying to convince coders they should use just one character
more was a difficult sell, so PC found its way into all the Medium System
and Small System Cobol-68 compilers.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 14)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367137F8.B07B4091@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews>`

```
Randall Bart wrote:
> 
> 'Twas Wed, 09 Dec 1998 15:21:54 GMT, when "Judson McClendon"
…[10 more quoted lines elided]…
> >in the Burroughs COBOL 68 compilers.

This was in 1980.
 
> All the Burroughs Medium System Cobol 68 compilers accepted PC for
> PICTURE, VA for VALUE and OC for OCCURS.

I had to change those also.  But OC saves 4 keystrokes, VA saves 3, but
PC saves only 1.  Adding an incompatibility to save 1 keystroke (and
making it harder to read) is not worth it.  (sure I know PIC is widely
used in a program, and in the days of coding sheets, we couldn't cut and
paste, but still)
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 15)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OitF5$SJ#GA.85@upnetnews03>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <367137F8.B07B4091@home.com>`

```

Howard Brazee wrote in message <367137F8.B07B4091@home.com>...
>Randall Bart wrote:
>>
…[6 more quoted lines elided]…
>> >>machine once.  One change was to change PC  to PIC .   And then check
to
>> >>make sure we didn't move a period to column 73.   What a rediculous
>> >>keystroke saver PC ?!?!?!
…[13 more quoted lines elided]…
>paste, but still)

That was then, this is now.  Think about the relative costs of memory and
storage circa 1968, Howard.  That was probably the justification for those
cited COBOL abbreviations implemented in Burroughs compilers 3 decades ago.
I do agree that such practices are no longer acceptable.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 16)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367191CF.A9A2AC0E@home.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <367137F8.B07B4091@home.com> <OitF5$SJ#GA.85@upnetnews03>`

```
Dennis J. Minette wrote:

> >I had to change those also.  But OC saves 4 keystrokes, VA saves 3, but
> >PC saves only 1.  Adding an incompatibility to save 1 keystroke (and
…[7 more quoted lines elided]…
> I do agree that such practices are no longer acceptable.

I don't get it.  This is source code stored on 80 column images.  It
takes just as much space to store an 80 column image with "PC" on it as
"PIC" on it.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 17)_

- **From:** Scott Ramey <scottr@bdssoftware.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3671C909.1EFF4B2B@bdssoftware.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <367137F8.B07B4091@home.com> <OitF5$SJ#GA.85@upnetnews03> <367191CF.A9A2AC0E@home.com>`

```


Howard Brazee wrote:
> 
> Dennis J. Minette wrote:
…[14 more quoted lines elided]…
> "PIC" on it.

Maybe it was out of consideration of programmers doing two finger
typing.  Back then most programmers back then didn't type worth a hoot. 
Maybe it was marketing thinking this would be a neat sales gimmick:  "We
give you the whole picture in just 2 keystrokes!
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 18)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74sis2$5d$1@news.igs.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <367137F8.B07B4091@home.com> <OitF5$SJ#GA.85@upnetnews03> <367191CF.A9A2AC0E@home.com> <3671C909.1EFF4B2B@bdssoftware.com>`

```
Scott Ramey wrote in message <3671C909.1EFF4B2B@bdssoftware.com>...

>Maybe it was out of consideration of programmers doing two finger
>typing.  Back then most programmers back then didn't type worth a hoot.
>Maybe it was marketing thinking this would be a neat sales gimmick:  "We
>give you the whole picture in just 2 keystrokes!

Naw, every programmer worth their salt had a drum card made up
with "PICTURE " set to auto-dupe in column 45 or so ... even card
punches allowed you to cut and paste (after a fashion) ... and that
required only *one* keystroke, including the "tabs".

BTW, I STILL two finger type ... after thirty years, though, I can
do it in the dark at about 75 words per minute.  But only if I don't
think about it.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 19)_

- **From:** Scott Ramey <scottr@bdssoftware.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3671D869.2E3F476@bdssoftware.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews> <367137F8.B07B4091@home.com> <OitF5$SJ#GA.85@upnetnews03> <367191CF.A9A2AC0E@home.com> <3671C909.1EFF4B2B@bdssoftware.com> <74sis2$5d$1@news.igs.net>`

```


Donald Tees wrote:
> 
> Scott Ramey wrote in message <3671C909.1EFF4B2B@bdssoftware.com>...
…[9 more quoted lines elided]…
> required only *one* keystroke, including the "tabs".

Which reminds me of a "girl friend" I had who marveled that I could
program an 029.  
I figured with such admiration I ought to be able to program her and
punch a few more holes (not square ones) but it didn't work out that
way.

> 
> BTW, I STILL two finger type ... after thirty years, though, I can
> do it in the dark at about 75 words per minute.  But only if I don't
> think about it.

So could my dad, I was always amazed.  Talk about fists of fury.

When I was in college I typed freight bills at night on a teletype
machines, the old four level mechanical monstrosities with three rows of
keys that you had to shift in/out for numbers, etc.  I had rhythm, I had
speed.  Since then I got married and my wife took away my rhythm rating
after our first dance -- but I still got speed.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 14)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74rk6p$392$1@mail.pl.unisys.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <748ou1$mjs$1@news.igs.net> <3667FD03.9F81F22A@home.com> <mAwb2.10706$Jl.3836679@news3.mia> <3670a359.171884986@netnews>`

```
So did the Burroughs B1000-series COBOL (68) compiler (which was modelled on
the Medium System compiler), and I believe also the B700 and L-series COBOL
cross-compilers that ran on Medium Systems (the B700 compiler was ultimately
made available as an "on-board" product, but it was excruciatingly slow; our
local  users used it only as a last resort when they could not get local
Medium System time).

    -Chuck Stevens


Randall Bart wrote in message <3670a359.171884986@netnews>...
>'Twas Wed, 09 Dec 1998 15:21:54 GMT, when "Judson McClendon"
><judmc123@bellsouth.net> illuminated comp.lang.cobol thusly:
…[21 more quoted lines elided]…
>l    |/ MS^7=6/28/107   http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 10)_

- **From:** wobconsult@sprynet.com
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74a5db$bvq$1@nnrp1.dejanews.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews>`

```
In article <3667d1bb.180873407@netnews>,
  Barticus@att.spam.net (Randall Bart) wrote:
> 'Twas Thu, 3 Dec 1998 18:55:08 -0500, when "Donald Tees"
> <donald@willmack.com> illuminated comp.lang.cobol thusly:
…[24 more quoted lines elided]…
>

Speaking purely from a Big-Iron background, check your PMAP. You'll see that
it doesn't matter which flavor you use, regardless of the data-type. COBOL
Knows....

WOB

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 11)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3668B05F.F1AAE0E3@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <74a5db$bvq$1@nnrp1.dejanews.com>`

```
wobconsult@sprynet.com wrote:
> 
(snip)
> 
> Speaking purely from a Big-Iron background, check your PMAP. You'll see that
> it doesn't matter which flavor you use, regardless of the data-type. COBOL
> Knows....

While this is true, it has nothing to do withn this discussion.

Bill Lynch <G>
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 12)_

- **From:** wobconsult@sprynet.com
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74b6ar$5jb$1@nnrp1.dejanews.com>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <74a5db$bvq$1@nnrp1.dejanews.com> <3668B05F.F1AAE0E3@att.net>`

```
In article <3668B05F.F1AAE0E3@att.net>,
  wblynch@worldnet.att.net wrote:
> wobconsult@sprynet.com wrote:
> >
…[9 more quoted lines elided]…
>

What was the original discussion about? Must have missed it....

WOB

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 13)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uo1PsHFI#GA.240@upnetnews03>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <74a5db$bvq$1@nnrp1.dejanews.com> <3668B05F.F1AAE0E3@att.net> <74b6ar$5jb$1@nnrp1.dejanews.com>`

```

wobconsult@sprynet.com wrote in message <74b6ar$5jb$1@nnrp1.dejanews.com>...
>In article <3668B05F.F1AAE0E3@att.net>,
>  wblynch@worldnet.att.net wrote:
…[4 more quoted lines elided]…
>> > Speaking purely from a Big-Iron background, check your PMAP. You'll see
that
>> > it doesn't matter which flavor you use, regardless of the data-type.
COBOL
>> > Knows....
>>
…[6 more quoted lines elided]…
>


I can trace the prior incarnation back to "ELIF Proposal" posted by
RJRayhawk  on 11/30/98 at 12:39 PM.
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 13)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366A5515.E1D07721@att.net>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews> <74a5db$bvq$1@nnrp1.dejanews.com> <3668B05F.F1AAE0E3@att.net> <74b6ar$5jb$1@nnrp1.dejanews.com>`

```
wobconsult@sprynet.com wrote:
> 
(snip)
> > >
> > > Speaking purely from a Big-Iron background, check your PMAP. You'll see that
…[8 more quoted lines elided]…
> What was the original discussion about? Must have missed it....

My comment was more along the lines of "It doesn't matter what happens
in the real world (the compiler), we're more inclined to hash this about
over a week or two".

Bill Lynch
```

###### ↳ ↳ ↳ Re: ZERO or ZEROS or ZEROES

_(reply depth: 10)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OgNPdZCI#GA.332@upnetnews03>`
- **References:** `<3662de01.0@news1.ibm.net> <19981130142756.20613.00000236@ng21.aol.com> <eYnV4ndH#GA.123@upnetnews05> <36652831.0@news1.ibm.net> <#USW42eH#GA.214@upnetnews05> <36657d96.168710913@news.acucorp.com> <ewBuzUvH#GA.161@upnetnews05> <74781b$o5k$1@news.igs.net> <3667d1bb.180873407@netnews>`

```

Randall Bart wrote in message <3667d1bb.180873407@netnews>...
>'Twas Thu, 3 Dec 1998 18:55:08 -0500, when "Donald Tees"
><donald@willmack.com> illuminated comp.lang.cobol thusly:
…[3 more quoted lines elided]…
>>>I've actually seen (heard?) heated arguments among COBOL programmers as
to
>>>whether the figurative constant ZERO or ZEROS or ZEROES is the
'preferred'
>>>term for elegant usage.  But the correct answer here seems to be
'whatever
>>>floats your boat.'
>>
…[7 more quoted lines elided]…
>
There we have it, a Standard rule of application of the various forms of the
ZERO figurative constant ! It even looks to be logically arrived at.  But
I'm really glad that COBOL compilers don't enforce it. <G>
```

#### ↳ Re: ELIF Proposal

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.10ccaff335a79e6f9896bf@news.earthlink.net>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
In article <19981130123924.16775.00000169@ng131.aol.com>, 
rkrayhawk@aol.com says...
> 
<SNIP>

Robert, I agree with Leif. Spelling out ELSE-IF would be a lot
easier to read than ELIF and it would be consistent with the
existing Cobol standards. 
```

##### ↳ ↳ Re: ELIF Proposal

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667624b.152418467@netnews>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <MPG.10ccaff335a79e6f9896bf@news.earthlink.net>`

```
'Twas Mon, 30 Nov 1998 13:37:31 -0500, when JeffreyFarkas@earthlink.net
(Jeff Farkas) illuminated comp.lang.cobol thusly:

>Robert, I agree with Leif. Spelling out ELSE-IF would be a lot
>easier to read than ELIF and it would be consistent with the
>existing Cobol standards. 

ELSE-IF is out, because it looks too much like ELSE IF which it is just
slightly different than.  Consider:

    IF  A = B
        statement
    ELSE-IF C = D
        statement
    ELSE IF E = F
        statement
    END-IF
    ADD 1 TO X

The coder intends for the END-IF to end all the IFs, but due to a missing
hyphen, the ADD 1 is not always executed.  A subtle distinction because of
a missing punctuation character is A Bad Thing.  How about OR-IF or
possible OR IF?  As it stands, EVALUATE is good enough.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667F338.43439BDC@home.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <MPG.10ccaff335a79e6f9896bf@news.earthlink.net> <3667624b.152418467@netnews>`

```
What ever happened to OTHERWISE ?
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74hu7r$mp9@dfw-ixnews10.ix.netcom.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <MPG.10ccaff335a79e6f9896bf@news.earthlink.net> <3667624b.152418467@netnews> <3667F338.43439BDC@home.com>`

```

Howard Brazee wrote in message <3667F338.43439BDC@home.com>...
>What ever happened to OTHERWISE ?

On IBM mainframes, it was supported with the OS/VS COBOL and DOS/VS COBOL
compilers - but not anything newer.  I know that it was not a part of the
'74 Standard (much less the '85 Standard) but don't know if it was an
extension or part of the '68 Standard.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 5)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366D6E2B.4DAB@compaq.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <MPG.10ccaff335a79e6f9896bf@news.earthlink.net> <3667624b.152418467@netnews> <3667F338.43439BDC@home.com> <74hu7r$mp9@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Howard Brazee wrote in message <3667F338.43439BDC@home.com>...
…[5 more quoted lines elided]…
> extension or part of the '68 Standard.

It was not actually an extension origianlly.  It was part of the 
DOD-65 specification, which all of use used as a sort of standard 
before there was a standard.  The ANSI committee deleted it when they 
created the first "real" standard in 1968.
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366c9f36.521392405@news1.ibm.net>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <MPG.10ccaff335a79e6f9896bf@news.earthlink.net> <3667624b.152418467@netnews> <3667F338.43439BDC@home.com>`

```
On Fri, 04 Dec 1998 07:35:36 -0700, Howard Brazee
<NOSPAMbrazee@home.com> wrote:

>What ever happened to OTHERWISE ?

OTHERWISE-IF?
```

#### ↳ Re: ELIF Proposal

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-oEmIvfLzlGxt@Dwight_Miller.iix.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
On Mon, 30 Nov 1998 17:39:24, rkrayhawk@aol.com (RKRayhawk) wrote:

> Also, I must add, that EVALUATE statements start simple, and get complex late
> in life. They are very hard to maintain if there is a need to change the
…[15 more quoted lines elided]…
> 

Robert, 

I appreciate your posting!  Lots to think about.  I started using 
Evaluate about two years ago.  I have since moved to a shop that has 
used it much longer.  That said, I have had the distinct pleasure of 
having the maintain this code.  I find the Evaluate construct EASIER 
to maintain than the old nested if style of structure.

I think the harder to maintain versions might stem from programmers 
not understanding the construct fully before implementing it.  There 
is extreme power in this statement.

When you start combining multiple selection subjects, and using ANY, 
you find that it can condense a complex decision tree into an easy to 
UNDERSTAND and maintain segment of code.

The fact that it exits upon the first true condition means that it 
DOES have to be carefully constructed.  It requires THOUGHT up front. 
However, this feature also means that it can be efficient.  (In many, 
but not all implementations <G>).

Can you site an example we can hash about where your "need for more" 
is expressed?
```

#### ↳ Re: ELIF Proposal

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36631215.8CDA0A72@inficad.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
Would someone explain to me what ELIF is?  I need a place to start.
An example. It took years to understand If then else, and now I'm
learning evaluate. 

Thanks,

Warren Simmons


RKRayhawk wrote:
> 
> Barticus@att.spam.net (Randall Bart)
> Date: 29 Nov 1998 06:47:11 GMT
> Was kind enough to commented within an ong

-----------snip of all of message---------
```

#### ↳ Re: ELIF Proposal

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73v6ck$c4n@dfw-ixnews6.ix.netcom.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
If someone (other than me - given my current reputation at J4) were to write
a "concise" request for a new feature "ELSE-IF" for the FOLLOWING Standard
(not the one currently in draft status), there is a place in the J4 agenda
where this could be placed.

I would be happy to pass along the suggestion or you can send it directly to
J4 via its chair at
    das@microfocus.com
(but please make it clear that it is NOT for the current draft in progress)

Note: I have read the posts showing how it is syntactically separate from
just another ELSE IF - but have not understood whether this means there
would also need to be another scope terminator, e.g. END-ELSE-IF  (which
seems "clumsy" to me).

Note2: When writing your suggestion, please include a BRIEF reason why you
think it would be a useful enhancement over the current "ELSE IF" *and*
"EVALUATE" structures.
```

##### ↳ ↳ Re: ELIF Proposal

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36634B6F.73A9@swbell.net>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <73v6ck$c4n@dfw-ixnews6.ix.netcom.com>`

```
William M. Klein wrote:
>
[snip -- concerning the proposed ELIF or ELSE-IF syntax] 
> 
> Note: I have read the posts showing how it is syntactically separate from
> just another ELSE IF - but have not understood whether this means there
> would also need to be another scope terminator, e.g. END-ELSE-IF  (which
> seems "clumsy" to me).

Not only clumsy, but also illogical.  END-ELSE-IF would appear to
terminate only the most recent unterminated ELSE-IF.  A chain of
ELSE-IFs would then require a chain of END-ELSE-IFs, and we'd be
back where we started.

A chain of ELSE-IFs would start with an IF, and it is the scope of
that IF that we want to terminate.  Hence the most natural terminator
would be END-IF.  Thus this keyword would be overloaded, as has 
happened to other keywords such as TO and THRU.  It's not obvious to
me that this overloading would lead to any serious ambiguity.

I don't like spelling this new token "ELSE-IF" because it invites
troublesome typos -- all you have to do is omit the hyphen, or put
one in when you shouldn't.  I would prefer "ELSIF", as it is spelled
in PL/SQL.  It's less vulnerable to typos, but visually is more
distinct from "ELSE" than "ELIF" is, being one character longer.

Other possibilities, with or without hyphens:

	OR-IF
	OTHERWISE-IF
	ON-THE-OTHER-HAND-IF

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: ELIF Proposal

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hfb92.623$Lx2.1417@news1.atlantic.net>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <73v6ck$c4n@dfw-ixnews6.ix.netcom.com>`

```

William M. Klein wrote in message <73v6ck$c4n@dfw-ixnews6.ix.netcom.com>...
[...]
>Note: I have read the posts showing how it is syntactically separate from
>just another ELSE IF - but have not understood whether this means there
>would also need to be another scope terminator, e.g. END-ELSE-IF  (which
>seems "clumsy" to me).
>
No, it would not require another scope terminator. It would provide for
another conditional statement to occur at the same IF-nesting level as
the prior IF, or ELSE-IF (ELIF, EF, or whatever). As in:

IF conditional-expression [ THEN (optional) ]
    [ IF block ]
ELSE-IF conditional-expression [ THEN (optional) ]
    [ ELSE-IF block]
ELSE
    [ ELSE block ]
END-IF

Which is similar to FORTRAN 77.

IF (e) THEN
    [ IF block ]
ELSE IF (e) THEN
    [ ELSE IF block ]
ELSE
    [ ELSE block ]
END IF

In COBOL 85, the IF-nesting level is increased by 1 with each IF;
reduced by 1 with each END-IF. The IF-nesting level is reset to
zero with an end of sentence (period /full stop).

In FORTRAN 77, changes in the IF-nesting level are the same as
COBOL 85 with the exception that each ELSE IF has the same
IF-nesting level at the prior IF or ELSE IF. There is also no means
to reset the IF-nesting level in FORTRAN 77.

Because of these similarities, I find it curious that the COBOL 85
standard did not provide for a definition similar to FORTRAN 77.
It would have been easy to define it then; but difficult to change it
now.

Perhaps it was because FORTRAN was not Pascal? ;-)
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

##### ↳ ↳ Re: ELIF Proposal

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OZgD5ndH#GA.218@upnetnews05>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <73v6ck$c4n@dfw-ixnews6.ix.netcom.com>`

```

William M. Klein wrote in message <73v6ck$c4n@dfw-ixnews6.ix.netcom.com>...
>If someone (other than me - given my current reputation at J4) were to
write
>a "concise" request for a new feature "ELSE-IF" for the FOLLOWING Standard
>(not the one currently in draft status), there is a place in the J4 agenda
>where this could be placed.
>
>I would be happy to pass along the suggestion or you can send it directly
to
>J4 via its chair at
>    das@microfocus.com
…[5 more quoted lines elided]…
>seems "clumsy" to me).


My (admittedly incomplete) understanding of ELSE-IF is that it's scope is
terminated by the next ELSE-IF or a terminal END-IF (or, dare I say it, an
explicit period.)  I'll now accept a correction of my understanding from any
willing proponent of the ELSE-IF construct, which BTW I _do_ view favorably.
I'd also love to have a PERFORM ... DEPENDING construct authorized, but that
is another story.

>Note2: When writing your suggestion, please include a BRIEF reason why you
>think it would be a useful enhancement over the current "ELSE IF" *and*
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ELIF Proposal

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<REa92.622$Lx2.1358@news1.atlantic.net>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <73v6ck$c4n@dfw-ixnews6.ix.netcom.com> <OZgD5ndH#GA.218@upnetnews05>`

```

Dennis J. Minette wrote in message ...
>
>My (admittedly incomplete) understanding of ELSE-IF is that it's scope is
>terminated by the next ELSE-IF or a terminal END-IF (or, dare I say it, an
>explicit period.)  [...]
>
ELSE-IF may be terminated by an ELSE, as well.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: ELIF Proposal

_(reply depth: 4)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OqYQ9kjH#GA.221@upnetnews05>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <73v6ck$c4n@dfw-ixnews6.ix.netcom.com> <OZgD5ndH#GA.218@upnetnews05> <REa92.622$Lx2.1358@news1.atlantic.net>`

```
Thanks for the additional info on ELSE-IF terminators - as I noted, I do
have an incomplete understanding of this proposed construct, but I
definitely fully support the concept.

Rick Smith wrote in message ...
>
>Dennis J. Minette wrote in message ...
…[10 more quoted lines elided]…
>
```

#### ↳ Standards work in progress?

- **From:** "David A. Cobb" <dacobb2@excite.com>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366417A0.25C8@excite.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com>`

```
Hi!
Does anyone here know where on the internet one can read any of the
working papers for the current standardization cycle.

ISO or ANSI would like to sell the book - and it costs a fortune!  But
even that is the "old" version.  Many other standards groups post the
working papers for comment, does the COBOL committee?
```

##### ↳ ↳ Re: Standards work in progress?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<741o8t$is5@dfw-ixnews9.ix.netcom.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <366417A0.25C8@excite.com>`

```
For the ANSI draft document, send a note to the J4 chair at
    das@microfocus.com

David A. Cobb wrote in message <366417A0.25C8@excite.com>...
>Hi!
>Does anyone here know where on the internet one can read any of the
…[9 more quoted lines elided]…
>--
```

##### ↳ ↳ Re: Standards work in progress?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-dO2BnzJ7T1Pp@Dwight_Miller.iix.com>`
- **References:** `<19981130123924.16775.00000169@ng131.aol.com> <366417A0.25C8@excite.com>`

```
On Tue, 1 Dec 1998 16:21:52, "David A. Cobb" <dacobb2@excite.com> 
wrote:

> Hi!
> Does anyone here know where on the internet one can read any of the
…[5 more quoted lines elided]…
> 

They used to, but now they don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
