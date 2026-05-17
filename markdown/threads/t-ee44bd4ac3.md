[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Occurs Depending on

_4 messages · 4 participants · 1996-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Occurs Depending on

- **From:** "mike krueger" <ua-author-1374644@usenetarchives.gap>
- **Date:** 1996-04-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<317E8F91.A42@mobility.com>`

```
Cobol/370

I don't know before execution how many occurrences of a table element there
are so I am setting up a variable-length table definition using the OCCURS
DEPENDING ON clause.

Does anyone have any experience that would suggest that using OCCURS
DEPENDING ON clause is not worth the aggravation or any other comments about
this statement for or against its use.

Background: This structure is being used in a large billing program where
performance is always a consideration.
```

#### ↳ Re: Occurs Depending on

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1996-04-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee44bd4ac3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<317E8F91.A42@mobility.com>`
- **References:** `<317E8F91.A42@mobility.com>`

```
Mike Krueger wrote:
› 
› Cobol/370
…[10 more quoted lines elided]…
› performance is always a consideration.

I'm not sure what kind of aggravation you are experiencing. Generally,
the two most common problems with table handling (fixed or variable
occurrences) is index or subscript errors and not including code in the
program to check that you do not try to load more entries in a table
than are defined. This, of course, causes a multitude of problems
ranging from SOC7 data errors to program boundary errors.

The most important consideration for OCCURS DEPENDING ON is its use
for variable-length records. While an OCCURS DEPENDING ON table in
working-storage will allocate the maximum memory needed, variable-
length records will only be written out based on the size of
the occurrence.

I would not suspect there a any performance issues of any significance
to worry about.
```

#### ↳ Re: Occurs Depending on

- **From:** "harry d. fisher" <ua-author-17086939@usenetarchives.gap>
- **Date:** 1996-04-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee44bd4ac3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<317E8F91.A42@mobility.com>`
- **References:** `<317E8F91.A42@mobility.com>`

```

dlm··.@iqu··t.net (Doug Miller) wrote:
› Mike Krueger  wrote:
›› Cobol/370
…[21 more quoted lines elided]…
› 
Actually, OCCURS DEPENDING is an excellent construct and should be used
rather than a fixed length table. That way, you always know how many
occurrences you have.

By the way, it's too bad you don't use Micro Focus PC Cobol option.
They have a facility called ODOSLIDE, (Occurs Depending On SLIDE), which
allocates only the number of occurrences you actually have in your
table. Ordinarily COBOL allocates the maximum size of the table. With
ODOSLIDE, additional occurences are allocated in extended memory.

In any even, I strongly recommend using the Depending on option.
```

##### ↳ ↳ Re: Occurs Depending on

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-04-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee44bd4ac3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ee44bd4ac3-p3@usenetarchives.gap>`
- **References:** `<317E8F91.A42@mobility.com> <gap-ee44bd4ac3-p3@usenetarchives.gap>`

```

"Harry D. Fisher" wrote:

› dlm··.@iqu··t.net (Doug Miller) wrote:
›› Mike Krueger  wrote:
…[6 more quoted lines elided]…
› snip    >>
 
› Actually, OCCURS DEPENDING is an excellent construct and should be used
› rather than a fixed length table.  That way, you always know how many
› occurrences you have.
 
› By the way, it's too bad you don't  use Micro Focus PC Cobol  option.   
› They have a facility called ODOSLIDE, (Occurs Depending On SLIDE), which 
› allocates only the number of occurrences you actually have in your 
› table.   Ordinarily COBOL allocates the maximum size of the table.  With 
› ODOSLIDE, additional occurences are allocated in extended memory.
 
› In any even, I strongly recommend using the Depending on option.

odoslide assists in an IBM contruct that allows additional fixed
length fields to "slide" down to butt next to a variable occurs.
(of course the occured fields must be build BEFORE the fixed)

01 big-data.
05 somefixed pic x....
05 ... occurs depending on...
etc
05 anotherfixed (actually another occurs depending is allowed)
NEAT for string variable lengths together and putting the depending
variables with the early fixed part of the record.

JR

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
