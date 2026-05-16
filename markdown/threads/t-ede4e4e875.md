[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Philosophical "Wars" and what is or isn't "error-prone"

_22 messages · 9 participants · 1999-09_

---

### Philosophical "Wars" and what is or isn't "error-prone"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com>`

```
(A new thread - obviously as a follow-up to another in C.L.C.)
   (Sorry for sounding annoyed, but the "tone" of the previous thread does
have me annoyed.)

As most of those who read C.L.C. for any time know, I usually try to stay
out of the "religious wars" on what is or is not "error-prone" or "good
programming." Except to either "raise the question" or to report (often as a
possible source for the FAQ) on a summary of what I hear as all the sides of
the issue.  (Compare for example the previous SECTIONS/PARAGRAPH debates,
Efficiency/Readability debates, numbered-prefixes-or-not debates, and even
the previous Extensions/Portability discussions)

I do, however, have a STRONG bias against anyone who thinks that the method
that they know/like (are used to) is the ONLY way to avoid errors or to do
"good programming".  (I wasn't the author of the recent paint-brush/painter
discussion, but that's a great summary of my personal philosophy.)

IMHO,

Yes, there are some techniques that are more "prone" to be used to create
difficult to maintain source code. However, all of them can be used in
easy-to-maintain manners as well.

Yes, there are some techniques that are often "more efficient" on "more
platforms" than others - while other techniques (sometimes overlapping with
the previous - sometimes not) that are easier to maintain over the long
run - or to be "self-documenting" even in the short-run.

Yes, there are a variety of other issues that impact each programmer's
"selection" of the coding techniques that they use regularly or most
comfortably (or in code intended to be used more than once).

   BUT ...

To say (or imply) that some VALID (for *some* implementation) syntax,
standard, or other "coding technique" (or maintenance methodology or design
methodology, etc) is WRONG or awful or a "bug bomb" or other pejorative is
simply a matter of PREJUDICE - not a matter of God-Given-Truth.

For example, my experience has been that using a "bad technique" in a new
program - but where that technique is widely used and understood in a large
shop is a whole lot BETTER than using a "good technique" that no other
programmer will be able to maintain (or understand).  Clearly, if you are
developing code that will never be seen by any other programmer, this
doesn't apply - but you still shouldn't (IMHO) use techniques that you will
have trouble understanding when you get back to the problem in months or
years.

   ***

I *do* (obviously) have an opinion about "Next Sentence" (with or without
END-IF).

Given that COBOL
 - Does have sentences
 - Does support Next Sentence
 - Does even allow (in portable code) a Next Sentence in an IF terminated by
an END-IF (if you use the COPY technique that I documented elsewhere) - and
many/most implementations allow it without the COPY statement
 - Does CLEARLY define the difference between what a NEXT SENTENCE (clause)
and a CONTINUE (statement) does
 - Does FULLY support NEXT SENTENCE working identically in ANS'74 and ANS'85
(in either old or new code)

Then, if you, your programmers, or whoever doesn't know how to read,
maintain, and understand such code, I suggest that they learn how to.

I can't see that using "NEXT SENTENCE" as an EXPLICIT GO TO (which CONTINUE
is not) is any worse than using any other "GO TO" (of a exit that is defined
in the language construct).

Certainly there are people who think that any type of GO TO (including the
new "EXIT PERFORM" and "EXIT PARAGRAPH/SECTION" statements) are wrong,
error-prone, and hard to maintain.   They certainly are and always will be
"hard to understand" for those who haven't been trained in what they do.  As
someone who is visually impaired, I just find it hard (with today's tools)
to believe that the "deciding factor" should be how big a period (or
full-stop) is.  OTOH, if that really is what you (and your shop) is worried
about (on whether you can or cannot see periods), then "fine," let that be
your shop Standard - but don't tell me that the language is "flawed" because
it has a construct that uses it.

There are constructs in current COBOL Standard that are marked as "obsolete"
and I probably would encourage people to "flag" for these (occasionally) and
try and develop (new) code that avoids them. NEXT SENTENCE isn't in that
category.  (GO TO DEPENDING ON is - for those who wonder how I feel about
it. Although even it can be used in a maintainable manner in programs where
EVALUATE is not available.)

Bottom-Line:
   Do try and use the constructs in the COBOL language in a way that is
"clear" and "maintainable."  Please do not try and tell others that your
method is the only way of doing so.
```

#### ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7silov$uh4$1@nnrp1.deja.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com>`

```
Clap. Clap. Clap. Clap.....
-trblshtr-

In article <7shciv$sbd@dfw-ixnews5.ix.netcom.com>,
  "William M. Klein" <wmklein at ix dot netcom dot com> wrote:
> (A new thread - obviously as a follow-up to another in C.L.C.)
>    (Sorry for sounding annoyed, but the "tone" of the previous thread
does
> have me annoyed.)
>
> As most of those who read C.L.C. for any time know, I usually try to
stay
> out of the "religious wars" on what is or is not "error-prone" or
"good
> programming." Except to either "raise the question" or to report
(often as a
> possible source for the FAQ) on a summary of what I hear as all the
sides of
> the issue.  (Compare for example the previous SECTIONS/PARAGRAPH
debates,
> Efficiency/Readability debates, numbered-prefixes-or-not debates, and
even
> the previous Extensions/Portability discussions)
>
> I do, however, have a STRONG bias against anyone who thinks that the
method
> that they know/like (are used to) is the ONLY way to avoid errors or
to do
> "good programming".  (I wasn't the author of the recent paint-
brush/painter
> discussion, but that's a great summary of my personal philosophy.)
>
> IMHO,
>
> Yes, there are some techniques that are more "prone" to be used to
create
> difficult to maintain source code. However, all of them can be used in
> easy-to-maintain manners as well.
>
> Yes, there are some techniques that are often "more efficient" on
"more
> platforms" than others - while other techniques (sometimes
overlapping with
> the previous - sometimes not) that are easier to maintain over the
long
> run - or to be "self-documenting" even in the short-run.
>
…[7 more quoted lines elided]…
> standard, or other "coding technique" (or maintenance methodology or
design
> methodology, etc) is WRONG or awful or a "bug bomb" or other
pejorative is
> simply a matter of PREJUDICE - not a matter of God-Given-Truth.
>
> For example, my experience has been that using a "bad technique" in a
new
> program - but where that technique is widely used and understood in a
large
> shop is a whole lot BETTER than using a "good technique" that no other
> programmer will be able to maintain (or understand).  Clearly, if you
are
> developing code that will never be seen by any other programmer, this
> doesn't apply - but you still shouldn't (IMHO) use techniques that
you will
> have trouble understanding when you get back to the problem in months
or
> years.
>
>    ***
>
> I *do* (obviously) have an opinion about "Next Sentence" (with or
without
> END-IF).
>
…[3 more quoted lines elided]…
>  - Does even allow (in portable code) a Next Sentence in an IF
terminated by
> an END-IF (if you use the COPY technique that I documented elsewhere)
- and
> many/most implementations allow it without the COPY statement
>  - Does CLEARLY define the difference between what a NEXT SENTENCE
(clause)
> and a CONTINUE (statement) does
>  - Does FULLY support NEXT SENTENCE working identically in ANS'74 and
ANS'85
> (in either old or new code)
>
…[3 more quoted lines elided]…
> I can't see that using "NEXT SENTENCE" as an EXPLICIT GO TO (which
CONTINUE
> is not) is any worse than using any other "GO TO" (of a exit that is
defined
> in the language construct).
>
> Certainly there are people who think that any type of GO TO
(including the
> new "EXIT PERFORM" and "EXIT PARAGRAPH/SECTION" statements) are wrong,
> error-prone, and hard to maintain.   They certainly are and always
will be
> "hard to understand" for those who haven't been trained in what they
do.  As
> someone who is visually impaired, I just find it hard (with today's
tools)
> to believe that the "deciding factor" should be how big a period (or
> full-stop) is.  OTOH, if that really is what you (and your shop) is
worried
> about (on whether you can or cannot see periods), then "fine," let
that be
> your shop Standard - but don't tell me that the language is "flawed"
because
> it has a construct that uses it.
>
> There are constructs in current COBOL Standard that are marked as
"obsolete"
> and I probably would encourage people to "flag" for these
(occasionally) and
> try and develop (new) code that avoids them. NEXT SENTENCE isn't in
that
> category.  (GO TO DEPENDING ON is - for those who wonder how I feel
about
> it. Although even it can be used in a maintainable manner in programs
where
> EVALUATE is not available.)
>
> Bottom-Line:
>    Do try and use the constructs in the COBOL language in a way that
is
> "clear" and "maintainable."  Please do not try and tell others that
your
> method is the only way of doing so.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sjfbu$rka$1@aklobs.kc.net.nz>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com>`

```
trblshtr <trblshtr@my-deja.com> wrote:
:>
:> To say (or imply) that some VALID (for *some* implementation) syntax,
:> standard, or other "coding technique" (or maintenance methodology or
: design
:> methodology, etc) is WRONG or awful or a "bug bomb" or other
: pejorative is
:> simply a matter of PREJUDICE - not a matter of God-Given-Truth.

It is the Cobol standard that says that mixing NEXT SENTENCE
and END-IF is WRONG.  This is not an issue of prejudice but
of Committee-Given-Truth.

:>
:> For example, my experience has been that using a "bad technique" in a
: new
:> program - but where that technique is widely used and understood in a
: large
:> shop is a whole lot BETTER than using a "good technique" that no other
:> programmer will be able to maintain (or understand).  Clearly, if you

Exactly.  If they are used to NEXT SENTENCE and full-stops then
they should not be introduced to END-IF because they won't
be able to maintain or understand it </sarcasm>.

There is _nothing_ wrong with leaving NEXT SENTENCE in programs
as long as they are not in combination with END-IF (as I had
previously stated).  This is not a "bad technique".  However,
mixing NEXT SENTENCE and END-IF is disallowed by the standard
for good reasons and techniques to defeat this (and to hide
the deviousness in a COPY) can be interpreted as malicious.

:> Given that COBOL
:>  - Does have sentences
:>  - Does support Next Sentence
:>  - Does even allow (in portable code) a Next Sentence in an IF
: terminated by
:> an END-IF (if you use the COPY technique that I documented elsewhere)
: - and

No, it does not allow a NEXT SENTENCE in an IF terminated by an
END-IF.  In your example the outer IF was terminated by an
END-IF, the inner IF that contained the NEXT SENTENCE was
terminated by the ELSE of the outer IF.

:> many/most implementations allow it without the COPY statement
:>  - Does CLEARLY define the difference between what a NEXT SENTENCE
: (clause)
:> and a CONTINUE (statement) does
:>  - Does FULLY support NEXT SENTENCE working identically in ANS'74 and
: ANS'85
:> (in either old or new code)
:>
:> Then, if you, your programmers, or whoever doesn't know how to read,
:> maintain, and understand such code, I suggest that they learn how to.

Oh I certainly know how to read and understand such code.  I also
know how to maintain it - making it fit the intent of the
standard for the language.

But anyone used to _STANDARD_ COBOL will have problems with
your code.


:> I can't see that using "NEXT SENTENCE" as an EXPLICIT GO TO (which
: CONTINUE
:> is not) is any worse than using any other "GO TO" (of a exit that is
: defined
:> in the language construct).

Your lack of being able to see why it is worse is beside the point.

The problem is that you are concentrating on the NEXT SENTENCE
clause and the GO TO aspects of it and are missing completely
the implications of the target of these.

There is nothing wrong with a GO TO or a NEXT SENTENCE (when
not mixed with END-IF) or any other explicit control where
the target of these is _also_ explicit.

That is, if I see a label then I am alerted that this is a 
place to which transfer of control is made.  If I remove
that label then the compiler gives me an error if it was
used.  The label itself is sufficient to trigger the care
that is required in dealing with the code around it.

In the case of NEXT SENTENCE without END-IF the terminating
full stop is part of the IF statement and thus there is
a contained area of logic flow.

Use of NEXT SENTENCE and END-IF uses an anonymous label
(the next ful stop somewhere in the code) that is not
part of the IF statement.

Adding and removing full stops, deliberately or naievely,
will cahnge the effect of code that is not part of what
is being changed.

Similarly changing the END-IF back to a full stop will aslo
change (add bugs) when it alters the flow outside the IF
statement.

:> your shop Standard - but don't tell me that the language is "flawed"
: because
:> it has a construct that uses it.

While it may be that the standards committe were less vigilant
than those that want to abuse the standard, it is not the
language that is flawed - the standard prohibits this use 
for good reason.  It is your wanting to abuse the language
that is the flaw in your argument.

:> Bottom-Line:
:>    Do try and use the constructs in the COBOL language in a way that
: is
:> "clear" and "maintainable."  Please do not try and tell others that
: your
:> method is the only way of doing so.

I entirely agree with you, but you are using constructs that
are not in the Cobol language (or only so due to extreme
misinterpretation of the intent), are _not_ clear and are
_not_ "maintainable".

While you have continued to tell others "the way to do so",
I have not even disclosed 'my method', let alone claimed
it as 'the only way'.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sk2fd$hkq@dfw-ixnews3.ix.netcom.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
>
> There is nothing wrong with a GO TO or a NEXT SENTENCE (when
…[7 more quoted lines elided]…
> that is required in dealing with the code around it.

I assume that this means that you don't like the EXIT
PERFORM/PARAGRAPH/SECTION enhancements that are in the draft of the next
COBOL Standard.  This NG has already discussed them in detail, so I won't go
thru them again - but all of them very definitely "go  to an unlabeled"
point in the program.  If you strongly disagree with this "functionality"
(now not only being enhanced - but actually be added as a new feature - for
the next Standard)  I would suggest that you contact J4/WG4 "quickly" so
that your views can be considered during -or before - the next (quite
possibly final) public review period for the upcoming Standard.

Note:  In some ways, it always struck me that when the committees decided to
add the EXIT options, that they should have added a (synonym) for NEXT
SENTENCE of "EXIT SENTENCE". This would be "symetrical" with what each of
the new (not old) variations of EXIT does.  On the other hand, as the
current "NEXT SENTENCE" is a clause and the new EXIT variations are
statements, I don't really think this is needed.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sklfa$2j8$3@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sk2fd$hkq@dfw-ixnews3.ix.netcom.com>`

```
    The exit perform, etc constructs are self documenting, and as such
should be more or less trouble free.

    But if your code depends on the puesdo go to formed by a next sentence,
an end without a period, some more lines of code, followed by a period, than
mayby you should consider a perform thru for clarity.  The only time that I
normally get in real trouble is when I copy a set of paragraphs,  make small
changes, and forget to change an internal go to.  Why can't the compiler
flag that sort of thing.  Also performing a paragraph that is part of a
perform range.  The closest MF comes is a warning about inefficient code,
and you get that only when you generate.




William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7sk2fd$hkq@dfw-ixnews3.ix.netcom.com...
> Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
> >
…[12 more quoted lines elided]…
> COBOL Standard.  This NG has already discussed them in detail, so I won't
go
> thru them again - but all of them very definitely "go  to an unlabeled"
> point in the program.  If you strongly disagree with this "functionality"
> (now not only being enhanced - but actually be added as a new feature -
for
> the next Standard)  I would suggest that you contact J4/WG4 "quickly" so
> that your views can be considered during -or before - the next (quite
> possibly final) public review period for the upcoming Standard.
>
> Note:  In some ways, it always struck me that when the committees decided
to
> add the EXIT options, that they should have added a (synonym) for NEXT
> SENTENCE of "EXIT SENTENCE". This would be "symetrical" with what each of
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s1MH3.578$X71.5692@news4.mia>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sk2fd$hkq@dfw-ixnews3.ix.netcom.com> <7sklfa$2j8$3@ssauraac-i-1.production.compuserve.com>`

```
Russell Styles wrote:
>
>    But if your code depends on the puesdo go to formed by a next sentence,
…[6 more quoted lines elided]…
>and you get that only when you generate.

This is one of the advantages of using paragraph numbers and a source
code checker.  When you move the paragraphs, you do a search/replace
on the paragraph numbers (e.g. replace " 123???-" by " 456???-"), and
it also fixes any GOTO or PERFORM statements that refer to them.  The
code checker catches all PERFORM THRU wrong exits.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sl8l6$kci$1@nnrp1.deja.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz>`

```
In article <7sjfbu$rka$1@aklobs.kc.net.nz>,
  Richard Plinston <riplin@kcbbs.gen.nz> wrote:
> trblshtr <trblshtr@my-deja.com> wrote:
> :>
> :> To say (or imply) that some VALID (for *some* implementation)
syntax,
<snipped a lot>

Actually Mr. Plinston, Mr. Klein wrote that which you erroneously
attributed to myself.  I do applaud Mr. Klein's attempt to point out
that "my way..your way" *arguments* are often counterproductive.  As
regards the specific argument concerning 'next sentence' with end-if:
1) I, generally, avoid use of next sentence.
2) next sentence's action is, however, clearly defined.
3) You have been arguing in the initial thread that it "should" not be
used with end-if.
4) Mr. Klein has been arguing that it, like any other COBOL tool, "can"
be used.
I happen to agree that it "should not" but I also agree with Mr.
Klein's indicated position that if it is *needed* to accomplish a
specific action it's use is just as valid as the use of any other tool
in the kit.  Accomplishing the task at hand, at least sometimes,
supercedes whether something "should", or "should not", be done.

Cordially,
-trblshtr-
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7spqpd$2h8$1@aklobs.kc.net.nz>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com>`

```
trblshtr <trblshtr@my-deja.com> wrote:

: 2) next sentence's action is, however, clearly defined.

I am not sure that this is actually the case when used as
Klein suggested.

NEXT SENTENCE and END-IF are disallowed in the same IF
statement, however if NEXT SENTENCE is used in an inner
IF that does not have an END-IF but relies on being 
terminated by an outer IF's ELSE, then it may not
technically be disallowed (IMHO because the committee 
was not vigilant enough in eliminating misinterpretations).

In the case of MF they define the action of this inner
NEXT SENTENCE as being equivalent to CONTINUE (in some
earlier compilers or when OLDNEXTSENTENCE is specified)
or to go to the end of the current sentence indicated by
the next full stop even if this is outside the scope of 
the IF.

Fujitsu, however, do not word it this way.  They have:

 "When NEXT SENTENCE is written, control passes to the
execution sentence [sic] following the IF statement".

and

"The END-IF statement delimits the scope of an IF statement".

Now I doubt that Fujitsu considered the mix of NEXT SENTENCE
and END-IF as they are clearly disallowed, but these two
rules seem to imply that Klein's example would have
NEXT SENTENCE operate as MF's OLDNEXTSENTENCE in that it
would go to the end of the outer IF.

In fact it seems to go to the next full stop, but I 
certainly wouldn't rely on it in any compiler except
MF, and would not do so there because the behaviour 
may be changed.

Do you still think that NEXT SENTENCE is clearly defined
in this case ?  (It certainly is clear, unambiguous, and
useful where END-IF is not used).
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sq62j$6do@dfw-ixnews12.ix.netcom.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz>`

```
Yes,
  "Next Sentence" is clearly defined.  Please notice that your "sic" was
required to even make the Fujitsu situation ambiguous.  In COBOL a statement
is NOT the same thing as a sentence.  Both of these are clearly defined in
COBOL and are not the same thing.  NEXT SENTENCE goes to the "next
sentence" - NOT the "next statement".

It is true that with the MF "OLDNEXTSENTENCE" directive, you can change
that.  But you can also change the meaning of the MOVE statement with almost
every compiler that I know by using the "TRUNC" (or equivalent) directive or
compiler option.

Part of the vendor documentation is what impact directives have on
semantics.  This doesn't make it less well defined - or change what the
"base" meaning is, it just says that the vendor/compiler gives you one or
more options for OTHER *well defined* behavior.

NOTE:
  I am quite familiar with a BUNCH of MF directives that start "OLD" that
are for compatibility with behavior of previous compilers that MAY have been
"bugs" or may have been something else.  When MF did have a compiler that
treated "NEXT SENTENCE" like a CONTINUE, it was simply a bug - and I don't
think you will find any current MF documentation that says anything more
positive about it.  They could have just "fixed the bug" (and changed
program behavior - for existing customers - as some vendors did/do.)
However, they provided an option for continuing this behavior - and when you
select it you are running in non-Standard conforming mode - just as you are
when you use the IBM NOTRUNC/TRUNC(BIN) compiler option - which is
"required" when interacting with some other software.  So what does that
"prove"? Nothing.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sr3v6$cmc$1@aklobs.kc.net.nz>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com>`

```
William M. Klein <wmklein@nospam.netcom.com> wrote:
: Yes,
:   "Next Sentence" is clearly defined.  Please notice that your "sic" was
: required to even make the Fujitsu situation ambiguous.  In COBOL a statement
: is NOT the same thing as a sentence.  Both of these are clearly defined in
: COBOL and are not the same thing.  NEXT SENTENCE goes to the "next
: sentence" - NOT the "next statement".

When NEXT SENTENCE is used according to the standard the next sentence
_is_ the next statement after the IF because there must be a
terminating period for the IF statement.

MF think this is the case because an ANS85 directive will flag
your code as non-standard.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 7)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sr52l$9s2$1@nntp6.atl.mindspring.net>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com> <7sr3v6$cmc$1@aklobs.kc.net.nz>`

```
"The NEXT SENTENCE verb transfers control to the next COBOL sentence, that
is, following the next period. It does not transfer control to the logically
next COBOL verb as occurs with the  CONTINUE verb. "

"When OLDNEXTSENTENCE is specified, the NEXT SENTENCE statement behaves like
a CONTINUE statement."

As taken directly from the online help for netexpress...


Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7sr3v6$cmc$1@aklobs.kc.net.nz...
> William M. Klein <wmklein@nospam.netcom.com> wrote:
> : Yes,
> :   "Next Sentence" is clearly defined.  Please notice that your "sic" was
> : required to even make the Fujitsu situation ambiguous.  In COBOL a
statement
> : is NOT the same thing as a sentence.  Both of these are clearly defined
in
> : COBOL and are not the same thing.  NEXT SENTENCE goes to the "next
> : sentence" - NOT the "next statement".
…[9 more quoted lines elided]…
> --
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sr9hr$242@dfw-ixnews8.ix.netcom.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com> <7sr3v6$cmc$1@aklobs.kc.net.nz>`

```
I really (well almost) want to drop this whole conversation - because I have
lost any concept of what Richard is really trying to say (and I am getting
so that I don't believe that anyone who reads this NG via Deja.Com or online
will care much either), but ... in terms of "next sentence" really means
"next statement" - if you are ANSI/ISO conforming, it seems silly that
anyone would really suggest this. (Certainly the Standard has never said
it - and no vendor's documentation that I have read says this. Unless you
are using a "syntax modifying directive like OLDNEXTSENTENCE - but I think
that just as NOTRUNC changes MOVE, we can drop that irrelevance.) However,
just to make it clear that this isn't true (never was, never will be)
consider the following ANSI/ISO conforming (and not particularly obscure or
unusual situation) code:

If SomeField = "XYZ
   Search aTable
       When anItem (ind) = "ABC"
             Next Sentence
Else
    Perform Whatever
End-If
Display "In next Statement but, Still in same sentence"
  .
Display "In next Sentence"
 .
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F13785.2FF3D62@home.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com> <7sr3v6$cmc$1@aklobs.kc.net.nz> <7sr9hr$242@dfw-ixnews8.ix.netcom.com>`

```
William M. Klein wrote:
> 
> I really (well almost) want to drop this whole conversation - because I have

What a good idea. We are getting nowhere. Use what you want, when you
want. Get it wrong and you are soon going to find out when the irate
user says ".............".

Jimmy
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 8)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F1A19B.C5E8943D@att.net>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com> <7sr3v6$cmc$1@aklobs.kc.net.nz> <7sr9hr$242@dfw-ixnews8.ix.netcom.com>`

```
"William M. Klein" wrote:
> 
> I really (well almost) want to drop this whole conversation

Hear, hear, I'll second that. (should I call someone a Nazi?)

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 9)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AWqI3.23$W33.2701@typhoon01.swbell.net>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com> <7sr3v6$cmc$1@aklobs.kc.net.nz> <7sr9hr$242@dfw-ixnews8.ix.netcom.com> <37F1A19B.C5E8943D@att.net>`

```
> Hear, hear, I'll second that. (should I call someone a Nazi?)


I heard the operative rule is that a thread continues until
someone brings up Hitler. I guess you just did.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 10)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F2F57F.3CCDB095@att.net>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz> <7sq62j$6do@dfw-ixnews12.ix.netcom.com> <7sr3v6$cmc$1@aklobs.kc.net.nz> <7sr9hr$242@dfw-ixnews8.ix.netcom.com> <37F1A19B.C5E8943D@att.net> <AWqI3.23$W33.2701@typhoon01.swbell.net>`

```
Jerry P wrote:
> 
> > Hear, hear, I'll second that. (should I call someone a Nazi?)
> 
> I heard the operative rule is that a thread continues until
> someone brings up Hitler. I guess you just did.

QED, thread's over.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 5)_

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sr9ja$p5e$1@nnrp1.deja.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7silov$uh4$1@nnrp1.deja.com> <7sjfbu$rka$1@aklobs.kc.net.nz> <7sl8l6$kci$1@nnrp1.deja.com> <7spqpd$2h8$1@aklobs.kc.net.nz>`

```
In article <7spqpd$2h8$1@aklobs.kc.net.nz>,
  Richard Plinston <riplin@kcbbs.gen.nz> wrote:
> trblshtr <trblshtr@my-deja.com> wrote:
>
…[44 more quoted lines elided]…
>
Mr. Plinston,
You have taken that piece of my prior post somewhat out of the overall
context of that post(i.e. "can" vs "should").  However, because you
asked:  It *is* "difficult" to surmise the exact action which will
occur given "just" the documentation and, within *that* context, I
would agree that it is *not* "clearly defined".  That said: IMHO *some*
action will occur.  Whatever that action is will, usually, be
consistent given the specific compiler/system in use.  Once that action
has been determined, and verified as to consistency, one could then
state that the action is "clearly defined".  That being the case it is
valid to also state that, like any other language tool, it *can* be
used.  More to the point: it comes back to programming "style".  One
style is just as valid as any other and, while we all tend to judge
style, in the final analysis it should not be the final determinant as
to what can, or cannot, be accomplished with COBOL; or any other
programming language.  As to "style": I happen to dislike the use of
next sentence with, or without, end-if.
-trblshtr-
```

#### ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sj8cs$b4u$1@nnrp1.deja.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com>`

```
Clarification of prior post:

<applause>
```

##### ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ED514C.4570EEEB@home.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7sj8cs$b4u$1@nnrp1.deja.com>`

```
trblshtr wrote:
> 
> Clarification of prior post:
> 
> <applause>

I doubt anybody thought you meant a dose of the clap !

And as for 'Applause' as Bill is saying, there is more than one way to
skin a cat. (As a rider for the facetious - God help you if you try to
skin one of my two !)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ohhH3.721$dV4.43015@typhoon01.swbell.net>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7sj8cs$b4u$1@nnrp1.deja.com> <37ED514C.4570EEEB@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:37ED514C.4570EEEB@home.com...

> And as for 'Applause' as Bill is saying, there is more than one way
to
> skin a cat. (As a rider for the facetious - God help you if you try
to
> skin one of my two !)

Not to worry. The expression "To skin a cat" refers to removing
the hide from a catfish (which has no scales). The expression
does not refer to adorable little kitten-kittens. Oooo, kootchie-
coo. Meow.
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EDB15C.B4E10446@home.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7sj8cs$b4u$1@nnrp1.deja.com> <37ED514C.4570EEEB@home.com> <ohhH3.721$dV4.43015@typhoon01.swbell.net>`

```
Jerry P wrote:
> 
> James J. Gavan <jjgavan@home.com> wrote in message
…[11 more quoted lines elided]…
> coo. Meow.

DAMN. ! And I thought I'd covered my a.... by putting the rider in !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Philosophical "Wars" and what is or isn't "error-prone"

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sl8pc$kk6$1@nnrp1.deja.com>`
- **References:** `<7shciv$sbd@dfw-ixnews5.ix.netcom.com> <7sj8cs$b4u$1@nnrp1.deja.com> <37ED514C.4570EEEB@home.com>`

```
In article <37ED514C.4570EEEB@home.com>,
  "James J. Gavan" <jjgavan@home.com> wrote:
> trblshtr wrote:
> >
…[5 more quoted lines elided]…
>
Well, actually....
-trblshtr-
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
