[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The deal with the Inline Performs

_37 messages · 13 participants · 1998-07_

---

### The deal with the Inline Performs

- **From:** lvenick@aol.com (LVenick)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071401051700.VAA07236@ladder01.news.aol.com>`

```
So here's the story....
I  coded it without the IP
Evaluate t-code
     when '0'
          move.....
          add.....
          add..
      when '1'
          etc....
          etc....
End-evaluate
and it workes fine.  I was so happy i didn't bother doing it the other way so
I could get the error messages to share with you. Since I just moved the 
statements from the perform subroutine to the evaluate (after the 'when')
there WAS a period after the last statement in each perform 'grouping', so
there 
it is....the first period became the terminator for the Evaluate.
Larry
```

#### ↳ Re: The deal with the Inline Performs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35aab0a2.0@news1.ibm.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com>`

```
You see how harmful those periods are.
Advise: NEVER use periods except when necessary and then
put them on line by themselves, then you will never again make
that (and similar) errors.

LVenick wrote in message
<1998071401051700.VAA07236@ladder01.news.aol.com>...
>So here's the story....
>I  coded it without the IP
…[9 more quoted lines elided]…
>and it workes fine.  I was so happy i didn't bother doing it the other way
so
>I could get the error messages to share with you. Since I just moved the
>statements from the perform subroutine to the evaluate (after the 'when')
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: The deal with the Inline Performs

- **From:** "andy r" <andyr*NOSPAMMARAMA*@megsinet.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net>`

```
I say that you are wrong!

	Perhaps putting the period on its own line may make it less likely to make
'those' errors again, however, lack of periods at all makes the coding less
readable than was intended.  Its like saying 'do not use a 'go to' EVER and
then running your compiled code into an 'optimizer' (this can generate the
equivalent of cobol's goto's in a dump).

Better advice:   Use syntax for its intended purpose and it is not a
problem.  It is technically impossible to have a COBOL program completely
without periods.  You are better off being regimented and either use or do
not use them.  Don't mix.

	Really not trying to be anal about this.  I guess that there are different
coding preferences...

Andy

Leif Svalgaard <leif@ibm.net> wrote in article
<35aab0a2.0@news1.ibm.net>...
> You see how harmful those periods are.
> Advise: NEVER use periods except when necessary and then
…[16 more quoted lines elided]…
> >and it workes fine.  I was so happy i didn't bother doing it the other
way
> so
> >I could get the error messages to share with you. Since I just moved the
> >statements from the perform subroutine to the evaluate (after the
'when')
> >there WAS a period after the last statement in each perform 'grouping',
so
> >there
> >it is....the first period became the terminator for the Evaluate.
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oh7n7$23s@bgtnsc03.worldnet.att.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>`

```
andy r wrote:
> 
> I say that you are wrong!
…[6 more quoted lines elided]…
> 

Whether the object code contains the equivalent of 'go to's is not the
issue (of course it will, it's a branch or jump instruction). The source
code should be written to be functional, readable and maintainable. IMHO
people are overly concerned with what the compiler generates - let it do
its job, the compiler people will improve it over time. We applications
folks should concentrate on writing good applications.

Bill Lynch

PS: No one in mind here, nor any intent of flaming.

(snipped)
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AB367C.51F9@erols.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>`

```
andy r wrote:
> 

[snippage]

> Better advice:   Use syntax for its intended purpose and it is not a
> problem.  It is technically impossible to have a COBOL program completely
> without periods.  You are better off being regimented and either use or do
> not use them.  Don't mix.

I would say that this is *sound* advice... what is important it the
context.  Many difficulties arise when coding styles are mixed in a
given program (as always happens over 20+ years of maintenance) so pay
close attention to the chunk you are working on... are there periods
used in the Olde Style?  Fine, then use periods likewise.  Is there a
mass of code with a single '.' as the paragraph's last line?  Best not
to interrupt the logic-flow with a period, then.

Aesthetics are fine, granted, but to paraphrase Wittgenstein's 'The
bridge must not fall down'... 'the program must run to a successful and
accurate completion'.

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ab4510.0@news1.ibm.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>`

```

andy r wrote in message <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>...
>I say that you are wrong!
>
> Perhaps putting the period on its own line may make it less likely to make
>'those' errors again, however, lack of periods at all makes the coding less
>readable than was intended

Give an example of how a period improves readability.

You can also use commas and semi-colons and these
might improve readability but are harmless as they act
as spaces. Periods, on the other hand, have a definite
(and sometimes large) effect.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4NIq1.126$Gp.595776@news1.atlantic.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <35ab4510.0@news1.ibm.net>...
>
>andy r wrote in message <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>...
>>I say that you are wrong!
>>
>> Perhaps putting the period on its own line may make it less likely to
make
>>'those' errors again, however, lack of periods at all makes the coding
less
>>readable than was intended
>
…[6 more quoted lines elided]…
>

IMHO, it is a question of style. As we all know, questions of
style lead to ... well, nowhere.

I will give two examples of style where a lack of periods *may*
make code less readable.

1. comment, code, white space, comment, code, white space.
In this style, the lack of a period preceding the white space
may make the code less readable. This is because we expect
periods to end paragraphs; but in this case, the paragraph is
not yet finished.

2. Nested else-if where the IFs are not indented. This style
leads to multiple end-if statements which may be less readable
than a single end-if followed by a period.

DD mentioned, separately, that maintaining the existing style
(of the program) is a more important consideration. I agree!

On a personal note, I find that, if a program is written in upper case,
I am more comfortable with periods at the end of sentences, which
must be some old habits. Whereas, a program written in lower case
seems more pleasing with a period on the line following the last
statement of the paragraph. These concepts of "comfortable" and
"pleasing" deal directly with the question of readability.
------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC088C.A0C@sprynet.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <4NIq1.126$Gp.595776@news1.atlantic.net>`

```
Rick Smith wrote:
> 
> I will give two examples of style where a lack of periods *may*
…[6 more quoted lines elided]…
> not yet finished.

Please post a code example of what you're talking about.  I don't
understnad what "comment, code, white space, etc." is referring to.
 
> 2. Nested else-if where the IFs are not indented. This style
> leads to multiple end-if statements which may be less readable
> than a single end-if followed by a period.

True, but use an EVALUATE statement instead to avoid this type of
coding.

> DD mentioned, separately, that maintaining the existing style
> (of the program) is a more important consideration. I agree!

This is definately true.  What's hard is trying to decide which of
the five styles that the program is already in do you copy?  :-)
 
> On a personal note, I find that, if a program is written in upper case,
> I am more comfortable with periods at the end of sentences, which
…[3 more quoted lines elided]…
> "pleasing" deal directly with the question of readability.

I personally am a "no period" person.  The one thing I will do is,
instead of using a period by itself, I instead use "EXIT."  A period
on a line by itself does seem rather silly.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC0816.170B@erols.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <4NIq1.126$Gp.595776@news1.atlantic.net>`

```
Rick Smith wrote:
> 

[snippage]

> 
> DD mentioned, separately, that maintaining the existing style
> (of the program) is a more important consideration. I agree!

You agree with *me*?  Then one of us must be wrong... but on a more
serious side...

... I remember, aways back when, it was a common assignment for an
instructor of English (either teacher or professor) to say to the class
'Next period I want three pages, one in the style of Faulkner, one in
Shakespeare and one in Woolf.' ...

... so maybe *this* is why it is better to have liberal-arts majors
write applications and leave the systems for the CS majors?

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ab5c65.0@news1.ibm.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <4NIq1.126$Gp.595776@news1.atlantic.net>`

```

Rick Smith wrote in message <4NIq1.126$Gp.595776@news1.atlantic.net>...
>
>Leif Svalgaard wrote in message <35ab4510.0@news1.ibm.net>...
…[19 more quoted lines elided]…
>style lead to ... well, nowhere.

that is, sad to say, true. But style is VERY important for the
future maintainability by people that may have a different style.

>
>I will give two examples of style where a lack of periods *may*
…[6 more quoted lines elided]…
>not yet finished.


This is not quite clear to me. Are you saying that there should be
a period in the middle of the paragraph?  Please show code example
rather than pseudo code.

>2. Nested else-if where the IFs are not indented. This style
>leads to multiple end-if statements which may be less readable
>than a single end-if followed by a period.


again show an example. You would rarely have a period after
the END-IF (except at end of para).

>DD mentioned, separately, that maintaining the existing style
>(of the program) is a more important consideration. I agree!


this is correct. Don't mess with existing style.

>
>On a personal note, I find that, if a program is written in upper case,
>I am more comfortable with periods at the end of sentences, which
>must be some old habits.

this is probably true. Old habits die hard

> Whereas, a program written in lower case
>seems more pleasing with a period on the line following the last
>statement of the paragraph. These concepts of "comfortable" and
>"pleasing" deal directly with the question of readability.


But, the we must code for somebody else's comfort because
somebody else will likely be stuck maintaining our code.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i4Mq1.37$hL.50521@news1.atlantic.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <4NIq1.126$Gp.595776@news1.atlantic.net> <35ab5c65.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <35ab5c65.0@news1.ibm.net>...
>
>Rick Smith wrote in message <4NIq1.126$Gp.595776@news1.atlantic.net>...
>>
[...]
>>
>>I will give two examples of style where a lack of periods *may*
…[20 more quoted lines elided]…
>
In _The Psychology of Computer Programming_, Gerald Weinberg
talks about "... the eye for wholeness, or gestalt."

Then later, "... the process by which many programming errors are
found. First, there is only the gestalt, a general feeling that something
is out of place without any particular localization."

My point is that in the "comment, code, white space" style, a missing
period MAY trigger the "gestalt," the feeling that something is out of
place. It is that trigger which affects readability.

I cannot give a specific code example, at this time

The problem with readability of the nested "else if" should be apparent.
Particularly, if the nesting is "very" deep.

if some-condition
    perform some-things
else if some-other-condition
    perform some-other-things
else if another-condition
    perform another-thing
else if yet-another-condition
    perform yet-another-thing
else if a-different-condition
    perform a-different-thing
else if still-another-condition
    perform still-another-thing
else if still-more-conditions
    perform still-more-things
end-if
end-if
end-if
end-if
end-if
end-if
end-if
perform some common activity
.

is, IMO, less readable than

if some-condition
    perform some-things
else if some-other-condition
    perform some-other-things
else if another-condition
    perform another-thing
else if yet-another-condition
    perform yet-another-thing
else if a-different-condition
    perform a-different-thing
else if still-another-condition
    perform still-another-thing
else if still-more-conditions
    perform still-more-things
end-if.
perform some common activity
.

Some, in this newsgroup, have suggested ELSE-IF as a means
of eliminating multiple END-IF statements, for this style. Until then
all we have is the period.
--------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ab913d.0@news1.ibm.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <4NIq1.126$Gp.595776@news1.atlantic.net> <35ab5c65.0@news1.ibm.net> <i4Mq1.37$hL.50521@news1.atlantic.net>`

```

Rick Smith wrote in message ...
>
>Leif Svalgaard wrote in message <35ab5c65.0@news1.ibm.net>...
…[6 more quoted lines elided]…
>>>make code less readable.

>The problem with readability of the nested "else if" should be apparent.
>Particularly, if the nesting is "very" deep.
…[43 more quoted lines elided]…
>.



I see what you mean. you are quite right.
I would not even have the single (dubious) end-if
there at all (since it just the end of the last if).
so:
...
else if still-more-conditions
     perform still-more-things
.
perform some common activity
.

I'm happy to see that you put the period after the 'perform some common...'
on
a line by itself where it belongs.

Some people would replace the whole structure with
evaluate true
  when ...
  when ...
end-evaluate

note no periods are needed nor should be coded.
This brings us full circle back to the original problem
where Larry had a problem with a period in the
middle of his evaluate statement.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WKMq1.39$hL.68490@news1.atlantic.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <4NIq1.126$Gp.595776@news1.atlantic.net> <35ab5c65.0@news1.ibm.net> <i4Mq1.37$hL.50521@news1.atlantic.net> <35ab913d.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <35ab913d.0@news1.ibm.net>...
>
>
…[9 more quoted lines elided]…
>.
After changing the options on MF3.2 from ANS85 MF(10) OSVS
to ANS85 MF(10) NOOSVS. The checker began rejecting IFs
that were not terminated by END-IF. I "think" the 85 standard may
require at least one END-IF before a period because that is what
was required to fix the syntax errors. This is also what I understand
from the Micro Focus Language Reference.
----------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofn35$42n$1@clarknet.clark.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net>`

```
In article <35ab4510.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:
>
>andy r wrote in message <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net>...
…[6 more quoted lines elided]…
>Give an example of how a period improves readability.

Readability is in the eye of the beholder, no?  *Any* example given can be
met with 'Nope, that ain't more readable to *me*!'

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oh7tg$23s@bgtnsc03.worldnet.att.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <01bdaeee$807a7380$0aa051d1@ns1.megsinet.net> <35ab4510.0@news1.ibm.net> <6ofn35$42n$1@clarknet.clark.net>`

```
docdwarf@clark.net wrote:
> 
> In article <35ab4510.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:
…[12 more quoted lines elided]…
> 

True, but in this case, you're simply wrong.

Bill Lynch :-)

> DD
```

##### ↳ ↳ Re: The deal with the Inline Performs

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofi5b$pt2$1@news.igs.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net>`

```
>Advise: NEVER use periods except when necessary and then
>put them on line by themselves, then you will never again make
>that (and similar) errors.

I've heard this before, but find it (the code) ugly looking ...mind you,
I'll grant that the period/no period in the middle of the if is probably
the most common typing error, even if easy to catch.  I find I do it
often as a result of cut and paste and have gotten quite fast at
<END><BACKSPACE> sequences.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ab5247.0@news1.ibm.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net>`

```

Donald Tees wrote in message <6ofi5b$pt2$1@news.igs.net>...
>>Advise: NEVER use periods except when necessary and then
>>put them on line by themselves, then you will never again make
…[6 more quoted lines elided]…
><END><BACKSPACE> sequences.


Then use the END-xxxx delimiters (if your compiler supports them).
they are better anyway and people do seem to be putting them on a
line by themselves.

I have yet to see:
    IF A > B
         MOVE X TO Z END-IF

The point is, don't use points. By this may be pointless as it borders
on a near-religious issue with some people, like using an asterisk in
col 7 on otherwise blank lines (but now I'm ranting, so I'll stop...)
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 4)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC0B04.6342@sprynet.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
> 
> Donald Tees wrote in message <6ofi5b$pt2$1@news.igs.net>...
…[16 more quoted lines elided]…
> col 7 on otherwise blank lines (but now I'm ranting, so I'll stop...)

I've never seen your weird END-IF example either (praise god!), but I am
currently working with some code that we bought from another company, and
look at some of the crazy stuff they have:

  IF CONDITION IS EQUAL TO 1
      PERFORM SOMETHING
      ELSE
      PERFORM SOMETHING-ELSE.

  IF CONDITION IS EQUAL TO 2
      IF CONDITION-2 IS EQUAL TO 45
          NEXT SENTENCE ELSE
          PERFORM NOT-45
      ELSE
      PERFORM CRAZY-ONE.

   IF THE-NAME IS EQUAL TO 'JOE'
       PERFORM NAME-FOR-JOE
           ELSE
       PERFORM NAME-NOT-JOE.

and more idiotic stuff.  This guy (the main coder) is not dumb, but his style sucks!  And it's
not even consistant within one program.  The programs are also all in COBOL-74, so no END-IFs
allowed...
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC0C09.1D35@erols.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net> <35AC0B04.6342@sprynet.com>`

```
Frank Swarbrick wrote:
> 

[snippage of... unattractive code; welcome to COBOL's warts, Mr
Swarbrick!]

> 
> and more idiotic stuff.  This guy (the main coder) is not dumb, but his style sucks!  >And it's not even consistant within one program.  The programs are also all in >COBOL-74, so no END-IFs allowed...

Slight correction... no END-IFs *existed* in COBOL until '85... but are
you saying that you'll be compiling this code under '74 restrictions? 
Please advise *someone* that if you're using IKFCBL00 as your compiler
it is guaranteed *not* to be Y2K-compliant.

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 4)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oh8bd$23s@bgtnsc03.worldnet.att.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
> 
> Donald Tees wrote in message <6ofi5b$pt2$1@news.igs.net>...
…[4 more quoted lines elided]…
> >I've heard this before, but find it (the code) ugly looking ...mind you,

It's really a question of what one is used to, and not just programming,
either (in spite of what I said earlier about DD). People who are used
to drinking whole milk hate skim at first - yet, after drinking the skim
for a week or two they don't like the whole milk, too greasy. Same for
coffee with milk & sugar vs. black coffee. Regarding the period (full
stop) on a line by itself, try it, you'll like it (if anyone else
remembers that commercial from late early 70's, or so).

> >I'll grant that the period/no period in the middle of the if is probably
> >the most common typing error, even if easy to catch.  I find I do it
…[13 more quoted lines elided]…
> col 7 on otherwise blank lines (but now I'm ranting, so I'll stop...)

Thanks for mentioning one of my pet peeves. IMHO the asterisk makes the
white space messy. Reminds me of the otherwise blank pages in manuals
which state "This page intentionally left blank" - not any more, man.

Bill Lynch
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofngc$513$1@clarknet.clark.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net>`

```
In article <35ab5247.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:

[snippage]

> By this may be pointless as it borders
>on a near-religious issue with some people, like using an asterisk in
>col 7 on otherwise blank lines (but now I'm ranting, so I'll stop...)

What's *this*?  You do not know that the col 7 '*' is required for
efficiency during compiling?

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC0B76.59BB@sprynet.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net>`

```
docdwarf@clark.net wrote:
> 
> In article <35ab5247.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:
…[8 more quoted lines elided]…
> efficiency during compiling?

Wasn't the '*' on a blank line from the punch-card days when the card had to
have *something* on it to be meaningful?

Or not...Just a guess.  I'm only 29, so I don't have any firsthand experience
regarding that.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 6)_

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC0B36.1505@erols.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net> <35AC0B76.59BB@sprynet.com>`

```
Frank Swarbrick wrote:
> 
> docdwarf@clark.net wrote:
…[13 more quoted lines elided]…
> have *something* on it to be meaningful?

To the best of my knowledge, no... then again I'll be the first to admit
that I am of rather limited knowledge.

An *, a / or a D (if SOURCE-COMPUTER... WITH DEBUGGING MODE is not
specified) in col 7 tells the compiler to skip the rest of the 'card'
entirely.

> 
> Or not...Just a guess.  I'm only 29, so I don't have any firsthand experience
> regarding that.

Not to worry... if you're very, very lucky and a little bit smart then
you'll spend far more years over 29 than under it.

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 6)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oh8kh$23s@bgtnsc03.worldnet.att.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net> <35AC0B76.59BB@sprynet.com>`

```
Frank Swarbrick wrote:
> 
> docdwarf@clark.net wrote:
…[16 more quoted lines elided]…
> regarding that.

This bit is fascinating - I had my COBOL training in early '66 (that's
1966 to your Y2K-compliant youngsters) and this is the first I've ever
heard about the "*" in 7 being more efficient. BTW, I was taught COBOL
on a 1401 - you think the early 360's were slow?? Oy!

Bill Lynch

> --
> Frank Swarbrick
> home: infocat@sprynet.com
> work: frank.swarbrick@1stbank.com
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ab6965.0@news1.ibm.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net>`

```

docdwarf@clark.net wrote in message <6ofngc$513$1@clarknet.clark.net>...
>In article <35ab5247.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:
>
…[8 more quoted lines elided]…
>


Hey, for those of you that complained that DD never posted Cobol related
stuff, here is a Cobol related, on-topic, DD posting offering compile time
optimization.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofr06$c56$1@clarknet.clark.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net> <35ab6965.0@news1.ibm.net>`

```
In article <35ab6965.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:
>
>docdwarf@clark.net wrote in message <6ofngc$513$1@clarknet.clark.net>...
…[15 more quoted lines elided]…
>optimization.

I'm *terribly* sorry, it'll *never* happen again... and I won't post any
more PMAPs, either, no matter how much The Frog begs me.

DD
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 7)_

- **From:** "COBOLFrog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ABBE59.F93748E5@IMN.nl>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net> <35ab6965.0@news1.ibm.net> <6ofr06$c56$1@clarknet.clark.net>`

```


docdwarf@clark.net wrote:

> In article <35ab6965.0@news1.ibm.net>, Leif Svalgaard <leif@ibm.net> wrote:

8<

> ... here is a Cobol related, on-topic, DD posting offering compile time
> >optimization.
>
> I'm *terribly* sorry, it'll *never* happen again... and I won't post any
> more PMAPs, either, no matter how much The Frog begs me.

Would you please, please, please post less PMAPs.
I hate PMAPS.
I love DMAPS
I love jumps
period
.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 8)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ogrr2$61o$2@news.igs.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net> <35ab6965.0@news1.ibm.net> <6ofr06$c56$1@clarknet.clark.net> <35ABBE59.F93748E5@IMN.nl>`

```
>I love DMAPS
>I love jumps
>period
>.
But then you are a frog ...
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofvcj$9fs$1@news.igs.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6ofi5b$pt2$1@news.igs.net> <35ab5247.0@news1.ibm.net> <6ofngc$513$1@clarknet.clark.net> <35ab6965.0@news1.ibm.net>`

```
>>on a near-religious issue with some people, like using an asterisk in
>>col 7 on otherwise blank lines (but now I'm ranting, so I'll stop...)
…[3 more quoted lines elided]…
>


>Hey, for those of you that complained that DD never posted Cobol related
>stuff, here is a Cobol related, on-topic, DD posting offering compile time
>optimization.

So now we go on to religious issues do we? <S>.  That should
get it back to normal.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 7)_

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071422063600.SAA16429@ladder03.news.aol.com>`
- **References:** `<6ofvcj$9fs$1@news.igs.net>`

```
This question of readability and comfort can also harken back to
our youthful days as fledgling programmers.

A blank line without an * in column 7 was a no-no.
A sentence in the procedure division without a period was a no-no.
A field defined in working storage always begans with WS-.

Now the effort required for maintenance on this old code is
high indeed, and it behooves us all to make our maintenance
code look just like the original code so that the next poor sap that
comes along behind us won't be confused by the change in styles.

New code can look just like you want it to.  I don't think anyone
with a few years under their belt would have trouble with 
maintenance on either style.  But IMHO maintenance code that
looks like the original code is more likely to compile & run
cleaner, I guess due to the 'gestalt' or 'zen' of COBOL programming.

James Jones.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35abe8ce.0@news1.ibm.net>`
- **References:** `<6ofvcj$9fs$1@news.igs.net> <1998071422063600.SAA16429@ladder03.news.aol.com>`

```

JCJ0347 wrote in message
<1998071422063600.SAA16429@ladder03.news.aol.com>...
>Now the effort required for maintenance on this old code is
>high indeed, and it behooves us all to make our maintenance
>code look just like the original code so that the next poor sap that
>comes along behind us won't be confused by the change in styles.


absolutely agree
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 8)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ogs69$6i2$1@news.igs.net>`
- **References:** `<6ofvcj$9fs$1@news.igs.net> <1998071422063600.SAA16429@ladder03.news.aol.com>`

```
>New code can look just like you want it to.  I don't think anyone
>with a few years under their belt would have trouble with
>maintenance on either style.  But IMHO maintenance code that

Hear hear.  I think that anybody that consciously attempts to write
readable code will do so, and I would take their code over the code
of someone that religiously adheres to some "rule book of style"
anyday.  Style in coding can evolve in the same way that style in
any kind of writing can.  Many styles can be eminently readable.
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

_(reply depth: 8)_

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC09D3.3540@erols.com>`
- **References:** `<6ofvcj$9fs$1@news.igs.net> <1998071422063600.SAA16429@ladder03.news.aol.com>`

```
JCJ0347 wrote:
> 
> This question of readability and comfort can also harken back to
> our youthful days as fledgling programmers.

'Our'?  Who you callin' 'we', white man... remember there are folks
reading this newsgroup who've coded COBOL '85 only on PCs.
> 
> A blank line without an * in column 7 was a no-no.

... because it was inefficient during compiles; machines were *slow*.

> A sentence in the procedure division without a period was a no-no.

... because COBOL is English-like and in English sentences have periods
or else the sentence gets long and confusing or else there is too much
trying to be accomplished and maybe it should be broken down into more
discrete, easily-maintainable subcomponents or else there might be
another reason or else there might not?

> A field defined in working storage always begans with WS-.

... or WK-... to distinguish it from names in the FD (which always began
with the 8-digit file identifier signifying from which file it came so
it could be fit into the system it was taken from.)

You see? There's a reason for everything... as to whether it is a 'good'
reason or not we can debate... and lo, to discuss such matters at great
length is indeed praiseworthy.

DD
```

##### ↳ ↳ Re: The deal with the Inline Performs

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oemd6$ijk@bgtnsc02.worldnet.att.net>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
> 
> You see how harmful those periods are.
…[3 more quoted lines elided]…
> 

There are those who disagree with this, but I recommend it very highly.
Use the scope delimiters as religiously as you code END-EXEC for
CICS/COBOL.

Bill Lynch

> LVenick wrote in message
> <1998071401051700.VAA07236@ladder01.news.aol.com>...
…[19 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofp9v$jsu@lotho.delphi.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com> <35aab0a2.0@news1.ibm.net> <6oemd6$ijk@bgtnsc02.worldnet.att.net>`

```
I'm one of the ones that disagree. I do however, agree with the 
use of verbose scope deliminators. In fact I can't agree enough!
Especially in IF statements!!

-Paul


Bill Lynch (wblynch@att.net) wrote:
: Leif Svalgaard wrote:
: > 
: > You see how harmful those periods are.
: > Advise: NEVER use periods except when necessary and then
: > put them on line by themselves, then you will never again make
: > that (and similar) errors.
: > 

: There are those who disagree with this, but I recommend it very highly.
: Use the scope delimiters as religiously as you code END-EXEC for
: CICS/COBOL.

: Bill Lynch

: > LVenick wrote in message
: > <1998071401051700.VAA07236@ladder01.news.aol.com>...
: > >So here's the story....
: > >I  coded it without the IP
: > >Evaluate t-code
: > >     when '0'
: > >          move.....
: > >          add.....
: > >          add..
: > >      when '1'
: > >          etc....
: > >          etc....
: > >End-evaluate
: > >and it workes fine.  I was so happy i didn't bother doing it the other way
: > so
: > >I could get the error messages to share with you. Since I just moved the
: > >statements from the perform subroutine to the evaluate (after the 'when')
: > >there WAS a period after the last statement in each perform 'grouping', so
: > >there
: > >it is....the first period became the terminator for the Evaluate.
: > >Larry
: > >
```

###### ↳ ↳ ↳ Re: The deal with the Inline Performs

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071406005400.CAA17930@ladder01.news.aol.com>`
- **References:** `<6oemd6$ijk@bgtnsc02.worldnet.att.net>`

```
In article <6oemd6$ijk@bgtnsc02.worldnet.att.net>, Bill Lynch <wblynch@att.net>
writes:

>There are those who disagree with this, but I recommend it very highly.
>Use the scope delimiters as religiously as you code END-EXEC for
>CICS/COBOL.

Agreed! You wouldn't believe how many problems have been tracked down to an
extra period or a missing period. Scope terminators (END-IF, END-PERFORM,
END-EVALUATE, END-READ, END-STRING, etc.) really do find a lot of those kinds
of problems!

Mark A. Young
```

#### ↳ Re: The deal with the Inline Performs

- **From:** pvenkatesan@my-dejanews.com
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oggdr$pm8$1@nnrp1.dejanews.com>`
- **References:** `<1998071401051700.VAA07236@ladder01.news.aol.com>`

```
Yes, Its Obvious.
Any of the Scope Terminators like

   End-if, End-Evaluate, End-Read, End-Start ..etc..

 can be replaced with a period.

Venkat


In article <1998071401051700.VAA07236@ladder01.news.aol.com>,
  lvenick@aol.com (LVenick) wrote:
> So here's the story....
> I  coded it without the IP
…[17 more quoted lines elided]…
>


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
