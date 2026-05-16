[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SQL SUBSTRING format in Fujitsu COBOL (PARADOX)

_2 messages · 2 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### SQL SUBSTRING format in Fujitsu COBOL (PARADOX)

- **From:** HiGHBoy <hallh@evangel.edu>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7de85o$523$1@nnrp1.dejanews.com>`

```
Hi,

I'm accessing (read: learning how to deal with) a Paradox database on NT using
Fujitsu Cobol with embedded SQL.  All is fine until I tried a SUBSTRING (field
FROM 8 FOR 4), which is a valid SQL expression in Paradox Je(s)t SQL.  I get a
sqlcode of -3100 and a "syntax error (missing operator) in expression
substring...".  I tried various other forms of SUBSTRING syntax with
less-than-happy results. SUBSTRING(field,8,4) produces "undefined function".
SUBSTR is right out.

What is the format for that? The Fujitsu doc give the word SUBSTRING as a
valid expresion but doesnt give the syntax.

Thanks for any input.

Hayward
Springfield MO

-----
I think we've forgotten the Viking foremost rule of thumb: Pillage
before burn.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: SQL SUBSTRING format in Fujitsu COBOL (PARADOX)

- **From:** "G���ran Holm" <goran.holm@enator.se>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dpuhk$bs1$1@news1.enator.se>`
- **References:** `<7de85o$523$1@nnrp1.dejanews.com>`

```
Try to insert a <space> after comma, ie:
    SUBSTRING(col1, 8, 4)
which is the correct syntax on AS/400

regards
Peter Meister

HiGHBoy wrote in message <7de85o$523$1@nnrp1.dejanews.com>...
>Hi,
>
>I'm accessing (read: learning how to deal with) a Paradox database on NT
using
>Fujitsu Cobol with embedded SQL.  All is fine until I tried a SUBSTRING
(field
>FROM 8 FOR 4), which is a valid SQL expression in Paradox Je(s)t SQL.  I
get a
>sqlcode of -3100 and a "syntax error (missing operator) in expression
>substring...".  I tried various other forms of SUBSTRING syntax with
>less-than-happy results. SUBSTRING(field,8,4) produces "undefined
function".
>SUBSTR is right out.
>
…[13 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
