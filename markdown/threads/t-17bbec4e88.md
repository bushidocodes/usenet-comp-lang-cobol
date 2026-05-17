[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help in an Evalute statement

_5 messages · 4 participants · 1995-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help in an Evalute statement

- **From:** "kmd..." <ua-author-6421711@usenetarchives.gap>
- **Date:** 1995-02-10T11:42:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3hg52e$gg2@news.tamu.edu>`

```
In the following code what is wrong? It follows the meta-language. I lost please
advise.
evaluate make also color also use-type-in also year > 1990
when "Chev" also any also "work" also "Y" goto 7000-cal
when "Chev" also any also "work" also "N" perform 7001-cal
when "Chev" also any also "family" also "Y" perform 7002-cal
when "Chev" also any also "family" also "N" perform 7003-cal
when "Chev" also any also "sports" also "Y" perform 7004-cal

Thanks,
kmd··.@tam··u.edu
```

#### ↳ Re: Help in an Evalute statement

- **From:** "bwil..." <ua-author-12789603@usenetarchives.gap>
- **Date:** 1995-02-10T16:36:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17bbec4e88-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3hg52e$gg2@news.tamu.edu>`
- **References:** `<3hg52e$gg2@news.tamu.edu>`

```
kmd··.@tam··u.edu (Kristen Blair) writes:

› In the following code what is wrong?  It follows the meta-language. I lost please
› advise.     
…[5 more quoted lines elided]…
›        when "Chev" also any also "sports" also "Y" perform 7004-cal
 
› Thanks,
›   kmd··.@tam··u.edu

The problem is in the clause "year > 1990". The EVALUATE does
not allow a relation test in the syntax. Assuming YEAR is a
numeric display field and all others alphanumeric, try:

EVALUATE MAKE ALSO COLOR ALSO USE-TYPE-IN ALSO YEAR
WHEN "Chev" ALSO ANY ALSO "work" ALSO 1991 THRU 9999
GOTO 7000-CAL
WHEN "Chev" ALSO ANY ALSO "work" ALSO 0000 THRU 1990
PERFORM 7001-CAL
WHEN "Chev" ALSO ANY ALSO "family" ALSO 1991 THRU 9999
PERFORM 7002-CAL
:: ::
:: ::
END-EVALUATE

See if this helps.

Smiles and grins,
Boyce Williams
```

##### ↳ ↳ Re: Help in an Evalute statement

- **From:** "e..." <ua-author-17073894@usenetarchives.gap>
- **Date:** 1995-02-11T17:07:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17bbec4e88-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17bbec4e88-p2@usenetarchives.gap>`
- **References:** `<3hg52e$gg2@news.tamu.edu> <gap-17bbec4e88-p2@usenetarchives.gap>`

```
In article <3hgm9h$c.··.@cab··u.edu>
bwi··.@cab··u.edu "Boyce G. Williams" writes:

› kmd··.@tam··u.edu (Kristen Blair) writes:
› 
…[15 more quoted lines elided]…
› numeric display field and all others alphanumeric, try:

Evaluate DOES allow relation test. But you don't have to use the
literals "Y" or "N" but the words TRUE or FALSE (or eventually ANY).

Provided there is no type mismatch in the other fields tested, it should
work.

Enzo------------------------------------------------------------------
And everything under the sun is in tune
but the sun is eclipsed by the moon.
Siri------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Help in an Evalute statement

- **From:** "bwil..." <ua-author-12789603@usenetarchives.gap>
- **Date:** 1995-02-13T08:30:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17bbec4e88-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17bbec4e88-p3@usenetarchives.gap>`
- **References:** `<3hg52e$gg2@news.tamu.edu> <gap-17bbec4e88-p2@usenetarchives.gap> <gap-17bbec4e88-p3@usenetarchives.gap>`

```
›› The problem is in the clause "year > 1990".  The EVALUATE does
›› not allow a relation test in the syntax.  Assuming YEAR is a
›› numeric display field and all others alphanumeric, try:
 
› Evaluate DOES allow relation test. But you don't have to use the
› literals "Y" or "N" but the words TRUE or FALSE (or eventually ANY).
 
› Provided there is no type mismatch in the other fields tested, it should
› work.
 
› Enzo------------------------------------------------------------------
› Siri------------------------------------------------------------------

Thank you. I stand corrected.

Smiles and grins,
Boyce Williams
```

#### ↳ Re: Help in an Evalute statement

- **From:** "je..." <ua-author-17087565@usenetarchives.gap>
- **Date:** 1995-02-24T11:26:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17bbec4e88-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3hg52e$gg2@news.tamu.edu>`
- **References:** `<3hg52e$gg2@news.tamu.edu>`

```
In article , t.··.@i··.net (Tony B. Shepherd) writes:
[munch]
› 
› And one of my favorites:
…[11 more quoted lines elided]…
› The 88-name symbols show up in a crossreference - literals don't.

This raises question I've had regarding the evaluate statement. I've seen
conflicting stories on whether the following is legal. It clearly isn't
'legal' using our DEC COBOL, since the compiler complains bitterly, but certain
books I've read have shown examples virtually identical to the following, and
proclaim it as legal code:

EVALUATE MAKE 03 MAKE
WHEN MAKE-CHEV PERFORM {routine-1}, 88 MAKE-CHEV "Chev"
WHEN MAKE-FORD PERFORM {routine-2}, 88 MAKE-FORD "Ford"
WHEN OTHER PERFORM {else-routine}

IOW, why can't I EVALUATE the {data-name}, and WHEN the conditionals? Of
course,

EVALUATE TRUE 03 MAKE
WHEN MAKE-CHEV IN MAKE PERFORM {routine-1}, 88 MAKE-CHEV "Chev"
WHEN MAKE-FORD IN MAKE PERFORM {routine-2}, 88 MAKE-FORD "Ford"
WHEN OTHER PERFORM {else-routine}

works just fine and is what we're using, but often the conditionals have to be
qualified, which makes for wordiness, and the other way just 'seems' natural...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
