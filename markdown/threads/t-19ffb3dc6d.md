[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New Wording for EXIT rules.

_7 messages · 5 participants · 2001-07_

---

### Re: New Wording for EXIT rules.

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-05T15:47:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i2jrm$uq7$1@slb4.atl.mindspring.net>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com>`

```
This ties in with the original German comment on the "implicit" CONTINUEs.

As I understood the German comment (and I am NOT certain that I do), they
were concerned about all the "implicit" statements and which one came/comes
first.

In my opinion, this is a "misunderstanding" of the implicit CONTINUE
"approach"  (for NEXT SENTENCE, EXIT whatever, etc).  In my opinion, these
"implicit CONTINUE" statements are virtual (as someone said in an earlier
note).  They *never* exist - all they are, are places to go "as if".  In
other words, it is IMPOSSIBLE to need the CONTINUE associated with NEXT
SENTENCE and the one for EXIT PROGRAM at the same time - as they exist ONLY
at run-time and only one of those statements can possibly be "in effect" at
any one time.

Therefore, (to me - but not as I understand it to J4 or Germany), this is
simply a "non-issue".  Those two CONTINUEs simply NEVER exist together - so
there is no issue about what order they are in.
```

#### ↳ Re: New Wording for EXIT rules.

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-07-06T01:30:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tkajacaqng9484@corp.supernews.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com> <9i2jrm$uq7$1@slb4.atl.mindspring.net>`

```
Not surprisingly, I disagree with your explanation. :-)

Having spent several more hours with the FCD, it occurs to
me that there is no statement about how to interpret the rules.

If EXIT GR 10 is interpreted statically, there is a problem!

If EXIT GR 10 is interpreted dynamically, there is no problem!

As I use dynamic interpretation, the rule does not apply until
the required conditions occur. As the compiler processes
items (tokens), the set of "active" rules will change.

For IF GR 4, the condition for processing implicit CONTINUE
is "the next separator period". For the example, the separator
period is obvious.

For EXIT GR 10, the condition is "the last statement in the current
paragraph." This condition cannot occur until the token stream
advances to "the next paragraph-name or section-name, ..." as
defined in 14.5.2. This is because the compiler cannot determine
the last statement until the end of paragraph is known. By the time
it finds the end of the paragraph, all other implicit CONTINUEs,
except that for EXIT SECTION, will have been processed; their
rules having been triggered by other conditions, now passed.

For EXIT GR 11, the condition "the last statement in the last
paragraph in the current section" cannot be known until the
token stream advances to the word "SECTION" in the next
section header. (See 14.5.1 for the definition of section.)

Using dynamic interpretation of the rules, clears up a few
other problems I had with the FCD.

I have worked on this problem, off and on, for more than one
year. I recommend the wording of EXIT GRs 10 and 11 remain
unchanged and withdraw all previous suggested changes.
------------------
Rick Smith

William M. Klein wrote in message <9i2jrm$uq7$1@slb4.atl.mindspring.net>...
>This ties in with the original German comment on the "implicit" CONTINUEs.
>
…[60 more quoted lines elided]…
>
```

##### ↳ ↳ Re: New Wording for EXIT rules.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-07-08T14:27:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b486da8.48849287@news1.attglobal.net>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com> <9i2jrm$uq7$1@slb4.atl.mindspring.net> <tkajacaqng9484@corp.supernews.com>`

```
Thanks Rick - that's what I said to start with!

On Fri, 6 Jul 2001 01:30:02 -0400, "Rick Smith"
<ricksmith@aiservices.com> wrote:

>Not surprisingly, I disagree with your explanation. :-)
>
…[103 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: New Wording for EXIT rules.

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-10T17:03:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107101603.5fb80ebb@posting.google.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com> <9i2jrm$uq7$1@slb4.atl.mindspring.net> <tkajacaqng9484@corp.supernews.com> <3b486da8.48849287@news1.attglobal.net>`

```
It looks as if we have come to the end of the discussion...  Any more
comments before I write it up?  The write-up will be posted for
critique, of course.

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: New Wording for EXIT rules.

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-07-11T12:48:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0107111148.1d2feca4@posting.google.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com> <9i2jrm$uq7$1@slb4.atl.mindspring.net> <tkajacaqng9484@corp.supernews.com> <3b486da8.48849287@news1.attglobal.net> <4145699b.0107101603.5fb80ebb@posting.google.com>`

```
Stephen,

Before you go to the trouble, look at 01-0456.

stephenjspiro@hotmail.com (Stephen J Spiro) wrote in message news:<4145699b.0107101603.5fb80ebb@posting.google.com>...
> It looks as if we have come to the end of the discussion...  Any more
> comments before I write it up?  The write-up will be posted for
…[3 more quoted lines elided]…
> Member, J4 COBOL Standards Committee
```

##### ↳ ↳ Re: New Wording for EXIT rules.

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-10T15:16:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ifur8$a00$1@mail.pl.unisys.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com> <9i2jrm$uq7$1@slb4.atl.mindspring.net> <tkajacaqng9484@corp.supernews.com>`

```
After studying Rick's proposals, and Thane's "massaging" of them to match
context and standards wording conventions better, I've come to agree with
the basic idea.  The existing rules are correct but perhaps unclear, and I
believe the changes they've come up with resolve the issues.  And while the
wording of EXIT GR10 and 11 is unchanged, notes are added to clarify the
application of those rules.  This is a better solution than mine.

    -Chuck Stevens

Rick Smith <ricksmith@aiservices.com> wrote in message
news:tkajacaqng9484@corp.supernews.com...
> Not surprisingly, I disagree with your explanation. :-)
>
…[38 more quoted lines elided]…
> William M. Klein wrote in message
<9i2jrm$uq7$1@slb4.atl.mindspring.net>...
> >This ties in with the original German comment on the "implicit"
CONTINUEs.
> >
> >As I understood the German comment (and I am NOT certain that I do), they
> >were concerned about all the "implicit" statements and which one
came/comes
> >first.
> >
> >In my opinion, this is a "misunderstanding" of the implicit CONTINUE
> >"approach"  (for NEXT SENTENCE, EXIT whatever, etc).  In my opinion,
these
> >"implicit CONTINUE" statements are virtual (as someone said in an earlier
> >note).  They *never* exist - all they are, are places to go "as if".  In
> >other words, it is IMPOSSIBLE to need the CONTINUE associated with NEXT
> >SENTENCE and the one for EXIT PROGRAM at the same time - as they exist
ONLY
> >at run-time and only one of those statements can possibly be "in effect"
at
> >any one time.
> >
> >Therefore, (to me - but not as I understand it to J4 or Germany), this is
> >simply a "non-issue".  Those two CONTINUEs simply NEVER exist together -
so
> >there is no issue about what order they are in.
> >
…[45 more quoted lines elided]…
>
```

#### ↳ Re: New Wording for EXIT rules.

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-07-07T14:12:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tkekai9njfho86@corp.supernews.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <tk7rl1qfvvs010@corp.supernews.com> <9i2jrm$uq7$1@slb4.atl.mindspring.net>`

```
I did not previously explain my disagreement. Let's begin
with a definition, a fact, and an opinion.

a. An implicit CONTINUE statement is a CONTINUE statement
whose existence is implied by the rules of COBOL.

b. The location of that CONTINUE statement is stated in the
rule that implies the existence of the CONTINUE statement.

c. The compilation process proceeds "as if" these CONTINUE
statements where explicitly coded CONTINUE statements.

These three statements convey my understanding of the use
of implicit CONTINUE statements in the FCD. With this
understanding, all run time behavior of the transfers of control
to each implicit CONTINUE statement is included in the
executable code produced by the compiler.

With this understanding and with dynamic interpretation, there
remains, at least, one conflict I cannot resolve within the current
rules. This occurs with an inline PERFORM statement when the
following conditions are present:

1. A declarative containing RESUME NEXT STATEMENT is
coded.

2. A TURN directive activates checking for an exception
condition which uses that declarative.

3. The evaluation of expressions within the phrases of the
PERFORM statement may cause the exception condition.

4. The PERFORM has an EXIT PERFORM statement,
without the CYCLE phrase, within it.

The conflict is that RESUME NEXT STATEMENT requires
an implicit CONTINUE statement "immediately" following the
PERFORM statement ("the statement that was executing
when control was transferred to the declarative"). This is
equivalent to "immediately" following the END-PERFORM.
The EXIT PERFORM requires an implicit CONTINUE
statement at that same point.

While this conflict has no practical consequence for execution
of the program, finding these conflicts, at least, provides me
with a source of wry amusement until I find a problem with
practical consequences.
------------------
Rick Smith

William M. Klein wrote in message <9i2jrm$uq7$1@slb4.atl.mindspring.net>...
>This ties in with the original German comment on the "implicit" CONTINUEs.
>
…[19 more quoted lines elided]…
> wmklein <at> ix.netcom.com
[...]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
