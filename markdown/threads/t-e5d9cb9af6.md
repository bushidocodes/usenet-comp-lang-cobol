[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# determine if executable built for debugging

_4 messages · 4 participants · 2002-02 → 2002-03_

---

### determine if executable built for debugging

- **From:** rc8740@hotmail.com (Kirk Condon)
- **Date:** 2002-02-19T07:03:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dd02143.0202190703.67784313@posting.google.com>`

```
Is there a technique, from the UNIX command level, to query an
executable built using Micro Focus to determine if was built for
debugging?  (We have slow-running programs and want to rule out this
potential cause.)
```

#### ↳ Re: determine if executable built for debugging

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-02-21T16:24:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a53s3h12vu3@enews3.newsguy.com>`
- **References:** `<7dd02143.0202190703.67784313@posting.google.com>`

```

"Kirk Condon" <rc8740@hotmail.com> wrote in message
news:7dd02143.0202190703.67784313@posting.google.com...
> Is there a technique, from the UNIX command level, to query an
> executable built using Micro Focus to determine if was built
for
> debugging?  (We have slow-running programs and want to rule
out this
> potential cause.)

How about elfdump?  I know it exists on Linux, so suspect you
can get ahold if it.  It allows you to extract portions of an
executable file format.  If the debug symbols are on board, you
should be able to tell with that utility.  (I've noticed from a
search result that these functions have been taken over by
dwarfdump and stdump.)

Without knowing, I would cleverly guess its a "debug" section.
It may take some qualitative analysis of the results of that
dump to give you your answer -- sorry I can't help there either.

Good luck.
```

##### ↳ ↳ Re: determine if executable built for debugging

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-02-22T16:38:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<euud8.5613$Im1.417927@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<7dd02143.0202190703.67784313@posting.google.com> <a53s3h12vu3@enews3.newsguy.com>`

```
Can't you just look at a physical dump of the file.  Most
of the time debug symbols are obvious when you look
at a file.


"Grinder" <grinder@no.spam.maam.com> wrote in message
news:a53s3h12vu3@enews3.newsguy.com...
>
> "Kirk Condon" <rc8740@hotmail.com> wrote in message
…[22 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: determine if executable built for debugging

- **From:** gary drummond <gdrumm@ont.com>
- **Date:** 2002-03-19T08:17:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96F226.D9E058ED@ont.com>`
- **References:** `<7dd02143.0202190703.67784313@posting.google.com> <a53s3h12vu3@enews3.newsguy.com> <euud8.5613$Im1.417927@bgtnsc05-news.ops.worldnet.att.net>`

```
Russell Styles wrote:
> 
> Can't you just look at a physical dump of the file.  Most
…[29 more quoted lines elided]…
> >

file programname
It should say stripped if it has no symbols for debugging.

Gary
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
