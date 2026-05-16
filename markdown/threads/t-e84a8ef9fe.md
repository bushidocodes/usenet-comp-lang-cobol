[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help reqd in reference modification

_3 messages · 3 participants · 1998-09_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### help reqd in reference modification

- **From:** "D.Bhaskar Reddy" <Bhaskar.Reddy@pcm.bosch.de>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360F5775.52F7BA92@pcm.bosch.de>`

```
Is there any one to clear my doubt in reference modification ? Pls tell
me if the following code is valid.

With reference modification we can move a part of string into another
string like

MOVE STRING1 (1:5) TO STRING2.

This will move 5 charecters from string1 starting from charecter 1. Now
look at this

MOVE STRING1(1:LENGTH) TO STRING2.

LENGTH is a Working storage variable and holds a value 5. Is this 2nd
statement valid ? Will this work same as the previous move statement ? I
am using the VS-COBOL II compiler.

TIA & Regds
```

#### ↳ Re: help reqd in reference modification

- **From:** "Peter Ruzicka" <RuzickaP@Wien.Spardat.at>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdeade$ddb04d00$394212ac@W0188000064.f000.d0188.sd.spardat.at>`
- **References:** `<360F5775.52F7BA92@pcm.bosch.de>`

```
> 
> MOVE STRING1(1:LENGTH) TO STRING2.
> 

I think it will not work, because LENGTH is a reserved COBOL word,
but it would work, if you use another name for the variable
(and the daclaration of the variable is correct numeric).
```

#### ↳ Re: help reqd in reference modification

- **From:** Jeff Farkas <Jeffrey.Farkas@gte.net>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6unvnn$lln$2@news-1.news.gte.net>`
- **References:** `<360F5775.52F7BA92@pcm.bosch.de>`

```


D.Bhaskar Reddy wrote:

> Is there any one to clear my doubt in reference modification ? Pls tell
> me if the following code is valid.
…[15 more quoted lines elided]…
> TIA & Regds

:Yes, this should work just fine.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
