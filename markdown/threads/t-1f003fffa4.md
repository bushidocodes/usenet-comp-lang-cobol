[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# invalid" source code (END-IF, Next Sentence, and mi...

_16 messages · 4 participants · 2001-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-06T17:25:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1E598A.D34434FC@Azonic.co.nz>`

```
-> Just for the "record" the following source code will compile
"cleanly" and
> is semi-valid with IBM mainframe compilers ...
>
…[3 more quoted lines elided]…
> messages).

You appear to be constructing an entirely semantic argument about what
the term "valid Cobol" means.

In my view what you describe is not 'valid COBOL' but may be valid
source code for a language that is very similar to Cobol called "IBM MVS
COBOL/2" or some such, though whether it actually is valid may depend on
compiler options or other settings.

That is, just because your compiler swallows it and produces am
executable in a deterministic way does not make this 'valid COBOL', it
only makes it 'valid compiler input'.
```

#### ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-06T11:02:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9flk74$54a$1@slb2.atl.mindspring.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz>`

```
Valid COBOL is the COBOL that the compiler vendor SAYS is valid for that
compiler.  ANSI/J4 has actually done an "interpretation request" where they
CONFIRMED this definition.

The question was related to a compiler that "accepted"

    Label Records IS
      or
    Label Record ARE

which is "illegal" according to the ANSI Standard and was *not* documented
as an extension by that vendor in their Language Reference Manual.

J4 (who - at least in the US - I consider the "authority" on such matters)
said,

A) This is a "conforming implementation"
B) As long as they did not document this as an extension, they did NOT need
to flag it as an extension - NOR were they required to produce *any*
compiler error (warning, informational or error severity).

I did not (and do not) "LIKE" that decision - but the bottom line is
conforming source code for a conforming compiler is WHATEVER the compiler
vendor says it is.

Let me know if you need/want web access to the J4 interpretation in which
this was "confirmed".
```

##### ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-07T07:42:16+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1F2247.6FDB3D26@Azonic.co.nz>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Valid COBOL is the COBOL that the compiler vendor SAYS is valid for that
> compiler.  

COBOL is not a vendor defined language (not even IBM).

What you are claiming is that what is 'valid COBOL' will depend on which
compiler you use, or indeed what options and settings.

> ANSI/J4 has actually done an "interpretation request" where they
> CONFIRMED this definition.
> [...]
> A) This is a "conforming implementation"

You are confusing 'conforming implementation' where a valid Cobol
program (that is one following all the standards) is processed correctly
and then extrapolating this to expect that whatever the compiler will
accept is 'valid Cobol'.

Just because some source code is valid for the compiler of a
cobol-derived language that some vendor supplies does not make it 'valid
COBOL'. And this is the case even if the compiler will pass all the
tests and has been declared conforming.

'Valid COBOL' is what passes a comparison with the COBOL standard.

'Valid IBM MVS COBOL/2' is what the compiler accepts.

I would expect the IBM compiler to accept all 'valid COBOL' programs
(perhaps with some documented provisos).  But this does not mean the
reverse that everything the compiler accepts is thus 'valid COBOL'.

The same situation exists in other languages.  A C/C++ compiler will
process correctly an ANSI C program or a C++ program.  By your
definition all C++ would thus be 'valid C'.
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-06T17:51:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fmc54$1j2$1@slb3.atl.mindspring.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B1F2247.6FDB3D26@Azonic.co.nz...
> William M. Klein wrote:
> >
  <snip>
>
> Just because some source code is valid for the compiler of a
…[4 more quoted lines elided]…
> 'Valid COBOL' is what passes a comparison with the COBOL standard.

Richard - you are simply WRONG.  This is not what the ANSI (or ISO) COBOL
Standard says - or what any COBOL standards commitee has EVER said.

What you are describing is what is "correctly" refered to as "conforming
source code".  By definition (of the ANSI/ISO Standards) *any* implementor
is allowed to add as many extensions as they want and still call the source
code that uses such extension "valid COBOL".  That is part of the definition
of what the COBOL programming language IS.

It is true that any "conforming compiler" *must* provide an OPTION to flag
any (all) documented extensions.  (IBM, MERANT, Fujitsu, etc all do this).
There is *no* requirement in the ANSI/ISO COBOL Standard (past or present)
that vendors *must* "catch" all source code that violates the rules of the
Standard or their Language Reference. (This is the fact that was recently
"confirmed" by J4).

The next Standard *does* include a NEW requirement that vendors must provide
an "option" to flag syntax that violates the "syntactically detectable"
violations of their own COBOL (including Standard and Extensions) - HOWEVER,
even with the new rules, it will still be the vendor in many (most?) cases
that determines what is "syntactically detectable".

   ***

Bottom-Line:
  If you want to talk about COBOL source code that is "limited" to that
defined in the current ANSI/ISO Standards, then refer to it as "ANSI/ISO
conforming source code".  If you want to refer to whether specific COBOL
source code is or is not "valid" - then you MUST refer (only) to that source
code that the VENDOR says is valid.
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-07T14:06:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1F7C3D.BA724241@Azonic.co.nz>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Richard - you are simply WRONG.  This is not what the ANSI (or ISO) COBOL
> Standard says - or what any COBOL standards commitee has EVER said.

Please quote the paragraph in the ANSI COBOL '84 Standard that defines
the word 'valid'.


> If you want to refer to whether specific COBOL
> source code is or is not "valid" - then you MUST refer (only) to that source
> code that the VENDOR says is valid.

What nonsense.  I get to choose the Vendor and I choose one that says
the code that I was talking about is 'invalid code'.

Therefore, even by your 'definition' it is invalid.
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-07T02:53:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1EED42.8B10459D@home.com>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net> <3B1F7C3D.BA724241@Azonic.co.nz>`

```


Richard Plinston wrote:

> William M. Klein wrote:
> >
…[13 more quoted lines elided]…
> Therefore, even by your 'definition' it is invalid.

Pardon the intrusion Richard, and I really don't give a damn what one can
currently do and not do. But boy, although currently down in Kiwiland, you sure
hang in there like a British bulldog <G>

May I make a very serious suggestion - both you and Rick Smith, (both Brits <G>),
have incisive minds as to what should and should not be. Both of you should
consider offering your time to J4 to help get 'our language' up and running and
picture perfect. Serious - it would be time well spent productively, rather than
discussing where old versions of COBOL are at. I betcha, on reflection, Bill would
warmly welcome you both aboard - even if the three of you had ring-a-ding battles.

Please both give it serious thought. And Stephen, pester these two with private
e-mail to get involved, not necessarily 'physically' but by
e-mail/tele-conferencing  contributions.

Jimmy
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-07T13:59:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9foitu$oe4$1@nntp9.atl.mindspring.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net> <3B1F7C3D.BA724241@Azonic.co.nz>`

```
Richard, (and I doubt that any others are actually interested in this - but
I am posting the references just in case)

  The documents that you are going to want to read (look at) concerning what
is and is not "COBOL" are the J4 documents:
   01-0022 (E-308.2) - Undetected User Errors (IQ-2204)
   01-0017 (E-308.1) - Undetected user errors
   01-0018 - Documents related to E-308.1
   01-0062 - Report of the X3J4 ad hoc group on interpretations

All of those can be found from:
   http://www.ncits.org/tc_home/j4htm/m229/j4m229.htm
(Use the document number to find each document)

I do NOT know (and have not looked to see) if they do or do not actually use
the word "valid" (or "invalid") but they certainly DO give the J4 answer to
any claim (that I can understand) that "valid COBOL" is something that exits
in the abstract and is not determined by each vendor.

As I say, I do believe that what you are talking about is "ANSI/ISO
conforming COBOL source code" - and that is well defined in the '85 Standard
(and those before and after).  See Page I-9 of the '85 Standard that says
(in part),

"1.6 DEFINITION OF A CONFORMING SOURCE PROGRAM

A conforming source program is one which does not violate the explicitly
stated provisions and specifications of Standard COBOL. In order for a
source program to conform to Standard COBOL, it must not include any
language elements not specified in this standard. The execution of a
program, the source text of which conforms to Standard COBOL, is predictable
only to the extent defined in this standard. The results of violating the
formats or rules of Standard COBOL
are undefined unless otherwise specified in this standard.

In order for a source program to conform to a specified subset of Standard
COBOL, it must include only language elements of that subset.

There are, in Standard COBOL, situations in which the results of executing a
statement are undefined or unpredictable (see page XVII-96, Undefined
Language Element List). A COBOL source program which allows this to happen
may nevertheless be a conforming program, although the resultant execution
is not defined by Standard COBOL."

   ***

Compare this with the earlier statement (on page I-8) which states,

"1.5.2.5.2 Extension Language Elements

An implementation that includes language elements in addition to the subset
and levels of optional modules for which support is claimed meets the
requirements of Standard COBOL. This is true even though it may imply the
extension of the list of reserved words by the implementor, and thereby may
prevent proper translation of some programs that meet the requirements of
Standard COBOL.

Documentation associated with an implementation must identify any standard
extensions (language elements not defined in the supported subset or
supported levels of optional modules but defined elsewhere in Standard
COBOL) or nonstandard extensions (language elements or functions not defined
in Standard COBOL) that are included in the implementation.

A conforming implementation of Standard COBOL must provide a warning
mechanism, which optionally may be invoked by the user at compile time to
indicate, if appropriate, that a program contains nonstandard extensions
that are included in the implementation."
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-06-07T09:10:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fnuis$2p5k$1@news.hitter.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net>`

```

William M. Klein wrote in message <9fmc54$1j2$1@slb3.atl.mindspring.net>...
[...]
>Bottom-Line:
>  If you want to talk about COBOL source code that is "limited" to that
>defined in the current ANSI/ISO Standards, then refer to it as "ANSI/ISO
>conforming source code".  If you want to refer to whether specific COBOL
>source code is or is not "valid" - then you MUST refer (only) to that
source
>code that the VENDOR says is valid.

Bill, I agree, but I want to take the explanation one step further.

"What COBOL is" is stated in the acknowledgment.

"COBOL is an industry language and is not the property of any
company or group of companies, or of any organization or
group of organizations. ..."

If the complete acknowledgment has been placed at the
beginning of a language reference, any specification that
follows is COBOL. This is true even if it looks like C, APL,
Ada, or classic COBOL. Furthermore, there is no requirement
that any COBOL compiler conform to any COBOL standard.
It also means that multiple, conflicting, COBOL standards
could exist at any time.

Hopefully, this makes it more clear that the compiler
manufacturer determines "valid COBOL" and a standard
determines "conforming COBOL".

Individuals determine whether any COBOL is a "true" or
"real" COBOL. :-)
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-08T15:42:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B20E468.AB60E68C@Azonic.co.nz>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net>`

```
William M. Klein wrote:

> I do NOT know (and have not looked to see) if they do or do not actually use
> the word "valid" (or "invalid") 

Well exactly.  You have been attempting to pummel me with leagalese for
using an informal term for which there is no actual formal definition.

> but they certainly DO give the J4 answer to
> any claim (that I can understand) that "valid COBOL" is something that exits
> in the abstract and is not determined by each vendor.

So you want to insist that I always use a phrase such as:

"does not comply with the definition of a conforming source program as
it violates the explicitly stated provisions and specifications of
Standard COBOL (I can't be bothered finishing this)".

instead of saying "it's wrong" or similar.

Why don't you make a mental footnote that whenever I use the informal
phrase "not valid Cobol" that it means whatever you want to use as a
several page document and that it refers to 'Cobol' as defined by the
standard without vendor changes.


> > If you want to refer to whether specific COBOL
> > source code is or is not "valid" - then you MUST refer (only) to that source
> > code that the VENDOR says is valid.

And if I want to refer to a specific vendor's compiler source I will use
that particular name (rather than a bare 'Cobol').

eg: your examples were 'valid IBM MVS Cobol/2'.

It would be a nonsense if each different vendors variations had to be
referred to with the phrase 'valid Cobol', as you seem to require,
without any need to specify the vendor, version or options.  And then
have to be entirely specific about Cobol in the standard.

I mean, what is your problem ?

There was an example piece of code that was IF .. NEXT SENTENCE ...
END-IF which I said in a completely informal way was 'invalid Cobol'* in
that there is a rule in the standard that prohibits this, and you start
off of a complete rant of legalese, and completely irrelevant examples,
only to wind up not being able to support a formal definition of
'valid'.


>   If you want to talk about COBOL source code that is "limited" to that
> defined in the current ANSI/ISO Standards, then refer to it as "ANSI/ISO
> conforming source code".  If you want to refer to whether specific COBOL
> source code is or is not "valid" - then you MUST refer (only) to that source
> code that the VENDOR says is valid.

MUST I ?  Or what, get thrown in jail ?  Have my compiler forcably
removed.

I will use whatever terminology that _I_ think fits the situation best. 
If you don't like this then don't read my posts.


Footnote: * convert this phrase to several pages of legalese where
required.
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-08T15:21:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9frc3q$f2o$1@slb0.atl.mindspring.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net> <3B20E468.AB60E68C@Azonic.co.nz>`

```
Richard,
  You of course (especially in a non-moderated newsgroup) may call PL/I
"valid" COBOL and the NIST conformance tests "invalid COBOL" - that just
doesn't make either of these correct statements.  Furthermore, in order to
insure that your implications (confusing "valid" which is not well defined
and "conforming" which is) do NOT confuse others, I will continue to correct
you when you use the WRONG term.

If there were no term for what you were talking about, then I would say -
fine go ahead and define your own terms and see if others agree (or if your
posts are clear).  HOWEVER, the fact remains that the people who DO define
the ANSI/ISO COBOL Standards have defined "conforming source code" to be
what you have (incorrectly termed) "valid COBOL".  They have also explicitly
stated that every vendor "defines" their own COBOL implementation - and that
such an implementation (with any number of extensions) remains a conforming
implementation (and thus any SANE person would call their "accepted" source
code "valid").

When you use the correct terms, I won't comment; when you use incorrect or
misleading ones, I will continue to correct the misconceptions that you try
to spread - whether you believe them or not.
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-10T09:38:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B233220.82DCBE64@Azonic.co.nz>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net> <3B20E468.AB60E68C@Azonic.co.nz>`

```
> William M. Klein wrote:
> 
>   You of course (especially in a non-moderated newsgroup) may call PL/I
> "valid" COBOL and the NIST conformance tests "invalid COBOL" - that just
> doesn't make either of these correct statements.  

Excuse me, but I have been quite clear on what it was that _I_ wanted to
call "invalid Cobol", I have never even implied that I wanted to call
PL/I as being 'valid Cobol' or anything that passed the tests as
'invalid Cobol'.

Quite the contrary in fact.  Rick Smitch wanted to be able to call C,
APL, or Ada as 'valid Cobol', go pontify at him.

Again you are simply talking crap and have obviously not read the actual
words that I used.

> Furthermore, in order to insure that your implications 

> (confusing "valid" which is not well defined

Or, indeed not defined at all as you have conspicuously failed to find
one.  And if it is so precious to you that the word "valid" is not used
then what were you doing with:

>> and is semi-valid with IBM mainframe compilers

If "valid" is 'not well defined' then does 'semi-valid' mean: 'on
alternate days' ?

> confusing "valid" and "conforming"  

I was not confused _at_all_, you are completely wrong on that point.  If
I had wanted to use the word 'conforming' I would have done so.  In fact
the word conforming would have not expressed what I wanted to convey.

> do NOT confuse others

If you were confused then it is probably just because it wasn't buried
in several pages of crap pontification and legalese.  So far I have not
seen any evidence that anyone else was 'confused' except that they were
unaware that the standard had a rule that excluded the use of NEXT
SENTENCE in an IF ... END-IF.

I blame this lack of knowledge of the actual standard on the exact thing
that you claim in that 'it is valid Cobol if _my_ compiler accepts it'.

If you actually wanted to reduce confusion you would be telling what the
standard says about Cobol instead of parading how wonderfully obscrure
*YOUR* compiler can be in accepting what I would call 'junk Cobol'.

In fact, some were confused enough by your examples to try writing
paragraphs without full-stops in their compilers.  If anyone wrote
confusing messages it was you.

> I will continue to correct you when you use the WRONG term.

And I will continue to tell you to stuff off trying to control me and to
censor my messages.

As you cannot justify your claims about what 'valid' should, or should
not be, let alone what your 'semi-valid' should be then I reject any
claims that it was WRONG.


> If there were no term for what you were talking about, then I would say -
> fine go ahead and define your own terms and see if others agree (or if your
> posts are clear).  HOWEVER, the fact remains that the people who DO define
> the ANSI/ISO COBOL Standards have defined "conforming source code" to be
> what you have (incorrectly termed) "valid COBOL".  

Then they may use their term as much as they like.  But I reject the
suggestion that I am only allowed to use 'approved terms'.

> They have also explicitly
> stated that every vendor "defines" their own COBOL implementation - and that
> such an implementation (with any number of extensions) remains a conforming
> implementation (and thus any SANE person 

And now you call me INSANE.

Do you always try to convince people with insults ?  Do you think that
it is easier to coerce them this way ?

> would call their "accepted" source code "valid").

Yet you cannot find how 'valid' should be defined.  It is just your
_OPINION_ that 'valid' should be used in this specific way.

But however, in spite of your complete rant on the subject, THERE WAS
NEVER ANY MENTION OF THE SPECIFIC IMPLEMENTATTION.

You _may_ be correct if the source in question has been specific about
which compiler was used and which options were in force.  However there
was no such thing.

Your argument that "it was 'valid' because the compiler would accept it"
fails miserably because the compiler was not specified.

You also make a serious error of logic:

            All cows are brown.
            This is brown.
            Therefore it is a cow.

            This is a Cobol compiler.
            It accept this line of source code.
            Therefore this line is valid Cobol.

Many years ago I could write into my source code:

          ENTER PLAN
              LDN    3,20
              STO    3,LACKSALOT
          ENTER COBOL

The compiler would accept this program as being a
*valid*Cobol*source*file*.  But no matter how much you patronise,
insult, lecture and pontificate, you will never get me to accept that:

             LDN   3,20

is a VALID COBOL STATEMENT.  Even though it is a valid source file for
this compiler and the compiler is/was a valid compiler of Cobol.

Now it certainly was a vaild statement of 'ICL XE13 COBOL'.  Your
examples of code were at least 'semi-valid' [sic] statements of the 'IBM
MVS COBOL/2' language.

If you insist that these statements are 'valid Cobol' then I just think
that you have extrapolated the standard in a completely invalid way, and
I relly don't f****g care about that.

In fact you have extrapolated "vaild Cobol source code" (as a complete
file of source for a program) into thinking it means that each and every
line and word therein is a 'valid Cobol statement'.


> When you use the correct terms, I won't comment; when you use incorrect or
> misleading ones, 

Axtually, in the particular case where I said:

>>> You have coded a NEXT SENTENCE in an IF ... END-IF.  
>>> This is invalid Cobol code and a bug looking for a place to happen.

There was no indication of the vendor or the compiler or the options
used.  The compiler _may_ have rejected that statement as being
'invalid'.  It is only your _assumption_ that it was just like your own
compiler.  Thus it is only your _opinion_, based on your assumption that
I used the wrong term.

> I will continue to correct the misconceptions that you try
> to spread - whether you believe them or not.

All this crap over an informal use of the word 'invalid'.

And I will use cobol, Cobol, or even coBoL instead of fully capitalised,
just because it annoys you.

And I will continue to use whatever terms that I want to just so that
you have to waste hours trying to 'correct' me and force me to use
'approved terms'.

It's no wonder the bloody standard isn't out yet. 

They say that if you see the way that sausages and laws are made then
you will cease to have anything to do with them.  Is this the way that
'standards' are made, or imposed ?
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-09T18:57:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fud5f$gdr$1@nntp9.atl.mindspring.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9fmc54$1j2$1@slb3.atl.mindspring.net> <3B20E468.AB60E68C@Azonic.co.nz> <3B233220.82DCBE64@Azonic.co.nz>`

```
Richard,
  I just love it.  Now COBOL that includes documented extensions is "junk
COBOL" (see below).

Conforming source code is EXACTLY what you are talking about.  It is
"conforming" source code that may not include a NEXT SENTENCE in an IF
terminated by an END-IF.  There is *no* other (defined) term for this
distinction.

Extensions to the COBOL Standard (defined by ANSI/ISO) are EXPLICITLY
allowed in a "conforming" implementation.  That you don't like SOME
conforming implementations or want programmers to limit their applications
to that subset (without acknowledging that even THAT subset is not
"portable" as far as either compile-time or run-time impact) seems strange -
if not counter-productive.

I have (repeatedly) pointed out that all conforming compilers MUST include a
compiler option to flag "non-conforming source code".  I know of almost no
programmers who ever use this option - as the "restricted" conforming source
code has such limited "real world use".  However, it does exist (in
conforming compilers) and is something that you might point people to - if
you want to have them check for conformance of their source code to the
defined ANSI/ISO standard.

If you want to "encourage" the use of "portable" source code, you might do a
little research into extensions that have "common implementations" and
especially those included in the draft of the next Standard.  Such "items"
include:
  - GoBack statement
  - USAGE POINTER (and/or procedure-pointer)
  - SET ADDRESS OF
  - LOCAL-STORAGE SECTION

By your definition, this is "junk COBOL" until some time at the end of next
year - when it will suddenly become "valid COBOL" (in your definition).
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-06-10T11:15:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g0307$te7$1@news.hitter.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz>`

```

Richard Plinston wrote in message <3B1F2247.6FDB3D26@Azonic.co.nz>...
>William M. Klein wrote:
>>
>> Valid COBOL is the COBOL that the compiler vendor SAYS is valid for that
>> compiler.
[...]
>'Valid COBOL' is what passes a comparison with the COBOL standard.

Which COBOL standard?

The BLOCK CONTAINS clause is defined in the ANSI 85
COBOL standard; but is excluded from the X/OPEN COBOL
standard. Is BLOCK CONTAINS valid COBOL or not?

If we can accept that each COBOL standard and each COBOL
language reference represents a distinct definition of COBOL,
then "valid COBOL" is that which conforms to a specific
definition of COBOL. The idea is that one cannot determine
whether COBOL source is valid without knowing which
definition applies.

It might be better to avoid the term "valid COBOL". ;-)
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-11T10:40:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2491F3.B8C0EAAE@Azonic.co.nz>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B1F2247.6FDB3D26@Azonic.co.nz> <9g0307$te7$1@news.hitter.net>`

```
Rick Smith wrote:
 
> "What COBOL is" is stated in the acknowledgment.
> 
…[14 more quoted lines elided]…
> determines "conforming COBOL".
 
Actually you completely missed the whole issue on 'dialects'.  You are
quite correct that you could have a product that claims to be Cobol, but
if it looked more like C then it would be a dialect, possibly called
'Ricks Cobol'.  In which case a C program, even thogh it can be
processed by the 'Ricks Cobol compiler', does not turn into being
'Cobol' it only turns into being of the dialect 'Ricks Cobol'.

> Individuals determine whether any COBOL is a "true" or
> "real" COBOL. :-)

Given that 'true', 'real' and 'valid' are all not defined anywhere then
if you can claim to be able to determine what is 'true Cobol', then I
can claim to be able to determine what is 'valid Cobol' (or actually
'invalid') in exactly the same way.

Bill is quite right that _IF_ I had used 'conforming' is a way that
_disagreed_ with the standard then he _may_ be able to argue that I was
wrong.

> then "valid COBOL" is that which conforms to a specific
> definition of COBOL. 

Is this a formal definition that you found in the standard, or did you
just make this up ?

You also need to be more careful, you used the word 'conform'.  I have
been repeatedly berated that 'conform' is to be used when referring to
the ANSI/ISO Standard.  Now it seem that you will use the term when
referring to dialects and versions.

Specifically Bill told me that I MUST use the term 'conforming Cobol'
instead of 'valid Cobol' when talking about ANSI/ISO Standard, yet you
seem to be free to use that term when referring to versions and dialects
that may be non-standard.

If there is specific version or dialect of Cobol then what would be
useful if if the actual dialect is specified.  Bill's full-stop-less
paragraphs may be 'valid IBM MVS Cobol/2' (or even semi-valid whatever
_that_ means).

> The idea is that one cannot determine
> whether COBOL source is valid without knowing which
> definition applies.

Exactly what I have been saying.  But, of course, when the version is
not specified then are you saying that it cannot be discussed ?

In any case what gets right up my nose is pompous prats attempting to
make every informal discussion into a legal argument with several page
quotes from the standard and lecturing me on what I can and cannot say.
```

##### ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-11T20:29:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B251C04.E808ACCD@Azonic.co.nz>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net>`

```
William M. Klein wrote:

> By your definition, this is "junk COBOL" 

I would be interested as to how you contrived to make my words into a
'definition'.

>   I just love it.  Now COBOL that includes documented extensions is "junk
> COBOL" (see below).

You are confused yet again.  The cobol in question is not 'junk cobol'
because it contains extensions, it is junk because it is difficult to
extract what it actually means and even harder to determine what it was
intended to mean.

It is easy to contrive a nested IF structure where the inner IF has a
NEXT SENTENCE and the outer IF has an END-IF, and this would be valid
standard cobol.  This alone would make it 'junk cobol' (without _any_
extensions) if the programmer relied on the NEXT SENTENCE to go to some
point beyond the end of the scope of the IFs.  This is because the NEXT
SENTENCE acts as a GO TO to the next full-stop wherever it may be
(except where an extension such as MF's OLDNEXTSENTENCE directive
changes its behaviour BTW).  The full-stop then acts as an _anonymous_
label.  This in itself is a very productive bug-nest.

The extension of not requiring a full-stop at the end of a paragraph
then potentially makes the target of the NEXT SENTENCE not only
anonymous, but _invisible_ (if I understand the compiler behaviour
correctly). This means that you need a language lawyer for that dialect
to understand what is _going_ to happen and a mind-reader to know what
the programmer _intended_ to happen.

Perhaps the compiler adds an implicit full-stop and this acts as a
target for the NEXT SENTENCE, perhaps the programmer thought that it
would take an actual full-stop on an executable statement to be the
target.  How would you ever know ?

Would _you_ even care ? As long as they use the correct terminology and
quote the relevant paragraphs when discussing it you may think that the
code is ok to use.

The only safe thing to do with such code is to dispose of it (junk it)
and rewrite from the specifications, otherwise it will just be a
bug-factory for each new coder to fall into the traps.

> Conforming source code is EXACTLY what you are talking about.  It is
> "conforming" source code that may not include a NEXT SENTENCE in an IF
> terminated by an END-IF.  There is *no* other (defined) term for this
> distinction.

Again you are confused.  There is a contrived way in which the standard
allows a NEXT SENTENCE to be 'included' in an IF ... END-IF, that is by
having it in a nested IF included in the IF ... END-IF.

You have been let down by sloppy use of words.  

You <<MUST>> say that 'If the END-IF is specified in an IF statement
then the NEXT SENTENCE phrase must not be specified'.  'Include' is not
part of the standard, There is *no* other (defined) way of saying this.

And I may keep repeating this at you in a thoughly boorish way until you
repent and admit that you were WRONG, WRONG, WRONG.

 

> Extensions to the COBOL Standard (defined by ANSI/ISO) are EXPLICITLY
> allowed in a "conforming" implementation.  That you don't like SOME
> conforming implementations or want programmers to limit their applications
> to that subset 

It has nothing to do wanting programmers to not use extensions, so you
rant is entirely misdirected (as usual).  It is about writing better
programs that are more easily maintained.  Though this doesn't seem to
be a concern of yours, you prefer people using the 'correct' terms.


> (without acknowledging that even THAT subset is not
> "portable" as far as either compile-time or run-time impact) seems strange -
> if not counter-productive.

It is nothing to do with portable.  You drew entirely the wrong
conclusions about what made 'junk' code and then extrapolated this in an
entirely haphazard and incompetent way.

 
> I have (repeatedly) pointed out 

ad nauseum ..

> that all conforming compilers MUST include a
> compiler option to flag "non-conforming source code".  I know of almost no
…[4 more quoted lines elided]…
> defined ANSI/ISO standard.

Unfortuately, if the manual doesn't distinquish between ANSI/ISO
standard and actual implementation the programmers won't actually be
able to understand why they are getting these messages.

> If you want to "encourage" the use of "portable" source code, you might do a
> little research into extensions that have "common implementations" and
…[5 more quoted lines elided]…
>   - LOCAL-STORAGE SECTION

What's your point ?  I know which are actual extensions and which will
be in the next standard.  Except for GOBACK (which always seemed to be
an IBMish thing and little point where EXIT PROGRAM and STOP RUN did the
same), I have used them for some years, but always knew they were
extensions.


> By your definition, this is "junk COBOL" until some time at the end of next
> year - when it will suddenly become "valid COBOL" (in your definition).
 
No. Wrong.  I never made any definition of 'junk', and my use of 'junk
Cobol' is not about extensions at all.

Your 'conclusion' is completely wrong and shows an incompetence in being
able to usefully understand what is written, to be able to extrapolate,
or to draw accurate conclusions.
```

###### ↳ ↳ ↳ Re: invalid" source code (END-IF, Next Sentence, and mi...

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-11T14:20:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g35mq$ld7$1@slb6.atl.mindspring.net>`
- **References:** `<3B1E598A.D34434FC@Azonic.co.nz> <9flk74$54a$1@slb2.atl.mindspring.net> <3B251C04.E808ACCD@Azonic.co.nz>`

```
Richard changes his definitions and terms yet again.  In the note (to which
I am replying), he states (some sections snipped - see the full note for
"context")


>
> > By your definition, this is "junk COBOL"
…[4 more quoted lines elided]…
> >   I just love it.  Now COBOL that includes documented extensions is
"junk
> > COBOL" (see below).
>
…[4 more quoted lines elided]…
>

 <snip>
>
> > (without acknowledging that even THAT subset is not
> > "portable" as far as either compile-time or run-time impact) seems
strange -
> > if not counter-productive.
>
…[4 more quoted lines elided]…
>

Now lets look at what Richard actually said in the note to which I was
replying,

"If you actually wanted to reduce confusion you would be telling what the
standard says about Cobol instead of parading how wonderfully obscrure
*YOUR* compiler can be in accepting what I would call 'junk Cobol'."

The "highlighted" "*YOUR* compiler" certainly seems to be stating that "junk
COBOL <sic>" is related to what a specific compiler allows (or doesn't
allow).  This *must* have to do with extensions and not with what is in the
ANSI/ISO Standard (which - I think we ALL agree *can* be obscure - but need
not be).

Terms that "make sense" to me and that I think that most CLC people would
agree to are:
   (Please reply to these terms in SEPARATE thread)

 - Conforming COBOL - source code conforms to ANSI/ISO Standard (current
ANSI/ISO Standard).
 - 'nn Conforming COBOL - source code that conforms to the "19nn" or "20nn"
ANSI/ISO Standard
 - Conforming XYZ COBOL - source code conforms to the XYZ Standard (e.g.
X/Open, MIA, SAA, etc)
 - Clear (and usually maintainable) COBOL - source code that can
(subjectively) be picked up and understood/maintained by a programmer OTHER
than the one who originally wrote it.  (Sorry, Tony - this doesn't include
your code that is "clear" to you, but not to many/most others)
 - Valid XYZ COBOL - COBOL which gets a "clean compile" with the XYZ
compiler.  The XYZ compiler vendor describes the rules for this source code
and whether informational or warning message may or may not be issued for
such code.  (The phrase "valid COBOL" may be used without mentioning XYZ -
if the context makes it clear which compiler - and possible release and
possibly operating system are being used.  The same is true for the "XYZ" in
"Conforming XYZ COBOL").
 - Portable COBOL - COBOL that compiles "cleanly" and produces the same
run-time results in multiple environments.  In most cases, one actually
needs to (at least initially) talk about which environments are in question,
as almost no "real world" COBOL is fully portable to ALL known ANSI/ISO
conforming compilers/operating systems.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
