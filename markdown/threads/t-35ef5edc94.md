[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Collaborative Article on COBOL

_25 messages · 10 participants · 1999-09_

---

### Collaborative Article on COBOL

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990922120110.00284.00000917@ng-fs1.aol.com>`

```
Ed Milne writes ...

[snip my orignal post]

>Your list doesn't include the inadvertent problems that occur on
>coversions and the costs they entail. It sounds like your article is
>entended to sell the concept of upgrading to the latest COBOL regardless
>of the cost.

Well, I wouldn't put it exactly like that. But I do believe in keeping my tools
up to date. 

>To show the other side of the story consider the following list of
>conversion traps T 

(typo for "I"?)

>made up when converting IBM VS/COBOL (ANSI 74) to
>COBOL II (ANSI 84).

Well, ANSI 85

>
>
…[24 more quoted lines elided]…
>VS/COBOL.

What COBOL II did was enforce the rules better than OS/VS COBOL. The programmer
using a picture of S9 is telling the compiler that only values -9 to +9 are
valid. COBOL II says, "OK, I'll take you at your word because you wouldn't lie
to me."

The cause here was really not paying attention to details in the first place. A
good programmer would not have been so sloppy in the first place. The
conversion was good because it caught these kinds of errors in addition to
bringing you the benefits of the new compiler.


>
>
…[26 more quoted lines elided]…
>physical size of the space used. 
I have always taught that packed fields shoud be defined with an odd number of
digits because that's how the hardware stores packed data. Again, this problem
has to do with careless programming, not any change in the language or
compiler.

>However, some fields, such as dates,
>should only have an even number of digits.
>

Not necessarily. There are lots of ways to store dates. In Julian formats, for
example (yyddd or yyyyddd or dddyy or dddyyyy) there are an odd number of
digits. You can store year, month, and day in separate binary, packed, or
display fields. I have become convinced that the right way to store dates is as
eight bytes of display data in yyyymmdd order.



>
>NEXT SENTENCE
…[30 more quoted lines elided]…
>

But you don't have to do this as part of the conversion. The old code would
have worked fine. You chose to use the new features because you get some
benefit (easier to code, read, maintain). But you have to pay attention to
details.

Yes, I guess overall I would say the conversion was good for you because it
caught careless practices and therefore made your code more robust. This is
truly a benefit, even if one unlooked for.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Collaborative Article on COBOL

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sb9nn$nen$1@aklobs.kc.net.nz>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com>`

```
:>NEXT SENTENCE
:>After converting a program to COBOL II, it is natural to use the COBOL
:>II structures for ending statements rather than
:>periods for new code. This mix of old and new code can cause problems
:>with the NEXT SENTENCE clause in existing
:>statements.
:>
:>For example, in the following code
:>
:>    IF <test> THEN
:>      NEXT SENTENCE
:>    ELSE
:>      <move statement>
:>    END-IF
:>    <add statement>.
:>    <subtract statement>
:>
:>if the test is true, the next statement executed is the <subtract
:>statement> rather than the expected <add statement>. This happens
:>because a "NEXT SENTENCE" clause continues following the next period
:>rather than with the next statement.

NEXT SENTENCE and END-IF are invalid in the same statement.  Your
compiler may allow this but the standard doesn't.  The code above
should be rejected.
```

##### ↳ ↳ Re: Collaborative Article on COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sbjkh$944@dfw-ixnews13.ix.netcom.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7sb9nn$nen$1@aklobs.kc.net.nz...
  <snip>
>
> NEXT SENTENCE and END-IF are invalid in the same statement.  Your
> compiler may allow this but the standard doesn't.  The code above
> should be rejected.
>

1) It is true that this is illegal according to the Standard.

2) (As far as I know) More compilers allow it (as an extension) than
prohibit it.

3) This "restriction" in the Standard is actually a totally USELESS
restriction, because the Standard does allow the following code:

NextSentence is the name of a "copy member" and it includes

   If A = A
       If A not= A
            Continue
       Else
             Next Sentence
   Else
            Continue
   End-IF

    ***
 then wherever you want to use NEXT SENTENCE in an "IF" that is terminated
with END-IF, you can (add a WS item called "A" with any old value) and code
the ANSI CONFORMING

   IF   whatever
          copy NextSentence.
   Else
         do something else
   End-IF


   ***

The reason that this is conforming - but using a NEXT SENTENCE instead of
the COPY statement, is fairly "obscure" but has been conformed by J4 and WG4
as "true".
```

##### ↳ ↳ Re: Collaborative Article on COBOL

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EBB00E.C6BE3B28@NOSPAMhome.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:

> NEXT SENTENCE and END-IF are invalid in the same statement.  

Why???  (why doesn't the standard allow it?)

> Your compiler may allow this but the standard doesn't.  

I bet most compilers allow it.

> The code above should be rejected.

Unless you have good reason for allowing it.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sgn1g$3rq$1@aklobs.kc.net.nz>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:

:> NEXT SENTENCE and END-IF are invalid in the same statement.  

: Why???  (why doesn't the standard allow it?)

Because a mix of NEXT SENTENCE and END-IF is a sure-fire
bug generator.  If you were to write code that mixed these
then you may well know to avoid creating bugs around those
areas, but the _next_ programmer that follows on these is
bound to fall into your traps.

Consider AMSI-74:

       IF ( something )
           NEXT SENTENCE
       ELSE
           staements
           .

The NEXT SENTENCE is defined as, and acts as, a GO TO to the
anonymous label formed by the full stop.  The placement of
this label is forced by the syntax to be the termination of
the IF (or of all active IFs).

When ANSI-85 END-IF is added:

         IF ( something )
             NEXT SENTENCE
         ELSE
             statements
          END-IF
         .    <- full stop 1
         lines of statements
         .    <- full stop 2

The IF ... END-IF is a complete statement and does not require
full stop 1.  The only requirement for a full-stop is at the
end of the paragraph.  If the NEXT SENTENCE had been used
deliberately (maliciously) or naievely to go to a full stop
and full stop 1 was removed, or lines were added between the
END-IF and full-stop 1, then the effect of the NEXT SENTENCE
is to go to the wrong place.

This means that changes _outside_ the IF statement affect the
action of that IF statement.  This makes the mix of NEXT 
SENTENCE and END-IF in the same category as ALTERed GO TOs.

If fact it makes it worse because the full stop is anonymous
and may usually be considered a matter of style when outside
a conditional statement.

If, for example, full stop 1 was ommitted to deliberately
cause the NEXT SENTENCE to GO TO full stop 2 and an extra
line was added in 'lines of statements' then the effect of
this addition would be different if it was done by an 'always
add a full-stop' programmer or a 'only at end of paragraph'
programmer.  And this is _outside_ a conditional.

:> Your compiler may allow this but the standard doesn't.  

: I bet most compilers allow it.

Microfocus seems unable to detect the problem because it
has NEXT SENTENCE as a staement in its own right rather than
a clause of the IF statement (or as well as).  But whether
the compiler allows it, or more specifically does not
flag it as an error, is irrelevant.  There are many things
that compilers do not give compiler errors on that are
disallowed by the standard.

:> The code above should be rejected.

: Unless you have good reason for allowing it.

There no _good_ reasons.  There may be _bad_ reasons (such
as maliciously wanting to trap the next programmer or ensuring
full employment in fixing ever more obscure bugs).

Of course, if you can think of a _good_ reason (laziness
doesn't count) then please do state what it might be.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sgomk$f46@dfw-ixnews10.ix.netcom.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7sgn1g$3rq$1@aklobs.kc.net.nz...
> Howard Brazee <brazee@nospamhome.com> wrote:
>
  <snip>
>
> : I bet most compilers allow it.
…[8 more quoted lines elided]…
>

This is simply "hogwash".

There is a SIGNIFICANT difference between extensions and errors.

Micro Focus has many *documented* EXTENSIONS - and UNDER NO CIRCUMSTANCES
should a documented extension get an error.

Micro Focus (like *ALL* ANSI/ISO/FIPS conforming compilers) provides a
FLAGGING (not error) method for detecting "NEXT SENTENCE" in an IF
terminated with an End-IF (or in other cases where the Standard doesn't
allow them).

It is true that some compilers do "miss" some errors - but most of them will
take "error/bug reports" on such situations - but please, PLEASE, don't
confuse what the Standard allows with what is required to get "error"
messages.

If you don't know how to get MF (or Fujitsu, or IBM, or any other compiler)
to issue "non-conformance" messages, then check their documentation.

(I will respond to some of the other parts of this "I hate NEXT SENTENCE"
diatribe in a separate note, but this just needed its own reply - because it
is so off base.)
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sh6t9$7hj$1@aklobs.kc.net.nz>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <7sgomk$f46@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein <wmklein@nospam.netcom.com> wrote:
:> Microfocus seems unable to detect the problem because it
:> has NEXT SENTENCE as a staement in its own right rather than
:> a clause of the IF statement (or as well as).  But whether
:> the compiler allows it, or more specifically does not
:> flag it as an error, is irrelevant.  There are many things
:> that compilers do not give compiler errors on that are
:> disallowed by the standard.

: This is simply "hogwash".

Which bits are 'hogwash' ?

: There is a SIGNIFICANT difference between extensions and errors.

: Micro Focus has many *documented* EXTENSIONS - and UNDER NO CIRCUMSTANCES
: should a documented extension get an error.

They do in the circumstance of having a NOMF directive.

I obviously have to spell out my statement in more detail.  There
are things that the standard disallows, and are not extensions,
that do not generate compiler errors or flags.

For example: directly or indirectly recursive performs.

: Micro Focus (like *ALL* ANSI/ISO/FIPS conforming compilers) provides a
: FLAGGING (not error) method for detecting "NEXT SENTENCE" in an IF
: terminated with an End-IF (or in other cases where the Standard doesn't
: allow them).

: It is true that some compilers do "miss" some errors - but most of them will
: take "error/bug reports" on such situations - but please, PLEASE, don't
: confuse what the Standard allows with what is required to get "error"
: messages.

Who were you thinking made this confusion ?

: If you don't know how to get MF (or Fujitsu, or IBM, or any other compiler)
: to issue "non-conformance" messages, then check their documentation.

: (I will respond to some of the other parts of this "I hate NEXT SENTENCE"
: diatribe in a separate note, but this just needed its own reply - because it
: is so off base.)

Actually the 'diatribe' was 'I hate bug bombs' while answering
the question as why NEXT SENTENCE was disallowed by the standards
committee in IF ... END-IF.
```

###### ↳ ↳ ↳ Next Sentence, etc (was: Collaborative Article on COBOL

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sha5q$rid@dfw-ixnews5.ix.netcom.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <7sgomk$f46@dfw-ixnews10.ix.netcom.com> <7sh6t9$7hj$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:7sh6t9$7hj$1@aklobs.kc.net.nz...

>
> : Micro Focus has many *documented* EXTENSIONS - and UNDER NO
CIRCUMSTANCES
> : should a documented extension get an error.
>
> They do in the circumstance of having a NOMF directive.

Have you ever read the MF documentation?  It has been quite a while since I
had to explain what the various compiler directives do in MF.  (These are
all well documented in the MF manuals - but you seem unable to understand
what they say.)

MF, OSVS, VSC2, etc are a set of directives which ONLY determine which
Reserved Words are "turned on" for a specific compilation.  They do not
(directly) impact what syntax is or is not supported.  Therefore, if a
specific "syntax construct" does not require any reserved words outside of
the set supported by the language directives selected, that syntax is
supported.  (For example, the words "NEXT" and "SENTENCE" are included with
EVERY language dialect possible - including NOMF.)

ON THE OTHER HAND,  there are also a set of "flagging" directives which are
aimed at determining whether a certain piece of syntax is or is not
supported in the dialect chosen.  For example, FLAG(ANS85) will detect ALL
"extensions" which are not part of the ANSI Standard.  (There is a slight
difference betweent the FLAG(ANS85) and FLAGSTD directives - which is best
documented by MF.  But the bottom-line is that the former is for ANSI
conformance while the latter is follows the FIPS rules - the 2 are quite
similar but the format of messages differs.)

Similarly FLAG(OSVS), FLAG(VSC2), etc check for syntax outside the language
definitions of those products.

There are a couple of other options that MF offers that can "modify" the
"severity level" of flagging messages (either on a universal level - or
message-by-message).

   ***

Each compiler (that I know of) has various types of messages and methods of
selecting "dialects".  Compare the OS/VS COBOL "LANGLVL(1)" and "LANGLVL(2)"
options - which are often misunderstood as ANS74 and ANS68.

Bottom-Line: (as I said originally) - If a vendor documents something as an
extension and you have selected the options that specify for ALLOWING their
extensions, then the extensions should not (EVER) get an error message.
```

###### ↳ ↳ ↳ Re: Next Sentence, etc (was: Collaborative Article on COBOL

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ec2fc0@news3.prserv.net>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <7sgomk$f46@dfw-ixnews10.ix.netcom.com> <7sh6t9$7hj$1@aklobs.kc.net.nz> <7sha5q$rid@dfw-ixnews5.ix.netcom.com>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7sha5q$rid@dfw-ixnews5.ix.netcom.com...
> Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
> news:7sh6t9$7hj$1@aklobs.kc.net.nz...
>
> Have you ever read the MF documentation?  It has been quite a while since
I
> had to explain what the various compiler directives do in MF.  (These are
> all well documented in the MF manuals - but you seem unable to understand
> what they say.)

Don't be so hard on the poor guy. I can sympathize with him. Last time I
counted
(it was in April 1993) there were 300+ compiler options; many of which with
intricate
interdependencies. It is not an easy task to navigate this maze to find what
will work for you. I have several grey hairs in several places that without
a doubt
are due to the grief MF compiler options have caused me.
```

###### ↳ ↳ ↳ Re: Next Sentence, etc

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7shvea$da0$1@aklobs.kc.net.nz>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <7sgomk$f46@dfw-ixnews10.ix.netcom.com> <7sh6t9$7hj$1@aklobs.kc.net.nz> <7sha5q$rid@dfw-ixnews5.ix.netcom.com>`

```
William M. Klein <wmklein@nospam.netcom.com> wrote:
: Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
: news:7sh6t9$7hj$1@aklobs.kc.net.nz...

:> : Micro Focus has many *documented* EXTENSIONS - and UNDER NO
: CIRCUMSTANCES
:> : should a documented extension get an error.
:>
:> They do in the circumstance of having a NOMF directive.

: Have you ever read the MF documentation?  It has been quite a while since I

Quite right, what I should have said is: They do in the
circumstance of having a FLAG"ANS85" and FLAGAS"E".

: had to explain what the various compiler directives do in MF.  (These are
: all well documented in the MF manuals - but you seem unable to understand
: what they say.)

Oh please do give me a full explanation of all these options.

: Bottom-Line: (as I said originally) - If a vendor documents something as an
: extension and you have selected the options that specify for ALLOWING their
: extensions, then the extensions should not (EVER) get an error message.

That's not what you said originally, you have now added provisos
about selected options when originally you said 'never under
any circumstances'.

Also, you may note that the FLAG directive does not "ALLOW" or
"DISALLOW" extensions, it only flags them.  In the case of
flagging them as 'I'nformational this does not stop the
compilation or disallow the extension.

Even when it does give an error message the code will still
run.  So I can get an error message without disallowing the
extension.

(Unlike what you said).
```

###### ↳ ↳ ↳ Re: Next Sentence, etc (was: Collaborative Article on COBOL

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sojb9$cku@dfw-ixnews10.ix.netcom.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <7sgomk$f46@dfw-ixnews10.ix.netcom.com> <7sh6t9$7hj$1@aklobs.kc.net.nz> <7sha5q$rid@dfw-ixnews5.ix.netcom.com>`

```
Given all the discussion on the merits, sins, or whatever of "Next
Sentence," I thought that I should be "fair" and mention the (so far
unmentioned) fact that

"Next Sentence" (*regardless* of in what construct) is being added to the
new (with the next Standard) category called "archaic".

This means that it is NOT "obsolete" (which would mean - theoretically at
least - that it would be removed in the NEXT Standard after this draft one),
but rather that it is a technique that when/if it ever becomes "little used"
(replaced by another construct), will THEN be placed in the OBSOLETE
category and removed in the Standard after that.

What this means (sort-of) is that it is guaranteed to be included in both
the next Standard and the Standard after that (2100???) but might be removed
at some Standard after that.  (FYI, it does NOT mean that the feature will
not/never be "enhanced" - i.e. some future Standard *might* allow it with
END-IF - but I would say that this is unlikely.)
```

###### ↳ ↳ ↳ Re: Next Sentence, etc (was: Collaborative Article on COBOL

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<clQH3.788$Qw4.22447@dfw-read.news.verio.net>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sh6t9$7hj$1@aklobs.kc.net.nz> <7sha5q$rid@dfw-ixnews5.ix.netcom.com> <7sojb9$cku@dfw-ixnews10.ix.netcom.com>`

```
In article <7sojb9$cku@dfw-ixnews10.ix.netcom.com>,
William M. Klein <wmklein at ix dot netcom dot com> wrote:
>Given all the discussion on the merits, sins, or whatever of "Next
>Sentence," I thought that I should be "fair" and mention the (so far
…[9 more quoted lines elided]…
>category and removed in the Standard after that.

Wah and hoo... until then we can have archaic and eat it, too!

DD
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EF732D.913E7BBA@NOSPAMhome.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> :> The code above should be rejected.
…[8 more quoted lines elided]…
> doesn't count) then please do state what it might be.

I work in an IDMS shop with a pre-compiler putting in IF code with NEXT
SENTENCE.  I always terminate their code with a period as the surest way
of making sure the IF logic is finished.  I also use NEXT SENTENCE
within those sentences to make sure I know where the logic will drop
through.  Yes, I am knowledgeable enough to know what code the
pre-compiler will make, but I agree that the next programmer may not be.

This doesn't quite answer your question because I can avoid having
pre-compiler statements within nested IF's, but your reasoning for
disallowing mixing NEXT SENTENCE with END-IF, basically said "NEXT
SENTENCE is bad, since END IF makes NEXT SENTENCE unnecessary, they
should not be allowed together".   Explaining why NEXT SENTENCE is bad
doesn't explain why it should only be disallowed if the IF ends with an
END-IF.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7soi09$nvk$1@aklobs.kc.net.nz>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:
:> 
:> Of course, if you can think of a _good_ reason (laziness
:> doesn't count) then please do state what it might be.

: This doesn't quite answer your question because I can avoid having
: pre-compiler statements within nested IF's, but your reasoning for
: disallowing mixing NEXT SENTENCE with END-IF, basically said "NEXT
: SENTENCE is bad, since END IF makes NEXT SENTENCE unnecessary, they

I think that you would have trouble finding any words from me
that actually got close to your interpretation.

It is CONTINUE that make NEXT SENTENCE unnecessary and this is
quite independant of whether END-IF is used.  If an IF or nested
IF without END-IFs the NEXT SENTENCEs can be replaced by
CONTINUE without change of effect even though the two have
different meaning.

When an END-IF is introduced the NEXT SENTENCE becomes invalid
Cobol according to the standard (though an extension may allow
it to be used with varying actual effects).

: should not be allowed together".   Explaining why NEXT SENTENCE is bad
: doesn't explain why it should only be disallowed if the IF ends with an
: END-IF.

As I have specifically stated that NEXT SENTENCE is not bad when
not used in conjunction with END-IF, I find your statement
puzzling.  I have quite clearly stated in all my messages that
it is 'NEXT SENTENCE in conjunction with END-IF' that is
bad.

It is not me that disallows it, it is the standard that does so.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EFD991.4532D422@NOSPAMhome.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Howard Brazee <brazee@nospamhome.com> wrote:
…[16 more quoted lines elided]…
> different meaning.

I understand this, but the standard apparently didn't make it illegal to
have CONTINUE and NEXT SENTENCE in the same IF structure, or at least
that wasn't part of the discussion.

It very well could be that I missed the point - but I still have no idea
why they made this combination illegal.
 
> When an END-IF is introduced the NEXT SENTENCE becomes invalid
> Cobol according to the standard (though an extension may allow
> it to be used with varying actual effects).

Yes, but why did they decide to make this rule?  What harm would have
been done if they had left it alone?


> : should not be allowed together".   Explaining why NEXT SENTENCE is bad
> : doesn't explain why it should only be disallowed if the IF ends with an
…[6 more quoted lines elided]…
> bad.

I thought you said that it "against standards", in that case.  I asked
why the standards committee decided to make it against the standards.  I
thought you were describing why NEXT SENTENCE was undesirable (bad), and
because of this they could outlaw it in the case an END-IF were used. 
Apparently I missed your real reason given as to why they outlawed it,
which doesn't surprise me, as the reason I inferred is completely
bogus.  I still have no idea why it was outlawed.
 
> It is not me that disallows it, it is the standard that does so.

Understood.  I hope someone could supply me with the answer as to why
the standards committee chose to do so.
```

###### ↳ ↳ ↳ Next Sentence - "Why?" (was: Collaborative Article on COBOL

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sooth$ogb@dfw-ixnews8.ix.netcom.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:37EFD991.4532D422@NOSPAMhome.com...
> Richard Plinston wrote:
   <snip>
>
> It very well could be that I missed the point - but I still have no idea
…[5 more quoted lines elided]…
>
  <various snippage>

> > It is not me that disallows it, it is the standard that does so.
>
> Understood.  I hope someone could supply me with the answer as to why
> the standards committee chose to do so.

OK, let's try and answer this.  (By way of "preface," The Standards
committees "hate" when they get "why did you do this" questions - especially
when they come in years after the "decision" was made.  Therefore, this is
definitely MY understanding and not necessarily "truth" on their reasoning.)

A) The JOD (Journal of Development) which was (while the '85 Standard was
being developed) the "source" of new enhancements to COBOL - *DID* allow a
NEXT SENTENCE to be in an IF statement that was terminated by an END-IF
clause.

B) During development of the '85 Standard, there were some (but definitely
not all) of the developers who agreed with Richard that mixing the "new"
CONTINUE statement with the old NEXT SENTENCE clause would lead to
maintenance problems.

C) If you put in enough "switches," then every NEXT SENTENCE's "logic" CAN
be re-coded with a CONTINUE - but the reverse is NOT true.  Therefore, the
more "general" syntax, CONTINUE, was seen as the "syntax of the future".

D) Therefore, (I think) they decided to remove the JOD facility and stay
with a more "restricted" syntax of allowing CONTINUE with END-IF, to keep
"upward compatibility" of NEXT SENTENCE withOUT END-IF, but to disallow the
"old" NEXT SENTENCE with the new END-IF (if they were both at the same level
of "nesting").

   ***

Because some users and vendors have found the ANSI/ISO restriction
counter-productive and/or counter-intuitive, many (but definitely not all)
vendors have explicitly allowed (as a documented extension), the old NEXT
SENTENCE clause to be used with the new END-IF (and END-SEARCH) feature.

Does this help (at all)?
```

###### ↳ ↳ ↳ Re: Next Sentence - "Why?" (was: Collaborative Article on COBOL

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F0C011.126EE9EC@NOSPAMhome.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com> <7sooth$ogb@dfw-ixnews8.ix.netcom.com>`

```
William M. Klein wrote:

> > Understood.  I hope someone could supply me with the answer as to why
> > the standards committee chose to do so.
…[37 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com

Yes.  It sounds to me that they're saying "NEXT SENTENCE" is bad coding,
but we can't disallow it because it is used so much, so we're
disallowing it when it is used with obviously new code.  Nothing
particular about END-IF which makes NEXT SENTENCE worse, except that
END-IF is obviously newer code, giving them the opportunity to force us
to code "correctly".

Trouble is, there are cases (with some pre-compilers), where we still
need to use NEXT SENTENCE and full stop periods.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 7)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf0940$ec4a4330$0100007f@vaagshaugen>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com> wrote in article
<37EFD991.4532D422@NOSPAMhome.com>...
> It very well could be that I missed the point - but I still have no idea
> why they made this combination illegal.
…[3 more quoted lines elided]…
> > it to be used with varying actual effects).

I agree with you.  Why this fuzz about NEXT SENTENCE?  After all it works
as designed.  It is by definition a GO TO a virtual label after the next
period, the period is the sentence terminator.  When used in an IF
construct it works exactly that way.  I can even see a sensible use for it.
 Imagine a lot of code interspersed in nested IF/ELSE/END-IFs, and a period
at some point after the outermost IF/END-IF.  Then NEXT SENTENCE at any
place within this mess will bring you directly after the period.  That can
be used as error exits.  Of course GO TO and a real label will do the same
thing, but as I understand it is not comme-il-faut to use GO TO nowadays
(or has that changed).

Gunnar.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7srla6$h2f$1@aklobs.kc.net.nz>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com> <01bf0940$ec4a4330$0100007f@vaagshaugen>`

```
Gunnar Opheim <gunnar.opheim@eunet.no> wrote:
:> > When an END-IF is introduced the NEXT SENTENCE becomes invalid
:> > Cobol according to the standard (though an extension may allow
:> > it to be used with varying actual effects).

: I agree with you.  Why this fuzz about NEXT SENTENCE?  A
: After all it works
: as designed.  

It was designed to work without END-IFs.  Yes it always
works exactly as this design would imply.

A
: It is by definition a GO TO a virtual label after the next
: period, the period is the sentence terminator.  When used in an IF
: construct it works exactly that way.  I can even see a sensible use for it.

Exactly, no problem, use it myself. (without END-IF).

:  Imagine a lot of code interspersed in nested IF/ELSE/END-IFs, and a period
: at some point after the outermost IF/END-IF.  Then NEXT SENTENCE at any
: place within this mess will bring you directly after the period.  That can
: be used as error exits.  Of course GO TO and a real label will do the same
: thing, but as I understand it is not comme-il-faut to use GO TO nowadays
: (or has that changed).

It is specified that way in current MF compilers as an extension.
Older compilers or use of OLDNEXTSENTENCE have it as equivalent
to a CONTINUE, ie they go to the end of the outermost IF, the
point at which the full stop _should_ be.

Other compilers may have either of these behaviours as an
extension or they may disallow NEXT SENTENCE and END-IF entirely.

The Fujitsu wording expects a full stop terminating the IF in
that it goes to the sentence following the IF statement.

That is it expects the next sentence to follow on immediately
after the IF statement, which would be true where a full stop
is used to terminate the IF.

The problem is, however, little to do with the IF or the NEXT
SENTENCE but is entirely to do with full stops.  The target
of the NEXT SENTENCE, when abused, is an anonymous label
and thus is a potential bug-nest.

Where OO is a mechanism to improve reliability by encapsulating
and localising control and other effects, this misuse of
NEXT SENTENCE is the opposite in that the effect of the NEXT
SENTENCE depends on code that is outside the statement it is
in (ie the adding or removing of full stops in the rest of
the paragraph.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 9)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ssv6h$h04$1@news.igs.net>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com> <01bf0940$ec4a4330$0100007f@vaagshaugen> <7srla6$h2f$1@aklobs.kc.net.nz>`

```

Richard Plinston wrote in message <7srla6$h2f$1@aklobs.kc.net.nz>...
>Gunnar Opheim <gunnar.opheim@eunet.no> wrote:
>:> > When an END-IF is introduced the NEXT SENTENCE becomes invalid
…[13 more quoted lines elided]…
>: construct it works exactly that way.  I can even see a sensible use for
it.
>
>Exactly, no problem, use it myself. (without END-IF).
>
>:  Imagine a lot of code interspersed in nested IF/ELSE/END-IFs, and a
period
>: at some point after the outermost IF/END-IF.  Then NEXT SENTENCE at any
>: place within this mess will bring you directly after the period.  That
can
>: be used as error exits.  Of course GO TO and a real label will do the
same
>: thing, but as I understand it is not comme-il-faut to use GO TO nowadays
>: (or has that changed).
…[27 more quoted lines elided]…
>
Cobol has always been code that depended on the adding or removal of periods
throughout the paragraphs. What else is new?
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 10)_

- **From:** Randall Bart <Barticus@usa.spam.net>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oIryNwtOS00QwvsjuPJD3HfX=x=8@4ax.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com> <01bf0940$ec4a4330$0100007f@vaagshaugen> <7srla6$h2f$1@aklobs.kc.net.nz> <7ssv6h$h04$1@news.igs.net>`

```
On Wed, 29 Sep 1999 07:54:39 -0400, "donald tees"
<donald@willmack.com> wrote:

>Richard Plinston wrote in message <7srla6$h2f$1@aklobs.kc.net.nz>...
>>Gunnar Opheim <gunnar.opheim@eunet.no> wrote:
…[3 more quoted lines elided]…
>>>> etc.

Now Randall is going to write.

The semantic problem stems from the fact that NEXT SENTENCE is NEXT
SENTENCE.  If NEXT SENTENCE had been NEXT STATEMENT then it would have
meant "next statement" which is what CONTINUE means.  Unfortunately,
NEXT SENTENCE is NEXT SENTENCE and is defined as "next sentence".
This leads to the following counter-intuitive behavior:

IF  COND-A
    NEXT SENTENCE
ELSE
    PERFORM PARA-A  
END-IF
PERFORM PARA-B.

If you implement NEXT SENTENCE as "next statement", PARA-B is
performed unconditionally.  If you implement NEXT SENTENCE as "next
sentence", PARA-B is performed only when COND-A is false.  AFAIK, JOD
was never clear on this, but J4 has clearly ruled that NEXT SENTENCE
means "next sentence", and therefore PARA-B is dependent on COND-A.  

But J4 has admitted that using NEXT SENTENCE this way is illogical and
destined to confuse maintenance programmers.  Furthermore, there are
compilers which have always implemented NEXT SENTENCE as "next
statement".  I believe all the major ones have a compile time option
to make NEXT SENTENCE mean "next sentence", but many are hesitant to
turn on an option to get non-intuitive behavior.

Therefore, J4 has banned the mixing of NEXT SENTENCE with END-IF, and
designated NEXT SENTENCE archaic.  All good Cobol programmers should
use CONTINUE instead of NEXT SENTENCE.  CONTINUE is easier to type,
and where the two constructs differ, NEXT SENTENCE is illogical and
possibly inconsistently implemented.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 11)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F3646B.E01839E9@NOSPAMhome.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com> <01bf0940$ec4a4330$0100007f@vaagshaugen> <7srla6$h2f$1@aklobs.kc.net.nz> <7ssv6h$h04$1@news.igs.net> <oIryNwtOS00QwvsjuPJD3HfX=x=8@4ax.com>`

```
Randall Bart wrote:

> Therefore, J4 has banned the mixing of NEXT SENTENCE with END-IF, and
> designated NEXT SENTENCE archaic.  All good Cobol programmers should
> use CONTINUE instead of NEXT SENTENCE.  CONTINUE is easier to type,
> and where the two constructs differ, NEXT SENTENCE is illogical and
> possibly inconsistently implemented.

If they have a pre-compiler putting in IF logic, good programmers should
code unambiguous code which will be clear whether or not the
pre-compiler inserted code is visible.  This usually means putting in
full stop periods and often means putting in NEXT SENTENCE to get around
the unseen code.

Other than that, I do not see any reason to use NEXT SENTENCE.
```

###### ↳ ↳ ↳ Re: Collaborative Article on COBOL

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F20F92.48BEEE44@NOSPAMhome.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sb9nn$nen$1@aklobs.kc.net.nz> <37EBB00E.C6BE3B28@NOSPAMhome.com> <7sgn1g$3rq$1@aklobs.kc.net.nz> <37EF732D.913E7BBA@NOSPAMhome.com> <7soi09$nvk$1@aklobs.kc.net.nz> <37EFD991.4532D422@NOSPAMhome.com> <01bf0940$ec4a4330$0100007f@vaagshaugen> <7srla6$h2f$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Gunnar Opheim <gunnar.opheim@eunet.no> wrote:
…[9 more quoted lines elided]…
> works exactly as this design would imply.

But so was ELSE (designed to work without END-IFs).  Adding the END-IF
in no way changed the advantage or disadvantage of using ELSE or of
using NEXT SENTENCE.   It simply allowed the compiler to determine
whether the code is legacy  (pre END-IF) or not.

If the standards committee is going to use that enforce their coding
styles, why not work on something which really makes a difference?
```

#### ↳ Re: Collaborative Article on COBOL

- **From:** Ed Milne <emilne@my-deja.com>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sd2kn$vgb$1@nnrp1.deja.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com>`

```
[snip]
> >COMP-3 Fields
> >
> >Problem
> >
> >The version of VS/COBOL used before August 1996 used the full
physical
> >size of a COMP-3 field regardless of the picture.
> >If a picture only defined an even number of digits, an extra digit
was
> >automatically used. For example, the compiler treated
> >"COMP-3 PIC S9(4)" as if it were "COMP-3 PIC S9(5)". However, COBOL
II
> >truncates any values moved to such fields to
> >the number of digits actually defined.
> >
> >For example, suppose a program contains a field defined as "COMP-3
PIC
> >S9(4)" and moves 12345 to that field. Under the old VS/COBOL compiler
> >the result is 12345. Under the new VS/COBOL compiler and COBOL II,
the
> >result is 2345.
> >
> >Programs recompiled since August 1996 should have been changed to
> >correct this problem. However, any reengineering project may
recompile
> >programs that have not been changed in many years.
> >
> >Solution
> >
> >Change the pictures for all COMP-3 fields so they define an odd
number
> >of digits unless they should only contain an even number of digits.
Most
> >fields should have an odd number of digits to take full advantage of
the
> >physical size of the space used.
> I have always taught that packed fields shoud be defined with an odd
number of
> digits because that's how the hardware stores packed data. Again, this
problem
> has to do with careless programming, not any change in the language or
> compiler.

Yes, it is better programming practice to use an odd number of digits
with COMP-3 fields.  But the point is that an upgrade to a new version
of a COBOL compiler from the same manufacturer destabilized a previously
working program.  Because of this possibility, you have to treat an
upgrade as a mass change to all the programs in a system with all the
appropriate cost and timing implications.

>
> >However, some fields, such as dates,
…[3 more quoted lines elided]…
> Not necessarily. There are lots of ways to store dates. In Julian
formats, for
> example (yyddd or yyyyddd or dddyy or dddyyyy) there are an odd number
of
> digits. You can store year, month, and day in separate binary, packed,
or
> display fields. I have become convinced that the right way to store
dates is as
> eight bytes of display data in yyyymmdd order.
>
…[5 more quoted lines elided]…
> >After converting a program to COBOL II, it is natural to use the
COBOL
> >II structures for ending statements rather than
> >periods for new code. This mix of old and new code can cause problems
…[20 more quoted lines elided]…
> >Make a mass change of all occurrences of "NEXT SENTENCE" to
"CONTINUE".
> >The new CONTINUE clause does nothing. It just continues with the next
> >statement, which is the real intent of the "NEXT SENTENCE" clause.
…[3 more quoted lines elided]…
> But you don't have to do this as part of the conversion. The old code
would
> have worked fine. You chose to use the new features because you get
some
> benefit (easier to code, read, maintain). But you have to pay
attention to
> details.

Your original post stated that one of the justifications upgrades was
the ability to use new features.  However, you have to weigh that
against the cost of destabilizing the programs.

>
> Yes, I guess overall I would say the conversion was good for you
because it
> caught careless practices and therefore made your code more robust.
This is
> truly a benefit, even if one unlooked for.

The people that you are addressing and this newsgroup and IEEE are all
techies who recognize the personal benefits of learning the latest and
greatest software.  We benefit regardless of what happens to the systems
we convert.  So your proposed article is preaching to the converted.

However, the user department who paid for the upgrade still feel that
they got no benefit from the project.  BTW, the project was to modernize
 a legacy payroll system that was bad code to start and then was hacked
over for 30 years.  The programmers who maintain the system love the
version.  The users don't see any difference.  That is the real problem
with upgrades.
```

##### ↳ ↳ Re: Collaborative Article on COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sd61d$md3@dfw-ixnews12.ix.netcom.com>`
- **References:** `<19990922120110.00284.00000917@ng-fs1.aol.com> <7sd2kn$vgb$1@nnrp1.deja.com>`

```

Ed Milne <emilne@my-deja.com> wrote in message
news:7sd2kn$vgb$1@nnrp1.deja.com...
> [snip]
  <much nore snippage>
> >
> > But you don't have to do this as part of the conversion. The old code
…[10 more quoted lines elided]…
>

Probably the reason why (at least in the case of IBM - OS/VS COBOL to VS
COBOL II *or* the more resent COBOL for this-and-that) made it perfectly
clear that you did NOT need to "upgrade" or change - much less "destabilize"
existing code.  The old code continues to work as it did then and can even
be called from new programs.  The only time that things CHANGE are when you
actually *do* write new code or maintain the old code (or - because it is
cost-justified based on other benefits) decide to re-compile existing code
with the new compiler.

As a reminder both OS/VS COBOL and VS COBOL II *object* code is FULLY
support today, after March 2001 (the drop date for VS COBOL II), and for the
foreseeable future - if you are using the LE run-time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
