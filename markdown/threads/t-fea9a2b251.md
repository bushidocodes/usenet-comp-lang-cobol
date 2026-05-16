[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and Perl

_1 message · 1 participant · 1998-09_

---

### Re: COBOL and Perl

- **From:** Darrin Edwards <d-edwards@nospam.uchicago.edu>
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.perl.misc,comp.lang.cobol
- **Message-ID:** `<tgr9xnx1dc.fsf@noise.bsd.uchicago.edu>`
- **References:** `<6r7fi0$9a7$1@nnrp1.dejanews.com> <6rldhj$na5@lotho.delphi.com> <tglnnz8roi.fsf@noise.bsd.uchicago.edu> <6t0dk0$ep5$4@news.enterprise.net>`

```
scm@enterprise.net (Shaun C. Murray) writes:

> >Well, I think that depends on the problem domain the language is
> >designed to handle.  Again, I don't think this criticism is particular
…[10 more quoted lines elided]…
> notation for that that's evolved over 100's of years.

So one might infer from the age and popularity of such notational
conveniences that notational conveniences are sometimes considered
useful.
[More on shorthand at end.]

> >If I say that I really don't understand whether "test-data" and
> >"data-rec" here are builtin operators, user-supplied functions, or
…[4 more quoted lines elided]…
> from other languages. Try just reading it as English.
[snip my guesses]
> Nope that's all it was doing and you had more than a vague idea. From not 
> seeing any COBOL before, you know what the program segment was doing.
> Does that prove my point?

I said I didn't understand some of the constructs.  You said "Try reading
it as English," and I still don't understand what some of the constructs are
or what they are meant to do.  If your point was that the semantics
should be trivially extractable from the syntax, even for someone who
(like me) does not know the syntax, then I would have to say no.  (Does
this prove my point, that even a "relatively simple" syntax does not
guarantee transparency of semantics?)

> >  Is data-file the actual filename, or
> >is it a variable for a filename supplied elsewhere?
…[3 more quoted lines elided]…
> you understood it was a file.

Just as one might reasonably guess that a line of perl code like

$next_line = <DATA_FILE>;

was reading in another line of input from a data file.

> COBOL punctuation makes sense if you know English.

No; I know English, and didn't thoroughly understand your
example.  COBOL punctuation makes sense if you know COBOL.

> >Seriously, let's
> >take a simple example: line-termination chars vs. line-continuation
> >chars.

> COBOL doesn't have line termination of line continuation characters except in
	^^^^^^^^^^^^
> the case where you want to continue a long string. You stick a hyphen at the 
> beginning of the next line.

[snip COBOL e.g.'s]

> >  Since I don't see any of the former in your example, I'm gonna
> >guess that COBOL uses some punctuation to denote that a line is
…[3 more quoted lines elided]…
> See above. That's a wrong assumption. If I write a long sentance than
		      ^^^^^^^^^^^^^^^^
> continues onto another line I can work out that it continues by parsing
> it. Why can't a computer?
…[6 more quoted lines elided]…
> You're wrong.
	^^^^^^^

So my _guess_ as to the semantics based only on a _limited knowledge_
of COBOL syntax from several lines of code was _wrong_.  Good, that's
pretty much the point I was trying to make! :)

> >To sum up an already long post: I don't think this is a criticism
> >of perl per se (these features are shared by many languages).
…[5 more quoted lines elided]…
> Simplification makes it much easier to understand other peoples code.

And simplification means different things in different problem
domains.  Do you disagree that a notational convenience ("shorthand")
can be a simplification?  Are your criticisms particular to perl?

> >> I don't want to learn shorthand as 
> >> only people who know shorthand can read it.
…[6 more quoted lines elided]…
> written it.

[Back to shorthand]
I wasn't calling you a secretary.  I was trying to point out examples
of problem domains in which shorthand could be useful.  One person's
"shorthand" ("line noise" was where I jumped in this thread :))
is another's mission-critical tool.

Darrin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
