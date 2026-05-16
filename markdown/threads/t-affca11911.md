[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Date data-type?

_5 messages · 3 participants · 2006-08_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Date data-type?

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2006-08-08T19:39:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N7SdnZu-0s7sR0XZnZ2dnUVZ8qCdnZ2d@pipex.net>`

```
Hi,

I know some of the posters here take a keen interest in the 
proposed standards for Cobol.

Do you know if a date data-type has (ever) been proposed; if 
yes, what cogent reasons led to its exclusion?

If it's not presently proposed, how exposed does that leave 
Cobol, when it's proposed as a viable commercial language?

Ok, the question might not be perfect; make of it what you 
think is better .... and answer that!   :-)

Regards

Michael
```

#### ↳ Re: Date data-type?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-08-08T21:53:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sJ7Cg.337254$Zr.85193@fe06.news.easynews.com>`
- **References:** `<N7SdnZu-0s7sR0XZnZ2dnUVZ8qCdnZ2d@pipex.net>`

```
All previous discussion of a specific "date" data-type have been rejected. 
HOWEVER, the draft '08 Standard does have functions to "format" dates (based on 
locale).  Is this what you looking for?
```

##### ↳ ↳ Re: Date data-type?

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2006-08-09T19:07:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I76dnd9L95DEuUfZnZ2dnUVZ8sydnZ2d@pipex.net>`
- **In-Reply-To:** `<sJ7Cg.337254$Zr.85193@fe06.news.easynews.com>`
- **References:** `<N7SdnZu-0s7sR0XZnZ2dnUVZ8qCdnZ2d@pipex.net> <sJ7Cg.337254$Zr.85193@fe06.news.easynews.com>`

```
No, William, not really.

I'd expect to see the ability to define a field as a date, 
perform date arithmetic; have an "if date" test (like "if 
numeric"), too, besides the functions you mention.

I'd also expect this to extend to date-time, with similar
functionality for this.

Heavens, how long have spread-sheets been offering 
'date'-types, let alone databases ...

What's the point of Cobol just seemingly ignoring
this obvious possible improvement.

It just acts as a credibility deficit, imo.

Not vitally important, in operational terms, maybe,
but missing a trick here, proponents of Cobol.
(there are some, perhaps?)  :-)

Michael

William M. Klein wrote:
> All previous discussion of a specific "date" data-type have been rejected. 
> HOWEVER, the draft '08 Standard does have functions to "format" dates (based on 
> locale).  Is this what you looking for?
>
```

###### ↳ ↳ ↳ Re: Date data-type?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-08-09T12:17:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh9kd2t6mult7p3vc06qb0qkpemneadidg@4ax.com>`
- **References:** `<N7SdnZu-0s7sR0XZnZ2dnUVZ8qCdnZ2d@pipex.net> <sJ7Cg.337254$Zr.85193@fe06.news.easynews.com> <I76dnd9L95DEuUfZnZ2dnUVZ8sydnZ2d@pipex.net>`

```
That's a big reason library based languages have pretty much taken
over.    When someone wants to have a date data type with a library
language, he either downloads it or adds it.   No Codysyl needed.
```

###### ↳ ↳ ↳ Re: Date data-type?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-08-09T20:27:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uyrCg.366548$tQ4.19608@fe01.news.easynews.com>`
- **References:** `<N7SdnZu-0s7sR0XZnZ2dnUVZ8qCdnZ2d@pipex.net> <sJ7Cg.337254$Zr.85193@fe06.news.easynews.com> <I76dnd9L95DEuUfZnZ2dnUVZ8sydnZ2d@pipex.net>`

```
FYI,
  IBM (possibly others) included this as an EXTENSION in their compiler before 
Y2K.  This included a lot of "100-year window" option stuff.

Users did NOT find it worth using and although it is still in their compiler, I 
know of almost no users of it.

Most "existing" COBOL shops have routines to do this and very few "new" COBOL 
sites discover a need to "invent" them (is my perception).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
