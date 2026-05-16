[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Useless conditional compilation?

_14 messages · 8 participants · 2000-08 → 2001-08_

---

### Useless conditional compilation?

- **From:** Herwig Huener <Herwig.Huener@fujitsu-siemens.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3993D947.CAE2B464@fujitsu-siemens.com>`

```
2000-08-11 12:50:00 MESZ

Consider this:

       >> if blahblah = "something"
       >> if blahblah = "something"
          ... some code ...
       >> end-if
       >> end-if

Obviously nonsense. Should a OO-Cobol compiler
give a hint in such cases?

As for the conditional compilation in OO-Cobol
I am implementing right now, I am not issuing
a warning in this case: If a programmer wants
garbage, I let him have it.

Also, catching such cases in all generality
might be quite difficult.

Herwig
```

#### ↳ Re: Useless conditional compilation?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n1dpv$52e$1@slb7.atl.mindspring.net>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com>`

```
There is nothing "sillier" with that code than having a "normal" piece of
code saying,

  If A = "A"
      If A = "A"
           perform whatever            *> this is always true
       Else
          Perform something-else   *> this is never possible
      End-if
   End-If

some compilers do issue an INFORMATIONAL message on code that is always true
or always false.  However, the code is ANSI/ISO conforming so any compiler
claiming to be conforming must support it.
```

##### ↳ ↳ Re: Useless conditional compilation?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39944A3E.CF5AEBFE@brazee.net>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <8n1dpv$52e$1@slb7.atl.mindspring.net>`

```


"William M. Klein" wrote:

> There is nothing "sillier" with that code than having a "normal" piece of
> code saying,
…[11 more quoted lines elided]…
> claiming to be conforming must support it.

Some languages this is common.  I have even seen the informational error with
Cobol, both where it was useful to catch an error, and where it was intentional.

It can be used similarly to the REXX command DO FOREVER, but I am not thinking
of a case off the top of my head where I would code that way.
```

#### ↳ Terminology (was: Useless conditional compilation?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n1e5p$euq$1@nntp9.atl.mindspring.net>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com>`

```
Herwig,
  I may be a little sensitive on this, but one thing in your terminology
bothers me.

"OO-COBOL" does *not* support/require conditional compilation.

The draft Standard which includes OO  support (among MANY other things) also
includes conditional compilation.

It is ENTIRELY possible to create a COBOL compiler with OO but not
conditional compilation AND VICE VERSA.  Micro Focus (for example) supported
conditional compilation LONG before they introduced support for OO. Fujitsu
currently supports much of the draft Standard's OO but no conditional
compilation.

If you are talking about implementing the draft Standard, then it is
preferable (IMHO) to use the phrase COBOL-200x or the next COBOL Standard -
but it is NOT correct to call the entire language "OO-COBOL".

(And <G> absolutely not correct to call it "OO-Cobol")
```

##### ↳ ↳ Re: Terminology (was: Useless conditional compilation?

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3994870F.7C7B1DAF@Josella-Simone-Playton.de>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <8n1e5p$euq$1@nntp9.atl.mindspring.net>`

```
2000-08-12 01:04:16 MEST

"William M. Klein" wrote:
> 
> Herwig,
…[12 more quoted lines elided]…
> compilation.

I know these two concepts are orthogonal to each other - but I
often formulate things less precise for the sake of brevity.

As for my company, we would like to implement the full stuff.
Might be that we fail (unlikely), but the intent is there.

> If you are talking about implementing the draft Standard, then it is
> preferable (IMHO) to use the phrase COBOL-200x or the next COBOL Standard -
> but it is NOT correct to call the entire language "OO-COBOL".

what about Cobol++? - OK, just kiding.

> (And <G> absolutely not correct to call it "OO-Cobol")

Mmh. what was Mrs. oppers opinion about this?

Herwig
```

###### ↳ ↳ ↳ Re: Terminology (was: Useless conditional compilation?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n278g$scb$1@nntp9.atl.mindspring.net>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <8n1e5p$euq$1@nntp9.atl.mindspring.net> <3994870F.7C7B1DAF@Josella-Simone-Playton.de>`

```
"Herwig Huener & Josella Simone Playton"
<webmaster@Josella-Simone-Playton.de> wrote in message
news:3994870F.7C7B1DAF@Josella-Simone-Playton.de...
> 2000-08-12 01:04:16 MEST
>
 <snip>
>
> > (And <G> absolutely not correct to call it "OO-Cobol")
>
> Mmh. what was Mrs. oppers opinion about this?

One more time for those who haven't read it from me before. Please look at
the "Acknowledgement" at the start of every ANSI/ISO COBOL Standard (and most
vendor's LRM) for an explanation of WHY this language *must* be referred to
as "COBOL" and not "Cobol" - unless you want to take it out of the "public
domain".
```

###### ↳ ↳ ↳ Re: Terminology (was: Useless conditional compilation?

_(reply depth: 4)_

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39951776.7BE7DF39@Josella-Simone-Playton.de>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <8n1e5p$euq$1@nntp9.atl.mindspring.net> <3994870F.7C7B1DAF@Josella-Simone-Playton.de> <8n278g$scb$1@nntp9.atl.mindspring.net>`

```
2000-08-12 11:11:11 MESZ

"William M. Klein" wrote:
> 
> ...
…[5 more quoted lines elided]…
> domain".

I have a copy at work, not here at home.

BTW: Here in Germany we have a lawyer who's main interest
are such details of whether a word is in public domain or
owned privately as a trademark and such. Even Microsoft
pays dues to a small company in Germany who "invented"
the word "Explorer" before Microsoft did.

I feel that this is a misuse of the law. Maybe his lawyer
could be tempted to look at the words "COBOL" or "Cobol"
and take action against somebody, based on subtle legal
interpretations. Quite a few people wait for that, and
they wait for hom making an error.

If he does, maybe one can make him feel the heat.

In personal communication, everybody is entitled to use,
misuse and misspelling of any word. The risk is not
being understood - but beyond that, freedom of speech
is more important than precision of wording.

But this is an entirely other subject. - Excuse me when
my English is insuffucient for legal matters.

Herwig Huener
```

##### ↳ ↳ Re: Terminology (was: Useless conditional compilation?

- **From:** rovani@rech.com.br
- **Date:** 2001-08-09T01:34:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9kspc1$fl1$1@news.netmar.com>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <8n1e5p$euq$1@nntp9.atl.mindspring.net>`

```

   The absence of conditional compilation in PowerCobol, in my opinion is a
great deficiency. In my company we have PowerCobol since 1998, but up to now
we could not migrate from NetExpress to Fujitsu due to absence of this
resource. We used the conditional compilation a lot in NetExpress, to
increase the reuse of Copy's in several programs that are a little different
some of the other ones.

   I don't get to understand because Fujitsu still didn't implement the
conditional compilation in Fujitsu COBOL/PowerCobol.

   Another great lack in PowerCobol is the absence of SORT for tables
(occurs).
I apologize for my bad English.

Rovani Marcelo Rech
Novo Hamburgo/RS - Brazil


In article <8n1e5p$euq$1@nntp9.atl.mindspring.net>, William M. Klein
<wmklein@nospam.ix.netcom.com> writes:
>Herwig,
>  I may be a little sensitive on this, but one thing in your terminology
…[46 more quoted lines elided]…
>


 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

###### ↳ ↳ ↳ Re: Terminology (was: Useless conditional compilation?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-08-10T14:52:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l1e6o$lab$1@slb7.atl.mindspring.net>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <8n1e5p$euq$1@nntp9.atl.mindspring.net> <9kspc1$fl1$1@news.netmar.com>`

```
Both of those features ARE included in the draft of the next ANSI/ISO
Standard.  Have you contacted Fujitsu to see what their plans are for them?
(They have already implemented AS EXTENSIONS many - but not all - the
features from the draft.)

NOTE WELL: "conditional compilation" in the draft Standard is NOT identical
to that in Micro Focus COBOL - but could "easily" be converted from/to it.
```

#### ↳ Re: Useless conditional compilation?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3993DCEB.A7ECFF@zip.com.au>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com>`

```
Herwig Huener wrote:
> 
> 2000-08-11 12:50:00 MESZ
…[18 more quoted lines elided]…
> might be quite difficult.

The answer is no,  for optimizing compilers it should warn of such
stupidity because it should understand such stupidity.  Precompiler
are a fairly cheap process in the scheme of things,  they should not
be made too complex.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

##### ↳ ↳ Re: Useless conditional compilation?

- **From:** Herwig Huener <Herwig.Huener@fujitsu-siemens.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3993F1BC.49DEC988@fujitsu-siemens.com>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <3993DCEB.A7ECFF@zip.com.au>`

```
2000-08-11 14:33:41 MESZ

Ken Foskey wrote:
>
> ...
…[4 more quoted lines elided]…
> be made too complex.

Analyzing directives is not a precompiler-activity. Some
directives give later phases concrete hints about what to do.
So, analyzing directives is best done in a first phase -
sort of parallel to the already existing source-text-manipulation
stuff.

To make things more complicated, we *have* a precompiler - an
ESQL-Precompiler. This is indeed a genuine precompiler, which
partly analyzes Cobol and converts the ESQL-stuff into comments
and calls to the database.

This ESQL-Precompiler understands some but not all Cobol - and
of course, it does not understand OO-Cobol. However, in some
easy cases, OO-Cobol is allowed to pass the precompiler without
anything harmful taking place.

In case we make the ESQL-precompiler fit for for OO-Cobol, the
precompiler needs to understand, among other things, conditional
compilation. I see a case of code-duplication there and I do not
like it. But things are not yet thoroughly discussed and
understood.

Herwig
```

###### ↳ ↳ ↳ Re: Useless conditional compilation?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39953AED.A7EE3904@zip.com.au>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com> <3993DCEB.A7ECFF@zip.com.au> <3993F1BC.49DEC988@fujitsu-siemens.com>`

```
Herwig Huener wrote:
> 
> In case we make the ESQL-precompiler fit for for OO-Cobol, the
…[3 more quoted lines elided]…
> understood.

All instances of conditionals and SQL precompilers that I have seen do
not do this.  It is the programmers responsibility to make the
precompilers work together.  Making them talk together only allows the
programmer to write very confusing code.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

#### ↳ Re: Useless conditional compilation?

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sp83f9t1n4t171@corp.supernews.com>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com>`

```
Conditional compilation should, in my opinion, simply be
compile-time evalution of some conditionals.

Clearly one could build an interpreter instead of a compiler.  Then
"conditional compilation" must act just like other run-time IF
statements, in that they would get evaluated at runtime.

So the issues of "ugly nesting" and "rats nests" of conditional
compiles is no different than the same issues for regular
conditionals.

You either fix the programmers,
live with it,
or get a tool that will fold conditionals together at the source level.
(Our DMS Reengineering Toolkit could do this.)
```

#### ↳ Re: Useless conditional compilation?

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u8s8pssao8ichv93jbrh52m9tajo2etk6i@4ax.com>`
- **References:** `<3993D947.CAE2B464@fujitsu-siemens.com>`

```
Herwig Huener <Herwig.Huener@fujitsu-siemens.com> wrote:

>2000-08-11 12:50:00 MESZ
>
…[6 more quoted lines elided]…
>       >> end-if

>Obviously nonsense. Should a OO-Cobol compiler
>give a hint in such cases?

no, but a programmer who does maintenance on the code and who has the
authority to fix it should.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
