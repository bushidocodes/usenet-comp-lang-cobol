[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accuracy/Knowledge score-card

_521 messages · 36 participants · 2003-04 → 2003-06_

---

### Accuracy/Knowledge score-card

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-07T15:14:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net>`

```
I thought I would start a "running" thread on issues that explain my opinion
(and it is only an OPINION) of one specific poster to CLC.  The following
are NOT in any specific order (chronological or "importance")

NOTE WELL:
   This is (and only claims to be) one side of the picture.  There have been
accurate statements made as well.  Particularly when "pinned down" to
stating that something *is* an opinion and not "fact/truth", some posts have
value.  The trouble is in finding the good among the less so good.

1) Doesn't know/use Intrinsic Functions (available since '89)

2) Hadn't seen any (many?) reference modifications where the starting
position or length was a variable - much less an arithmetic expression

3) Unaware that all ANSI/ISO ('85 Standard) conforming compilers return file
status 35 on file not found.  (Claimed that some current compilers didn't -
when running in '85 Standard mode)

4) Didn't think that the '85 Standard INITIALIZE statement was "well
defined" (my quotes) and totally predictable (and/or was  useable as it
was).  Specifically claimed that *I* thought it didn't work the way that it
should.

5) Thought that the 1989 in the ISO Standards was a date.

6) Claims that it is only mainframe (possibly IBM mainframe?) programmers
who use periods in the procedure division - where they are not required -
and thinks that doing so is a BAD thing that should be prohibited (not just
a style issue).

7)  Thinks that reference-modification doesn't look COBOL-like, so it
shouldn't be used, but thinks that "lists" are better than tables and should
be used.

8) Claimed that ANSI/ISO *required* that subscripts and/or indexes (I can't
remember if it was both or not) *must* cause an error at run-time when set
to an out-of-bound value.

9) Claimed that some ANSI/ISO conforming compiler actually *did* return a
4-digit year when the receiving field of ACCEPT FROM DATE was 8 characters.
(Didn't know about the YYYYMMDD and YYYYYDDD keywords available on many -
but not all - compilers since well before 2000.)

10) Claims to know what the majority of COBOL programmers think about a
variety of issues.  Also, makes claims (that I am still a little fuzzy
about) concerning "modern" compilers and computer environments.  Pretty much
"writes off" all mainframe COBOL environments and makes generic statements
about such environments that MAY apply to IBM mainframe environments, but
certainly not to all others.

11) Doesn't believe manuals and thinks that what the compiler "does" today
is more important than what the vendor CLAIMS the compiler supports (rather
than lets thru).
```

#### ↳ Re: Accuracy/Knowledge score-card

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-07T15:36:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6snhg$87h$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b6sm6g$9uq$1@slb9.atl.mindspring.net...
> I thought I would start a "running" thread on issues that explain my
opinion
> (and it is only an OPINION) of one specific poster to CLC.  The following
> are NOT in any specific order (chronological or "importance")
>
> NOTE WELL:
>    This is (and only claims to be) one side of the picture.  There have
been
> accurate statements made as well.  Particularly when "pinned down" to
> stating that something *is* an opinion and not "fact/truth", some posts
have
> value.  The trouble is in finding the good among the less so good.
>
…[5 more quoted lines elided]…
> 3) Unaware that all ANSI/ISO ('85 Standard) conforming compilers return
file
> status 35 on file not found.  (Claimed that some current compilers
didn't -
> when running in '85 Standard mode)
>
> 4) Didn't think that the '85 Standard INITIALIZE statement was "well
> defined" (my quotes) and totally predictable (and/or was  useable as it
> was).  Specifically claimed that *I* thought it didn't work the way that
it
> should.
>
…[4 more quoted lines elided]…
> and thinks that doing so is a BAD thing that should be prohibited (not
just
> a style issue).
>
> 7)  Thinks that reference-modification doesn't look COBOL-like, so it
> shouldn't be used, but thinks that "lists" are better than tables and
should
> be used.
>
> 8) Claimed that ANSI/ISO *required* that subscripts and/or indexes (I
can't
> remember if it was both or not) *must* cause an error at run-time when set
> to an out-of-bound value.
>
> 9) Claimed that some ANSI/ISO conforming compiler actually *did* return a
> 4-digit year when the receiving field of ACCEPT FROM DATE was 8
characters.
> (Didn't know about the YYYYMMDD and YYYYYDDD keywords available on many -
> but not all - compilers since well before 2000.)
…[3 more quoted lines elided]…
> about) concerning "modern" compilers and computer environments.  Pretty
much
> "writes off" all mainframe COBOL environments and makes generic statements
> about such environments that MAY apply to IBM mainframe environments, but
…[3 more quoted lines elided]…
> is more important than what the vendor CLAIMS the compiler supports
(rather
> than lets thru).
>

12) Claimed that some IBM compilers have accepted NEXT SENTENCE in places
other than IF and SEARCH.  (Then used "Realia" compiler to determine if this
was true or not).

13) Stated there were no exceptions to a rule that a conditional phrase of a
containing statement provided an implicit scope terminator for a nested
statement - without knowing that ONLY an ELSE phrase may follow a nested
conditional statement within an ANSI/ISO conforming (and clean compile of
most - not all vendor's compiler) program.
```

##### ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-08T06:38:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e926a64.117918669@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:


>13) Stated there were no exceptions to a rule that a conditional phrase of a
>containing statement provided an implicit scope terminator for a nested
>statement - without knowing that ONLY an ELSE phrase may follow a nested
>conditional statement within an ANSI/ISO conforming (and clean compile of
>most - not all vendor's compiler) program.

I'm puzzled by this statement. 

if foo equal to '1'
   (do something)
end-if 

..is certainly valid. There is no ELSE required.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-08T02:35:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6tu4a$m1f$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e926a64.117918669@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e926a64.117918669@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
>
> >13) Stated there were no exceptions to a rule that a conditional phrase
of a
> >containing statement provided an implicit scope terminator for a nested
> >statement - without knowing that ONLY an ELSE phrase may follow a nested
…[10 more quoted lines elided]…
>

It is true that an END-IF may terminate a nested conditional statement with
an implicit conditional statement.  I was too limited in my original
statement.  The distinction that I was attempting to make was between the IF
statement (which may have nested conditional statements - terminated by a
following "valid" phrase of the IF statement causing an implicit scope
terminator) and *ALL* other statements in the ANSI/ISO COBOL language
definition which may NOT have nested conditional statements - and therefore,
their conditional phrases NEVER create an implicit scope terminator.

The original question in the original thread had two things that indicated
that this was unclear to the original poster:

"The next  phrase of the containing statement (for example, ELSE, WHEN, AT
END, and so on) following the contained statement terminates the scope of
any unterminated contained statement. ..."

   and

"From this I gather that when any COBOL statement may have nested
statements (like IF, PERFORM, etc.), any following statements are tied to
the nearest containing statement. ...

Is this rule correct in general, or are there any exceptions I should be
aware of (of course, with respect to COBOL'85) ?"

  ***

It was to this question/post that the following reply was made,

"Correct. There are no exceptions."
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-08T23:14:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e934956.175001795@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e926a64.117918669@news.optonline.net> <b6tu4a$m1f$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[49 more quoted lines elided]…
>"Correct. There are no exceptions."

To make sure I understand your point, I'll restate it with examples. You say
this is valid:

if  (condition)
    read file-name at end
        display 'error'
end-if    *> implicitly terminates read

Whereas this is not: 

read file-name at end
    if  (condition)
        display 'error'
end-read

But this is valid:

read file-name at end
    if  (condition)
        display 'error'
    end-if
end-read

Ok, I'll concede I was incorrect. The next phrase of the containing statement 
following the contained statement (ELSE or END-IF) terminates the scope of
any unterminated contained statement ONLY when the containing statement is IF. 
In all other cases, the contained statement must be explicitly terminated.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-08T18:26:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6vls8$pvb$1@slb0.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e926a64.117918669@news.optonline.net> <b6tu4a$m1f$1@slb9.atl.mindspring.net> <3e934956.175001795@news.optonline.net>`

```
Your summary and examples are correct - for an ANSI/ISO conforming program.
Some vendors *may* allow other extensions (nested conditionals in other than
IF statements).
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-09T22:44:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9497c4.260629034@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e926a64.117918669@news.optonline.net> <b6tu4a$m1f$1@slb9.atl.mindspring.net> <3e934956.175001795@news.optonline.net> <b6vls8$pvb$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Your summary and examples are correct - for an ANSI/ISO conforming program.
>Some vendors *may* allow other extensions (nested conditionals in other than
>IF statements).

I tried this today on two compilers, which led to understanding the problem but
raised a few questions. 

First, the original question was quoting the standard when it said:

Kris De Schutter <legolas.greenleaf@advalvas.be> wrote:

>I'm trying to find out how the COBOL'85 standard handles implicit scope
>termination, and I found the following on the web
…[9 more quoted lines elided]…
>>        scope of any unterminated contained statement.

.. then went on to say he interpreted that to mean anything could be nested
inside anything. The second paragraph strongly suggests that. If the only
possible containing statement is IF, the example should have been ELSE or
END-IF. My experience with Micro Focus shows it to be in concord with the above.
The combination of standard language plus Micro Focus performance is why I
responded "No exceptions". 

To verify this, I compiled a program reading:

perform
    if  (condition)
        display 'something'
end-perform

It compiled without error. Through this point everything is sane. 

Next, I compiled the same program with Fujitsu. It returned an error 'imperative
statement required'. Huh? I could understand if it said 'IF statement not
terminated'. So I dusted off the manual and looked at the prototype for PERFORM,
which reads:

perform ...
    imperative-statement

That explains the compiler's message, but leaves me even more confused. We all
know one can put IF statements under PERFORM. Checking a few other verbs, I see
they _all_ read imperative-statement .. all except IF, which permits conditional
statements as well. That's the basis for your analysis, which would have been
much clearer if you had mentioned the word "imperative". 

Next I terminated the IF with an END-IF. Fujitsu was happy with that. This means
a terminated if ... end-if is considered (by somebody) to be an imperative
statement. How can that be? The standard clearly defines "imperative-statement"
to be MOVE, ADD, etc. without conditionals (such as on size error), and defines
IF, EVALUATE, etc. to be "conditional-statements". 

My questions are:

1.  Why does the standard say PERFORM ... imperative-statement?

2.  Where does the standard say IF ... END-IF is an imperative-statement,
whereas an unterminated IF is a conditional-statement?

3.  Why does the 'implicit termination' paragraph quoted above give as examples
"WHEN, AT END, etc." if they can never happen?

Respectfully, 
Robert

Thread history:

> wmklein <at> ix.netcom.com
>"Robert Wagner" <robert@wagner.net> wrote in message
…[94 more quoted lines elided]…
>> In all other cases, the contained statement must be explicitly terminated.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-09T18:30:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72aea$tdp$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e926a64.117918669@news.optonline.net> <b6tu4a$m1f$1@slb9.atl.mindspring.net> <3e934956.175001795@news.optonline.net> <b6vls8$pvb$1@slb0.atl.mindspring.net> <3e9497c4.260629034@news.optonline.net>`

```
Answers below:
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9624c3.362275401@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e926a64.117918669@news.optonline.net> <b6tu4a$m1f$1@slb9.atl.mindspring.net> <3e934956.175001795@news.optonline.net> <b6vls8$pvb$1@slb0.atl.mindspring.net> <3e9497c4.260629034@news.optonline.net> <b72aea$tdp$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

Thank you for the time and effort that went into your answer. 

Robert

>Answers below:
>
…[82 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-10T12:15:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72d3b$t2n$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e934956.175001795@news.optonline.net> <b6vls8$pvb$1@slb0.atl.mindspring.net> <3e9497c4.260629034@news.optonline.net>`

```
Robert Wagner wrote:

> Next I terminated the IF with an END-IF. Fujitsu was happy with that. This
> means a terminated if ... end-if is considered (by somebody) to be an
…[3 more quoted lines elided]…
> "conditional-statements".

A conditional statement is only that part which evaluates true or false and 
does not include the statements that are executed when the conditional 
determines truth or falseness.

    IF x           

    is a 'conditional statement'.

    IF x
    THEN something

    is a 'conditional statement' followed by an 'imperitive statement',
    ie is two statements.

    IF x
    THEN something
    END-IF

    is a 'delimited scope statement' and is thus not a 'conditional 
    statement'

An 'imperitive statement' is 'any statement that is neither a conditional 
statement nor ...'

A 'delimited scope statement' is not 'conditional', thus is 'imperitive'.
```

##### ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-09T03:46:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93602c.180848320@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>> 1) Doesn't know/use Intrinsic Functions (available since '89)

They encourage a C-like style of telescoping multiple functions into a single
statement. 

Most are trivial; one can accomplish the same end with regular COBOL. For
instance, function integer(). Integer-of-date is a non-trivial exception.

>> 2) Hadn't seen any (many?) reference modifications where the starting
>> position or length was a variable - much less an arithmetic expression

I haven't .. in large mainframe shops with thousands of programs. 

>> 3) Unaware that all ANSI/ISO ('85 Standard) conforming compilers return
>file
>> status 35 on file not found.  (Claimed that some current compilers
>didn't -
>> when running in '85 Standard mode)

Ok, I was wrong there. 

>> 4) Didn't think that the '85 Standard INITIALIZE statement was "well
>> defined" (my quotes) and totally predictable (and/or was  useable as it
>> was).  Specifically claimed that *I* thought it didn't work the way that
>it
>> should.

We all know what the standard says. I find it dangerous and error-prone because
it doesn't initialize FILLERs. 

>> 5) Thought that the 1989 in the ISO Standards was a date.

Well .. it _looks_ like a date. Especially because there _was_ a COBOL standard
published in 1989.  For those of us who don't work with ISO nomenclature often,
it's an understandable mistake. 

>> 6) Claims that it is only mainframe (possibly IBM mainframe?) programmers
>> who use periods in the procedure division - where they are not required -
>> and thinks that doing so is a BAD thing that should be prohibited (not
>>just a style issue).

I never said that. It's a style issue which I believe is BAD style. 

>> 7)  Thinks that reference-modification doesn't look COBOL-like, so it
>> shouldn't be used, but thinks that "lists" are better than tables and
>>should be used.

Yes. I didn't advocate avoiding reference-modification. I mentioned in passing
that I don't like it. I _did_ advocate lists and there has been little
substantive rebuttal. 

>> 8) Claimed that ANSI/ISO *required* that subscripts and/or indexes (I
>can't
>> remember if it was both or not) *must* cause an error at run-time when set
>> to an out-of-bound value.

Indexes. They did cause an out of bounds under COBOL '74. I haven't used them
much since, which explains why I was unaware bounds checking had changed. 

>> 9) Claimed that some ANSI/ISO conforming compiler actually *did* return a
>> 4-digit year when the receiving field of ACCEPT FROM DATE was 8
>characters.
>> (Didn't know about the YYYYMMDD and YYYYYDDD keywords available on many -
>> but not all - compilers since well before 2000.)

Answered in another post. 

>> 10) Claims to know what the majority of COBOL programmers think about a
>> variety of issues.  Also, makes claims (that I am still a little fuzzy
…[4 more quoted lines elided]…
>> certainly not to all others.

Hand waving. 

>> 11) Doesn't believe manuals and thinks that what the compiler "does" today
>> is more important than what the vendor CLAIMS the compiler supports
>(rather
>> than lets thru).

Over the years, I've encountered many discrepencies between reality and what the
manual said. 

>12) Claimed that some IBM compilers have accepted NEXT SENTENCE in places
>other than IF and SEARCH.  (Then used "Realia" compiler to determine if this
>was true or not).

Realia was an IBM clone. It originally shipped with IBM COBOL manuals.
Compatibility was 99+%. Thus, it's valid to infer IBM standards from Realia's
performance. 

>13) Stated there were no exceptions to a rule that a conditional phrase of a
>containing statement provided an implicit scope terminator for a nested
>statement - without knowing that ONLY an ELSE phrase may follow a nested
>conditional statement within an ANSI/ISO conforming (and clean compile of
>most - not all vendor's compiler) program.

A very technical point, answered in another thread.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-09T14:15:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b719t5$1ci$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net>`

```

On  8-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >> 1) Doesn't know/use Intrinsic Functions (available since '89)
>
> They encourage a C-like style of telescoping multiple functions into a single
> statement.

I wish they were designed with a better return code mechanism though.  C has an
advantage here.

> Most are trivial; one can accomplish the same end with regular COBOL. For
> instance, function integer(). Integer-of-date is a non-trivial exception.

Of course, the issue that started this discussion was a need for CURRENT-DATE.
If you think the language needed this ability (which you said it does), then it
doesn't matter whether it is trivial or not.

An advantage of trivial functions over "regular CoBOL", is having consistent
results everywhere.


> >> 2) Hadn't seen any (many?) reference modifications where the starting
> >> position or length was a variable - much less an arithmetic expression
>
> I haven't .. in large mainframe shops with thousands of programs.

Interesting.   String manipulation tends to use this almost exclusively these
days.   Stuff like name and address cleansing, or finding the end of a variable
length, space filled string work well with variable start positions.

But you have said that the programs that you have seen are old and don't use
"modern" techniques.


> >> 5) Thought that the 1989 in the ISO Standards was a date.
>
…[4 more quoted lines elided]…
> it's an understandable mistake.

I always assumed it.  And 1968 & 1972 as well.   Were they intended to be dates
- but as deadlines were missed, they were redefined?


> Over the years, I've encountered many discrepencies between reality and what
> the manual said.

I haven't.   But generally when someone makes a statement which contradicts the
manuals - the amount of supporting evidence should go up.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-09T08:05:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71csj$fe7$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b719t5$1ci$1@peabody.colorado.edu...

<regarding the assumption that "1989" in "ISO/IEC 1989:2002" (for example)
was a date>:

>
> I always assumed it.  And 1968 & 1972 as well.   Were they intended to be
dates
> - but as deadlines were missed, they were redefined?

It is indeed a common misunderstanding to those familiar with COBOL but not
much familiar with the international standards process (and the
International Standards Organization).  ANSI X3.23-1974 was also published
and promulgated in 1978 as "ISO International Standard 1989 - 1978".  The
document states on the inside front cover "This International Standard
cancels and replaces ISO Recommendation R 1989 - 1972, of which it
constitutes a technical revision".  The fact that the international standard
(or international recommendation) was known as 1989 in 1972 is, of course,
some sort of clue that 1989 isn't a date, any more than ISO 9000, to which
many companies conform today, was actually promulgated in, or scheduled to
be promulgated in, A. D. 9000, or that the encoding scheme for 7-bit coded
data reflected in ISO/IEC 646 was actually promulgated in A. D. 646.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-10T09:59:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b747sr$2f2u$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b719t5$1ci$1@peabody.colorado.edu...
>
> On  8-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
> > They encourage a C-like style of telescoping multiple functions into a
single
> > statement.
>
> I wish they were designed with a better return code mechanism though.  C
has an
> advantage here.

Are you referring to something like C's ability to "throw" exceptions?  If
so, a very similar feature is provided in the 2002 COBOL standard in the
context of Common Exception Handling, including the ability to "propagate"
exceptions back through the calling/invoking sequence.

     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-10T17:31:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b749om$fab$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com>`

```

On 10-Apr-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> > I wish they were designed with a better return code mechanism though.  C
> has an
…[5 more quoted lines elided]…
> exceptions back through the calling/invoking sequence.

That would help.

But let's say we have a non-OO program.   I want a Return Code or an exception
that easily lets me know if and why the function failed.

Start here with my wish (easily accomplished with some languages)

e.g.   Display function date-of-integer  (my-variable)
	on exception perform tell-me-why-this-function-failed
	end-function.
why-this-function-failed.
	evaluate function-code
                  when '30'   display 'date out of range'
                  when '40'   display 'date not numeric'
                  when other display 'library not working'
            end-evaluate.

If I had integer-of-date, I might have an error code for February 29 in a year
without a February 29th.   This might even return a value equivalent to March
1st when I do check for exceptions, allowing me to do with it what I choose.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-10T11:48:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74e96$2ji4$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu>`

```
<howard@brazee.net> wrote in message
news:b749om$fab$1@peabody.colorado.edu...
I wrote:
> > Are you referring to something like C's ability to "throw" exceptions?
If
> > so, a very similar feature is provided in the 2002 COBOL standard in the
> > context of Common Exception Handling, including the ability to
"propagate"
> > exceptions back through the calling/invoking sequence.

Howard Brazee responded:

> But let's say we have a non-OO program.

I don't think the use or declaration of user-defined functions is limited to
the OO environment as commonly understood.  And propagation of exceptions
applies to called programs just as it does to methods and functions.

> I want a Return Code or an exception
> that easily lets me know if and why the function failed.

I'm not sure what you mean by a "return code", but I believe the Common
Exception feature provides what you need.  For your own functions, you can
define whatever exceptions you choose, set them, process them, ignore them
if you like.

> Start here with my wish (easily accomplished with some languages)
>
…[8 more quoted lines elided]…
>             end-evaluate.

I'm not going to try equivalent code because I don't have a 2002-compliant
compiler handy.  But I would encourage you to look into the Common Exception
Processing feature, because I believe it provides everything you need,
though perhaps not in the syntax you wish.

> If I had integer-of-date, I might have an error code for February 29 in a
year
> without a February 29th.   This might even return a value equivalent to
March
> 1st when I do check for exceptions, allowing me to do with it what I
choose.

For intrinsic functions, EC-ARGUMENT-FUNCTION indicates a problem with the
range of a function argument.

Also, FUNCTION EXCEPTION-LOCATION provides an implementor-defined
alphanumeric string indicating where the problem occurred (this might, for
example, be the sequence number in fixed-form reference format); FUNCTION
EXCEPTION-STATEMENT can return the name of the procedural statement that
caused the problem; and FUNCTION EXCEPTION-STATUS returns the name of the
exception raised.  These can all be used with exceptions raised (and
transmitted using e.g. EXIT FUNCTION RAISING EC-xxxx, or even more
automatically with the >>PROPAGATE directive set to ON in the caller)
defined by the user as well as the standard ones.   In user code, RAISE
EXCEPTION <exception-name> does what it says; once it's been processed, the
program can SET LAST EXCEPTION TO OFF.

I'm not sure what it is that you're requesting beyond what's already there
in the new standard.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-10T19:35:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74h2t$jhl$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com>`

```

On 10-Apr-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> I'm not going to try equivalent code because I don't have a 2002-compliant
> compiler handy.  But I would encourage you to look into the Common Exception
> Processing feature, because I believe it provides everything you need,
> though perhaps not in the syntax you wish.

Me neither.   It will be nice if this does this job.  It was a IMNO, a fault
that we could find out so little about why a function failed.   If we ever get a
compliant compiler, I certainly will look into this.
```

###### ↳ ↳ ↳ Exceptions and Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-10T15:07:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74iuu$7$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com> <b74h2t$jhl$1@peabody.colorado.edu>`

```
Howard,
  There is a long and SAD story behind why the original Intrinsic Functions
Amendment was "issued" without proper (any) error detection method.

*ORIGINALLY* there were "return-codes" issued when invalid arguments were
used.  This version was in the JOD and went out for "public review".  The
problem was that it was "numeric" values returned when an invalid argument
was found.  This meant that in SOME cases, the SAME returned value could be
EITHER
  - an error indication
 - a valid numeric returned value

Therefore (luckily), this POOR design was pulled and rather than wait for a
"better" solution to be introduced, the Intrinsic Function Amendment was
"issued" in 1989 with NO method of detecting invalid arguments.  Partially,
this was done (in 1989 - hold your breath for the"laugh") because it was
THOUGHT that the next full revision of the Standard *with* an improved
exception handling facility (or a separate amendment with such) would be
available in a "couple" (or at most few) years!!!

Well, you know the rest ...
```

###### ↳ ↳ ↳ Re: Exceptions and Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-10T22:15:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E95EDC1.ADF636A4@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com> <b74h2t$jhl$1@peabody.colorado.edu> <b74iuu$7$1@slb9.atl.mindspring.net>`

```


"William M. Klein" wrote:

> Howard,
>   There is a long and SAD story behind why the original Intrinsic Functions
> Amendment was "issued" without proper (any) error detection method.
> <snip>

Come to think of it, that Iraqi Information Minister is currently out of a job
(Sahed or some such). Perhaps J4 have an 'opening' for a PR man <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Exceptions and Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-11T14:46:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e96c73d_1@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com> <b74h2t$jhl$1@peabody.colorado.edu> <b74iuu$7$1@slb9.atl.mindspring.net> <3E95EDC1.ADF636A4@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E95EDC1.ADF636A4@shaw.ca...
>
>
…[3 more quoted lines elided]…
> >   There is a long and SAD story behind why the original Intrinsic
Functions
> > Amendment was "issued" without proper (any) error detection method.
> > <snip>
>
> Come to think of it, that Iraqi Information Minister is currently out of a
job
> (Sahed or some such). Perhaps J4 have an 'opening' for a PR man <G>.
>
LOL!

Actually, I kinda liked him.
(Mohammed Saeed al Shahaf)

He was sort of avuncular, like your favourite Uncle who turns up at your
Birthday Party and tells the most unlikely, but entertaining, stories.

Who could ever forget the scene from the roof of the Palestine where he was
claiming no Americans in Baghdad, and when the BBC's Rageh Omar pointed to
the tanks bearing down on the place he said: "Well, they pushed a half dozen
or so forward just to test us but we are slaughtering them and they will all
be buried in Iraq."

I was in stitches...

But the next day, when the regime fell and none of the Official "minders"
turned up to escort the journalists on their outings, he was the only one
who sent a message and said: "I'm having the day off..."

Sadly (at least in my opinion) we haven't heard from him since. I really
hope he isn't on the official "Wanted Dead or Alive - Top 50 people in
Hussein's Regime" list, distributed by the US forces to their men today. He
was real good value...

I totally agree with Jimmy, he would be an ideal front man for the Standards
Committee...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Exceptions and Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-11T17:02:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E96F652.B07C424@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com> <b74h2t$jhl$1@peabody.colorado.edu> <b74iuu$7$1@slb9.atl.mindspring.net> <3E95EDC1.ADF636A4@shaw.ca> <3e96c73d_1@127.0.0.1>`

```


"Peter E.C. Dashwood" wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3E95EDC1.ADF636A4@shaw.ca...
…[21 more quoted lines elided]…
>

I agree, I liked him too. He even put his fairy tales across sometimes with a smile on
his chops. I wish him well and hope he isn't characterized as an appartchik of the
regime - rather some poor sod who had to do the job.

>
> Who could ever forget the scene from the roof of the Palestine where he was
…[4 more quoted lines elided]…
>

Yep Rageh Omar is doing an excellent job for the BBC - something to do with the
'natural' sun tan that he has <G>. I pick up the BBC World News local time 18:00 from
PBS (Public Broadcasting Service). Fronted by a gorgeous sun-tanned anchor lady
Mishail Hussan - was originally broadcasting from UK (Wimbledon or S. London ???). She
now does her bit located in Washington DC, with a joint anchor back in the UK.

In half an hour I get a pretty unbiased summary of what's going on - rather than the
drudge of sitting through endless hours of CNN coverage, regurgitating the same news,
over and over again. We pick up CNN, primarily anchored by Aaron Brown through our US
links - so this is for the N. American 'domestic' market. Whereas, I believe, if you
are looking at CNN you are picking up on the 'international' version.

I don't know if you pick up on him but the CNN version I see has retired General
Wesley Clarke, an Atlantist and former NATO Supreme Commander, a charming and well
reasoned commentator. If our friends south of the border want a presidential candidate
for 2004 - go with Wesley Clarke, regardless of which party picks up on him !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-10T14:42:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74hg6$a0c$1@slb5.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com>`

```
Just to add to Chuck's post.

For date and numval intrinsic functions, there are NEW intrinsic functions:

 - TEST-DATE-YYYYMMDD
 - TEST-DAY-YYYYDDD
 - TEST-NUMVAL
 - TEST-NUMVAL-C
 - TEST-NUMVAL-F

which provide specific facilities for testing dae and numval "inputs" with
error specific "errors" for specific types of input problems.

I would hope that vendors (such as IBM) that haven't announced any intent to
provide a FULL 2002 Standard compiler (with exception handling), that they
would add these functions - sooner rather than later
```

###### ↳ ↳ ↳ Re: Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-10T19:56:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74i91$k6e$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com> <b74hg6$a0c$1@slb5.atl.mindspring.net>`

```

On 10-Apr-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> For date and numval intrinsic functions, there are NEW intrinsic functions:
>
…[4 more quoted lines elided]…
>  - TEST-NUMVAL-F

I've read about these and would use them if I could.  But if I were designing
functions in the first place, I would look into a more integrated design.

We don't have TEST-COMPUTE to an arithmetic expression to check for overflow.
```

###### ↳ ↳ ↳ Re: Intrinsic Functions (was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-10T13:11:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74j6a$2ms0$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b719t5$1ci$1@peabody.colorado.edu> <b747sr$2f2u$1@si05.rsvl.unisys.com> <b749om$fab$1@peabody.colorado.edu> <b74e96$2ji4$1@si05.rsvl.unisys.com> <b74hg6$a0c$1@slb5.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b74hg6$a0c$1@slb5.atl.mindspring.net...
> Just to add to Chuck's post.
>
> For date and numval intrinsic functions, there are NEW intrinsic
functions:
>
>  - TEST-DATE-YYYYMMDD
…[8 more quoted lines elided]…
> I would hope that vendors (such as IBM) that haven't announced any intent
to
> provide a FULL 2002 Standard compiler (with exception handling), that they
> would add these functions - sooner rather than later

While we're on the subject of dates, there's yet another new one that'd
probably help people "undo" their date-windowing logic:  FUNCTION
YEAR-TO-YYYY.  Provides for fixed and sliding window algorithms.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-09T14:15:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304091315.4cded057@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> 1) Doesn't know/use Intrinsic Functions (available since '89)
> 
> They encourage a C-like style of telescoping multiple functions into a single
> statement. 

And the problem with this is ?

But in fact they do not 'encourage' at all. Can you point to one word
in the standard, or even in some manual that can actually be
interpreted as _encouraging_ this ?

It does not do so any more than COMPUTE 'encourages' long calculations
with many operators.  It only _allows_, and leaves it up to the choice
of the programmer.

Of course Cobol does not allow anywhere near the freedom that C has.
It disallows many of the C styles and idioms and avoids many of the
potential problems that C can create.

> Most are trivial; one can accomplish the same end with regular COBOL. For
> instance, function integer(). Integer-of-date is a non-trivial exception.

With any set of functions there will be a range of complexity from the
least complex to the least simple.  You can achieve _all_ of the
intrinsinc functions with 'regular Cobol'.  Note that FUNCTION INTEGER
is not truncation.
 
> >> 2) Hadn't seen any (many?) reference modifications where the starting
> >> position or length was a variable - much less an arithmetic expression
> 
> I haven't .. in large mainframe shops with thousands of programs. 

Perhaps you are given all the old junk, while new systems are done by
vibrant youngsters with better outlooks and longevity.

> We all know what the standard says. I find it dangerous and error-prone
> because it doesn't initialize FILLERs. 

I find it predictable and useful that it doesn't initialize fillers.

> >> 7)  Thinks that reference-modification doesn't look COBOL-like, so it
> >> shouldn't be used, but thinks that "lists" are better than tables and
> >>should be used.
> 
> Yes. I didn't advocate avoiding reference-modification. 

> I mentioned in passing that I don't like it. 


> I _did_ advocate lists and there has been little substantive rebuttal. 

There has been 'little substantive rebuttal' that you haven't ignored
or dismissed.

While complaining above that functions 'encouraged C-like style', you
advocate making programs into being C-like.

One of the major problems with C was its use of pointers and how these
must be manually tracked and freed to ensure that there are no
memory-leaks or wild pointers.  One of the advantages of C++ and Java
is that manual pointers are replaced by automatic objects where
constructors and destrauctors look after the messy details and
dereferecing is done in the syntax.

Cobol has avoided the problems associated with pointers by only
introducing them to interract with software that requires their use,
such as Windows.

You are advocating that Cobol should be dragged back to the 1970s C
style with malloc() and free().

If you actually wanted to move forward then create a list class and
use mechanisms that make it _easier_ not harder to get working code
that is better than 'mostly'.
 
But the major problem with lists is that they _not_ the same as
tables.  The lists are accessed serially, start at the base and step
through every item until you reach the one you want.

Tables can be accessed randomly, for example in binary chop, or two
items can be accessed together. Your lists can't do that (as easily).

You claimed a speed advantage for lists (only when compared to serial
table access), but in fact there was none, or no significant
difference, so one major claim for them disappears.

The _only_ advantage is they are expandable.  As I only use tables for
small data items because large items there is _no_ advatage (for
anything I do).

The disadvantages are:

    Non-standard and unsupported syntax, not always available.
    Serial only access.
    C-like programming.
    Overly complex programming.
    Obsolete mechanism replaced by OO
    Risk of program failure in anything other than trivial use.
    The 'next programmer' will be unfamiliar with it.     

Which of those aren't substantive ?

> >> 11) Doesn't believe manuals and thinks that what the compiler "does" today
> >> is more important than what the vendor CLAIMS the compiler supports
…[3 more quoted lines elided]…
> what the manual said. 

Given your track record here in explaining 'what the manual said' then
I am not surprised that you found discrepancies between what you
_thought_ was 'reality' and what you _thought_ the manual said, or
didn't say.

However, it is not reality that is the problem.

> Realia was an IBM clone. It originally shipped with IBM COBOL manuals.
> Compatibility was 99+%. Thus, it's valid to infer IBM standards from Realia's
> performance. 

So how do you determine where the 1% is ?

And just because it is upwards compatible from some IBM compiler does
not mean that it doesn't have it own extensions.

So testing any particular behaviour using Realia may result in one of
the following:

   Using exact IBM code:
     Exact IBM behaviour (99%)
     Different behaviour because it is in the '1%'
   Using code IBM would reject:
     Exact IBM behaviour 
     Different behaviour because it is in the 1%
     Different behaviour because it is a realia extension

You are trying to assess how well a Ferrari performs by driving a
kitcar replica.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9618c9.359208255@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>> >> 2) Hadn't seen any (many?) reference modifications where the starting
>> >> position or length was a variable - much less an arithmetic expression
…[4 more quoted lines elided]…
>vibrant youngsters with better outlooks and longevity.

You make it sound as though work was parceled out based on personality. That's
not how it works. When a contractor is put on a system, he has access to all
programs in it. 

Teams are usually comprised of 'vibrant youngsters' (recent college grads
willing to work for peanuts) and a few Old Pros (like me) to bail them out when
they get in technical trouble. 

>> We all know what the standard says. I find it dangerous and error-prone
>> because it doesn't initialize FILLERs. 
>
>I find it predictable and useful that it doesn't initialize fillers.

It's not predictable when you change data-name to filler without understanding
the consequences. 

>> I _did_ advocate lists and there has been little substantive rebuttal. 
>
>There has been 'little substantive rebuttal' that you haven't ignored
>or dismissed.

When someone (you?) challenged relative speed, I wrote and posted a benchmark
showing they were about the same. That's not ignored or dismissed. 

>While complaining above that functions 'encouraged C-like style', you
>advocate making programs into being C-like.

C-like, to my mind, means nested and telescoped functions. Pointers are not
C-like, they are basic data structures. Assembly language programmers use them
routinely without being accused of promoting 'C-style'. 

>One of the major problems with C was its use of pointers and how these
>must be manually tracked and freed to ensure that there are no
…[3 more quoted lines elided]…
>dereferecing is done in the syntax.

I can't disagree with that. 

>Cobol has avoided the problems associated with pointers by only
>introducing them to interract with software that requires their use,
>such as Windows.

Nope. They're available to application programmers. I use them extensively.

>You are advocating that Cobol should be dragged back to the 1970s C
>style with malloc() and free().

It's better than 1960s COBOL with perform 100-initialize thru
100-initialize-exit. I see that kind of crap code posted daily on CLC. They're
still teaching it in trade schools. 

>But the major problem with lists is that they _not_ the same as
>tables.  The lists are accessed serially, start at the base and step
…[3 more quoted lines elided]…
>items can be accessed together. Your lists can't do that (as easily).

They can if you build an index or tree around them. 

>You claimed a speed advantage for lists (only when compared to serial
>table access), but in fact there was none, or no significant
>difference, so one major claim for them disappears.
>
>The _only_ advantage is they are expandable. 

That's a significant advantage. 

> As I only use tables for
>small data items because large items there is _no_ advatage (for
…[4 more quoted lines elided]…
>    Non-standard and unsupported syntax, not always available.

The exact same syntax is available on Micro Focus, IBM and Fujitsu. Soon on all
2002 compilers. 

>    Serial only access.

Usually, that's all you need. If not, build a tree. 

>    C-like programming.

See above. 

>    Overly complex programming.

Overly is subjective. 

>    Obsolete mechanism replaced by OO

That's true. 

>    Risk of program failure in anything other than trivial use.

Is this your FUD argument? 

>    The 'next programmer' will be unfamiliar with it.

The maintenance programmer will probably know C as his first language. He'll
understand in a flash.  

Check your calendar. It is running 20 years slow.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-11T20:43:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b75v86$egd$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net>`

```
Robert Wagner wrote:

>>I find it predictable and useful that it doesn't initialize fillers.
> 
> It's not predictable when you change data-name to filler without
> understanding the consequences.

Yeah, but then _I_ read the manual.
 
>>> I _did_ advocate lists and there has been little substantive rebuttal.
>>
>>There has been 'little substantive rebuttal' that you haven't ignored
>>or dismissed.

> C-like, to my mind, means nested and telescoped functions. 

Nested ? are you thinking of Pascal perhaps ?

You can't do nested in C, though static can do interesting things.

'Telescoped' ? what's telescoped ?  Did you misunderstand 'scope' ?

> Pointers are
> not C-like, they are basic data structures. Assembly language programmers
> use them routinely without being accused of promoting 'C-style'.

It's the idiom.  You are using pointers in a C idiom.
 
>>Cobol has avoided the problems associated with pointers by only
>>introducing them to interract with software that requires their use,
…[3 more quoted lines elided]…
> extensively.

They may be available for any purpose, they were _introduced_ as an 
extension in order to interract with software that required them, such as 
Windows.

For example with MicroFocus they were first available in the early-release 
MS Windows programming pack.  The Windows API requires pointers to be used.

>>You are advocating that Cobol should be dragged back to the 1970s C
>>style with malloc() and free().
> 
> It's better than 1960s COBOL with perform 100-initialize thru
> 100-initialize-exit. 

Now there is a complete irrelevancy.

> I see that kind of crap code posted daily on CLC.

Daily ?  There has been a couple in the last month.

> They're still teaching it in trade schools.

I agree, I was appalled.  However, it is not a solution to try to get them 
to handle pointers when they can barely cope with simple stuff.  If they 
can't grok and/or then they will blow themselves up on 114 errors.
 
>>Tables can be accessed randomly, for example in binary chop, or two
>>items can be accessed together. Your lists can't do that (as easily).
> 
> They can if you build an index or tree around them.

More complexity, slower speed, more likelyhood of dangling pointers, memory 
leaks, 114 errors.

And it _still_ doesn't access two items at once.  You need to have two 
based items for that, or store away one into W-S and find the other.

Even more complexity, more chance of errors.

At least with a table if you get a bound check error the program tells you 
where it happened.  When a pointer goes awry you can get anything from 
complete silence with wrong output to blue screen (on systems with this 
feature).

>>The _only_ advantage is they are expandable.
> 
> That's a significant advantage.

It is _only_ an advantage if it is required.  I have never had any need for 
it, therefore there is no advantage (to me).

While you may well have particular items that you feel it does give an 
advantage to and therefore want to use them, you also want others to use 
them (in your 'best' practices) _regardless_ of whether expandability would 
be an advantage, and _regardless_ of the many, many disadvantages.

>>    Non-standard and unsupported syntax, not always available.
> 
> The exact same syntax is available on Micro Focus, IBM and Fujitsu. Soon
> on all 2002 compilers.

No.  While Fujitsu _may_ not disable the use of that code it is entirely 
unsupported and may not work in some versions and may be removed.  The 2002 
standard is different from what you have been using.

MF, FJ and IBM and _not_ 'all systems'.

>>    Serial only access.
> 
> Usually, that's all you need. If not, build a tree.

Building a tree is hugely more complex than a serially linked list.  It 
requires inserts, rotations and traveses.  This would make it significantly 
slower than a table load.

If you don't do rotations then ordered data turns it into a serially linked 
list with only the > pointer being used.

> Overly is subjective.

It is more complex and more error prone than a table.  Thus it is more 
complex (read overly) than code required to do the job.

>>    Risk of program failure in anything other than trivial use.
> 
> Is this your FUD argument?

No, it is not FUD.  Pointers are error prone and need careful attention, 
abd you are suggesting even more complexity with trees .

When items are malloc()ed to  the size of the text and the text changes 
then the this needs to be free()ed and a new item malloc()ed.  This gives 
plenty of scope for pointers to be danngling, especially when you also have 
trees, doubly linked lists and other refinements.
 
>>    The 'next programmer' will be unfamiliar with it.
> 
> The maintenance programmer will probably know C as his first language.
> He'll understand in a flash.

So you _do_ agree that it is all so C-like ?
 
> Check your calendar. It is running 20 years slow.

No one does C anymore, that was so 80s. For the last decade or so they have 
done OO C++ (and use objects not pointers) or have moved yet again onto 
Java.

And here is yet _another_ disadvantage: you can't use your lists with the 
intrinsic functions as you can the tables.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-11T14:38:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76k1a$o0f$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz>`

```

On 11-Apr-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > That's a significant advantage.
>
> It is _only_ an advantage if it is required.  I have never had any need for
> it, therefore there is no advantage (to me).

It is an advantage if it is used.

And it should be used when the advantages outweigh the disadvantages.   So far
this has been rare for me, never for you, and common for Robert Wagner.


> More complexity, slower speed, more likelyhood of dangling pointers, memory
> leaks, 114 errors.
…[4 more quoted lines elided]…
> Even more complexity, more chance of errors.

Agreed.   We don't need to turn CoBOL into C.   Almost every time where
something like this is warranted, we have other tools (such as databases) to
handle it.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T05:07:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e978267.65231865@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:

>> C-like, to my mind, means nested and telescoped functions. 
>
>Nested ? are you thinking of Pascal perhaps ?

Nested means one function calls another. You can do it in any laguage.

>'Telescoped' ? what's telescoped ?  Did you misunderstand 'scope' ?

It means functions telescoped within a single statement:  compute last-month =
function integer-to-date (function-date-to-integer (function int (date-today) -
30)). Look for multiple right parens at the end. 

>> I see that kind of crap code posted daily on CLC.
>
>Daily ?  There has been a couple in the last month.

Ok, I hyperbolized. 

>> They're still teaching it in trade schools.
>
>I agree, I was appalled.  However, it is not a solution to try to get them 
>to handle pointers when they can barely cope with simple stuff.  If they 
>can't grok and/or then they will blow themselves up on 114 errors.

Your point is valid. If I were teaching COBOL in trade school,  I'd first teach
them logic, which is NOT intuitive. Second, I'd teach program structure, also
not intuitive. Third, I'd teach COBOL. 

>And it _still_ doesn't access two items at once.  You need to have two 
>based items for that, or store away one into W-S and find the other.

This is true, and a source of frustration. 

>At least with a table if you get a bound check error the program tells you 
>where it happened.  When a pointer goes awry you can get anything from 
>complete silence with wrong output to blue screen (on systems with this 
>feature).

That hasn't happened in ten years, since we got memory-protected operating
systems. 

>>>The _only_ advantage is they are expandable.
>> 
…[3 more quoted lines elided]…
>it, therefore there is no advantage (to me).

I work with documents containing a variable number of variable-length 'words'
per line. They are printable reports. My problem is similar to that of a
compiler: figure out what the words mean, Usually they are numbers arranged in
columns. Variations include two-up (columns side by side), two-deep where the
right side of each line is pasted below, and many others. 

Variable length lines and words are important in this application. It would be
infeasible using tables. What's the maximum number of words on a line? 300? And
the maximum lines on a document? 5,000? Allowing 30 bytes per word, that's 45M
per document. In practice, I get by with less than 1 meg. 

> While Fujitsu _may_ not disable the use of that code it is entirely 
>unsupported and may not work in some versions and may be removed.  The 2002 
>standard is different from what you have been using.

Not much. We are required to set the 'based' pointer rather than 'address of'.
The change can be done mechanically. 

>MF, FJ and IBM and _not_ 'all systems'.

They're 98% of all COBOL compilers shipped. 

>When items are malloc()ed to  the size of the text and the text changes 
>then the this needs to be free()ed and a new item malloc()ed.  This gives 
>plenty of scope for pointers to be danngling, especially when you also have 
>trees, doubly linked lists and other refinements.

That's a problem. Text size doesn't change but array sizes sometimes do as other
programs 'discover' sparsely populated columns which weren't apparent at first.
I usually over-allocate three entries to allow room for expansion. 

>>>    The 'next programmer' will be unfamiliar with it.
>> 
…[3 more quoted lines elided]…
>So you _do_ agree that it is all so C-like ?

No, I think it is 'modern'  per Indian universities. 

>No one does C anymore, that was so 80s. For the last decade or so they have 
>done OO C++ (and use objects not pointers) or have moved yet again onto 
>Java.

I can't disagree except to say this is a COBOL forum, primarily COBOL '85. 

>And here is yet _another_ disadvantage: you can't use your lists with the 
>intrinsic functions as you can the tables.

I'd not used intrinsic functions until this week. Based on discussions here, I
actually changed a production program to use integer-of-date rather than calling
my own date function. And I'm about to impliment ORD-MAX in lieu of homegrown
code.  

When I think about intrinsic functions, they seem so un-COBOL like. If the
standards people  wanted to give us dates, why didn't they give us a date TYPE?
Then we really could 'add 1 to a date'. 

Intrinsic functions look like a political Band-Aid. Rather than improving the
language, they find workarounds.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-12T12:46:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304121146.2a1bc029@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote
> >> C-like, to my mind, means nested and telescoped functions. 
> >
> >Nested ? are you thinking of Pascal perhaps ?
> 
> Nested means one function calls another. You can do it in any laguage.

The term 'Nested functions' referes to defining a local function
within another function, such as can be done in Pascal and Java, but
not C.  Just like 'Nested Procedures' in Cobol.  This is a common and
long-standing usage.

Nested calls may be what you meant.
 
> >'Telescoped' ? what's telescoped ?  Did you misunderstand 'scope' ?
> 
> It means functions telescoped within a single statement:  compute last-month =
> function integer-to-date (function-date-to-integer (function int (date-today) 

That is nested calls.  Where did you get telescoped from ?

You have _almost_ got to:

compute date-plus-one =
   function integer-to-date(function date-to-integer(date-today) + 1
))

> That hasn't happened in ten years, since we got memory-protected operating
> systems. 

I thought that you used Windows ?    ;-)

From another thread:

RW>> Since I use pointers so much, I occasionally get a 114. It means
invalid
pointer.

> >It is _only_ an advantage if it is required.  I have never had any need for 
> >it, therefore there is no advantage (to me).
…[3 more quoted lines elided]…
> compiler: 

Well exactly, that is a specifici advantage to _you_, but not to me. 
You had been advocating the use of lists as a general replacement for
tables.  As I had said, define the requirements and _then_ choose an
implementation.

If there is a need for huge number of itsm and there is little
requirement for super high-speed then it may be more suitable to use
the Cobol built-in expandable data mechanism - the disk file.

> Variable length lines and words are important in this application. It would be
> infeasible using tables. What's the maximum number of words on a line? 300? And
> the maximum lines on a document? 5,000? Allowing 30 bytes per word, that's 45M
> per document. In practice, I get by with less than 1 meg. 

That may be what you get by multiplying 300 x 5000 x 30.  But why
would you do it with a complete table per line ?  There may be a max
of 300 but an average of , say, 20, so a single dimension table of
10000 words would do.  Just put the line number into the table item if
required, and/or have a table of line starts with 5000 index entries
pointing to the first word in each line.

> Not much. We are required to set the 'based' pointer rather than 'address of'.
> The change can be done mechanically. 

Maybe, but you may not get a 2002 compiler from all vendors at the
same time and will be constantly changing from on to another.
 
> They're 98% of all COBOL compilers shipped. 

Is this a reliable figure, like the 90% alive was ?
 
> >And here is yet _another_ disadvantage: you can't use your lists with the 
> >intrinsic functions as you can the tables.
…[4 more quoted lines elided]…
> code.  

Perhaps on a table ?    Max-Entry = FUNCTION ORD-MAX
(Entry-Table(ALL))

> When I think about intrinsic functions, they seem so un-COBOL like. 

When I think of linked lists I think they seem so un-Cobol like, well
actually C-like.  But that is because I used them in C for so many
years.

> If the
> standards people  wanted to give us dates, why didn't they give us a date TYPE?
> Then we really could 'add 1 to a date'. 

Well Duhh, they already _done_ that.  They gave you OO (well actually
vendors gave you OO and standards approved a version of these).

> Intrinsic functions look like a political Band-Aid. Rather than improving the
> language, they find workarounds.

It took you 14 years to discover intrinsic functions and 5 seconds to
judge them.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T23:31:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98a1a4.14569853@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote

>The term 'Nested functions' referes to defining a local function
>within another function, such as can be done in Pascal and Java, but
>not C.  Just like 'Nested Procedures' in Cobol.  This is a common and
>long-standing usage.

Ok. I wasn't familiar with the phrase because I don't work with Pascal (except
briefly, 20 years ago) nor Java. 

 >> >'Telescoped' ? what's telescoped ?  Did you misunderstand 'scope' ?
>> 
>> It means functions telescoped within a single statement:  compute last-month
=
>> function integer-to-date (function-date-to-integer (function int (date-today)

>
>That is nested calls.  Where did you get telescoped from ?

My own terminology. With all the parens, such statements look like a telescope.
And they don't read left to right, they read inside to outside. (Yes, I know how
to evaluate them left to right using a stack. My mind cannot readily push and
pop ideas.)

>You have _almost_ got to:
>
>compute date-plus-one =
>   function integer-to-date(function date-to-integer(date-today) + 1
>))

Yes, I did just that in a production program last week. It made me feel so
MODERN.  :)

It still requires two statements: accept date-today from date, followed by the
above. If they _really_ wanted to make it C-like, they'd permit COBOL verbs to
be nested inside:

compute tomorrow = 
 function date-of-integer(function integer-of-date (accept . from date)) + 1)

Can one do reference modification inside? If so, we get this (in)elegant code:

compute tomorrow = 
 function date-of-integer(function integer-of-date 
 (function int (function current-date)(1:8)) + 1)

>> That hasn't happened in ten years, since we got memory-protected operating
>> systems. 
>
>I thought that you used Windows ?    ;-)

When machines had only 16M, Microsoft did the best they could with limited
resources. The group most responsible for besmirching Windows were OEMs
clamoring for their buggy 16-bit drivers to run in privilege level 0. 

Windows has real memory protection. Despite its other failings, I've never seen
an _application_ program stomp on someone else's memory. 

>From another thread:
>
>RW>> Since I use pointers so much, I occasionally get a 114. It means
>invalid pointer.

There you go. At least machine/operating system caught the error. 

>> >It is _only_ an advantage if it is required.  I have never had any need for 
>> >it, therefore there is no advantage (to me).
…[8 more quoted lines elided]…
>implementation.

I advocate lists when the number of data elements is variable, as is usually the
case. When it is fixed, I use tables. 

>If there is a need for huge number of items and there is little
>requirement for super high-speed then it may be more suitable to use
>the Cobol built-in expandable data mechanism - the disk file.

Disk is for transport through time, not a substitute for data structures. This
site has a production program which uses a temporary indexed file solely as a
sorting mechanism. It inserts records then extracts them in order. At the end,
it deletes the file. Is that an example of your suggestion? <sticking finger in
throat and gagging>

>> Variable length lines and words are important in this application. It would
be
>> infeasible using tables. What's the maximum number of words on a line? 300?
And
>> the maximum lines on a document? 5,000? Allowing 30 bytes per word, that's
45M
>> per document. In practice, I get by with less than 1 meg. 
>
…[5 more quoted lines elided]…
>pointing to the first word in each line.

That's how I'd do it if pointers were not available. But why pad words out to 30
(which may not be big enough) and lines out to 512? It's wasted space that the
virtual memory manager will be unable to optimize out. Why? Just so I can use
the blunt instrument provided by tables?

>> Not much. We are required to set the 'based' pointer rather than 'address
of'.
>> The change can be done mechanically. 
>
>Maybe, but you may not get a 2002 compiler from all vendors at the
>same time and will be constantly changing from on to another.

I doubt IBM, Micro Focus and (maybe) Fujitsu will drop backward compatibility.
Even the standard gives it a nod with SET ADDRESS OF, which 'doesn't really mean
what it looks like'. No no, it's a 'syntactical feature'. It doesn't mean set
the address of, it means set the based pointer to. 

This is the kind of compromise we get from committees. Einstein said "no good
idea has ever been produced by a committee, but many have been killed by
committees". He got that right.
> 
>> They're 98% of all COBOL compilers shipped. 
>
>Is this a reliable figure, like the 90% alive was ?

No. Depends on your definition of 'shipped'. We covered this before. I should
have said 'in active use'.

>> >And here is yet _another_ disadvantage: you can't use your lists with the 
>> >intrinsic functions as you can the tables.
>> 
>> I'd not used intrinsic functions until this week. Based on discussions here,
I
>> actually changed a production program to use integer-of-date rather than
calling
>> my own date function. And I'm about to impliment ORD-MAX in lieu of homegrown
>> code.  
>
>Perhaps on a table ?    Max-Entry = FUNCTION ORD-MAX
>(Entry-Table(ALL))

Yes, in a table, exactly like your example. When I go through a document I'm
looking for columns of numbers. So I accumulate the columns where numbers begin
and end (because they may be left- or right-justified). The accumulator table
has 512 entries. Then I find the most frequently occurring (max) and it defines
a column. After zeroing accumulators left or right, depending on whether it was
leading or trailing, I look for the next most frequent. It defines a second
column of numbers. Analysis reiterates until the hit density is low. That's an
over-simplification which doesn't account for reports printed 2-up or '2-deep',
i.e. the report generator sliced lines and put the right side below. 

>> When I think about intrinsic functions, they seem so un-COBOL like. 
>
>When I think of linked lists I think they seem so un-Cobol like, well
>actually C-like.  But that is because I used them in C for so many
>years.

I used to think the same. Now I realize COBOL programmers have been impoverished
so long, they've forgotten what Real Programming looks like. They reject
pointers because 'that's not how we did it in the '70s and 80s'. They'd be
embarassed to phrase it that way, so they say 'use the appropriate tools for the
job'. Nobody could disagree that that. It's just rationalization. 

>> If the
>> standards people  wanted to give us dates, why didn't they give us a date
TYPE?
>> Then we really could 'add 1 to a date'. 
>
>Well Duhh, they already _done_ that.  They gave you OO (well actually
>vendors gave you OO and standards approved a version of these).

Yeahbut, in 1985 we didn't know about OO. They should have given us a date type
then. Database people did. 

>> Intrinsic functions look like a political Band-Aid. Rather than improving the
>> language, they find workarounds.
>
>It took you 14 years to discover intrinsic functions and 5 seconds to
>judge them.

I've seen them in manuals for years. I'm ashamed to admit I thought they were
vendor extensions rather than standards. Anyway, none of them seemed very
compelling. I could do the same with 'regular COBOL', so I ignored them. 

My newfound knowledge is not the existence of intrinsic functions, it is their
standardization.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-12T23:08:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7akb4$nq$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net>`

```
In article <3e98a1a4.14569853@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>riplin@Azonic.co.nz (Richard) wrote:
>

[snip]

>>When I think of linked lists I think they seem so un-Cobol like, well
>>actually C-like.  But that is because I used them in C for so many
…[6 more quoted lines elided]…
>job'. 

Mr Wagner, not only might a few people conclude that saying that the users
of a particular computer programming language are 'impoverished', 'have
forgotten what Real Programming (caps original) looks like', reject
certain techniques because of decades-old prejudices and distort what they
know to be truth (or, in common parlance, 'lie') about it is
'insulting'...

... but what you have admitted to learning here over the past few days 
seems to contradict this, as well.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T05:57:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98fb67.37552045@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com>`

```
ocdwarf@panix.com wrote:

>In article <3e98a1a4.14569853@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[9 more quoted lines elided]…
>>I used to think the same. Now I realize COBOL programmers have been
impoverished
>>so long, they've forgotten what Real Programming looks like. They reject
>>pointers because 'that's not how we did it in the '70s and 80s'. They'd be
>>embarassed to phrase it that way, so they say 'use the appropriate tools for
the
>>job'. 
>
…[8 more quoted lines elided]…
>seems to contradict this, as well.

I have admitted to learning here over the past few days about intrinsic
functions. That's all. 

Given that you obviously feel insulted, I suggest you learn pointers and the
benefits of dynamic, variable-length structures. Once you grok it, you'll never
go back.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-13T06:46:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7bf5j$64r$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com> <3e98fb67.37552045@news.optonline.net>`

```
In article <3e98fb67.37552045@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>ocdwarf@panix.com wrote:
>
…[30 more quoted lines elided]…
>functions. That's all. 

Good of you to admit this, Mr Wagner.

>
>Given that you obviously feel insulted, I suggest you learn pointers and the
>benefits of dynamic, variable-length structures. Once you grok it, you'll never
>go back. 

Mr Wagner, please try to read carefully.  What was made above was a 
subjunctive statement about interpretation, nothing more; if you wish to 
indulge in what some professionals refer to as 'projection' it might be 
appreciated were you to do so in a less public forum.

As for 'grokking'... how quaint!  I've noticed this term before... my 
memory is, admittedly, porous but if it serves me correctly this word was 
all the rage some forty or so years back... all the young hep-cats just 
thought it was the bee's knees!

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T16:55:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9995b6.77061831@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com> <3e98fb67.37552045@news.optonline.net> <b7bf5j$64r$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e98fb67.37552045@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[38 more quoted lines elided]…
>>benefits of dynamic, variable-length structures. Once you grok it, you'll
never
>>go back. 
>
…[8 more quoted lines elided]…
>thought it was the bee's knees!

[begin quote]
'Grok' means to understand so thoroughly that the observer becomes a part of the
observed - to merge, blend, intermarry, lose identity in group experience. It
means almost everything that we mean by religion, philosophy, and science - and
it means as little to us (because we are from Earth) as color means to a blind
man.
        Robert Heinlein, Stranger in a Strange Land

Since you raised the question of style, yours seems pedantic. You're long on
questions, short on conclusions. Rather than giving lessons on logical
inference, please share YOUR ideas about programming style, lists, tables,
functions, etc. as they relate to COBOL .... Mr. Dwarf, Sir.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-14T00:01:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7dbq3$jl1$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98fb67.37552045@news.optonline.net> <b7bf5j$64r$1@panix1.panix.com> <3e9995b6.77061831@news.optonline.net>`

```
In article <3e9995b6.77061831@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[57 more quoted lines elided]…
>        Robert Heinlein, Stranger in a Strange Land

Yes, that book was published in 1961... about forty years back.  Your 
quoting it shows that you might be a regular Joe, a good egg.

>
>Since you raised the question of style, yours seems pedantic.

Mr Wagner, I commented on a slang-term four decades old, nothing more, 
nothing less.  How you read what I type is of your own making... 
interpretation is in the mind of the beholder, last I looked.

>You're long on
>questions, short on conclusions.

I ask more than I preach?  How horrid... it might be seen as a ready 
symptom of the many answers I know I do not have.

>Rather than giving lessons on logical
>inference, please share YOUR ideas about programming style, lists, tables,
>functions, etc. as they relate to COBOL .... Mr. Dwarf, Sir.

Mr Wagner, you seem to contradict yourself... how is it that I can, in one 
sentence, 'be long on questions, short on conclusions' and in the next 
sentence I am 'giving lessons on logical inference'?

Oh... sorry, that was another question.  And please, it is not 'Sir', it 
was 'sergeant'... *my* parents were married.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T07:35:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9a6350.41397025@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98fb67.37552045@news.optonline.net> <b7bf5j$64r$1@panix1.panix.com> <3e9995b6.77061831@news.optonline.net> <b7dbq3$jl1$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>Oh... sorry, that was another question.  And please, it is not 'Sir', it 
>was 'sergeant'... *my* parents were married.

I was unaware that first cousins could legally wed in the UK.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-14T05:48:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7e068$jdp$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9995b6.77061831@news.optonline.net> <b7dbq3$jl1$1@panix1.panix.com> <3e9a6350.41397025@news.optonline.net>`

```
In article <3e9a6350.41397025@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[3 more quoted lines elided]…
>I was unaware that first cousins could legally wed in the UK. 

Mr Wagner, not everything is the same as it was where and when your 
antecedants encountered each other.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T08:22:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ejo4$cv5$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com> <3e98fb67.37552045@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e98fb67.37552045@news.optonline.net...

> >... but what you have admitted to learning here over the past few days
> >seems to contradict this, as well.
>
> I have admitted to learning here over the past few days about intrinsic
> functions. That's all.

Didn't the ability to use something other than literals as the starting
location and field length arguments to reference modification also fall into
this category?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T16:30:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9ae1e6.73808452@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com> <3e98fb67.37552045@news.optonline.net> <b7ejo4$cv5$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[10 more quoted lines elided]…
>this category?

No, I knew that. I said I'd seen only literals in other peoples' code.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:28:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80rmc$rqf$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com> <3e98fb67.37552045@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Given that you obviously feel insulted, I suggest you learn pointers and the
> benefits of dynamic, variable-length structures. Once you grok it, you'll
> never go back.

I learned pointers, and I would be very surprised if DD hasn't.   There art
times when they are appropriate.  In some languages they are more often the best
tool.

But when I discover a new useful tool, I don't use it to solve all problems.   I
do "go back" to my old tools when appropriate.

Relative files are a type of structure using pointers, and I used them over 20
years ago.  In CoBOL.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T16:40:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea41975.238159062@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7akb4$nq$1@panix1.panix.com> <3e98fb67.37552045@news.optonline.net> <b80rmc$rqf$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>Relative files are a type of structure using pointers, and I used them over 20
>years ago.  In CoBOL.

That's true. Good point.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T08:20:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ejkj$cr9$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e98a1a4.14569853@news.optonline.net...

> >That is nested calls.  Where did you get telescoped from ?
>
> My own terminology. With all the parens, such statements look like a
telescope.
> And they don't read left to right, they read inside to outside. (Yes, I
know how
> to evaluate them left to right using a stack. My mind cannot readily push
and
> pop ideas.)

Which explains why you don't like COMPUTE, or arithmetic expressions
(particularly with parentheses to ensure clarity of scope)!


> No. Depends on your definition of 'shipped'. We covered this before. I
should
> have said 'in active use'.

I haven't yet seen where you "covered this before", but I'd say the same
thing here:  the average large-server copy of a given COBOL compiler is
likely to see a heck of a lot more "active use" than the average copy on a
single-user desktop system.
> I've seen them in manuals for years. I'm ashamed to admit I thought they
were
> vendor extensions rather than standards. Anyway, none of them seemed very
> compelling. I could do the same with 'regular COBOL', so I ignored them.

Some you could, some you couldn't.  For example, WHEN-COMPILED is a bit
tough to get to with "regular COBOL", I'd warrant.  So is "offset of local
time, in hours and minutes, from coordinated universal time" as available
within CURRENT-DATE.  Many of the others *could* be handled using "regular
COBOL" -- presuming the implementation had "native" floating-point support
of some sort -- but calculating SIN, TAN and the other trig functions, as
well as LOG and LOG10 (with or without such support directly in COBOL)
would, I think, be far less obvious than simply referring to the function.
Why reinvent a wheel that the vendor has provided?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b45b1.99358779@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e98a1a4.14569853@news.optonline.net...
…[12 more quoted lines elided]…
>(particularly with parentheses to ensure clarity of scope)!

I dwell on logic much more than arithmetic. In logical expressions I insist on
parentheses when there are both ands and ors. 

>> No. Depends on your definition of 'shipped'. We covered this before. I
>should
…[5 more quoted lines elided]…
>single-user desktop system.

The disparity is more between free vs. expensive than it is between desktop vs.
mainframe. Millions of free (or nearly free) compilers are downloaded
('shipped') and then deleted or unused. 

>> I've seen them in manuals for years. I'm ashamed to admit I thought they
>were
…[4 more quoted lines elided]…
>tough to get to with "regular COBOL", I'd warrant.  

I've never fealt a tinge of requirement for that. What's it useful for? I
thought we used Change Management (aka Version Control) to perform that
function.

>So is "offset of local
>time, in hours and minutes, from coordinated universal time" as available
>within CURRENT-DATE. 

There are API functions which return GMT offset.

 Many of the others *could* be handled using "regular
>COBOL" -- presuming the implementation had "native" floating-point support
>of some sort -- but calculating SIN, TAN and the other trig functions, as
>well as LOG and LOG10 (with or without such support directly in COBOL)
>would, I think, be far less obvious than simply referring to the function.
>Why reinvent a wheel that the vendor has provided?

Personally, I've seldom needed trig or log functions. If I did, I would have
used  the vendor-provided function rather than coding a power series. One
function which would have been useful to me is linear regression. That should
have been number one on the want list.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-15T12:23:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7hm7u$2hta$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9b45b1.99358779@news.optonline.net...


> I dwell on logic much more than arithmetic. In logical expressions I
insist on
> parentheses when there are both ands and ors.

That's arguably more of an issue in COBOL than in some other languages, by
the way.  Most other higher-level languages (e.g., Fortran, ALGOL, PL/1,
Pascal, and of course the one that started the trend, C ;-)     ) apply
higher precedence to AND than to OR in evaluating Boolean/conditional
expressions; COBOL does not.  And this very point causes some decidedly
unobvious problems for the neophyte using *abbreviated* combined relation
conditions in particular!

> >Some you could, some you couldn't.  For example, WHEN-COMPILED is a bit
> >tough to get to with "regular COBOL", I'd warrant.
…[3 more quoted lines elided]…
> function.

I have seen this requirement imposed on companies from outside auditors --
the DATE-COMPILED on the compilation disting, the creation date and time of
the object code file as reflected in the disk file header records, and the
program's own perception of when it is compiled as reflected during
execution all had to match, and if they didn't match to the hundredth of a
second, the mismatch resulted in a Priority A Trouble Report against the
compiler, as the auditors would not certify the validity of the programs and
would not accept the financial reports they produced, thereby crippling the
company's financial operations.  Do I think this is short-sighted?  Yes.
Does it matter that I think it's short-sighted?  No, not a bit.

A historical note:  Unisys MCP/AS COBOL(68) programs had access to a variety
of compile-time date and time values over thirty years ago, and the reason
it had them is that people wanted them.  The only reason we didn't continue
them into our COBOL74 implementation is that they were unique to the Large
System architecture and weren't available in any sort of parallel form on
the Small and Medium Systems of the day.  Management decided (appropriately,
I think) that there needed to be a *corporate* standard for the extensions
beyond ANSI-74 COBOL, and that *all* of the extensions be available on *all*
then-current machines.  (Although the several implementations of the '68
standard all complied with that standard, their extensions were widely
disparate, and migration among our own systems was often difficult.  This
corporate standard was a very good thing, in my view).

 Moreover, the Large System intrinsic COMPILETIME (adopted in whole cloth
from the ALGOL implementation)  when supplied a parameter of 15 returned the
date part of DATE-COMPILED in a decidedly-unCOBOL fashion (six characters of
EBCDIC data in a word-oriented numeric item!), so at best it was hardly a
suitable candidate for corporate standardization.  Same for COMPILETIME(11),
returning 2.4-microsecond system clock ticks since midnight of the day on
which the compile occurred, or COMPILETIME(1), reflected in sixtieths of a
second when the system clocks with the finest resolution on Small and Medium
systems did their ticking in hundredths of a second.

<<There are API functions which return GMT offset.>>

What percentage of currently-in-existence COBOL programs do you think have
ready access to an API function that returns GMT offset?

> Personally, I've seldom needed trig or log functions. If I did, I would
have
> used  the vendor-provided function rather than coding a power series.

I haven't either; in my youth,  if you were going to do that much with such
functions in all probability you'd have written your programs in Fortran in
the first place.  But for those that do want them, FUNCTION SIN, FUNCTION
ATAN, FUNCTION LOG provide exactly what you'd be looking for.  The assertion
to which I was referring was that the intrinsic functions specified in the
1989 amendment could all be trivially coded directly in standard COBOL, with
a single exception.  My contention all along has been that ain't the case.

> One function which would have been useful to me is linear regression. That
should
> have been number one on the want list.

Are you sure that COBOL users desiring, say, linear regression analysis far
outnumber those who have need for, for example, internal standardized
support support for equal comparison of umlaut-U and UE in character
strings, or for a FLOATING leading "DM" as a valid currency symbol?   How
about such simple things as a vendor-supplied as-precise-as-possible
representation for PI and E, in a format appropriate for the destination?

The function list in the '89 amendment, as well as the function list in
ISO/IEC 1989:2002 reflect *user demand*, and I don't see any evidence that
the *user demand* for a linear regression analysis intrinsic function in
COBOL over the last couple of decades has been all that pressing.

Why should a linear regression analysis routine have been number one on
anyone's want list but yours?   If I'm writing a report program detailing
bank balances for a bank that included Venezuelan Bolivares among the
currencies it handled, which  you think it'd be more likely that I'd find
useful in that program --  "Bs." as a floating currency symbol, or direct
access to a linear regression analysis routine?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-16T03:35:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9cb23c.192696378@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[11 more quoted lines elided]…
>expressions; COBOL does not. 

Yes it does. AND is logical multiplication; OR is addition. AND takes precedence
over OR in COBOL. 

>And this very point causes some decidedly
>unobvious problems for the neophyte using *abbreviated* combined relation
>conditions in particular!

Not if (s)he uses parentheses. 

>I have seen this requirement imposed on companies from outside auditors --
>the DATE-COMPILED on the compilation disting, the creation date and time of
…[7 more quoted lines elided]…
>Does it matter that I think it's short-sighted?  No, not a bit.

That's all posturing. Testing who has the largest BSD (Big Swinging Dick). 

>A historical note:  Unisys MCP/AS COBOL(68) programs had access to a variety
>of compile-time date and time values over thirty years ago, and the reason
…[19 more quoted lines elided]…
>systems did their ticking in hundredths of a second.

Sounds like fertile ground for 'overloading' them with functions which return
'normal' values. As debated here recently (today), dates and times are not
integers. They should be returned as strings. 
>
><<There are API functions which return GMT offset.>>
>
>What percentage of currently-in-existence COBOL programs do you think have
>ready access to an API function that returns GMT offset?

Nearly all in the PC and Unix worlds. Few in the mainframe worlds, without
resorting to assembly language. 
>
>> Personally, I've seldom needed trig or log functions. If I did, I would
…[5 more quoted lines elided]…
>the first place.  

I wrote them in COBOL. My SIN function used three algorithms, depending on
whether you were asking at the low, medium or high end of the range. Such
optimization was heady stuff in those days. 

>> One function which would have been useful to me is linear regression. That
>should
…[7 more quoted lines elided]…
>representation for PI and E, in a format appropriate for the destination?

I don't see how they are exclusive. The others have nothing to do with
functions. 
OBOL is supposed to be a Business Oriented Language. Well, businesses compute
linear regression more often than trig functions. 
>
>The function list in the '89 amendment, as well as the function list in
>ISO/IEC 1989:2002 reflect *user demand*, and I don't see any evidence that
>the *user demand* for a linear regression analysis intrinsic function in
>COBOL over the last couple of decades has been all that pressing.

Delegates may have a different agenda than the businesses they represent. They
may be harkening back to school days, or trying to impress others. 

>Why should a linear regression analysis routine have been number one on
>anyone's want list but yours?   If I'm writing a report program detailing
…[3 more quoted lines elided]…
>access to a linear regression analysis routine?

As I said, they're not exclusive. If I'm at a retail company trying to ascertain
corellation between gross profit and various environmental factors, I need
linear regression.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-16T00:12:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ionr$lpj$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net>`

```
RW is correct and Chuck was in error (at least for  the '85 Standard), i.e.
that "AND" has precedence over "OR" in COBOL.  See the '85 Standard, page
VI-60 which states (in part),

"i.3.2.3 Precedence of Logical Operators and the Use of Parentheses
In the absence of the relevant parentheses in a complex condition, the
precedence (i.e., binding power) of the logical operators determines the
conditions to which the specified logical operators apply and implies the
equivalent parentheses. The order of precedence is 'NOT', 'AND', 'OR'. Thus,
Specifying 'condition-1 OR NOT condition-2 AND condition-3' implies and is
equivalent to specifying 'condition-1 OR ((NOT condition-2) AND
condition-3)'."
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-16T13:06:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7kd55$1oqh$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net> <b7ionr$lpj$1@slb6.atl.mindspring.net>`

```
You're right, Bill, and so is RW.  I don't see this rule in '74, where I've
run into the "right-to-left" evaluation issue in Abbreviated Combined
Relation Conditions.

    -Chuck Stevens


"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b7ionr$lpj$1@slb6.atl.mindspring.net...
> RW is correct and Chuck was in error (at least for  the '85 Standard),
i.e.
> that "AND" has precedence over "OR" in COBOL.  See the '85 Standard, page
> VI-60 which states (in part),
…[5 more quoted lines elided]…
> equivalent parentheses. The order of precedence is 'NOT', 'AND', 'OR'.
Thus,
> Specifying 'condition-1 OR NOT condition-2 AND condition-3' implies and is
> equivalent to specifying 'condition-1 OR ((NOT condition-2) AND
…[21 more quoted lines elided]…
> > >the way.  Most other higher-level languages (e.g., Fortran, ALGOL,
PL/1,
> > >Pascal, and of course the one that started the trend, C ;-)     ) apply
> > >higher precedence to AND than to OR in evaluating Boolean/conditional
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Logical Operator Precedence (was Re: Accuracy/Knowledge score-card)

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-16T14:33:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ki6e$1sh3$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net> <b7ionr$lpj$1@slb6.atl.mindspring.net> <b7kd55$1oqh$1@si05.rsvl.unisys.com>`

```
Found the rule, even in '74.  "AND" has higher precedence than "OR".

The issue I was referring to doesn't turn out to be one of precedence, but
of the rules for "expanding" abbreviated conditions.

For example,
    IF A = B AND C = D OR E OR F
is NOT evaluated as if it had been coded
    IF (A= B) AND
        ((C = D) OR (C = E) OR (C = F))
as a first glance might lead one to expect, but rather as if it had been
coded
    IF (A = B AND C = D) OR
        (C = E) OR
        (C = F)
because the truth value associated with the AND is determined before that
for the ORs.

IF C = E or C = F, regardless of the relationship between A and B, or
between C and D, the condition will evaluate to TRUE in COBOL.

RW's policy (as I recall it) of ALWAYS using parentheses whenever "AND" and
"OR" appear in a condition is a good one.

In my opinion, so is avoiding Abbreviated Combined Relation Conditions
altogether in the first place.  Abbreviations do NOT override the
precedence/association rules.  The abbreviations are expanded, and then the
precedence rules are applied.   That's an easy rule to forget, and an easy
one to miss in other people's code.

    -Chuck Stevens

<history snipped>
```

###### ↳ ↳ ↳ Re: Logical Operator Precedence (was Re: Accuracy/Knowledge score-card)

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:36:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea034b5.422739180@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net> <b7ionr$lpj$1@slb6.atl.mindspring.net> <b7kd55$1oqh$1@si05.rsvl.unisys.com> <b7ki6e$1sh3$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>RW's policy (as I recall it) of ALWAYS using parentheses whenever "AND" and
>"OR" appear in a condition is a good one.
…[5 more quoted lines elided]…
>one to miss in other people's code.

There is no reason to avoid ACRC, which I call elision, when parentheses are
used. It is expecially cohesive when testing a range: if (A not < 2 and not >
5). Also, when testing for a set: if (A = 2 or 3 or 4 or 5). Elisision is one of
the features that makes COBOL superior to all other programming languages.
```

###### ↳ ↳ ↳ Re: Logical Operator Precedence (was Re: Accuracy/Knowledge score-card)

_(reply depth: 17)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:37:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80s6g$s1o$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net> <b7ionr$lpj$1@slb6.atl.mindspring.net> <b7kd55$1oqh$1@si05.rsvl.unisys.com> <b7ki6e$1sh3$1@si05.rsvl.unisys.com> <3ea034b5.422739180@news.optonline.net>`

```

On 18-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> There is no reason to avoid ACRC, which I call elision, when parentheses are
> used. It is expecially cohesive when testing a range: if (A not < 2 and not >
> 5). Also, when testing for a set: if (A = 2 or 3 or 4 or 5). Elisision is one
> of
> the features that makes COBOL superior to all other programming languages.

I'm unfamiliar with the term "elision".  What does it mean?
```

###### ↳ ↳ ↳ Re: Logical Operator Precedence (was Re: Accuracy/Knowledge score-card)

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T02:57:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea46c28.259333101@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net> <b7ionr$lpj$1@slb6.atl.mindspring.net> <b7kd55$1oqh$1@si05.rsvl.unisys.com> <b7ki6e$1sh3$1@si05.rsvl.unisys.com> <3ea034b5.422739180@news.optonline.net> <b80s6g$s1o$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 18-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[7 more quoted lines elided]…
>I'm unfamiliar with the term "elision".  What does it mean?

It means "the act or an instance of omitting something" [Merriam-Webster]. 

In the COBOL 68 era, we could elide the logical operator as well: 
if (A = 2 3 4 or 5).
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-16T20:59:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-03458D.20591516042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3e9cb23c.192696378@news.optonline.net>`

```
In article <3e9cb23c.192696378@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

> ><<There are API functions which return GMT offset.>>
> >
…[4 more quoted lines elided]…
> resorting to assembly language. 

I'm pretty sure you get this with CURRENT-DATE.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2003-04-16T17:02:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9DC500.8040708@newsguy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
 > Most other higher-level languages (e.g., Fortran, ALGOL, PL/1,
 > Pascal, and of course the one that started the trend, C ;-)     )
 > apply higher precedence to AND than to OR in evaluating
 > Boolean/conditional expressions; COBOL does not.

While logical-and technically has higher precedence than logical-or in
C, which may have consequences for parsing expressions, as far as
evaluation goes their relative precedence is moot because the two both
guarantee left-to-right evaluation, a sequence point after the left
operand is evaluated, and short-circuiting.  See ISO 9899-1990 6.3.13
and 6.3.14.

Try this C snippet:

-----
#include <stdio.h>

int a(void) {puts("in a"); return 1;}
int b(void) {puts("in b"); return 0;}
int c(void) {puts("in c"); return 1;}

int main(void)
{
    int result = a() || b() && c();
    printf("result is %d\n", result);
    return 0;
}
-----

If you compile and run this, you'll see:

	in a
	result is 1

The expression "b() && c()" is never evaluated; functions b and c are
not invoked.  If you change a() to return 0 instead, a and b will be
invoked, but not c.

IIRC, Pascal is broken in some manner regarding the evaluation of
logical operators, but I've forgotten the details.  It's been a long
time since I did anything with Pascal.  Does it not short-circuit,
perhaps?  Or maybe it evaluates expressions with mixed logical-and and
logical-or by treating logical-and as having a higher precedence for
evaluation, rather than using strict left-to-right order?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-04-16T16:33:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7klo0$20igu$1@ID-184804.news.dfncis.de>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3E9DC500.8040708@newsguy.com>`

```
My recollection of my 9th grade Pascal is that Pascal does not short
circuit, just as you state.  Given the following (and pardon if I don't have
my Pascal quite write; it's been quite a while):

if (func1(abcd) = true and func2(abcd) = true)
  then println('both are true!');
  else println('one or the other or both are not true');

Not only with both func1 and func2 be called regardless of the results of
the other function, but func2 may be called before func1 is called.

Now I don't know if this is part of the Pascal language standard or if it
was a 'feature' of the Pascal we were using (can't remember the exact
compiler name, but we were using Apple IIe computers!).

And of course there's the possibility that I'm mis-remembering!  I do
specifically remember learning about how Pascal does not 'short circuit',
though, while other languages do.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation

>>> Michael Wojcik<mwojcik@newsguy.com> 04/16/03 03:02PM >>>
Chuck Stevens wrote:
 > Most other higher-level languages (e.g., Fortran, ALGOL, PL/1,
 > Pascal, and of course the one that started the trend, C ;-)     )
 > apply higher precedence to AND than to OR in evaluating
 > Boolean/conditional expressions; COBOL does not.

While logical-and technically has higher precedence than logical-or in
C, which may have consequences for parsing expressions, as far as
evaluation goes their relative precedence is moot because the two both
guarantee left-to-right evaluation, a sequence point after the left
operand is evaluated, and short-circuiting.  See ISO 9899-1990 6.3.13
and 6.3.14.

Try this C snippet:

-----
#include <stdio.h>

int a(void) {puts("in a"); return 1;}
int b(void) {puts("in b"); return 0;}
int c(void) {puts("in c"); return 1;}

int main(void)
{
    int result = a() || b() && c();
    printf("result is %d\n", result);
    return 0;
}
-----

If you compile and run this, you'll see:

	in a
	result is 1

The expression "b() && c()" is never evaluated; functions b and c are
not invoked.  If you change a() to return 0 instead, a and b will be
invoked, but not c.

IIRC, Pascal is broken in some manner regarding the evaluation of
logical operators, but I've forgotten the details.  It's been a long
time since I did anything with Pascal.  Does it not short-circuit,
perhaps?  Or maybe it evaluates expressions with mixed logical-and and
logical-or by treating logical-and as having a higher precedence for
evaluation, rather than using strict left-to-right order?
```

###### ↳ ↳ ↳ Pascal "early exit" in Boolean expressions (was: Re: Accuracy/Knowledge score-card)

_(reply depth: 14)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-16T16:35:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7kpbs$21bd$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net> <b7ejkj$cr9$1@si05.rsvl.unisys.com> <3e9b45b1.99358779@news.optonline.net> <b7hm7u$2hta$1@si05.rsvl.unisys.com> <3E9DC500.8040708@newsguy.com> <b7klo0$20igu$1@ID-184804.news.dfncis.de>`

```
I found standards for "regular" Pascal and "Extended" Pascal at
http://www.moorecad.com/standardpascal/standards.html in downloadable form.

It appears to me that in (regular) Pascal the implementor gets to decide
whether "early exit" happens during evaluation of a Boolean expression or
not for AND and OR (ISO/IEC 7185:1990 Page 48).

Extended Pascal has AND_THEN and OR_ELSE logical operators in which the
"right part" is ONLY evaluated if the he "left part" fails to determine the
value of the expression (ISO/IEC 10206:1990 Page 88).

However, I don't see a requirement for AND and OR that the "right part" must
unconditionally be evaluated; that appears to be left to the implementor as
it was in "regular" Pascal.

I may well be wrong, but that's how I read the standards.

    -Chuck Stevens


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:b7klo0$20igu$1@ID-184804.news.dfncis.de...
> My recollection of my 9th grade Pascal is that Pascal does not short
> circuit, just as you state.  Given the following (and pardon if I don't
have
> my Pascal quite write; it's been quite a while):
>
…[73 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:23:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80rd9$rpv$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com> <3e98a1a4.14569853@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> I used to think the same. Now I realize COBOL programmers have been
> impoverished
…[4 more quoted lines elided]…
> job'. Nobody could disagree that that. It's just rationalization.

Nobody could disagree with that?   I agree that your statement is just a
rationalization, but I certainly disagree with your conclusion.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:19:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80r5f$rj3$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <217e491a.0304121146.2a1bc029@posting.google.com>`

```

On 12-Apr-2003, riplin@Azonic.co.nz (Richard) wrote:

> Well exactly, that is a specifici advantage to _you_, but not to me.
> You had been advocating the use of lists as a general replacement for
…[5 more quoted lines elided]…
> the Cobol built-in expandable data mechanism - the disk file.

I very much like the above response, and decided it should be repeated.
```

###### ↳ ↳ ↳ Please DOCUMENT this (was: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-12T21:14:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ah73$3lu$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e978267.65231865@news.optonline.net...
> Richard Plinston <riplin@Azonic.co.nz> wrote:
>
> >Robert Wagner wrote:
>
<snip>
> >MF, FJ and IBM and _not_ 'all systems'.
>
> They're 98% of all COBOL compilers shipped.
>

We have been thru this one before.

A) Please provide any documentation for this claim.

B) Please provide information on how many users (programmers) use the
average compiler provided by each of this vendors (i.e. for Windows, 1
programmer per compiler / for IBM mainframe 20-200 programmers per compiler)

C) Please provide information on how many end-users use the output from each
of these individual compilers.

***

Bottom-Line:
   This statistic has little or no basis in fact, but even if "true" it
means almost nothing, i.e. "number of COBOL compilers shipped" has little or
no relationship to number of programmers using said compilers much less end
users using the output of such compilers.
```

###### ↳ ↳ ↳ Re: Please DOCUMENT this (was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T05:57:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98ede9.34097740@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <b7ah73$3lu$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

You're right. I said to Richard, 'the test should be how many are actively being
used.'

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e978267.65231865@news.optonline.net...
…[27 more quoted lines elided]…
>users using the output of such compilers.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T07:30:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7egmm$ao4$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e978267.65231865@news.optonline.net...

> >MF, FJ and IBM and _not_ 'all systems'.
>
> They're 98% of all COBOL compilers shipped.

A meaningless statistic.  How many *lines of COBOL code currently in
production use* are compiled with each?  How many programmers share the same
copy of each of these varieties of COBOL compiler at any given time?

My strong suspicion is that, in general, a single licensed copy of a given
COBOL compiler on a large traditional enterprise server process a heck of a
lot more lines of code per unit time, and has a heck of a lot more
simultaneous users, than the average Micro Focus or Fujitsu compiler on a
Wintel system.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b4adc.100681998@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net> <b7egmm$ao4$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[14 more quoted lines elided]…
>Wintel system.

You're right, and I apologize in advance for the perceived affront to Unisys.
It's not so much Micro  Focus, its the freebies.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-14T18:02:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304141702.657052c@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b75v86$egd$1@aklobs.kc.net.nz> <3e978267.65231865@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >MF, FJ and IBM and _not_ 'all systems'.
> 
> They're 98% of all COBOL compilers shipped. 

I suspect that OpenCobol, TinyCobol and Kobol _ship_ the majority of
compilers on any given day.
When you make up statistics like this you simply reduce your
credability, not that it could get much lower.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-11T07:33:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7696e$3vc$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net>`

```
In article <3e9618c9.359208255@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>riplin@Azonic.co.nz (Richard) wrote:
>
…[12 more quoted lines elided]…
>programs in it. 

Mr Wagner, our experiences on this are *very* different; from what I have 
seen a contractor/consultant/hired gun is often given only the most 
tedious, most unpleasant, ugliest problems that all the in-house personnel 
(sometimes referred to as 'indigenous fauna') have had a whack at - and 
failed - and the possible solution-paths are then described as 'simple' 
and 'all ya gotta do is...'.

It might be a good thing, Mr Wagner, to learn that generalising from one's 
own experience - the leap from 'I have seen' to 'It *is* this way' - can 
generate readily conclusions that are logically fallacious and empirically 
disproveable.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9816c6.103221550@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b7696e$3vc$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e9618c9.359208255@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[26 more quoted lines elided]…
>disproveable.

My contracting experience has been five recent gigs, about one year each, at
very large (Fortune 50) companies and government agencies. At all five, the
reason for using contractors rather than indigenous was a short time horizon. In
four out of five, the project was scheduled to end within a year. In the other,
contractors were sacrificial goats for the predictable annual 10% staff
reduction.

I've not seen _developers_ assigned to the most tedious, most unpleasant,
ugliest problems. I have seen that happen in production support, test teams and
documentation administration, which tend to be staffed by failed programmers ...
about half from India and Russia, the rest locals. 

There is definitely a Class distinction between employees and contractors. When
a contractor says something derogatory about an perm, (s)he is gone the next
day. It doesn't matter whether the contractor is right or wrong. Contractors can
also be convenient scapegoats for production errors when managers demand the
guilty be punished. 

Positives are earning twice as much money and an annual change of geographical
and technical scenery. If I'd stayed in one place the last five years, I
wouldn't have experience with DB2 _and_ Informix _and_ Oracle _and_ Sybase
(which aren't very different, but recruiters think they are).
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-12T23:12:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7akip$3ec$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9618c9.359208255@news.optonline.net> <b7696e$3vc$1@panix1.panix.com> <3e9816c6.103221550@news.optonline.net>`

```
In article <3e9816c6.103221550@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[35 more quoted lines elided]…
>reduction.

How very nice for you... but your experience is, by definition, as
anecdotal as anyone else's.  As was stated before, though... it might be a
good thing, Mr Wagner, to learn that generalising from one's own
experience - the leap from 'I have seen' to 'It *is* this way' - can
generate readily conclusions that are logically fallacious and empirically
disproveable.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T05:57:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98e4b6.31742798@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9618c9.359208255@news.optonline.net> <b7696e$3vc$1@panix1.panix.com> <3e9816c6.103221550@news.optonline.net> <b7akip$3ec$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e9816c6.103221550@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[16 more quoted lines elided]…
>>>>You make it sound as though work was parceled out based on personality.
That's
>>>>not how it works. When a contractor is put on a system, he has access to all
>>>>programs in it. 
…[15 more quoted lines elided]…
>>reason for using contractors rather than indigenous was a short time horizon.
In
>>four out of five, the project was scheduled to end within a year. In the
other,
>>contractors were sacrificial goats for the predictable annual 10% staff
>>reduction.
…[6 more quoted lines elided]…
>disproveable.

I'll grant my conclusions may be hasty. How large a sample does it take? Keep in
mind, the sigma between US companies isn't very big.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-13T06:49:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7bfb8$6fs$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9816c6.103221550@news.optonline.net> <b7akip$3ec$1@panix1.panix.com> <3e98e4b6.31742798@news.optonline.net>`

```
In article <3e98e4b6.31742798@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[51 more quoted lines elided]…
>I'll grant my conclusions may be hasty.

Mst gracious of you to admit this, Mr Wagner.

>How large a sample does it take? Keep in
>mind, the sigma between US companies isn't very big. 

I am not sure what you are referring to as 'it' here, Mr Wagner, and as 
such I cannot answer with any precision.  Regarding this 'sigma' you refer 
to, though... on what are you basing your conclusion about its size?

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T16:55:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e999562.76977698@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9816c6.103221550@news.optonline.net> <b7akip$3ec$1@panix1.panix.com> <3e98e4b6.31742798@news.optonline.net> <b7bfb8$6fs$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e98e4b6.31742798@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[12 more quoted lines elided]…
>>>>>>>> >> 2) Hadn't seen any (many?) reference modifications where the
starting
>>>>>>>> >> position or length was a variable - much less an arithmetic
expression
>>>>>>>> 
>>>>>>>> I haven't .. in large mainframe shops with thousands of programs. 
…[6 more quoted lines elided]…
>>>>>>not how it works. When a contractor is put on a system, he has access to
all
>>>>>>programs in it. 
>>>>>
…[14 more quoted lines elided]…
>>>>reason for using contractors rather than indigenous was a short time
horizon.
>>In
>>>>four out of five, the project was scheduled to end within a year. In the
…[20 more quoted lines elided]…
>to, though... on what are you basing your conclusion about its size?

It is based on the fact that organizations consciously copy each others' style.
They call it 'benchmarking' and 'best practice'. IT departments formalize
procedures in a written 'methodology', thereby making it easier to copy and
distribute. Three of five organizations where I contracted used CMM level 3. A
fourth used a similar methodology.

Therefore, it seems reasonable to extrapolate my observations to US IT shops
using formal methodologies.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-14T00:05:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7dc1k$kj9$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98e4b6.31742798@news.optonline.net> <b7bfb8$6fs$1@panix1.panix.com> <3e999562.76977698@news.optonline.net>`

```
In article <3e999562.76977698@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
>>In article <3e98e4b6.31742798@news.optonline.net>,
>>Robert Wagner <robert@wagner.net> wrote:

[snip]

>>>I'll grant my conclusions may be hasty.
>>
…[16 more quoted lines elided]…
>using formal methodologies. 

Mr Wagner, you seem to find it a reasonable thing to extrapolate your 
personal experience with three or four companies to a generalised 'US 
companies'... and yet this does not seem to take into account that 
consultants/contractors/hired guns, by the nature of their employ, tend to 
see the insides of more 'sick' shops than healthy ones.  Do you believe 
that this tendency might possibly have an effect on the sample to which 
you have been exposed?

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:40:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80scs$s8c$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b7696e$3vc$1@panix1.panix.com> <3e9816c6.103221550@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> There is definitely a Class distinction between employees and contractors.
> When
> a contractor says something derogatory about an perm, (s)he is gone the next
> day. It doesn't matter whether the contractor is right or wrong.

I've been a contractor more often than I have been an employee.  I haven't seen
this.

In cases where you have seen this happen, were you on the employee side, or the
contractor side?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T16:40:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea41a49.238371452@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b7696e$3vc$1@panix1.panix.com> <3e9816c6.103221550@news.optonline.net> <b80scs$s8c$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[6 more quoted lines elided]…
>this.

I've seen contractors fired for that reason on every project (5). I've never
been fired.

>In cases where you have seen this happen, were you on the employee side, or the
>contractor side?

I was a contractor.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-11T14:06:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76i5n$naj$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net>`

```

On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >I find it predictable and useful that it doesn't initialize fillers.
>
> It's not predictable when you change data-name to filler without understanding
> the consequences.

I suppose programming is never predictable when you make any changes without
understanding the consequences.

On the other hand, it is quite predictable when we do understand the
consequences.   Manuals and experience are useful tools.  If you have brand new
programmers, I suggest you make sure they have access to manuals.

They can even be useful for us old-timers.


> >Cobol has avoided the problems associated with pointers by only
> >introducing them to interract with software that requires their use,
> >such as Windows.
>
> Nope. They're available to application programmers. I use them extensively.

I don't.   So manuals will be useful when I want to use pointers.

I do use FILLER extensively though.


> It's better than 1960s COBOL with perform 100-initialize thru
> 100-initialize-exit. I see that kind of crap code posted daily on CLC. They're
> still teaching it in trade schools.

I fought when EDS had that as a standard in the late 1970s.   But I lost and had
to code by their standards while I worked for them.

I suppose you have had to use practices that you felt were less than optimal as
well.  If not, you are unusual.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9822f0.106335061@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
>> It's not predictable when you change data-name to filler without
understanding
>> the consequences.
>
…[5 more quoted lines elided]…
>programmers, I suggest you make sure they have access to manuals.

Shops where I've worked don't give programmers any manuals. The only reference
books programmrs have were purchased from bookstores or Amazon. I have a 60
pound box of such books. When we get lucky, we find manuals on Web sites. But
management thinks we're wasting time when we use the Web, so they try to block
access. At one site, every time I needed to look something up in the Micro Focus
manuals, I had to go home.

>I fought when EDS had that as a standard in the late 1970s.   But I lost and
>had to code by their standards while I worked for them.

Having recently worked on an EDS project, I can report they're still using that
obsolete COBOL programming standard. I ignored it. When challenged by a team
lead (once), I said I didn't know it existed. <G>

>I suppose you have had to use practices that you felt were less than optimal as
>well.  If not, you are unusual.

Fortunately for us COBOL programmers, today's managers and team leads come from
non-COBOL cultures. As a result, they don't understand what the COBOL
programming standard says, nor think it important to enforce it. They just want
to 'get that old code out the door' as expeditiously as possible. 

In-house C standards are a different story. They _are_ enforced because managers
understand them. I hate wasting a whole line for a trailing scope delimiter
(curly bracket). It reduces video 'real estate' -- the amount of code one can
see on a screen. They kept insisting I waste the line, because the standard said
to.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-12T16:22:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E98839C.9020301@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net>`

```
Robert Wagner wrote:
> Shops where I've worked don't give programmers any manuals. The only reference
> books programmrs have were purchased from bookstores or Amazon. I have a 60
…[3 more quoted lines elided]…
> manuals, I had to go home.

I would protest loudly for manuals if they weren't there...  They're 
invaluable, not only for the more experienced programmer finding the 
more advanced features, but for letting the aforementioned more 
experienced programmer stop having to answer a bunch of questions from 
those less experienced.  :)

We work in a UNISYS 2200/ClearPath environment, and since HMP IX 5.1 (an 
operating system, which is up to 8.0 now), they've had a CD with all the 
manuals in PDF, with a pretty good menu interface.  They're great - we 
put the all files on a share, then tell the other programmers to map to 
it and go nuts...

(Of course, it helps that the UNISYS manuals are pretty good, too...  I 
haven't noticed any "documentation vs. behavior" problems that you've 
alluded to with some other compilers.)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T01:29:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98ae59.17823141@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net>`

```
LX-i <DanielJS@Knology.net> wrote:

>Robert Wagner wrote:
>> Shops where I've worked don't give programmers any manuals. The only
reference
>> books programmrs have were purchased from bookstores or Amazon. I have a 60
>> pound box of such books. When we get lucky, we find manuals on Web sites. But
>> management thinks we're wasting time when we use the Web, so they try to
block
>> access. At one site, every time I needed to look something up in the Micro
Focus
>> manuals, I had to go home.
>
…[4 more quoted lines elided]…
>those less experienced.  :)

Contractors are not permitted to "protest loudly". If they try, they're seen as
troublemakers/malcontents and summarily dismissed. We have to endure the
disrespect that management lays on us without comment. 

When they staff a project, they usually include a few Old Pros like me to rescue
low paid recent college grads when they get in trouble. But they don't give us
any manuals. We're supposed to KNOW this stuff. So I go home to consult manuals.
In Montgomery, it was less than ten minutes from downtown to the Eastern exit,
where I lived.
```

###### ↳ ↳ ↳ Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-12T21:08:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7agqp$dbf$1@slb1.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net>`

```
In this day and age, most of the shops that I know use compilers with
"online" versions of their documentation. (They may or may not ALSO provide
hard-copy versions).

In mainframe environments, documentation is usually available to all
programmers via a central "server" or "mainframe" application.  This may be
in addition to online (web) versions - such as those provided by IBM.

In PC and Unix environments, I don't know of ANY *purchasable* compiler that
doesn't come with "optional" machine readable documentation.  There might be
one, but I don't know of such.

If either a contractor or an in-house programmer doesn't have access to the
appropriate manual, the chances are that is only because he/she hasn't asked
where it is.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T05:57:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98e977.32959650@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net>`

```
How about when management blocks access to the Web with a 'reverse firewall'? It
happens every day. They think we're frittering away time viewing entertainment
or porn. I didn't drive home to view manuals because I was too stupid to ask
where they were; I did it because they were unavailable at work. 

Mainframes usually have Bookmanager online. It's a poorly designed product
offering NO search at the highest level. If you can figure out which manual the
answer is in, then it works fine. But there are a dozen COBOL manuals. 

"William M. Klein" <wmklein@ix.netcom.com> wrote:

>In this day and age, most of the shops that I know use compilers with
>"online" versions of their documentation. (They may or may not ALSO provide
…[58 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T08:02:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7eii8$c3g$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e98e977.32959650@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e98e977.32959650@news.optonline.net...

> Mainframes usually have Bookmanager online. It's a poorly designed product
> offering NO search at the highest level. If you can figure out which
manual the
> answer is in, then it works fine. But there are a dozen COBOL manuals.

They do?  Really?  And all these years I thought I was accessing the Unisys
MCP/AS documentation through Adobe on a Windows share.  Silly me.

        -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b4dfe.101483861@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e98e977.32959650@news.optonline.net> <b7eii8$c3g$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e98e977.32959650@news.optonline.net...
…[7 more quoted lines elided]…
>MCP/AS documentation through Adobe on a Windows share.  Silly me.

Once again I succumbed to equating mainframe with IBM. A thousand pardons.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-04-14T21:25:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9B5F89.8020705@ix.netcom.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e98e977.32959650@news.optonline.net> <b7eii8$c3g$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> "Robert Wagner" <robert@wagner.net> wrote in message
> news:3e98e977.32959650@news.optonline.net...
…[15 more quoted lines elided]…
> 

And I have a pack of CDs from IBM that is ALL PDF. Hmmmm. I think 
I have COBOL manuals in PDF.... Well, wadda-u-know, GC26-9045-02 
in PDF, GC26-9044-02 in PDF, GC26-4764-05 in PDF... Which 
translates to "COBOL for OS/390 & VM V2R2 Customization under 
OS/390", "COBOL for OS/390 & VM V2R2 Licensed Program Specs 
(LPS)", and "COBOL for OS/390 & VM V2R2 - COBOL for MVS & VM V2R2 
Compiler and Run-Time Migration Guide". And lookie there, they 
are even in PDF from IBM's web site!
www-1.ibm.com/servers/eserver/zseries/zos/bkserv/zswpdf/vacobol22.html
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:50:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80sus$sbp$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e98e977.32959650@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> How about when management blocks access to the Web with a 'reverse firewall'?
> It
> happens every day. They think we're frittering away time viewing entertainment
> or porn. I didn't drive home to view manuals because I was too stupid to ask
> where they were; I did it because they were unavailable at work.

While I haven't contracted to companies that allowed me to ignore standards, I
also haven't contracted to companies that refused to make documentation
available when I asked.   Sometimes it hasn't arrived in a timely manner.  
Oddly enough, I have had harder time getting manuals as an employee than as a
contractor.

> Mainframes usually have Bookmanager online. It's a poorly designed product
> offering NO search at the highest level. If you can figure out which manual
> the
> answer is in, then it works fine. But there are a dozen COBOL manuals.

I agree.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T20:38:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e99c971.2000152@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>In this day and age, most of the shops that I know use compilers with
>"online" versions of their documentation. (They may or may not ALSO provide
…[12 more quoted lines elided]…
>where it is.

That was my first question. The manager gestured toward someone's bookshelf and
said "Most programmers buy them at Barnes & Noble".
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-13T15:48:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7cifj$1b1$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e99c971.2000152@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
<snip>
> >
> >If either a contractor or an in-house programmer doesn't have access to
the
> >appropriate manual, the chances are that is only because he/she hasn't
asked
> >where it is.
>
> That was my first question. The manager gestured toward someone's
bookshelf and
> said "Most programmers buy them at Barnes & Noble".

I know that you have worked at a number of shops with a number of different
compilers.  For which compiler did the manager respond this way?

1) For IBM, this doesn't make sense because IBM manuals are *NOT* available
at "bookstores"

2) For PC (Fujitsu and Micro Focus), this doesn't make sense as the
documenation is available electronically with the software.

   ***

The fact that the manager's response doesn't make sense, doesn't mean that I
am doubting your report - as manager statements often don't.  I simply am
trying to understand what type of environment (today) doesn't provide easy
access to all programmers of the manuals.

P.S.  Regarding IBM's BookManager, if you bring up the correct bookshelf,
there is a SEARCH ALL facility that lets you find a word, phrase, whatever,
throughout the bookshelf - not just in a specific manual.  When working with
an IBM mainframe shop (with a firewall), check to see how they have their
internal bookshelves set up.  It is also possible to purchase the ENTIRE IBM
bookshelf (of all z/OS or OS/390) manuals for $150 (as I recall) on CD-rom.
I would think that a contractor who frequently works at shops without "easy"
access to these manuals would buy this as a business expense.  OTOH, I don't
know of any IBM mainframe shops where all programmers don't have easy access
to the full documentation set "easily" available.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T22:56:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e99d843.5795019@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net> <b7cifj$1b1$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e99c971.2000152@news.optonline.net...
…[15 more quoted lines elided]…
>compilers.  For which compiler did the manager respond this way?

Micro Focus. Also HP-UX, Informix and Pro-C. He thought 'popular press' books
were as good as manuals.

In case you think this was in some technical backwater, he worked for EDS and
the client was US Dept of Education. 

>1) For IBM, this doesn't make sense because IBM manuals are *NOT* available
>at "bookstores"
>
>2) For PC (Fujitsu and Micro Focus), this doesn't make sense as the
>documenation is available electronically with the software.

We didn't have it installed. Micro Focus was also available on the Web (then on
the Merant site). Most programmers didn't have access to the Web, only the
organization's intranet. My solution was my home computer. 

Lack of Web access was a serious problem for production support folks, because
they often needed to download updated device drivers and other software fixes.
Their solution was modems. Think about the security implications. They are on
the network inside the firewall, have lots of server-side function on their
machines, and have just provided an open path for ANYone to get into the
network. They've made an end-run around all firewalls. Attempting to make the
network secure by denying Web access ironically made it completely insecure. 

>   ***
>
…[3 more quoted lines elided]…
>access to all programmers of the manuals.

I see it as a sign of disrespect toward programmers .. but that's just my
sardonic take.

>P.S.  Regarding IBM's BookManager, if you bring up the correct bookshelf,
>there is a SEARCH ALL facility that lets you find a word, phrase, whatever,
>throughout the bookshelf - not just in a specific manual.

Yes, that's what I meant when I said manual. The problem is finding the
bookshelf. IBM has a plethora of them and its not always evident which covers
the topic of interest. An attempted remedy at one place was a supplemental flat
file listing manual titles on each bookshelf. One could search on "COBOL" and
find a dozen bookshelves containing COBOL manuals. Eliminating irrelevant
operating systems narrowed it to perhaps half a dozen.

The system really needs a consolidated index. I realize there are installation,
'mounting' and security issues involved.

> When working with
>an IBM mainframe shop (with a firewall), check to see how they have their
…[5 more quoted lines elided]…
>to the full documentation set "easily" available.

Both mainframe shops where I worked recently DID make BookManager available to
all. Absence of manuals is a problem in Unix environments.

FWIW, I read somewhere that IBM is the second most prolific publisher in the US,
after the Federal government. One place I managed ('80-'86) had a full-time
librarian keeping IBM manuals up to date with page replacements.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-13T19:22:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-EA781F.19225913042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net> <b7cifj$1b1$1@slb6.atl.mindspring.net> <3e99d843.5795019@news.optonline.net>`

```
In article <3e99d843.5795019@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

><snip> 
> In case you think this was in some technical backwater, he worked for EDS and
> the client was US Dept of Education. 

I just spent a year fighting with lots of EDS / Department of Ed / 
Accenture systems.  I would exactly call them a technical backwater but 
they certain had many more pressing 'issues' than where to find a manual.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b4438.98982194@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net> <b7cifj$1b1$1@slb6.atl.mindspring.net> <3e99d843.5795019@news.optonline.net> <joe_zitzelberger-EA781F.19225913042003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <3e99d843.5795019@news.optonline.net>,
> robert@wagner.net (Robert Wagner) wrote:
…[7 more quoted lines elided]…
>they certainly had many more pressing 'issues' than where to find a manual.

Anything involving student loans? If so, you're probably seeing data I touched.
<g>

Have you seen any Foundation (FCP)? Now, there's a user interface. <g>
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-15T21:55:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-B25BAD.21550415042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net> <b7cifj$1b1$1@slb6.atl.mindspring.net> <3e99d843.5795019@news.optonline.net> <joe_zitzelberger-EA781F.19225913042003@corp.supernews.com> <3e9b4438.98982194@news.optonline.net>`

```
In article <3e9b4438.98982194@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:
> 
…[17 more quoted lines elided]…
> 

I've not see FCB, but I have seen enough to know that I never, ever, 
ever, want anything to do with any of the above entities again.  Not a 
technical problem -- more of a policies, procedures, organization and 
management problem.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-16T03:35:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9cc592.197646458@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net> <b7cifj$1b1$1@slb6.atl.mindspring.net> <3e99d843.5795019@news.optonline.net> <joe_zitzelberger-EA781F.19225913042003@corp.supernews.com> <3e9b4438.98982194@news.optonline.net> <joe_zitzelberger-B25BAD.21550415042003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>In article <3e9b4438.98982194@news.optonline.net>,
> robert@wagner.net (Robert Wagner) wrote:
…[25 more quoted lines elided]…
>management problem.

You got it right. That's the kind of travail I put up with every day. The
bullshit here in CLC is mild by comparison.

Posters have no idea how bad it can get out there in the real world.
```

###### ↳ ↳ ↳ Re: Manuals (was: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** "Don Leahy" <xdb2imsN@nospam.whatever.net>
- **Date:** 2003-04-15T10:27:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sFUma.1773$f34.365073@news20.bellglobal.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <3e98ae59.17823141@news.optonline.net> <b7agqp$dbf$1@slb1.atl.mindspring.net> <3e99c971.2000152@news.optonline.net> <b7cifj$1b1$1@slb6.atl.mindspring.net> <3e99d843.5795019@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e99d843.5795019@news.optonline.net...
<much snippage>
> Yes, that's what I meant when I said manual. The problem is finding the
> bookshelf. IBM has a plethora of them and its not always evident which
covers
> the topic of interest. An attempted remedy at one place was a supplemental
flat
> file listing manual titles on each bookshelf. One could search on "COBOL"
and
> find a dozen bookshelves containing COBOL manuals. Eliminating irrelevant
> operating systems narrowed it to perhaps half a dozen.
>
> The system really needs a consolidated index. I realize there are
installation,
> 'mounting' and security issues involved.

FWIW, BookManager allows you to create your own indexed bookshelves.  I've
used this to consolidate several messages and codes manuals into one
searchable bookshelf, and all of my frequently used manuals on another.
The former is really handy because I have configured the SDSF 'BOOK' command
to point to my messages and codes bookshelf.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T08:00:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7eidn$c00$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net>`

```

"LX-i" <DanielJS@Knology.net> wrote in message
news:3E98839C.9020301@Knology.net...

> (Of course, it helps that the UNISYS manuals are pretty good, too...  I
> haven't noticed any "documentation vs. behavior" problems that you've
> alluded to with some other compilers.)

I can't speak to the IX/2200 side.  But I think the convention on in MCP/AS
languages, that if the compiler allows something that the documentation
expressly prohibits, the results are undefined and unpredictable, is well
known and well understood.

While we strive to issue syntax errors for most prohibitions that occur in
the documentation, ultimately it is the documentation that prevails as the
authority, and if a programmer ignores a documented prohibition, whether the
compiler detects that usage or not, the fault for violating a documented
prohibition lies with the programmer and not the compiler.  If a trouble
report is filed on such a syntactic element, the submitter will almost
certainly receive a response pointing out the documentation reference where
it prohibits the usage:  document title, version, form number, page, chapter
and verse.   If I'm providing closure text to Field Support, and the
standard is applicable to the question, I will also thrown in the reference
from that document so the submitter as well as the support staff know that
we're not just being capricious.

I don't see failure of management of any given company or organization to
provide its programmers access to vendor documentation for the products they
are expected to use as a failing of the product vendor.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b4c11.100991298@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <3E98839C.9020301@Knology.net> <b7eidn$c00$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"LX-i" <DanielJS@Knology.net> wrote in message
…[22 more quoted lines elided]…
>we're not just being capricious.

That's a reasonable posture. Other companies do the same. 

>I don't see failure of management of any given company or organization to
>provide its programmers access to vendor documentation for the products they
>are expected to use as a failing of the product vendor.

I didn't say it was the vendor's fault. It's clearly management's fault.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:47:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80sp1$s90$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >I fought when EDS had that as a standard in the late 1970s.   But I lost and
> >had to code by their standards while I worked for them.
…[4 more quoted lines elided]…
> lead (once), I said I didn't know it existed. <G>

Interesting.   You must be a very special person if you can stay employed while
ignoring your employers' requirements.


> >I suppose you have had to use practices that you felt were less than optimal
> >as well.  If not, you are unusual.
…[6 more quoted lines elided]…
> to 'get that old code out the door' as expeditiously as possible.

I haven't come across this.   In fact, but I have found a bit of the opposite. 
The less someone knows about CoBOL, the more strict they are about standards
that don't matter.


> In-house C standards are a different story. They _are_ enforced because
> managers
…[3 more quoted lines elided]…
> said to.

Why do managers understand C better than CoBOL?   I haven't seen this.    To a
non-programmer, C is harder to follow than CoBOL is.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-21T13:27:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304211227.a1a9acc@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <b76i5n$naj$1@peabody.colorado.edu> <3e9822f0.106335061@news.optonline.net> <b80sp1$s90$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> > Having recently worked on an EDS project, I can report they're still using
> > that
…[4 more quoted lines elided]…
> ignoring your employers' requirements.

'Having recently worked' is past tense.  

That may be the reason he is no longer there, but then I can think of
several reasons why he would be currently unemployed.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T08:30:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76n2k$147d$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9618c9.359208255@news.optonline.net...

> >> We all know what the standard says. I find it dangerous and error-prone
> >> because it doesn't initialize FILLERs.
…[3 more quoted lines elided]…
> It's not predictable when you change data-name to filler without
understanding
> the consequences.

It's the programmer's job to understand the behavior of the constructs of
the language he uses.  It's not the construct's fault if the programmer
fails in that responsibility.  Failing to accept responsibility for the
consequences of one's own actions strikes me as childish.

>> I _did_ advocate lists and there has been little substantive rebuttal.
> >
…[3 more quoted lines elided]…
> When someone (you?) challenged relative speed, I wrote and posted a
benchmark
> showing they were about the same. That's not ignored or dismissed.

You wrote a benchmark showing they were about the same on the machine you
were running on.  I'm not convinced that that's true on every machine.  The
message containing the program has timed out on my server, so to get the
original source I'd have to hunt it up on Google, then most probably turn it
into standard COBOL, before I could run my own tests.  I'm not interested
enough in debating this subject to go to all that trouble.

> >While complaining above that functions 'encouraged C-like style', you
> >advocate making programs into being C-like.
>
> C-like, to my mind, means nested and telescoped functions. Pointers are
not
> C-like, they are basic data structures. Assembly language programmers use
them
> routinely without being accused of promoting 'C-style'.

As I pointed out earlier, the use of nested function calls significantly
predates C.  In all probability the authors of C decided that this was a
*useful* feature of Fortran, Algol, PL/1, Pascal, etc., etc., etc.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-16T23:45:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KvidnUN9u8v5vgOjXTWcqQ@comcast.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net>`

```
> >> We all know what the standard says. I find it dangerous and error-prone
> >> because it doesn't initialize FILLERs.
…[3 more quoted lines elided]…
> It's not predictable when you change data-name to filler without
understanding
> the consequences.
>

    I normally bypass the initialize filler problem by doing a move
spaces first, than initialize replacing numeric by zero.

    Some compilers (microfocus) generate much less code
with the above than with a simple initialize.  And it nails
those pesky fillers.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:54:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80t77$sg1$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <KvidnUN9u8v5vgOjXTWcqQ@comcast.com>`

```

On 16-Apr-2003, "Russell Styles" <RWS0202@comcast.net> wrote:

>     I normally bypass the initialize filler problem by doing a move
> spaces first, than initialize replacing numeric by zero.
…[3 more quoted lines elided]…
> those pesky fillers.

Depending on how complex your data are.   Another alternative to INITIALIZE
could be to have an initialized record sitting there ready to be copied to the
working record.   This may also be more efficient - and may be more clear as
well, depending on the knowledge level of the other programmers.

But sometimes we don't WANT those pesky fillers nailed.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-21T21:22:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sqmdnfEbs9_nBDmjXTWcqA@comcast.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <217e491a.0304091315.4cded057@posting.google.com> <3e9618c9.359208255@news.optonline.net> <KvidnUN9u8v5vgOjXTWcqQ@comcast.com> <b80t77$sg1$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b80t77$sg1$1@peabody.colorado.edu...
>
> On 16-Apr-2003, "Russell Styles" <RWS0202@comcast.net> wrote:
…[8 more quoted lines elided]…
> Depending on how complex your data are.   Another alternative to
INITIALIZE
> could be to have an initialized record sitting there ready to be copied to
the
> working record.   This may also be more efficient - and may be more clear
as
> well, depending on the knowledge level of the other programmers.
>
> But sometimes we don't WANT those pesky fillers nailed.

    True.  When organizing "general" working storage in a program,
I typically organize them into two 01's.  One has values, the other does
not.  Initialize the one without values, do something else (maybe nothing)
for
the one with values.
```

###### ↳ ↳ ↳ COBOL and "exceptions" (was: Accuracy/Knowledge score-card

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-09T16:43:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72464$9s3$1@slb3.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e93602c.180848320@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
<snip>
>
> >> 8) Claimed that ANSI/ISO *required* that subscripts and/or indexes (I
> >can't
> >> remember if it was both or not) *must* cause an error at run-time when
set
> >> to an out-of-bound value.
>
> Indexes. They did cause an out of bounds under COBOL '74. I haven't used
them
> much since, which explains why I was unaware bounds checking had changed.
>

I thought that this error had been "put to bed" - but in case anyone (RW or
other) is still confused:

*ALL* previous COBOL Standards have defined what happens when index values
are "within bounds".  The important error in the original posts was the
claim that when a boundary violation occurred (no matter when this was
detected) that an ANSI/ISO conforming compiler was REQUIRED to do something,
e.g.

 - issue an error message
 - abnormally terminate the program
 - take some other "negative" action.

The important truth about not only THIS exception but all similar situations
in previous COBOL Standards is that the Standard defines what happens when
the rules are obeyed; they did NOT dictate what was required to happen when
such rules were violated.

For upward compatibility purposes, even the 2002 Standard (where
significantly enhanced exception handling is added), there is STILL no
requirement for specific behavior when such errro/exceptions occur UNLESS
additional code/directives/syntax is used.  The important wording
(guaranteeing upward compatibility - and telling what that means) appears on
page 393 of the new Standard where it states (under the topic "14.5.12.1.2
Fatal exception conditions"),

"5) If checking for the exception condition is not enabled, the implementor
defines whether or not execution will continue, how it will continue, and
how any receiving operands are affected."

P.S. As originally noted, some - but certianly not all - vendors of '74 and
'85 (and possibly earlier) Standards have provided "debugging" tools that
could (when turned on) check for and take programmer selected action for:
  - boundary violations
 - incompatible data
 - divide by zero

and a number of other "situations".  Such tools did NOT violate the earlier
Standard as *any* action in such cases was conforming.  However, neither was
the lack of such "tools" violate the Standard - for the same reason.
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94f1a0.283636220@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e93602c.180848320@news.optonline.net...
…[31 more quoted lines elided]…
>such rules were violated.

That's the equivaocation. Practice did change between '74 and '85, but it would
be difficult to cite a passage in the standard supporting the change. The
standard never said 'a conformining compiler must check indexes when set'. So
why did they all change in '85? There must have been something different,
perhaps subtle, in the language of the '85 standard.
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-10T23:10:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b75fa5$om1$1@slb5.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net>`

```
No,  I know of NO compiler that changed as far as issuing or not issuing
"error messages" (at run-time) for boundary violations between the '85 and
'74 Standards.

Those that had an "extension" for indicating a boundary violation with their
'74 compilers *also* provided an extension for checking boundary violations
with their '85 Standard compilers.  There *may* have been some that added
additional debugging/error processing with their '85 Standard compilers -
but that was simply as they added additional enhancements "in general".

Can you give an example of a compiler that DID issue a run-time error with
its '74 Standard compiler but did not (does not) provide such an option with
their '85 Standard compiler?   There *may* be one - as having or not having
such a feature is totally OUTSIDE the requirements of either Standard, but I
don't PERSONALLY know of any.

(FYI - IBM's mainframe compiler has an "interesting" history related to
this.  For the OS/VS COBOL compiler, there was no built-in boundary
violation detecting support. The only time that you would expect a run-time
indication of such an error was when you "clobered" someone else's storage.
In fact, it was relatively common to "subscript" out of range for larger
tables and to access a files' RDW.   However, most sites *also* licensed
CAPEX, then CA's "Optimizer" product which *did* introduce a feature for
OS/VS COBOL for "subscript checking" - whether the OS/VS COBOL compiler was
run in '74 or '68 Standard mode.  When IBM introduced its VS COBOL II
compiler - which was ONLY a '74 Standard compiler for its first 2 releases,
they also provided subscript range checking.  This was, of course, continued
with VS COBOL II, R3 - their first '85 Standard compiler - and all
subsequent compilers.)
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-11T06:56:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304110556.58dba7a9@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net> <b75fa5$om1$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<b75fa5$om1$1@slb5.atl.mindspring.net>...
> 
> (FYI - IBM's mainframe compiler has an "interesting" history related to
…[11 more quoted lines elided]…
> subsequent compilers.)

I know of some of us who used this lack of a check as a feature - to
get tables > 32K.
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e983cce.112958847@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net> <b75fa5$om1$1@slb5.atl.mindspring.net>`

```
No, I can't cite a specific compiler family. 


"William M. Klein" <wmklein@ix.netcom.com> wrote:

>No,  I know of NO compiler that changed as far as issuing or not issuing
>"error messages" (at run-time) for boundary violations between the '85 and
…[89 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-12T15:45:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b79tu2$9ij$1@slb0.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net> <b75fa5$om1$1@slb5.atl.mindspring.net> <3e983cce.112958847@news.optonline.net>`

```
Please accept, then, that you were in error on this (both whey you
originally posted about it - and in these recent posts).

It simply didn't happen.

Again, my original post indicated that the error was that you thought that
the Standard ('74 or '85) *required* an error message or program/application
termination when a boundary violation occurred.

Again, such behavior is ALLOWED by both Standards - but so is its
alternative of continuing using whatever the vendor allows as the index
value.
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T12:51:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7f3f9$o90$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net> <b75fa5$om1$1@slb5.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b75fa5$om1$1@slb5.atl.mindspring.net...

> No,  I know of NO compiler that changed as far as issuing or not issuing
> "error messages" (at run-time) for boundary violations between the '85 and
> '74 Standards. ...

Just as a clarification:  The behaviors of Unisys MCP/AS COBOL74 and Unisys
MCP/AS COBOL85 actually do differ in this respect, but not for any reason
having to do with the standard.

The difference has two basic components:  the way memory is allocated within
the program, and with the way bounds checking selection is handled.  COBOL74
and COBOL85 are two different implementations.

With COBOL85, you can select strict bounds checking for both indices and
subscripts, or for neither, but cannot select one or the other.  With
COBOL74, strict bounds checking is available only for subscripts; strict
bounds checking is unavailable for indices.

With either compiler, whether bounds checking is in effect or not, indices
and subscripts cannot stray outside the bounds of the allocated memory
space; they are prevented from doing so by the hardware.   For COBOL85, that
memory space can be a "pool" containing a number of 01-level and 77-level
records, but in COBOL74 every 01-level record and every elementary item has
its own memory space.

Thus, with or without bounds checking selected, in COBOL74 you can't "index"
or "subscript" outside the 01-level record containing a table.  In COBOL85,
you may be able to get outside the 01-level record, but won't be able to get
outside, say, the particular program's working-storage section.

These differences have nothing whatever to do with the requirements of
either the '74 or '85 standards.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T09:05:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76p4b$15k1$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net>`

```
In
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e94f1a0.283636220@news.optonline.net...

> >The important truth about not only THIS exception but all similar
situations
> >in previous COBOL Standards is that the Standard defines what happens
when
> >the rules are obeyed; they did NOT dictate what was required to happen
when
> >such rules were violated.

> That's the equivaocation. Practice did change between '74 and '85, but it
would
> be difficult to cite a passage in the standard supporting the change. The
> standard never said 'a conformining compiler must check indexes when set'.
So
> why did they all change in '85? There must have been something different,
> perhaps subtle, in the language of the '85 standard.

Why did *what* "all" change?  Our implementations of COBOL74 and COBOL85
differ SOME in this area, but not for any standards-related reason -- they
differ because our COBOL85 compiler was written from scratch by people who
were writing to a different standard, a different set of limitations, and a
different era, from those who had written the COBOL74 compiler.  Both
standards have the rule that index-names used as destinations in a SET must
represent an occurrence number -- but it is not a SYNTAX rule, and neither
standard describes the consequences.   It is sometimes possible in COBOL85
to index or subscript outside of the 01-level record your table is in, it is
NOT possible in COBOL74 to do so, and the difference has nothing to do with
standards but with hardware and the way that hardware is used.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL and "exceptions" (was: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T13:14:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b777mn$1frk$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72464$9s3$1@slb3.atl.mindspring.net> <3e94f1a0.283636220@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e94f1a0.283636220@news.optonline.net...

> That's the equivaocation. Practice did change between '74 and '85, but it
would
> be difficult to cite a passage in the standard supporting the change. The
> standard never said 'a conformining compiler must check indexes when set'.
So
> why did they all change in '85?

I've already addressed "all".

> There must have been something different, perhaps subtle, in the language
of the '85 standard.

No.  Wrong.

Given the presumption that the behavior exhibited by an implementor's COBOL
compilers differed in some way between their '74-compliant and their
'85-compliant implementations, it does not follow that there is no possible
reason or motive for the difference other than a change in the wording of
the '85 standard from that found in the '74.  Certainly that's one possible
motive, if a difference in the wording of the standard can be shown, but not
otherwise.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-09T16:39:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72avl$14jn$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e93602c.180848320@news.optonline.net...

> They encourage a C-like style of telescoping multiple functions into a
single
> statement.

Goes WAY back before C.   I see nested function calls in arithmetic
expressions from code from the 1950's.  I think just about every common
higher-level language *but* COBOL and RPG has this in one form or another.

> Most are trivial; one can accomplish the same end with regular COBOL. For
> instance, function integer(). Integer-of-date is a non-trivial exception.

I personally think most of the intrinsic functions are non-trivial
exceptions.  Also, the presumption here seems to be that COBOL functions are
always numeric; that's not true.  Some return alphanumeric, not arithmetic,
results.

While it's true that the features of the UPPER-CASE and LOWER-CASE functions
can be done in a straightforward fashion using INSPECT ... CONVERTING in
COBOL2002, that won't work with COBOL85, in which a "step-through-it"
mechanism would be required.

REVERSE is actually very useful indeed.  INSPECT FUNCTION REVERSE (item)
TALLYING (counter) FOR LEADING SPACE strikes me as a fairly elegant way to
find out how many TRAILING blanks a data item has, and the "straightforward"
pre-intrinsics-amendment COBOL code to do the same thing decidedly
unattractive.   Some have proposed an INSPECT ... TALLYING TRAILING as a
feature for the next standard, but there's some resistance to it precisely
because of the presence of FUNCTION REVERSE.

MIN and MAX take arguments of any type, so long as they're the same type,
and lest anybody misundeerstand, they can take any number of arguments, and
if they're alphanumeric, the size of the return item varies to match the
size of the selected argument.

And any function that takes a variable number of parameters (like MIN and
MAX) can take, as one or more of those parameters, a table with the
subscript ALL, in which case each element of that table is functionally
included as a subscript. Using ALL as subscript to one or more table-names
as one or more of the parameters to the likes of Functions MAX, MEAN,
MEDIAN, MIDRANGE, MIN, ORD-MAX, ORD-MIN, PRESENT-VALUE, STANDARD-DEVIATION,
SUM and VARIANCE strikes me as potentially saving a HECK of a lot of PERFORM
VARYING ... END-PERFORM statements.

Trivial?  Depends.  The sum of two items?  probably.  But I can calculate
the total of the contents of five different tables in one simple COBOL
statement and, depending on the size of the table names, I can probably fit
the statement on a single fixed-format source image; the purpose and intent
of that statement would almost certainly obvious to any casual reader.
Can you say the same for the "hard-coded" equivalent?

In general, I can probably accomplish some sort of analog to some of these
in COBOL, but I'm not convinced that the COBOL code to do so can generally
be regarded as "trivial", I'm not convinced that the "longhand" code is
necessarily clearer, and I'm not convinced that it's likely to be "better
practice" in either performance or accuracy than the vendor-supplied
mechanisms for these functions.

> We all know what the standard says. I find it dangerous and error-prone
because
> it doesn't initialize FILLERs.

It's dangerous ONLY if you refuse to read the manual, or to know what it
actually is required to do and described as doing.  Another tip:  it doesn't
initialize to the contents of the VALUE clauses either (unless the VALUE
clauses match the values specified for the usage).    It is DOCUMENTED that
it doesn't initialize fillers; it's the programmer that assumes that it
should do otherwise that's dangerous and error-prone.

Initializing fillers, and initializing to values, are features of
2002-compliant COBOL, and may be available as extensions in some earlier
implementations, but the syntax is different.

> Yes. I didn't advocate avoiding reference-modification. I mentioned in
passing
> that I don't like it.

As I recall, you recommended against the use of reference modification, and
when pressed for reasons you indicated that one of the big reasons was that
you could only use literals, not variables, as location specifiers.  That
premise is false.  Recommending against something is rather different from
expressing a personal distaste for it.

> Over the years, I've encountered many discrepencies between reality and
what the
> manual said.

Proper response to that is to file a trouble report with the vendor, not
presume that what the compiler did was right and what the manual said was
wrong.  Familiarity with the COBOL standards to which the vendor strives to
comply is a really helpful tool here.

> Realia was an IBM clone. It originally shipped with IBM COBOL manuals.
> Compatibility was 99+%. Thus, it's valid to infer IBM standards from
Realia's
> performance.

I'm sure IBM's COBOL support team, as well as all of their loyal customers,
will be delighted to hear that.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-09T17:01:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72c9f$15g9$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com>`

```
I wrote:

> While it's true that the features of the UPPER-CASE and LOWER-CASE
functions
> can be done in a straightforward fashion using INSPECT ... CONVERTING in
> COBOL2002, that won't work with COBOL85, in which a "step-through-it"
> mechanism would be required.

MOVE DN-1 TO DN-2
INSPECT DN-2 REPLACING ALL
            "a" by "A",
            "b" by "B",
            ...
            "z" by "Z"
would work as a shorter alternative to a character-by-character replacement
(and it's blindingly fast in the implementation with which I'm familiar),
but I remain unconvinced that the clarity, the conciseness, the intent, the
maintainability, the robustness or the reliability of this code is somehow
superior to the same characteristics as they apply to, say,
    MOVE FUNCTION UPPER-CASE (DN-1) TO DN-2 (which should be no less fast).

There might be some questions about overlapping operands getting in the way
of the predictability of MOVE FUNCTION UPPER-CASE (DN-1) TO DN-1, but the
caveats there should hardly be news.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-09T19:54:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E94C0C9.70807@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
 > REVERSE is actually very useful indeed.  INSPECT FUNCTION REVERSE (item)
 > TALLYING (counter) FOR LEADING SPACE strikes me as a fairly elegant 
way to
 > find out how many TRAILING blanks a data item has, and the 
"straightforward"
 > pre-intrinsics-amendment COBOL code to do the same thing decidedly
 > unattractive.   Some have proposed an INSPECT ... TALLYING TRAILING as a
 > feature for the next standard, but there's some resistance to it 
precisely
 > because of the presence of FUNCTION REVERSE.

That's brilliant!  I've made a loop to loop backwards through a string
(which is easier in 85 than 74, using inline performs and reference
modification) - but that's even better!  (Especially since they took the
"TRAILING" keyword off the INSPECT statement in the 85 implementation of
the compiler we use.)  I plan to test that out.  :)

I had a feeling this newsgroup was really going to help...  In the less
than a week that I've been here, this is the second really great
technique I've seen.  (The first is (IMO) prefacing paragraph names with
periods (full stops), and eliminating them elsewhere.)



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-10T01:20:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E94C456.29E5A8@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net>`

```


LX-i wrote:

> Chuck Stevens wrote:
>  > REVERSE is actually very useful indeed.  INSPECT FUNCTION REVERSE (item)
…[20 more quoted lines elided]…
>

Don't get excited all at once >G>. If Chuck and the other merry men (and lady
?) on J4 can see there way to a quick discussion/agreement/implementation of
the following - then you wont need a 'neato' solution :-

From a J4 published 'wishlist' :-

13. Improved string handling
    .....
intrinsic function LENGTH-OF-STRING to return length of item minus
trailing spaces.

Sighhhh - I bet the concise sentence above finishes up as half a page !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-09T20:23:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E94C7A9.9020707@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca>`

```
James J. Gavan wrote:
> 13. Improved string handling
>     .....
> intrinsic function LENGTH-OF-STRING to return length of item minus
> trailing spaces.

I cast my vote for that one...  :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T03:05:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94d177$1_2@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <3E94C7A9.9020707@Knology.net>`

```

"LX-i" <DanielJS@Knology.net> wrote in message
news:3E94C7A9.9020707@Knology.net...
> James J. Gavan wrote:
> > 13. Improved string handling
…[5 more quoted lines elided]…
>
Good for you!

Now all you have to do is wait 17 years...

Or join J4 and bring about "change" from the inside...

Pete.
(PS please ignore the above post. It is the ravings of a twisted, cynical,
COBOL lover... Don't ask how he got that way, just continue to support the
standard.)




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-09T21:22:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XPicnYC6oPr3SAmjXTWcow@giganews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E94C456.29E5A8@shaw.ca...
>
>

> >
>
> Don't get excited all at once >G>. If Chuck and the other merry men (and
lady
> ?) on J4 can see there way to a quick discussion/agreement/implementation
of
> the following - then you wont need a 'neato' solution :-

Fujitsu already has it as

COMPUTE Length = FUNCTION STORED-CHAR-LENGTH(dataname)
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-10T08:27:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca>`

```
In article <3E94C456.29E5A8@shaw.ca>,
 "James J. Gavan" <jjgavan@shaw.ca> wrote:

> Don't get excited all at once >G>. If Chuck and the other merry men (and lady
> ?) on J4 can see there way to a quick discussion/agreement/implementation of
…[12 more quoted lines elided]…
> 


How about a compressed string -- leading and trailing removed and runs 
of more than one space reduced to 1...
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-10T17:50:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E95B01D.3A9C9253@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com>`

```


Joe Zitzelberger wrote:

> In article <3E94C456.29E5A8@shaw.ca>,
>  "James J. Gavan" <jjgavan@shaw.ca> wrote:
…[18 more quoted lines elided]…
> of more than one space reduced to 1...

See - now you've complicated it <G>. Once they get side tracked it will last
forever ! I believe you are into OO with Java (?). There is a method in one of the
Net Express classes that sort of lets you do what you want. You can take a string
and put each separate 'word' into collection(list) elements, losing the intervening
'white space'. You know from the collection count (size) how many elements there
are - now you re-string it together with each 'word' followed by one white space.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T20:27:02+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e95c590_2@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com> <3E95B01D.3A9C9253@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E95B01D.3A9C9253@shaw.ca...
>
> > How about a compressed string -- leading and trailing removed and runs
> > of more than one space reduced to 1...
>
> See - now you've complicated it <G>. Once they get side tracked it will
last
> forever ! I believe you are into OO with Java (?). There is a method in
one of the
> Net Express classes that sort of lets you do what you want. You can take a
string
> and put each separate 'word' into collection(list) elements, losing the
intervening
> 'white space'. You know from the collection count (size) how many elements
there
> are - now you re-string it together with each 'word' followed by one white
space.
>
I really like the sound of that, Jimmy.

I am toying with the idea of producing a general string handling component
but I just haven't the time at the moment. That would certainly be a useful
method to include.

I'll check the Fujitsu Class library and see if there is anything
equivalent.

Maybe in the coming Winter Down Under I may have some time to get around to
some of these thngs. Where I live it doesn't get cold but it will rain a
lot. Rainy days are ideal for computer work...<G>

Pete.




> Jimmy, Calgary AB
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-10T19:57:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E95CDBC.6E1D6FC@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com> <3E95B01D.3A9C9253@shaw.ca> <3e95c590_2@127.0.0.1>`

```


"Peter E.C. Dashwood" wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3E95B01D.3A9C9253@shaw.ca...
…[30 more quoted lines elided]…
> Pete.

I've only briefly looked at the F/J Collections - but what you will want to support
this is a class 'Array' or 'CharacterArray' (string manipulation), because these are
encapsulated in the method I referred to.

Jimmy
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-10T11:20:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304101020.15a952f@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com>`

```
Joe - a user defined function is tailor made for this - or a string
object class.  Which COBOL are you using on what platform.


Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com>...
> In article <3E94C456.29E5A8@shaw.ca>,
>  "James J. Gavan" <jjgavan@shaw.ca> wrote:
…[19 more quoted lines elided]…
> of more than one space reduced to 1...
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-10T18:05:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-F45E60.18051610042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <joe_zitzelberger-2D8EB3.08275710042003@corp.supernews.com> <bfdfc3e8.0304101020.15a952f@posting.google.com>`

```
In article <bfdfc3e8.0304101020.15a952f@posting.google.com>,
 thaneh@softwaresimple.com (Thane Hubbell) wrote:

> Joe - a user defined function is tailor made for this - or a string
> object class.  Which COBOL are you using on what platform.
> 

IBM Cobol for OS/390 v2.2 -- but I'm looking forward to better sometime 
in the near future.  Whenever my systems folks decide the v3 compilers 
actually work as advertised...
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-10T08:38:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7434o$2bi3$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E94C456.29E5A8@shaw.ca...

> intrinsic function LENGTH-OF-STRING to return length of item minus
> trailing spaces.
>
> Sighhhh - I bet the concise sentence above finishes up as half a page !

I don't think it's quite that bad.  Given an alphanumeric item ALPH and a
numeric item LEN:
    MOVE ZEROES TO LEN
    INSPECT FUNCTION REVERSE (ALPH) TALLYING LEN FOR LEADING SPACES
    COMPUTE NUM = FUNCTION LENGTH (ALPH) - LEN

    -Chuck Stevens


>
> Jimmy, Calgary AB
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-10T08:57:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7448c$2cb3$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3E94C0C9.70807@Knology.net> <3E94C456.29E5A8@shaw.ca> <b7434o$2bi3$1@si05.rsvl.unisys.com>`

```
Oops.  Didn't finish re-editing.  Please read my previous example code
fragment substitute for
    COMPUTE LEN = FUNCTION STORED-CHAR-LENGTH (ALPH)
as if it had been written
    MOVE ZEROES TO LEN
    INSPECT FUNCTION REVERSE (ALPH) TALLYING LEN FOR LEADING SPACES
    COMPUTE LEN = FUNCTION LENGTH (ALPH) - LEN

Also, the 2002 standard allows the declaration and use of user-defined
FUNCTIONs, so it would be straightforward to incorporate the above into the
user's own repository as FUNCTION STORED-CHAR-LENGTH.   The function's
syntax for declaration, inclusion and reference are all defined within the
standard, so the whole shebang should be portable to any 2002-compliant
compiler.  The standards committee needn't really be involved in this one.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-09T21:20:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XPicnYG6oPr0SAmjXTWcow@giganews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com>
>
> And any function that takes a variable number of parameters (like MIN and
…[4 more quoted lines elided]…
> MEDIAN, MIDRANGE, MIN, ORD-MAX, ORD-MIN, PRESENT-VALUE,
STANDARD-DEVIATION,
> SUM and VARIANCE strikes me as potentially saving a HECK of a lot of
PERFORM
> VARYING ... END-PERFORM statements

MyTotal = Function SUM (MyArray(ALL))

Well, I'll be damned.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-10T09:29:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7465j$2dr0$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <XPicnYG6oPr0SAmjXTWcow@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:XPicnYG6oPr0SAmjXTWcow@giganews.com...

> MyTotal = Function SUM (MyArray(ALL))
>
> Well, I'll be damned.

Not only that, but if you really want to take it to extremes:

MyGrandTotal = Function SUM (
    FirstArray (ALL),
    SecondArray (ALL),
    SomeVariable,
    AnotherVariable,
    Function MIN (ThirdArray (ALL)),
    Function INTEGER (Function MEAN (FourthArray (ALL))),
    FifthArray (ALL),
    SixthArray (Function INTEGER (Function MEDIAN (SeventhArray (ALL))))
    ).

It may not look all that straightforward (in fact, I first terminated it
with a semicolon -- not because of C but because of Algol and Pascal!! ),
but I'd bet dollars to doughnuts it'd be a lot easier for a novice
programmer to determine accurately at a quick glance what this code does
than it would for that novice to figure out at a similar quick glance what
the "longhand" equivalent did ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9607da.354872922@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e93602c.180848320@news.optonline.net...

> the presumption here seems to be that COBOL functions are
>always numeric; that's not true.  Some return alphanumeric, not arithmetic,
>results.

Current-date returns alphanumeric date and time, whereas date-of-integer returns
an 'integer' date. The latter says it returns (YYYY * 10000) + (MM * 100) + DD.
Why doesn't the former return a similar integer version of yyyymmddhhmmsshh?

>REVERSE is actually very useful indeed.  INSPECT FUNCTION REVERSE (item)
>TALLYING (counter) FOR LEADING SPACE strikes me as a fairly elegant way to
…[4 more quoted lines elided]…
>because of the presence of FUNCTION REVERSE.

I concur. It is fairly elegant. I couldn't imagine why REVERSE would be used
before reading your post. 

>And any function that takes a variable number of parameters (like MIN and
>MAX) can take, as one or more of those parameters, a table with the
…[5 more quoted lines elided]…
>VARYING ... END-PERFORM statements.

I do that kind of stuff all the time. Go through a document tallying where
numbers begin and end, then find the max, blank out nearby columns and find the
next max. Whoops. FUNCTION MAX doesn't tell me WHERE it found the max. Back to
longhand code. 

>> We all know what the standard says. I find it dangerous and error-prone
>because
…[7 more quoted lines elided]…
>should do otherwise that's dangerous and error-prone.

The issue is not in development, it is in maintenance. A maintenance programmer
might not know that a record is being INITIALIZEd. (S)he might change a
data-name to filler without understanding the consequences. 

>> Yes. I didn't advocate avoiding reference-modification. I mentioned in
>passing
…[4 more quoted lines elided]…
>you could only use literals, not variables, as location specifiers

I never said that. I said I'd not seen anything but literals used in production
code .. as a lazy substitute for subdefining the field. 

>> Over the years, I've encountered many discrepencies between reality and
>what the
…[5 more quoted lines elided]…
>comply is a really helpful tool here.

They don't listen .. or say it will take YEARS to effect a fix. Justice delayed
is justice denied. I do the best I can with reality.

>> Realia was an IBM clone. It originally shipped with IBM COBOL manuals.
>> Compatibility was 99+%. Thus, it's valid to infer IBM standards from
…[4 more quoted lines elided]…
>will be delighted to hear that.

The issue is collecting facts, not customer loyalty or other 'religious' issues.
Realia was very close to the 'IBM standard'.
```

###### ↳ ↳ ↳ Know your function (was: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-10T23:14:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b75feq$5jn$1@slb3.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9607da.354872922@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> >"Robert Wagner" <robert@wagner.net> wrote in message
> >news:3e93602c.180848320@news.optonline.net...
>
<snip>
> >And any function that takes a variable number of parameters (like MIN and
> >MAX) can take, as one or more of those parameters, a table with the
> >subscript ALL, in which case each element of that table is functionally
> >included as a subscript. Using ALL as subscript to one or more
table-names
> >as one or more of the parameters to the likes of Functions MAX, MEAN,
> >MEDIAN, MIDRANGE, MIN, ORD-MAX, ORD-MIN, PRESENT-VALUE,
STANDARD-DEVIATION,
> >SUM and VARIANCE strikes me as potentially saving a HECK of a lot of
PERFORM
> >VARYING ... END-PERFORM statements.
>
> I do that kind of stuff all the time. Go through a document tallying where
> numbers begin and end, then find the max, blank out nearby columns and
find the
> next max. Whoops. FUNCTION MAX doesn't tell me WHERE it found the max.
Back to
> longhand code.

Your correct that the MAX function doesn't tell you which item was the
largest.  That is what the ORD-MAX function does.  In fact, that is ALL that
function does.
```

###### ↳ ↳ ↳ Re: Know your function (was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T16:34:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e96ee73.27350282@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75feq$5jn$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9607da.354872922@news.optonline.net...
…[27 more quoted lines elided]…
>function does.

I'll start using it this afternoon. Thank you.
```

###### ↳ ↳ ↳ Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-10T23:19:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b75fon$3g5$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9607da.354872922@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
…[4 more quoted lines elided]…
> >always numeric; that's not true.  Some return alphanumeric, not
arithmetic,
> >results.
>
> Current-date returns alphanumeric date and time, whereas date-of-integer
returns
> an 'integer' date. The latter says it returns (YYYY * 10000) + (MM * 100)
+ DD.
> Why doesn't the former return a similar integer version of
yyyymmddhhmmsshh?

The reason that the funcitons CURRENT-DATE and WHEN-COMPILED cannot return
numeric items is that they need to have a "+" or "-" to indicate whether the
offset from Coordinated Universal Time is "positive" or "negative".  See
postionss 17-21 of these functions.

NOTE: It is entirely possible to reference modify the returned value from
these functions - and nest this within another function such as NUMVAL and
INTEGER-PART to get the results that you want.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T11:10:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b770fe$1at7$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net>`

```

Robert Wagner queried:

> > Why doesn't the former return a similar integer version of
> yyyymmddhhmmsshh?
>

Bill Klein responded:

> The reason that the funcitons CURRENT-DATE and WHEN-COMPILED cannot return
> numeric items is that they need to have a "+" or "-" to indicate whether
the
> offset from Coordinated Universal Time is "positive" or "negative".  See
> postionss 17-21 of these functions.
…[3 more quoted lines elided]…
> INTEGER-PART to get the results that you want.

I agree, Bill.

To make it a little clearer, the desired integer-form "yyyymmddhhmmsshh"
value (in any numeric usage big enough to hold a sixteen-digit integer) can
be obtained by
    COMPUTE yyyymmddhhmmsshh = FUNCTION NUMVAL (FUNCTION CURRENT-DATE
(1:16)).

Likewise, OffsetFromUniversalTime, IF it's meaningful on the system
(CURRENT-DATE (17:1) is NOT equal to "0" )  is provided by
    COMPUTE OffsetFromUniversalTime = FUNCTION NUMVAL (FUNCTION CURRENT-DATE
(17:5))
so long as OffsetFromUniversalTime is signed and allows for at least four
digits.

Thus, the answer to the question is that it's trivial to get it oneself from
what CURRENT-DATE *does* provide.

Oh, and by the way, yes, one CAN avoid the use of reference modification by
putting the value of CURRENT-DATE into a properly-structured record with all
the appropriate subordinate field names and applicable redefinitions, but
I'm not entirely convinced that's inherently preferable in either style or
clarity to the above examples.

   -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T11:47:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b772ku$1ceu$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <b770fe$1at7$1@si05.rsvl.unisys.com>`

```
I wrote:

> Oh, and by the way, yes, one CAN avoid the use of reference modification
by
> putting the value of CURRENT-DATE into a properly-structured record with
all
> the appropriate subordinate field names and applicable redefinitions, but
> I'm not entirely convinced that's inherently preferable in either style or
> clarity to the above examples.

NUMVAL accounts for the possibility of leading blanks, blanks between a
leading sign and the first numeric digit, a decimal point, one or more
fractional digits, spaces between the last numeric digit and a trailing
sign, trailing signs of "+", "-", "CR" and "DB", and trailing spaces.  Not
that anybody has ever expressed an interest in having COBOL provide an
automated method for converting such disparate strings to their numeric
values, of course.

But in this instance, it's quite possible that the "record method" might be
faster than the "NUMVAL method", because the format in which the data is
returned is known, and NUMVAL's decoding and contents-decision
determinations are unnecessary for this case.

I would expect MOVE A TO B, where B is a four-digit signed numeric item, A
is described PIC S9999 SIGN LEADING SEPARATE, and we can trust that the
contents of A match their description, to be faster as a rule than MOVE
FUNCTION NUMVAL (C) TO B, where C is PIC X(5) and contains a leading sign
and four numeric digits.  .

Is going to the trouble of setting up a record describing the contents of
CURRENT-DATE worth it?  Well, that depends on how many times a microsecond
you really need to verify with the system that we haven't drifted into
another century, or that the offset between local time and universal time
hasn't been changed by the government while the program was running.   The
more likely of these two requirements, during a given execution of a
program -- crossing a century boundary -- can be detected through other
means.  All but century and offset are also available, and in numeric form,
and have been since the '74 standard, from ACCEPT.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T12:00:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b773cu$1ctg$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <b770fe$1at7$1@si05.rsvl.unisys.com> <b772ku$1ceu$1@si05.rsvl.unisys.com>`

```
I wrote:

> I would expect MOVE A TO B, where B is a four-digit signed numeric item, A
> is described PIC S9999 SIGN LEADING SEPARATE, and we can trust that the
> contents of A match their description, to be faster as a rule than MOVE
> FUNCTION NUMVAL (C) TO B, where C is PIC X(5) and contains a leading sign
> and four numeric digits.

Another not-quite-so-fast possibility here for MOVE A TO B is to declare the
source field, A, as PIC +9999.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e983f0e.113534246@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

It could have returned + or - as the sign of a 20 digit integer. But wait, COBOL
didn't support integers bigger than 18 digits. That might be the reason it's a
string. 

There could have been a separate function for GMT offset, which doesn't change
from one call to the next. 


>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9607da.354872922@news.optonline.net...
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T11:48:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7evpu$lmh$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e983f0e.113534246@news.optonline.net...

> It could have returned + or - as the sign of a 20 digit integer. But wait,
COBOL
> didn't support integers bigger than 18 digits. That might be the reason
it's a
> string.

I think this comes under the category of "well, duh!".

> There could have been a separate function for GMT offset,

Yes, there could have been.  With 2002-standard-compliant COBOL, there now
can be, if you want to build your own and make your living marketing it.  I
think most programmers with some practice with COBOL85 would regard doing so
as a trivial exercize.

> which doesn't change from one call to the next.

Ummm ... not even because of Daylight Savings Time?

In some locations within the United States, I would expect that value to
change something on the order of twice a year -- that's twice as frequently
as the year-of-century value obtained from either elsewhere within
CURRENT-DATE or from ACCEPT ... FROM DATE.

Is there some reason I should *not* expect the offset from local time to GMT
to differ when Daylight Savings Time is in effect from its value when
Standard Time is in effect in a given time zone?   Or the value returned by
a call (on CURRENT-DATE or on a hypothetical GMT-OFFSET function) to differ
after the time specified for "spring forward" (or "fall backward") from its
value before the local time change?

"GMT offset doesn't change" seems to me to be another one for the list!
Granted, it doesn't change often, but then again, neither does the current
century.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T02:50:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b7029.110232855@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[4 more quoted lines elided]…
>value before the local time change?

I never understood that mnemonic. You push on a spring and what does it do? It
pushes back. Have you ever seen someone trip and fall? Ninety percent of the
time he falls forward, not backward.  <G>

>"GMT offset doesn't change" seems to me to be another one for the list!
>Granted, it doesn't change often, but then again, neither does the current
>century.

Richard will contrive a case involving a business traveler with a laptop on a
Concorde.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-14T22:38:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304142138.7195e979@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com> <3e9b7029.110232855@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> I never understood that mnemonic. You push on a spring and what does it do? It
> pushes back. Have you ever seen someone trip and fall? Ninety percent of the
> time he falls forward, not backward.  <G>

It's a mnemonic, not a bedtime story.  You seem to want to quibble
about everthing.

Just as a script kiddie troll would, actually.
 
> >"GMT offset doesn't change" seems to me to be another one for the list!
> >Granted, it doesn't change often, but then again, neither does the current
…[3 more quoted lines elided]…
> Concorde.

Will I ? I didn't know that, but you must be right given your past
track record of psychic predictions.

But the computer doesn't need to be moving to require different time
zones, I have web sites at clients that process users from around the
world.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T23:27:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9c7d96.179216139@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com> <3e9b7029.110232855@news.optonline.net> <217e491a.0304142138.7195e979@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>But the computer doesn't need to be moving to require different time
>zones, I have web sites at clients that process users from around the
>world.

Why do you need to know the user's local time? 

If you do need it, getting the time from the user would be more reliable than
calculating it with time zones. For political reasons, all places in a time zone
may not observe Daylight Savings Time. In the US, the State of Indiana is very
irregular about time. Some cities observe DST, others do not.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-15T16:49:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7i5qs$30t5$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com> <3e9b7029.110232855@news.optonline.net> <217e491a.0304142138.7195e979@posting.google.com> <3e9c7d96.179216139@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9c7d96.179216139@news.optonline.net...

> >But the computer doesn't need to be moving to require different time
> >zones, I have web sites at clients that process users from around the
> >world.
>
> Why do you need to know the user's local time?

The reason is that local time is more meaningful to humans.  Where I'm
sitting as I write this it's not USEFUL for me to think of it as being
REALLY something like three in the morning of April 16, 2003.   I can think
of numerous instances in which the relative timing of two events occurring
in different time zones would be important to an application, and I also
believe reporting of those times and dates in Coordinated Universal Time
would be of not much use to anyone but the programmer.   Reporting the times
and dates of these events as they were in the location in which they
occurred, wherever they occurred, would likely be much more meaningful to
the client than recording them as having occurred at a given time *in
Greenwich*, regardless of where the event occurred.

> If you do need it, getting the time from the user would be more reliable
than
> calculating it with time zones.

Huh?  Getting the time stamp for a retail order from the purchaser rather
than getting it, say, from the cash register?

> For political reasons, all places in a time zone
> may not observe Daylight Savings Time. In the US, the State of Indiana is
very
> irregular about time. Some cities observe DST, others do not.

And ...?    Which delayed transaction coming into your computer in
Vladivostok:  the one that was entered into the cash register at noon from,
say, Terre Haute, or the one, say, from South Bend?   The time at which
events occur, *wherever* they occur, may be meaningful to an application,
and *reporting* those events to humans in universal time is only really
useful if you're looking at the reports in Greenwich.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-15T21:21:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9CBE21.1050406@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com> <3e9b7029.110232855@news.optonline.net> <217e491a.0304142138.7195e979@posting.google.com> <3e9c7d96.179216139@news.optonline.net> <b7i5qs$30t5$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> The reason is that local time is more meaningful to humans.  Where I'm
> sitting as I write this it's not USEFUL for me to think of it as being
…[8 more quoted lines elided]…
> Greenwich*, regardless of where the event occurred.

Being in the military, we're infatuated with Zulu (GMT)...  But, now 
that I've seen the kinds of things we can do, and the issues that it 
eliminates having all the mainframes running on Zulu, I'm not so sure 
that I'm not going to set up PC-based servers that way once I get my 
farm going...  :)

<unisys_stuff>
We have a DMS record that stores offsets from GMT.  It hangs of a record 
for each "unit" in the database, and they're connected with a set that's 
sorted on date/time.  Using this set, we can go back and "convert" a 
time back to local, based on what local -was- when whatever it was 
occurred.  It's a pretty cool little setup (I kinda wish I had come up 
with it)...
</unisys_stuff>


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-16T00:09:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304152309.38fb0397@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com> <3e9b7029.110232855@news.optonline.net> <217e491a.0304142138.7195e979@posting.google.com> <3e9c7d96.179216139@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> Why do you need to know the user's local time? 

So that I can send an appropriate and polite: 'Good morning', 'Good
afternoon' or 'Good evening' of course.

Cookies are sent to the client machine with an expiry time.  It
wouldn't be very useful to send already expired cookies.
 
> If you do need it, getting the time from the user would be more reliable 

<choke>, you obviously don't deal with client machines.  

My server can sync with clock.org.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-17T02:20:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9e06ed.279926454@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b7evpu$lmh$1@si05.rsvl.unisys.com> <3e9b7029.110232855@news.optonline.net> <217e491a.0304142138.7195e979@posting.google.com> <3e9c7d96.179216139@news.optonline.net> <217e491a.0304152309.38fb0397@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[3 more quoted lines elided]…
>afternoon' or 'Good evening' of course.

If that's the only reason, send a generic 'greetings'.

>Cookies are sent to the client machine with an expiry time.  It
>wouldn't be very useful to send already expired cookies.

You send cookies that expire the same day? That's unusual. 

>> If you do need it, getting the time from the user would be more reliable 
>
><choke>, you obviously don't deal with client machines.  
>
>My server can sync with clock.org.

Ok, check whether it's within a reasonable range, say +-10 minutes. Better to be
off by a few minutes than by an hour.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-17T15:13:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7l68s$9od$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c7d96.179216139@news.optonline.net> <217e491a.0304152309.38fb0397@posting.google.com> <3e9e06ed.279926454@news.optonline.net>`

```
Robert Wagner wrote:

>>So that I can send an appropriate and polite: 'Good morning', 'Good
>>afternoon' or 'Good evening' of course.
> 
> If that's the only reason, send a generic 'greetings'.

No, its not the 'only reason', I had a 2nd one too. Oh, you had read it.

But, no, I don't like you 'solution'. It seems you only posted it to 
quibble.
 
>>Cookies are sent to the client machine with an expiry time.  It
>>wouldn't be very useful to send already expired cookies.
> 
> You send cookies that expire the same day? That's unusual.

Is it ?  and what is your vast experience with cookies that lead you to 
this conclusion ?

In fact it is _not_ unusual for session cookies that are tied to a login 
system.  The cookies are updated on each interraction so as long as the 
system is in use the user doesn't expire.  

General ad-tracking cookies may last for weeks or months, but they don't 
get onto my systems.

> Ok, check whether it's within a reasonable range, say +-10 minutes. Better
> to be off by a few minutes than by an hour.

And what makes you think that the client machine would be 'more reliable' 
with, say, daylight saving.  Windows will update the daylight saving time 
based on the general rules and regardless of 'local politics'.

In any case what is your prefered method of getting the local time from a 
web client ?  Perhaps you could share how you get IE to send local time to 
Apache (or any other).
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:37:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea07ac8.894555@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c7d96.179216139@news.optonline.net> <217e491a.0304152309.38fb0397@posting.google.com> <3e9e06ed.279926454@news.optonline.net> <b7l68s$9od$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:


>And what makes you think that the client machine would be 'more reliable' 
>with, say, daylight saving.  Windows will update the daylight saving time 
>based on the general rules and regardless of 'local politics'.

There is a checkbox in Date/Time properties allowing the user to enable or
disable daylight saving time.

>In any case what is your prefered method of getting the local time from a 
>web client ?  Perhaps you could share how you get IE to send local time to 
>Apache (or any other).

JavaScript. 
>
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-18T22:41:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YeqdnZosuu4VWD2jXTWJjQ@giganews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c7d96.179216139@news.optonline.net> <217e491a.0304152309.38fb0397@posting.google.com> <3e9e06ed.279926454@news.optonline.net> <b7l68s$9od$1@aklobs.kc.net.nz> <3ea07ac8.894555@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net>
>
> >In any case what is your prefered method of getting the local time from a
> >web client ?  Perhaps you could share how you get IE to send local time
to
> >Apache (or any other).
>
> JavaScript.

But, but, but, Java's sick (or sickly) and will presently go the way of MAD
(Michigan Algorithmic Decoder). What, oh what, will we do then?

And why would an Indian give a fig about local time?
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-18T22:16:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304182116.59961bcb@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c7d96.179216139@news.optonline.net> <217e491a.0304152309.38fb0397@posting.google.com> <3e9e06ed.279926454@news.optonline.net> <b7l68s$9od$1@aklobs.kc.net.nz> <3ea07ac8.894555@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> There is a checkbox in Date/Time properties allowing the user to enable or
> disable daylight saving time.

Do you think users will care ? or will be able to find it ?

In any case if they have Office 2000 they have probably set their
clocks back a couple of years (as advised to by MS).
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:08:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b811h1$11q$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> It could have returned + or - as the sign of a 20 digit integer. But wait,
> COBOL
> didn't support integers bigger than 18 digits. That might be the reason it's a
> string.

I wish CoBOL had a "large" type that held a number of any size.   Sure it would
be inefficient and wouldn't be used much - but it wouldn't be that hard to
implement.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-21T19:48:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:b811h1$11q$1@peabody.colorado.edu...
>
> On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
> > It could have returned + or - as the sign of a 20 digit integer. But
wait,
> > COBOL
> > didn't support integers bigger than 18 digits. That might be the reason
it's a
> > string.
>
> I wish CoBOL had a "large" type that held a number of any size.   Sure it
would
> be inefficient and wouldn't be used much - but it wouldn't be that hard to
> implement.

A). COMP-1, COMP-2 (IEEE reals, comp-1 range approx +/- 10^38,  comp-2 range
approx +/-10^307). Of course, you only get 6 or 18 SIGNIFICANT digits of
accuracy with these.

B) new standard (31 decimal digits).

MCM
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2003-04-22T10:46:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA555B7.8030500@newsguy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com>`

```
Michael Mattias wrote:
 > "Howard Brazee" <howard@brazee.net> wrote in message
 > news:b811h1$11q$1@peabody.colorado.edu...
…[9 more quoted lines elided]…
 > B) new standard (31 decimal digits).

Unfortunately, neither of those is suitable for "large integer"
arithmetic.  I don't know if that's what Howard was thinking of, but
it'd be useful for me, as I'm currently dabbling with implementing
cryptographic primitives in COBOL.  The new bitwise operators (b-and and
so forth) are handy for that; having built-in support for large
arithmetic would be a great complement.

For a 1024 bit-operand, you need 309 decimal digits (if my q&d
calculation was correct).
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-22T16:54:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b83s4t$c20$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com> <3EA555B7.8030500@newsguy.com>`

```

On 22-Apr-2003, Michael Wojcik <mwojcik@newsguy.com> wrote:

> Unfortunately, neither of those is suitable for "large integer"
> arithmetic.  I don't know if that's what Howard was thinking of, but
…[6 more quoted lines elided]…
> calculation was correct).

That's exactly what I meant.  An unlimited size for a decimal number.  
Obviously this wouldn't use the chips built in limits of words and bytes.   But
it IS possible to do arithmetic with strings.   We can calculate PI to a
thousand digits.

So create a LARGE numeric type and make sure users know that this is a SLOW
implementation.   CoBOL would accept PIC 9(10000)V9(333) USAGE LARGE, if you
wanted.   I suppose the limit would be how large of a number the compiler could
accept in the 9(x).    There is not much use for this - but you have shown one.
And I don't like limits.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2003-04-22T23:03:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA60298.3040600@newsguy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com> <3EA555B7.8030500@newsguy.com> <b83s4t$c20$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
 > [re large integer arithmetic]
 >
 > That's exactly what I meant.  An unlimited size for a decimal number.
 >  Obviously this wouldn't use the chips built in limits of words and
 > bytes.   But it IS possible to do arithmetic with strings.

Strings of digit characters are one possible representation,
but they're not very space- or time-efficient.  BCD is twice as
space-efficient, with two digits per byte (where "byte" is the
conventional eight-bit octet).  Radix-256, where each byte is a digit
from 0 to 255, is maximally space-efficient, but there are actually
better representations for performance on certain kinds of computations
(notably multiplication).  Google for "Montgomery multiplication
algorithms" if you're curious.

 > There is not much use for this - but you have shown one.

As Richard Plinston noted in another post, there probably isn't
sufficient demand to get this implemented even as an extension to
someone's implementation, much less get it into the standard.  But I
admit it would be handy for me.  Sure, I can call CryptoLib or OpenSSL's
bignum routines, but having it native in COBOL would mean I could write
once and run on any of the platforms MF supports.

And while I'm wishing, I'd like a Standard COBOL pony...
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-23T03:58:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea5e056.15913437@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com> <3EA555B7.8030500@newsguy.com> <b83s4t$c20$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:


>So create a LARGE numeric type and make sure users know that this is a SLOW
>implementation.   CoBOL would accept PIC 9(10000)V9(333) USAGE LARGE,

USAGE LARGE is superfluous. The compiler could determine that from the number of
digits. 

It it went as most things seem to be going, they provide a function rather than
change the language syntax. Or a Class in the Factory. 

>And I don't like limits.

I agree.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-23T13:34:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b864ot$eb8$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com> <3EA555B7.8030500@newsguy.com> <b83s4t$c20$1@peabody.colorado.edu> <3ea5e056.15913437@news.optonline.net>`

```

On 22-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >So create a LARGE numeric type and make sure users know that this is a SLOW
> >implementation.   CoBOL would accept PIC 9(10000)V9(333) USAGE LARGE,
>
> USAGE LARGE is superfluous. The compiler could determine that from the number
> of digits.

Anything that changes efficiency this much I prefer to have to explicitly state.
  And I don't want my compiler determining how my data are stored.  I want to do
it myself.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-23T20:03:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b847as$5a6$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com> <3EA555B7.8030500@newsguy.com> <b83s4t$c20$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>  We can calculate PI to a thousand digits.

I thinks its been done to a few million now hasn't it.

> So create a LARGE numeric type and make sure users know that this is a
> SLOW
…[5 more quoted lines elided]…
> one. And I don't like limits.

There is insufficient demand and no financial incentive to do this in 
standard Cobol, nor probably in any implementation as an extension.

There are, however, sets of routines that will work with large numbers and 
these should be able to be CALLed from some implementations of Cobol.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-24T01:39:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dIqdnXAMpcwF5TqjXTWcqg@comcast.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <8WXoa.2240$%_3.1777696@newssrv26.news.prodigy.com> <3EA555B7.8030500@newsguy.com> <b83s4t$c20$1@peabody.colorado.edu> <b847as$5a6$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b847as$5a6$1@aklobs.kc.net.nz...
> Howard Brazee wrote:
>
…[8 more quoted lines elided]…
> > wanted.   I suppose the limit would be how large of a number the
compiler
> > could
> > accept in the 9(x).    There is not much use for this - but you have
shown
> > one. And I don't like limits.
>
…[6 more quoted lines elided]…
>
    They have done it to more than a trillion digits.  I think that Fujitsu
did it to 1.5 trillion to test a new mainframe.  Someone else devised
a way to rapidly calculate any digit of PI, without doing all of the digits
in front of that digit.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T02:57:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea4a7b9.274584423@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net> <3e983f0e.113534246@news.optonline.net> <b811h1$11q$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
>> didn't support integers bigger than 18 digits. That might be the reason it's
a
>> string.
>
>I wish CoBOL had a "large" type that held a number of any size.   Sure it would
>be inefficient and wouldn't be used much - but it wouldn't be that hard to
>implement.


Good idea. I concur.
```

###### ↳ ↳ ↳ Re: Know your functions 2(was: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T15:50:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7fdvm$vd6$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b75fon$3g5$1@slb6.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b75fon$3g5$1@slb6.atl.mindspring.net...
> The reason that the funcitons CURRENT-DATE and WHEN-COMPILED cannot return
> numeric items is that they need to have a "+" or "-" to indicate whether
the
> offset from Coordinated Universal Time is "positive" or "negative".  See
> postionss 17-21 of these functions.

The functions can also return a "0" in this location, which indicates that
the system on which the function is evaluated doesn't support the local time
differential mechanism in the first place.   Presumably a given
implementation would either always produce "0" or always produce either "+"
or "-", but there is nothing in the standard that says those responsible for
the "operating environment" are precluded from making the availability of
this mechanism a system option.

Note that CURRENT-DATE (17:5) = "+0000" means something quite different from
CURRENT-DATE (17:5) = "00000".  The former means the system is providing you
the offset from local time to GMT, and that offset is zero minutes and zero
seconds (that is, local time = GMT), and the latter means the time is
whatever the system's set to with no clue about how that time relates to
GMT.

It seems to me the "three-state" nature of CURRENT-DATE (17:1) tends to
mitigate against the idea of a single separate function like OFFSET-FROM-GMT
that provides the same numeric and logical information in an integer that
CURRENT-DATE (17:5) provides in a string somewhat problemmatical, I'd say.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-11T21:16:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76165$ffd$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net>`

```
Robert Wagner wrote:

> The issue is not in development, it is in maintenance. A maintenance
> programmer might not know that a record is being INITIALIZEd. (S)he might
> change a data-name to filler without understanding the consequences.

That is why we do testing, we find the consequences before the customer 
does.
 
> I never said that. I said I'd not seen anything but literals used in
> production code .. as a lazy substitute for subdefining the field.

So you want to eliminate all uses of reference notation because one lazy 
programmer worked on code that you see.

Or perhaps he did not have access to change the copy book that field was in 
because he would then have to retest _all_ the programs that used the 
copybook.

(If he didn't then a later recompile of one of them may discover a bug).
 
> They don't listen .. or say it will take YEARS to effect a fix. Justice
> delayed is justice denied. I do the best I can with reality.

Hmmmm, and yet you use stuff that the Fujitsu does support and may not have 
tested and may break without them caring at all.

> The issue is collecting facts, not customer loyalty or other 'religious'
> issues. Realia was very close to the 'IBM standard'.

But collecting 'facts' about Realia isn't collecting _facts_ about IBM.

You can't comment on Intel Pentium instruction performance by measuring 
what an AMD Athlon does.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e982a1b.108171306@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[5 more quoted lines elided]…
>does.

The consequence is garbage in the output file. No amount of testing will detect
that because the obsolete field cannot be referenced. 

>> I never said that. I said I'd not seen anything but literals used in
>> production code .. as a lazy substitute for subdefining the field.
>
>So you want to eliminate all uses of reference notation because one lazy 
>programmer worked on code that you see.

I didn't advocate for or against reference modification. I just made a passing
comment that I don't like it. 

It wasn't one programmer; it was dozens to hundreds in at least five programming
shops. 

>Or perhaps he did not have access to change the copy book that field was in 
>because he would then have to retest _all_ the programs that used the 
>copybook.
>
>(If he didn't then a later recompile of one of them may discover a bug).

Fortunately, I never worked at a place with testing policies like that. Don't
give them ideas. <g>

>> The issue is collecting facts, not customer loyalty or other 'religious'
>> issues. Realia was very close to the 'IBM standard'.
…[4 more quoted lines elided]…
>what an AMD Athlon does.

The issue was syntax checking, not execution. One _can_ infer IBM syntax from
Realia, particularly when an 'IBM dialect' option is used.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-12T16:45:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304121545.28c49cda@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >That is why we do testing, we find the consequences before the customer 
> >does.
> 
> The consequence is garbage in the output file. No amount of testing will detect
> that because the obsolete field cannot be referenced. 

If the field is never referenced then there are no consequences.  If
the field is to be reused later for something else then a pass must be
made to clear it, or set it to some useful value.

In your contrived example _all_ records will have junk in the old ytd
field because the old value becomes meaningless.

But, in fact, a file dump can be part of the testing.  I often view
the actual file when testing to confirm that records are being written
correctly, don't you?

> The issue was syntax checking, not execution. One _can_ infer IBM syntax from
> Realia, particularly when an 'IBM dialect' option is used.

You can only infer what Realia _thinks_ IBM syntax is, for that
compiler that Realia tried to copy, and then only for the 99%, and not
for negatives.

While Realia may accept all programs that can be written for IBM, it
may _also_ accept syntax that IBM won't _without_ this reducing the
claim that it is IBM compatible.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T05:57:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98f84a.36755232@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote

>But, in fact, a file dump can be part of the testing.  I often view
>the actual file when testing to confirm that records are being written
>correctly, don't you?

Seldom. Only when file format is an issue. 

When running regression tests, I compare output files to previous outputs.
Microsoft's FC (file compare) and mainframe FileAid are much better than Unix's
diff. FileAid lets you mask out fields that don't matter, such as date/time in a
report header. 

>While Realia may accept all programs that can be written for IBM, it
>may _also_ accept syntax that IBM won't _without_ this reducing the
>claim that it is IBM compatible.

The test was whether NEXT SENTENCE could be used in statements other than IF.
The finding was no, it cannot. I doubt Realia would change its syntax to
prohibit usage accepted by IBM.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-13T14:25:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304131325.61ed3f9d@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >While Realia may accept all programs that can be written for IBM, it
> >may _also_ accept syntax that IBM won't _without_ this reducing the
…[4 more quoted lines elided]…
> prohibit usage accepted by IBM.

No, but what if Realia allowed NEXT SENTENCE where IBM did not ? What
wrong conclusions would you have drawn ?

It doesn't actually matter what Realia does, or does not do, what
matters is the approach that you demonstate to determining what is
factual and what is not, and the claims that you make about your
'knowledge' of things.

Whan a claim of fact is made we either accept it, based on how likely
it seems or how much confidence we place in the author, or we question
it.  So far your methodology and (lack of ) accuracy had led me to the
conclusion that everything you say must be questioned.
```

###### ↳ ↳ ↳ IBM vs Realia (was: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-13T16:46:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7cls9$an5$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com>`

```
This current discussion started with an issue of whether IBM's OS/VS COBOL
(pre-VS COBOL II) compiler did or did not accept NEXT SENTENCE in
non-Standard places.  I cannot speak with any certaintity on which
"undocumented extensions" Realia did or did not (does or does not) support.
However, I do think that it is worth reading about HOW EXTENSIVE the number
of things that the OS/VS COBOL compiler *did* accept that they never
documented as supported.  (Many of these were *dropped* in VS COBOL II -
others became documented and supported).  For others who are interested in
this, please see:

 "4.1.6 Undocumented OS/VS COBOL extensions that are not supported"
at
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg10/4.1.6

and

 "4.1.7 Language elements that changed from OS/VS COBOL"
at
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg10/4.1.7

***

Finally, as I stated in a previous thread, if anyone in this NG *thinks*
that some code compiled cleanly with OS/VS COBOL but doesn't currently have
access to that compiler, I believe there are several participants in the NG
who would be willing to try and compile with that (currently unsupported)
compiler for them.  Simply ask.

Note:
  I believe that Micro Focus offers a FLAG(OSVS) directive that will
indicate MANY items that are and are not supported by the OS/VS COBOL
compiler.  However, just as I personally wouldn't use Realia to "justify" a
claim about OS/VS COBOL, neither would I use this feature of Micro Focus.
OTOH, it might give you a "good" starting point on determining whether a
claim passes a "reasonablity" test for what OS/VS COBOL did and did not
support.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T01:19:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9a0b55.18870702@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[9 more quoted lines elided]…
>wrong conclusions would you have drawn ?

[paraphrasing my mentor, who taught me so much about scholarship]

Here we have the presumption of innocence found in a court of law being
inappropriately transferred to how logical theories are to be established or
seriously entertained.  Normally, we would argue on BEHALF of a  theory by
presenting evidence FOR it, not by pointing to our current lack of evidence
unless one is arguing AGAINST a theory. Those who argue for Realia extensions
would turn the logical process on its head. 

Now, in a general it is trivially true  that there is no  "proof" against the
notion that Realia would expand its syntax, but then there is also no ultimate
proof against unicorns or ghosts.  It is a well known informal fallacy to
conclude from a lack of disproof for something's existence that it therefore
exists or must be taken as a serious possibility for existence.  That is to
say, it is simply false to argue that a proposition is true simply on the basis
that it has not been proved false.  The idea here is to try to persuade people
of a proposition which avails itself of facts and reasons the falsity or
inadequacy of which is not readily discerned.

This flawed logic is technically referred to by logicians as the
"ARGUMENTUM AD IGNORANTIUM" (argument from ignorance).  This is a
logically invalid argument, one that would exploit our common ignorance of
things. 

>It doesn't actually matter what Realia does, or does not do, what
>matters is the approach that you demonstate to determining what is
…[6 more quoted lines elided]…
>conclusion that everything you say must be questioned.

Ordinarily I would dismiss this as irrelevant because it relies on claims of
expertise or authority. But in the instant case, I DID claim to be a COBOL
expert. So let's review my 'deficiencies'. 

..Claimed that indexes are bounds checked when set rather than when used.
...Used to be true, but no longer.

..Claimed that FILE-STATUS is non-standard for 'file not found'
...Used to be true, but no longer.

What have I forgotten? 

The pattern seems to be obsolete rather than totally incorrect information.
COBOL programmers are no strangers to obsolesence. Thus, my failings here are
less serious than they would be in, say, chip design. 

On the positive side, I've tried to introduce the list as a fundamental data
structure. Because you find them C-like doesn't diminish their utility. That's a
'religious' argument. I also advocated nested programs, which are not widely
used, especially in the mainframe community. 

What ideas have you advanced to help people _grow_ rather than become
curmudgeons?
```

###### ↳ ↳ ↳ Put up - or shut up; PLEASE (was: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-13T20:52:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7d49f$vt1$1@slb4.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9a0b55.18870702@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
> >robert@wagner.net (Robert Wagner) wrote
<snip>
>
> ..Claimed that indexes are bounds checked when set rather than when used.
> ...Used to be true, but no longer.

and your evidence that ANY compiler actually did "used to" work as you claim
they did?  And your evidence that there has been a change in some compiler
from this old behavior?

Also, the most significant error in this area was your claim that the
Standard (ANY Standard) actually required run-time validation that boundary
violations be "checked" and that some run-time behavior would indicate this.

FYI - if you actually *do* still think that there was a change from the '74
to '85 ANSI/ISO Standard concerning when index values would be checked,
please look at the section,

"Substantive Changes"

starting on page XVII-42 of the '85 Standard

    ***

This is the type of thing that annoys me (and possibly others).  You simply
keep making the same error without acknowledging that you were wrong.  There
was *no* requirement in the '74 (or any other) Standard for run-time errors
on boundary violations;  There was *no* change between the '74 and '85
Standard concerning index boundary checking; There has been *no* documented
example of a compiler changing between their '74 and '85 Standard compilers
concerning when index boundary violations were detected.

Accept AND acknowledge this - and stop make your erroneous claim on this.
```

###### ↳ ↳ ↳ Re: Put up - or shut up; PLEASE (was: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T08:15:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9a675e.42435356@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net> <b7d49f$vt1$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9a0b55.18870702@news.optonline.net...
…[10 more quoted lines elided]…
>from this old behavior?

In the '70s and '80s I worked with compilers which in fact did bounds check on
indexes when they were set. A statement as simple as 'perform .. varying
an-index from 1 by 1 until an-index greater than 100' would crap out when it
tried to set the index to 101. SEARCH had a special dispensation. 

I don't recall which compiler it was. It was probably Burrroughs medium systems
or, less likely, Honeywell.  

>Also, the most significant error in this area was your claim that the
>Standard (ANY Standard) actually required run-time validation that boundary
>violations be "checked" and that some run-time behavior would indicate this.

I never cited the Standard. I described actual performance. 

>This is the type of thing that annoys me (and possibly others).  You simply
>keep making the same error without acknowledging that you were wrong.  There
…[4 more quoted lines elided]…
>concerning when index boundary violations were detected.

You are understandably focussed on The Standard. While not ignoring standards,
my primary concern is practicality. What to do when there is a conflict? I go
with reality whereas you want to hold their feet to the fire. 

>Accept AND acknowledge this - and stop make your erroneous claim on this.

It is not erroneous. I endured it for ten years.
```

###### ↳ ↳ ↳ Re: Put up - or shut up; PLEASE (was: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-14T07:46:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7eaif$pa7$1@slb4.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net> <b7d49f$vt1$1@slb4.atl.mindspring.net> <3e9a675e.42435356@news.optonline.net>`

```
In this thread, you state,

"> I never cited the Standard. I described actual performance. "


And I quote from Robert Wagner replying to Chuck Stevens  in the thread "
COBOL indexes" in his post of 2003-02-24 17:22:13 PST

""Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e5a4b8a.526004@news.optonline.net...
>
>> I agree. The problem with indexes is that they are bounds-checked when
you
>> modify them, not when you use them.
>
>Not on all systems, and the standard does not specify when (or even
whether)
>index bounds are checked.

The Micro Focus manual, under SET, says:

"If index-name-1 is specified, the value of the index after the execution of
the
SET statement must correspond to an occurrence number of an element in the
table
associated with index-name-1. The value of the index associated with an
index-name after the execution of a PERFORM or SEARCH statement may be set
to an
occurrence number that is outside the range of its associated table."

That looks like it is quoting the standard, but I cannot find the same
language
in the '89 standard. Was it in the '85 standard?

I encountered the same manditory bounds checking on an earlier IBM mainframe
compiler. I find it hard to believe compiler vendors are making this stuff
up.

>For me, this program gets P-DS'ed at the reference to antecedent with an
>expression (the index) out of range.

Mine gets P-DS'ed when I SET the index to 101, not when I reference entry
101,
which I never do."

and replying to someone else in that same thread,

">> The Micro Focus manual, under SET, says:
>>
>> "If index-name-1 is specified, the value of the index after the execution
of the
>> SET statement must correspond to an occurrence number of an element in
the table
>> associated with index-name-1.
>
>This doesn't say that it will be bound checked and/or cause an abend
>as you asserted.

The word "must" means mandatory."

and directly to the point, you went on to post,

">> The program abends when the index is SET to 101, even though you never
reference
>> element 101. It doesn't matter whether the compiler option for bounds
checking
>> is on or off.
>> All compilers do it this way because the standard requires them to.
>
>Show me in the _standard_ ('85 or '2002) where it requires this.

I quoted Micro Focus and IBM manuals containing nearly identical language,
which
was copied from the '85 standard.

>When you have read the standard and discovered that you were clueless
>about it then you can appologise to the standards committee.

One of the committee members helpfully explained the change."
```

###### ↳ ↳ ↳ Re: Put up - or shut up; PLEASE (was: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T22:14:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b31ab.94231698@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net> <b7d49f$vt1$1@slb4.atl.mindspring.net> <3e9a675e.42435356@news.optonline.net> <b7eaif$pa7$1@slb4.atl.mindspring.net>`

```
I apologize. I'd forgotten what I said in that thread. 

Robert


"William M. Klein" <wmklein@ix.netcom.com> wrote:

>In this thread, you state,
>
…[149 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-14T00:10:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7dcc4$m0c$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net>`

```
In article <3e9a0b55.18870702@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:

[snip]

>Because you find them C-like doesn't diminish their utility. That's a
>'religious' argument.

Hmmmmm... so, by these same lights, were someone to say that they did not
like reference modification because it was BASIC-like would, likewise, not
diminish its utility and be, similarly, a 'religious' argument.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T07:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9a62d9.41277658@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net> <b7dcc4$m0c$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e9a0b55.18870702@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[8 more quoted lines elided]…
>diminish its utility and be, similarly, a 'religious' argument.

You got me there. 

DD  1
RW 0
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-14T05:55:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7e0ir$lqm$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9a0b55.18870702@news.optonline.net> <b7dcc4$m0c$1@panix1.panix.com> <3e9a62d9.41277658@news.optonline.net>`

```
In article <3e9a62d9.41277658@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[15 more quoted lines elided]…
>RW 0

Mr Wagner, I would say that the important thing here is not some kind of
schoolyardish scorekeeping; what appears to merit noticing is that what
seems to be a kind of hitherto-unnoticed double-standard was being made
manifest.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b4dde.101452605@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9a0b55.18870702@news.optonline.net> <b7dcc4$m0c$1@panix1.panix.com> <3e9a62d9.41277658@news.optonline.net> <b7e0ir$lqm$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e9a62d9.41277658@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[22 more quoted lines elided]…
>manifest.


Your withering logic revealed the truth -- I'm human. So shoot me.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-14T22:03:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7fp9h$aih$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9a62d9.41277658@news.optonline.net> <b7e0ir$lqm$1@panix1.panix.com> <3e9b4dde.101452605@news.optonline.net>`

```
In article <3e9b4dde.101452605@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[27 more quoted lines elided]…
>Your withering logic revealed the truth -- I'm human. So shoot me. 

Mr Wagner, granted that I have known only humans to display that kind of
double-standard... but not all humans I have known have done so so it 
might be possible that with diligence and care you might, possible, be 
able to change from one category to the other.

As far as shooting you goes... the possibility brings to mind the words
of that profound Philosopher, Moe Howard, from that exercise in
cinematographic art released under the title of 'Disorder in the Court' 
(Columbia Pictures, 1936) when he e'er-so-succinctly stated 'Wasted five 
perfectly good slugs on a divot'.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T23:27:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9c92a2.184604880@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9a62d9.41277658@news.optonline.net> <b7e0ir$lqm$1@panix1.panix.com> <3e9b4dde.101452605@news.optonline.net> <b7fp9h$aih$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>As far as shooting you goes... the possibility brings to mind the words
>of that profound Philosopher, Moe Howard, from that exercise in
>cinematographic art released under the title of 'Disorder in the Court' 
>(Columbia Pictures, 1936) when he e'er-so-succinctly stated 'Wasted five 
>perfectly good slugs on a divot'.

<chuckle> You have a droll sense of humor.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-15T22:09:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ie02$qvq$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9b4dde.101452605@news.optonline.net> <b7fp9h$aih$1@panix1.panix.com> <3e9c92a2.184604880@news.optonline.net>`

```
In article <3e9c92a2.184604880@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[6 more quoted lines elided]…
><chuckle> You have a droll sense of humor. 

Pfoo... you'se jes' easily amused.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-13T22:32:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304132132.536b3421@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >No, but what if Realia allowed NEXT SENTENCE where IBM did not ? What
> >wrong conclusions would you have drawn ?
…[3 more quoted lines elided]…
> basis that it has not been proved false.

First of all you should note that my claim was in the form of
speculation and was not a claim of true or false.

> This flawed logic is technically referred to by logicians as the
> "ARGUMENTUM AD IGNORANTIUM" (argument from ignorance).  This is a
> logically invalid argument, one that would exploit our common ignorance of
> things. 

You completely mis-understand the issue.

You were arguing about a product based on _something_different_.

It doesn't matter what you prove to be false or true about the
different product, it is still not the actual product.

> Ordinarily I would dismiss this as irrelevant because it relies on claims of
> expertise or authority. But in the instant case, I DID claim to be a COBOL
…[3 more quoted lines elided]…
> ...Used to be true, but no longer.

> ..Claimed that FILE-STATUS is non-standard for 'file not found'
> ...Used to be true, but no longer.
> 
> What have I forgotten? 

Dozens.  Your ability to ignore, dismiss and deflect seems almost
infinite.

* That the standards committee had not provided century date
  (and criticised for this, even though they had).
* Did not know that intrinsic functions were standard
* Did not know what 'user functions' meant
* Called Nested Procedures as Functions (which they are not)
* Failed to know that BINARY could have V and be > S9(9).
* Claimed things could not be done with UNSTRING
* Thought NEXT SENTENCE was a statement
* Failed to understand conditional/imperitive
* Confused standard Cobol and extensions
* Failed to identfy actual cause of report program failure
  (while claiming you had and no one else was clever enough).

I am sure that others can be added.
 
> The pattern seems to be obsolete rather than totally incorrect information.

You manage to offer both, in large quantities.

This just highlights that you will _never_ understand other's
attitudes to you. Here you almost claim that you are 'always right'
(with a couple of minor 'used to be') when actually you are almost
always WRONG.

> On the positive side, I've tried to introduce the list as a fundamental data
> structure. Because you find them C-like doesn't diminish their utility. That's a
> 'religious' argument. 

It wasn't that you 'introduced' linked lists, that was hardly a
novelty, but you advocated them as a general replacement for tables
regardless of the disadvantages that they have.

You have an emotional attachment to lists and therefore ignore the
disadvantages.

I don't dislike them because they are C-like, though it doesn't
surprise me one little bit that you filtered out all my substantive
objections and substituted this superficial one _that_I_never_made_.

What I _did_ say about C-like is that you had objected to C-like code
while advocating the very C-like linked lists using pointers.

> What ideas have you advanced to help people _grow_ rather than become
> curmudgeons?

Why don't you do some googling.

I suppose that you think that your 'contributions' have made people
'grow' with your vast knowledge and experience.  Sorry, but your
errors get in the way too much.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T00:14:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b32ca.94518799@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <217e491a.0304131325.61ed3f9d@posting.google.com> <3e9a0b55.18870702@news.optonline.net> <217e491a.0304132132.536b3421@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[20 more quoted lines elided]…
>different product, it is still not the actual product.

It a replica of the actual product. I don't have access to an IBM compiler, so I
did the best I could with the tools available. Pragmatism is a good thing.

Since the results CONFIRMED the assertion, I don't know what your argument is.
If it's a free lesson in problem solving methodology, you'd do better to attach
it to debate where it has some relevance. 

>> Ordinarily I would dismiss this as irrelevant because it relies on claims of
>> expertise or authority. But in the instant case, I DID claim to be a COBOL
…[17 more quoted lines elided]…
>* Called Nested Procedures as Functions (which they are not)

Four variants on functions. Ok, your single point is valid.

>* Failed to know that BINARY could have V and be > S9(9).

Another valid point -- the first one.

As for the second, my Best Practices gave this example:
01  long-integer		comp-5	pic s9(18).	*> eight bytes, 64bits

>* Claimed things could not be done with UNSTRING
>* Thought NEXT SENTENCE was a statement
…[3 more quoted lines elided]…
>  (while claiming you had and no one else was clever enough).

These are all clutching at straws. There are an infinite number of things which
cannot be done with UNSTRING. If you want to make a point, you need to be
specific. I don't recall commenting on the distinction between statements and
phrases because I regard it as meaningless hair-splitting. As for the student
question in the last bulleted line, we're told repeatedly not to do the
student's homework, so I limited my comments to the non-obvious (to the student)
logic error. 

>I am sure that others can be added.

You should set up a folder to collect them, waiting for the right moment to
spring them on me. 

>This just highlights that you will _never_ understand other's
>attitudes to you. Here you almost claim that you are 'always right'
>(with a couple of minor 'used to be') when actually you are almost
>always WRONG.

Hand waving. You haven't shown that. You've shown two new instances. 

>> On the positive side, I've tried to introduce the list as a fundamental data
>> structure. Because you find them C-like doesn't diminish their utility.
That's a
>> 'religious' argument. 
>
…[9 more quoted lines elided]…
>objections and substituted this superficial one _that_I_never_made_.

I don't have time to dig through the archive. 

>What I _did_ say about C-like is that you had objected to C-like code
>while advocating the very C-like linked lists using pointers.

I regard them as basic data structures. They weren't 'invented' by the C
languge; they've been used since computers began. The news here in this COBOL
forum is that compilers and the standard finally offer them. 

>> What ideas have you advanced to help people _grow_ rather than become
>> curmudgeons?
>
>Why don't you do some googling.

I did briefly. I saw you brow-beating a guy in an x86 assembly language forum,
similar to your behavior here. 

I used to be a hotshot assembly language programmer. I did x86 full-time for six
years during which I wrote a commercial operating system as well as device
drivers, TSRs, copy-protection hacks (notably a complete break of ProLok) and
lots of security stuff (shootouts with guys at Mitre). It's fortunate I didn't
subscribe to that newsgroup, where I would have been informed I didn't know
jack. 

>I suppose that you think that your 'contributions' have made people
>'grow' with your vast knowledge and experience.  Sorry, but your
>errors get in the way too much.

For you. Let's let others judge for themselves.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-17T22:38:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WIOdnYerZf6y-AKjXTWcqw@comcast.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e98f84a.36755232@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
…[9 more quoted lines elided]…
> Microsoft's FC (file compare) and mainframe FileAid are much better than
Unix's
> diff. FileAid lets you mask out fields that don't matter, such as
date/time in a
> report header.
>
…[4 more quoted lines elided]…
> The test was whether NEXT SENTENCE could be used in statements other than
IF.
> The finding was no, it cannot. I doubt Realia would change its syntax to
> prohibit usage accepted by IBM.
>

    To be honest, any question concerning NEXT SENTENCE is moot.  As with
ALTER,
it is so dangerous that it should not be used, ever.  It is not safe, even
in old code.

    It can be used with the no period technique, but unless periods are
banned,
NEXT SENTENCE is a time bomb, and serves no usefull purpose.

    If you want a go to, use one.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-18T09:14:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7p89j$23jo$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <WIOdnYerZf6y-AKjXTWcqw@comcast.com>`

```
Just as a point of clarification:  ALTER was marked as obsolete in the '85
standard and is GONE from the '02 standard (though some implementors might
be tempted to retain it as an extension for compatibility.  My opinion:  bad
idea.).

    -Chuck Stevens

"Russell Styles" <RWS0202@comcast.net> wrote in message
news:WIOdnYerZf6y-AKjXTWcqw@comcast.com...
>
> "Robert Wagner" <robert@wagner.net> wrote in message
…[11 more quoted lines elided]…
> > When running regression tests, I compare output files to previous
outputs.
> > Microsoft's FC (file compare) and mainframe FileAid are much better than
> Unix's
…[8 more quoted lines elided]…
> > The test was whether NEXT SENTENCE could be used in statements other
than
> IF.
> > The finding was no, it cannot. I doubt Realia would change its syntax to
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-04-18T14:15:45-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA032C1.E4F02031@istar.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <WIOdnYerZf6y-AKjXTWcqw@comcast.com> <b7p89j$23jo$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> 
> Just as a point of clarification:  ALTER was marked as obsolete in the '85
> standard and is GONE from the '02 standard (though some implementors might
> be tempted to retain it as an extension for compatibility.  My opinion:  bad
> idea.).

Only if all of the programs that I wrote in the 1960's and maybe early
1970's are now dead or rewritten.  Otherwise, noone will want to make
the changes.  I did it originally to save memory on a 32K IBM S360 and
would scrounge a different way.  I now will not code a GO TO because it
messes up compiler optimization.
> 
>     -Chuck Stevens
**** rest snipped
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-18T15:07:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7plta$5qo$1@slb1.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <WIOdnYerZf6y-AKjXTWcqw@comcast.com> <b7p89j$23jo$1@si05.rsvl.unisys.com> <3EA032C1.E4F02031@istar.ca>`

```
Clark,
  I think you work (primarily? exclusively?) in IBM mainframe environments.

So far IBM:
 - has given no indication that they will EVER (much less soon) produce a
2002 conforming compiler
 - previously indicated that they had no intention of "ever" removing
support for OBSOLETE items - even after they were removed from following
Standards.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:04:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80tov$so6$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <WIOdnYerZf6y-AKjXTWcqw@comcast.com>`

```

On 17-Apr-2003, "Russell Styles" <RWS0202@comcast.net> wrote:

>     To be honest, any question concerning NEXT SENTENCE is moot.  As with
> ALTER,
> it is so dangerous that it should not be used, ever.  It is not safe, even
> in old code.

Agreed.   Terminate every IF and in most environments NEXT SENTENCE won't even
compile.  (It will with IBM mainframes though).

>     It can be used with the no period technique, but unless periods are
> banned,
> NEXT SENTENCE is a time bomb, and serves no useful purpose.

You mean as an EXIT PARAGRAPH?    This is more dangerous than using it with
periods.   Good terminated code will not work wrong if a period is found.  I
don't call this good code.

>     If you want a go to, use one.

Agreed, if your optimizer understands.     GO TO ABORT works for me.   I detest
GO TO EXIT-PARAGRAPH.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T13:56:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80tap$sgl$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> The test was whether NEXT SENTENCE could be used in statements other than IF.
> The finding was no, it cannot. I doubt Realia would change its syntax to
> prohibit usage accepted by IBM.

Since that behavior is prohibited by ANSI, why not?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T16:40:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea41bd9.238771191@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76165$ffd$1@aklobs.kc.net.nz> <3e982a1b.108171306@news.optonline.net> <217e491a.0304121545.28c49cda@posting.google.com> <3e98f84a.36755232@news.optonline.net> <b80tap$sgl$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[5 more quoted lines elided]…
>Since that behavior is prohibited by ANSI, why not?

Because Realia was marketed as an IBM clone. Its documentation was a copy of the
IBM published COBOL manual.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-11T14:43:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76kb6$o74$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net>`

```

On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> The issue is not in development, it is in maintenance. A maintenance
> programmer
> might not know that a record is being INITIALIZEd. (S)he might change a
> data-name to filler without understanding the consequences.

A newbie might make lots of silly errors.  But why in the world would (s)he make
this one?   Is there some problem a maintenance programmer could solve by
changing a data name to a filler?    I'm not thinking of one.


BTW:    I think of an old "Karmac" joke.

Answer:    9-W


Question:   Do you spell your name with a "V", herr Wagner?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-11T12:30:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304111130.6ab72566@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> A newbie might make lots of silly errors.  But why in the world would (s)he make
> this one?   Is there some problem a maintenance programmer could solve by
> changing a data name to a filler?    I'm not thinking of one.

A W-S record area has a VALUE clause and somehow the VALUE becomes
space filled, how do you solve this when INITIALISE is used on the
record ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-17T22:44:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7iydnVSE5Jcf-wKjXTWcpg@comcast.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <217e491a.0304111130.6ab72566@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304111130.6ab72566@posting.google.com...
> "Howard Brazee" <howard@brazee.net> wrote
>
> > A newbie might make lots of silly errors.  But why in the world would
(s)he make
> > this one?   Is there some problem a maintenance programmer could solve
by
> > changing a data name to a filler?    I'm not thinking of one.
>
> A W-S record area has a VALUE clause and somehow the VALUE becomes
> space filled, how do you solve this when INITIALISE is used on the
> record ?

    I do this, in "general" working storage, by putting items
with a value clause into an 01 by themselves, and
NEVER initializing it.

    Other initializes I prefix with a move spaces.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e982cd1.108864644@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[6 more quoted lines elided]…
>A newbie might make lots of silly errors.  But why in the world would (s)he
make
>this one?   Is there some problem a maintenance programmer could solve by
>changing a data name to a filler?    I'm not thinking of one.

That's easy. Suppose YTD-EARNINGS has a pic of s9(7)v99. We want to change it to
s9(9)v99 (short-sighted, I know). We change the old field to filler and create a
new YTD-EARNINGS in the reserved-for-expansion area  at the end of the record.
There is no need to change affected programs; just recompile them. 

Now, every new employee gets garbage in that field .. most likely ytd earnings
of the previous employee. Then we discover we forgot to recompile one program.
It is reporting a file clerk earning $100K. 

Something like this actually happened at a major credit card company where I
worked. In that case, every new cardholder got a 'beginning balance' from
another cardholder. Statements went out for a month without any complaint from
cardholders. Half of them paid the beginning balance. The person who finally
pointed it out was a newly hired VP of Operations at the credit card company!!,
when he got his first statement. It was a Major Whoops. 

I actually saw the programmer who did it standing in front of an open 12th floor
window, extremely despondent and thinking of jumping. Instead they promoted him
to IT manager and I took over programming. <g> I'm not making this up.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-12T16:25:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304121525.d0079e@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> That's easy. Suppose YTD-EARNINGS has a pic of s9(7)v99. We want to change it to
> s9(9)v99 (short-sighted, I know). We change the old field to filler and create a
> new YTD-EARNINGS in the reserved-for-expansion area  at the end of the record.
> There is no need to change affected programs; just recompile them. 

No, that is not all that is needed.  Some program must run through the
file moving the data to the new YTD-EARNINGS, using say:

         MOVE FILLER     TO YTD-EARNINGS

No, that won't work.  Ohhh, I am confused, what can I do.  I know, we
_don't_ change it to FILLER, we change it to OLD-YTD-EARNINGS and then
we can say:

         MOVE OLD-YTD-EARNINGS TO YTD-EARNINGS

> Now, every new employee gets garbage in that field .. 

Not any more, not whan a realistic scenario is used.

> Then we discover we forgot to recompile one program.
> It is reporting a file clerk earning $100K. 

Well, Duhhh, that is _why_ we retest all programs using that.

> Something like this actually happened at a major credit card company where I
> worked. In that case, every new cardholder got a 'beginning balance' from
> another cardholder. 

But that is not 'like this'.  You are now saying that a
FIELD_THAT_WAS_USED got a value from a previous record.  Can you
explain how the 'beginning balance' was a FILLER and yet was used. 
Perhaps it wasn't INITIALISE's 'fault' at all in that case after all. 
Perhaps INITIALISE wasn't used, perhaps it was nothing to do with
FILLER.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T01:29:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98b4e3.19498154@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>> Something like this actually happened at a major credit card company where I
>> worked. In that case, every new cardholder got a 'beginning balance' from
…[7 more quoted lines elided]…
>FILLER.

You're right. It predated INITIALIZE, but the idea was similar. The program had
been initializing a new cardholder by moving low-values to the 500 byte record.
Other code appeared to initialize fields individually (with the overlooked
exception of previous balance), so the programmer tried to increase speed by
eliminating movement of low-values to 500 bytes. 

I said "something like this". Maybe I'm neurotic, but I'm unconfortable with
records containing garbage. The INITIALIZE verb promotes that.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:07:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80tu4$soj$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com> <3e98b4e3.19498154@news.optonline.net>`

```

On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> I said "something like this". Maybe I'm neurotic, but I'm unconfortable with
> records containing garbage. The INITIALIZE verb promotes that.

How about records containing data you are not interested in?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T16:40:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea41c4a.238884162@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com> <3e98b4e3.19498154@news.optonline.net> <b80tu4$soj$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 12-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[4 more quoted lines elided]…
>How about records containing data you are not interested in?

Now you're playing with fire. Commenting out data by changing the name to FILLER
is an invitation for some maintenance programmer to move spaces to the record.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T01:29:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98bb57.21149560@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>No, that is not all that is needed.  Some program must run through the
>file moving the data to the new YTD-EARNINGS, using say:
…[7 more quoted lines elided]…
>         MOVE OLD-YTD-EARNINGS TO YTD-EARNINGS

We probably used a utility like FileAid to do it rather than writing a COBOL
program. 

>> Then we discover we forgot to recompile one program.
>> It is reporting a file clerk earning $100K. 
>
>Well, Duhhh, that is _why_ we retest all programs using that.

If we'd known at the program in Joe Shmoe's private library, we would have
recompiled it. He runs it quarterly for his buddy in HR. He never bothered to
put it into production.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-14T12:51:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304141151.567a1b06@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com> <3e98bb57.21149560@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >No, that won't work.  Ohhh, I am confused, what can I do.  I know, we
> >_don't_ change it to FILLER, we change it to OLD-YTD-EARNINGS and then
…[9 more quoted lines elided]…
> put it into production.

You continue to bring up more and more problems and yet never see that
there can be solutions.  You may have felt insulted at being called a
'coder', but you behave like one.

Anyone with two clues to rub together would have noticed that all
these problems cease to exist with a properly designed file
modification.

One could, for example, have the update program continuing to
increment both the old (named) field and the new one.

Or better, one could not only move the old (named) field over to the
new one, but could zeroise the old.  Then Joe Shmoe would get zero and
would actually notice, which is a vast improvement over getting wrong
results.

Once there is a culture of solving problems, rather than just whining
about them as coders do, then these issues get resolved
satisfactorily.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T23:27:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9c8ea7.183585328@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com> <3e98bb57.21149560@news.optonline.net> <217e491a.0304141151.567a1b06@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[31 more quoted lines elided]…
>satisfactorily.

I too have a better idea. Write an 'access module' which returns the requested
'logical view' of the payroll file. Joe's program will get the _new_
YTD-EARNINGS truncated to the old format. Production programs will get the
expanded field. 

Doesn't this require a lot of work? Don't we have to change all production
programs to ask for a new view and use a new copybook? No. The view ID can be in
a copybook and the old production record copybook can contain a one-line
reference to the new one. 

That's the kinda solution you'd get from a system designer. Redundant updates
and zeroising fields is are the kind you'd get from a coder.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-15T22:35:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304152135.6486beef@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com> <3e98bb57.21149560@news.optonline.net> <217e491a.0304141151.567a1b06@posting.google.com> <3e9c8ea7.183585328@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> That's the kinda solution you'd get from a system designer. 

But your examples _weren't_ designing a system, they were a small
maintenance item.  Solutions should be appropriate to the scope of the
problem, systems designers know that, coders don't.

> Redundant updates
> and zeroising fields is are the kind you'd get from a coder.

The problems in your examples were because the fields _weren't_
zeroised. If you had suggested that you would have been at least as
good as a coder.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-17T22:48:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agmdnU5DdYU4-gKjXTWcog@comcast.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76kb6$o74$1@peabody.colorado.edu> <3e982cd1.108864644@news.optonline.net> <217e491a.0304121525.d0079e@posting.google.com> <3e98bb57.21149560@news.optonline.net> <217e491a.0304141151.567a1b06@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304141151.567a1b06@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote
>
…[9 more quoted lines elided]…
> > If we'd known at the program in Joe Shmoe's private library, we would
have
> > recompiled it. He runs it quarterly for his buddy in HR. He never
bothered to
> > put it into production.
>
…[18 more quoted lines elided]…
> satisfactorily.

    Maybe everybody is perfect where you come from, but around here
they are not.  If you try to buy trouble, you just might get it.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-11T08:53:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76odq$156a$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9607da.354872922@news.optonline.net...
> Current-date returns alphanumeric date and time, whereas date-of-integer
returns
> an 'integer' date. The latter says it returns (YYYY * 10000) + (MM * 100)
+ DD.

No.  Date-of-integer returns the number of days after December 31, 1600 that
the argument, an integer in the form YYYYMMDD, represents.  It's
Integer-of-date that takes a date represented as the number of days past
December 31, 1600 and turns it into a calendar date.

> Why doesn't the former return a similar integer version of
yyyymmddhhmmsshh?

Uhhh... because it doesn't; the people who asked for it wanted it to contain
MORE than that, and the designers agreed.   You left off five characters,
one of which is an embedded sign.  You may not have NEED for local-time
conversion offsets from GMT, but some people have actually found such things
useful.  If your system returns a "0" in the 17th character position, IT
doesn't support GMT offset, and thus the remaining four character positions
aren't meaningful.  But that character position can also be "+" or "-".

What is the source of your expectation that CURRENT-DATE return the same
thing as DATE-OF-INTEGER (or, for that matter, INTEGER-OF-DATE), contrary to
their official descriptions?



> I do that kind of stuff all the time. Go through a document tallying where
> numbers begin and end, then find the max, blank out nearby columns and
find the
> next max. Whoops. FUNCTION MAX doesn't tell me WHERE it found the max.
Back to
> longhand code.

Nope.  Wrong again.  Back to FUNCTION ORD-MAX.

> The issue is not in development, it is in maintenance. A maintenance
programmer
> might not know that a record is being INITIALIZEd. (S)he might change a
> data-name to filler without understanding the consequences.

That's a programming error, not a failure on the part of the construct, just
like all sorts of other programming errors.


> They don't listen .. or say it will take YEARS to effect a fix. Justice
delayed
> is justice denied. I do the best I can with reality.

Who be "they"?   Certainly the folks that work on the compilers I'm familiar
with listen.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98352b.111003306@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[9 more quoted lines elided]…
>December 31, 1600 and turns it into a calendar date.

You got the functions backwards. 

>> Why doesn't the former return a similar integer version of
>yyyymmddhhmmsshh?
…[11 more quoted lines elided]…
>their official descriptions?

Consistancy. One function returns a date as a string whereas another returns it
as an integer, which it is not. 

The COBOL-like solution is none of the above. Why didn't they give us a date
TYPE? Then we really could 'add 1 to a date', except it would probably be 'set
date up by 1'. 

>> I do that kind of stuff all the time. Go through a document tallying where
>> numbers begin and end, then find the max, blank out nearby columns and
…[5 more quoted lines elided]…
>Nope.  Wrong again.  Back to FUNCTION ORD-MAX.

Yes. Yesterday, I actually changed a production program to use ORD-MAX.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T10:07:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7eptg$hga$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e98352b.111003306@news.optonline.net...
> >> Current-date returns alphanumeric date and time, whereas
date-of-integer
> >returns
> >> an 'integer' date. The latter says it returns (YYYY * 10000) + (MM *
100)
> >+ DD.
> >
> >No.  Date-of-integer returns the number of days after December 31, 1600
that
> >the argument, an integer in the form YYYYMMDD, represents.  It's
> >Integer-of-date that takes a date represented as the number of days past
> >December 31, 1600 and turns it into a calendar date.
>
> You got the functions backwards.

Yes, you're right.  DATE-OF-INTEGER produces an integer that can be
interpreted as YYYYMMDD from integer days past 12/31/1600; INTEGER-OF-DAY
produces days past 12/31/1600 from an integer value, interpreting it as a
decimal gregorian date in the form YYYYMMDD.

> >What is the source of your expectation that CURRENT-DATE return the same
> >thing as DATE-OF-INTEGER (or, for that matter, INTEGER-OF-DATE), contrary
to
> >their official descriptions?
>
> Consistancy. One function returns a date as a string whereas another
returns it
> as an integer, which it is not.

Might try reading the standard to understand which expectations you might
have are reasonable and which are not.  If you want to get your shorts in a
bunch because The World Isn't Exactly The Way I Want It To Be, well, I guess
you're free to do that, but all you'll accomplish is getting your shorts in
a bunch.  The date CONVERSION functions DATE-OF-INTEGER and INTEGER-OF-DATE
have been documented as returning a value in INTEGER NUMERIC form, and the
date RETRIEVAL functions CURRENT-DATE and WHEN-COMPILED a value in
ALPHANUMERIC form, for fourteen years now, and you seem to be the only one
complaining about the fact that two sets of routines designed for two
different purposes produce their results in different forms!

One set returns strings because they return more than a date.  The other set
returns values in integer form.

Where do you get the idea that when the standard says that the "type" of the
function is integer that the function is NOT returning an integer?

The standard committee could arguably have entitled the date RETRIEVAL
routines something a bit more complete like  like
CURRENT-DATE-TIME-AND-TIME-ZONE-OFFSET-FROM-COORDINATED-UNIVERSAL-TIME-AS-RE
PRESENTED-IN-CHARACTER-FORMAT-AS-OF-TIME-OF-CALL and
CURRENT-DATE-TIME-AND-TIME-ZONE-OFFSET-FROM-COORDINATED-UNIVERSAL-TIME-AS-RE
PRESENTED-IN-CHARACTER-FORMAT-AS-OF-TIME-OF-PROGRAM-UNIT-COMPILATION, I
suppose, but I am not yet convinced that such function-names (and the
required expansion of the number of characters COBOL needs to support in
defining identifiers) would provide a significant improvement to the
language or the clarity of the user code.

Furthermore, I believe CURRENT-DATE and WHEN-COMPILED have twenty-two digits
of numeric information, plus a character indicating both the validity of
four of those digits as well as how they are to be interpreted, precisely
because the designers of the function, way back in the 1980's, had
sufficient indication from the user community that the information provided
by CURRENT-DATE and WHEN-COMPILED was useful enough so as to warrant the
format as it now stands (despite the assertions that there was no user input
into the standards development process!).

I'm sorry you think they were wrong; as I've said before, with the 2002
standard you are free to develop your own functions (under a different name,
of course) and market them to all and sundry.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-14T18:42:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304141600.5cd7bab6@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote 

> > Consistancy. One function returns a date as a string whereas another
>  returns it
…[3 more quoted lines elided]…
> function is integer that the function is NOT returning an integer?

It is probably because RW thinks that a 'cardinal' is type of bird, or
someone in a church hierarchy.

A date in a numeric form such as 20030415 is a perfectly good integer,
of course it is not a cardinal number, though it may resemble one.  RW
is making the wrong argument.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T11:15:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9be3b7.139819159@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>"Chuck Stevens" <charles.stevens@unisys.com> wrote 
>
…[12 more quoted lines elided]…
>is making the wrong argument.

A cardinal number specifies the number of things in a set. For example, 12
months in a year. 'OCCURS 12' is a cardinal number. 

An ordinal number does that and additionally specifies the order of things
within a set. For example, 88 January value 01, 88 February value 02 ...

An integer, which derives from entire, specifies an ordinal set with no holes in
it. For example, -32768 thru 32767.

A date is an ordinal; it is not an integer.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-15T09:09:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7h09c$b3$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net>`

```
In article <3e9be3b7.139819159@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:

[snip]

>An integer, which derives from entire, specifies an ordinal set with no holes in
>it. For example, -32768 thru 32767.

Mr Wagner, this equating an 'integer' with a range of numbers is entirely 
new to me; please be so kind as to supply the source from which you 
derived it.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-15T19:33:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x8Zma.574$%_3.434068@newssrv26.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:b7h09c$b3$1@panix1.panix.com...
> In article <3e9be3b7.139819159@news.optonline.net>,
> Robert Wagner <robert@wagner.net> wrote:
…[3 more quoted lines elided]…
> >An integer, which derives from entire, specifies an ordinal set with no
holes in
> >it. For example, -32768 thru 32767.
>
> Mr Wagner, this equating an 'integer' with a range of numbers is entirely
> new to me; please be so kind as to supply the source from which you
> derived it.


Mr Wagner made no such equation. The equation he made was,  "an ordinal set
with no holes in it" [A simply awful  choice of words. Ed.]

The range was clearly prefaced by, "for example."

ADD 1 TO NOISE
SUBTRACT 1 FROM SIGNAL

MCM
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-15T15:35:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7hmu5$79l$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <x8Zma.574$%_3.434068@newssrv26.news.prodigy.com>`

```
In article <x8Zma.574$%_3.434068@newssrv26.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:
><docdwarf@panix.com> wrote in message news:b7h09c$b3$1@panix1.panix.com...
>> In article <3e9be3b7.139819159@news.optonline.net>,
…[13 more quoted lines elided]…
>with no holes in it" [A simply awful  choice of words. Ed.]

Perhaps Mr Wagner might be able to clarify his own words... and, of 
course, if he both chooses and is capable of doing so it might be 
addressed.

If he chooses, is capable and attempts to do so in the manner suggested 
above, of course, then it might be pointed out that what was described 
appears to be 'a series of things in a line' (in the classic Dedekind use 
of a number-line) which is, according to the WRU, a definition of 
'range'.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-15T14:45:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304151345.6c829774@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <x8Zma.574$%_3.434068@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote 

> > >An integer, which derives from entire, specifies an ordinal set with no
>  holes in
…[7 more quoted lines elided]…
> with no holes in it" [A simply awful  choice of words. Ed.]

In what way is 'an ordinal set with no holes' [sic] _not_ a 'range of
numbers' ?

In what way is 'An integer .. specifies ..' _not_ equating ?
 
> The range was clearly prefaced by, "for example."

The example range was clearly prefixed by "for example:".

RW mistakes what an 'interger' is and how some computers may store a
limited range of integers.

The drink is not the bottle.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-15T22:13:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ie8o$iv$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <x8Zma.574$%_3.434068@newssrv26.news.prodigy.com> <217e491a.0304151345.6c829774@posting.google.com>`

```
In article <217e491a.0304151345.6c829774@posting.google.com>,
Richard <riplin@Azonic.co.nz> wrote:

[snip of all context]

>The drink is not the bottle.

Ceci N'est Pas Une Pipe.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T23:27:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9c8130.180137914@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e9be3b7.139819159@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[3 more quoted lines elided]…
>>An integer, which derives from entire, specifies an ordinal set with no holes
in
>>it. For example, -32768 thru 32767.
>
>Mr Wagner, this equating an 'integer' with a range of numbers is entirely 
>new to me; please be so kind as to supply the source from which you 
>derived it.

I defined it as a set and used range as an example. It may be valid to define a
range, depending on the context of the word integer. The source was my logic,
below. 

In math, per below references, the range of an integer is negative infinity to
positive infinity. We're not doing math, we're doing computer programming. There
is no such thing as infinity in a computer. The range of an computer integer is
usually determined by machine word size and/or compiler type size (e.g. COBOL's
18 digits). One could write a library or OO class which does arithmetic on
million-digit integers, but there must be a limit somewhere (due to finite disk
space). 

In programming the word integer is used in two contexts. Here, we are using it
in the abstract. The C language and others use it to mean 16-bit word, to
distinguish it from tiny int and long int. So in the latter context, integer is
defined as -32768 through +32767; in the former, it could be defined as a set of
numbers containing no gaps within a range specified by the type. 

Dates contain gaps on the integer scale. For instance, there is a gap between
20030331 and 20030401.. Therefore, dates are not integers. 

The key concept here is the set. The word for limiting an set's range is called
cardinalization. Richard's introduction of the word cardinal started this
thread. 

http://searchvb.techtarget.com/gDefinition/0,294236,sid8_gci212358,00.html

http://searchsecurity.techtarget.com/sDefinition/0,290660,sid14_gci333100,00.html
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-15T22:23:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ieql$3h9$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net>`

```
In article <3e9c8130.180137914@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[14 more quoted lines elided]…
>below. 

If the source is your logic (posted, quite obviously, a posteriori the 
use) then it can be concluded that your use is completely idiosyncratic... 
not that there is anything wrong, per se, with idiosyncratic definitions, 
mind you, but it might be a superior course of action to post said 
definitions before their use so as to avoid confusion.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-15T23:27:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304152227.6c182d7a@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >>An integer, which derives from entire, specifies an ordinal set with no holes
> >> in it. For example, -32768 thru 32767.

> I defined it as a set and used range as an example. 

Perhaps you don't know that 'ordinal numbers' are positive integers so
your 'definition' makes no sense at all.

> The C language and others use it to mean 16-bit word, to
> distinguish it from tiny int and long int. 

You don't know much about C, do you. C does not specify at all what
size an 'int' is, only that it be a size suitable for the machine.  It
may be 16bit, or 32bit, or 36, or 60bit or some other.  short (not
'tiny') and long may be the same size as int or a short may be smaller
than int, and a long larger.

But C does _not_ use 'integer' to _mean_ anything.  It does use type
'int' to create a variable which can _contain_ an integer.

> So in the latter context, integer is
> defined as -32768 through +32767; 

No. Wrong. while a 16bit signed (short) variable can contain an
integer in the range specified, this does _not_ define what an
'integer' _is_, only what a varible of type int (or short) can
contain.

> in the former, it could be defined as a set of
> numbers containing no gaps within a range specified by the type. 

In Cobol I can have a field PIC S9999PP which can contain an integer
in a range that _does_ have gaps.

As is usual you start with some unfounded conclusion that you asserted
and then just make stuff up to attempt to support this.

> Dates contain gaps on the integer scale. For instance, there is a gap between
> 20030331 and 20030401.. Therefore, dates are not integers. 

What crap.  The gaps stop it being a cardinal, they stop it being an
ordinal. But only adding a decimal part will stop it being an integer.

This is why I said you were making the wrong argument.  It _is_ an
integer, it is not a cardinal or an ordinal.

So far you have simply demonstrated that you do not understand
ordinals and integers, nor C.

> The key concept here is the set. The word for limiting an set's range is 
> called cardinalization. 

Which is quite irrelevant because dates represented as 20030415 are
not cardinals.

> http://searchvb.techtarget.com/gDefinition/0,294236,sid8_gci212358,00.html

Exactly:

"""An integer (pronounced IN-tuh-jer) is a whole number (not a
fractional number) that can be positive, negative, or zero."""
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-17T00:07:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9de0f1.270200298@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

Here is the history of how we got to this point. First there was math, which
defines its words very rigorously.

Second came programming language designers who used the technical words from
math but, in some cases, used them incorrectly. 

Third came programming students, innumerate beyond high-school math,  who
learned all their 'math terminology' from flawed programming languages. 

Now we have those matured students arguing 'their' terminology (actually,
language designers' terminology) is correct. They make silly statements such as
"Simple numbers are divided into two groups: integer and real.  If it is a 
number then it is either an integer or a real number." which fails to apprehend
the fact that integers are all real numbers. Your statement derives from two
data types provided by programming languages: fixed point and floating point. If
language designers had used the simpler terms fixed and floating, they wouldn't
have miseducated you. In fact, the two kinds of numbers are real and complex,
which includes imaginary. You didn't learn that terminology because most
programming languages don't support complex numbers. 

Applying the wrong name to something doesn't make it so. For instance, calling a
date an integer doesn't make it an integer, it only makes it misrepresented.  

>> >>An integer, which derives from entire, specifies an ordinal set with no
holes
>> >> in it. For example, -32768 thru 32767.
>
…[3 more quoted lines elided]…
>your 'definition' makes no sense at all.

Nonsense. Ordinal means a member of an ordered set (more on this when get to
dates). An ordinal number is a member of an ordered set containing exclusively
numbers. They can be positive or negative. 

>> The C language and others use it to mean 16-bit word, to
>> distinguish it from tiny int and long int. 
…[4 more quoted lines elided]…
>'tiny') and long may be the same size as int or a short may be smaller

'Tiny' is an 8-bit integer in some implementations. You are technically correct,
but I've not seen a C compiler which used int for anything but 16-bit short int.
Changing it to 32-bit would 'break' many programs. 

This is analogous to COBOL's BINARY or (vendor extension) unsuffixed COMP. It
can mean whatever you want it to mean. That sounds good in the conference room,
but hardly supports portability. 

>> So in the latter context, integer is
>> defined as -32768 through +32767; 
…[4 more quoted lines elided]…
>contain.

That's what I said in the passages you snipped. If integer is defined as 16
bits, as it is in C, then it is defined by the range +-32K. If the definition is
generic, its range (cardinality) is defined by the data type. 

>> in the former, it could be defined as a set of
>> numbers containing no gaps within a range specified by the type. 
>
>In Cobol I can have a field PIC S9999PP which can contain an integer
>in a range that _does_ have gaps.

In that case, it's not an integer. 

>As is usual you start with some unfounded conclusion that you asserted
>and then just make stuff up to attempt to support this.

When reason flags, resort to ad hominem. 

>> Dates contain gaps on the integer scale. For instance, there is a gap between
>> 20030331 and 20030401.. Therefore, dates are not integers. 
…[4 more quoted lines elided]…
>integer, it is not a cardinal or an ordinal.

Integers are both cardinal (in the computer) and ordinal. You've been so badly
miseducated, your statements make no sense. 

>> The key concept here is the set. The word for limiting an set's range is 
>> called cardinalization. 
>
>Which is quite irrelevant because dates represented as 20030415 are
>not cardinals.

Out of curiosity, what do you think cardinal means? I defined it as range and
used OCCURS as an example. Evidently you are working from another (faulty)
definition.
```

###### ↳ ↳ ↳ Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-16T19:51:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ktr1$bgp$1@slb4.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9de0f1.270200298@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
> >robert@wagner.net (Robert Wagner) wrote
>
<snip>
> >> in the former, it could be defined as a set of
> >> numbers containing no gaps within a range specified by the type.
…[4 more quoted lines elided]…
> In that case, it's not an integer.

PIC S9999PP

is a COBOL construct.  Therefore, *ONLY* the COBOL definition of an integer
should be used to determine whether or not it is an integer.  The COBOL
definition (all Standards - although it is clearer in the 2002 Standard) is
that this DOES define an integer - as COBOL uses the term.

Saying that  PIC S9999PP "is not an integer" is like saying that "Fr�uilein"
must be grammattically femine in German.

Find some "reference" to your (RW's) definition of "integer" in COBOL and we
may pay attention to you.  Until then, you are simply in ERROR when talking
about what an "integer" is *IN COBOL*.

FYI - For the '85 COBOL Standard, the definition (which certainly does
include PIC S9999PP) is found on page III-12

where it states,
  "Integer. A numeric literal or a numeric data item that does not include
any digit position to the right of the assumed decimal point."

Knowing that RW uses IBM has his "real world" compiler for some posts, the
definition they give is at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/BACK_3

where they state,

" integer. (1) A numeric literal that does not include any digit positions
to the right of the decimal point.
(2) A numeric data item defined in the Data Division that does not include
any digit positions to the right of the decimal point.
(3) A numeric function whose definition provides that all digits to the
right of the decimal point are zero in the returned value for any possible
evaluation of the function."

or sometimes he uses Micro Focus.  See:

 http://supportline.microfocus.com/documentation/books/nx31sp1/lrpubb.htm

and look at the Glossary where they say,

"integer
A numeric literal or a numeric data item that does not include any digit
positions to the right of the decimal point."

or if you want to use Fujitsu, look at their LRM, pageg 202 in their V7 LRM
where it states,

"d. A numeric data item that does not have digits after the decimal point is
called "integer item."  "

    ***

Bottom-Line is that the term "integer" is well defined and has a constant
meaning in COBOL references and context.  What you are talking about has
NOTHING to do with the term "integer" used in a COBOL context.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-17T10:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9e7386.307730958@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9de0f1.270200298@news.optonline.net...
…[25 more quoted lines elided]…
>about what an "integer" is *IN COBOL*.

"Whole number" is the correct descriptor for numbers with all zeros to the right
of the decimal point. Calling S9999PP an integer doesn't make it so any more
than calling a pig with a nice dress and lipstick a lady makes it into one. 

The COBOL standard took a rigorouslyl defined math term and simply used it
incorrectly. The error is not corrected by piling on 'authority'. Who gave them
authority to expropriate words from another discipline and ignorantly get the
meaning wrong? Answer: they gave themselves the authority. Most thinking people
would find that unacceptable. 



>
>FYI - For the '85 COBOL Standard, the definition (which certainly does
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-17T08:22:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7mgri$72a$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9e7386.307730958@news.optonline.net...

> The COBOL standard took a rigorouslyl defined math term and simply used it
> incorrectly. The error is not corrected by piling on 'authority'. Who gave
them
> authority to expropriate words from another discipline and ignorantly get
the
> meaning wrong? Answer: they gave themselves the authority. Most thinking
people
> would find that unacceptable.

Well, this thinking person is of the opinion that the appropriate response,
if you feel this way, is to submit a paper to J4 detailing every single
"expropriation" of any and every word from another discipline, proposing
alternative terms to be used in future standards for each such case.  Oh,
and make sure the terms you use can be automatically translated into
Tlingkit and Hill Bondo without introducing any ambiguities!  .

COBOL uses "FILE" in a manner different from how it's used by a file clerk.
Have to fix that one.  How about "SIZE" and "BLOCK"?   Everybody knows
"SIZE" has to do with dimensional measurement, and "BLOCK" is either a
cuboid toy, a measurement in urban geograpy, or a verb, right?

That COBOL defines the terms it uses, and endeavors to do so carefully and
rigorously *for use when describing the COBOL language and its behavior*
strikes me as laudable.

Once again, you seem to be throwing rotten tomatoes from the sidelines at
the people who have actually been working to build an internally-consistent
standard using carefully-designed terms for the last forty years or so.

If this "misuse" of the term "integer" offends you so deeply, fix it.
Whining is unattractive, annoying and generally unproductive behavior in an
adult.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-17T20:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9F092C.5E172E8@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com>`

```


Chuck Stevens wrote:

>
> COBOL uses "FILE" in a manner different from how it's used by a file clerk.
…[3 more quoted lines elided]…
>

Are you really sure about that one Chuck <G>. From my RAF experience, and I
certainly produced many filing systems. Maybe a DB is a little closer, but I
think the comparison between COBOL files and clerical files is still "close".

At unit level (airfield or camp) the file systems were categorized into three
major topics, Flying, Technical and Admin, the latter obviously breaking down
into Buildings, Discipline (courts martial, courts of inquiry - note that's when
we Brits spell Inquiry with an "I"),  Personnel (officers and non-coms),
accounting/payroll, medical etc....... A pre-set range of file numbers (titles)
existed for each, allowing for a breakdown into sub topics.

Let's get specific - back in Egypt at MEAF Command level, I had 'Postings - Wing
Commanders Flying". The file covered a specific set of transactions. We used to
punch hole each piece of correspondence so that it was held in place with a
string tag, two metal bars at each end.

Strictly speaking our files were SEQUENTIAL although last in was 'first on top'.
Each Enclosure was ringed with a rubber stamp, top right, and given an ascending
Enclosure Number.

Given latest enclosure said "With reference to your MEAF/1023.P2 dated
........." - the reference was ringed in red and given the cross reference to
the relevant enclosure. Linked Lists perhaps ? <G>. Something COBOL doesn't have
- Notes.
Some blank sheets of paper filed on the left of the cover, where 'Minutes" could
be written for internal use between 'viewers' without the necessity of typing an
answer/comment. (The 'minutes' were also cross-referenced to the Enclosures they
were referring to).

OK - so we didn't have ISAM.

Nor did we have a DELETE feature. Once the file became 'chunky' it was 'put on
ice' and a fresh Part 2 was opened. Sometime in the future a Court of Inquiry
was convened, (just paperwork) to 'officially' dispose of files no longer
required. There's a lovely tale on that one when I got to RAF Northolt (north of
Heathrow) back in 1955. We had recently taken ownership back from BEA.. Been
there about 18 months and our civilian cleaner said, "Sarge, come look at this
lot". He took me up into the attic where there were some 300-400 files,
Restricted, Confidential and Secret, (coloured tan, green and red). When the RAF
quit Northolt about 1945/46 they *should* have had a Court of Inquiry to dispose
of these. "Screw it !", somebody must have said, with his mind already set into
'civilian' mode  - and they chucked them up into the attic area.

Do you still want to fix the COBOL file definition <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-18T09:35:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7n6pi$579$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca>`

```
James J. Gavan wrote:


> When the RAF quit Northolt about 1945/46 they

I don't know when the RAF actually quit Northolt, if they have, but I 
recall living on base between 1956 and 1958 when my father was 2IC there.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-17T22:46:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9F3009.B4BE634A@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz>`

```


Richard Plinston wrote:

> James J. Gavan wrote:
>
…[3 more quoted lines elided]…
> recall living on base between 1956 and 1958 when my father was 2IC there.

S'amazin ! Used by Polish squadrons during WW2, (Fighter Command) - it's a
guess they moved out around 45/46 - the space being used as an extension of
the then small London airport (Heathrow). During BEA's tenure the RAF had a
maintenance unit there.

That continued up until 54/55 when BEA vacated going to Heathrow. I arrived
approx June 55 when it was already again RAF Northolt, under Transport
Command. We still had maintenance, with a couple of RCAF guys. Other than a
convenience for RAF types flying into London it was also used by Prince "X"
of the "Z" for weekend 'nooky', plus flights for the Indian High Commissioner
which we nicknamed the 'Chapati Run'. About 56/57 the AIDU (Aeronautical
Document Unit) moved in from Ruislip. The only branch of the RAF to make
money - they produced all air traffic control maps for the UK.

I left in December '59 when I went to NATO in N. Germany. So far as I know it
is still RAF 'property'. Princess Di's casket was taken from an aircraft by
an RAF Regiment guard of honour.

Plinston, Plinston ? I don't recall the name. Could it be that 'Plinston' is
a nom de plume just like 'RW' <G>. If your old man was #2 he would definitely
have known me - I worked in the HQ building.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T18:52:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304171752.759dcda1@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote

> Plinston, Plinston ? I don't recall the name. Could it be that 'Plinston' is
> a nom de plume 

No. Squadron Leader F A (Tony) Plinston.

> If your old man was #2 he would definitely
> have known me - I worked in the HQ building.

I'll ask hime.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-18T03:16:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9f5fd9.368239140@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:


>Plinston, Plinston ? I don't recall the name. Could it be that 'Plinston' is
>a nom de plume just like 'RW' <G>.

My name is real, not a nom de plume. If you want to talk to me, send email to
robert@wagner.net. I _might_ reply with a phone number.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-25T22:18:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304252118.7850a4b7@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> My name is real, not a nom de plume. 

RW >> I adopted the name of a composer 

I can see why you may have confused people on this issue. A 'Nom de
Plume' _is_ an adopted name.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-04-26T16:27:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uYBqa.5165$Zj2.1112052@news20.bellglobal.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304252118.7850a4b7@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote
>
…[5 more quoted lines elided]…
> Plume' _is_ an adopted name.

Not correct.  It is a name assumed for writing purposes only.  A name
adopted for all purposes is a complete name change, and not a nom de plume
at all.

Donald
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-26T17:51:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304261651.1e9a88b2@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote

> > I can see why you may have confused people on this issue. A 'Nom de
> > Plume' _is_ an adopted name.
> 
> Not correct.  It is a name assumed for writing purposes only.  

A 'Nom de Plume' is an adopted name for the purposes of writing only. 

A 'Nom de Plume' _is_ an adopted name (for the purposes of writing
only).

> A name adopted for all purposes is a complete name change, and not a nom de
>  plume at all.

What logic led you to inverting what I said as the basis of a
criticism.

I did not, for example, claim that 'an adopted name is a nom de
plume'.  I did not claim they were equivalent terms, but rather that
one was a subset of the other.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T14:34:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8je67$c9s$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com>`

```

On 26-Apr-2003, "Donald Tees" <Donald_Tees@sympatico.ca> wrote:

> > > My name is real, not a nom de plume.
> >
…[7 more quoted lines elided]…
> at all.

Names can't be adopted for writing purposes only?   Why not?   Does "for writing
purposes only" involve all writing?   Maybe check writing?   Or does it apply to
authors of published works?

Still, he's saying "my name is real - but it isn't really my name".   There's an
oxymoron here.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-28T17:33:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ead5c53.339617084@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 26-Apr-2003, "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
…[11 more quoted lines elided]…
>Names can't be adopted for writing purposes only?   Why not?   Does "for
writing
>purposes only" involve all writing?   Maybe check writing?   Or does it apply
to
>authors of published works?
>
>Still, he's saying "my name is real - but it isn't really my name".   There's
an
>oxymoron here.

Under US and British Common Law, one can call himself any name he wants so long
as there is no fraud involved. Additionally, he can (but is not required to)
petition a court for 'legal' acknowledgement. 

My name has been Robert Wagner since 1972.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T17:47:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jpfj$gvu$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net>`

```

On 28-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >Still, he's saying "my name is real - but it isn't really my name".   There's
> > an oxymoron here.
…[6 more quoted lines elided]…
> My name has been Robert Wagner since 1972.

In that case, Robert Wagner's really your name.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-29T03:51:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eade027.373370807@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 28-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
>> >Still, he's saying "my name is real - but it isn't really my name".
There's
>> > an oxymoron here.
>>
…[7 more quoted lines elided]…
>In that case, Robert Wagner's really your name.

It used to be Robert Quackenbush (Dutch: frogs in woods). The Marx Brothers used
"Doctor Quackenbush" in at least one movie. I trust you can appreciate why I
changed it.

My father was news anchor on the CBS affiliate in Lincoln, Nebraska, for some 25
years. He changed his name to Bud DuVal. 

In retrospect, I wish I'd chosen a French rather than German name. My temperment
is French. 

While we're on the subject of name change, I detest the idea that women, upon
marriage, should change their surname to the husband's. It makes them seem like
property, like a chattal. I've never asked a woman to do that, and would protest
if she wanted to. The whole idea is so ignoble. Only rarely do I get raised
eyebrows when I say "I'm Robert Wagner and this is my wife Marjorie (Smith)."
Unlike other posters, I regard women as human beings with intelligence the same
as men, not as sex objects, bimbos nor property.

Yes, I've known women who WANTED to be property. They're called submissives and
they wear collars Many biker babes are like that. In the right enviroment, it
doesn't take longer than a month to disabuse them of that kink.
```

###### ↳ ↳ ↳ OT: What's in a name?

_(reply depth: 27)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-04-29T17:32:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EAEFD8D.9090407@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net>`

```
Robert Wagner wrote:
> While we're on the subject of name change, I detest the idea that women, upon
> marriage, should change their surname to the husband's. It makes them seem like
…[4 more quoted lines elided]…
> as men, not as sex objects, bimbos nor property.

Some would say that rather than being a "property" thing, that it is a 
sign of her commitment to him.  She commits herself to no longer be Jane 
Smith (single girl), but to be John Doe's wife, and the lady of their 
new family.  In formal communication, her name is now Mrs. John Doe. 
It's usually far more benign that your description above.

(Plus, married folks with the same last name don't get audited as much - 
I remember reading that on a "tax tips" website somewhere...)
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 28)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-30T13:55:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8okkf$hbd$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net>`

```

On 29-Apr-2003, LX-i <DanielJSNOSPAM@Knology.net> wrote:

> Some would say that rather than being a "property" thing, that it is a
> sign of her commitment to him.  She commits herself to no longer be Jane
> Smith (single girl), but to be John Doe's wife, and the lady of their
> new family.  In formal communication, her name is now Mrs. John Doe.
> It's usually far more benign that your description above.

So what's the husband's commitment to his wife?  Shouldn't they be the same?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 29)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-30T08:43:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8oquf$2qlu$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu>`

```
A friend of mine took his wife's last name upon their marriage.

    -Chuck Stevens

"Howard Brazee" <howard@brazee.net> wrote in message
news:b8okkf$hbd$1@peabody.colorado.edu...
>
> On 29-Apr-2003, LX-i <DanielJSNOSPAM@Knology.net> wrote:
…[7 more quoted lines elided]…
> So what's the husband's commitment to his wife?  Shouldn't they be the
same?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 30)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-01T10:35:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb0eb58.572873471@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <b8oquf$2qlu$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>A friend of mine took his wife's last name upon their marriage.

If a Japanese family has girls only, when the eldest marries, the man is obliged
to take her family name. 


>"Howard Brazee" <howard@brazee.net> wrote in message
>news:b8okkf$hbd$1@peabody.colorado.edu...
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 31)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-01T07:25:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8rao8$1hpu$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <b8oquf$2qlu$1@si05.rsvl.unisys.com> <3eb0eb58.572873471@news.optonline.net>`

```
In this case, the husband was of Irish descent, the wife of Native American.

    -Chuck Stevens


"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb0eb58.572873471@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> >A friend of mine took his wife's last name upon their marriage.
>
> If a Japanese family has girls only, when the eldest marries, the man is
obliged
> to take her family name.
>
…[6 more quoted lines elided]…
> >> > Some would say that rather than being a "property" thing, that it is
a
> >> > sign of her commitment to him.  She commits herself to no longer be
Jane
> >> > Smith (single girl), but to be John Doe's wife, and the lady of their
> >> > new family.  In formal communication, her name is now Mrs. John Doe.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 29)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-02T21:37:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB32B52.9030104@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On 29-Apr-2003, LX-i <DanielJSNOSPAM@Knology.net> wrote:
> 
…[8 more quoted lines elided]…
> So what's the husband's commitment to his wife?  Shouldn't they be the same?

He gives her his word, sets up a home with her, provides for her...  A 
lot of it is tradition.  Besides, it would really be sort of silly for 
her to take his name and him to take her name - you're still not 
establishing a new family...  :)
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 30)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T14:46:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95tg2$p2a$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <3EB32B52.9030104@Knology.net>`

```

On  2-May-2003, LX-i <DanielJSNOSPAM@Knology.net> wrote:

> > So what's the husband's commitment to his wife?  Shouldn't they be the same?
>
…[3 more quoted lines elided]…
> establishing a new family...  :)

So if she sets up a home with him, provides for him...  Tradition is broken.

Why not both of them take a new name?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 31)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-05T23:42:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-99BD4A.23420305052003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <3EB32B52.9030104@Knology.net> <b95tg2$p2a$1@peabody.colorado.edu>`

```
In article <b95tg2$p2a$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:
> 
> So if she sets up a home with him, provides for him...  Tradition is broken.
> 
> Why not both of them take a new name?

When I married, I tried to convince my new wife that we should both 
change our names.  She was and Atkinson, I a Zitzelberger.  For some 
reason she did not like Atkinberger...
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 32)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-06T03:54:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB72E4C.3F381BEB@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <3EB32B52.9030104@Knology.net> <b95tg2$p2a$1@peabody.colorado.edu> <joe_zitzelberger-99BD4A.23420305052003@corp.supernews.com>`

```


Joe Zitzelberger wrote:

> In article <b95tg2$p2a$1@peabody.colorado.edu>,
>  "Howard Brazee" <howard@brazee.net> wrote:
…[7 more quoted lines elided]…
> reason she did not like Atkinberger...

Even better - the vet we go to, (for the animals not us), when he got married, his
wife became :-

        Allison Allison.

Each time I see him I ask, "How many vehicles has Allison Allison rolled over this
year ?" He just grimaces.

Jimmy
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 32)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-06T14:09:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b98fmp$6f8$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <3EB32B52.9030104@Knology.net> <b95tg2$p2a$1@peabody.colorado.edu> <joe_zitzelberger-99BD4A.23420305052003@corp.supernews.com>`

```

On  5-May-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> When I married, I tried to convince my new wife that we should both
> change our names.  She was and Atkinson, I a Zitzelberger.  For some
> reason she did not like Atkinberger...

Then you should have become Zitsons??
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 31)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-09T09:55:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBBC168.7030102@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca> <b7n6pi$579$1@aklobs.kc.net.nz> <3E9F3009.B4BE634A@shaw.ca> <3e9f5fd9.368239140@news.optonline.net> <217e491a.0304252118.7850a4b7@posting.google.com> <uYBqa.5165$Zj2.1112052@news20.bellglobal.com> <b8je67$c9s$1@peabody.colorado.edu> <3ead5c53.339617084@news.optonline.net> <b8jpfj$gvu$1@peabody.colorado.edu> <3eade027.373370807@news.optonline.net> <3EAEFD8D.9090407@Knology.net> <b8okkf$hbd$1@peabody.colorado.edu> <3EB32B52.9030104@Knology.net> <b95tg2$p2a$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  2-May-2003, LX-i <DanielJSNOSPAM@Knology.net> wrote:
> 
…[11 more quoted lines elided]…
> Why not both of them take a new name?

I know of people who have...  I was just sticking up for 
traditionalists, who don't see their spouse as property but still like 
for her to take their name as part of the commitment.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 28)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-04T06:55:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030504025552.01745.00000511@mb-m28.aol.com>`
- **References:** `<3EAEFD8D.9090407@Knology.net>`

```
Well gents - here's a female point of view....

The first time I married I took my husband's last name, had to change Social
Security records, employement records, this, that and the other thing.  I was
also attending college at that time.  When we divorced I had to legally drop
his name (a woman never looses her maiden name btw and I wasn't forced to drop
his name - my choice ) and I returned to my maiden name, and all the paper work
again.  Then I enrolled at the university for the next semester and they
demanded a copy of my divorce papers to prove the name change!  They didn't ask
for a copy of my marriage license to prove that change as I had done 2
semesters in my maiden name, the next 3 in my married name, and now back to my
maiden name.  What a zoo.

I married a second time and took his name, again all the paperwork.  This time
however I didn't enroll in the university in my married name just kept it at my
maiden name.  This time around I had children so when we divorced I kept his
name so I would match my children and avoid all the hassle that comes when a
parent doesn't have the same name as their child.

I'm married now a third time and I haven't taken his hame.  He's fine with
that.  I had figured that maybe when my youngest graduated high school (which
he has done) I'd change my name since I wouldn't have the dang beauracrates to
deal with any more.  Then my mother got sick and I discovered that all her
paperwork refers to me in my maiden name hyphen previous married name.  So much
for taking my current husband's name.  I'm not going to go through the
nightmare of explaining to everyone who the heck I am because the name on my
driver's license doesn't match the name on the paperwork.   Right now I'm
tempted to drop my previous husband's name and just keep to my maiden name for
the rest of my life.  

I should note that at all times my driver's license has had both my maiden name
and whatever married name I had at the same time.  I needed this because I have
various things in my maiden name still and needed proof of identity (what
little a DL gives you).

Now both my parents had changed their names before I was born.  My mother
married my father when he had his original last name.  When he changed that
name (and his first name) she also had to change her name otherwise she would
still be his original last name.  In doing so however she did loose her maiden
name as it was treated as a total legal name change as if she was a single
woman. (she changed her first name as well).  Instead of maiden name her
original name is now birth name. Now hows that for 'what's in a name'?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 29)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2003-05-04T04:40:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0305040340.18dbbcd7@posting.google.com>`
- **References:** `<3EAEFD8D.9090407@Knology.net> <20030504025552.01745.00000511@mb-m28.aol.com>`

```
Unbelievable, Eileen (if that really is your name <G>...I should think
by now even you are not sure <G>)

Really quite amazing, and an object lesson for people designing Civil
systems where names figure large...

Pete.



yukonmama@aol.com (YukonMama) wrote in message news:<20030504025552.01745.00000511@mb-m28.aol.com>...
> Well gents - here's a female point of view....
> 
…[39 more quoted lines elided]…
> original name is now birth name. Now hows that for 'what's in a name'?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 30)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-07T03:30:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030506233051.21533.00000944@mb-m17.aol.com>`
- **References:** `<b3638c46.0305040340.18dbbcd7@posting.google.com>`

```
>From: dashwood@enternet.co.nz  (Peter E. C. Dashwood)
>Date: 5/4/03 7:40 AM Eastern Daylight Time

>Unbelievable, Eileen (if that really is your name <G>...I should think
>by now even you are not sure <G>)

That is the one name I'm sure of <g>.  I don't have a middle name which has
caused all sorts of weird situations.  And to add to the mix while I may not be
Eileen Jones it is correct to call me Mrs John Jones <g>.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-04T23:05:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb58a2b.86270765@news.optonline.net>`
- **References:** `<3EAEFD8D.9090407@Knology.net> <20030504025552.01745.00000511@mb-m28.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote:

>Well gents - here's a female point of view....
>
…[9 more quoted lines elided]…
>maiden name.  What a zoo.

You can call yourself whatever you want, but people with whom you do business
are not required to honor the change until you produce a document which
satisfies them. 

>I married a second time and took his name, again all the paperwork.  This time
>however I didn't enroll in the university in my married name just kept it at my
…[26 more quoted lines elided]…
>original name is now birth name. Now hows that for 'what's in a name'?

Thank you for confirming what I thought -- women who marry more than once must
find name changes a major inconvenience. I like your idea of using your maiden
name for everything.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 30)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-07T03:12:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030506231252.21533.00000941@mb-m17.aol.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net>`

```
>From: robert@wagner.net  (Robert Wagner)
>Date: 5/4/03 7:05 PM Eastern Daylight Time

>You can call yourself whatever you want, but people with whom you do business
>are not required to honor the change until you produce a document which
>satisfies them. 
>

If this were true then they should have demanded a copy of my marriage license,
which they did not.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 31)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-08T08:39:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba152c.123530531@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote:

>>From: robert@wagner.net  (Robert Wagner)
>>Date: 5/4/03 7:05 PM Eastern Daylight Time
…[7 more quoted lines elided]…
>which they did not.

It does seem like a double standard. People, especially women, think marriage is
a 'good' thing to be encouraged whereas divorce is a 'bad' thing. 

I'm told that changing your name on a driver's license DOES require a marriage
license or divorce document. The college should have accepted the Department of
Motor Vehicles' authentication in both cases.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 32)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-08T09:25:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-CCA558.09245908052003@corp.supernews.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net>`

```
In article <3eba152c.123530531@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:
> 
> It does seem like a double standard. People, especially women, think marriage 
…[8 more quoted lines elided]…
> 

In my case (Georgia) the DMV grants automatic name changes to women.  
But men wishing to change their name as a result of marriage are 
required to go through the standard name change process (and fees).

The patriarchary of Georgia doing its bit to combat hypenation I 
suppose... ;-)
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 32)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-08T13:55:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sRwua.4378$vS4.532159@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
> >>You can call yourself whatever you want, but people with whom you do
business
> >>are not required to honor the change until you produce a document which
> >>satisfies them.
> >>

A rather moot point, as people with whom you do bussiness can call you
anything they want.  There is no requirement in law, as far as I know, for
anybody to ever call anybody anything.  It is all simple courtesy.

Even legal documents can be signed with anything you want, including an "X"
for the illiterate. The person that you are signing for can decide to accept
it or not, as they wish. They can set any criteria they want, including you
getting it certified by a notary, or two hundred independent witnesses.
Regardless of name.

Sometimes, Robert, I think you make statements "off-the-cuff" without even
thinking ... it seems to be a reflex re-action in an attempt to show
superiority.  That is the real reason that you get so much flack. People
sense it, and resent your attempts to put them down. You are not the only
person on the internet with the ability to think.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 33)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-09T02:03:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebaf0dd.29351397@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:


>Sometimes, Robert, I think you make statements "off-the-cuff" without even
>thinking ... it seems to be a reflex re-action in an attempt to show
>superiority.  That is the real reason that you get so much flack. People
>sense it, and resent your attempts to put them down. You are not the only
>person on the internet with the ability to think.

My intention is not to show superiority, it is to communicate useful
information. 

I've heard the same complaint in real life, in particular from a former
girlfriend with a physics degree from MIT. She said "If I wanted to be lectured,
I'd enroll in a college course. Your didactically talking to me like a student
is demeaning." I was nonplussed. At the time, I was trying to enhance her
knowledge by explaining something she obviously didn't know. 

This must be a cultural dynamic that I don't understand. When someone educates
me, I thank him/her. I don't get resentful.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 34)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-08T23:10:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305082210.531a2ce@posting.google.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> My intention is not to show superiority, it is to communicate useful
> information. 

It may well be true that is your intent.  However, when you make a
huge generalisations, explicitly or implicitly, you imply that you
have knowledge beyond what is knowable.  You take a limited view
(which is all that any of us can have) and expand it to apply to the
whole world.  Often this conflicts with our individual experiences and
views, so you become wrong.

For example you claimed that [all] IT departments are classless.  I
have been in IT departments that were rigidly hierarchical.

> I've heard the same complaint in real life, 

Then perhaps it might be true.

> in particular from a former girlfriend with a physics degree from MIT. 
> She said "If I wanted to be lectured, > I'd enroll in a college course. 
> Your didactically talking to me like a student is demeaning." 

She took the time to explain it to you, perhaps because she did care
(at the time).  From other anecdotes it seems they couldn't be
bothered explaining it, eg doctors, lawyers, computer scientists,
computer managers, sysadmins, ..

> I was nonplussed. At the time, I was trying to enhance her
> knowledge by explaining something she obviously didn't know. 

I think that I mentioned that you would never understand why you get
told ....
 
> This must be a cultural dynamic that I don't understand. When someone educates
> me, I thank him/her. I don't get resentful.

Often, you dismiss attempts to educate you by saying or implying that
you know better than the manual/standard/definition/other's
experience.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 35)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T03:12:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebc442c.116227995@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <217e491a.0305082210.531a2ce@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[8 more quoted lines elided]…
>views, so you become wrong.

In cases like that, you should rebut with your own contrary experiences. If they
are convincing enough, I'll revise (back down from) my generalizations. 

>For example you claimed that [all] IT departments are classless.  I
>have been in IT departments that were rigidly hierarchical.

I haven't. Perhaps it was an effect of British vs. US style. We could explore
that cultural difference .. rather than resorting to flammage. 

>> I've heard the same complaint in real life, 
>
>Then perhaps it might be true.

That's why I mentioned it.

>> in particular from a former girlfriend with a physics degree from MIT. 
>> She said "If I wanted to be lectured,  I'd enroll in a college course. 
…[5 more quoted lines elided]…
>computer managers, sysadmins, ..

Having given this some thought, I've concluded that aversion to 'lecturing' is
dirrectly proportion to the others' experience with 'higher education'. Those
who protest the most have been exposed to post-grad programs or unusually
difficult undergrad programs such as physics. A law degree is post-grad and
usually designated in the US as LLD. A medical doctor is, of course, a doctorial
graduate .. even though he's really just a technician. I've not seen the
aversion in people of average education. 

Why are people with advanced degrees so sensitive to 'lecturing'? I see two
possible explanations -- they see knowledge as a weapon to establish class
supremacy or they fealt humiliated when undergoing the educational process. For
lawyers and medical doctors, I would assume the former; for all others, I would
assume the latter. Programmers with advanced degrees definitely are the latter. 

>> I was nonplussed. At the time, I was trying to enhance her
>> knowledge by explaining something she obviously didn't know. 
>
>I think that I mentioned that you would never understand why you get
>told ....

Once, when I tried to teach her GUT (General Unification Theory), she went
ballistic. II was stomping in her pond. 

People are silly about defending their egos. 

>> This must be a cultural dynamic that I don't understand. When someone
educates
>> me, I thank him/her. I don't get resentful.
>
>Often, you dismiss attempts to educate you by saying or implying that
>you know better than the manual/standard/definition/other's
>experience.

Sometimes I do. For instance the question about logographs vs. alphabetic words.
Most programming dweebs know nothing about linguistics. They just adopt and
misuse the lingo, as they did with integer. 

We autodidacts are not impressed with manual/standard/definition. We're more
concerned with truth. If that makes us seem off-center .. well, that's more a
comment on the reviewer.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 36)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-11T16:26:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9hv32$bc2$1@aklobs.kc.net.nz>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <3ebaf0dd.29351397@news.optonline.net> <217e491a.0305082210.531a2ce@posting.google.com> <3ebc442c.116227995@news.optonline.net>`

```
Robert Wagner wrote:

> In cases like that, you should rebut with your own contrary experiences.
> If they are convincing enough, I'll revise (back down from) my
> generalizations.

Why do they need to be 'convincing enough' ?
 
>>For example you claimed that [all] IT departments are classless.  I
>>have been in IT departments that were rigidly hierarchical.
> 
> I haven't. 

So why can't you just accept, as most people do, that their personal 
experience is not every possible one ?

Have you ever heard the term 'know it all', it is a derogitory one, applied 
to people who don't even know enough to know they can be wrong.

> Having given this some thought, I've concluded that aversion to
> 'lecturing' is dirrectly proportion to the others' experience with 'higher
> education'. 

Or perhaps it is just that you are exposing your lack of understanding so 
much that they couldn't begin to explain where you started off wrong, even 
if it was likely that you would accept it.

> I've not seen the aversion in people of average education.

Because they are more easily bulshitted.

> Why are people with advanced degrees so sensitive to 'lecturing'? I see
> two possible explanations -- they see knowledge as a weapon to establish
…[3 more quoted lines elided]…
> definitely are the latter.

I see a completely different third alternative.

> Once, when I tried to teach her GUT (General Unification Theory), she went
> ballistic. II was stomping in her pond.

Probably because you got it wrong and were insistent that you were right in 
spite of her rebuttals and arguments.
 
> People are silly about defending their egos.

It seems that you have been doing that more so than any other I have come 
across.

> They just adopt and misuse the lingo, as they did with integer.

Once again you demonstrate that you will never understand.

> We autodidacts are not impressed with manual/standard/definition. We're
> more concerned with truth. If that makes us seem off-center .. well,
> that's more a comment on the reviewer.

Is it ?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 36)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-12T14:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9obhl$b59$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <217e491a.0305082210.531a2ce@posting.google.com> <3ebc442c.116227995@news.optonline.net>`

```

On  9-May-2003, robert@wagner.net (Robert Wagner) wrote:

> Sometimes I do. For instance the question about logographs vs. alphabetic 
> words.
> Most programming dweebs know nothing about linguistics. They just adopt and
> misuse the lingo, as they did with integer.

Here's an interesting article.  I have Word Of The Day e-mailed to me and this
came over the weekend.

http://www.yourdictionary.com/cgi-bin/wotd.cgi?word=logogram
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 36)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-12T08:33:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9oesr$k2b$1@si05.rsvl.unisys.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <217e491a.0305082210.531a2ce@posting.google.com> <3ebc442c.116227995@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ebc442c.116227995@news.optonline.net...

> >It may well be true that is your intent.  However, when you make a
> >huge generalisations, explicitly or implicitly, you imply that you
…[5 more quoted lines elided]…
> In cases like that, you should rebut with your own contrary experiences.
If they
> are convincing enough, I'll revise (back down from) my generalizations.

Been there.  Done that.  My experience is that you adjust your fundamental
premises to show how right you were.

> >For example you claimed that [all] IT departments are classless.  I
> >have been in IT departments that were rigidly hierarchical.
>
> I haven't. Perhaps it was an effect of British vs. US style. We could
explore
> that cultural difference ..

Why?  What difference does national style make in an assertion of
*universal* truth?  A single exception that meets the stated criterion
demonstrates the falsehood of the generalization.

> >I think that I mentioned that you would never understand why you get
> >told ....
…[4 more quoted lines elided]…
> People are silly about defending their egos.

A family saying:  "Never try to teach your grandmother how to milk ducks."

Another saying, not from my family:  "Never try to teach a pig to sing.  It
wastes your time and annoys the pig."

> >> This must be a cultural dynamic that I don't understand. When someone
> >> educates me, I thank him/her. I don't get resentful.
…[5 more quoted lines elided]…
> Sometimes I do. For instance the question about logographs vs. alphabetic
words.
> Most programming dweebs know nothing about linguistics. They just adopt
and
> misuse the lingo, as they did with integer.

Some, maybe.  I think I count as a programming dweeb, having entered the
field (and having never left it) in 1967.

My university degree was in linguistics with a minor in German, a second
minor in Mandarin, a couple of years in Russian (ending with senior-level
Russian literature -- as a plebe -- at the U. S. Naval Academy), two years
of high school Latin, and significant study in Old and Middle English.  That
was nigh onto forty years ago now, so I deem my knowledge of the subject a
bit on the rusty side.   There is at least one other well-respected poster
in this and similar threads in this very forum who has a similar (and
probably more extensive and more current -- several of my teachers were
well-regarded Chomsky students) background to mine.  But I do know a bit
about linguistics, in particular as it relates to English, and I don't think
I count as an autodidact on the subject.

Why would you presume otherwise?

> We autodidacts are not impressed with manual/standard/definition. We're
more
> concerned with truth.

So far, I'm not convinced of that.

> If that makes us seem off-center .. well, that's more a
> comment on the reviewer.

No.  Descriptions of English as being closer to Italian than to German, or
about the first alphabet in which a (proto-)Indo-European language was
written being the Roman alphabet, are "wrong", not "off-center".  That isn't
a comment on the reviewer; it's a demonstration that the autodidact author
might be well-served by finding out if the statements have merit before
presenting them.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 35)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T17:29:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd00b2.164496632@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <217e491a.0305082210.531a2ce@posting.google.com>`

```
[second attempt]

riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[8 more quoted lines elided]…
>views, so you become wrong.

That's why we have forii like this: to provide a reality check on our limited
experience. When enough people, more than one, have contrary experiences, that
should give us a clue our premises are invalid. We'll probably not concur on the
'right' premis, but at least we'll avoid the 'wrong' one. 

>For example you claimed that [all] IT departments are classless.  I
>have been in IT departments that were rigidly hierarchical.

I've not worked in any. I've been interviewed in a few I suspected were rigid.
Evidently their antennae were equally sensitive. <G>

>> in particular from a former girlfriend with a physics degree from MIT. 
>> She said "If I wanted to be lectured,  I'd enroll in a college course. 
…[5 more quoted lines elided]…
>computer managers, sysadmins, ..

Their big mistake is saying 'If you think you're so good, let's see you do it
better.' I LOVE that kind of invitation. <G>

>> I was nonplussed. At the time, I was trying to enhance her
>> knowledge by explaining something she obviously didn't know. 
>
>I think that I mentioned that you would never understand why you get
>told ....

Oh, I understand why. I just don't share their feelings. When someone challenges
me in an area where I have knowledge and, perhaps, emotional attachments (e.g.
COBOL), I don't feel the least bit threatened. The exchange might be educational
for one person or the other. But when it devolves to name-calling, information
exchange ceases. 

>> This must be a cultural dynamic that I don't understand. When someone
educates
>> me, I thank him/her. I don't get resentful.
>
>Often, you dismiss attempts to educate you by saying or implying that
>you know better than the manual/standard/definition/other's
>experience.

I don't ask you to take my word, I try to present a cogent argument ...  most of
the time.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 36)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-10T16:04:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305101504.d1ebf6f@posting.google.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <217e491a.0305082210.531a2ce@posting.google.com> <3ebd00b2.164496632@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >For example you claimed that [all] IT departments are classless.  I
> >have been in IT departments that were rigidly hierarchical.
> 
> I've not worked in any. I've been interviewed in a few I suspected were rigid.
> Evidently their antennae were equally sensitive. <G>

So you do agree that your vast generalisation was unfounded by your
own experience.
 
> Their big mistake is saying 'If you think you're so good, let's see you do it
> better.' I LOVE that kind of invitation. <G>

Of course there is no assurance that what you did is 'better' by their
standards, or even that you have taken into account what they would
done.

An example strings to mind where you used Realia in a shared mechanism
rather than open/close exclusive.  It isn't 'better' if you had got
index corruptions.
 
> But when it devolves to name-calling, information
> exchange ceases. 

When it _starts_ as _mis-information_ exchange (and it is not accepted
that it is _not_ information), then it may as well be name calling.

> >Often, you dismiss attempts to educate you by saying or implying that
> >you know better than the manual/standard/definition/other's
…[3 more quoted lines elided]…
> most of the time.

Yhey may be cogent, but if you just made them up then they are just
your word.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 34)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-09T13:55:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9gc0j$913$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net>`

```

On  8-May-2003, robert@wagner.net (Robert Wagner) wrote:

> I've heard the same complaint in real life, in particular from a former
> girlfriend with a physics degree from MIT. She said "If I wanted to be
…[6 more quoted lines elided]…
> me, I thank him/her. I don't get resentful.

I understand this completely.   But when I see a pattern of behavior (such as
responses to my messages), I have gradually learned to accept that that behavior
exists, regardless of whether it makes sense.   So if people don't take my
communication the way I would, I figure I need to learn to change my methods of
communication if I value communicating.  (If I don't value communicating, then I
should shut up).   Other people aren't me - and talking to them as though they
were me is not optimal.

This is/was a hard thing to learn, and I have a ways to go.

Mr. Spock was the most irrational character on Star Trek, always being surprised
when humans acted like humans.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 35)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T17:29:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd0af7.167126441@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <b9gc0j$913$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On  8-May-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[3 more quoted lines elided]…
>> I'd enroll in a college course. Your didactically talking to me like a
student
>> is demeaning." I was nonplussed. At the time, I was trying to enhance her
>> knowledge by explaining something she obviously didn't know.
>>
>> This must be a cultural dynamic that I don't understand. When someone
educates
>> me, I thank him/her. I don't get resentful.
>
>I understand this completely.   But when I see a pattern of behavior (such as
>responses to my messages), I have gradually learned to accept that that
behavior
>exists, regardless of whether it makes sense.   So if people don't take my
>communication the way I would, I figure I need to learn to change my methods of
>communication if I value communicating.  (If I don't value communicating, then
I
>should shut up).   Other people aren't me - and talking to them as though they
>were me is not optimal.
>
>This is/was a hard thing to learn, and I have a ways to go.

Your points are well taken. The talented among us use wit and erudition to cut
through communication barriers. For the rest of us, there are rules of order,
which can range from moderation to common courtesy. The unresolved problem is
what to do when someone doesn't follow the rules --- more accurately, your
interpretation of the rules --- on the anarchistic internet. Do you 'become the
enemy' by shouting back? Do you 'become the enemy' by adopting his errant
protocols? If you do either, he wins. My approach is to go an equal distance
off-center in an unexpected  direction .. in hope the resulting frustration will
bring the other back to center.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 34)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-09T09:06:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7JNua.6560$J%5.624481@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ebaf0dd.29351397@news.optonline.net...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
>
> >Sometimes, Robert, I think you make statements "off-the-cuff" without
even
> >thinking ... it seems to be a reflex re-action in an attempt to show
> >superiority.  That is the real reason that you get so much flack. People
…[7 more quoted lines elided]…
> girlfriend with a physics degree from MIT. She said "If I wanted to be
lectured,
> I'd enroll in a college course. Your didactically talking to me like a
student
> is demeaning." I was nonplussed. At the time, I was trying to enhance her
> knowledge by explaining something she obviously didn't know.
>

I am sure.  Perhaps she knew enough that  your superior knowledge was
not as obvious to her.  So far, in this forum, I have never seen you assume
that *anybody* knew as much as you, about *any* topic whatsoever. Every
post you make is to lecture somebody on their lack of knowledge, and
with at least half of them, you know less than the person that you are
lecturing. I
have never noticed you asking a question, ever. It gets tiring living as a
child
with such an infinitely wise superior being.

> This must be a cultural dynamic that I don't understand. When someone
educates
> me, I thank him/her. I don't get resentful.
>

When someone indulges in ego-babble, it is not educating me.  It is raising
the noise
level.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 35)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T17:29:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd0942.166689151@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ebaf0dd.29351397@news.optonline.net...
…[23 more quoted lines elided]…
>not as obvious to her.  

She was a physicist who unplugged electrical appliances when not in use because
(in her words) "there is still current flowing through it". Her remark was in
response to my offer to put a meter on her toaster so she could see there was no
current flowing. She "knew enough" to understand her neurosis was about to be
exposed. 

>So far, in this forum, I have never seen you assume
>that *anybody* knew as much as you, about *any* topic whatsoever. Every
…[5 more quoted lines elided]…
>with such an infinitely wise superior being.

>> This must be a cultural dynamic that I don't understand. When someone
>educates
>> me, I thank him/her. I don't get resentful.

>When someone indulges in ego-babble, it is not educating me.  It is raising
>the noise level.

How hypocritical to flame me, then in the next paragraph complain about the
noise level.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 36)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-10T15:15:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uccva.7261$J%5.777293@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3ebd0942.166689151@news.optonline.net...


> How hypocritical to flame me, then in the next paragraph complain about
the
> noise level.

You also dismiss any disagreement as a flame, yet disagree with everything
anybody else says and claim it is a well presented arguement.  If you used
the same standard for yourself as you use for everyone else, you might give
your paranoia a break.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 37)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-10T15:33:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<veGdncbXWuuR_yCjXTWJjA@giganews.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com>`

```

"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:Uccva.7261$J%5.777293@news20.bellglobal.com...
> "Robert Wagner" <robert@wagner.net> wrote in message
> news:3ebd0942.166689151@news.optonline.net...
…[8 more quoted lines elided]…
> the same standard for yourself as you use for everyone else, you might
give
> your paranoia a break.

Block annoying posters. Your blood pressure will thank you.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 38)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T22:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd7961.195397171@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
>news:Uccva.7261$J%5.777293@news20.bellglobal.com...
…[14 more quoted lines elided]…
>Block annoying posters. Your blood pressure will thank you.

I might not respond but I'd never deny them a voice. Freedom of speech is too
precious. 

In the instant case, I would have blocked Donald Tees and missed his
well-thought followup article.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 39)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-10T19:08:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9k0pg$m74$1@panix1.panix.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <3ebd7961.195397171@news.optonline.net>`

```
In article <3ebd7961.195397171@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>"JerryMouse" <nospam@bisusa.com> wrote:
>
…[16 more quoted lines elided]…
>I might not respond but I'd never deny them a voice.

Mr Wagner, blocking a poster does not deny anyone a voice, the posting 
still goes out.  Blocking a poster denies *you* the listening, just like 
turning off the radio or flipping a newspaper's page.

>Freedom of speech is too
>precious. 

Freedom of speech is 'freedom of speech', not 'the right to have those who
do not wish to listen'; this has been discussed here previously.

DD
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 38)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-10T20:28:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NOgva.12716$VJ.977132@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:veGdncbXWuuR_yCjXTWJjA@giganews.com...
>
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
…[5 more quoted lines elided]…
> > > How hypocritical to flame me, then in the next paragraph complain
about
> > the
> > > noise level.
> >
> > You also dismiss any disagreement as a flame, yet disagree with
everything
> > anybody else says and claim it is a well presented arguement.  If you
used
> > the same standard for yourself as you use for everyone else, you might
> give
…[4 more quoted lines elided]…
>
Hell, Jerry, I've been posting far too long to let my shorts get into a knot
over the odd flame.They are mildly annoying at worst, and even then mostly
from a noise perspective.  I do admit to the odd sympathetic pang for the
rebels without a clue, and horrible urges to educate, but I generally am
able to control the worst of them.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 39)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-11T02:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebdb3b4.210329807@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:


>Hell, Jerry, I've been posting far too long to let my shorts get into a knot
>over the odd flame.

Especially when self-initiated. 

> I do admit to the odd sympathetic pang for the
>rebels without a clue, and horrible urges to educate, but I generally am
>able to control the worst of them.

What about the rebel WITH a clue? Every teacher's worst nightmare is the student
who really does know more than the teacher. 

Would you like to hear anecdotes?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 40)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-11T10:38:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uftva.248$st.26649@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3ebdb3b4.210329807@news.optonline.net...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
>
> >Hell, Jerry, I've been posting far too long to let my shorts get into a
knot
> >over the odd flame.
>
…[6 more quoted lines elided]…
> What about the rebel WITH a clue? Every teacher's worst nightmare is the
student
> who really does know more than the teacher.
>
> Would you like to hear anecdotes?

No, I prefer to hear truth.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 41)_

- **From:** "Lorne Sunley" <lsunley@mb.sympatico.ca>
- **Date:** 2003-05-11T15:34:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JMPlV5b5VFnN-pn2-QIlddd21Y6dp@h24-82-204-17.wp.shawcable.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <Uftva.248$st.26649@news20.bellglobal.com>`

```
On Sun, 11 May 2003 17:38:50 UTC, "Donald Tees" 
<Donald_Tees@sympatico.ca> wrote:

> "Robert Wagner" <robert@wagner.net> wrote in message
> news:3ebdb3b4.210329807@news.optonline.net...
…[23 more quoted lines elided]…
> 

Boy, are you hanging out in the wrong place :-)
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 40)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-11T11:01:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bBtva.254$st.29000@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3ebdb3b4.210329807@news.optonline.net...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote:
>
>
> >Hell, Jerry, I've been posting far too long to let my shorts get into a
knot
> >over the odd flame.
>
…[6 more quoted lines elided]…
> What about the rebel WITH a clue? Every teacher's worst nightmare is the
student
> who really does know more than the teacher.
>

As a PS to that, Robert, perhaps you should read the above several times.
That you think it a "teacher's worst nightmare", is more indicative of your
own mind than it is about anything else.  Most of the decent teachers that I
know, and I include myself as I have trained more than one programmer, would
find it a huge delight.  It means that you can relax, and let the young ones
take over. That you see it as a threat is indicative of what I said earlier
... your psyche sees anybody that you cannot intelectually bully as a
threat.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 41)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-11T18:30:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebe8b12.265471745@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <bBtva.254$st.29000@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ebdb3b4.210329807@news.optonline.net...
…[15 more quoted lines elided]…
>> who really does know more than the teacher.

>As a PS to that, Robert, perhaps you should read the above several times.
>That you think it a "teacher's worst nightmare", is more indicative of your
>own mind than it is about anything else.  

The phrase was not my invention; I've heard it from several teachers. 

>Most of the decent teachers that I
>know, and I include myself as I have trained more than one programmer, would
…[3 more quoted lines elided]…
>threat.

We seem to made a wrong turn down Threat Street. I don't feel threatened. 

What do you expect to accomplish by putting me down? Will it make you appear
smarter by comparison? Perhaps in your own eyes, but nobody else's. If you want
to 'win' you must post _factual_ rebuttal.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 41)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-12T14:43:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9obub$bbq$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <bBtva.254$st.29000@news20.bellglobal.com>`

```

On 11-May-2003, "Donald Tees" <Donald_Tees@sympatico.ca> wrote:

> As a PS to that, Robert, perhaps you should read the above several times.
> That you think it a "teacher's worst nightmare", is more indicative of your
…[5 more quoted lines elided]…
> threat.

Especially since "knowing more" doesn't mean "knowing everything I have to
teach".   It can't.   The most knowledgeable among us still can learn from the
least knowledgeable, occasionally.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 40)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-12T14:42:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9obro$bbn$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net>`

```

On 10-May-2003, robert@wagner.net (Robert Wagner) wrote:

> What about the rebel WITH a clue? Every teacher's worst nightmare is the
> student who really does know more than the teacher.
>
> Would you like to hear anecdotes?

Such anecdotes could support that SOME teacher's don't like this.

But there are some teachers who have worse nightmares.

And some teachers like this quite a bit.   Of course Tiger Wood's coach can
still teach him some stuff - even though Tiger knows more than his teacher.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 41)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-12T11:10:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9odgp$lu9$1@panix1.panix.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <b9obro$bbn$1@peabody.colorado.edu>`

```
In article <b9obro$bbn$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 10-May-2003, robert@wagner.net (Robert Wagner) wrote:
…[8 more quoted lines elided]…
>But there are some teachers who have worse nightmares.

'Do it to Julia!  Do it to Julia!  Not me!  Julia!'... no, wait, Winston 
Smith wasn't a teacher.

DD
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 42)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-13T12:39:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec03c22_3@corp-news.newsgroups.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <b9obro$bbn$1@peabody.colorado.edu> <b9odgp$lu9$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b9odgp$lu9$1@panix1.panix.com...
> In article <b9obro$bbn$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
<snip>
> >
> >But there are some teachers who have worse nightmares.
…[3 more quoted lines elided]…
>

The Thought Police have moved on since 1984...(so has the general populace;
there are some people now who would LIKE the thought of rats chewing on
their face...fortunately (for the rest of us) most of them live in New York
City...<G>).

No, the current Thought Police are much more subtle... they infiltrate the
last bastions of Free Speech and try to disrupt them by posting boring,
tedious, provocative, inaccurate, messages ...oops,  just realised where I
am...

Pete.
(A double plus good citizen...)
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 43)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-12T21:30:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9phr2$bbb$1@panix1.panix.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <b9obro$bbn$1@peabody.colorado.edu> <b9odgp$lu9$1@panix1.panix.com> <3ec03c22_3@corp-news.newsgroups.com>`

```
In article <3ec03c22_3@corp-news.newsgroups.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b9odgp$lu9$1@panix1.panix.com...
…[13 more quoted lines elided]…
>City...<G>).

Of *course*... that's just what They want you to think!

DD
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 40)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-12T13:28:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305121228.3fc4f0ab@posting.google.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> What about the rebel WITH a clue? Every teacher's worst nightmare is the student
> who really does know more than the teacher. 

You are not trying to imply that you were dumped from school because
you knew more than the teacher are you ?  Or indeed that you are a
rebel with a clue ?

But no, their worst nightmare is a child who acts as if they know more
than the teacher and won't accept that their assertions are wrong, 
For they will not learn anything.
 
> Would you like to hear anecdotes?

No.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 41)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-13T03:02:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec04fef.31622215@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> What about the rebel WITH a clue? Every teacher's worst nightmare is the
student
>> who really does know more than the teacher. 
>
>You are not trying to imply that you were dumped from school because
>you knew more than the teacher are you ?  Or indeed that you are a
>rebel with a clue ?

I wasn't dumped, I dropped out. 

>But no, their worst nightmare is a child who acts as if they know more
>than the teacher and won't accept that their assertions are wrong, 
>For they will not learn anything.

I can understand and concur with that. 

>> Would you like to hear anecdotes?
>
>No.

I'll tell one anyway. After showing my mastery of the subject on the second day
of class, I asked the teacher what I should do for the rest of the year. He
assigned me to tutor the worst he had, a 'dumb Polock' who would likely have
failed. I did it right. I didn't do the work for him nor give him the answers, I
ELICITED them from him. In the end, he was at the top of the class. 

I think that shows unusual wisdom and leadership from a fifteen year-old.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 42)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-13T03:56:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EC06902.C54133C1@shaw.ca>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net>`

```


Robert Wagner wrote:

> riplin@Azonic.co.nz (Richard) wrote:
>
…[28 more quoted lines elided]…
> I think that shows unusual wisdom and leadership from a fifteen year-old.

Possibly *reasonably* fair comment about the fifteen year old. But Jesus would I
have been pissed off if I was the teacher !

Reminds me of arguing the toss with my twin grandsons, about 8 years old at the
time. They INSISTED the Calgary Tower was NOT the tallest building downtown, which
it was at the time. We were travelling one of the busiest roads, full of autos, the
Deerfoot, (how do you convey that in N. America - motorway or autobahn in UK or
Germany respectively). I screamed at my wife, "I'm going to toss the buggers out of
the car, but don't bother to stop !"

The fifteen year old. But now he is 60. And so many of us reading your career must
be saying to  ourselves...............?

Jimmy
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 43)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-13T14:17:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9qupm$jb1$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca>`

```

On 12-May-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> Possibly *reasonably* fair comment about the fifteen year old. But Jesus would
> I have been pissed off if I was the teacher !

More times than not, many more times than not, the know-it-all teen knows a lot
less than he thinks.   He usually will argue to death how right he is and often
drops out of school because "the teachers are ignorant".   I know of cases where
these people want to be artists but can't get the ignorant publishers and public
to buy.   Often they can't keep jobs because of their ignorant supervisors.  
Sometimes they find jobs where they are left unsupervised - and they survive for
a while.   Even professionals in fields remote from their areas of expertise are
ignorant.

There are exceptions to this stereotype, of course.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 44)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-14T07:09:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9rfv6$iqg$1@aklobs.kc.net.nz>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>> Possibly *reasonably* fair comment about the fifteen year old. But Jesus
>> would I have been pissed off if I was the teacher !
…[12 more quoted lines elided]…
> expertise are ignorant.

Do you think that somebody could be like that until they were, say, 60 ?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 44)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-13T12:25:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305131125.50c6f9f3@posting.google.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote

> More times than not, many more times than not, the know-it-all teen knows 
> a lot less than he thinks. ...

Mark Twain once said, "When I was 14 years old, my father was so
ignorant I hated to have the old man around. But when I was 21 years
old, I was astonished to see how much my father had learned in only 7
years."
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 45)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-05-14T14:27:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ngk4cvonei2ebenb3br4onajvj4gbbarvk@4ax.com>`
- **References:** `<7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu> <217e491a.0305131125.50c6f9f3@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>"Howard Brazee" <howard@brazee.net> wrote
>
…[6 more quoted lines elided]…
>years."


Whoops!  Looks like Richard beat me to the punch.........I posted my
reply before I stumbled on Richard's reply.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 46)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-14T10:39:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9tkf7$iqk$1@panix1.panix.com>`
- **References:** `<7JNua.6560$J%5.624481@news20.bellglobal.com> <b9qupm$jb1$1@peabody.colorado.edu> <217e491a.0305131125.50c6f9f3@posting.google.com> <ngk4cvonei2ebenb3br4onajvj4gbbarvk@4ax.com>`

```
In article <ngk4cvonei2ebenb3br4onajvj4gbbarvk@4ax.com>,
Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:
>riplin@Azonic.co.nz (Richard) wrote:
>
…[12 more quoted lines elided]…
>reply before I stumbled on Richard's reply.

To tie in another thread in which Yogi Berra is mentioned... this quote 
has been labelled as an 'apochryphal Twainism' by

http://www.snopes.com/quotes/twain.htm

DD
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 44)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-14T02:46:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec18751.65154779@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 12-May-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
>> Possibly *reasonably* fair comment about the fifteen year old. But Jesus
would
>> I have been pissed off if I was the teacher !
>
>More times than not, many more times than not, the know-it-all teen knows a lot
>less than he thinks.   He usually will argue to death how right he is and often
>drops out of school because "the teachers are ignorant".   I know of cases
where
>these people want to be artists but can't get the ignorant publishers and
public
>to buy.   Often they can't keep jobs because of their ignorant supervisors.  
>Sometimes they find jobs where they are left unsupervised - and they survive
for
>a while.   Even professionals in fields remote from their areas of expertise
are
>ignorant.

Everything you said is generally true. 

>There are exceptions to this stereotype, of course.  

Since the internet became widely available, some twelve years ago, I've
discovered there are many more autodidacts than I would have guessed. There are
hundreds of thousands of them in the US posessing expert level knowledge of
physics, engineering and (I'm sure) other fields. It's not bullshit or bluster,
they really know the subject .. as well as or better than authorities. 

A good friend who was an engineer at NASA Ames told me NASA used to employ them
as engineers, and they were some of the best. Hewlett-Packard did the same.  I
doubt that would happen today.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 44)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-14T04:10:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030514001025.29088.00000452@mb-m15.aol.com>`
- **References:** `<b9qupm$jb1$1@peabody.colorado.edu>`

```
>From: "Howard Brazee" howard@brazee.net 
>Date: 5/13/03 10:17 AM Eastern Daylight Time

>More times than not, many more times than not, the know-it-all teen knows a
>lot
…[11 more quoted lines elided]…
>ignorant.


I take it you've met my eldest stepson and my daughter?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 44)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-05-14T14:26:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1pj4cv4339lpa30tkh68uqa04qs7k63t9k@4ax.com>`
- **References:** `<3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 12-May-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:
…[13 more quoted lines elided]…
>There are exceptions to this stereotype, of course.  

Howard:

A quote has been attributed to Mark Twain.  I understand that the
quote has not been actually verified as having originated by Twain,
but it is one of my favorites..........with regard to "know-it-all"
teenagers.

"When I was a boy of fourteen, my father was so ignorant I could
hardly stand to have the old man around. But when I got to be
twenty-one, I was astonished at how much the old man had learned in
seven years."



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 45)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-14T15:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9tmlq$1s4$1@peabody.colorado.edu>`
- **References:** `<3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu> <1pj4cv4339lpa30tkh68uqa04qs7k63t9k@4ax.com>`

```

On 14-May-2003, Bob Wolfe <rtwolfe@flexus.com> wrote:

> A quote has been attributed to Mark Twain.  I understand that the
> quote has not been actually verified as having originated by Twain,
…[6 more quoted lines elided]…
> seven years."

I always attributed it to Twain too.  It is one of my all time favorite
observations.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 46)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-05-16T15:11:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <b9qupm$jb1$1@peabody.colorado.edu> <1pj4cv4339lpa30tkh68uqa04qs7k63t9k@4ax.com> <b9tmlq$1s4$1@peabody.colorado.edu>`

```
On Wed, 14 May 2003 15:17:14 GMT, "Howard Brazee" <howard@brazee.net>
enlightened us:

>
>On 14-May-2003, Bob Wolfe <rtwolfe@flexus.com> wrote:
…[12 more quoted lines elided]…
>observations.

It twas Twain who penned that quote.  See (at your local library if
they have it)  "Old Times on the Mississippi" Atlantic Monthly, 1874

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Next time you think you're perfect try walking on water.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 47)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-16T19:05:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba3qs4$qk5$1@panix1.panix.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <1pj4cv4339lpa30tkh68uqa04qs7k63t9k@4ax.com> <b9tmlq$1s4$1@peabody.colorado.edu> <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com>`

```
In article <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com>,
SkippyPB  <swiegand@neo.NOSPAM.rr.com> wrote:
>On Wed, 14 May 2003 15:17:14 GMT, "Howard Brazee" <howard@brazee.net>
>enlightened us:
…[18 more quoted lines elided]…
>they have it)  "Old Times on the Mississippi" Atlantic Monthly, 1874

You mean like the version OCR'd at 
http://docsouth.unc.edu/twainold/twain.html , where the word 'fourteen' 
occurs three times (and always in reference to speed) and the word 
'ignorant' twice, once in describing a watch and the other in describing 
the ship's night-watchman?

DD
```

###### ↳ ↳ ↳ OT: "When I was a boy" quote (was: OT: What's in a name?

_(reply depth: 48)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-16T19:18:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba3v4a$aol$1@slb4.atl.mindspring.net>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <1pj4cv4339lpa30tkh68uqa04qs7k63t9k@4ax.com> <b9tmlq$1s4$1@peabody.colorado.edu> <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com> <ba3qs4$qk5$1@panix1.panix.com>`

```
At:
  http://www.twainquotes.com/Father.html

It says,

 "When I was a boy of fourteen, my father was so ignorant I could hardly
stand to have the old man around. But when I got to be twenty-one, I was
astonished at how much the old man had learned in seven years.
- attributed by Reader's Digest, Sept. 1937. This quote has been attributed
to Mark Twain, but until the attribution can be verified, the quote should
not be regarded as authentic."

I found the web-page "Misattributed Quotes: What Mark Twain Didn't Say" at:
  http://www.boondocksnet.com/twaintexts/quotes_not_twain.html

fairly interesting (amusing?)
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 48)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-05-17T11:45:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i6mccvo4064r6svjvoismsbg6iec6t76ap@4ax.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <1pj4cv4339lpa30tkh68uqa04qs7k63t9k@4ax.com> <b9tmlq$1s4$1@peabody.colorado.edu> <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com> <ba3qs4$qk5$1@panix1.panix.com>`

```
On 16 May 2003 19:05:40 -0400, docdwarf@panix.com enlightened us:

>In article <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com>,
>SkippyPB  <swiegand@neo.NOSPAM.rr.com> wrote:
…[28 more quoted lines elided]…
>DD

Right magazine, wrong year.  The one UNC has OCR's is from 1875.  The
quote was published in the 1874 version.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Next time you think you're perfect try walking on water.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 49)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-17T21:52:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba6p0o$80$1@panix1.panix.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com> <ba3qs4$qk5$1@panix1.panix.com> <i6mccvo4064r6svjvoismsbg6iec6t76ap@4ax.com>`

```
In article <i6mccvo4064r6svjvoismsbg6iec6t76ap@4ax.com>,
SkippyPB  <swiegand@neo.NOSPAM.rr.com> wrote:
>On 16 May 2003 19:05:40 -0400, docdwarf@panix.com enlightened us:
>
…[33 more quoted lines elided]…
>quote was published in the 1874 version.

Interesting you should conclude this... from what I read on that page:

--begin quoted text:

This text originally appeared as a series of seven short stories in The 
Atlantic Monthly.

--end quoted text

... and then there are seven sections.  The section beginning I. shows a 
range of page numbers from 70 to 73, section II. (A "CUB" PILOT'S 
EXPERIENCE; OR, LEARNING THE RIVER.) (punctuation original) shows pages 
218 to 224, section III. (THE CONTINUED PERPLEXITIES OF "CUB" PILOTING.) 
shows 284 to 289, section IV. pages 446 to 452, etc.

It might be, then, that this series began in 1874 and ended in 1875, hence 
the difference in dates.  Do you have any citations which might lead one 
to conclude that there were two different series of the same name?

DD
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 50)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-05-18T11:37:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k19fcv0agvmgv02m5v2grh01l9lgl9731g@4ax.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <1udacvom0a20jd8jh9qv7v3di7rda7gepc@4ax.com> <ba3qs4$qk5$1@panix1.panix.com> <i6mccvo4064r6svjvoismsbg6iec6t76ap@4ax.com> <ba6p0o$80$1@panix1.panix.com>`

```
On 17 May 2003 21:52:24 -0400, docdwarf@panix.com enlightened us:

>In article <i6mccvo4064r6svjvoismsbg6iec6t76ap@4ax.com>,
>SkippyPB  <swiegand@neo.NOSPAM.rr.com> wrote:
…[56 more quoted lines elided]…
>DD

Well further research shows that possibly my source for the quote
stating it appeared in the 1874 version may have been wrong.

In June 2001 a story in the Atlantic appeared about Twain being
published in that magazine.  They were getting ready to publish a
Twain story submitted to the magazine in 1876 but was never published.
In the article it states, "Twain appeared in the magazine, followed by
many more over the next decade, including Old Times on the
Mississippi, which appeared in seven installments in 1875 and was
later released as a book under the title Life on the Mississippi."
[see complete article at:
http://www.theatlantic.com/unbound/flashbks/twain.htm ]

Another editor, Jim Zwick of BoondocksNet.com, writing about "Old
Times..." states the series appeared in The Atlantic Monthly from
January through August of 1875.

But the source I had may not be completely wrong.  Old Times was
written in pieces and submitted to William Dean Howells. Howells was,
in 1874, the assistant editor of The Atlantic Monthly.  In September
of 1874, Twain submitted to Howells a story named, "True Story".  It
was published in November of 1874 in the magazine.  Soon, Howells
asked Twain for more work like "A True Story". Twain responded with
the following pitch:

"Twichell & I have had a long walk in the woods & I got to telling him
about old Mississippi days of steamboating glory & grandeur as I saw
them (during 5 years) from the pilot house. He said "What a virgin
subject to hurl into a magazine!" . . . Would you like a series of
papers to run through 3 months or 6 or 9?--or about 4 months, say? "

The idea, possibly because of Twain's excited tone in describing it,
must have appealed to Howells, because the finished product, called
"Old Times on the Mississippi", was serialized in seven issues of The
Atlantic Monthly in 1875.

[source:  http://www.yorku.ca/twainweb/filelist/howe1.html ]

Hence I conclude that my original source,
http://www.quotegarden.com/fathers.html

was either mistaken or confused about the origin of "Old Times".

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Next time you think you're perfect try walking on water.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 51)_

- **From:** docdwarf@panix.com
- **Date:** 2003-05-18T12:51:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba8dlt$feb$1@panix1.panix.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net> <i6mccvo4064r6svjvoismsbg6iec6t76ap@4ax.com> <ba6p0o$80$1@panix1.panix.com> <k19fcv0agvmgv02m5v2grh01l9lgl9731g@4ax.com>`

```
In article <k19fcv0agvmgv02m5v2grh01l9lgl9731g@4ax.com>,
SkippyPB  <swiegand@neo.NOSPAM.rr.com> wrote:

[snip]

>Hence I conclude that my original source,
>http://www.quotegarden.com/fathers.html
>
>was either mistaken or confused about the origin of "Old Times".

... or, possibly, the attribution of the quotation to Twain altogether.

DD
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 43)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-14T02:46:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec182c5.63990265@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>Robert Wagner wrote:
>
…[3 more quoted lines elided]…
>> >

>> After showing my mastery of the subject on the second day
>> of class, I asked the teacher what I should do for the rest of the year. He
>> assigned me to tutor the worst he had, a 'dumb Polock' who would likely have
>> failed. I did it right. I didn't do the work for him nor give him the
answers, I
>> ELICITED them from him. In the end, he was at the top of the class.
>>
>> I think that shows unusual wisdom and leadership from a fifteen year-old.
>
>Possibly *reasonably* fair comment about the fifteen year old. But Jesus would
I
>have been pissed off if I was the teacher !

You have no idea. An unrelated teacher got red in the face and threw chalk,
blackboard erasers and books around the room, I thought he was going to hit me.
He ordered me out of the room even though I had 100% average on his weekly
calculus exams and the number two student (class valedictorian) had an 85%
average. 

>Reminds me of arguing the toss with my twin grandsons, about 8 years old at the
>time. They INSISTED the Calgary Tower was NOT the tallest building downtown,
which
>it was at the time. We were travelling one of the busiest roads, full of autos,
the
>Deerfoot, (how do you convey that in N. America - motorway or autobahn in UK or
>Germany respectively).

Interstate highway.

>The fifteen year old. But now he is 60. And so many of us reading your career
must
>be saying to  ourselves...............?

Please elucidate. It isn't clear what you mean by ....?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 44)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-05-14T01:13:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_LecnX8u-MlKTVyjXTWcqQ@comcast.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <veGdncbXWuuR_yCjXTWJjA@giganews.com> <NOgva.12716$VJ.977132@news20.bellglobal.com> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net> <3EC06902.C54133C1@shaw.ca> <3ec182c5.63990265@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ec182c5.63990265@news.optonline.net...
> "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[8 more quoted lines elided]…
> >> of class, I asked the teacher what I should do for the rest of the
year. He
> >> assigned me to tutor the worst he had, a 'dumb Polock' who would likely
have
> >> failed. I did it right. I didn't do the work for him nor give him the
> answers, I
> >> ELICITED them from him. In the end, he was at the top of the class.
> >>
> >> I think that shows unusual wisdom and leadership from a fifteen
year-old.
> >
> >Possibly *reasonably* fair comment about the fifteen year old. But Jesus
would
> I
> >have been pissed off if I was the teacher !
>
> You have no idea. An unrelated teacher got red in the face and threw
chalk,
> blackboard erasers and books around the room, I thought he was going to
hit me.
> He ordered me out of the room even though I had 100% average on his weekly
> calculus exams and the number two student (class valedictorian) had an 85%
> average.
>

    Reminds me of something that happened to my Nephew just this
year.  They are supposed to read a number of books, and take a
test on the computer to see if they actually read the book.

    He read a book (Harry Potter), and passed it.  But the teacher refused
to give him credit because it was above his grade level.

    Huh?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 42)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-14T18:09:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9q2a5$vcq$1@aklobs.kc.net.nz>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <3ebdb3b4.210329807@news.optonline.net> <217e491a.0305121228.3fc4f0ab@posting.google.com> <3ec04fef.31622215@news.optonline.net>`

```
Robert Wagner wrote:

>>> Would you like to hear anecdotes?
>>
>>No.
> 
> I'll tell one anyw

'Freedom of speech' allows you to post, but nothing requires me to read it.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 37)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-10T22:03:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebd76e6.194762043@news.optonline.net>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ebd0942.166689151@news.optonline.net...
…[6 more quoted lines elided]…
>anybody else says and claim it is a well presented argument. 

I don't understand the logic of this sentence. It doesn't dispute nor approve
the logic of my arguments. And it is simply incorrect about my dismissing ANY
disagreement. I thought we weren't supposed to use words like all, any and none.
Instead, we're supposed to show gentility with qualifying adjectives such as
most, the vast majority of and few. 

>If you used
>the same standard for yourself as you use for everyone else, you might give
>your paranoia a break.

Paranoia is a form of psychosis. You probably meant to say neurotic:

" a mental and emotional disorder that affects only part of the personality, is
accompanied by a less distorted perception of reality than in a psychosis, does
not result in disturbance of the use of language, and is accompanied by various
physical, physiological, and mental disturbances (as visceral symptoms,
anxieties, or phobias)" 

m-w

I don't have any visceral symptoms or phobias. I am a tad anxious about finding
the next COBOL project, but that's based on reality. The world is ever so slowly
replacing COBOL with the language de jour.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 38)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-10T21:02:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nihva.12730$VJ.979747@news20.bellglobal.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <3eba152c.123530531@news.optonline.net> <sRwua.4378$vS4.532159@news20.bellglobal.com> <3ebaf0dd.29351397@news.optonline.net> <7JNua.6560$J%5.624481@news20.bellglobal.com> <3ebd0942.166689151@news.optonline.net> <Uccva.7261$J%5.777293@news20.bellglobal.com> <3ebd76e6.194762043@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message

> Paranoia is a form of psychosis. You probably meant to say neurotic:
>

What I probably meant to say is "pompous ass", but seeing as how you are
incapable of understanding subtilety, perhaps you can tell me what I really
mean.

Donald
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 36)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-11T05:34:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030511013417.29266.00000117@mb-m15.aol.com>`
- **References:** `<3ebd0942.166689151@news.optonline.net>`

```
>From: robert@wagner.net  (Robert Wagner)
>Date: 5/10/03 1:29 PM Eastern Daylight Time
>

>She was a physicist who unplugged electrical appliances when not in use
>because
…[6 more quoted lines elided]…
>

I'm surprised she didn't toss that toaster into the bathtub with you.  What you
should have done is keep your mouth shut, shrug and get on with life.  Perhaps
she unpluged a TV one afternoon and it threw her across the room at the age of
12.  Things like this do leave a lasting impression on a person (it sure did
me).
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 31)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-08T11:31:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uB6dnTVfrZbYGyejXTWJkg@giganews.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com>`

```

"YukonMama" <yukonmama@aol.com> wrote in message
news:20030506231252.21533.00000941@mb-m17.aol.com...
> >From: robert@wagner.net  (Robert Wagner)
> >Date: 5/4/03 7:05 PM Eastern Daylight Time
>
> >You can call yourself whatever you want, but people with whom you do
business
> >are not required to honor the change until you produce a document which
> >satisfies them.
> >
>
> If this were true then they should have demanded a copy of my marriage
license,
> which they did not.

What about the appellation of the form: "Suzie Jones-Smith." Here, a woman
has chosen to identify herself in terms of TWO men.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 32)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-08T16:53:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9e231$429$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <uB6dnTVfrZbYGyejXTWJkg@giganews.com>`

```

On  8-May-2003, "JerryMouse" <nospam@bisusa.com> wrote:

> What about the appellation of the form: "Suzie Jones-Smith." Here, a woman
> has chosen to identify herself in terms of TWO men.

Not necessarily.   Chances are one name was hers all her life, and her mothers
for longer than her life.   Origins before that really don't matter (is she
identifying herself by some ancestor's job as a smith?).

Or maybe she choose to add her "real" mother's name to her birth/biological
mother's name - honoring the person who raised her, but keeping some history.

(some people have a different idea on who is her "real" mother than I do).
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 32)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-05-08T20:36:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bdzua.10611$%_3.5857200@newssrv26.news.prodigy.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <uB6dnTVfrZbYGyejXTWJkg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:uB6dnTVfrZbYGyejXTWJkg@giganews.com...
> What about the appellation of the form: "Suzie Jones-Smith." Here, a woman
> has chosen to identify herself in terms of TWO men.


I never liked those hyphenated dual names.

Seems to me one should defecate or relinquish control of the porcelain
throne.

MCM
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 33)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-08T20:39:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9efas$9fr$1@peabody.colorado.edu>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <uB6dnTVfrZbYGyejXTWJkg@giganews.com> <Bdzua.10611$%_3.5857200@newssrv26.news.prodigy.com>`

```

On  8-May-2003, "Michael Mattias" <michael.mattias@gte.net> wrote:

> > What about the appellation of the form: "Suzie Jones-Smith." Here, a woman
> > has chosen to identify herself in terms of TWO men.
…[5 more quoted lines elided]…
> throne.

Of course one can say the same thing about having a surname at all.   Only in
that case, it is established by tradition that we belong to the husband's family
(there is a fascinating town in China where families are matriarchal without
marriage).   Our surname is the brand we use in identifying whose family we are
associated with.

To get away from this we have some choices:
1.   Reject the surname altogether.  Either pick a new surname or have none.
2.  Accept male and female surnames together  (hyphenation).
3.  Roll a die.

I do know a couple with an adopted daughter.  All three have different surnames.

I also know every single Brazee-Cannon within 2 parsecs of trolly #7.
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 34)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-08T21:18:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-9D5151.21181408052003@corp.supernews.com>`
- **References:** `<3eb58a2b.86270765@news.optonline.net> <20030506231252.21533.00000941@mb-m17.aol.com> <uB6dnTVfrZbYGyejXTWJkg@giganews.com> <Bdzua.10611$%_3.5857200@newssrv26.news.prodigy.com> <b9efas$9fr$1@peabody.colorado.edu>`

```
In article <b9efas$9fr$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:
> 
> To get away from this we have some choices:
…[7 more quoted lines elided]…
> I also know every single Brazee-Cannon within 2 parsecs of trolly #7.

Or even option 4.

We could design a Globally Unique Personality Identifier (GUPI) by 
taking all know data about a person and hashing it into a 128-byte hex 
string.

To make it relavent to this ng, we would write the system in Cobol...
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 29)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-05T03:38:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB5D91A.549064F4@shaw.ca>`
- **References:** `<3EAEFD8D.9090407@Knology.net> <20030504025552.01745.00000511@mb-m28.aol.com>`

```


YukonMama wrote:

> Well gents - here's a female point of view....
>

<snip> Talk about convoluted - why not just change your name to Eileen WAGNER Still
seeing as you've been around the block several times, perhaps Pete's got it right -
you should stick with YukonMama <G>

Jimmy
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 29)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T14:48:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95tkn$p2i$1@peabody.colorado.edu>`
- **References:** `<3EAEFD8D.9090407@Knology.net> <20030504025552.01745.00000511@mb-m28.aol.com>`

```

On  4-May-2003, yukonmama@aol.com (YukonMama) wrote:

> When we divorced I had to legally drop
> his name (a woman never looses her maiden name btw and I wasn't forced to drop
> his name - my choice ) and I returned to my maiden name, and all the paper
> work again.

Why?   Was this some local law that forced you to do this?   (Certainly it is
not universal).


> This time around I had children so when we divorced I kept his
> name so I would match my children and avoid all the hassle that comes when a
> parent doesn't have the same name as their child.

Did you move or did the law change so that this time you didn't need to drop his
name?
```

###### ↳ ↳ ↳ Re: OT: What's in a name?

_(reply depth: 30)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-07T03:18:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030506231849.21533.00000942@mb-m17.aol.com>`
- **References:** `<b95tkn$p2i$1@peabody.colorado.edu>`

```
>From: "Howard Brazee" howard@brazee.net 
>Date: 5/5/03 10:48 AM Eastern Daylight Time

>
>Why?   Was this some local law that forced you to do this?   (Certainly it is
>not universal).
>

It was my choice to drop his name, I didn't have to.  I had no children and
nothing in this particular name that I needed to continue using it.  Of course
it put me at the front of the alphabet (started with 'A') but otherwise of no
value to keep it.

>
>Did you move or did the law change so that this time you didn't need to drop
>his
>name?
>

It is much much easier dealing with the beauracracy when you don't have to keep
correcting someone as to your name when they call about a sick child and say
'Mrs Smith your child is sick' and you have to say 'It's Mrs Jones now - and
yes Jimmy Smith is my son'.  Nobody questions your signature and so on and so
on.  And it especially helps when your ex remarries and there is another woman
with his last name.  Had I changed my name then they would automatically assume
she was the parent - as almost happened once anyway. Again - it was my choice.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-17T15:46:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7nasv$pl6$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com> <3E9F092C.5E172E8@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3E9F092C.5E172E8@shaw.ca...

> Are you really sure about that one Chuck <G>. From my RAF experience, and
I
> certainly produced many filing systems. Maybe a DB is a little closer, but
I
> think the comparison between COBOL files and clerical files is still
"close".

There are parallels and there are differences.  "I need that file" in an
E-mail (or remember speed-o-letters?) could have at least four separate and
relatively disparate meanings to a person sitting at a desk, depending on
what's on the desk:  a folder containing papers (or other stuff), a floppy
disk, a baggie containing some powdered young sassafrass leaves intended for
cooking (popular in Louisiana!), and an implement used to remove rough edges
from one's fingernails.   ;-)

The third of these is pronounced differently, but it's spelt the same ...

Since every word can have one, and only one, definition, which one's right:
that of the paperwork shuffler, the person with a computer, the cook or the
manicurist?   ;-)

I won't even get into the verbs ...     ;-)

Whereas a "file" in traditional computing usually can be considered as
containing a number of records with *similar* data in *similar or identical*
formats for different subjects, a "file" in the traditional paper sense
contains a number of records of *different* data in *different* formats
associated with a *given* subject.   A computer *file* is really more like a
*file cabinet*, I think.

I don't think there's anything wrong with the COBOL file definition, by the
way (or the integer definition).  Unless you insist that when writing "FILE
SECTION" in a COBOL program you're actually talking about a repository for
powdered sassafrass leaves in your program, and not what the COBOL standards
define "FILE", any combined term using "FILE", or any description using
"FILE" to be, and even then, it's on you, not on COBOL.     ;-)

I'm reminded of a number of discussions with somebody who I think should
have known better who insisted that all computer implementations that
produced anything other than 2 when adding 1 to 1.345987112348, regardless
of the precision of the destination, were clearly wrong.   Until the advent
of "standard arithmetic", I *think* this was ambiguous in the standard
(which left most such matters to the implementor), and some actually did
such things.  I think the intent of the original implementors of COBOL was
made abundantly clear in the 2002 standard in the provisions of "standard
arithmetic":  every operand in a calculation or an arithmetic expression is
treated as if it were contained in a Standard Intermediate Data Item, a
floating-point item with an exponent of three digits and a mantissa
precision of 32 decimal digits, with a magnitude range from (10 ** -999) to
((10 ** 1000) - (10 ** 968) inclusive.  Thus, in standard arithmetic the sum
in question is treated as if it were the sum of 1.0000000...E0 and
1.345987112348000000...E0, and any presumption on the part of a
mathematician that the result should be exactly 2 is explicitly contradicted
by the rules of the language.     In other words, one may want the result to
be 2.  One might whine and scream and kick until one's blue in the face that
the result ought to be 2.  But, given COBOL's careful definitions, it ain't.

COBOL defines "integer" for the specific context of describing COBOL
behavior.  Whether the lexicon of COBOL disagrees with any other definition
is as irrelevant as whether "burro" means the same thing in Spanish and
Italian, or whether "bicho" is a bad word or not (in Venezuela it has about
the force of "thingamajig" in American English; it's not a word one would
use in polite company in Cuba, according to my Venezuelan relatives).  Have
you knocked up any of your neighbo[u]rs lately?   ;-)

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:37:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea09e3f.9974743@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mgri$72a$1@si05.rsvl.unisys.com>`

```
In general, COBOL uses integer correctly. My complaint is the type returned by
function date-of-integer. It's very name seems to acknowledge that dates are not
integers. 

The error doesn't offend me "deeply"; it's relatively minor. And since COBOL
doesn't have strong type checking, I can receive into X(8), just as I now ACCEPT
X(6) FROM DATE.


"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9e7386.307730958@news.optonline.net...
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-17T10:55:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7mipr$mq3$1@slb1.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net>`

```
Robert,
   You are WRONG.

COBOL defines the terms used in its specification.  For example, the '85
Standard calls the reserved word "IF" a "verb".

That doesn't mean that it meets the definition of "verbs" *OUTSIDE* of
COBOL - but it does mean that it is a "verb" in COBOL.

Now, of course, as others have pointed out - you are mistaken in your belief
of what the term "integer" means OUTSIDE of COBOL. You have not provided any
evidence that your "opinion" of what the term means in "math" or "computers"
or anywhere actually MEANS what you think it does.  OTOH, that is irrelevant
in CLC - when compared to the fact that you simply don't understand that
COBOL is a "language" and as such defines its own terms - and these
definitions are what should be used when talking about COBOL.

This is similar to your arguments on INITIALIZE.  Making statements about
what *YOU* think the existing language should be "like" - doesn't provide
any useful input to anyone.  It is especially confusing when you don't seem
to understand those parts of the COBOL language that are well defined and
constantly implemented by all standard-conforming vendors.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:37:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0ab80.13368410@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <b7mipr$mq3$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Robert,
>   You are WRONG.
…[13 more quoted lines elided]…
>definitions are what should be used when talking about COBOL.

How can I be wrong when the COBOL standard does not define integer? The closest
it comes to a definition is the one you pointed out:

"When the term 'integer' is used as a constraint for an operand in a syntax
rule, then .. if that operand is a data-name or an identifier, it shall
reference one of the following:

b) a fixed-point numeric data item ... whose description does not include any
digit positions to the right of the radix point."

Ok. Numeric data item is well defined, but what is the definition of fixed-point
data item? 

There isn't one. Nowhere is fixed-point nor fixed-point data item defined. 



--------- history follows -------------
>This is similar to your arguments on INITIALIZE.  Making statements about
>what *YOU* think the existing language should be "like" - doesn't provide
…[123 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T13:48:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304171248.173b403e@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> >In Cobol I can have a field PIC S9999PP which can contain an integer
> >> >in a range that _does_ have gaps.
…[3 more quoted lines elided]…
> >PIC S9999PP
 
> "Whole number" is the correct descriptor for numbers with all zeros to the 
> right of the decimal point. 

"""Whole number.

Numbers ..., -3, -2, -1, 0, 1, 2, 3, ... are said to be integers,
numbers 0, 1, 2, 3, 4, ... are called whole numbers, numbers 1, 2, 3,
... are the counting numbers (cardinals).""""

"Whole numbers" (nor integers nor cardinals nor ordinals)
_do_not_have_ a decimal point, and thus 'all zeros to the right' is
nonsense.

> Calling S9999PP an integer doesn't make it ...

I want you to listen very carefully to this.  Read it twice:

  S9999PP is a _picture_ defining a _field_ that can _contain_ an
interger.

  The field defined is an 'integer field', or variable.

  S9999PP is not 'an integer', it defines where an integer can be
stored.

You consistently confuse the container and the content.

The word 'interger' is often used as an adjective to qualify
containers such as 'variable', 'field', 'word'.  When you drop the
noun you confuse yourself into thinking that 'integer' is being used
as a noun in that case.

Hence you get confused by the subtleties of the language.

> The COBOL standard took a rigorouslyl defined math term and simply used it
> incorrectly. The error is not corrected by piling on 'authority'. Who gave them
> authority to expropriate words from another discipline and ignorantly get the
> meaning wrong? Answer: they gave themselves the authority. 

Cobol defines a language, one that is not English.  They define it for
the benefit of Cobol programmers, and take their authority from them. 
If you don't like it then stop calling yourself a Cobol programmer.

> Most thinking people would find that unacceptable. 

You calim that Cobol standards 'gave themselves authority', and them
immediately 'give yourself the authority to talk on behalf of 'most
thinking people'.

But it is not the standard, nor the rest of the world, that define
integer wrongly, it is only you who fails to understand what these
terms mean.

Now if you could come up with some evidence that ordinals can be
negative, or whole number have a decimal point and zeroes, or an
integer is a range, or any of the other grade school mistakes you have
made then we may stop thinking that you are just making it up as you
go along and actually will see the source of your mistakes.

Otherwise we will simply conclude you are doing this as flame bait.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** "JC" <Kaos_Theory99@hotmail.com>
- **Date:** 2003-04-17T20:59:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7n4ka$qt7$1@sparta.btinternet.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <217e491a.0304171248.173b403e@posting.google.com>`

```
Richard <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304171248.173b403e@posting.google.com...
>
> Otherwise we will simply conclude you are doing this as flame bait.
>
You two should get a room for night
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-18T03:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9f6328.369086087@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net> <217e491a.0304171248.173b403e@posting.google.com> <b7n4ka$qt7$1@sparta.btinternet.com>`

```
"JC" <Kaos_Theory99@hotmail.com> wrote:

>Richard <riplin@Azonic.co.nz> wrote in message
>news:217e491a.0304171248.173b403e@posting.google.com...
…[3 more quoted lines elided]…
>You two should get a room for [the] night

Sorry, I'm straight.
```

###### ↳ ↳ ↳ Re: Integer - RW's error (was: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:56:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b810q5$p3$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7ktr1$bgp$1@slb4.atl.mindspring.net> <3e9e7386.307730958@news.optonline.net>`

```

On 17-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> The COBOL standard took a rigorouslyl defined math term and simply used it
> incorrectly. The error is not corrected by piling on 'authority'. Who gave
> them
> authority to expropriate words from another discipline and ignorantly get the
> meaning wrong? Answer: they gave themselves the authority.

That happens.

> Most thinking people would find that unacceptable.

If CoBOL is a unacceptable for that reason, there are other languages available.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T01:23:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304170023.389e60a6@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> They make silly statements such as
> "Simple numbers are divided into two groups: integer and real.  If it is a 
> number then it is either an integer or a real number." which fails to apprehend
> the fact that integers are all real numbers.

While it may be true that there are real numbers that have the same
value as the integers it is convenient to separate these values by
representation. 1 is an integer 1.0 is a real number with the same
value.  There is no exclusion.

> Your statement derives from two
> data types provided by programming languages: fixed point and floating point.

Actually 'fixed point' does not indicate integer. Real numbers may be
fixed point or floating point.  Integers are 'no point'.

> In fact, the two kinds of numbers are real and complex,

You may note that I excluded complex.

> You didn't learn that terminology because most
> programming languages don't support complex numbers. 

Did I _not_ learn this ?  How strange because I distinctly remeber
learning complex numbers, and using them, when I used Fortran in the
60s.

> Applying the wrong name to something doesn't make it so. For instance, calling 
> a date an integer doesn't make it an integer, it only makes it misrepresented.  

A number of the form 20030415 is an integer.  Your not knowing this is
irrelevant to the facts.

> Nonsense. Ordinal means a member of an ordered set (more on this when get to
> dates). An ordinal number is a member of an ordered set containing exclusively
> numbers. They can be positive or negative. 

"""In common usage, an ordinal number is an adjective which describes
the numerical position of an object, e.g., first, second, third,
etc."""

So how do you say 'two places before the first' ?

"""The ordinals for finite sets are denoted 0, 1, 2, 3, ..., i.e., the
integers one less than the corresponding nonnegative integers."""

What part of 'nonnegative' do you fail to understand ?

> 'Tiny' is an 8-bit integer in some implementations.

Can you name one ?

> You are technically correct, 

Only 'technically' ?

> but I've not seen a C compiler which used int for anything but 16-bit 
> short int. 

What a very restricted world you have been in.

> Changing it to 32-bit would 'break' many programs. 

It _isn't_ a change, the only thing required for C is:

      short <= int <= long

They can _all_ be 32 bit or 64bit or ...

If your program break because of the size of int then they are very
poorly written, even if their beauty makes you cry again, I judge
programs by how well they work - and don't break.

> This is analogous to COBOL's BINARY or (vendor extension) unsuffixed COMP. It
> can mean whatever you want it to mean. That sounds good in the conference
> room, but hardly supports portability. 

Don't you _ever_ read manuals ?  Until you do you will continue to
make these silly mistakes.  While COMP-x is whatever _the_vendor_ (not
me) wants it to be, BINARY is clearly defined in the '85 standard, it
therefore _does_ support portability.

> That's what I said in the passages you snipped. If integer is defined as 16
> bits, as it is in C, 

You are really not following this at all well.  

   C does not define what 'an integer' _is_.
   C only defines that type 'int' use the machines 'integer' type.
   C does _not_ define the size of 'int'

> then it is defined by the range +-32K. If the definition is
> generic, its range (cardinality) is defined by the data type. 

You are still confusing the container and the content. A '16bit
integer variable' (or type, field, register) may define the range, but
this is not the definition of 'integer'.

Note the qualifier: variable, field, type, etc.

Just because you leave words off in a casual way does not entitle you
to redefine what computer languages use for their definitions.

> >In Cobol I can have a field PIC S9999PP which can contain an integer
> >in a range that _does_ have gaps.
> 
> In that case, it's not an integer. 

Yes it is.  There is _no_ definition, _none_ that specifies 'no gaps'.
 That is entirely an invension that attempt to apply because it suits
your argument.

> >As is usual you start with some unfounded conclusion that you asserted
> >and then just make stuff up to attempt to support this.
> 
> When reason flags, resort to ad hominem. 

No. You really do just make stuff up. It's not 'ad hominen' if its
true.

You started with '20030415 is not an integer' and then made up the
requirement for 'no gaps'.  42, 177, 8745643 are integers.  20030415
is an integer.

> Integers are both cardinal (in the computer) and ordinal. You've been so badly
> miseducated, your statements make no sense. 

No. Wrong.  Ordinals are integers, cardinals are integers.  The
reverse (what you said) is not true.  Integers may be negative. 
Cardinals and Ordinals are nonegative integers.

When you finally grasp this significant issue then you will remain
undereducated.

 >Which is quite irrelevant because dates represented as 20030415 are
>not cardinals.

> Out of curiosity, what do you think cardinal means? I defined it as range and
> used OCCURS as an example. Evidently you are working from another (faulty)
> definition.

In what way do you think 20030415 represents a 'range' ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-17T08:27:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7mh56$746$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304170023.389e60a6@posting.google.com...

> Don't you _ever_ read manuals ?  Until you do you will continue to
> make these silly mistakes.  While COMP-x is whatever _the_vendor_ (not
> me) wants it to be, BINARY is clearly defined in the '85 standard, it
> therefore _does_ support portability.

The behavior of BINARY is defined just about as well as that of
COMPUTATIONAL and PACKED-DECIMAL and (elementary numeric) DISPLAY  in the
'85 standard; however, the format and "edge case" (e.g. SIZE ERROR) behavior
is largely up to the implementor.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-17T11:09:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7mjj0$cgd$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <b7mh56$746$1@si05.rsvl.unisys.com>`

```
I agree that BINARY and PACKED-DECIMAL have about the "same" status in the
Standard, but I think they are "significantly" better defined (more
poratable) than COMPUTATIONAL.

Compare GR(4) and GR(6) on page 363 of the 2002 Standard - which state,

"4) The USAGE BINARY clause specifies that a radix of 2 is used to represent
a numeric item in the storage of the computer. Each implementor specifies
the precise effect of the USAGE BINARY clause upon the alignment and
representation of the data item in the storage of the computer, including
the representation of any algebraic sign. Sufficient computer storage shall
be allocated by the implementor to contain the maximum range of values
implied by the associated decimal picture character-string."

    versus

"6) The USAGE COMPUTATIONAL clause specifies that a radix and format
specified by the implementor is used to represent a numeric item in the
storage of the computer. Each implementor specifies the precise effect of
the USAGE COMPUTATIONAL clause upon the alignment and representation of the
data item in the storage of the computer, including the representation of
any algebraic sign, and upon the range of values that the data item may
hold."
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-17T09:35:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ml4u$aan$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <b7mh56$746$1@si05.rsvl.unisys.com> <b7mjj0$cgd$1@slb6.atl.mindspring.net>`

```
Good point, Bill.  In our '85 implementation, COMPUTATIONAL and
PACKED-DECIMAL are identical (and in our '74 implementation, COMPUTATIONAL
is the same even though that dialect doesn't have PACKED-DECIMAL).  I think
that's what led me to lump them all together in my head as relates to
rigorousness.  The '02 standard as you cite it defines that USAGE
COMPUTATIONAL exists, but doesn't tell the implementor much more about it
than that the items must represent numbers.

About the only thing the '74 standard says about COMPUTATIONAL is that an
item so described is capable of representing a value used in computations
and must be numeric, but leaves the rest up to the implementor.  Yes, I
think I would have rather it made clear that whatever VALUE was stored in a
COMP item had to be numeric, but it didn't, it said that the ITEM is treated
as a numeric item regardless of what it contains, as I read it.

    -Chuck Stevens

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b7mjj0$cgd$1@slb6.atl.mindspring.net...
> I agree that BINARY and PACKED-DECIMAL have about the "same" status in the
> Standard, but I think they are "significantly" better defined (more
…[4 more quoted lines elided]…
> "4) The USAGE BINARY clause specifies that a radix of 2 is used to
represent
> a numeric item in the storage of the computer. Each implementor specifies
> the precise effect of the USAGE BINARY clause upon the alignment and
> representation of the data item in the storage of the computer, including
> the representation of any algebraic sign. Sufficient computer storage
shall
> be allocated by the implementor to contain the maximum range of values
> implied by the associated decimal picture character-string."
…[6 more quoted lines elided]…
> the USAGE COMPUTATIONAL clause upon the alignment and representation of
the
> data item in the storage of the computer, including the representation of
> any algebraic sign, and upon the range of values that the data item may
…[17 more quoted lines elided]…
> > COMPUTATIONAL and PACKED-DECIMAL and (elementary numeric) DISPLAY  in
the
> > '85 standard; however, the format and "edge case" (e.g. SIZE ERROR)
> behavior
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T14:05:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304171305.6d4a2a16@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote 

> A number of the form 20030415 is an integer.  

> > Applying the wrong name to something doesn't make it so. For instance, calling 
> > a date an integer doesn't make it an integer, it only makes it misrepresented.  

I'll try and make this as simple as possible.

    A number of the form 20030415 is an integer

    This interger may be _interpreted_ as a date by breaking it into
    3 component parts (each of which are ordinals).

It is obviously too subtle for you.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-18T02:02:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9f4d01.363414286@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote

>> Your statement derives from two
>> data types provided by programming languages: fixed point and floating point.
>
>Actually 'fixed point' does not indicate integer. Real numbers may be
>fixed point or floating point.  Integers are 'no point'.

For what it's worth, use of 'integer' for fixed point is the reason why I didn't
know picture V could be used on BINARY. I equate machine registers with
integers, and COMP-5/BINARY with machine registers. I could see picture P used
as a scaling factor but never thought of picture V used as such. 

>> In fact, the two kinds of numbers are real and complex,
>
…[7 more quoted lines elided]…
>60s.

The C++ standard library has class.complex, which calls its components REAL and
imaginary. Here the word real has a different definition than in languages which
use it to mean floating point .. refreshingly, a mathematically correct
definition.

>> Applying the wrong name to something doesn't make it so. For instance,
calling 
>> a date an integer doesn't make it an integer, it only makes it
misrepresented.  
>
>A number of the form 20030415 is an integer.  Your not knowing this is
…[3 more quoted lines elided]…
>> dates). An ordinal number is a member of an ordered set containing
exclusively
>> numbers. They can be positive or negative. 
>
…[4 more quoted lines elided]…
>So how do you say 'two places before the first' ?

You don't; negative subscripts are invalid. But negative numbers can be members
of an ordered set, which makes them ordinals. 

Note that the definition is qualified with "in common usage". 

>"""The ordinals for finite sets are denoted 0, 1, 2, 3, ..., i.e., the
>integers one less than the corresponding nonnegative integers."""
>
>What part of 'nonnegative' do you fail to understand ?

The author is confusing ordinal with enumeration. 
>
>> 'Tiny' is an 8-bit integer in some implementations.
>
>Can you name one ?

Any C/C++ compiler with a typedef to char, if not already provided. Did you want
me to say Python?

>> You are technically correct, 
>
…[5 more quoted lines elided]…
>What a very restricted world you have been in.

That's because your broadly enlightened world neglects to cite specific
compilers in rebuttal. 
>
>> Changing it to 32-bit would 'break' many programs. 
…[9 more quoted lines elided]…
>programs by how well they work - and don't break.

I didn't say my programs would break. They wouldn't. But many poorly written
programs would. Surely you know the software landscape is filled with crap code.
Compiler writers are held hostage by it because they fear any change that breaks
'working' code will be a black mark against them. 

>> This is analogous to COBOL's BINARY or (vendor extension) unsuffixed COMP. It
>> can mean whatever you want it to mean. That sounds good in the conference
>> room, but hardly supports portability. 

>Don't you _ever_ read manuals ?  Until you do you will continue to
>make these silly mistakes.  While COMP-x is whatever _the_vendor_ (not
>me) wants it to be, BINARY is clearly defined in the '85 standard, it
>therefore _does_ support portability.

Yeahbut, nobody uses BINARY because it's too slow (on many impementations), and
because it requires 'too much typing' .. two more keystrokes than COMP. The
standards committee would have had a winner if they's gone with BIN.

>> That's what I said in the passages you snipped. If integer is defined as 16
>> bits, as it is in C, 
…[12 more quoted lines elided]…
>this is not the definition of 'integer'.

A set member is defined by the definition of the set it belongs to. This is a
key concept; don't brush it aside. 

>Note the qualifier: variable, field, type, etc.

>> >In Cobol I can have a field PIC S9999PP which can contain an integer
>> >in a range that _does_ have gaps.
…[5 more quoted lines elided]…
>your argument.

There certainly is. I'll find and post them tomorrow, which is a legal holiday
in the US (Good Friday, which is a good reason to know how to compute Easter).
>
>> >As is usual you start with some unfounded conclusion that you asserted
…[5 more quoted lines elided]…
>true.

That depends on your definition of 'make this stuff up'. It originates in my
logic, as opposed to looking it up in a Web site or book; but it's based on
corrigible evidence such as real-world experience with compilers and knowledge
of math fundamentals. 

I speak with my own voice rather than parroting reference material. It's riskier
.. I've sometimes been wrong .. but it also holds the promise of illuminating
truth. Those who look everything up are limited to the vision of their sources. 

>You started with '20030415 is not an integer' and then made up the
>requirement for 'no gaps'.  42, 177, 8745643 are integers.  20030415
>is an integer.

20030331 is an integer only if I can add 1 and get a meaningful result. That's
why I said "you can't add 1 to a date", which no one seemed to understand. 

>> Integers are both cardinal (in the computer) and ordinal. You've been so
badly
>> miseducated, your statements make no sense. 
>
>No. Wrong.  Ordinals are integers, cardinals are integers.  The
>reverse (what you said) is not true.  Integers may be negative. 
>Cardinals and Ordinals are nonegative integers.

The site you referenced had a correct definition of cardinal. If you'll click on
it, you'll find that cardinal is the size of a set, just as I said when I gave
the example OCCURS 12. 

As for ordinal, see above. Many set members can be ordinals, not just numbers.
For instance, the letters of the alphabet .. and dates in the form yyyymmdd. 

>> Out of curiosity, what do you think cardinal means? I defined it as range and
>> used OCCURS as an example. Evidently you are working from another (faulty)
>> definition.
>
>In what way do you think 20030415 represents a 'range' ?

You avoided the question. I'm curious about computer programming 'math
terminology'.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T23:11:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304172211.266de4d4@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> The C++ standard library has class.complex, which calls its components REAL and
> imaginary. Here the word real has a different definition than in languages which
> use it to mean floating point .. refreshingly, a mathematically correct
> definition.

Is this something else that you had to make up with no guidence from
actual definitions ?

A complex number has two parts: a real number and an imaginary number.
 The Real number is exactly the same as non-complex real numbers.  The
need for an imaginary part is because there is no real value for the
square root of -1.

There is _no_ difference between a 'real number in a complex' and a
'real number'.  The difference between a real and a complex is the
imaginary part.

The above is mathemtaics.

'Floating point' is one way to _represent_ a subset of real numbers. 
In a complex number it is usual to use two 'floating point' fields,
one to represent the real number and the other represents a real
number giving the value of the imaginary number which must be
implicity multiplied by the sqrt of -1.

'Fixed point' is _another_ way to represent a sub-set of real numbers.

The numbers are 'real numbers', the term 'floating point' is the name
of one way of representing real numbers (eg 0.56784212 E+5).  This
representation is not directly related to computers and has been used
since well before computers.

You are probably confused, yet again, because computer storage for
real numbers may be called 'float' (C/C++) or 'real' (Algol, FORTRAN,
Pascal).  These are _containers_ and have a floating point
_representation_ for the real number they hold (or approximate).

Take one real number:   3.14159..

This may be held approximately using a floating point representation
as 0.314159 E+1 in a COMP-1 (MF) or a C 'float' or a Pascal 'real'.

Or it may be held approximately as a fixed point:  PIC S9V99999 VALUE
3.14159.

Computer languages only need to define the representation they will
use to store real numbers or complex numbers, they do not define what
a 'real number' is.
This is exactly the same problem you have with integers.  Computer
languages do not define what an integer _is_, they only define how
integers can be represented.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T06:30:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0dac6.25472246@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> The C++ standard library has class.complex, which calls its components REAL
and
>> imaginary. Here the word real has a different definition than in languages
which
>> use it to mean floating point .. refreshingly, a mathematically correct
>> definition.
>
>Is this something else that you had to make up with no guidence from
>actual definitions ?

Yep, I just made it up. There's no class.complex. They do it with COMP-2, 'as
god intended'.

>A complex number has two parts: a real number and an imaginary number.
> The Real number is exactly the same as non-complex real numbers.  The
>need for an imaginary part is because there is no real value for the
>square root of -1.

No, not exactly the same. In languages such as Pascal, real ALWAYS means
floating point. In languages which support complex, the real portion MAY be
fixed-point. 

>The above is mathemtaics.

Whoops, I should have read ahead. 

>Computer languages only need to define the representation they will
>use to store real numbers or complex numbers, they do not define what
…[3 more quoted lines elided]…
>integers can be represented.

That's exactly my point to WMK. COBOL doesn't define what an integer _is_, only
that it should be stored in a "fixed-point numeric data item", which turns out
to be undefined. By failing to define integer, the standard is implicitly
incorporating definitions from other disciplines, specifically mathematics. Yet
when I bring up the math definition, you and WMK brush it aside as irrelevant.

You can't have it both ways.  Either define the word or comply with the math
definition, which says a date expressed as 20030331 is NOT an integer.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-28T09:58:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jmkh$27j6$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ea0dac6.25472246@news.optonline.net...

> That's exactly my point to WMK. COBOL doesn't define what an integer _is_,
only
> that it should be stored in a "fixed-point numeric data item", which turns
out
> to be undefined. By failing to define integer, the standard is implicitly
> incorporating definitions from other disciplines, specifically
mathematics. Yet
> when I bring up the math definition, you and WMK brush it aside as
irrelevant.
>
> You can't have it both ways.  Either define the word or comply with the
math
> definition, which says a date expressed as 20030331 is NOT an integer.

Just out of curiosity, from where, and from which standard, do you get the
assertion that the only general definition of "integer" is something that
"should be stored in a fixed-point numeric data item"?

While I agree that COBOL doesn't define what an integer is in any context
other than that of the COBOL language, the framers of the standard for COBOL
have gone to great lengths to provide a definition of the term "integer" as
it applies to the specific context of COBOL, and have also made clear that
whatever the term might mean in any context other than COBOL, it means
nothing more and nothing less than what that definition specifies *in the
context of the COBOL language*.   They could have called it a "blivet" or a
"whoozis" instead, had they chosen, but I believe "integer" in this context
is much clearer.

Here are some definitions of "integer" (along with salient introductory
material) from COBOL standards:

ANSI X3.23-1974 page I-52, 4.1, GLOSSARY, introduction:

    The terms in this chapter are defined in accordance with their meaning
as used in this document describing COBOL and may not have the same meaning
in other languages.
    These definitions are also intended to be either reference material or
introductory material to be reviewed prior to reading the detailed language
specifications that follow. ...

ANSI X3.23-1974 page I-60, entry for _Integer_:

    A numeric literal or a numeric data item that does not include any
character positions to the right of the assumed decimal point.  ...

ANSI X3.23-1985 page III-1, Section III: GLOSSARY, introduction:

    The terms in this section are defined in accordance with their meaning
in COBOL, and may or may not have the same meaning for other languages.
    These definitions are also intended as either reference or introductory
material to be reviewed prior to reading the detailed language
specifications that follow. ...

ANSI X3.23-1985 page III-12, Section III, GLOSSARY, paragraph 2,
Definitions, entry for _Integer_:

    A numeric literal or a numeric data item that does not include any digit
positions to the right of the assumed decimal point.  ...

ISO/IEC 1989:2002 page 20, section 5, Description techniques, paragraph 5.4,
Integer operands:
1)  When the term 'integer-n' (n = 1, 2, ...) is used in a general format
and associated rules, it refers to a fixed-point integer literal that shall
be unsigned and non-zero unless otherwise specified in the associated rules.

2)  When the term 'integer' is used as a constraint for an operand in a
syntax rule, then
  a)  if that operand is a loiteral, it shall be an integer literal, as
defined in 8.3.1.2.2.1, Fixed-point numeric literals;
  b)  if that operand is a data-name or an identifier, it shall reference
one of the following:
        1.  an integer intrinsic function
        2.  a fixed-point numeric data item, other than an intrinsic
function, whose description does not include any digit positions to the
right of the radix point.

3) When the term 'integer' is used as a constraint for an operand in a
general rule, the operand shall evaluate at runtime as follows:
  a)  If native arithmetic is in effect, the implementor shall define when
the operand is an integer.
  b)  If standard arithmetic is in effect, the operand shall be equal to a
standard intermediate data item that has the unique value zero or whose
decimal fixed-point representation contains only zeroes to the right of the
decimal point.
    NOTES:
      1.  If the value of the exponent is greater than 31, the value of the
standard intermediate data item is an integer.
      2.  If the value of the exponent is less than 1 then the value of the
standard intermediate data item is not an integer.
  c)  If native arithmetic is in effect, the implementor shall define when
an arithmetic expression is an integer.

Note that the framers of the 2002 standard have moved away from a policy of
providing short definitions for technical terms *in a glossary*, and toward
a policy of establishing more complete and more rigorous definitions for
those terms in more meaningful context, to which the primary entry in the
index refers.  Such a policy was applied, and is in evidence, in ISO/IEC
1989:2002 for the term "integer"; the first index entry "in general formats
and rules" points to Page 20 where the term is defined for all instances in
which it is used in that context.

While other languages (including that of mathematics) may choose to define
the term "integer" differently from the above, these are the formal
definitions of the term that apply to COBOL.  Nothing in these definitions
requires that Z(n) + 1 = Z(n+1).  20030331 is an integer, regardless of how
it is interpreted.  20030401 is also an integer, regardless of how it is
interpreted.  The relationship between 20030331 and 20030401 is an
application question, not a language question.

You issued the challenge:  "Either define the word or comply with the math
definition, which says that a date expressed as 200303031 is NOT an
integer".  The COBOL standards answered this demand very nearly thirty years
ago by defining the word "integer" as it was to be understood in the context
of the COBOL language.

       -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-28T14:28:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304281328.38e47ed5@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote 

> > You can't have it both ways.  Either define the word or comply with the
>  math
> > definition, which says a date expressed as 20030331 is NOT an integer.

>     A numeric literal or a numeric data item that does not include any
> character positions to the right of the assumed decimal point.  ...

This particular definition is one used by maths, and has been since
way before any 'set theory'.  This has also been pointed out to RW who
choose to ignore this as it shows the whole basis of his tirade is
completely flawed and groundless.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-28T16:39:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8k734$3om$1@slb1.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <217e491a.0304281328.38e47ed5@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304281328.38e47ed5@posting.google.com...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote
>
> > > You can't have it both ways.  Either define the word or comply with
the
> >  math
> > > definition, which says a date expressed as 20030331 is NOT an integer.
…[7 more quoted lines elided]…
> completely flawed and groundless.

and so we don't get another repeat of his erroneous reasoning,

It is true that in EVERY definition (that *I* know of) the "set of all
integerS" is defined such that for every integer "X", that the arithmetic
expression "X + 1" yields *another* integer.  This, however, never (other
than in RW's view that I have seen - certainly not in the references he
provided) support a claim that any set of "numbers" for which the statement

  If "X" is a member of the set, then "X + 1" is also a member of the set
    is not true,

that it means that such a set does NOT include only "integer" members.

Furthermore, the fact that the COBOL definition (in the 2002 Standard) of
"what an  integer is" refers to "fixed point numeric data items" which are
not explicitly defined, does NOT mean that the existing definition is not
valid, unless the "common usage" of the term "fixed-point numeric data item"
is unclear or unusable in this context.

    ***

Bottom-Line (yet again):
   The definition of "integer" in all contexts (COBOL or math or general
usage) is clear and consistent - and has nothing to do with whether or not
the usage of the specific item type allows one to "add 1" to yield another
valid member of the same type.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-29T14:13:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8m1ag$qu0$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <217e491a.0304281328.38e47ed5@posting.google.com> <b8k734$3om$1@slb1.atl.mindspring.net>`

```

On 28-Apr-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> It is true that in EVERY definition (that *I* know of) the "set of all
> integerS" is defined such that for every integer "X", that the arithmetic
…[7 more quoted lines elided]…
> that it means that such a set does NOT include only "integer" members.

If it did, then there is no set of even integers.   I could call this a subset,
but I have been told that subsets don't exist in math.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-29T03:51:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eadbca2.364276112@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ea0dac6.25472246@news.optonline.net...
…[17 more quoted lines elided]…
>"should be stored in a fixed-point numeric data item"?

The 2002 standard. 

>Here are some definitions of "integer" (along with salient introductory
>material) from COBOL standards:

[quotes from earlier standards regretably snipped in order to get to the point]

>ISO/IEC 1989:2002 page 20, section 5, Description techniques, paragraph 5.4,
>Integer operands:
…[5 more quoted lines elided]…
>syntax rule, then

>  b)  if that operand is a data-name or an identifier, it shall reference
>one of the following:
…[3 more quoted lines elided]…
>right of the radix point.

This defines integer as a FIXED-POINT numeric data item. But 'fixed-point' is
nowhere defined in the standard. Thus, the definition fails internally within
the standard. 

>You issued the challenge:  "Either define the word or comply with the math
>definition, which says that a date expressed as 20030331 is NOT an
>integer".  The COBOL standards answered this demand very nearly thirty years
>ago by defining the word "integer" as it was to be understood in the context
>of the COBOL language.

Writers of the standard tried to careful to distinguish the container from its
contents. The container is a 'numeric data item', meaning a field containing
only numbers. The standard uses the word integer when talking about contents --
numeric literals and operands.  The intent of the flawed definition is that
integer operands may contain ANY natural number. Some (techies) have incorrectly
concluded that this means integer and numeric data item are synonymous .. that
any number is both an integer and can be stored in a numeric data item. If that
were true, the authors would have called them numbers rather than integers. 

Granted, a function which can accept all natural numbers as input can process
pic s999PPP, so I won't quibble about whether that data item is an integer
operand or not. But the function integer-of-date CANNOT process 20030332. It
cannot process integer operands, only date operands. 

The solution, in my opinion, is:

1.  Define fixed-point. A no-brainer.
2.  Leave the definition of integer intact. 
3.  Change the definition of integer-of-date to use an operand 'numeric data
item' While you're at it, change accept ... from date and accept ... from time
similarly. 

[I breeched my 'no more integer debate' because Chuck Stevens has been silent
for a month. Let's not reopen the thread, please.]
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-28T23:55:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8l0jn$f59$1@slb0.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net>`

```
Mr. Wagner  - I won't go thru this again.

You are wrong about integers in the 2002 Standard.  You are wrong on how
definitions work in this Standard (or elsewhere). You are wrong about
"containers" versus "contents" in the COBOL Standard.

Please go eat some meat (after reviewing all the already provided
explanations of your errors) and come back when you can accept when you have
made an error and it has been pointed out to you with explanations.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-29T09:55:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8m096$emq$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea0dac6.25472246@news.optonline.net> <3eadbca2.364276112@news.optonline.net>`

```
In article <3eadbca2.364276112@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:

[snip]

>[I breeched my 'no more integer debate' because Chuck Stevens has been silent
>for a month. Let's not reopen the thread, please.]

Hmmmmmm... smells like 'one rule for me, a different one for others' 
again.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-29T08:38:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8m69e$utm$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eadbca2.364276112@news.optonline.net...
>
> >ISO/IEC 1989:2002 page 20, section 5, Description techniques, paragraph
5.4,
> >Integer operands:

<some snippage>

> >2)  When the term 'integer' is used as a constraint for an operand in a
> >syntax rule, then
…[8 more quoted lines elided]…
> This defines integer as a FIXED-POINT numeric data item.

No, it defines it as a subset of fixed-point numeric data items,
specifically as distinguished from floating-point numeric data items (USAGE
FLOAT-SHORT, FLOAT-LONG and FLOAT-EXTENDED), fixed-point numeric literals,
fixed-point numeric-edited data items, floating-point numeric-edited data
items and floating-point numeric literals.  Numeric data items that are not
floating-point are fixed-point.  Fixed-point numeric data items are not
necessarily integer data items, but integer data items are always
fixed-point numeric data items so far as I know.   Note that a
floating-point data item that evaluates to an integer (e.g., a
FLOAT-EXTENDED containing exactly the value +1.0E010) does not qualify as an
integer data item or a fixed-point numeric data item in the above-cited rule
because the DESCRIPTION of the data item allows digits to the right of the
radix point, whether there are any non-zero ones in the contents or not.

> But 'fixed-point' is
> nowhere defined in the standard. Thus, the definition fails internally
within
> the standard.

No, I don't think it does, any more than "floating-point numeric data item"
fails because "floating-point" is not expressly defined.

While you're looking at the standard, take a peek at the bibliography on
page 836.  The lead-in paragraph states "The following documents are useful
references for implementors and users of this International Standard, in
addition to normative references."

The second entry in this bibliography is a standard American English
dictionary, I think it can be presumed that for any terms whose definitions
are *not* explicitly stated in the standard but *are* found in that
reference, the latter can be considered an adequate guide to understanding
what the term means in the context of the standard, for anybody who finds
the term confusing to begin with.  That's one major reason  the authors of
the standard included a standard, readily-available American English
dictionary among the references.  .

I don't happen to have a copy of Webster's Tenth Collegiate handy, but I do
have a Ninth, and my experience is that the definitions for these terms
probably haven't changed much.  That dictionary has this to say:

Fixed-point:  ... involving or being a mathematical notation (as in a
decimal system) in which the point separating whole numbers and fractions is
fixed -- compare FLOATING-POINT

Floating-point:  ... involving or being a mathematical notation in which a
quantity is denoted by one number multiplied by a power of the number base
... -- compare FIXED-POINT.

Thus, anyone who is incapable of understanding at a glance what any given
term not expressly defined in the standard (for example, "fixed-point" and
how it relates to "floating-point")  is expressly guided *by the standard*
toward a generally-accepted reference work that contains sufficient
information to clarify the question.   Terms used, but not expressly
defined, within the standard can generally be presumed to be used in ways
consistent with their *standard* dictionary definitions.

(Personally, I would have preferred that the standard's bibliography cite
the Third Unabridged on the grounds that I believe it's the closest thing we
have to a "definitive" dictionary of American English.  Because it's not as
readily available and because the Collegiate series is frequently found in
offices, I compromised on the latest Collegiate, which like all
Merriam-Webster dictionaries is based on the Unabridged anyway. )

> Writers of the standard tried to careful to distinguish the container from
its
> contents. The container is a 'numeric data item', meaning a field
containing
> only numbers. The standard uses the word integer when talking about
contents --
> numeric literals and operands.

No, that's not true.  A data item with digit POSITIONS to the right of the
decimal point, regardless of its contents, is not an integer when the syntax
or general rules require it to be an integer.  It's the *description* of the
data item that counts, unless the "local" rules override it.  You yourself
cited the rule; see above.

> The intent of the flawed definition is that
> integer operands may contain ANY natural number. Some (techies) have
incorrectly
> concluded that this means integer and numeric data item are synonymous ..

Well, aside from "flawed definition", I'm pretty much OK so far ...

> that any number is both an integer and can be stored in a numeric data
item.

Uhh ... no ... I don't think that's the assertion that's been made.  An
integer value can typically be stored in any numeric data item that has
enough whole number digit positions in its description to contain the value.
Integer data items form a proper subset of fixed-point numeric data items,
in my view.

> If that
> were true, the authors would have called them numbers rather than
integers.

If pigs had wings, they could fly.  If we had some ham, we could have some
ham and eggs, if we had some eggs.  Who knows what they would have done?

> Granted, a function which can accept all natural numbers as input can
process
> pic s999PPP, so I won't quibble about whether that data item is an integer
> operand or not. But the function integer-of-date CANNOT process 20030332.
It
> cannot process integer operands, only date operands.

Yes, it can indeed process such a value.  What I would expect it to do is
recognize that the INTEGER it was passed does not REPRESENT a valid date,
and raise the EC-ARGUMENT-FUNCTION exception.

 > The solution, in my opinion, is:
>
> 1.  Define fixed-point. A no-brainer.

If it's a no-brainer, why define it?  The standard already directs the user
to a standard dictionary in which he can expect to find definitions for
standard terms.  Like fixed-point.

> 2.  Leave the definition of integer intact.

I agree with that one.

> 3.  Change the definition of integer-of-date to use an operand 'numeric
data
> item'

Why expand the description of this function to allow numbers with fractional
digits as well as floating-point values along with integers?   I don't see
this change to the existing functionality as having a particular
"value-add".

> While you're at it, change accept ... from date and accept ... from time
> similarly.

The date and time ACCEPTs already allow non-integer destinations; however,
the result of a FRACTION-PART function using the destination as an argument
should unconditionally be zero.  Are you saying that you will personally
guarantee that NO existing program anywhere in the world would be
deleteriously affected by your suggested change in what the
currently-well-defined results of the chronological variants of ACCEPT
produce, and are willing and able, out of your own pocket, to indemnify the
worldwide COBOL community to that effect?

> [I breeched my 'no more integer debate' because Chuck Stevens has been
silent
> for a month. Let's not reopen the thread, please.]

(Just out of curiosity, how do you go about breeching a debate?)

I was out of town all last week.  Not that "a month" could be in any way
considered an exaggeration, but my system-provided submission log indicate
that there was a gap in my submissions to this forum of a few hours shy of
ten calendar days (from about 1PM on Friday 18 April until about 10AM on
Monday 28 April).

There is new information in the above response, and that new information is
that the standard explicitly suggests the use of an American English
dictionary when attempting to understand terms not expressly defined in the
standard.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-29T14:14:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304291314.73bebff1@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote

> The second entry in this bibliography is a standard American English
> dictionary, I think it can be presumed that for any terms whose definitions
…[5 more quoted lines elided]…
> dictionary among the references.  .

There must be hundreds or possibly thousands of words that are used in
the text of the standard that are not defined within it.  One must
rely on the reader having some understanding of what common words
mean.

> > 3.  Change the definition of integer-of-date to use an operand 'numeric
>  data
…[5 more quoted lines elided]…
> "value-add".

I suspect that part of the problem is that RW doesn't use the words
'number' and 'integer' in the same way that the rest of us do, and as
found in the dictionaries you mention.

He doesn't seem to notice that 'fixed-point' allows digits after a
decimal point and that 'number' refers to any number.  He reserves the
term 'integer' for some special purpose, such as being part of set Z. 
He wants to call 20030415 a 'number' because he doesn't want it to be
in _his_  definition of an 'integer'.

He seems not to want to have decimal digits, but just doesn't realise
that that is the implication of changing to 'number'.

In other words he wants to change from 'integer' to 'number without a
decimal part'.
 
> > While you're at it, change accept ... from date and accept ... from time
> > similarly.
…[8 more quoted lines elided]…
> worldwide COBOL community to that effect?

I don't think that he realises that it would be a change of
functionality.  He actually only wants to change the terminology, not
whether there is a fractional part or not.  Presumably he thinks that
this will make him 'right'.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-30T17:20:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb005b3.514075751@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>"Chuck Stevens" <charles.stevens@unisys.com> wrote
>
…[12 more quoted lines elided]…
>mean.

Funny, I had exactly the same thought yesterday. Then the answer came to me.
When people are presented with something claiming to be authoritative and free
of error, our natural human reaction is look for errors. It doesn't matter if we
have to pick nits to find them. I likened the situation to medical doctors, who
all too often project an attitude of perfection. When talking to one, I have on
occasion used medical terminology, their weapon of choice. Big mistake. Their
authority had been questioned. They visibly stiffen and turn UP the obfuscation
level. 

Once, when talking to a lawyer, I cited cases which chearly proved he was wrong.
He got red in the face, stood up behind his desk and shouted, "IF YOU KNOW SO
DAMNED MUCH, WHY DON'T YOU DRAW THE DOCUMENTS YOURSELF?" (I did, and saved the
client several hundred thousand over the lawyer's solution.) <g>

My point is: the standard projects an air of being definitive and exhaustive.

>> > 3.  Change the definition of integer-of-date to use an operand 'numeric
>>  data
…[9 more quoted lines elided]…
>found in the dictionaries you mention.

No, my definition was just sloppy. I meant to say 'numeric data item containing
a valid date as a whole number'. Wait, that doesn't allow literals. Since the
standard has already defined 'integer' for just this purpose -- whole number
operands, and that's not going to change, I'd be happy with "integer containing
a valid date". 

>He doesn't seem to notice that 'fixed-point' allows digits after a
>decimal point and that 'number' refers to any number.  He reserves the
>term 'integer' for some special purpose, such as being part of set Z. 
>He wants to call 20030415 a 'number' because he doesn't want it to be
>in _his_  definition of an 'integer'.

A fair summation, except it's not _my_ definition.

>He seems not to want to have decimal digits, but just doesn't realise
>that that is the implication of changing to 'number'.

>In other words he wants to change from 'integer' to 'number without a
>decimal part'.

Whole number is shorter.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-30T13:44:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8pcig$65k$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net>`

```
I noticed an interesting contrast in wording:

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb005b3.514075751@news.optonline.net...

> When people are presented with something claiming to be authoritative and
free
> of error, our natural human reaction is look for errors.  ...

While the COBOL standard is intended to be authoritative -- by its authors
in INCITS/J4 and by ISO/IEC, and I suspect by all those national standards
bodies that voted for its adoption -- it does not claim to be free of
errors.  Moreover, there is a defect handling process for the new standard
already in place, and several defect reports have already been filed.  The
fact that J4 and WG4 continue to meet and discuss defect reports is
indicative of a willingness to correct errors, which itself acknowledges the
possibility that errors might exist.  My personal opinion is that *no* human
endeavor is free of error.

> My point is: the standard projects an air of being definitive and
exhaustive.

Much of the *style* of the standard (like the use of "shall" in syntax
rules, which in that context indicates a requirement, not a sense of future
requirement, ability or plan) is dictated to the authors by ISO/IEC.  See
Reference 1 in the bibliography.   (In this instance, Reference 2 in the
bibliography does include this present-tense regulatory intent of "shall" in
the context of laws, regulations or directives as a possibility, but it is
in that context a "formal" usage that disagrees with the more common
"future" semantics of the word).

As to "exhaustiveness", well, it tries to cover as much as it can cover.
I'm not sure what your point is in that respect.

Have you been presented with a document that *claims* to be both
authoritative and free from errors?   The authoritativeness of the document
is a result of international agreement and treaty that it be authoritative,
not through its claim that it is authoritative.  And I am unaware of any
claim either within the document or otherwise that it is free from errors
(of omission or of comission).  So I believe the answer to my question is
"no, you haven't."

If the document *projects* an air of definitiveness:  well, yeah ... would
you rather, for example, that syntax rule 1 of DISPLAY read something like
"It'd probably be a good idea if identifier-1 didn't reference a pointer or
an object" rather than "Identifier-1 shall not reference a data item of
class object or class pointer."?  Isn't the point of a standard to be
defnitive?   As to exhaustiveness, I'm not sure how the document "projects"
an air of exhaustiveness, except through its sheer size and complexity; it
does indeed try to "cover all the bases".  Would you rather it didn't?

<<No, my definition was just sloppy. I meant to say 'numeric data item
containing
a valid date as a whole number'. Wait, that doesn't allow literals. Since
the
standard has already defined 'integer' for just this purpose -- whole number
operands, and that's not going to change, I'd be happy with "integer
containing
a valid date". >>

"Containing" is an execution-time determination.  While the '85 standards
don't provide much for exceptions being raised by functions, the '02
standard does provide for them -- in this case, the raising of
EC-ARGUMENT-FUNCTION -- and I would expect such an exception here if the
contents of the integer argument were not as specified for the function.
If the compiler *can* determine (as in the case of a literal argument to
integer-of-date) that an exception condition will unconditionally be raised
during such a call (as, for example, "FUNCTION INTEGER-OF-DATE
(12345678)" ), and does indeed make that determination, the implementor is
not required to produce executable code (either for the function reference
or for the program as a whole).  It seems to me that the '02 standard
already provides what you want.  Why do you think it is necessary to change
it?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Defects, Dates, Arguments, Exceptions, etc (was: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-30T16:16:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8pega$jup$1@slb2.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net> <b8pcig$65k$1@si05.rsvl.unisys.com>`

```
Just wanted to add a couple things to Chuck's excellent reply.

1) As far a "defect reports" go, I posted a note a few weeks ago on how
ANYONE may submit such a report.  Use GOOGLE or equivalent to find my note
with the subject:

  "Reporting defects in the ANSI/ISO COBOL Standards"

dated March19th.

2) As far as validating dates/integers in functions (and elsehwere), besides
the EC-ARGUMENT-FUNCTION mentioned by Chuck below, the 2002 Standard adds
the following intrinsic functions that meet these and/or similar needs:

 - TEST-DATE-YYYYMMDD
 - TEST-DAY-YYYYDDD
 - TEST-NUMVAL
 - TEST-NUMVAL-C
 - TEST-NUMVAL-F

See the 2002 Standard for the exact features and functionality of these new
intrinsic functions.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-30T16:37:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304301537.4fc1d813@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> When people are presented with something claiming to be authoritative and free
> of error, our natural human reaction is look for errors. 

Where is the claim to 'free of error' ?

It seems to me that (based on previous comments that you have made)
you want to be able to criticise the J4 committee for not writing the
language spec that you would like.

> It doesn't matter if we have to pick nits to find them. 

> I likened the situation to medical doctors, who
> all too often project an attitude of perfection. When talking to one, I have on
> occasion used medical terminology, their weapon of choice. Big mistake. Their
> authority had been questioned. They visibly stiffen and turn UP the
> obfuscation level. 

Perhaps, as here, you used it in a completely incorrect way and
appeared to be an upstart talking way beyond their knowledge.  Of
course if you contrive to demonstrate that you know the jargon then
they may assume you can use it.

> Once, when talking to a lawyer, I cited cases which chearly proved he was wrong.
> He got red in the face, stood up behind his desk and shouted, "IF YOU KNOW SO
> DAMNED MUCH, WHY DON'T YOU DRAW THE DOCUMENTS YOURSELF?" (I did, and saved the
> client several hundred thousand over the lawyer's solution.) <g>

Yes, I had mentioned that you would _never_ understand why people just
told you to fuck off.  The Doctor probably was telling you that too,
but in terms that you wouldn't understand.

Just because you saved the Lawyer's fees doesn't mean you saved
thousands, you may have made a mistake or missed a step and left the
client with a potential liability.  You wouldn't know whether that was
true or not.

> My point is: the standard projects an air of being definitive and exhaustive.

It is, for the purposes of implementing a Cobol compiler or writing a
program.

> >I suspect that part of the problem is that RW doesn't use the words
> >'number' and 'integer' in the same way that the rest of us do, and as
…[7 more quoted lines elided]…
> containing a valid date". 

Well Duhh |  That is _exactly_ what the standard states:

      ".. integer of the form YYYYMMDD whose value is .."

> A fair summation, except it's not _my_ definition.

Well, yes it is.  The common definition of an integer is a number
without a fractional or decimal part.

You rely on what some forms of Set Theory _uses_ to define "The Set of
All Integers" and then invert this (as no one else does) to claim that
this defines what "An Integer" is. If it were true that what you use
is the _definition_ of an integer then it would be entirely a circular
definition:

           Z is the set of all integers
           an integer is a member of the set Z

As this is untenable we (that is everyone except you) recognises that
the definition of 'integer' is found elsewhere.  Such as "A number
with no fractional or decimal part".

> >He seems not to want to have decimal digits, but just doesn't realise
> >that that is the implication of changing to 'number'.
…[4 more quoted lines elided]…
> Whole number is shorter.

And integer is shorter and more precise (for rational definitions of
integer).

'Whole number' is often a synonym for integer but may be used to mean
only 'non-negative integer', but is primarily a casual term for
cardinality.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T17:42:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb3e417.80393848@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net> <217e491a.0304301537.4fc1d813@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>It seems to me that (based on previous comments that you have made)
>you want to be able to criticise the J4 committee for not writing the
>language spec that you would like.

My comments are not directed at the J4 committee; they are directed at a
programming culture which adopts technical words from other cultures, mostly
math and logic, and misuses them. It gets the meaning almost right but not
quite. This is irritating because the reasan WHY the words were invented was to
give them definitions more precise than common usage. 

Every field has jargon that was created to facilitate accurate communication.
Doctor, lawyers or plumbers would be offended if laymen redefined their
professional argot by using the terms casually.

>> I likened the situation to medical doctors, who
>> all too often project an attitude of perfection. When talking to one, I have
on
>> occasion used medical terminology, their weapon of choice. Big mistake. Their
>> authority had been questioned. They visibly stiffen and turn UP the
…[3 more quoted lines elided]…
>appeared to be an upstart talking way beyond their knowledge. 

I do that frequently. Ultracrepidarian: One who tries to work outside his field
of knowledge, where he has no business being. <G>

If I'd used the word incorrectly, it would have been easy to make me look
foolish. 

I've represented myself in court ("pro se") a few times. Judges and lawyers hate
that. The first thing that happens is the judge throws me a 'trick' or unusually
difficult question. If I can't answer, he says the equivalent of your mantra:
'See, RW doesn't know what he's talking about, therefore everything he says is
wrong. Case dismissed. Next.' I say this because I've seen them do it to others;
I never failed their silly little test. 

>> Once, when talking to a lawyer, I cited cases which chearly proved he was
wrong.
>> He got red in the face, stood up behind his desk and shouted, "IF YOU KNOW SO
>> DAMNED MUCH, WHY DON'T YOU DRAW THE DOCUMENTS YOURSELF?" (I did, and saved
the
>> client several hundred thousand over the lawyer's solution.) <g>

>Just because you saved the Lawyer's fees doesn't mean you saved
>thousands, you may have made a mistake or missed a step and left the
>client with a potential liability.  You wouldn't know whether that was
>true or not.

The case involved emending leasehold rights so we could deepen an oil well. The
lawyer's way would have spent 6-12 months in research, trying to determine which
heirs and assigns were the legal owners of a 50 year old lease which had never
produced anything. It had a high probability of failure, because people change
their names through marriage or simply 'disappear'. My solution cost zero and
permitted us to drill within less than a month. The lawyer's delay is called
'opportunity cost'. We did, in fact, find oil coming from the same formation,
2,000 feet below where textbooks say it is 'supposed' to be. For more
information, Google on "Lower Spraberry Trend" and "Dean Sands". 

>> My point is: the standard projects an air of being definitive and exhaustive.
>
>It is, for the purposes of implementing a Cobol compiler or writing a
>program.

Not so. Using he '85 standard as an example, a compiler writer _should_ (not
must) know about IBM-isms such as pointers and goback. He should know about free
format. When generating code, he should know which features are heavily used and
which don't warrant optimization. 

>> operands, and that's not going to change, I'd be happy with "integer
>> containing a valid date". 
…[3 more quoted lines elided]…
>      ".. integer of the form YYYYMMDD whose value is .."

A second reading of the standard shows you're correct. I withdraw the proposal.

[snipped restart of the integer debate]
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-05-03T14:56:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0305031356.5f2e6db4@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net> <217e491a.0304301537.4fc1d813@posting.google.com> <3eb3e417.80393848@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> If I'd used the word incorrectly, it would have been easy to make me look
> foolish. 

"I can't make a monkey out of you, nature has beaten me to it."

> I've represented myself in court ("pro se") a few times. Judges and lawyers hate
> that. 

"A man that represents himself has a fool for a client."

> The first thing that happens is the judge throws me a 'trick' or unusually
> difficult question. If I can't answer, he says the equivalent of your mantra:
> 'See, RW doesn't know what he's talking about, therefore everything he says is
> wrong. Case dismissed. Next.' I say this because I've seen them do it to others;
> I never failed their silly little test. 

I am sure that, in your own mind, you have never failed any 'test'.

However, there has not been any 'trick questions here', you have
voluntarily shown that you "don't know what you are talking about" on
several items.

> The case involved emending leasehold rights so we could deepen an oil well. The
> lawyer's way would have spent 6-12 months in research, trying to determine which
…[6 more quoted lines elided]…
> information, Google on "Lower Spraberry Trend" and "Dean Sands". 

And, no doubt, all that it will take is one 'heir and assign' to show
up now for the whole cost to be a complete loss.  That is called
'risk'.  You took the risk on your employer's behalf because you knew
that you personnally would not make the loss.  Lawyers don't take
risks because they have a fidelity fund.  Your employer probably never
realised that they were taking a risk.


> >Well Duhh |  That is _exactly_ what the standard states:
> >
…[3 more quoted lines elided]…
> proposal.

As I have said before, "I wish that you would read _before_ ...."

Or is this a run up to making a different demand for a change ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-04T00:31:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb43e2e.1269130@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net> <217e491a.0304301537.4fc1d813@posting.google.com> <3eb3e417.80393848@news.optonline.net> <217e491a.0305031356.5f2e6db4@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>

>> The case involved emending leasehold rights so we could deepen an oil well. 
>
>And, no doubt, all that it will take is one 'heir and assign' to show
>up now for the whole cost to be a complete loss.

The operator of the lease below ours, as legal agent for the heirs and assigns,
gave us a properly executed and recorded assignment. There was no possible loss
to them because they would never have been permitted to produce from that
formation due to Field Rules (State regulatory agency). But in the unlikely
event owners thought they had a complaint, it would be against their own
operator (Exxon) not us. 

>That is called
>'risk'.  You took the risk on your employer's behalf because you knew
>that you personnally would not make the loss.  Lawyers don't take
>risks because they have a fidelity fund.  Your employer probably never
>realised that they were taking a risk.

That is called FUD. There was no legal risk to anyone, only the risk that we'd
spend $30K 'wildcatting' and end up with a dry hole.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-05T14:43:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b95tak$p20$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <217e491a.0304291314.73bebff1@posting.google.com> <3eb005b3.514075751@news.optonline.net> <217e491a.0304301537.4fc1d813@posting.google.com> <3eb3e417.80393848@news.optonline.net>`

```

On  3-May-2003, robert@wagner.net (Robert Wagner) wrote:

> My comments are not directed at the J4 committee; they are directed at a
> programming culture which adopts technical words from other cultures, mostly
> math and logic, and misuses them. It gets the meaning almost right but not
> quite. This is irritating because the reasan WHY the words were invented was
> to give them definitions more precise than common usage.

Don't limit this to programming cultures.   Every culture adapts jargon and
gives it its own meaning(s).   Words don't mean the same thing over time, space,
nor specialty.   This does cause confusion, such as when a non-scientist says
"it's only a theory", thinking that there is a different meaning between
"theory" and "law".   Or when an Englishman and a Californian talk together.

The thing is - the claim that one math definition is more right than the English
definition and the CoBOL definition isn't supportable.

So we make sure our definitions are well defined and go from there.


> Every field has jargon that was created to facilitate accurate communication.
> Doctor, lawyers or plumbers would be offended if laymen redefined their
> professional argot by using the terms casually.

Which explains why some people are offended when you redefine our professional
argot.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-30T17:20:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb00395.513533519@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3eadbca2.364276112@news.optonline.net...

>> But 'fixed-point' is
>> nowhere defined in the standard. Thus, the definition fails internally
…[4 more quoted lines elided]…
>fails because "floating-point" is not expressly defined.

Floating-point is defined. And fixed-point literal is defined fairly well at
8.3.1.2.2.1. But fixed-point numeric data item is not defined (except as you
point out below).

An observation, not a criticism: that's what happens when you move definitions
out of a glossary, into the body.

>Thus, anyone who is incapable of understanding at a glance what any given
>term not expressly defined in the standard (for example, "fixed-point" and
…[4 more quoted lines elided]…
>consistent with their *standard* dictionary definitions.

Fair enough. I was unaware that reference is in the standard. 


>> Writers of the standard tried to careful to distinguish the container from
>its
…[10 more quoted lines elided]…
>cited the rule; see above.

You are right, again.

>> 3.  Change the definition of integer-of-date to use an operand 'numeric
>data
…[5 more quoted lines elided]…
>"value-add".

My wording was sloppy. I'd be happy with "integer containing a valid date".

>> While you're at it, change accept ... from date and accept ... from time
>> similarly.
…[3 more quoted lines elided]…
>should unconditionally be zero. 

Technically, the function returns a number, then COBOL's rules for MOVE put the
number into the receiving field. 

I'd wager STRONG on pic x(6) would cause a type mismatch.


>> [I breeched my 'no more integer debate' because Chuck Stevens has been
>silent
>> for a month. Let's not reopen the thread, please.]
>
>(Just out of curiosity, how do you go about breeching a debate?)

By omitting the word policy. :)

>There is new information in the above response, and that new information is
>that the standard explicitly suggests the use of an American English
>dictionary when attempting to understand terms not expressly defined in the
>standard.

Yes, that's useful information. Thank you for the response.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-30T11:57:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8p6af$1du$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb00395.513533519@news.optonline.net...
> >> 3.  Change the definition of integer-of-date to use an operand 'numeric
> >data
> >> item'
> >
> >Why expand the description of this function to allow numbers with
fractional
> >digits as well as floating-point values along with integers?   I don't
see
> >this change to the existing functionality as having a particular
> >"value-add".
>
> My wording was sloppy. I'd be happy with "integer containing a valid
date".

For the 2002 standard, function integer-of-date does already accept any
value that represents a valid date, and rejects any value that does not, at
execution time.  In the latter case, the process includes the raising of an
appropriate exception and the expectation that the value returned from the
function be undefined.

As Bill K. pointed out a while back, in the case of '85 COBOL, there's no
standard exception handling.  In our implementation, the result of a call on
integer-of-date when the argument is invalid is zero, and while that's a
valid value, it wouldn't be unreasonable for the application program to
"trap" for December 31, 1600.   As a corollary to this point, our '85
implmentation of date-of-integer also returns zero for a negative argument.
This result, while a valid integer, is clearly not a valid date.
Determination as to whether the original argument to integer-of-date is
valid or not can thus be made by comparing SOME-GREGORIAN-DATE with FUNCTION
DATE-OF-INTEGER (FUNCTION INTEGER-OF-DATE (SOME-DATE)), at least in our
implementation of that dialect.

> >> While you're at it, change accept ... from date and accept ... from
time
> >> similarly.
> >
> >The date and time ACCEPTs already allow non-integer destinations;
however,
> >the result of a FRACTION-PART function using the destination as an
argument
> >should unconditionally be zero.
>
> Technically, the function returns a number, then COBOL's rules for MOVE
put the
> number into the receiving field.
>
> I'd wager STRONG on pic x(6) would cause a type mismatch.

No, it'd cause a syntax error before you ever got to the ACCEPT.   TYPEDEF
STRONG and PIC (X) cannot appear on the same declaration.  TYPEDEF STRONG
cannot appear on an elementary item, PIC X(6) cannot appear anywhere else.

Moreover, the rules for MOVE explicitly allow an alphanumeric destination
here, and the behavior of ACCEPT is explicitly defined in terms of those
rules.  Perhaps you've misunderstood the use of TYPE and TYPEDEF in COBOL.
There's a summary of COBOL's use of "types" on pages 742-744 of ISO/IEC
1989:2002.  Can you couch your wager in terms that an implementation of that
standard would reasonably accept?   As it stands, every way I can interpret
your assertion, given the rules of the language, you'd lose your wager.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-30T16:56:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8pnrs$e16$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb00395.513533519@news.optonline.net...

> Floating-point is defined.

I did a search and didn't find a satisfactory definition.  Absent an
explicit general definition (that covers both floating-point numeric data
item and floating-point numeric literal), I believe the Tenth Collegiate
definition is adequate in any case.

> An observation, not a criticism: that's what happens when you move
definitions
> out of a glossary, into the body.

*What* is what happens?  Everything that's defined in the standard is
defined in the standard; for anything that isn't, there's always the
dictionary definition.  And the standard even tells you *which* dictionary
is most likely to provide a good approximation of the authors' intents!

Even with a glossary within the standard, the terms still need to be defined
in context, and in general, the glossary entries have historically tended to
be condensed versions of the "real" definitions -- and there have
occasionally been some conflicts.  With the availability of electronic
versions, in which a "click" on the index entry takes you directly to the
page containing the definition, the usefulness of the glossary is somewhat
diminished.

> Fair enough. I was unaware that reference is in the standard.

Ummm... that's why we suggested you *read* it, and be familiar with what it
contained, some weeks back ...


> >The date and time ACCEPTs already allow non-integer destinations;
however,
> >the result of a FRACTION-PART function using the destination as an
argument
> >should unconditionally be zero.
>
> Technically, the function returns a number, then COBOL's rules for MOVE
put the
> number into the receiving field.

Presuming by "the function" you meant "ACCEPT ... FROM DATE" (for example),
no, it's not a function, and no, it doesn't return (just) a number.  It
causes the information in a CONCEPTUAL data item that "behaves as if it had
been described as an unsigned elementary integer data item of usage display
six digits in length ..." to be transferred into the destination according
to the rules for MOVE.  The declaration of this CONCEPTUAL data item is thus
something like  PIC 9(6) USAGE DISPLAY, whatever sorts of destinations one
can use for such a source field in MOVE are valid destinations for this form
of the ACCEPT, and the results are the same as if the information (e.g., the
value 030430) in a PIC 9(6) DISPLAY data item had been MOVEd to the
destination.  That there's also a CONCEPTUAL redefinition of this six-digit
field into three two-digit subfields, two of which have valid ranges, does
not diminish the importance of the fact that the basic information returned
is an unsigned elementary integer field of usage display six digits in
length, not a set of three two-digit fields that happens to get passed as
six contiguous digits.

If on the other hand what you meant by "the function" is FUNCTION
FRACTION-PART, it indeed does return a numeric value, but the rules for MOVE
are relevant only for MOVE FUNCTION FRACTION-PART (some-field) TO somewhere,
not for all uses of the function.  And in that case, the whether the result
is fixed-point or floating-point all the digits to the LEFT of the
conceptual decimal-point are zero, so the only "whole number" "the function"
can return is zero.

The COBOL standard carefully describes what such mechanisms provide;
"returns a number" was considered insufficiently precise by the framers.
While FUNCTION FRACTION-PART returns a "numeric value", FUNCTION FACTORIAL
returns an "integer".

Perhaps tangential, but similarly:  FUNCTION EXP10 doesn't return "the value
of 10 raised to the power of the argument", it returns "an approximation of
the value of 10 raised to the power of the argument.".  This is one of the
cases in which, even if "standard arithmetic" is in use, results for
arithmetic expressions may differ from one implementation to another.
ANNUITY, E, EXP, LOG, LOG10, PRESENT-VALUE, PI, SQRT, STANDARD-DEVIATION,
VARIANCE and the trig functions and their inverses, also produce results
that are implementor-defined approximations.  So does the exponentiation
operator, for example, in the expression A ** B, the result is an
approximation for all values of  B other than the integers -4, -3, -2, -1,
0, 1, 2, 3 and 4.   That means that if B is a floating-point item, the
result of the expression is still an approximation, even if B contains an
exact representation of +4.0E+000, precisely because no floating-point
numeric data item qualifies as "an integer" in the rules for exponentiation.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-03T17:42:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb3f379.84331666@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:


>Perhaps tangential, but similarly:  FUNCTION EXP10 doesn't return "the value
>of 10 raised to the power of the argument", it returns "an approximation of
…[11 more quoted lines elided]…
>numeric data item qualifies as "an integer" in the rules for exponentiation.

The spec was written that way to give compiler writers the option of using
logarithms. The solution is simple -- use ROUNDED to get a whole number result
-- but could cause serious cumulative error to the unaware.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-05T11:15:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b969om$2nu$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb3f379.84331666@news.optonline.net...

> The spec was written that way to give compiler writers the option of using
> logarithms. The solution is simple -- use ROUNDED to get a whole number
result
> -- but could cause serious cumulative error to the unaware.

The spec made no presumption of the use of logarithms (for EXP10 in
particular, for all of the functions producing inexact results in general),
though I concur that's what an implementor is most likely to do in the case
of EXP10.  The spec doesn't care whether you use logarithms or a motorized
abacus run by a D-to-A converter.

As I read it, the spec does not specify the degree of exactness of the
result of any function for which the results are explicitly described as
approximations (with the exception of FUNCTION PI and FUNCTION E, each
defined with explicit values to 32 digits of precision) even when standard
arithmetic is in effect.

When the result of a function that returns an inexact result is used in a
MOVE or other statement that does not allow the ROUNDED clause, the use of
ROUNDED is not a simple solution.

When the result of a function that returns an inexact result is used as a
component of an arithmetic expression, the use of ROUNDED may or may not be
a simple solution.

When the destination of an activity that uses a function that returns an
inexact result is a floating-point item, the use of ROUNDED will most likely
not be a simple solution.

In sum, I don't think the answer to making the results of functions defined
as producing approximate results identical and thus portable across all
platforms is to be found in the ROUNDED clause in every case.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-07T03:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb87638.17286648@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3eb3f379.84331666@news.optonline.net...
…[10 more quoted lines elided]…
>abacus run by a D-to-A converter.

There are successive approximation techniques which consume much less cpu time
than logarithms. A classic is Heron's method used by all calculators to compute
square roots,

>As I read it, the spec does not specify the degree of exactness of the
>result of any function for which the results are explicitly described as
…[6 more quoted lines elided]…
>ROUNDED is not a simple solution.

So don't use MOVE, instead use COMPUTE. 

>When the result of a function that returns an inexact result is used as a
>component of an arithmetic expression, the use of ROUNDED may or may not be
>a simple solution.

Yes, You'll have to break up those expressions and manage intermediate results
yourself. 

>When the destination of an activity that uses a function that returns an
>inexact result is a floating-point item, the use of ROUNDED will most likely
>not be a simple solution.

Correct. ROUNDED is meaningless for floating point. 

>In sum, I don't think the answer to making the results of functions defined
>as producing approximate results identical and thus portable across all
>platforms is to be found in the ROUNDED clause in every case.

Not true. Consider:

compute d rounded = (c ** b) * a

versus 

compute e rounded = (c ** b)
compute d rounded = e * a

Assuming all variables except a are whole numbers, the former will return an
approximate answer whereas the latter will return an exact answer.
```

###### ↳ ↳ ↳ ARITHMETIC EXPRESSION not "exact" (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-06T22:54:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9a0io$ogp$1@slb0.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb87638.17286648@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> >"Robert Wagner" <robert@wagner.net> wrote in message
> >news:3eb3f379.84331666@news.optonline.net...
> >
<snip>
> >In sum, I don't think the answer to making the results of functions
defined
> >as producing approximate results identical and thus portable across all
> >platforms is to be found in the ROUNDED clause in every case.
…[10 more quoted lines elided]…
> Assuming all variables except a are whole numbers, the former will return
an
> approximate answer whereas the latter will return an exact answer.

Robert,
  This is another error in your knowledge of the '85, 2002, or any other
ANSI/ISO Standard.  The "expression" to the right of the "=" sign in the
COMPUTE statement is (was, and always will  be BY DEFAULT), "implementor
defined".  This is true whether the operand is "**" or "*" or "+".

The 2002 Standard adds two ways of getting "more exact/portable" results.

1) If the (non-default) ARITHMETIC IS STANDARD phrase is specified, then
many (but not all) arithmetic expressions have portable results.

2) In the 2002 Standard *but NOT* in the '85 Standard, if a single operand
is to the right of the "=" then the results are "exact"

  ***

Bottom-line:
  RW's statement

  "Assuming all variables except a are whole numbers, the former <exprssion
'e * a'> will return an exact answer."

is simply NOT guaranteed by ANSI/ISO COBOL. Should you wish to verify what
the '85 Standard says about this, see page XVII-89 which states (in part),

     "(27) Arithmetic expression. Each implementor will indicate the
techniques used in handling arithmetic expressions. (See 6.2.3, rule 6, on
page VI-53.)"

and to see how this changes in the 2002 Standard section "Substantive
changes not affecting existing programs" on page 823 where it states,

    "4) ARITHMETIC clause. The STANDARD phrase specifies that certain
arithmetic will be performed in a welldefined manner and may yield results
that are portable. When standard arithmetic is in effect there is no
restriction on composite of operands."
```

###### ↳ ↳ ↳ Re: ARITHMETIC EXPRESSION not "exact" (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-08T16:29:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba84e6.1708184@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net> <b9a0io$ogp$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3eb87638.17286648@news.optonline.net...
…[59 more quoted lines elided]…
>restriction on composite of operands."

I was not representing what the standard says; I was talking about practice and
how we applications programmers can correct inexact results.

I posted a demo of this in reply to Chuck Stevens.
```

###### ↳ ↳ ↳ Re: ARITHMETIC EXPRESSION not "exact" (was: Accuracy/Knowledge score-card

_(reply depth: 28)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-08T13:16:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9e6tk$lte$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net> <b9a0io$ogp$1@slb0.atl.mindspring.net> <3eba84e6.1708184@news.optonline.net>`

```
And did you run your demo program under EVERY implementation?  What I was
trying to point out was that *any* COMPUTE statement (with or without
ROUNDED, with or without any operator) may produce DIFFERENT results under
different implementations.

As you often cite "real word experience" with Micro Focus - check out the
existing MF "arithmetic" compiler directive.
```

###### ↳ ↳ ↳ Re: ARITHMETIC EXPRESSION not "exact" (was: Accuracy/Knowledge score-card

_(reply depth: 29)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-09T02:03:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ebaf2f0.29883083@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net> <b9a0io$ogp$1@slb0.atl.mindspring.net> <3eba84e6.1708184@news.optonline.net> <b9e6tk$lte$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>And did you run your demo program under EVERY implementation?  What I was
>trying to point out was that *any* COMPUTE statement (with or without
>ROUNDED, with or without any operator) may produce DIFFERENT results under
>different implementations.

Running it under every implementation would be impractical and unnecessary. The
point is: my solution will produce a correct result under EVERY implementation. 

>As you often cite "real word experience" with Micro Focus - check out the
>existing MF "arithmetic" compiler directive.

I found MF produced the correct answer without micromanaging intermediate
results. So there is no reason to play with compiler directives.
```

###### ↳ ↳ ↳ Re: ARITHMETIC EXPRESSION not "exact" (was: Accuracy/Knowledge score-card

_(reply depth: 30)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-08T22:25:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9f75i$iin$1@slb5.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net> <b9a0io$ogp$1@slb0.atl.mindspring.net> <3eba84e6.1708184@news.optonline.net> <b9e6tk$lte$1@slb6.atl.mindspring.net> <3ebaf2f0.29883083@news.optonline.net>`

```
Sorry, Robert - but you are missing the point (again),

There is *NO* guarantee of any "accuracy" (or inaccuracy) for a COMPUTE
statement with an '85 Standard compiler - or with any earlier compiler - or
with a 2002 Standard compiler (unless ARITHMETIC IS STANDARD - which is NOT
the default - is specified).

Therefore, you statement,

   "The point is: my solution will produce a correct result under EVERY
implementation."

canNOT be verified to be true - unless you either change it to NOT use the
COMPUTE statement or you test it on every implementation.  You *may*
(correctly) state,

  "The point is: my solution will produce a correct result under EVERY
implementation that I have used <with every variation of compiler options or
directives that I have tested.>"

But other than that, you are jumping to an unverified (and in fact dubious)
conclusion.
```

###### ↳ ↳ ↳ Re: ARITHMETIC EXPRESSION not "exact" (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-08T13:27:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9eejg$2qb3$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net> <b9a0io$ogp$1@slb0.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b9a0io$ogp$1@slb0.atl.mindspring.net...

> Robert,
>   This is another error in your knowledge of the '85, 2002, or any other
…[17 more quoted lines elided]…
>   "Assuming all variables except a are whole numbers, the former
<exprssion
> 'e * a'> will return an exact answer."
>
…[14 more quoted lines elided]…
>

I agree, Bill.  The point I was trying to make to Robert was that even when
standard arithmetic is in effect there are some cases (as in LOG10) that are
EXPLICITLY defined as producing INEXACT results, and other cases that are
explicitly defined as producing exact results in an extremely limited
context (as in exponentiation).  Rounding has no impact on the exactness or
inexactness of the expression.    And as you point out, precision and
exactness when *native* arithmetic is in effect (and for implementations
compliant with prior standards) is exactly what the implementor defines it
to be.

In a COBOL2002 program, FUNCTION PI yields an approximation of the ratio of
the circumference of a circle to its diameter.   This approximation is
defined as being equivalent to the value 3.1415926535897932384626433832795
(whether or not standard arithmetic is in effect).  It is NOT an EXACT
representation of the ratio but an approximation of that ratio.

(A similar approximation for that ratio can be obtained in COBOL85 with, for
example, "2 * FUNCTION ASIN (1)" or "4 * FUNCTION ATAN (1)".  Our
implementation produces an approximation that is more precise -- 
3.1415926535897932384626 in both cases -- than the 2002 standard requires,
but nonetheless it is INEXACT, as for any value produced by FUNCTION ASIN or
ATAN in any implementation).

One can round this value to 3, or to 3.14, or to 3.14159, or to
3.1415926535898 if one chooses, but rounding it or any other intermediate or
final result does not make it more exact, it merely makes it a different
(and perhaps more useful) approximation.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-05-07T09:14:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9bbdi$j0t$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eb87638.17286648@news.optonline.net...
> >In sum, I don't think the answer to making the results of functions
defined
> >as producing approximate results identical and thus portable across all
> >platforms is to be found in the ROUNDED clause in every case.
…[10 more quoted lines elided]…
> Assuming all variables except a are whole numbers, the former will return
an
> approximate answer whereas the latter will return an exact answer.

Wrong.  In the 2002 standard, the expression -- or subexpression -- (c **
b) is only defined as producing an exact answer when b is an integer and its
value is a member of a very limited subset of the set of whole numbers.  To
wit:

For b = 0, (a ** b) is defined as equivalent to the arithmetic expression
(1).
For b = +1, (a ** b) is defined as equivalent to (a).
For b = +2, (a ** b) is defined as equivalent to (a * a).
For b = +3, (a ** b) is defined as equivalent to ((a * a) * a).
For b = +4, (a ** b) is defined as equivalent to ((a * a) * (a * a)).

For negative b, (a ** b) is defined as equivalent to (1 / (a ** FUNCTION ABS
(b))).

Thus, when b is a member of the set (-1 .. -4), the expression (a ** b)
likewise produces standards-defined values.  For all other values of b, "the
value of the result shall be an implementor-defined value that is normalized
and stored in a standard intermediate data item." , even when standard
arithmetic is specified.

In previous standards, all arithmetic was implementor defined.

     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-08T16:24:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eba83da.1440137@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net> <b8m69e$utm$1@si05.rsvl.unisys.com> <3eb00395.513533519@news.optonline.net> <b8pnrs$e16$1@si05.rsvl.unisys.com> <3eb3f379.84331666@news.optonline.net> <b969om$2nu$1@si05.rsvl.unisys.com> <3eb87638.17286648@news.optonline.net> <b9bbdi$j0t$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3eb87638.17286648@news.optonline.net...
…[37 more quoted lines elided]…
>arithmetic is specified.

Thank you for confirming what I said. 

We application programmers can correct the error and produce an exact result by
managing intermediate values. Here is a demo program how:

 identification division.
 program-id. test29a.
*> author. Robert Wagner.
*>  Demonstrates error in computation and how to correct it.
*>  Compiled under Fujitsu V3.0

 data division.
 working-storage section.
 01  unqualified-variables.
     05  a  value 10  comp     pic s9(04).
     05  b  value 19  comp     pic s9(04).
     05  c  value 12  comp     pic s9(03)v9.
     05  d1           comp     pic s9(18).
     05  d2           comp     pic s9(18).
     05  i            comp     pic s9(18).
     05  quotient     comp     pic s9(18).
     05  r1           comp     pic s9(04).
     05  r2           comp     pic s9(04).

 procedure division.

*>  returns incorrect answer
     compute d1 rounded = (b ** c) * a
*>  correct error in intermediate result by rounding it to an integer
     compute i  rounded = b ** c
     compute d2         = i * a

     divide 100 into d1 giving quotient remainder r1 *> incorrect
     divide 100 into d2 giving quotient remainder r2 *> correct
     display r1 space r2
     goback.
```

###### ↳ ↳ ↳ ACCEPT from DAY/DATE/DAY-OF-WEEK/TIME (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-29T16:47:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8mruf$c20$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <217e491a.0304172211.266de4d4@posting.google.com> <3ea0dac6.25472246@news.optonline.net> <b8jmkh$27j6$1@si05.rsvl.unisys.com> <3eadbca2.364276112@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eadbca2.364276112@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> >"Robert Wagner" <robert@wagner.net> wrote in message
> >news:3ea0dac6.25472246@news.optonline.net...
> >
<snip>

> 3.  Change the definition of integer-of-date to use an operand 'numeric
data
> item' While you're at it, change accept ... from date and accept ... from
time
> similarly.

I have ignored (up to now) Mr. Wagner's "problems" with ACCEPT from
DAY/DATE/DAY-OF-WEEK/TIME, because they seemed to be "minor" part of his
misunderstanding of the COBOL definition of integer.  However, I thought it
was about time to go into this particular issue.

1) There is currently no restriction on the type of "numeric" operand that
the RECEIVING item of a Format 2 ACCEPT statement may be.  Therefore, a
change from the (2002 Standard) statement,

  "DATE without the phrase YYYYMMDD behaves as if it had been described as
an unsigned elementary integer data item of usage display six digits in
length, ..."

seems to gain nothing.

3) In fact, changing from an integer sending item would cause serious
problems with the current rules of GR(6) which currently states,

"6) The ACCEPT statement causes the information requested to be transferred
to the data item specified by identifier-2 according to the rules for the
MOVE statement."

If you look at "Table 17 - Validity of types of MOVE statements" on page 478
of the 2002 Standard (or any comparable table in most vendors' LRMs or
previous Standards), you will see that Standard COBOL allows one to have a
sending item that is an integer and a receiving item that is

 - Alphanumeric
 - Alphanumeric-Edited
 - National
 - National-Edited

While having a sending item that is a numeric NON-integer item is prohibited
for such MOVEs.  Therefore, the following (relatively common) COBOL source
code would become invalid if RW's change to the ACCEPT statement were
implemented,

  05  Alpha-Date   Pic X(6).
        ...
 Accept Alpha-Date from Date

or the possibly even more useful

  05  Alpha-Edit  Pic XXXX/XX/XX.
        ..
  Accept Alpha-Edit from Date YYYYMMDD

***

Bottom-Line:
  Having the "implicit" sending item of Format 2 of the ACCEPT date defined
as an INTEGER and not just as a "numeric" operand is a HIGHLY useful (as
well as correct) feature of the COBOL language.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-19T04:28:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7nv0o$f9a$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net>`

```
Robert Wagner wrote:

>>So how do you say 'two places before the first' ?
> 
> You don't; negative subscripts are invalid. But negative numbers can be
> members of an ordered set, which makes them ordinals.

No.No.No.No.  Obviously you picked this up years ago and have been using 
this wrongly ever since.

If we have an ordered set of integers [-3, -2, -1, 0] Then -3 is the 
_first_ integer and thus has the ordinal 1.

'-3' isn't the ordinal, 1 is the ordinal for '-3' in that set.  

Get a basic book and learn something.

In Cobol terms the subscripts of a table are ordinals, not the contents.

> The author is confusing ordinal with enumeration.

Good one, it's everyone else's fault.  The whole world is wrong because RW 
has made up his mind.

>>Can you name one ?
 
> Any C/C++ compiler with a typedef to char, if not already provided. 

So, you couldn't actually find any, so you deflect 'implemented' to 'anyone 
can write a typedef'.

But you are wrong about C in yet another respect.  An integer may be 
negative or positive.  If you typedef 'tiny int' to 'char' then you will 
not get an integer, you need to specify 'signed char'.

> Did you want me to say Python?

Do you think that Python is a C compiler ?

> That's because your broadly enlightened world neglects to cite specific
> compilers in rebuttal.

Have you tried the one on your Sun machine ?  CP/M and DOS C compilers may 
well have used 16 bit int for 8088, but that is so 80s.  Almost any 
Windows, Unix, Linux or mainframe C/C++ compiler will be 32 bit, or have 
32bit option, over the last decade at least.

> I didn't say my programs would break. They wouldn't. But many poorly
> written programs would. 

Can you name any of them ?  Can you say _why_ they might break ?  Or is 
this merely speculation on your part ?

> Compiler writers are held hostage by it because they fear
> any change that breaks 'working' code will be a black mark against them.

What crap you spout.  Name one compiler that is 'held hostage' by 16bit ?

You are just making it up, again.

> Yeahbut, nobody uses BINARY because it's too slow (on many
> impementations), and because it requires 'too much typing' .. two more

Yet more dismissal and deflection.  Instead of noticing you were wrong you 
try to change the subject.

> keystrokes than COMP. The standards committee would have had a winner if
> they's gone with BIN.

Get some decent tools, I don't type keywords I have an editor that has them 
as two-key shortcuts.  Whining that it is too hard for you to type it is 
hardly in the same categorey as not knowing that is it defined.


> There certainly is. I'll find and post them tomorrow, 

That'll be a first.

> which is a legal
> holiday in the US (Good Friday, which is a good reason to know how to
> compute Easter).

Don't you read calendars ?  are they too much like manuals ?


> That depends on your definition of 'make this stuff up'. It originates in
> my logic, as opposed to looking it up in a Web site or book; but it's
> based on corrigible evidence such as real-world experience with compilers
> and knowledge of math fundamentals.

Yeah, right.  Only is seems that you got the fundementals wrong.

> I speak with my own voice rather than parroting reference material. It's
> riskier .. I've sometimes been wrong .. but it also holds the promise of
> illuminating truth. Those who look everything up are limited to the vision
> of their sources.

You mean people might all get it the same ?  That would be a tragedy, they 
would be able to understand each other instead of talking at cross purposes 
as you do.

> 20030331 is an integer only if I can add 1 and get a meaningful result.

Where does 'meaningful result' come into it ?  You just made up that bit.

But of course you also fail to notice that it is possible to do:

     20030331 + 1 -> 20030401

But then you probably don't know how to overload an operator.

> The site you referenced had a correct definition of cardinal. If you'll
> click on it, you'll find that cardinal is the size of a set, just as I
> said when I gave the example OCCURS 12.

Exactly.  cardinals may be zero, but cannot be negative.

You finally looked something up and found out what it really is:

RW>>  The word for limiting an set's range is called cardinalization

No. Cardality is the _size_ of the set, not the range of its contents.


> As for ordinal, see above. Many set members can be ordinals, not just
> numbers. For instance, the letters of the alphabet .. and dates in the
> form yyyymmdd.

No. Wrong. In the set ['a', 'b', 'c'] the ordinal of 'a' is 1.  'a' is not 
an ordinal, 1 is the ordinal of 'a'.  The cardinality of the set is 3.  It 
is an ordinal (ordered) set, not a set of ordinals (it is actually a set of 
letters).

What did that site say about ordinals ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T06:30:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0dd1d.26070844@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b7nv0o$f9a$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[6 more quoted lines elided]…
>this wrongly ever since.

Didn't you know? ALL my knowledge is antequated. 

>If we have an ordered set of integers [-3, -2, -1, 0] Then -3 is the 
>_first_ integer and thus has the ordinal 1.
…[3 more quoted lines elided]…
>Get a basic book and learn something.

As I said elsewhere, the word ordinal can be used in two ways. It can mean
'ordinal data' -- the member of an ordinal set -- and 'ordinal number' -- the
position of the member within the set. You are using it in the latter sense. 

>In Cobol terms the subscripts of a table are ordinals, not the contents.
>
…[3 more quoted lines elided]…
>has made up his mind.

Don't you like the way I use 'deflection' and 'projection'? 

>>>Can you name one ?
> 
…[7 more quoted lines elided]…
>not get an integer, you need to specify 'signed char'.

Thanks for the technical correction.

>> Did you want me to say Python?
>
>Do you think that Python is a C compiler ?

The question was 'which languages support tiny?' It was not about C. A little
Googling revealed that Python supports tiny. 

>> That's because your broadly enlightened world neglects to cite specific
>> compilers in rebuttal.
>
>Have you tried the one on your Sun machine ? 

They don't trust me with a C compiler. Hard to believe but true. 

>CP/M and DOS C compilers may 
>well have used 16 bit int for 8088, but that is so 80s.  Almost any 
>Windows, Unix, Linux or mainframe C/C++ compiler will be 32 bit, or have 
>32bit option, over the last decade at least.

Ok, I'll take your word as true. 

>> I didn't say my programs would break. They wouldn't. But many poorly
>> written programs would. 
>
>Can you name any of them ?  Can you say _why_ they might break ?  Or is 
>this merely speculation on your part ?

It could be as stupid as for (i=1, i >0, i++), expecting the loop to quit after
16K iterations. 

>> Yeahbut, nobody uses BINARY because it's too slow (on many
>> impementations), and because it requires 'too much typing' .. two more
>
>Yet more dismissal and deflection.  Instead of noticing you were wrong you 
>try to change the subject.

Wanna talk about chemistry or physics?

>Get some decent tools, I don't type keywords I have an editor that has them 
>as two-key shortcuts.  Whining that it is too hard for you to type it is 
>hardly in the same category as not knowing that is it defined.

See recent posts saying they're not blame, their editors put everything in upper
case.

I wrote the editor I use. If one wants another feature, (s)he can have it by
writing an extension in any language that compiles and links to an .exe. I wrote
it in 1990. Today I'd use .dll. 

>> which is a legal
>> holiday in the US (Good Friday, which is a good reason to know how to
>> compute Easter).
>
>Don't you read calendars ?  are they too much like manuals ?

Computers have a hard time reading printed calendars. It's easier to compute
dates like the Friday before Easter. 

>> That depends on your definition of 'make this stuff up'. It originates in
>> my logic, as opposed to looking it up in a Web site or book; but it's
…[3 more quoted lines elided]…
>Yeah, right.  Only is seems that you got the fundementals wrong.

Check my references in the thread What is an Integer. 

>> I speak with my own voice rather than parroting reference material. It's
>> riskier .. I've sometimes been wrong .. but it also holds the promise of
…[5 more quoted lines elided]…
>as you do.

Your statement would be valid if people were rational. Sadly, they're not. They
have bones to pick and emotional injuries to revenge, just as I do. If they are
mainframe programmers, they fear obsolescence. It's all about emotion -- fear
and greed. 

I used to be a floor trader on the Chicago Board of Options Exchange (CBOE).
There, you could look into someone's eyes and SEE whether he's motivated by fear
or greed. If it's fear (he's selling), you offer him a low price. If it's greed
(he's buying), you offer him a high price.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:18:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80uk2$t0f$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net>`

```

On 17-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Yeahbut, nobody uses BINARY

I use BINARY

> because it's too slow (on many impementations), and
> because it requires 'too much typing' .. two more keystrokes than COMP.

I found a long time ago that programming is much easier if I can type.   Adding
a few letters (or periods) is not onerous.

> The standards committee would have had a winner if they's gone with BIN.

BIN would be faster than BINARY?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T16:40:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea41d13.239084847@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 17-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[13 more quoted lines elided]…
>BIN would be faster than BINARY?

Eventually. Programmers would use BIN to reduce typing. Studies would find that
BIN is a speed bottleneck.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-21T15:51:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304211451.6a6e43f8@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >> The standards committee would have had a winner if they's gone with BIN.
>
> Eventually. Programmers would use BIN to reduce typing. 

That is a particularly pathetic argument.  You had previously argued
that you liked Cobol because it is more English-like, and this made it
more reliable.  Now you want the committee to have made it less so.

Am I surprised by your inconsistencies ?  Not at all.

You are also using very poor tools if you actually have to type in
reserved words, haven't you heard of 'keyboard macros' over the last
couple of decades ?

> Studies would find that BIN is a speed bottleneck.

Only on Intel.  Have you tried it on Sun ? ARM ? native Alpha ?

For portability (remember this started as one of your claims about
portability that showed you hadn't a clue) BINARY is big-endian, as
are all Cobol defined storage types.  On big-endian machines BINARY is
fast.
```

###### ↳ ↳ ↳ Binary (was: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T18:05:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b81tg4$jnj$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com>`

```
Although I agree with most of Richard's comments below, I am "confused" by
the sentence,

" For portability ... BINARY is big-endian, as  are all Cobol defined
storage types."

I don't know of any specific place in the STANDARD that requires this, and I
believe (but could be mistaken) that SOME compilers do use "little-endian"
formats for BINARY - and claim (accurately as far as I know) that this is
ANSI/ISO conforming.
```

###### ↳ ↳ ↳ Re: Binary (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-04-21T22:45:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA4ACCB.3010707@ix.netcom.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b81tg4$jnj$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:
> Although I agree with most of Richard's comments below, I am "confused" by
> the sentence,
…[7 more quoted lines elided]…
> ANSI/ISO conforming.
<snip>

I really thought this was controlled by the HARDWARE not the 
software.

High order bit determines sign v. low order bit controlling the 
sign. How could the compiler control this UNLESS the hardware was 
switchable?
```

###### ↳ ↳ ↳ Re: Binary (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T22:12:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b82bua$i8r$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b81tg4$jnj$1@slb9.atl.mindspring.net> <3EA4ACCB.3010707@ix.netcom.com>`

```
The *only* requirement that the COBOL Standard places on a data item with
USAGE BINARY is (from the 2002 Standard)

"The USAGE BINARY clause specifies that a radix of 2 is used to represent a
numeric item in the storage of the computer. Each implementor specifies the
precise effect of the USAGE BINARY clause upon the alignment and
representation of the data item in the storage of the computer, including
the representation of any algebraic sign. Sufficient computer storage shall
be allocated by the implementor to contain the maximum range of values
implied by the associated decimal picture character-string."

Therefore, in cases (unlike most mainframe enviornments) where the compiler
vendor and the hardware vendor and the operating system vendor are *NOT* the
same, it is the compiler vendor (alone) who determines how USAGE BINARY
items are stored (which may or may not match any hardware or OS "native"
type).
```

###### ↳ ↳ ↳ Re: Binary (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-21T21:46:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304212046.35bf746b@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b81tg4$jnj$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote 

> I don't know of any specific place in the STANDARD that requires this, and I
> believe (but could be mistaken) that SOME compilers do use "little-endian"
> formats for BINARY - and claim (accurately as far as I know) that this is
> ANSI/ISO conforming.

Is it not an actual requirement for standard numeric data items (ie
excluding COMP etc) to be big-endian - most significant in lowest
address bytes. ? Perhaps I had assumed too much.
```

###### ↳ ↳ ↳ Re: Binary (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** "Lorne Sunley" <lsunley@mb.sympatico.ca>
- **Date:** 2003-04-22T04:56:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JMPlV5b5VFnN-pn2-NBHddIYoeIgL@h24-82-204-17.wp.shawcable.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b81tg4$jnj$1@slb9.atl.mindspring.net> <217e491a.0304212046.35bf746b@posting.google.com>`

```
On Tue, 22 Apr 2003 04:46:22 UTC, riplin@Azonic.co.nz (Richard) wrote:

> "William M. Klein" <wmklein@ix.netcom.com> wrote 
> 
…[7 more quoted lines elided]…
> address bytes. ? Perhaps I had assumed too much.

Depends on the CPU the compiler is generating code for, and the people
who write the compliler. I believe it is one of those "implementer 
defined" things... The compiler writers do it the way they think it 
should be done, and according to the standard that is acceptable, so 
the compiler is ANSI/ISO conforming.
```

###### ↳ ↳ ↳ Re: Binary (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T02:06:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304220106.145324a5@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b81tg4$jnj$1@slb9.atl.mindspring.net> <217e491a.0304212046.35bf746b@posting.google.com> <JMPlV5b5VFnN-pn2-NBHddIYoeIgL@h24-82-204-17.wp.shawcable.net>`

```
"Lorne Sunley" <lsunley@mb.sympatico.ca> wrote 

> > Is it not an actual requirement for standard numeric data items (ie
> > excluding COMP etc) to be big-endian - most significant in lowest
> > address bytes. ? Perhaps I had assumed too much.
> 
> Depends on the CPU the compiler is generating code for, 

Not necessarily.  On Intel MF have COMP and BINARY as big-endian
though the machine is little-endian.  Use COMP-5 for native.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-22T13:59:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b83hsb$7la$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com>`

```

On 21-Apr-2003, riplin@Azonic.co.nz (Richard) wrote:

> That is a particularly pathetic argument.  You had previously argued
> that you liked Cobol because it is more English-like, and this made it
> more reliable.  Now you want the committee to have made it less so.

Except periods are English like.


> You are also using very poor tools if you actually have to type in
> reserved words, haven't you heard of 'keyboard macros' over the last
> couple of decades ?

If you are worried about such things, the best thing to do is to work on typing
skills.  Once you realize how work it is to not be able to type quickly and
accurately, it is obvious that working on typing pays off.


> For portability (remember this started as one of your claims about
> portability that showed you hadn't a clue) BINARY is big-endian, as
> are all Cobol defined storage types.  On big-endian machines BINARY is
> fast.

That makes sense.  I wondered how binary would NOT be fast - I didn't think of
little-endian computers being slower.   Too bad those little-endian chips are
dropping decimal support.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T12:37:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304221137.3f9d79dd@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote

> That makes sense.  I wondered how binary would NOT be fast - I didn't think of
> little-endian computers being slower.   Too bad those little-endian chips are
> dropping decimal support.

Little-endian machines aren't slower .. when the numbers they work on
are little-endian.  With MF's COMP and BINARY the Intel machines have
to swap bytes.  This is why COMP-5 is slightly faster for real work
involving calculations*.

However where there is a mixed workload typical of Cobol applications
where there is data being read, calculations done and output being
done to files, screens and printer then the conversions between
display, numeric edited and binary or native formats can take more
time than the savings in using native formats for calculations.

* RW will try to tell you it up to 30 times faster, but that is for
trivial stuff that is probably optimised away to nothing.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-23T14:32:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304221137.3f9d79dd@posting.google.com...
> "Howard Brazee" <howard@brazee.net> wrote
>
> > That makes sense.  I wondered how binary would NOT be fast - I didn't
think of
> > little-endian computers being slower.   Too bad those little-endian
chips are
> > dropping decimal support.

I have to believe with all this discussion of "big-endian v little-endian"
someone can come up with one of those cute mnemonic devices to remember
which is which.. you know, like the "bad boys rape young girls but Violet
gives willingly" used to remember the color-coding on resistors.

Come to think of it, here's a starter....."big-endian" could use a reference
to Jennifer Lopez.......

MCM
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-23T12:08:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b86dq4$53g$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com>`

```
In article <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:

[snip]

>I have to believe with all this discussion of "big-endian v little-endian"
>someone can come up with one of those cute mnemonic devices to remember
>which is which.. you know, like the "bad boys rape young girls but Violet
>gives willingly" used to remember the color-coding on resistors.

Mr Mattias... whose young girls are subject to these attacks?

(Orange you glad I asked?)

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-24T10:50:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea718e8_1@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <b86dq4$53g$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b86dq4$53g$1@panix1.panix.com...
> In article <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com>,
> Michael Mattias <michael.mattias@gte.net> wrote:
…[3 more quoted lines elided]…
> >I have to believe with all this discussion of "big-endian v
little-endian"
> >someone can come up with one of those cute mnemonic devices to remember
> >which is which.. you know, like the "bad boys rape young girls but Violet
…[3 more quoted lines elided]…
>
PMFJI, but, obviously, the leaders of the Resistance...

> (Orange you glad I asked?)
>
No, I took it as red <G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-23T20:53:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b87cij$dno$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <b86dq4$53g$1@panix1.panix.com> <3ea718e8_1@127.0.0.1>`

```
In article <3ea718e8_1@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b86dq4$53g$1@panix1.panix.com...
…[12 more quoted lines elided]…
>PMFJI, but, obviously, the leaders of the Resistance...

All the ones who sang along when Paul Henreid lead the band at Rick's Cafe 
Americain in La Maresilles, then!

>
>> (Orange you glad I asked?)
>>
>No, I took it as red <G>

Red?  I could'a sworn that one was from Calcutta... honest Injun, I 
could'a!

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-24T03:31:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA75201.A8250C49@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <b86dq4$53g$1@panix1.panix.com> <3ea718e8_1@127.0.0.1> <b87cij$dno$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:

>
> >PMFJI, but, obviously, the leaders of the Resistance...
…[3 more quoted lines elided]…
>

What a movie ! Bogey, Ingrid, Paul (as above), Sydney Greenstreet, Peter Lorre,
Claude Rains, Conrad Veidt. Old enough to be my mother, but I fall in love with
Ingrid each time I see it.

Made in 1942, did you realize "You must remember this..." was written in the year
I was born - 1931.

Jimmy
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-24T09:10:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b88nn8$7dt$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea718e8_1@127.0.0.1> <b87cij$dno$1@panix1.panix.com> <3EA75201.A8250C49@shaw.ca>`

```
In article <3EA75201.A8250C49@shaw.ca>, James J. Gavan <jjgavan@shaw.ca> wrote:
>
>
…[11 more quoted lines elided]…
>Ingrid each time I see it.

A curious 'B pic that became a classic', this 'Everybody Goes to 
Rick's'... as I recall nobody knew how it was going to end because they 
kept rewriting the script just before scenes were shot.

'And what in Heaven's name brought you to Casablanca?'

'My health.  I came to Casablanca for the waters.'

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-23T17:01:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA70D39.8010001@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com>`

```
Michael Mattias wrote:
> Come to think of it, here's a starter....."big-endian" could use a reference
> to Jennifer Lopez.......

I'll second that, as long as there are pictures in the manual...
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-23T23:03:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA717E5.FB4889EC@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <3EA70D39.8010001@Knology.net>`

```


LX-i wrote:

> Michael Mattias wrote:
> > Come to think of it, here's a starter....."big-endian" could use a reference
…[3 more quoted lines elided]…
>

How Lo can you get ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-23T19:52:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA73545.8010704@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <3EA70D39.8010001@Knology.net> <3EA717E5.FB4889EC@shaw.ca>`

```
James J. Gavan wrote:
> 
> LX-i wrote:
…[11 more quoted lines elided]…
> How Lo can you get ?

Have you seen the movie "Maid in Manhattan"?  There's a scene in there 
where she's walking out of this fundraiser, and she turns around - she's 
wearing this really pretty dress, and there's a light shining behind her...

Man...  :)
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-24T14:04:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D9Spa.3080$%_3.2451717@newssrv26.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <3EA70D39.8010001@Knology.net> <3EA717E5.FB4889EC@shaw.ca> <3EA73545.8010704@Knology.net>`

```
INTELigent Jennifer is big-endian?

MCM
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-24T02:02:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea7256a.99146076@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote:

>"Richard" <riplin@Azonic.co.nz> wrote in message
>news:217e491a.0304221137.3f9d79dd@posting.google.com...
…[11 more quoted lines elided]…
>gives willingly" used to remember the color-coding on resistors.

No, it was "bad boys rape young girls behind vertical garden walls."

>Come to think of it, here's a starter....."big-endian" could use a reference
>to Jennifer Lopez.......

Monica Lewinsky has a much bigger butt. 
>
>MCM
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-24T14:01:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b88qna$ndl$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net> <b80uk2$t0f$1@peabody.colorado.edu> <3ea41d13.239084847@news.optonline.net> <217e491a.0304211451.6a6e43f8@posting.google.com> <b83hsb$7la$1@peabody.colorado.edu> <217e491a.0304221137.3f9d79dd@posting.google.com> <7uxpa.2787$%_3.2202561@newssrv26.news.prodigy.com> <3ea7256a.99146076@news.optonline.net>`

```

On 23-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >I have to believe with all this discussion of "big-endian v little-endian"
> >someone can come up with one of those cute mnemonic devices to remember
…[3 more quoted lines elided]…
> No, it was "bad boys rape young girls behind vertical garden walls."

I hadn't heard your variation.

Another one I remember is:
Oh, Be A Fine Girl, Kiss Me Right Now! Smack

Checking the internet, I find:

http://www.frii.com/~geomanda/mnemonics.html

This has both versions and more.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:23:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80usu$t7b$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <217e491a.0304170023.389e60a6@posting.google.com> <3e9f4d01.363414286@news.optonline.net>`

```

On 17-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> 20030331 is an integer only if I can add 1 and get a meaningful result.

cite?

> That's why I said "you can't add 1 to a date", which no one seemed to
> understand.

Almost always we do not use such a date as an integer.

But we have posted examples where adding 1 to such a date is meaningful and
useful.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-17T08:07:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7mfvt$67n$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9de0f1.270200298@news.optonline.net...

> This is analogous to COBOL's BINARY or (vendor extension) unsuffixed COMP.

Unsuffixed COMP[UTATIONAL] has always been in the ANSI COBOL standards; the
behavior is implementor-defined.

BINARY has been in the ANSI COBOL standard since '85; the behavior is
implementor-defined.

<<It can mean whatever you want it to mean.>>

No, it can mean whatever the *implementor of the compiler* decides it should
mean.

<<That sounds good in the conference room, but hardly supports
portability.>>

Portability of files is of course an issue in this respect; less so is
portability of *logic* except in the extreme edge cases.

"Standard Arithmetic", new in ISO/IEC 1989:2002, helps in this area (though
there are some cases in which, despite the programmer's best efforts to
maintain "standard arithmetic" the implementor is allowed to escape to
"native arithmetic").

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-18T02:02:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9f3a0a.358558705@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[13 more quoted lines elided]…
>mean.

Some compilers make unsuffixed COMP mean whatever YOU want it mean, via a
compiler option. You might say I want all my COMPs to be COMP-5 or BINARY or
PACKED DECIMAL. 

><<That sounds good in the conference room, but hardly supports
>portability.>>
…[7 more quoted lines elided]…
>"native arithmetic").

I wish you wouldn't use 'implementor' in a perjorative or demeaning sense, as
others use 'vendor' and 'contractor'. You make them sound like members of the
unwashed masses standing at the curbside, awaiting your invitation to join the
party. In fact, implementors such as Micro Focus, IBM and Fujitsu gave us
pointers and OO COBOL _years_ before the standards committee did. 

I trust you'll understand because you're so sensitive to nuance and perceived
slight against Unisys.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-18T05:23:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9F841F.29124521@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net>`

```


Robert Wagner wrote:

> I wish you wouldn't use 'implementor' in a perjorative or demeaning sense, as
> others use 'vendor' and 'contractor'. You make them sound like members of the
…[3 more quoted lines elided]…
>

Chuck's hands are clean, he's a comparative newcomer to J4 - the current
representative for Unisys. While I positively hate the long delays there have been
getting COBOL 2002 out, which incorporates OO - keep the thing in perspective.

Hitachi, IBM, F/J and M/F would *not* have OO compilers based on an 'iffy'
situation. None of the four would have attempted an implementation on something so
major if there hadn't been a nod from J4. (At one stage there was publicity on the
Web that Unisys were going to pick up on Hitachi's OO - but it fizzled out, and
the reason was of their own corporate making. We don't need to know why. Full
Stop/Period).

I've forgotten the three individuals referred to by Ann Bennett (IBM's J4 rep),
though I recall one was from Micro Focus, and I *think* another was HP. These
three gave the first impetus to OO, (at least in her mind), as an idea back in
92/93 (??). J4 went along with it and set up a separate group OOCTG, (OO COBOL
Technical Group). The results were summarized in a paperback from the OOCTG,
authored by Ray Obin of M/F. The syntax arrived at is very, very close to what we
have now, with the exception of Standard Classes (collections/lists currently
being discussed by J4, with a lot of work done by Thane Hubbell which I've only
just picked up on as a result of somebody currently querying).

So the above four vendors went with it, IBM initially with Visual Age, and now
their Enterprise compiler which uses Java for support.

If there's a disappointment - it is because new features have taken so bloody
long. Again there was somewhat of an admission  - we were overloaded with a whole
daffy of suggestions, so we had to prioritize. OO was NOT a top priority. With
hindsight that seems daft, but that's how they saw it at the time. It's worth
noting that some of the observers, as opposed to the regular J4 team, as of a
couple of years back,  had *no* intention of adding OO. It may have changed since
COBOL 2002 was issued - but who knows.

Is this just the vendors ? No. If you wish to make yourself as popular as a pork
pie in a synagogue, (perhaps I should have written "a second pork pie" <G>'), -
just start a thread titled "Mainframe People MUST Start using OO".

Bill Klein is well versed on the above - so if I've missed out or misinterpreted -
be sure he will jump in.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T06:30:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0c0dc.18837191@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

Thanks for taking the time to provide insider information, which is probably
unavailable elsewhere.

> If you wish to make yourself as popular as a pork pie in a synagogue, ..
>just start a thread titled "Mainframe People MUST Start using OO".

I think mainframers would ignore the thread. An alternative idea is posting lots
of OO 'sample code' written in uppercase, using periods galore, awkward logic,
and four digit method name prefixes. It would be like watching grandparents
trying to be modern. Hilarious. And the real OO programmers (both of them) would
be on blood pressure medication.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-19T18:16:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA193CA.1D635CD7@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net>`

```


Robert Wagner wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[10 more quoted lines elided]…
> be on blood pressure medication.

Well have I got a surprise for you <G>. For the most part my method-names do not
have prefixes, just 'Camel backed' like "getCustomerDiscountRate". However, working
totally in class structures there is merit in prefixes in some instances. For
example I have a program (class) which is performing a series of calculations. (Now
of course you wont find this in other OO languages - but do we have to serviley ape
them, when this is a pretty neat feature of COBOL ?)

Method-id. "begin".

set ContinueProgram to true
invoke self "openFiles"

if ConrtinueProgram
    invoke self "getLiistboxItems"

   if ContinueProgram
     invoke self "P0-processTransactions"

     .      *> Note - the IMPORTANT period/full-stop appears here

P0-processTransactions is a 'Section Header' or 'Control Paragraph' if you like,
which could invoke self :-

P1-ReadNext
P2-ProcessTransation
P3-doSomethingElse
P4-etc....

Note the 'Prefixes" are internal to this program - and I would NEVER use them when
invoking other classes or super, the one higher up in the hierarchy. My reasoning
for those prefixes - a question of personal style :-

Within one program/class -

- Non-prefixed names - listed in alphabetical order at the top of the program,
invariably starting with a method "begin' - really no different to 'Main" or
'Mainline"

- Prefixed names - these follow as a group below the above and obviously I have them
in ascending sequence by the "P-numeric".

I absolutely *detest* non-OO programs where I see the flow listed in 'progress'
sequence, and the programmer has chosen concise/appropriate paragraph names BUT
which are totally out of sync alphabetically. (It becomes a real pain in the butt
moving up and down the source looking for such paragraphs).

BTW - if you want 'Best Practices" for COBOL 2002 onwards - take a look at :-

http://www.cobolportal.com/j4/index.asp

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T22:08:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea1bf5e.84001192@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>
>
>Robert Wagner wrote:
>
>> "James J. Gavan" <jjgavan@shaw.ca> wrote:

>> > If you wish to make yourself as popular as a pork pie in a synagogue, ..
>> >just start a thread titled "Mainframe People MUST Start using OO".
…[8 more quoted lines elided]…
>not have prefixes, just 'Camel backed' like "getCustomerDiscountRate". 

It's called Object Oriented because the word order is noun.verb. Your naming
convention reverses that, turning it back into verb.noun. You're packaging old
wine in new bottles. 

>However, working
>totally in class structures there is merit in prefixes in some instances. For
>example I have a program (class) which is performing a series of calculations.
(Now
>of course you wont find this in other OO languages - but do we have to serviley
ape
>them, when this is a pretty neat feature of COBOL ?)
>
…[11 more quoted lines elided]…
>     .      *> Note - the IMPORTANT period/full-stop appears here

That's nothing more than a string of PERFORMs.

>P0-processTransactions is a 'Section Header' or 'Control Paragraph' if you
>like, which could invoke self :-
…[4 more quoted lines elided]…
>P4-etc....

Your methods are ordered by time, not alphabetically as you say below.

>Note the 'Prefixes" are internal to this program - and I would NEVER use them
when
>invoking other classes or super, the one higher up in the hierarchy. My
reasoning
>for those prefixes - a question of personal style :-
>
…[6 more quoted lines elided]…
>- Prefixed names - these follow as a group below the above and obviously I have
them
>in ascending sequence by the "P-numeric".

When you say listed, do you mean comment lines or method prototypes? 

>I absolutely *detest* non-OO programs where I see the flow listed in 'progress'
>sequence, and the programmer has chosen concise/appropriate paragraph names BUT
>which are totally out of sync alphabetically. (It becomes a real pain in the
>butt moving up and down the source looking for such paragraphs).

I too detest temporal cohesion, preferring instead functional cohesion. Given
that you prefer alphabetic cohesion, why divide code into small source units?
Why not one monolithic source program with everything listed alphabetically?

Time to leave .. this is where I came in.

Sounds like you need a better editor. With mine (which I wrote), I select the
name or put the cursor anywhere on the line, hit the hyperlink key and, shazam,
I'm there. It doesn't matter whether the target is a paragraph, called program
or copybook. It can even be a .jpg or .gif. When finished, I hit the escape key
and it puts me back where I was.

>BTW - if you want 'Best Practices" for COBOL 2002 onwards - take a look at :-
>
>http://www.cobolportal.com/j4/index.asp

A conference for OO COBOL programmers. Where will it be held, in the back seat
of a Volkswagen? <ducking and running> Just kidding.
```

###### ↳ ↳ ↳ Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-19T17:20:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7si40$opb$1@slb4.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3ea1bf5e.84001192@news.optonline.net...
> "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
<snip >
> >Well have I got a surprise for you <G>. For the most part my method-names
do
> >not have prefixes, just 'Camel backed' like "getCustomerDiscountRate".
>
> It's called Object Oriented because the word order is noun.verb. Your
naming
> convention reverses that, turning it back into verb.noun. You're packaging
old
> wine in new bottles.

OK, RW - where did you get this bit of information that

 "It's called Object Oriented because the word order is noun.verb."

For a good explanation of the "Object" in "Object-oriented" see:

 http://www.webopedia.com/TERM/o/object_oriented_programming_OOP.html

which says (in part),

"A type of programming in which programmers define not only the data type of
a data structure, but also the types of operations (functions) that can be
applied to the data structure. In this way, the data structure becomes an
object that includes both data and functions. In addition, programmers can
create relationships between one object and another. For example, objects
can inherit characteristics from other objects."

The COBOL explanation starts on page 768 of the 2002 Standard where it says,

"Object oriented programming is all about developing and implementing
application systems as sets of interacting
software objects.

A software object, like most objects in everyday life, such as an
automobile, has a unique identity, and certain attributes and behaviors. The
automobile has a unique identity, its serial number; it has many attributes
such as color, number of doors, and weight. It also has such behaviors as
forward, reverse, accelerate, shift, and the like. Software objects are used
to model real world objects and as such they abstract the key concepts of
the real world object in software. A software object used to model an
automobile would for example, have a unique identity, and attributes such as
color, weight, and length, as well as such behaviors as forward and reverse.

Software objects can be used to model any of the concepts germane to a given
problem domain. For example they can represent bank accounts, employees,
parts, processes, programs, fields, files, structures and the like.

Therefore, we can say a software object is an entity that has a unique
identity, specific data values, and specific behaviors or program code. The
program code is organized into small modules. In object oriented terminology
these modules are called methods. Data is encapsulated within each object
and can only be accessed by using one or more of the object's methods."

   ***

There is nothing in either of these that in ANY WAY gets into "word order" -
whether noun.verb or anything else.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-19T19:40:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA1EC99.20400@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net>`

```
William M. Klein wrote:
>>It's called Object Oriented because the word order is noun.verb. Your
> 
…[12 more quoted lines elided]…
> 

I believe the point is that in object-oriented, you would have a "car" 
class that has a "drive" method, not a "drive" class that has a "car" 
property or attribute.  IOW, car.drive, not drive.car (or "driveTheCar").

Man, I wish they'd let us play with OO at work...  Unisys has an OO 
interface using Hitachi on the front end, and we own licenses for it, we 
just can't get a fire under the right people's rears to get it to us.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-20T03:18:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA212D9.9AB3ED5C@shaw.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net>`

```


LX-i wrote:

> William M. Klein wrote:
> >>It's called Object Oriented because the word order is noun.verb. Your
…[18 more quoted lines elided]…
>

LX-i,

Don't get ballsed-up in the fancy terminology - go with what works for you <G>.
So happens that Net Express has a class called 'Vocabulary' where you could make
a 'credit' turn into a 'debit'. Just think what fun RW could have with switching
integers and dates <G>

> Man, I wish they'd let us play with OO at work...  Unisys has an OO
> interface using Hitachi on the front end, and we own licenses for it, we
> just can't get a fire under the right people's rears to get it to us.
>

Chuck,

Please expand - I thought the Unisys/Hitachi tie-up had died out ?????? Is there
an on-line doc I can look at ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-19T22:39:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA21656.7000508@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca>`

```
James J. Gavan wrote:
> Don't get ballsed-up in the fancy terminology - go with what works for you <G>.
> So happens that Net Express has a class called 'Vocabulary' where you could make
> a 'credit' turn into a 'debit'. Just think what fun RW could have with switching
> integers and dates <G>

I'm actually fascinated by OO.  It took about four classes (I guess I 
should say "training sessions") for it to click, but now that it's 
clicked, I'm intrigued.  I think there are -quicker- ways of doing 
things, but I'm not sure that for <buzzword warning> reusability, 
encapsulation, and ease of future maintenance, it's not the way to go.

>>Man, I wish they'd let us play with OO at work...  Unisys has an OO
>>interface using Hitachi on the front end, and we own licenses for it, we
…[7 more quoted lines elided]…
> an on-line doc I can look at ?

Maybe that explains part of my problem...  :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:51:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b810h0$of$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net>`

```

On 19-Apr-2003, LX-i <DanielJS@Knology.net> wrote:

> I'm actually fascinated by OO.  It took about four classes (I guess I
> should say "training sessions") for it to click, but now that it's
> clicked, I'm intrigued.  I think there are -quicker- ways of doing
> things, but I'm not sure that for <buzzword warning> reusability,
> encapsulation, and ease of future maintenance, it's not the way to go.

Me too.  Encapsulation will be the selling point which might eventually give me
an "in" to use it.   Certainly not reusability which will make maintenance more
complex and expensive in typical mainframe CoBOL environments that have higher
standards for testing than do most environments that use OO with a lot of
reusability.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-21T20:12:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA4970C.7090702@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
>>I'm actually fascinated by OO.  It took about four classes (I guess I
>>should say "training sessions") for it to click, but now that it's
…[9 more quoted lines elided]…
> reusability.

My biggest gripe right now has to do more with the environment I'm in. 
Unisys' link processor allows you to do "static linking" (where all the 
object modules are linked into one executable) or "dynamic linking" 
(where all external references are resolved at runtime), or a 
combination of the two (ex. static link system subroutines, dynamically 
link custom ones).

I'm the keeper of two widely-used subprograms in our system, one that 
handles output messaging and one that handles security.  Any time I need 
to work on one of these programs, every program in the system has to be 
recompiled (actually, only relinked, but we don't save the intermediate 
object modules) to pick up this change.  It would be a whole lot simpler 
to use dynamic linking to pick these up without having to make a "new 
version" of every executable.

However, our programs run in the TIP (transaction) environment, and 
everything I've read about dynamic linking and the TIP environment says 
that it can't be done, because of the way TIP loads things into memory. 
  I'm just wondering if OO would help me get around some of that.

Along those lines, does anyone have customers like this?  Their managers 
go read magazines in the john, and then they come ask us if we can use 
"x" technology or "y" buzzword-of-the-week in their system.  It's 
frustrating, but they'd just be ecstatic if we told them we could make 
their existing COBOL object-oriented.  :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-04-21T22:48:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA4AD68.3060204@ix.netcom.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net>`

```
LX-i wrote:
<snip>
> Along those lines, does anyone have customers like this?  Their managers 
> go read magazines in the john, and then they come ask us if we can use 
> "x" technology or "y" buzzword-of-the-week in their system.  It's 
> frustrating, but they'd just be ecstatic if we told them we could make 
> their existing COBOL object-oriented.  :)
<snip>

Are you sure they weren't on some business trip and stayed at a 
Holiday Inn Express?
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-21T21:50:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA4ADF3.1020604@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net> <3EA4AD68.3060204@ix.netcom.com>`

```
Steve Thompson wrote:
> LX-i wrote:
> <snip>
…[10 more quoted lines elided]…
> Inn Express?

Could be...  :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-21T23:21:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-12E034.23214121042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net>`

```
In article <3EA4970C.7090702@Knology.net>, LX-i <DanielJS@Knology.net> 
wrote:

> Howard Brazee wrote:
> >>I'm actually fascinated by OO.  It took about four classes (I guess I
…[39 more quoted lines elided]…
> their existing COBOL object-oriented.  :)

I run into plenty of people that suggest that I should statically link 
to save a few milliseconds of CICS time....

Tell them to wake up and get into the 80's...programmer time costs more 
than CPU...
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-22T14:03:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b83i3k$7sh$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net> <joe_zitzelberger-12E034.23214121042003@corp.supernews.com>`

```

On 21-Apr-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> I run into plenty of people that suggest that I should statically link
> to save a few milliseconds of CICS time....
>
> Tell them to wake up and get into the 80's...programmer time costs more
> than CPU...

I finally persuaded my shop to change the standard compile to do bounds checking
on tables.   It's funny how companies would tout PL/I because it didn't have
table overflow, but would turn off the compiler feature of CoBOL that did the
same thing - for efficiency sake.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2003-04-22T11:07:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA55AB5.7010209@newsguy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net>`

```
LX-i wrote:
 > I'm the keeper of two widely-used subprograms in our system, one that
 >  handles output messaging and one that handles security.  Any time I
…[10 more quoted lines elided]…
 > that.

Probably not.  OO and linking are orthogonal.  OO is a language issue;
it's a matter of providing rich encapsulation functions in the language
so that polymorphism and inheritance are (relatively) easy to achieve.
(It's entirely possible to implement polymorphism and inheritance
without OO language features; you just have to do the work yourself.
Polymorphism, for example, is just a matter of putting jump tables in
your data structures, so each data type "knows" what routine to invoke
to perform a given function.)

Dynamic linking is usually a function of the OS or a runtime environment
that's part of the language implementation.  It's unrelated to object
orientation.

I suspect if they tell you that dynamic linking isn't available in TIP,
it's not available.

As an aside, generally you don't want security modules to be linked
dynamically; it gives a local attacker another link in the chain to
attack.  (If the attacker can substitute their own module for the real
security module in the dynamic linking process, they can subvert the
security mechanism.)
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-28T15:26:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8k9pt$2l41$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net>`

```
"LX-i" <DanielJS@Knology.net> wrote in message
news:3EA4970C.7090702@Knology.net...

>   I'm just wondering if OO would help me get around some of that.

> Along those lines, does anyone have customers like this?  Their managers
> go read magazines in the john, and then they come ask us if we can use
> "x" technology or "y" buzzword-of-the-week in their system.  It's
> frustrating, but they'd just be ecstatic if we told them we could make
> their existing COBOL object-oriented.  :)

I seem to recall that that you are using some sort of Unisys IX/2200 system
(as distinct from a Unisys MCP/AS system).   I don't have access to product
catalogs, but there either is or used to be an OO COBOL compiler available
on the Unisys IX / 2200 line, an implementation of at least part of the OO
features of the draft standard from a few years back.  I would expect it to
be upward compatible with earlier COBOL compilers on that platform.  Have
you (or your managers) checked into it?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-04-28T20:29:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EADD590.8070001@Knology.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net> <b8k9pt$2l41$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
> I seem to recall that that you are using some sort of Unisys IX/2200 system
> (as distinct from a Unisys MCP/AS system).   I don't have access to product
…[4 more quoted lines elided]…
> you (or your managers) checked into it?

We tried - I haven't gotten a response yet.  :)  But then, we sent the 
schedule for our current project up to HQ AF, and they said "if it's 
gonna take this long, never mind".  So, we're now in hurry-up mode to 
get something out the door, which has reduced our play time (for now). 
Maybe by the time we get this software out, the people will have gotten 
us a copy of what we need.  (I think the bottleneck is in DISA, not 
Unisys.)
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-29T05:23:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eadf8b3.379654936@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3EA1EC99.20400@Knology.net> <3EA212D9.9AB3ED5C@shaw.ca> <3EA21656.7000508@Knology.net> <b810h0$of$1@peabody.colorado.edu> <3EA4970C.7090702@Knology.net> <b8k9pt$2l41$1@si05.rsvl.unisys.com>`

```
>"LX-i" <DanielJS@Knology.net> wrote in message
>news:3EA4970C.7090702@Knology.net...
…[7 more quoted lines elided]…
>> their existing COBOL object-oriented.  :)

Almost right. 90% of managers' computer knowledge comes from airline magazines.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-20T03:12:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea20d13.103896318@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ea1bf5e.84001192@news.optonline.net...
…[15 more quoted lines elided]…
> "It's called Object Oriented because the word order is noun.verb."

It's my visionary take on OO, which says 'change the word order and everything
else will fall in place.'  <g> 

You can see it in most non-COBOL OO languages where the syntax is
'instance.method' or 'class.method'

Please, let's not start an OO debate. I could rant for hours, which would not
entertain other subscribers.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T15:07:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304221407.e3d0b9@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3ea20d13.103896318@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> > "It's called Object Oriented because the word order is noun.verb."
> 
> It's my visionary take on OO, which says 'change the word order and everything
> else will fall in place.'  <g> 

Others may say it was overly simplistic, superficial, missing the
point, or just wrong. You see it as 'visionary', am I surprised ?
 
> You can see it in most non-COBOL OO languages where the syntax is
> 'instance.method' or 'class.method'

That is _not_ a change in those other languages.  C always had
object.dataitem where 'object' was of type struct.  Pascal has always
used that for record access.

Objects hold data and methods, the reference to a method for the
object simply follows the same mechanism as has been used for the data
items for decades.

This _may_ give you a clue that there is something else going on.

> Please, let's not start an OO debate. I could rant for hours, 

Yes you could.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-23T03:58:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea5e3e4.16823291@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3ea20d13.103896318@news.optonline.net> <217e491a.0304221407.e3d0b9@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote

>> You can see it in most non-COBOL OO languages where the syntax is
>> 'instance.method' or 'class.method'
…[3 more quoted lines elided]…
>used that for record access.

That was C/Pascal's version of qualification, where one noun qualified another
(required even when the target was unequivocal, thereby punishing us for using
structures). Linking verbs to nouns is linguistically different. 
>
>Objects hold data and methods, the reference to a method for the
…[3 more quoted lines elided]…
>This _may_ give you a clue that there is something else going on.

Yes, there is something else going on. It's a fundamental linguistic change
starting with word order.
```

###### ↳ ↳ ↳ Re: Where did you get this one? (was: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-23T12:35:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304231135.11b5cc85@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net> <b7si40$opb$1@slb4.atl.mindspring.net> <3ea20d13.103896318@news.optonline.net> <217e491a.0304221407.e3d0b9@posting.google.com> <3ea5e3e4.16823291@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >That is _not_ a change in those other languages.  C always had
> >object.dataitem where 'object' was of type struct.  Pascal has always
…[4 more quoted lines elided]…
> structures). 

In what way is it 'punishing' ? Are your tired old fingers incapable
of typing ? Perhaps you don't understand namespaces and how using them
makes the program more readable.

> Linking verbs to nouns is linguistically different. 

This is programming languages, not english.  Objects can now contain
methods along with data and so the reference to those follows the
pattern already established.

> >This _may_ give you a clue that there is something else going on.
> 
> Yes, there is something else going on. It's a fundamental linguistic change
> starting with word order.

It is not a change of word order.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-19T21:08:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-6E7A42.21083919042003@corp.supernews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <3EA193CA.1D635CD7@shaw.ca> <3ea1bf5e.84001192@news.optonline.net>`

```
In article <3ea1bf5e.84001192@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote:
> >BTW - if you want 'Best Practices" for COBOL 2002 onwards - take a look at 
…[5 more quoted lines elided]…
> seat of a Volkswagen? <ducking and running> Just kidding. 

I suppose you would have to overload the Volkswagen to behave like hotel  
confrence room...
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:46:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8107r$hc$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net>`

```

On 19-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> I think mainframers would ignore the thread. An alternative idea is posting
> lots
…[3 more quoted lines elided]…
> would be on blood pressure medication.

Except for the "awkward logic", the others don't matter.

"Grandparents" (my 4th grandchild is less than a month old) are more likely to
emulate the style without understanding the substance than the other way around.

It's far better to understand the substance of OO without the style, than the
style of OO without the substance.

Or of programming.

Or of life.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T02:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea4a095.272756498@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <b8107r$hc$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 19-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
>> of OO 'sample code' written in uppercase, using periods galore, awkward
logic,
>> and four digit method name prefixes. It would be like watching grandparents
>> trying to be modern. Hilarious. And the real OO programmers (both of them)
…[5 more quoted lines elided]…
>emulate the style without understanding the substance than the other way
around.
>
>It's far better to understand the substance of OO without the style, than the
…[4 more quoted lines elided]…
>Or of life.


The pholosopher, Frank Zappa, said only four things matter in life:

. laughter
..kindness
..beauty/grace
..really good pizza

I would rewrite the fourth, but the others are pretty good.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T02:02:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304220102.46f53faf@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <3E9F841F.29124521@shaw.ca> <3ea0c0dc.18837191@news.optonline.net> <b8107r$hc$1@peabody.colorado.edu> <3ea4a095.272756498@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> The pholosopher, Frank Zappa, said only four things matter in life:

I may be missing what 'pholopsophy' is (is it to do with April 1), but
assuming this is just a typing error:

If there is a 'list of things that matter' then, for sure, philosphy
isn't on it.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-18T09:08:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7p7u6$2380$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9f3a0a.358558705@news.optonline.net...

> >"Standard Arithmetic", new in ISO/IEC 1989:2002, helps in this area
(though
> >there are some cases in which, despite the programmer's best efforts to
> >maintain "standard arithmetic" the implementor is allowed to escape to
> >"native arithmetic").

> I wish you wouldn't use 'implementor' in a perjorative or demeaning sense,
as
> others use 'vendor' and 'contractor'. You make them sound like members of
the
> unwashed masses standing at the curbside, awaiting your invitation to join
the
> party. In fact, implementors such as Micro Focus, IBM and Fujitsu gave us
> pointers and OO COBOL _years_ before the standards committee did.

I am absolutely baffled as to why you might think I intended to use
"implementor" in any pejorative or demeaning sense.  As someone who has (I
believe) contributed significantly to the implementation of three separate
standards-conforming COBOL compilers, I do not view "implementor" as a
pejorative or demeaning term.  I am absolutely baffled as to why you would
put the "spin" you describe on that paricular term, or feel that I have done
so.

I was using "implementor" in the sense in which it is used in ANSI
X3.23-1974, ANSI X3.23-1985 and ISO/IEC 1989:2002, that is, whatever person
or group of people is producing a compiler with the intent of conforming to
the particular standard.  Moreover, neither I nor the standard seems to care
who's "vending" the compiler, or whether or not "contractors" were employed
in its production, marketing or use.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T06:30:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0c7f0.20649360@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b7p7u6$2380$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[18 more quoted lines elided]…
>"implementor" in any pejorative or demeaning sense.

Because you said "despite the programmer's best efforts ... the implementor is
allowed to escape to "native arithmetic". That sounds like implementors try to
undercut the efforts of right-thinking programmers. And quotes around native
arithmetic make it sound pseudo-, quasi- or unimportant.

>I was using "implementor" in the sense in which it is used in ANSI
>X3.23-1974, ANSI X3.23-1985 and ISO/IEC 1989:2002, that is, whatever person
…[3 more quoted lines elided]…
>in its production, marketing or use.

I was making a simile to implementor. I didn't say the standard had an opinion
on vendors and contractors.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-19T04:50:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7o09n$fl9$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net>`

```
Robert Wagner wrote:

>>No, it can mean whatever the *implementor of the compiler* decides it
>>should mean.
> 
> Some compilers 

Can you specify which ones you were thinking of ?

> make unsuffixed COMP mean whatever YOU want it mean, 

No. Not 'whatever', it could only only be a certain range of options, and 
wouldn't include, say, excess-3.

> via a
> compiler option. You might say I want all my COMPs to be COMP-5 or BINARY
> or PACKED DECIMAL.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-18T12:59:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7plfs$2clc$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9f3a0a.358558705@news.optonline.net...

> Some compilers make unsuffixed COMP mean whatever YOU want it mean, via a
> compiler option. You might say I want all my COMPs to be COMP-5 or BINARY
or
> PACKED DECIMAL.

Naah.  Some compilers *may* make unsuffixed COMP mean whatever *you* want it
to mean, but it is not at all clear to me that some compilers make
unsuffixed COMP mean whatever *I* might want it to mean, as you assert (and
as you emphasize!).   I might say I want all my COMPs to be BINARY or
PACKED-DECIMAL (note the hyphen) (I doubt I'd want them to be declared
COMP-5, though, as that usage isn't meaningful to me), but it's not clear
that that represents the entirety of what *I* would place in the category of
"whatever", whether or not it represents the entirety of what *you* would
place in that category.

One that I don't see among the possibilities you list could be important for
file portability, a factor you have stressed as desirable in the past.
Suppose I want to make all my COMPs to be the same as if they'd been
declared DISPLAY?  Can *your* compiler do this?  Can *my* compiler do this?
Which compilers can?  Which compilers can't?

How about "A floating-point item, 144 bits long, allocated as follows:  One
bit for the sign of the mantissa (0=positive, 1 = negative); three bits
ignored; one bit for the sign of the exponent (0 = positive, 1 = negative);
eleven bits for the exponent magnitude (permissible magnitude range: 0 -
999), in base 2, representing the power of ten to which the mantissa is
scaled; and thirty-two decimal digits representing the mantissa, each
decimal digit occupying four bits.

This representation is one of a number of possible representations (ignoring
normalization) of a Standard Intermediate Data Item as described in ISO/IEC
1989:2002.  You wrote that some compilers allow me to specify *whatever I*
want COMP to mean.  That's what I want to specify COMP to mean.  I think
it'd be really, really useful.

Which of those "some compilers" allow me to specify that that description is
what I want COMP to mean, and what option do I use in that compiler to
direct it to do so?

     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T06:30:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0cb5a.21523645@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b7plfs$2clc$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9f3a0a.358558705@news.optonline.net...
…[20 more quoted lines elided]…
>Which compilers can?  Which compilers can't?

You are in a better position to answer that. The obvious syntax would be
COMP=DISPLAY. I 'think' I've seen that on some compilers. 

I would never put a generic COMP in a record. Doing so is guaranteed
non-portability. My records are all absent from COMP-, BINARY and
PACKED-DECIMAL.

>How about "A floating-point item, 144 bits long, allocated as follows:  One
>bit for the sign of the mantissa (0=positive, 1 = negative); three bits
…[10 more quoted lines elided]…
>it'd be really, really useful.

Assuming we're talking non-OO, the compiler must have some way of typing this
behemouth. Perhaps it would be something like COMP-6. In that case, you'd say
COMP=COMP-6
```

###### ↳ ↳ ↳ Standard Intermediate Data Item (was: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-19T10:02:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7roe7$pib$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b7plfs$2clc$1@si05.rsvl.unisys.com> <3ea0cb5a.21523645@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3ea0cb5a.21523645@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> >"Robert Wagner" <robert@wagner.net> wrote in message
> >news:3e9f3a0a.358558705@news.optonline.net...
> >
<snip>
> >
> >This representation is one of a number of possible representations
(ignoring
> >normalization) of a Standard Intermediate Data Item as described in
ISO/IEC
> >1989:2002.  You wrote that some compilers allow me to specify *whatever
I*
> >want COMP to mean.  That's what I want to specify COMP to mean.  I think
> >it'd be really, really useful.
>
> Assuming we're talking non-OO, the compiler must have some way of typing
this
> behemouth. Perhaps it would be something like COMP-6. In that case, you'd
say
> COMP=COMP-6
>
>

The 2002 Standard is *quite* clear that a conforming implementation need NOT
provide any "USAGE/PICTURE" specification that corresponds to a Standard
Intermediate Data Item's structure.  (This is similar to the fact that old
and new Standards don't require any implementation to make a "file
connector" a visible to the programmer structure.)

The rules for what happens when you move an SIDI (Standard Intermediate Data
Item) to any numeric receiving item (of any USAGE) are clear, but there is
no requirement that an implementation have such a "external" format.

P.S.  COMP-6 is in "medium" common usage among a variety of implementations
to indicate an unsigned Packed-Decimal item, i.e. one in which
    Pic  9(6) Comp-6
takes 3, not 4 bytes of storage (while COMP-3 or Packed-Decimal would take 4
bytes).  Obviously, this is implementation specific, as are *ALL* COMP-?
usages, but it is available in more than one implementation.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-19T13:51:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304191251.1fa37c37@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b7plfs$2clc$1@si05.rsvl.unisys.com> <3ea0cb5a.21523645@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> Some compilers make unsuffixed COMP mean whatever YOU want it mean, via a
> >> compiler option. You might say I want all my COMPs to be COMP-5 or BINARY
…[4 more quoted lines elided]…
> COMP=DISPLAY. I 'think' I've seen that on some compilers. 

So you may have just made this up.

> Assuming we're talking non-OO, the compiler must have some way of typing this
> behemouth. Perhaps it would be something like COMP-6. 

But you don't actually know and have made this up.

> In that case, you'd say COMP=COMP-6

On some comiler that you don't know exists, or if this would be an
option, so you just made this up.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-20T00:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea1c977.86586513@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b7plfs$2clc$1@si05.rsvl.unisys.com> <3ea0cb5a.21523645@news.optonline.net> <217e491a.0304191251.1fa37c37@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[8 more quoted lines elided]…
>So you may have just made this up.

The COMP= option is certainly not made up. I 'think' I've seen DISPLAY as one of
the possible selections. 

>> Assuming we're talking non-OO, the compiler must have some way of typing this
>> behemouth. Perhaps it would be something like COMP-6. 
>
>But you don't actually know and have made this up.

WMK explained intermediate formats can, but need not, have an identifier. 

>> In that case, you'd say COMP=COMP-6
>
>On some comiler that you don't know exists, or if this would be an
>option, so you just made this up.

We were discussing a hypothetical. Of necessity, it's made up; it doesn't exist
yet.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-21T05:12:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7tach$sjm$2@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea0cb5a.21523645@news.optonline.net> <217e491a.0304191251.1fa37c37@posting.google.com> <3ea1c977.86586513@news.optonline.net>`

```
Robert Wagner wrote:

>>> >> Some compilers make unsuffixed COMP mean whatever YOU want it mean,

> We were discussing a hypothetical. Of necessity, it's made up; it doesn't
> exist yet.

It what way was your initial claim a hypothetical ?

Once again you can't support a claim and so try to change it.
```

###### ↳ ↳ ↳ Programmer specification of what "COMP" means (was: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-19T16:43:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7sftj$dj0$1@slb3.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b7plfs$2clc$1@si05.rsvl.unisys.com>`

```
Chuck,
  I don't (personally)  know of any other compiler that supports programmer
control of what COMP means, but Micro Focus does.  There are two directives
that provide the facility of changing the meaning of COMP to mean *any*
other (already defined) USAGE.  From:

 http://supportline.microfocus.com/documentation/books/sx2011sp1/cypubb.htm

"COMP
Makes the Compiler produce very compact and efficient code for some
statements involving COMP data items, by treating COMP items as COMP-X."

    ***

"MAKESYN
Makes one reserved word synonymous with another."

*OBVIOUSLY* neither of these directives are included in Micro Focus'
"standard conforming" directives list.

FYI, there are other directives that impact things like COMP-6 and COMP-1/-2
... but these are the two that do provide "mostly" what RW mentions.  A
programmer may *not* (via these directives) "invent" their own USAGE, but
can change the meaning of COMP to whichever *other* USAGE they want.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T14:28:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80v72$t9b$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net>`

```

On 17-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Some compilers make unsuffixed COMP mean whatever YOU want it mean, via a
> compiler option. You might say I want all my COMPs to be COMP-5 or BINARY or
> PACKED DECIMAL.

That would be useful in conversion.  I would like to know which ones can do this
in case I have to do such a conversion - could you name a couple?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T02:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea4a4ce.273837122@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b80v72$t9b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 17-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[5 more quoted lines elided]…
>That would be useful in conversion.  I would like to know which ones can do
this
>in case I have to do such a conversion - could you name a couple?

Realia
Ryan McFarland
Micro Focus
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T22:06:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b82biu$l6$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b80v72$t9b$1@peabody.colorado.edu> <3ea4a4ce.273837122@news.optonline.net>`

```
I know how MF does it (and posted a note with the details)

Please tell me/us how either RM or Realia does this?
  (What "directive" or other facility lets you treat COMP as
Packed-Decimal)?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T15:55:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea56321.322567704@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <b7h09c$b3$1@panix1.panix.com> <3e9c8130.180137914@news.optonline.net> <217e491a.0304152227.6c182d7a@posting.google.com> <3e9de0f1.270200298@news.optonline.net> <b7mfvt$67n$1@si05.rsvl.unisys.com> <3e9f3a0a.358558705@news.optonline.net> <b80v72$t9b$1@peabody.colorado.edu> <3ea4a4ce.273837122@news.optonline.net> <b82biu$l6$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>I know how MF does it (and posted a note with the details)
>
>Please tell me/us how either RM or Realia does this?
>  (What "directive" or other facility lets you treat COMP as
>Packed-Decimal)?

RM:
 compiler-options.
  computational-type [binary | packed-decimal]

The default is display.

Realia:
On compiler option line, designated by "*$"
 no keyword, just
 comp-3, comp-5 or other comp-x

I think the default was comp-5. There is no comp-x associated with display. 


--- history follows ---
>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ea4a4ce.273837122@news.optonline.net...
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-04-15T11:16:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EmVma.1796$f34.369861@news20.bellglobal.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9be3b7.139819159@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>

> An integer, which derives from entire, specifies an ordinal set with no
holes in
> it. For example, -32768 thru 32767.
>
> A date is an ordinal; it is not an integer.
>
Huh?  A date is a date.  An integer is a number without a fractional
portion. Ordinals are specific sets of integers, not an alternatives to
them.  Do you thing integers were invented by computer people?  They were
able to count on fingers well before computers.

Donald
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-15T12:27:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304151127.13e89649@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >A date in a numeric form such as 20030415 is a perfectly good integer,
> >of course it is not a cardinal number, though it may resemble one.  RW
…[3 more quoted lines elided]…
> months in a year. 'OCCURS 12' is a cardinal number. 

Isn't google wonderful for looking these things up, and so simple to
cut and paste.
 
> An ordinal number does that and additionally specifies the order of things
> within a set. For example, 88 January value 01, 88 February value 02 ...
 
> A date is an ordinal; 

No.  A date in the form 20030415 is _not_ an ordinal.

The components of the date are ordinals, not the whole date.  The day
is an ordinal within the month, the month number is within the year,
the year within the era.

A Julian date is an ordinal number of days since 4147BC or whatever it
is.

> An integer, which derives from entire, 

An integer is a number without a fractional or decimal part, ie it is
entire in being a whole number. For a number to not be an integer it
must have a fractional or decimal part and be a real number, or have
an imaginary part and be a complex number.

> specifies an ordinal set with no holes in
> it. For example, -32768 thru 32767.
 
You just made that up.  An integer is _not_ a range, nor does it imply
a range. _An_ integer is a single number.

> it is not an integer.

An 'integer' is just the representation of digits _without_ a
fractional or decimal part.

A number 20030415 is an integer for the very simple reason that it is
a whole number without any fractional or decimal component.

It is _not_ cardinal, it is _not_ ordinal, though its parts are.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-16T03:35:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9ca90b.190342340@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[8 more quoted lines elided]…
>cut and paste.

I didn't look any of this up, and certaintly didn't cut and paste my responses. 

>> An ordinal number does that and additionally specifies the order of things
>> within a set. For example, 88 January value 01, 88 February value 02 ...
…[7 more quoted lines elided]…
>the year within the era.

You're correct. But when the whole date is returned as an 'integer', it is not.
That's what we're debating here. 
>
>A Julian date is an ordinal number of days since 4147BC or whatever it
>is.

Yes, it is. 

>> An integer, which derives from entire, 
>> specifies an ordinal set with no holes in
…[3 more quoted lines elided]…
>a range. _An_ integer is a single number.

It does imply a range in the context of 'computer integer'. See my reply to DD.

>An 'integer' is just the representation of digits _without_ a
>fractional or decimal part.
>
>A number 20030415 is an integer for the very simple reason that it is
>a whole number without any fractional or decimal component.

Now who's thinking like a 'coder'? Just because it it numeric doesn't make it an
integer. No more than a ZIP code or social security number or part number.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-16T00:16:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7iout$7ki$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net>`

```
Richard was correct and RW was wrong - at least as far as the *COBOL
definition* of an integer goes, i.e. if an intrinsic function returns the
date

    YYYYMMDD

as an "integer function" - then that date *is* an integer in COBOL's
definition.  Such integer functions may be used wherever COBOL allows an
integer to be used as a sending field (in the 2002 Standard - or where an
integer may be used as an arithmetic expression in the '89 Standard).

(See separate post on the 2002 Standard's full definition of what an integer
is in COBOL)
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-17T02:20:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9e0532.279483210@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Richard was correct and RW was wrong - at least as far as the *COBOL
>definition* of an integer goes, i.e. if an intrinsic function returns the
…[5 more quoted lines elided]…
>definition. 

Yes, but COBOL's definition is discordant with the mathematical definition of
integer. COBOL is simply using the word incorrectly. If COBOL used the word
'number' rather than 'integer', this wouldn't be an issue.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-16T22:40:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7l460$nap$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9ca90b.190342340@news.optonline.net> <3e9e0532.279483210@news.optonline.net>`

```
In article <3e9e0532.279483210@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>"William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[10 more quoted lines elided]…
>integer.

Mr Wagner, please be so kind as to supply the source you are using for 
'the mathematical definition of integer'; reading the text directly might 
prove interesting.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:37:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea065ea.435338471@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9ca90b.190342340@news.optonline.net> <3e9e0532.279483210@news.optonline.net> <b7l460$nap$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e9e0532.279483210@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[16 more quoted lines elided]…
>prove interesting.

I posted some references in a new thread: What is an Integer.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-19T10:38:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7rn0n$4u2$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b7l460$nap$1@panix1.panix.com> <3ea065ea.435338471@news.optonline.net>`

```
In article <3ea065ea.435338471@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[20 more quoted lines elided]…
>I posted some references in a new thread: What is an Integer.

Mr Wagner, according to one of those references:

http://www.bartleby.com/61/58/I0175800.html

--begin quoted text:

1. A member of the set of positive whole numbers {1, 2, 3, . . .},
negative whole numbers {-1, -2, -3, . . . }, and zero {0}

--end quoted text

... a date returned as YYYYMMDD - e.g., 20030331 - is returned as a 
positive whole number and is, by definition, an integer.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-17T14:47:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7l4me$8vq$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net>`

```
Robert Wagner wrote:

> "William M. Klein" <wmklein@ix.netcom.com> wrote:
> 
…[10 more quoted lines elided]…
> of integer. 

No, it is only discordant with what _you_think_ the 'mathematical 
definition of integer' is.

As I said (and I often have to say several times), it is not and ordinal or 
a cardinal, but number of the form 20030415 _is_ an integer.

In any case you wanted to change the argument to 'computer context', that 
didn't work, so now you try to change it to 'mathematical'.  Either way you 
get it all wrong ('ordinal set with range' - ROFL).

> COBOL is simply using the word incorrectly. If COBOL used the
> word 'number' rather than 'integer', this wouldn't be an issue.

'Numbers' are either 'integer' or 'real'.  The determinent is whether they 
have a decimal part.   A number of the form 20030415 has no decimal part 
and therfore _is_ an integer.

To say that they should use 'number' for an integer shows that you are 
unaware of the actual definitions of these words.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:37:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0663d.435422015@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b7l4me$8vq$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:

>In any case you wanted to change the argument to 'computer context', that 
>didn't work, so now you try to change it to 'mathematical'.  Either way you 
>get it all wrong ('ordinal set with range' - ROFL).

The only difference between computer context and mathematical context is range.
In math, integers go to infinity; in a computer, there is no infinity.

>> COBOL is simply using the word incorrectly. If COBOL used the
>> word 'number' rather than 'integer', this wouldn't be an issue.

>'Numbers' are either 'integer' or 'real'.  The determinent is whether they 
>have a decimal part.   A number of the form 20030415 has no decimal part 
>and therfore _is_ an integer.

I should have said 'whole number'.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-19T10:40:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7rn4o$5ur$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b7l4me$8vq$1@aklobs.kc.net.nz> <3ea0663d.435422015@news.optonline.net>`

```
In article <3ea0663d.435422015@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>Richard Plinston <riplin@Azonic.co.nz> wrote:
>
>>Robert Wagner wrote:

[snip]

>>> COBOL is simply using the word incorrectly. If COBOL used the
>>> word 'number' rather than 'integer', this wouldn't be an issue.
…[5 more quoted lines elided]…
>I should have said 'whole number'.

Mr Wagner, it may be that you 'should have'... but you did not.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:01:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8114f$10u$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net>`

```

On 16-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >
> >    YYYYMMDD
…[6 more quoted lines elided]…
> 'number' rather than 'integer', this wouldn't be an issue.

Huh?  Why would "number" be superior nomenclature to "integer"?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T02:57:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea4a510.273903349@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 16-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[11 more quoted lines elided]…
>Huh?  Why would "number" be superior nomenclature to "integer"?

Because number is not formally defined in math, whereas integer is. 

Actually, COBOL does use 'numeric data item' to describe pic 9 containers. It
uses integer to describe the 'class' of operands and function types. In all
cases but two, that I can think of, the term is used correctly, because terms
can have any value from zero to the limit of expression. 

The exceptions are ACCEPT .. FROM DATE and FUNCTION DATE-OF-INTEGER.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T22:08:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b82bnp$aqh$1@slb1.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net>`

```
Robert,
  What do you think about the COBOL *requirement* that a data item defined
with

       PIC 9999PP

be considered an integer data item?   As such a data item may only include
whole numbers "ending with 00", this seems to NOT fit into your use of the
term "integer".

(I thought you had dropped the integer debate, but if you haven't - I have
*never* seen your response to this.)
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T16:35:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea565f1.323288205@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Robert,
>  What do you think about the COBOL *requirement* that a data item defined
…[9 more quoted lines elided]…
>*never* seen your response to this.)

When Richard posed the question, I responded it's not an integer. The test for
integer is whether adding 1 will produce the next set member. 

I've always regarded pic P as an editing feature, intended for output. 

What happened to the unusual idea of permitting arithmetic on edited fields? Was
that in the 85 standard? The only use I could see was de-editing a report file
for data recovery.  

>
>--
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-22T16:08:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b84b26$69t$1@slb5.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net>`

```
"P" is *not* an editing symbol; the corresponding editing symbol is "0".
Therefore, one might find code such as:

   05 Num-Field    Pic S9999PP.
   05 Num-Ed-Field  Pic +++,900.
       ...
   Move Num-Field to Num-Ed-Field
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-23T03:58:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea5da3e.14353305@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net>`

```
Say I want to print a report with numbers rounded to thousands of dollars. This
is very common in the financial services industry. I'd write: 

  05  Num-Field   pic s9(12), 
  05  Num-Ed-Field pic zzz,zzz,zz9ppp-. 

  compute Num-Ed-Field rounded = Num-Field

The alternative would be:

 05  Num-Ed-Field pic zzz,zzz,zz9-.

 compute Num-Ed-Field rounded = Num-Field / 1000

--- history below ---
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"P" is *not* an editing symbol; the corresponding editing symbol is "0".
>Therefore, one might find code such as:
…[86 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Numeric-Edited and PIC P (was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-22T23:35:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8556n$moq$1@slb0.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net> <3ea5da3e.14353305@news.optonline.net>`

```
I think you will find that you get a compiler error if you try and mix "P"
and "Z" in the same picture clause (or you will get an extension flagging
message if your compiler allows it).

 P is valid in numeric fields (not edited)
Z (and ,) are valid in numeric-edited fields

The two cannot be mixed.

0 - is allowed in the picture of a numeric-edited field.


From page 214 of the 2002 Standard (which matches the meaning of the '85
Standard)

"11) To define an item as numeric, character-string-1
- shall include at least one symbol '9', and
- may contain a combination of symbols from the set 'P', 'S', and 'V'.

12) To define an item as numeric-edited, one of the following options shall
be specified:
a) To produce a fixed-point edited result, character-string-1 shall include:
- at least one symbol 'Z'; or
- at least one symbol '*'; or
- at least two identical symbols from the set '+', '-', currency symbol; or
- at least one symbol '9' and at least one of the symbols from the set 'B',
'CR', 'DB', '0', '/', ',', '.', '+', '-', the currency symbol."
```

###### ↳ ↳ ↳ Re: Numeric-Edited and PIC P (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-23T16:42:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea6b5f3.70607125@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net> <3ea5da3e.14353305@news.optonline.net> <b8556n$moq$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>I think you will find that you get a compiler error if you try and mix "P"
>and "Z" in the same picture clause (or you will get an extension flagging
>message if your compiler allows it).

Micro Focus, with FLAGSTD"H" and ANS85 on, did not complain. 

> P is valid in numeric fields (not edited)
>Z (and ,) are valid in numeric-edited fields
>
>The two cannot be mixed.

Page 331, section 13.16.41.5, of my proposed 2002 standard contains a precedence
chart for numeric-edited fields. It shows P. The text above discusses P used as
a floating insertion symbol. 

>From page 214 of the 2002 Standard (which matches the meaning of the '85
>Standard)
…[12 more quoted lines elided]…
>'CR', 'DB', '0', '/', ',', '.', '+', '-', the currency symbol."

I read that to say which symbols are required. It doesn't say others are
prohibited. 

------------------------------------------------------------------
I found the answer to my question about de-editing on page 393 eq seq. An edited
field _can_ be the sending operand of a MOVE, but not ADD. For example, this is
valid:

01  numeric-field         pic s9(9)v99.
01  edited-field           pic  z(9).99-.

move numeric-field to edited-field    *> editing
move edited-field to numeric-field    *> de-editing

Wierd. Forget UNSTRING, use PIC to do your parsing. 


--- history follows ---
>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ea5da3e.14353305@news.optonline.net...
…[114 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numeric-Edited and PIC P (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-23T12:36:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b86iuv$t8u$1@slb3.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net> <3ea5da3e.14353305@news.optonline.net> <b8556n$moq$1@slb0.atl.mindspring.net> <3ea6b5f3.70607125@news.optonline.net>`

```
I stand (sit, type) corrected.

The "Picture Precedence chart" (which is the final say on such things *does*
allow a "P" to be used with the numeric-editing symbols.  I have never seen
this used this way (and don't personally know exactly what it would do - any
more than I understand what would happen if the Standard allowed  using a
"V" or an "S" with a numeric-editing sign.

I plan to ask J4/WG4 about this.
```

###### ↳ ↳ ↳ Re: Numeric-Edited and PIC P (was: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-24T11:09:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea71d61_1@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net> <3ea5da3e.14353305@news.optonline.net> <b8556n$moq$1@slb0.atl.mindspring.net> <3ea6b5f3.70607125@news.optonline.net> <b86iuv$t8u$1@slb3.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b86iuv$t8u$1@slb3.atl.mindspring.net...
> I stand (sit, type) corrected.
>
> The "Picture Precedence chart" (which is the final say on such things
*does*
> allow a "P" to be used with the numeric-editing symbols.  I have never
seen
> this used this way (and don't personally know exactly what it would do -
any
> more than I understand what would happen if the Standard allowed  using a
> "V" or an "S" with a numeric-editing sign.
>
> I plan to ask J4/WG4 about this.

I agree that I have never seen it used this way, Bill. However, I've never
had occasion to use P anyway. (Like you, I did NOT consider it was an
editing character, rather a scaling factor.)

As to using V in an edited picture...

In the days of ICL 1900 COBOL (early seventies, for me) I remember that the
full stop was NOT a decimal alignment character (as it was in IBM COBOL at
the time). This meant that you needed to use a V AND a point if you wanted
alignment in an edited numeric picture. Like this:

1900 COBOL (XEKB, I think...)     = picture zzz,zzzV.99.
IBM DOS/VS COBOL  (I think...)  = picture zzz,zzz.99.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Numeric-Edited and PIC P (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-23T14:42:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304231342.3bffa80f@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net> <3ea5da3e.14353305@news.optonline.net> <b8556n$moq$1@slb0.atl.mindspring.net> <3ea6b5f3.70607125@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> I found the answer to my question about de-editing on page 393 eq seq. An edited
> field _can_ be the sending operand of a MOVE, but not ADD. For example, this is
…[8 more quoted lines elided]…
> Wierd. Forget UNSTRING, use PIC to do your parsing. 

In '85 standard de-editing only works if the data is correctly aligned
in the edited numeric field.  I believe that this restriction is
removed in '03 but haven't kept up with what is the current status.

MF has _always_ had (since CIS Cobol) the ability to do unaligned
de-editing:

         01  FX.
             03 FZ      PIC ------9.99.
         01  F9         PIC S9(8)V99.

     MOVE "1.2"     TO FX      (or ACCEPT FX AT col-pos)
     MOVE FZ        TO F9
     DISPLAY F9             -> +0000000120

You need a compiler directive DE-EDIT"1" for this feature.
```

###### ↳ ↳ ↳ Re: Numeric-Edited and PIC P (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-23T12:40:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304231140.65cf388f@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <b84b26$69t$1@slb5.atl.mindspring.net> <3ea5da3e.14353305@news.optonline.net> <b8556n$moq$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote 

> I think you will find that you get a compiler error if you try and mix "P"
> and "Z" in the same picture clause (or you will get an extension flagging
> message if your compiler allows it).
 
>  P is valid in numeric fields (not edited)
> Z (and ,) are valid in numeric-edited fields
 
> The two cannot be mixed.

Actually you can.  P may be in numeric or numeric edited.  It can be
used (eg) to suppress trailing digits to print 'thousands':  
Z,ZZZ,ZZ9PPPCR
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T15:34:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304221434.86b416c@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >Robert,
> >  What do you think about the COBOL *requirement* that a data item defined
…[9 more quoted lines elided]…
> >*never* seen your response to this.)
 
> When Richard posed the question, I responded it's not an integer. The test for
> integer is whether adding 1 will produce the next set member. 

The test for 'an integer' is whether it is a positive or negative
whole number - one that has no decimal part.  That is the only test,
that is all that is required.

If you want to use Set Theory (which is just one of the foundations of
maths) then the "Set of all Integers" has the characteristic that each
member is +1 away from some other member.  This defines that set.  It
is _of_ integers.

A subset of the set of all integers, such as [3, 5, 42] also consists
of integers.  The 3 members of that set are _also_ members of the set
of integers, they don't cease to be integers because they are in a
sub-set.  They don't become different things because they are also in
some sub-set.  They _are_ integers.

Similarly with [100, 200, 300, ..]. They don't cease to be integers
because this is a sub-set of the set of all integers.

In Set Theory if we wanted to get slightly more complex we could have
a set [1,2, 3.14159, red].  Those members that are also members of the
'set of all integers' are integers (by definition), the other members
are not integers because they are not in the 'set of all integers'.

When you finally read and understand what Set Theory is about, you
will see that your claims about it have been wrong.  Hopefully soon.

 
> I've always regarded pic P as an editing feature, intended for output. 

It _isn't_ and editing feature, it is a scaling feature.  While may be
used in an output specification, it is also used in a storage
specification.

> What happened to the unusual idea of permitting arithmetic on edited fields? 

You seem to base this question on the mistaken idea that 'P' makes it
an edited field.  It doesn't.  I suggest that you read the manual and
come back when you understand what is a numeric field and what is a
numeric edited.

> Was
> that in the 85 standard? The only use I could see was de-editing a report file
> for data recovery.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-23T03:58:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea5dcda.15020941@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>


>If you want to use Set Theory (which is just one of the foundations of
>maths) then the "Set of all Integers" has the characteristic that each
…[7 more quoted lines elided]…
>some sub-set.  They _are_ integers.

There is no such thing as subset in math. What you describe are intersecting
sets. 

>> What happened to the unusual idea of permitting arithmetic on edited fields? 
>
…[3 more quoted lines elided]…
>numeric edited.

I base it on:

 05  numeric-edited  pic zzz,zzz.99-.

 add 1 to numeric-edited
 move numeric-edited to plain-numeric

That used to be described in manuals, circa. 1985, which makes me think it was
in some standard. No compiler company would make up something this bazarre. 

>> Was
>> that in the 85 standard? The only use I could see was de-editing a report
file
>> for data recovery.
```

###### ↳ ↳ ↳ Sets (yet again) (Was: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-22T23:45:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b855pm$634$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net>`

```
Wrong Robert,
  Subsets versus intersecting sets are *not* identical terms in set theory.

For Set "X" to be a subset of Set "Y", it must be true that every member of
Set "X" is also a member of Set "Y".  No other conclusion may be derived.

Set "X" and Set "Y" form an *intersecting* Set "Z" if and only if every
member of set "Z" is also a member of Set "X" and also a member of Set "Y" -
see
  http://www.nist.gov/dads/HTML/intersection.html

A subset may be identical to the set of which it is a subset.  If this is
*not* true, then the subset is referred to as a "proper subset" - see:
  http://www.nist.gov/dads/HTML/propersubset.html

    ***

P.S. your *erroneous* statement

  "There is no such thing as subset in math."

may explain why you have such difficulty in understanding that the COBOL
definition allowing all whole numbers reflecting valid dates in the format
YYYYMMDD to be integers.  Such a "set" (the set of all integers in the
format YYYYMMDD where those form valid dates) *IS* a subset of the set of
all valid COBOL integers - and each individual member of that set *is* an
integer - although there are *other* integers valid in COBOL which are not a
member of this set (hence, it is "by definition" a PROPER SUBSET of the set
of all COBOL integers.  Similarly, the set of all COBOL integers is a proper
subset of ALL integers - as there are integers that are either too big or
too small to be represented in COBOL as integers.)
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-23T13:26:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b864a9$e2s$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net>`

```

On 22-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >A subset of the set of all integers, such as [3, 5, 42] also consists
> >of integers.  The 3 members of that set are _also_ members of the set
…[4 more quoted lines elided]…
> There is no such thing as subset in math.

cite?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-24T02:02:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea727a6.99718404@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 22-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[9 more quoted lines elided]…
>cite?

We all know 'you can't prove a negative.' 

Why do COBOL programmers have such an attachment to sub-this and sub-that? They
call (performable parameterless) local functions Subroutines. Now they refer to
Subprograms. When I started in the biz, it was common to have master files and
sub-master files. 

Seems to me fuzzy thinking, almost illiteracy. When they cannot describe
taxonomic structures, they call lower levels sub-something. It sounds
authorative, but it's meaningless.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-24T15:53:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b87n5u$tbh$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net>`

```
Robert Wagner wrote:


>>> There is no such thing as subset in math.
>>
>>cite?
> 
> We all know 'you can't prove a negative.'

No, but it is easy to prove that your claim about 'no subset' is quite 
wrong.

"""Subsets

Sets made up of some or all of the elements in the Universal set are called 
subsets.
"""

Any number of references will show this to be the case.
 
> Why do COBOL programmers have such an attachment to sub-this and sub-that?

Because it is a useful abstraction, something less than the whole.

> Seems to me fuzzy thinking, almost illiteracy. 

Is this a deliberate insult of all programmers designed to provoke flames ?

Or is it just more of your usual pomposity ?

> It sounds authorative, but it's meaningless.

How ironic that you say this.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-24T14:17:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b88rls$nlg$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net>`

```

On 23-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >> There is no such thing as subset in math.
> >
> >cite?
>
> We all know 'you can't prove a negative.'

That means "just because we can't find an example of something, doesn't prove
that something doesn't exist".    We agree on what it is we're looking for, but
we agree that we haven't yet found it.    We can say "no ants are larger than 6'
tall", and not be able to prove that statement.   But if we said "The Golden
Gate Bridge is not a building", then we don't examine the structure - we discuss
definitions.

In this case we're discussing semantics.   Mathematicians use the word "subset".
  You imply that they are misusing the word.   Does anybody else believe this?
 How are they misusing the word?   Is there some authority that has proclaimed
them wrong?


> Why do COBOL programmers have such an attachment to sub-this and sub-that?
> They
…[7 more quoted lines elided]…
> authorative, but it's meaningless.

We use these words because we think they have meaning, and we think we
understand what they mean.  (I never heard "sub-master file" though).    What
words should we have used that would REALLY have had meaning?   What word would
have meant what we thought subroutine meant?  If we had used your word, would
our communication have been improved?

If the person saying the word thinks the word means something and the person
hearing the word thinks it means the same thing - how do we determine that it
really is meaningless?
```

###### ↳ ↳ ↳ Re: System limits on ant sizes (was Accuracy/Knowledge score-card)

_(reply depth: 23)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-04-24T13:56:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0304241256.23597a5b@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b88rls$nlg$1@peabody.colorado.edu>...
> That means "just because we can't find an example of something, doesn't prove
> that something doesn't exist".    We agree on what it is we're looking for, but
…[4 more quoted lines elided]…
> 

Just to be picky, using Ants as an example wasn't a very good idea,
because ants are insects and their breathing system relies on air
diffusion through their exoskeleton rather than it being forcibly
pumped into internal organs such as gills or lungs.  Consequently,
there are limits to insect sizes in general and other similarly
organised animal orders.  While insect muscle action and movement does
asssist the diffusion by pumping to a certain extent, it's incapable
of supporting the large body sizes of certain other animal types. 
This is probably fortunate for us as insects are extremely successful
evolutionally and I certainly wouldn't want to meet a six foot ant.

Robert
```

###### ↳ ↳ ↳ Re: System limits on ant sizes (was Accuracy/Knowledge score-card)

_(reply depth: 24)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-25T09:53:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea85d0b_1@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <fcd09c56.0304241256.23597a5b@posting.google.com>`

```

"Robert Jones" <robert@jones0086.freeserve.co.uk> wrote in message
news:fcd09c56.0304241256.23597a5b@posting.google.com...
>
> Just to be picky, using Ants as an example wasn't a very good idea,
…[9 more quoted lines elided]…
>
My information is that the cockroaches are working on it...

In another 50 million years (a mere lunch break in cockroach time), it is
quite likely that a 6 foot cockroach wearing a three piece suit, will drive
his BMW to work at the Cockroach Stock Exchange on Cupboard street in the
cockroach city of  Roachhattan...

No Human will ever witness this, as we will have polluted or nuked ourselves
to death 45 million years before that...

Pete.



> Robert




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: System limits on ant sizes (was Accuracy/Knowledge score-card)

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-24T21:55:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8a4is$s89$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <fcd09c56.0304241256.23597a5b@posting.google.com>`

```
In article <fcd09c56.0304241256.23597a5b@posting.google.com>,
Robert Jones <robert@jones0086.freeserve.co.uk> wrote:
>"Howard Brazee" <howard@brazee.net> wrote in message news:<b88rls$nlg$1@peabody.colorado.edu>...

[snip]

>> We can say "no ants are larger than 6'
>> tall", and not be able to prove that statement.

[snip]

>Just to be picky, using Ants as an example wasn't a very good idea,
>because ants are insects and their breathing system relies on air
>diffusion through their exoskeleton rather than it being forcibly
>pumped into internal organs such as gills or lungs.

Just to be pickier... ants are as good as an example as any due to 
limitations imposed by the square-cube law and commented-upon by Galileo 
in 'Two New Sciences'.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-26T18:41:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaa9d7d.159664522@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 23-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

>We use these words because we think they have meaning, and we think we
>understand what they mean.  (I never heard "sub-master file" though).    What
>words should we have used that would REALLY have had meaning?   What word would
>have meant what we thought subroutine meant?  If we had used your word, would
>our communication have been improved?

I call subroutines: methods, paragraphs, called programs, nested programs (local
functions in C) or user-defined functions. That's what the COBOL standard calls
them as well. The word subroutine is too vague. 

>If the person saying the word thinks the word means something and the person
>hearing the word thinks it means the same thing - how do we determine that it
>really is meaningless?

If you said '.. next the program uses subroutine foo to figure out ...', I would
not know what the word means .. other than an out of line lump of code.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-26T16:11:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304261511.36949e10@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

RW>> Why do COBOL programmers have such an attachment to sub-this and
sub-that?
RW>> They call (performable parameterless) local functions
Subroutines.
RW>> Now they refer to Subprograms.
RW>> When I started in the biz, it was common to have master files and
RW>> sub-master files. 

> I call subroutines: methods, paragraphs, called programs, nested programs (local
> functions in C) or user-defined functions. That's what the COBOL standard calls
> them as well. The word subroutine is too vague. 

This is called a 'straw man argument'.  You assert that programmers
call things 'subroutines' and then criticise the use of the word.

In fact you go further and claim that _you_ use the word for several
different things and then criticise _us_ because the word is 'too
vague'.

'Subprogram' is defined in Cobol as being a CALLed program. whether
this is nested or separately compiled.

A 'subroutine' is any 'routine' that is a self-contained part of a
complete program. Whether it is a performed paragraph or a CALLed
subprogram, or some other is an implementation detail that is only
useful to a coder.
 
> If you said '.. next the program uses subroutine foo to figure out ...', I would
> not know what the word means .. other than an out of line lump of code.

That is _exactly_ what it means - an out of line lump of code, with no
specific implementation mechanism defined, so you _do_ understand.

There is often no need to clutter up an issue with irrelevancies such
as implementation details.

But then you were thinking like a coder.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-27T14:56:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eabeef6.246070121@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <217e491a.0304261511.36949e10@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>There is often no need to clutter up an issue with irrelevancies such
>as implementation details.
>
>But then you were thinking like a coder.

You got something against coders? The room is full of them.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-28T13:01:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304281201.64ee9f5f@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <217e491a.0304261511.36949e10@posting.google.com> <3eabeef6.246070121@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >But then you were thinking like a coder.
> 
> You got something against coders?  

I have nothing against coders at all, whatever gave you that idea ?

> The room is full of them.

Are they Cobol Programmers ?  Do you voice your opinions to them ?  Do
you repititiously inform them of how much better your ideas are then
theirs ? Or do they just tell the old dinosaur to piss off ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-29T03:51:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eadd058.369322672@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <217e491a.0304261511.36949e10@posting.google.com> <3eabeef6.246070121@news.optonline.net> <217e491a.0304281201.64ee9f5f@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[4 more quoted lines elided]…
>I have nothing against coders at all, whatever gave you that idea ?

Because you use the word in disparagement, as quoted above. 

>> The room is full of them.
>
>Are they Cobol Programmers ?  

Yes.

>Do you voice your opinions to them ?

Yes.

> Do you repititiously inform them of how much better your ideas are then
>theirs ? 

No longer. I let them judge for themselves

>Or do they just tell the old dinosaur to piss off ?

I don't go out of my way to. If he tells me to piss off, I retaliate in like
kind.

If he feels 'insulted' by my criticism of a whole culture (not personal), he
should defend it as best he can .. or not.
```

###### ↳ ↳ ↳ What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-27T13:36:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8h80g$av1$1@slb6.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eaa9d7d.159664522@news.optonline.net...
<snip>
>
> I call subroutines: methods, paragraphs, called programs, nested programs
(local
> functions in C) or user-defined functions. That's what the COBOL standard
calls
> them as well. The word subroutine is too vague.
>

1) user-defined functions and methods are *not* part of any COBOL Standard
before the 2002 Standard, so this claim (about "what the cCOBOL standard
calls them")  must have been made about that Standard - not an earlier one.

2) The 2002 Standard uses the word "subroutine" *exactly* once - and that is
in the "informative" (not normative) CONCEPTS annex, in the sentece,
  "A method is procedural code that defines a specific function required by
all of the instances of a class. A method may be thought of as a module or
subroutine."

3) Paragraphs and sections are *never* (in this or any previous Standard)
"lumped" in with programs (nested, or separate).  They are (and have always
been) called "procedures".

4) The "generic" term for programs, methods, and  functions in the 2002
Standard (at run-time) is in the glossary as:
     " 4.2 activated runtime element: A function, method, or program placed
into the active state."
and you can see from this definition, there is no "generic" term for
"program, method, and function" when not talking about it at runtime.

5) The term "subprogram" appears frequently in the 2002 Standard - and is
(correctly) limited to PROGRAMS (not functions or methods) that are
"activated" from another runtime element (which may be a program, method, or
function)

6) If one wants more information on the 2002 Standard acceptable "elements"
of a compilation group, they should read,

     "10.4 Source elements and runtime elements"

starting on page 169

    ***

Bottom-Line:
   Some COBOL programmerss may (or may not) use the term "subroutine" - but
that is certainly NOT a generic term used in the 2002 COBOL Standard.
```

###### ↳ ↳ ↳ Re: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-28T01:26:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eac4c17.269914533@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[7 more quoted lines elided]…
>> them as well. The word subroutine is too vague.

>3) Paragraphs and sections are *never* (in this or any previous Standard)
>"lumped" in with programs (nested, or separate).  They are (and have always
>been) called "procedures".

While the standard doesn't lump them together, programmers refer to both
procedures and called programs as subroutines.

>Bottom-Line:
>   Some COBOL programmerss may (or may not) use the term "subroutine" - but
>that is certainly NOT a generic term used in the 2002 COBOL Standard.

Thank you.
```

###### ↳ ↳ ↳ Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-27T22:11:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8i654$tdr$1@slb9.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net>`

```
I'm curious (and I fully expect this to be something that is NOT universal -
one way or another),

RW states below

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eac4c17.269914533@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
<snip>
>
> >3) Paragraphs and sections are *never* (in this or any previous Standard)
> >"lumped" in with programs (nested, or separate).  They are (and have
always
> >been) called "procedures".
>
> While the standard doesn't lump them together, programmers refer to both
> procedures and called programs as subroutines.
>
  <snip>

I do NOT recall hearing many programmers refer to both paragraphs/sections
*and* called programs (nested or non-nested) as "subroutines".  How many
COBOL programmers (reading this NG - which may or may not be very
"representative") do use this same term when referring to both types of
COBOL source code?

If  *I* heard the term "subroutine" used in a COBOL context, I would have
assumed the person were talking about "subprograms".  What would others
think when they heard/used this term?
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-04-28T07:37:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EACDA9F.21EF044@worldnet.att.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net>`

```
"William M. Klein" wrote:
> (snip)
> I do NOT recall hearing many programmers refer to both paragraphs/sections
…[7 more quoted lines elided]…
> think when they heard/used this term?

When I use the term "subroutine", I am referring to a performed
paragraph.  But then I work in an IBM mainframe COBOL shop that does
not use procedure division sections or declaratives.

When I use the term "subprogram", I am referring to the target of a
CALL statement, even if the subprogram is nested (which is also
unheard of in my shop).

When I use the term "function", I am referring to COBOL standard
intrinsic functions.  I don't think we have the ability to write
user-defined functions yet.  Even if we did, I wouldn't expect to see
them adopted anytime soon.  Not because there's anything wrong with
them, but the COBOL programmers I see don't seem to be too eager to
try out new features.  Even with the standard intrinsic functions, we
seem to use only the date functions.

And I'm not saying my usage is "correct", it's just what I'm used to.  
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-04-28T09:00:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ebnpav8svg4j5jaqbve2pclcuucrgf7rv4@4ax.com>`
- **References:** `<3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net>`

```
On Sun, 27 Apr 2003 22:11:18 -0500, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>I'm curious (and I fully expect this to be something that is NOT universal -
>one way or another),
…[26 more quoted lines elided]…
>think when they heard/used this term?
I would normally use the term "routine" or "subroutine" to reference
pieces of code (normally a paragraph that can perform others and/or
call other programs) e.g if for example I perform a paragraph
"txx-get-table-record" this paragraph will in turn perform/call a set
of different paragraphs to 1-Load the table entries in memory (if not
loaded already), 2-do a binary search on the loaded table and 3-return
the record or an error if no record found.

I don't normally use the term "subprogram" as many of my programs can
be called either as "main" or as from another program, so it would not
make much sense calling them "sub's". 
I would never call them subroutines though.

FF
Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-28T02:05:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304280105.d60c10b@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote 

> If  *I* heard the term "subroutine" used in a COBOL context, I would have
> assumed the person were talking about "subprograms".  What would others
> think when they heard/used this term?

I would assume no specific implementation, just a block of conceptual
code that may be wrapped as a subprogram or as a procedure or even a
method.

Because Cobol makes no specific definition of this term, in fact
hardly mentions it, one falls back on common usage such as may be
found in the Penguin Dictionary of Computers:

"Subroutines are a self-contained section of a program that may be
incorporated into a complete program ..."
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-28T21:12:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eacf098_2@127.0.0.1>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b8i654$tdr$1@slb9.atl.mindspring.net...
> I'm curious (and I fully expect this to be something that is NOT
universal -
> one way or another),
>
…[4 more quoted lines elided]…
>

If a programmer referred to "subroutines", in a conversation with me, I
would believe he was talking about performed paragraphs/sections  within a
program.

If he said "books" I would know he was referring to source code included in
COBOL.

If he said "modules" I would know he was referring to either called programs
or nested programs (not necesarily in executable form, but certainly in
object form).

If he said "core images" or executables, I would know he was referring to
completely linked "standalone" programs that can be executed.

If he said "Classes" I would know he was referring to applications developed
in OO.

If he said "Objects" I would know he was referring to specific instances of
an OO Class.

If he said "Components" I would know he was talking about Objects that can
run anywhere and are wrapped as COM (or Java Beans)

If he said "Web Service" I would know he was talking about components on a
Web Server accessible from anywhere on Earth 24/7.

If SHE said any of the above, I wouldn't be listening...I'd be checking out
her cleavage and deciding what the chances were of dinner tonight. Besides,
women shouldn't be allowed near technology...apart from YukonMama, who has
demonstrated that she is wise and understands the limits of Political
Correctness...<G>

Pete.


> --
> Bill Klein
>  wmklein <at> ix.netcom.com
>
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 28)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-05-04T07:12:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030504031239.01745.00000512@mb-m28.aol.com>`
- **References:** `<3eacf098_2@127.0.0.1>`

```
>From: "Peter E.C. Dashwood" dashwood@enternet.co.nz 
>Date: 4/28/03 5:12 AM Eastern Daylight Time

>If SHE said any of the above, I wouldn't be listening...I'd be checking out
>her cleavage and deciding what the chances were of dinner tonight. Besides,
…[5 more quoted lines elided]…
>

LOL!!

Pete dahlink - I'll by you dinner if you ever wander into my neck of the woods
:)

Now as to the question.  I had to think on this one because I've heard the term
used for both CALLED programs and performed paragraphs about 50/50, and I think
I've used the term myself about 50/50 probably depending on how the original
speaker used it.  If I was to initiate the conversation how I would use it
would depend on what was being discussed.   Ok - that sounds convoluted so let
me put it this way...

If I was refering to a paragraph or set of paragraphs that were in a copybook
in the program I'd call it a subroutine because it was in a copybook because it
was used all over.  Then in the next program there is a called program that is
used all over and it is refered to as a subroutine.  Go figure.  Anyway a lot
of our called programs were once copybooks until someone decided to make them a
called program because if they had to change they wouldn't have to recompile
all the programs that used the copybook hence that is probably why the called
program is called a subroutine.
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 29)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-05-04T16:05:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cTata.27413$8e7.1133596@twister.austin.rr.com>`
- **References:** `<3eacf098_2@127.0.0.1> <20030504031239.01745.00000512@mb-m28.aol.com>`

```
LOL! That sounds like a familiar circumstance. : )

Right now I am figuring out how to port code from WangVS (sort of like an
ancient
VM running on a 370,with some cool additions like AS/400 style workstation
management,
using 3270 like data streams instead of 5250... well, you get the idea... :)
:)

The point is we are used to mainframe style meanings for CALL and LINK. But
UNIX does not have the same concept of a Load Module that the mainframe
does. (It does have the concept of Windows like DLLs, and shared libraries
and all that, but it is much more complex than under say, OS/390.)

Essentially, try explaining that every module that will be executed from the
OS needs to have an entry point called "main" and that all the CALLed
modules need to be link edited together. It is a bit of mind bender. Then
try to figure out what to call a CALLed module that is being link edited
together and called exactly like any other subroutine... <grin>

-Paul


"YukonMama" <yukonmama@aol.com> wrote in message
news:20030504031239.01745.00000512@mb-m28.aol.com...
> >From: "Peter E.C. Dashwood" dashwood@enternet.co.nz
> >Date: 4/28/03 5:12 AM Eastern Daylight Time
>
> >If SHE said any of the above, I wouldn't be listening...I'd be checking
out
> >her cleavage and deciding what the chances were of dinner tonight.
Besides,
> >women shouldn't be allowed near technology...apart from YukonMama, who
has
> >demonstrated that she is wise and understands the limits of Political
> >Correctness...<G>
…[6 more quoted lines elided]…
> Pete dahlink - I'll by you dinner if you ever wander into my neck of the
woods
> :)
>
> Now as to the question.  I had to think on this one because I've heard the
term
> used for both CALLED programs and performed paragraphs about 50/50, and I
think
> I've used the term myself about 50/50 probably depending on how the
original
> speaker used it.  If I was to initiate the conversation how I would use it
> would depend on what was being discussed.   Ok - that sounds convoluted so
let
> me put it this way...
>
> If I was refering to a paragraph or set of paragraphs that were in a
copybook
> in the program I'd call it a subroutine because it was in a copybook
because it
> was used all over.  Then in the next program there is a called program
that is
> used all over and it is refered to as a subroutine.  Go figure.  Anyway a
lot
> of our called programs were once copybooks until someone decided to make
them a
> called program because if they had to change they wouldn't have to
recompile
> all the programs that used the copybook hence that is probably why the
called
> program is called a subroutine.
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T14:40:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jeh0$cf8$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net>`

```

On 27-Apr-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> I do NOT recall hearing many programmers refer to both paragraphs/sections
> *and* called programs (nested or non-nested) as "subroutines".  How many
> COBOL programmers (reading this NG - which may or may not be very
> "representative") do use this same term when referring to both types of
> COBOL source code?

I use it both ways.   I generally use it to mean something like a canned
procedure, sometimes in a copy member, sometimes in its own program.   I don't
use it to describe a print paragraph.

But I don't use the term a lot with CoBOL.
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 27)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-04-29T01:32:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DCkra.42274$q02.1750629@twister.austin.rr.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:b8i654$tdr$1@slb9.atl.mindspring.net...
> I'm curious (and I fully expect this to be something that is NOT universal -
> one way or another),
…[27 more quoted lines elided]…
>

Subroutine usually means a paragraph that is performed to me, but it also means object modules that are searched
during link-edit steps; we use subroutine libraries. It makes it easy to call the same routine from CICS or BATCH.

Subprograms, at least as pertains to COBOL, are equivalent to "modules" to me.
```

###### ↳ ↳ ↳ Re: Time to vote <G> (was: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 28)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-04-29T03:34:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c30e00$25dc76a0$1591f243@chottel>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net> <b8i654$tdr$1@slb9.atl.mindspring.net> <DCkra.42274$q02.1750629@twister.austin.rr.com>`

```
To me subroutine means FORTRAN probably because it was my first language
and they used that term a lot.

Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote in article
<DCkra.42274$q02.1750629@twister.austin.rr.com>...
> 
> "William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b8i654$tdr$1@slb9.atl.mindspring.net...
> > I'm curious (and I fully expect this to be something that is NOT
universal -
> > one way or another),
> >
…[7 more quoted lines elided]…
> > > >3) Paragraphs and sections are *never* (in this or any previous
Standard)
> > > >"lumped" in with programs (nested, or separate).  They are (and have
> > always
> > > >been) called "procedures".
> > >
> > > While the standard doesn't lump them together, programmers refer to
both
> > > procedures and called programs as subroutines.
> > >
> >   <snip>
> >
> > I do NOT recall hearing many programmers refer to both
paragraphs/sections
> > *and* called programs (nested or non-nested) as "subroutines".  How
many
> > COBOL programmers (reading this NG - which may or may not be very
> > "representative") do use this same term when referring to both types of
> > COBOL source code?
> >
> > If  *I* heard the term "subroutine" used in a COBOL context, I would
have
> > assumed the person were talking about "subprograms".  What would others
> > think when they heard/used this term?
> >
> 
> Subroutine usually means a paragraph that is performed to me, but it also
means object modules that are searched
> during link-edit steps; we use subroutine libraries. It makes it easy to
call the same routine from CICS or BATCH.
> 
> Subprograms, at least as pertains to COBOL, are equivalent to "modules"
to me.
> 
> 
>
```

###### ↳ ↳ ↳ Re: What does the COBOL Standard call them? (was: Accuracy/Knowledge score-card

_(reply depth: 26)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-27T23:26:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304272226.306d41a6@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864a9$e2s$1@peabody.colorado.edu> <3ea727a6.99718404@news.optonline.net> <b88rls$nlg$1@peabody.colorado.edu> <3eaa9d7d.159664522@news.optonline.net> <b8h80g$av1$1@slb6.atl.mindspring.net> <3eac4c17.269914533@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> While the standard doesn't lump them together, programmers refer to both
> procedures and called programs as subroutines.

I am not sure if you are claiming _all_ programmers, or just the ones
in the same office as you, or that one programmer used it once 20
years ago.

Perhaps they know you object to this and use it deliberately to annoy
you.

Quite frankly it isn't a problem to me whether they use this term or
not.

If this is a problem for you, then the next time you find some
programmer doing this why don't you hold your breath until they change
to using some term that is Wagner-approved(tm).
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-23T13:29:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b864f6$e32$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net>`

```

On 22-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >You seem to base this question on the mistaken idea that 'P' makes it
> >an edited field.  It doesn't.  I suggest that you read the manual and
…[11 more quoted lines elided]…
> in some standard. No compiler company would make up something this bazarre.

I've never seen that.   I doubt if I worked with a compiler where that would
work (but I don't always try "impossible" code).

But I am missing the connection between your explanation and his paragraph.  
You are basing your conclusion about the "P" upon a description that does not
mention "P"?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-24T02:02:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea72b47.100647216@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <b864f6$e32$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 22-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[13 more quoted lines elided]…
>> That used to be described in manuals, circa. 1985, which makes me think it
was
>> in some standard. No compiler company would make up something this bazarre.
>
…[5 more quoted lines elided]…
>mention "P"?

I've since sorted it out. See my reply to WMK.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-23T12:07:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b86dnc$4ib$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <3ea5dcda.15020941@news.optonline.net>`

```
In article <3ea5dcda.15020941@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:

[snip]

>There is no such thing as subset in math.

Mr Wagner, most of the sources which did not support your definition of
integer do not support this assertion, either.

http://mathworld.wolfram.com/Subset.html

http://www.wikipedia.org/wiki/subset

http://www.cut-the-knot.org/do_you_know/few_words.shtml (under Subgroup)

http://www.bartleby.com/61/9/S0850900.html

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-24T02:02:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea72bd7.100791479@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <3ea5dcda.15020941@news.optonline.net> <b86dnc$4ib$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3ea5dcda.15020941@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[14 more quoted lines elided]…
>http://www.bartleby.com/61/9/S0850900.html

That means you win. Celebrate your victory by taking someone you love out to
dinner, during which you can brag about your accomplishment.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-23T22:30:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b87i7f$akt$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <b86dnc$4ib$1@panix1.panix.com> <3ea72bd7.100791479@news.optonline.net>`

```
In article <3ea72bd7.100791479@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[18 more quoted lines elided]…
>That means you win.

Mr Wagner, I have stated before that 'if something new is learned then all 
involved 'win'.'; my views have not changed in the interceding days.

>Celebrate your victory by taking someone you love out to
>dinner, during which you can brag about your accomplishment. 

This suggestion will be given all the consideration it deserves.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-24T16:06:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b87nv2$tm4$2@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <b86dnc$4ib$1@panix1.panix.com> <3ea72bd7.100791479@news.optonline.net>`

```
Robert Wagner wrote:

> That means you win. Celebrate your victory by 

'Winning' is not difficult, the victory is getting you to admit you were 
wrong instead of your usual deflection, dismissal, or just claiming the 
argument was a different one.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-23T13:08:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304231208.63801cf7@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >A subset of the set of all integers, such as [3, 5, 42] also consists
> >of integers.  The 3 members of that set are _also_ members of the set
…[5 more quoted lines elided]…
> sets. 

<sigh> Of course there are subsets, a set where all the members are
contained within another set is a subset.  An intersecting set is
where some members are contained in another set, and some not.

        [3,5,42] is a subset of integers
        [3,5,42,red,cow] has an intersect with integers

Of course this difficulty that are having with this and with other
simple concepts such as infinity explains why you have no proper
understanding of 'integers'.

> >You seem to base this question on the mistaken idea that 'P' makes it
> >an edited field.  It doesn't.  I suggest that you read the manual and
…[8 more quoted lines elided]…
>  move numeric-edited to plain-numeric

And this has _what_ to do with 'P' ?
 
> That used to be described in manuals, circa. 1985, which makes me think it was
> in some standard. No compiler company would make up something this bazarre. 

Yet more of your misunderstanding from nearly 20 years ago no doubt.

While you _can_ move from edited numeric to numeric to recover the
value (ie the de-editing move in your two lines above) you cannot do
arithmetic on edited numeric.  For the move to work in '85 Cobol the
value must be properly aligned.  MF has an extension for non-aligned
de-editing.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-24T02:02:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea72e9b.101499112@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[18 more quoted lines elided]…
>understanding of 'integers'.

I don't respond to flames. 

>> >You seem to base this question on the mistaken idea that 'P' makes it
>> >an edited field.  It doesn't.  I suggest that you read the manual and
…[12 more quoted lines elided]…
>> That used to be described in manuals, circa. 1985, which makes me think it
was
>> in some standard. No compiler company would make up something this bazarre. 
>
>Yet more of your misunderstanding from nearly 20 years ago no doubt.

[Hoping repetition will make the point] I don't respond to flames.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-23T22:34:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b87igd$bks$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <3ea72e9b.101499112@news.optonline.net>`

```
In article <3ea72e9b.101499112@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>riplin@Azonic.co.nz (Richard) wrote:

[snip]

>>Of course this difficulty that are having with this and with other
>>simple concepts such as infinity explains why you have no proper
>>understanding of 'integers'.
>
>I don't respond to flames. 

Mr Wagner, in that what you did here constitutes a reaction you just
did... or is respond with 'I don't respond' somehow not a response?

[snip]

>>Yet more of your misunderstanding from nearly 20 years ago no doubt.
>
>[Hoping repetition will make the point] I don't respond to flames. 

Mr Wagner, repeating your error (said error being that you are, by 
definition, responding) might make a point, true... but some might not 
consider it to reflect favorably upon you.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-24T16:03:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b87npj$tm4$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <3ea72e9b.101499112@news.optonline.net>`

```
Robert Wagner wrote:

>>Of course this difficulty that are having with this and with other
>>simple concepts such as infinity explains why you have no proper
>>understanding of 'integers'.
> 
> I don't respond to flames.

I shall use the fact that you responded as evidence that it is not a flame.

But, no, it is not a flame at all.  It is an observation.

>>> That used to be described in manuals, circa. 1985, which makes me think
>>> it was
>>> in some standard. No compiler company would make up something this
>>> bazarre. 

>>Yet more of your misunderstanding from nearly 20 years ago no doubt.

> [Hoping repetition will make the point] 

It has been noticed that you frequently try 'proof by repitition' as a 
substitute for rebuttal.

> I don't respond to flames.

Once again, it is not a flame, it is an observation. 'Circa 1985' is nearly 
20 years ago.  'add 1 to edited-numeric' is an obvious misunderstanding of 
what the manual actually said.  'Yet more' is another of several times that 
you have related 'learning' some mis-information decades ago.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 23)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-26T03:31:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea9f918.117573082@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <3ea72e9b.101499112@news.optonline.net> <b87npj$tm4$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:


>>>> That used to be described in manuals, circa. 1985, which makes me think
>>>> it was
…[3 more quoted lines elided]…
>>>Yet more of your misunderstanding from nearly 20 years ago no doubt.

Turns out it is au courant. COBOL 2002 supports 'de-edititing'.

>It has been noticed that you frequently try 'proof by repitition' as a 
>substitute for rebuttal.

You have me confused with someone else. Howard Brazee tried that when we
discussed periods. He posted at least 20 repititious messages, then got pissed
because no one responded to them.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-26T12:22:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304261122.32cc86ef@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <3ea72e9b.101499112@news.optonline.net> <b87npj$tm4$1@aklobs.kc.net.nz> <3ea9f918.117573082@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >>>> That used to be described in manuals, circa. 1985, which makes me think
> >>>> it was
…[5 more quoted lines elided]…
> Turns out it is au courant. COBOL 2002 supports 'de-edititing'.

As you had been told, 'de-editing' is in the '85 standard.  You
misunderstanding was that you could do arthimetic operations on
edited-numeric, as was clearly in the message.
 
> >It has been noticed that you frequently try 'proof by repitition' as a 
> >substitute for rebuttal.
> 
> You have me confused with someone else. 

No. Your memory must be very selective, or just lost.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-26T20:35:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaae949.179070957@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <3ea72e9b.101499112@news.optonline.net> <b87npj$tm4$1@aklobs.kc.net.nz> <3ea9f918.117573082@news.optonline.net> <217e491a.0304261122.32cc86ef@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[11 more quoted lines elided]…
>edited-numeric, as was clearly in the message.

I looked it up and corrected myself here BEFORE you or WMK answered my question.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 24)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-28T14:48:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jevb$ci1$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <3ea72e9b.101499112@news.optonline.net> <b87npj$tm4$1@aklobs.kc.net.nz> <3ea9f918.117573082@news.optonline.net>`

```

On 25-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> You have me confused with someone else. Howard Brazee tried that when we
> discussed periods. He posted at least 20 repititious messages, then got pissed
> because no one responded to them.

I deny this accusation.

My messages were responses to other messages and what I perceived as insults.  
I gave reasons for not considering "eliminating periods" to be how to fix bad
code, but when Robert Wagner kept repeating his mantra, I kept repeating my
addendum - so that new programmers won't assume that everybody agrees with him,
and that his way is The One True Way.

But the quoted message above is about the 4th time he has made that accusation
since the original thread died.
```

###### ↳ ↳ ↳ De-Editing (was: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-25T23:08:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8d0ou$a46$1@slb2.atl.mindspring.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com>`

```
(clarification below)

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304231208.63801cf7@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote
>
<snip>
>
> > >You seem to base this question on the mistaken idea that 'P' makes it
…[13 more quoted lines elided]…
> > That used to be described in manuals, circa. 1985, which makes me think
it was
> > in some standard. No compiler company would make up something this
bazarre.
>
> Yet more of your misunderstanding from nearly 20 years ago no doubt.
…[5 more quoted lines elided]…
> de-editing.

1) The '85 Standard *did* introduce "numeric de-editing" which allows one to
move a numeric-edited field to a numeric field. This is described in
"Substantive Change (78) on page XVII-47 on the '85 Standard - where it
states,

"78) MOVE statement (2 NUC). A numeric edited data item may be moved to a
numeric or numeric edited data item; thus de-editing takes place."

2) In the '85 Standard (and I don't know if this was new there or not) it is
totally legal to have a numeric-edited item as a RECEIVING item, but not as
a sending item in an arithmeric statement.  Furthermore, if the same operand
is both a sending and receiving item, then it may NOT be numeric-edited -
only numeric.  This has *nothing* to do with "numeric de-editing" as the
sending item is never edited.  See for example SR(1) of the ADD statement on
page VI-73

which states,

"(1) In formats 1 and 2, each identifier must refer to an elementary numeric
item, except that in format 2 each identifier following the word GIVING must
refer to either an elementary numeric item or an elementary numeric edited
item."

This means that source code such as the following  - listed above (with all
the required "stuff" around it)

05  numeric-edited  pic zzz,zzz.99-.

  add 1 to numeric-edited

is *NOT* ANSI/ISO conforming (according to the '85 Standard) and should
receive a compiler error message or extension flagging message - while the
following similar statement would not

05 num   pic S9(6)V99.
05  numeric-edited  pic zzz,zzz.99-.

  add 1 to Num Giving numeric-edited

3) I was in error (in another part of this related thread) when I thought
that having "P" (or even "V") in a numeric-edited field was non-conforming.
The '85 Standard (and continued in the 2002 Standard) *does* allow this.
Furthermore, the rules for "numeric-de-editing" of numeric-edited fields
that contain a "P" *require* that the "numeric value" used includes the
"implicit zeros and decimal point" in determining the value of the sending
field.  HOWEVER, simply having "P" "S" and "9" in a data description (with
no other characters and no BLANK WHEN ZERO clause) *does* specify a numeric
rather than numeric-edited field.  Again, when a numeric-edited field
contains a "P" in its PICTURE clause, it may be used as a receiving field
but not a sending field in an ARITHMETIC statement.

    ***

I hope this adds a little clarification on this topic.

P.S.  The only "major" enhancement related to any of this in the 2002
Standard (and it isn't directly related to this) is the ability to use a
numeric (or integer) intrinsic function wherever a numeri (or integer)
sending operand is allowed - while in the '89 Amendment these could only be
used in arithmetic expressions.
```

###### ↳ ↳ ↳ Re: De-Editing (was: Accuracy/Knowledge score-card

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-26T20:12:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaadc1c.175697989@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7iout$7ki$1@slb6.atl.mindspring.net> <3e9e0532.279483210@news.optonline.net> <b8114f$10u$1@peabody.colorado.edu> <3ea4a510.273903349@news.optonline.net> <b82bnp$aqh$1@slb1.atl.mindspring.net> <3ea565f1.323288205@news.optonline.net> <217e491a.0304221434.86b416c@posting.google.com> <3ea5dcda.15020941@news.optonline.net> <217e491a.0304231208.63801cf7@posting.google.com> <b8d0ou$a46$1@slb2.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>2) In the '85 Standard (and I don't know if this was new there or not) it is
>totally legal to have a numeric-edited item as a RECEIVING item, but not as
…[4 more quoted lines elided]…
>page VI-73

I already acknowledged that:

>I found the answer to my question about de-editing on page 393 eq seq.
>An edited field _can_ be the sending operand of a MOVE, but not ADD.

Thank you for researching and posting relevant sections from the standard.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-16T17:19:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ip7p$76a$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net>`

```
Robert Wagner wrote:

RW >>> A date is an ordinal;

RP >>No.  A date in the form 20030415 is not an ordinal.

> You're correct. But when the whole date is returned as an 'integer', it is
> not. 

So, having claimed that a date is an ordinal, you now agree that it is not.

>>> An integer, which derives from entire,
>>> specifies an ordinal set with no holes in
…[6 more quoted lines elided]…
> to DD.

You confuse the container with the content.  While a computer field of a 
certain type may be limited to holding integers and the range of these may 
be limited, this does not mean that 'an integer' implies a range.

It certainly does not imply in any way that all possible values must be 
used so that there are 'no holes'.

In any case, trying to twist 'An integer' into the context of 'computer 
integer' just doesn't work.  it is just another attempt of yours that when 
losing an argument you try to change it.
 
>>An 'integer' is just the representation of digits _without_ a
>>fractional or decimal part.
>>
>>A number 20030415 is an integer for the very simple reason that it is
>>a whole number without any fractional or decimal component.
 
> Now who's thinking like a 'coder'? Just because it it numeric doesn't make
> it an integer. 

Simple numbers are divided into two groups: integer and real.  If it is a 
number then it is either an integer or a real number. 

> No more than a ZIP code or social security number or part
> number.

If it is a _number_ then it is either ...

Perhaps you meant ".. ZIP code or social security _identification_ or part 
_code_ ...".

Text strings may consist of characters that are also numeric digits, it is 
incorrect to call them 'numbers'.

In the past we (or some of we) used numbers - integers - for part codes and 
customer codes, they really were part numbers and customer numbers.  They 
had check digits so that mispunchings could be tossed out before being 
checked.  We produced pages of unused valid numbers for new accounts and 
new parts by adding some offset and checking it wasn't invalid and didn't 
exist already.

These were integers (no decimal or fractional part) and had 'holes' in the 
range.

If you say "part number" then it may be taken as being a number.  If you 
use "part code" or SKU then it is just text.

Now SSNs may or may not be numbers, I won't take your word for it.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-17T00:07:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9de228.270511429@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[7 more quoted lines elided]…
>So, having claimed that a date is an ordinal, you now agree that it is not.

On second thought, I retract my agreement. I was concentrating on IN THE FORM OF
an integer. A date in that form isn't an integer, it is collection of three
integers. Now I realize that collections can indeed be ordinals in the set of
'all dates'. There are three levels here -- all dates, collections and integral
components of a date. 

>>>> An integer, which derives from entire,
>>>> specifies an ordinal set with no holes in
…[10 more quoted lines elided]…
>be limited, this does not mean that 'an integer' implies a range.

It is a member of a set defined by a range. The defining concept here is set,
the container.

>It certainly does not imply in any way that all possible values must be 
>used so that there are 'no holes'.

Yes it does. Look up the defininition of integer on any math site -- NOT a
dictionary or computer lingo site. 

>In any case, trying to twist 'An integer' into the context of 'computer 
>integer' just doesn't work.  it is just another attempt of yours that when 
>losing an argument you try to change it.

The only twist I added was cardinalization -- the recognition that infinity is
impossible in a computer. Otherwise, my definition is mathematically sound ..
and a lot better than we get from computer language people. 

>>>An 'integer' is just the representation of digits _without_ a
>>>fractional or decimal part.
…[8 more quoted lines elided]…
>number then it is either an integer or a real number. 

Rubbish. See previous. Computer variables are divided into three groups (sounds
like "omnes Galaii est divista in tres partes", opening line for Caesar's Gaelic
Wars). There are fixed point numbers, floating point numbers and strings. I wish
computer language designers would just call 'em that rather than misusing math
terminology. 

>Perhaps you meant ".. ZIP code or social security _identification_ or part 
>_code_ ...".

What do you propose we substitute for 'telephone number'? Telephone station id?
POTS subscriber address? They all seem awkward. 

>Text strings may consist of characters that are also numeric digits, it is 
>incorrect to call them 'numbers'.

Agreed. I have _always_ used strings for dates. I have never cast them as
integers. If the language doesn't provide a suitable type, it should be a
string. 

>In the past we (or some of we) used numbers - integers - for part codes and 
>customer codes, they really were part numbers and customer numbers.  They 
…[6 more quoted lines elided]…
>range.

In that case they weren't integers. They were 'numbers'. 

>If you say "part number" then it may be taken as being a number.  If you 
>use "part code" or SKU then it is just text.
>
>Now SSNs may or may not be numbers, I won't take your word for it.

US SSNs are numeric, do not have a check digit, and are doled out to States in
blocks. Some values in the block are never used, thus they are not integers.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T01:47:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304170047.2cd86d98@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >So, having claimed that a date is an ordinal, you now agree that it is not.
> 
…[4 more quoted lines elided]…
> components of a date. 

A date of the form 20030415 is not _an_ ordinal, it is a collection of
3 ordinals. A 'collection' cannot be _an_ ordinal.

But as a number it _is_ an integer.

> It is a member of a set defined by a range. The defining concept here is set,
> the container.

If the defining concept is the set, the container, then any value that
can be contained in an integer field, say PIC S9(8) must be an
integer, eg 20030415.

> Yes it does. Look up the defininition of integer on any math site -- NOT a
> dictionary or computer lingo site. 

Having looked at some I cannot find any such, please point the way.

> >Simple numbers are divided into two groups: integer and real.  If it is a 
> >number then it is either an integer or a real number. 
> 
> Rubbish. See previous. Computer variables are divided into three groups 

You keep switching.  I didn't say 'computer storage' I said 'numbers'.

> What do you propose we substitute for 'telephone number'? Telephone station id?
> POTS subscriber address? They all seem awkward. 

Not at all.  Telephone numbers _are_ numbers.
 
> Agreed. I have _always_ used strings for dates. I have never cast them as
> integers. 

I am indifferent to what you do.
 
> In that case they weren't integers. They were 'numbers'. 

I have absolutely no idea why you have this unique idea that integers
must be created contiguously.  You simply are confused between
integer, cardinal and ordinal.

Is 54865343 not an integer ?

How hard is this ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T02:37:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea0679c.435772721@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[3 more quoted lines elided]…
>> OF an integer. A date in that form isn't an integer, it is collection of
three
>> integers. Now I realize that collections can indeed be ordinals in the set of
>> 'all dates'. There are three levels here -- all dates, collections and
integral
>> components of a date. 
>
>A date of the form 20030415 is not _an_ ordinal, it is a collection of
>3 ordinals. A 'collection' cannot be _an_ ordinal.

The word ordinal is prone to sloppy usage. It can mean 'ordinal data' i.e. a set
member, or it can mean 'ordinal number' i.e. the position of that member in the
set, which is an integer. Set members can be anything; they need not be numbers.


>> It is a member of a set defined by a range. The defining concept here is set,
>> the container.
…[3 more quoted lines elided]…
>integer, eg 20030415.

Integers are a complete set where Z(n+1) = Z(n) + 1. Dates in that form do not
meet the test.

>> Yes it does. Look up the defininition of integer on any math site -- NOT a
>> dictionary or computer lingo site. 
>
>Having looked at some I cannot find any such, please point the way.

I posted some in a separate thread: What is an Integer.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-18T22:35:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304182135.6015429a@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> Integers are a complete set where Z(n+1) = Z(n) + 1. Dates in that form do not
> meet the test.

Just saying it backwards doesn't support your argument at all.

Yes, there is a 'complete set of integers', referred to as Z.  That
does not mean that you must say every number in order to make one an
integer.

Now it is true that the _ordinals_ of a set _are_ complete in a range.
 Amd that is why a number of the form 20030415 is not an ordinal.  It
is also not a cardinal.  (which is what this thread started as).

But an integer is just a whole number, any whole number. We don't need
to start at one and count up to it.  All that is required is that it
doesn't have a decimal part.

While 20030415 is an integer that can be treated as representing a
date, others, such as 20039999 may not represent a valid date.  That
stops it being a _date_ and doesn't stop it being an _integer_.

> I posted some in a separate thread: What is an Integer.

Yes, but did you _read_ them ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T16:07:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea16342.60416728@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net> <217e491a.0304182135.6015429a@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
>> Integers are a complete set where Z(n+1) = Z(n) + 1. Dates in that form do
not
>> meet the test.
>
>Just saying it backwards doesn't support your argument at all.

The references support my argument, especially the first one.

>But an integer is just a whole number, any whole number. We don't need
>to start at one and count up to it.  All that is required is that it
>doesn't have a decimal part.

Some math references say you do need to count up to it. They define integer a(n)
recursively as a(n-1) + 1. 

>While 20030415 is an integer that can be treated as representing a
>date, others, such as 20039999 may not represent a valid date.  That
…[4 more quoted lines elided]…
>Yes, but did you _read_ them ?

Evidently you didn't, or you wouldn't keep making the same 'coder' argument. In
programming, an integer is any whole number; in math, it is a member of a set
with no gaps.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-19T17:38:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304191638.6551ae40@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net> <217e491a.0304182135.6015429a@posting.google.com> <3ea16342.60416728@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >> Integers are a complete set where Z(n+1) = Z(n) + 1. Dates in that form do
>  not
…[4 more quoted lines elided]…
> The references support my argument, especially the first one.

No. They do not 'support' your argument. You have, as I said,
understood what it said backwards.

Integers are a 'complete set' when .. as you say.

This does not mean something must use the 'complete set' in order for
it to be an integer.

Following your argument: if we take the set of prime numbers, which
are [1,2,3,5,7,11,..] then these are not integers.  Therfore
(according to you) 1 is not an integer.

If we take the set of even numbers [2,4,6,8,..], then these are not
integers by your rules.

Using this it is possible to prove that all numbers are 'not integer'.

However, if we understand what the actual definitions _say_ (instead
of getting it backwards), then we can see that the definition of Z as
being a 'complete set' has no impact on what 'an inger' _is_.

If I were to define a complete set of letters as being ['a' .. 'z']
and then say that the set ['a', 'e', 'i', 'o', 'u'] were vowels, then
this doesn't stop 'a' being a letter.

In the same way 20030415 _is_ in the set of integers [-infinity .. 0
.. infinity] and therefore _is_ an integer.
 
> Some math references say you do need to count up to it. They define integer a(n)
> recursively as a(n-1) + 1. 

And the recursive list would include 20030415.
 
> Evidently you didn't, or you wouldn't keep making the same 'coder' argument. 

In that supposed to be an insult ?  an ad hominem even ?

> In programming, an integer is any whole number; 

Even your sites say that 'whole number' is inadequately defined and
may mean 'all positive integers', may include zero, or may also be
used to include negative integers.

In any context 'whole number' and 'positive integer' are synonymous.
Are you trying to say that programming can't have negatives ?  I don't
think so.  If you include the negaives then 'whole number' and
'integer' are _always_ synonymous.

> in math, it is a member of a set with no gaps.

Only if you get it backwards.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 19)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-20T03:12:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea1ff63.100392598@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net> <217e491a.0304182135.6015429a@posting.google.com> <3ea16342.60416728@news.optonline.net> <217e491a.0304191638.6551ae40@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[14 more quoted lines elided]…
>it to be an integer.

Yes it does. The definition of integer came from Set Theory, where things are
not defined in isolation but rather by their relationship to the set. In order
for a number to be an integer, it must belong to the complete set of natural
numbers and their negatives. 

If it's a member of a smaller set then it shouldn't be called an integer
(although it is too), it should be called 'a prime' or 'a date' or 'an even
number'.

>Using this it is possible to prove that all numbers are 'not integer'.

How's that?

>However, if we understand what the actual definitions _say_ (instead
>of getting it backwards), then we can see that the definition of Z as
>being a 'complete set' has no impact on what 'an integer' _is_.

Now you are confusing the container with its contents. You think if it contains
exclusively numeric data, it is an integer. That's incorrect. Dates and phone
numbers are not integers. 

>If I were to define a complete set of letters as being ['a' .. 'z']
>and then say that the set ['a', 'e', 'i', 'o', 'u'] were vowels, then
>this doesn't stop 'a' being a letter.

No, it is on the Intersection of both sets. But if I added 1 to 'a' and
discovered that 'b' is not a vowel then 'a' would cease being a letter in this
context. It would be a member of the set vowels. So too, if I added 1 to
20030331 and discovered that 20030332 was an invalid date then 20030331 would
cease being an integer. 

>> Evidently you didn't, or you wouldn't keep making the same 'coder' argument. 
>
>In that supposed to be an insult ?  an ad hominem even ?

Yes to both. Don't play innocent. You're the worst offendor when it comes to
insulting people here, particularly me. If you want to see flames, keep it up.
You ain't seen nothing yet. 

>In any context 'whole number' and 'positive integer' are synonymous.

Yes they are when it comes to ordinals. The number 1 is ordinal number  1 ...

I wonder about irrational numbers, which are more numerous than natural. What
ordinals do we use for them? We'll eventually 'run out of numbers', even though
both go to infinity. 

>Are you trying to say that programming can't have negatives ?  I don't
>think so.  If you include the negaives then 'whole number' and
>'integer' are _always_ synonymous.

You just disproved your argument. There are no negative dates.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-20T08:09:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7u2l1$gaq$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea16342.60416728@news.optonline.net> <217e491a.0304191638.6551ae40@posting.google.com> <3ea1ff63.100392598@news.optonline.net>`

```
In article <3ea1ff63.100392598@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>riplin@Azonic.co.nz (Richard) wrote:
>

[snip]

>>Integers are a 'complete set' when .. as you say.
>>
…[10 more quoted lines elided]…
>number'.

Mr Wagner, please revisit this last statement.  The conclusion is that any 
number 'shouldn't be called an integer (although it is too)' because it 
can be considered a member of a smaller set, such as 'the set of positive 
integers' or 'the set of negative integers' or 'the set of integers which 
contains all members which equal 5'.

>
>>Using this it is possible to prove that all numbers are 'not integer'.
>
>How's that?

See above.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:05:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b811cg$11j$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea16342.60416728@news.optonline.net> <217e491a.0304191638.6551ae40@posting.google.com> <3ea1ff63.100392598@news.optonline.net> <b7u2l1$gaq$1@panix1.panix.com>`

```

On 20-Apr-2003, docdwarf@panix.com wrote:

> >If it's a member of a smaller set then it shouldn't be called an integer
> >(although it is too), it should be called 'a prime' or 'a date' or 'an even
…[6 more quoted lines elided]…
> contains all members which equal 5'.

Actually, in another post he indicated a preference to call it a "number"
instead of an "integer".   Which would lead me to infer that he prefers exactly
the opposite of what I infer from the above quote.

I am confused.  Maybe it should be called anything except what CoBOL calls it.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 20)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-21T05:09:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ta5m$sjm$1@aklobs.kc.net.nz>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea16342.60416728@news.optonline.net> <217e491a.0304191638.6551ae40@posting.google.com> <3ea1ff63.100392598@news.optonline.net>`

```
Robert Wagner wrote:

> Yes it does. The definition of integer came from Set Theory, 

Is it your claim then that before there was a set theory there was no such 
thing as an integer ?

> In order for a number to be an integer, it must belong to the complete set
> of natural numbers and their negatives.

No. Wrong. Integers happen to exist independently of the theory of sets.

Integers are just numbers that have no decimal part.

In any case the number 20030415 _is_ a member of the set of all natural 
numbers.

> If it's a member of a smaller set then it shouldn't be called an integer
> (although it is too), it should be called 'a prime' or 'a date' or 'an
> even number'.

That may be your opinion, but it just happens to be a rather silly one that 
has no basis in anyone's theory (except yours).

>>However, if we understand what the actual definitions _say_ (instead
>>of getting it backwards), then we can see that the definition of Z as
…[4 more quoted lines elided]…
> Dates and phone numbers are not integers.

Where did you think that up  ?  You should actually look at what I write, 
not some version of it that only exists in your imagination.

> So too, if I added 1
> to 20030331 and discovered that 20030332 was an invalid date then 20030331
> would cease being an integer.

The number 20030331 is a member of the set Z.  The number 20030332 is a 
member of the set Z, both are thus integers.  Only one of them can validly 
claim to be a member of the set of integers that represents valid dates in 
the form YYYYMMDD.  How hard is that ?

> Yes to both. Don't play innocent. You're the worst offendor when it comes
> to insulting people here, 

When you insult people you seem to think that it doesn't count because it 
is 'all mainframers', or 'the J4 committee', or 'computer scientists' or 
somesuch.

> particularly me. 

Well, actually only you.

> I wonder about irrational numbers, which are more numerous than natural.
> What ordinals do we use for them? 

We don't.

> You just disproved your argument. There are no negative dates.

In what way does there need to be ?
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-18T22:44:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304182144.350f0bad@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> The word ordinal is prone to sloppy usage. It can mean 'ordinal data' i.e. a
> set member, 

No. Wrong. That is not just sloppy it is wrong.  'Ordinal data'
doesn't mean 'a set member', it means 'data that is in order'.

> or it can mean 'ordinal number' i.e. the position of that member in the
> set, which is an integer. 

 Note:-> a NON-NEGATIVE integer.

> Set members can be anything; they need not be numbers.

I am so glad that you retract your previous 'definition' of ordinal.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-19T16:07:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea16016.59605315@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net> <217e491a.0304182144.350f0bad@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[4 more quoted lines elided]…
>doesn't mean 'a set member', it means 'data that is in order'.

Ok, make that 'ordinal datum'.

>> or it can mean 'ordinal number' i.e. the position of that member in the
>> set, which is an integer. 
>
> Note:-> a NON-NEGATIVE integer.

Right. Some languages are obsessed with the first ordinal number being zero. Php
returns 0 for January and 11 for December.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-19T14:17:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304191317.31a8976e@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3e9be3b7.139819159@news.optonline.net> <217e491a.0304151127.13e89649@posting.google.com> <3e9ca90b.190342340@news.optonline.net> <b7ip7p$76a$1@aklobs.kc.net.nz> <3e9de228.270511429@news.optonline.net> <217e491a.0304170047.2cd86d98@posting.google.com> <3ea0679c.435772721@news.optonline.net> <217e491a.0304182144.350f0bad@posting.google.com> <3ea16016.59605315@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> Right. Some languages are obsessed with the first ordinal number being zero.
> Php returns 0 for January and 11 for December.

An 'obsession' should be more than just a single indiosyncrasy, so I
will consider you are using this in a perjoritive way.

In the case of PHP's localtime() it simply uses C's underlying
structures and results.  It is not a problem to those who are prepared
to read the manual instead of guessing what it may be.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-19T22:01:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7sv18$i50$1@panix1.panix.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <3ea0679c.435772721@news.optonline.net> <217e491a.0304182144.350f0bad@posting.google.com> <3ea16016.59605315@news.optonline.net>`

```
In article <3ea16016.59605315@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>riplin@Azonic.co.nz (Richard) wrote:
>
…[8 more quoted lines elided]…
>Ok, make that 'ordinal datum'.

It might be more accurate to make it a 'Gee, I was proven wrong and rather 
than admit it I will attempt to alter my assertion'.

DD
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-17T02:07:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304170107.2297d9b4@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com> <217e491a.0304141600.5cd7bab6@posting.google.com> <3e9be3b7.139819159@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> An integer, which derives from entire, 

No. Wrong.      ;-)

"""Integer The base root comes from the proto Indo-European root tag
for touch. The root evolved into a nasalized tang and became the root
for many "touch" words such as tangent and contaminate.
In integer it means "untouched" and that was the original Latin base
meaning. It also carried peripheral meanings associated with being
untouched, such as virtuous, pure, and whole or complete. These last
terms brought it into mathematics.
It appears, according to the Oxford English Dictionary, that the word
was first used as a noun in English by T. Digges in a 1571 in
Pantometria, a book on geometry."""
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-14T18:43:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304141601.4a2b5a47@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote 

> > Consistancy. One function returns a date as a string whereas another
>  returns it
…[3 more quoted lines elided]…
> function is integer that the function is NOT returning an integer?

It is probably because RW thinks that a 'cardinal' is type of bird, or
someone in a church hierarchy.

A date in a numeric form such as 20030415 is a perfectly good integer,
of course it is not a cardinal number, though it may resemble one.  RW
is making the wrong argument.
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T02:50:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b59e6.104532271@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[73 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Accuracy/Knowledge score-card

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T02:50:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b5ca7.105237903@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6snhg$87h$1@slb6.atl.mindspring.net> <3e93602c.180848320@news.optonline.net> <b72avl$14jn$1@si05.rsvl.unisys.com> <3e9607da.354872922@news.optonline.net> <b76odq$156a$1@si05.rsvl.unisys.com> <3e98352b.111003306@news.optonline.net> <b7eptg$hga$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[73 more quoted lines elided]…
>
```

#### ↳ Re: Accuracy/Knowledge score-card

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-07T13:48:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6so78$adc$1@si05.rsvl.unisys.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net>`

```
How about

12)  Describes all architectures developed by Burroughs as extinct
("Superior technology didn't help Burroughs ... survive.")?

I would think a quick glance at
www.unisys.com/about__unisys/history/index.htm would indicate that that is
perhaps an inappropriately pessimistic opinion!   There are some who feel
the purchase of Sperry Univac by Burroughs Corporation in 1986 was perhaps
rash on Blumenthal's part, but the truth is that what started life as the
Burroughs Large Systems and what started life as the Univac 1100/2200
computers are still very much a part of the Unisys product line, and are
still actively being enhanced!

    -Chuck Stevens
```

##### ↳ ↳ Re: Accuracy/Knowledge score-card

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-04-07T21:26:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com>`

```
I programmed on a Univac 90/30 and 90/60 in the mid to late 70s and was very
impressed by both.  Seemed to be much friendlier than IBM's equivalents at
the time.  Eventually the company I worked for then went the IBM route.
```

###### ↳ ↳ ↳ RCA/Univac/IBM history

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T14:31:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6umfg$g8f$1@peabody.colorado.edu>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com>`

```

On  7-Apr-2003, "Terry Heinze" <terryheinze@prodigy.net> wrote:

> I programmed on a Univac 90/30 and 90/60 in the mid to late 70s and was very
> impressed by both.  Seemed to be much friendlier than IBM's equivalents at
> the time.  Eventually the company I worked for then went the IBM route.

I worked in a 9030 shop in 1982 when we switched to IBM.  To keep the
functionality of their flat, relative, and keyed file systems we went to IBM
VSAM.   I later worked for a 1100 shop.   (I've also worked with Burroughs, DEC,
& Honeywell).

I'm told that when RCA decided to quit the computer business, they sold their
design to Univac which made the 9030 and then laid off their computer designers.
  My boss at the time used to be an RCA man.  IBM then hired them and created
the 360.   The Univac and IBM designs were very similar - probably because they
were designed around the same RCA theories and by the same people.

I would appreciate it if a historian here would expand on this hearsay.
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 4)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-04-08T15:51:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<geCka.3544$7I7.112@newssvr19.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu>`

```
My manager, at the time we had a PDP-8, was an ex-RCA employee, so when it
came time to go to a bigger machine, he pushed hard for the Univac 9030.
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 5)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-04-08T23:57:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wlJka.3719$OJ2.2432@newssvr19.news.prodigy.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu> <geCka.3544$7I7.112@newssvr19.news.prodigy.com>`

```
One thing I found interesting about Univac's COBOL circa 1976 was that they
stored current date in an 11-character field in MM/DD/YYDDD format.  When
moving it, the size of the destination field determined whether the move was
left-justified or right-justified!  An 8-character destination resulted in a
gregorian date, a 5-character one, a julian!
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-04-08T13:35:27-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E92FA4F.19A0CAFE@istar.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> On  7-Apr-2003, "Terry Heinze" <terryheinze@prodigy.net> wrote:
…[16 more quoted lines elided]…
> I would appreciate it if a historian here would expand on this hearsay.

Since the 360 came before the Spectra 70, the claim was false.  I
consider the dead-ending of the Spectra/9030 line another sample of
Univac snatching defeat from the jaws of victory.
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 4)_

- **From:** foodman123@aol.com (Anthony Dilworth)
- **Date:** 2003-04-08T11:40:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93dfc7c7.0304081040.75d57e43@posting.google.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu>`

```
> I'm told that when RCA decided to quit the computer business, they sold their
> design to Univac which made the 9030 and then laid off their computer designers.
…[4 more quoted lines elided]…
> I would appreciate it if a historian here would expand on this hearsay.

Hi:

I am far from being an historian, but dimly recall that RCA introduced
the Spectra-70 after the 360. So, RCA must have quit the business after 
the 360 was introduced. We used to buy time on the Spectra-70 when 360 
time was hard to get.

Thank you

Tony Dilworth
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 5)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2003-04-08T22:43:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9396F0.626C7F3C@mb.sympatico.ca>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu> <93dfc7c7.0304081040.75d57e43@posting.google.com>`

```
RCA plugged virtual memory before IBM did but couldn't take enough advantage of it.
Once IBM came out with vm, we at Univac had rather a tough time selling against it:
all we could do was talk about the superior method of re-entrant code.    The came the
glorious week when Univac bought out RCA and we could go back to the prospects and say
to them: Remember all those reasons we gave you not to use vm? Well, now they're not
true because we have vm too!  Didn't help us much, though; I seem to remember that a
lot of the RCA customer base defected to IBM as a CYA precaution.

Peter
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-04-09T01:17:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WwKka.46872$rd4.1441542@twister.austin.rr.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu>`

```
There is no real substance to the idea the 360 was based upon then current RCA designs.
When the 360 came out, RCA basically took one look at it and decided to leave the
computer business, as well it should. The 360 was an engineering marvel, and
not just for its instruction set!

Sperry/Univac 9030 - sigh- another example of snatching defeat out of the jaws of victory...

-Paul

"Howard Brazee" <howard@brazee.net> wrote in message news:b6umfg$g8f$1@peabody.colorado.edu...
>
> On  7-Apr-2003, "Terry Heinze" <terryheinze@prodigy.net> wrote:
…[16 more quoted lines elided]…
> I would appreciate it if a historian here would expand on this hearsay.
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-09T03:46:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9369ae.183282633@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  7-Apr-2003, "Terry Heinze" <terryheinze@prodigy.net> wrote:
…[7 more quoted lines elided]…
>VSAM.   I later worked for a 1100 shop.   (I've also worked with Burroughs,
DEC,
>& Honeywell).
>
>I'm told that when RCA decided to quit the computer business, they sold their
>design to Univac which made the 9030 and then laid off their computer
designers.
>  My boss at the time used to be an RCA man.  IBM then hired them and created
>the 360.   The Univac and IBM designs were very similar - probably because they
>were designed around the same RCA theories and by the same people.
>
>I would appreciate it if a historian here would expand on this hearsay.

Something is wrong with the time-line here. 

..RCA produced old-style machines such as the 301.
..IBM introduced the 360.
..RCA quickly responded with a clone: Spectra 70. It wasn't an RCA-style
machine, it was a copy of IBM.
..RCA folded its tent. 

This happened between 1964 and 1972. 

It's not possible for your former boss to have "created the 360" because RCA was
behind, not ahead.
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 5)_

- **From:** gary drummond <gdrumm@sbcglobal.net>
- **Date:** 2003-05-08T00:46:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB9A943.330DBF51@sbcglobal.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu> <3e9369ae.183282633@news.optonline.net>`

```
Robert Wagner wrote:
> 
> "Howard Brazee" <howard@brazee.net> wrote:
…[34 more quoted lines elided]…
> behind, not ahead.

As I remember, the Spectra was a copy of the 360 instruction set,
but the hardware had 4 interrupt states, each with it's own set of
registers. VMOS introduced support for vm, which looked much more 
efficient using the 4 states VS 2 states. I think Burroughs had a 
vm first, but I lost my Datamation collection...

Search for history and my name or doc's on google, he was collecting 
history pointers at one time...

Gary

Gary
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 6)_

- **From:** "Warren Simmons" <wsimmons5@cox.net>
- **Date:** 2003-05-16T12:08:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xabxa.1$%42.0@fed1read06>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu> <3e9369ae.183282633@news.optonline.net> <3EB9A943.330DBF51@sbcglobal.net>`

```
One CODASYL member who was an IBM user, also got some RCA systems based upon
the
instruction set copy. As with the H200, the gamble was bad. RCA engineers
felt they had a better
way to do some of the instructions or functions, and programs for the IBM or
the RCA could not
run on the other system without a recompile.

    Honeywell engineers trying to make a better IBM 1400 series system were
unaware that the IBM
systems considered blank posiations in cards as zeros. The H200 thought they
were spaces. A revision
was necessary to follow the sales plan.

The above "memory dump" is mine. It is based upon comments from the RCA
customer member of
the Executive Committee, and the Honeywell "dump" comes from attending a
demo of the H200 in
WDC were the demo's failed.

However, this is memory of an old f**t.... and I disown and deneigh
authorship of this message.

Warren
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-17T09:47:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ec5ef53.41592022@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu> <3e9369ae.183282633@news.optonline.net> <3EB9A943.330DBF51@sbcglobal.net> <xabxa.1$%42.0@fed1read06>`

```
"Warren Simmons" <wsimmons5@cox.net> wrote:

>One CODASYL member who was an IBM user, also got some RCA systems based upon
>the
…[19 more quoted lines elided]…
>authorship of this message.

I worked on all four machines, including a stint as Honeywell systems engineer
doing pre- and post-sales support.

The BCD (octal) code for space was indeed 00 (not 12, the character zero). It is
hard to imagine what other value early Honeywell engineers thought was a space.
Perhaps O'20', which was sometimes called "'alternate space" in printer specs.
(With typical technician illiteracy. The word should have been alternative.)

It is true that there were minor differences between Spectra/70 and IBM/360
machine code. Even if there weren't, a recompilation would still have been
necessary because called library functions were talking to the OS API, which was
somewhat  different. RCA never claimed 'binary compatibility', which would have
required cloning the entire IBM operating system.

The H-200 and Spectra/70 IBM clones failed because of inferior marketing, not
technical differences. 

There weren't any dumps above nor attached to your message.
```

###### ↳ ↳ ↳ Re: RCA/Univac/IBM history

_(reply depth: 8)_

- **From:** gary drummond <gdrumm@sbcglobal.net>
- **Date:** 2003-06-05T16:06:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EDF6AC7.6D833BC6@sbcglobal.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net> <b6so78$adc$1@si05.rsvl.unisys.com> <c2mka.429$Pn7.39626807@newssvr15.news.prodigy.com> <b6umfg$g8f$1@peabody.colorado.edu> <3e9369ae.183282633@news.optonline.net> <3EB9A943.330DBF51@sbcglobal.net> <xabxa.1$%42.0@fed1read06> <3ec5ef53.41592022@news.optonline.net>`

```
Robert Wagner wrote:
> 
> "Warren Simmons" <wsimmons5@cox.net> wrote:
…[41 more quoted lines elided]…
> There weren't any dumps above nor attached to your message.

I remember Sperry had to extend the contract to manufacture the
Spectra's
for a couple of years after we bought them-sold more than they did I
believe...

Gary
```

#### ↳ Re: Accuracy/Knowledge score-card

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-07T21:30:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uxGdnUN4r8r-qQ-jXTWJkQ@giganews.com>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b6sm6g$9uq$1@slb9.atl.mindspring.net...
> I thought I would start a "running" thread on issues that explain my
opinion
> (and it is only an OPINION) of one specific poster to CLC.  The following
> are NOT in any specific order (chronological or "importance")

[snip list]

You're being too kind. I once had a brilliant man tell me: "I'm not
interested in your OPINION! Opinions should be kept to yourself and anyone
expressing an opinion should be shot! I am interested in facts sufficiently
strong in themselves that they compel a rational mind of the probable truth
of the assertion."

You have not expressed an 'opinion.' You have proven, with overwhelming
evidence, jackassness.

But what else would one expect from a logical mind?
```

#### ↳ Re: Accuracy/Knowledge score-card

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-08T06:38:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9267b1.117228459@news.optonline.net>`
- **References:** `<b6sm6g$9uq$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

If you want to respond to my postings, killfile only puts you at a disadvantage.
Give it up and read the originals. 

Flaming should be beneath your dignity.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
