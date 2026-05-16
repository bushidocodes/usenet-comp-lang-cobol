[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# another j4 idea-comments welcome

_6 messages · 3 participants · 2000-03_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### another j4 idea-comments welcome

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jjo4ds0oi757t5uaepq0v2079j0l49sd6i@4ax.com>`

```
Recently, I was lookig at how you use instrinsic functions....
you have a table of a fixed size, and you execute the function.

this is nice and all, but suppose you have a disk file, and you want
to run an intrinsic function on that file. you have to determine the
number of records, compile to that spec, and then reload in the
records again. solution?


      *table-indexed example
       01 ws.
           02 wa-data-array occurs 10000 times
                   indexed by index-by-clause


       procedure division.
       perform open-file
       perform read-records varying index-by-clause from 1 by 1
               until eof-switch-found-in-read-records

       COMPUTE wa-min = FUNCTION MIN (wa-data-array (index-by-clause))

       perform close-file


you see, the wa-data-array uses an index-by-clause in the function

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: another j4 idea-comments welcome

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b0q2q$ubc$1@slb7.atl.mindspring.net>`
- **References:** `<jjo4ds0oi757t5uaepq0v2079j0l49sd6i@4ax.com>`

```
Gary,
  Do you know about the ALL "subscript" that is part of the '89 Intrinsic
Function amendment (and supported by all current vendors that I know of - as
it is Standard)?

COMPUTE wa-min = FUNCTION MIN (wa-data-array (ALL))

   works today.


Similarly,

 Compute which-is-smallest = Function Ord-Min (wa-data-array (all))

will tell you which element is the smallest.
```

##### ↳ ↳ Re: another j4 idea-comments welcome

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nmr7dsg8qgqrnl9br09unf0jgnlgbmn1cn@4ax.com>`
- **References:** `<jjo4ds0oi757t5uaepq0v2079j0l49sd6i@4ax.com> <8b0q2q$ubc$1@slb7.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>COMPUTE wa-min = FUNCTION MIN (wa-data-array (ALL))
>
…[5 more quoted lines elided]…
> Compute which-is-smallest = Function Ord-Min (wa-data-array (all))

yea, but i was worrying if one didn't know the umm number of records
in an indexed file to fill a table, then all may not work well.



reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: another j4 idea-comments welcome

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b3n4b$f9o$1@nntp9.atl.mindspring.net>`
- **References:** `<jjo4ds0oi757t5uaepq0v2079j0l49sd6i@4ax.com> <8b0q2q$ubc$1@slb7.atl.mindspring.net> <nmr7dsg8qgqrnl9br09unf0jgnlgbmn1cn@4ax.com>`

```
Geoff (sorry about wrong name before - and not really understanding your
point),

Earlier versions of the  revision included what was called "dynamic tables".
This was a variation on OCCURS DEPENDING ON that would "magically" grow at
run-time (based on memory available and a few other things).  In fact
SIGNIFICANT time was spent on trying to get a "good definition" of this
facility.  It underwent (at least) 3 distinct re-writes.  UNFORTUNATELY, none
of the "designs" really worked (with other features of COBOL - such as
INITIALIZE and VALIDATE) - and every time that someone would try and come up
with a "solution" to the previous design, it would either get more
complicated, cause more new problems, or both.

If this is a feature that you would still like the committee to try and
design (for a future revision), I would think that it is still a good idea to
communicate this to J4 and/or WG4.
```

###### ↳ ↳ ↳ Re: another j4 idea-comments welcome

_(reply depth: 4)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u0vadsku8rbnmhsv8i07r6714pj5heqbka@4ax.com>`
- **References:** `<jjo4ds0oi757t5uaepq0v2079j0l49sd6i@4ax.com> <8b0q2q$ubc$1@slb7.atl.mindspring.net> <nmr7dsg8qgqrnl9br09unf0jgnlgbmn1cn@4ax.com> <8b3n4b$f9o$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Earlier versions of the  revision included what was called "dynamic tables".
>This was a variation on OCCURS DEPENDING ON that would "magically" grow at
>run-time (based on memory available and a few other things).  In fact
>SIGNIFICANT time was spent on trying to get a "good definition" of this
>facility.

someone else said it was possible to use a variable instead of the all
noun, and that's just what i was wondering.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: another j4 idea-comments welcome

_(reply depth: 4)_

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b6rk3$1k3$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<jjo4ds0oi757t5uaepq0v2079j0l49sd6i@4ax.com> <8b0q2q$ubc$1@slb7.atl.mindspring.net> <nmr7dsg8qgqrnl9br09unf0jgnlgbmn1cn@4ax.com> <8b3n4b$f9o$1@nntp9.atl.mindspring.net>`

```
    Maybe J4 could reduce their work load and speed things up by delegating
some decisions to the compiler writers.  Ie, send all of the compiler writer
groups
requests (with a time frame) for their ideas on some of the new stuff, like
dynamic tables.

    If none of the writers (IBM and MF and ??????) respond with a proposal
or a beta version,
consider the idea dead.  A good many of the really good ideas already work
anyway.

    This idea sounds oddly like "ODOSLIDE" on MF cobol with an occurs
depending on, in
the linkage section.  I still do not understand why INITIALIZE does not
work.  It could, easily.
At the very least, issue a compiler warning.

    Making the table automatic would be easier, of course.  And performing
an automatic expand
of a LARGE table could consume a lot of memory (unless you manage to allow a
multi region
(non-contiguous) table somehow).


William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:8b3n4b$f9o$1@nntp9.atl.mindspring.net...
> Geoff (sorry about wrong name before - and not really understanding your
> point),
>
> Earlier versions of the  revision included what was called "dynamic
tables".
> This was a variation on OCCURS DEPENDING ON that would "magically" grow at
> run-time (based on memory available and a few other things).  In fact
> SIGNIFICANT time was spent on trying to get a "good definition" of this
> facility.  It underwent (at least) 3 distinct re-writes.  UNFORTUNATELY,
none
> of the "designs" really worked (with other features of COBOL - such as
> INITIALIZE and VALIDATE) - and every time that someone would try and come
up
> with a "solution" to the previous design, it would either get more
> complicated, cause more new problems, or both.
>
> If this is a feature that you would still like the committee to try and
> design (for a future revision), I would think that it is still a good idea
to
> communicate this to J4 and/or WG4.
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
