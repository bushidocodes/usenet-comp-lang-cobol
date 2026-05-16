[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Structure me this. . .

_6 messages · 5 participants · 2000-05_

---

### Re: Structure me this. . .

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fknt0$nu4$1@slb6.atl.mindspring.net>`

```
Replying to myself,
  Even though I consider the original code design "flawed" - I do think the
revised code (still with "odd" if not flawed "requirements") is an
improvement because it DOES show the possibility of a logic loop - mentioned
by others in this thread.  The original code had the same flaw - but "hid"
the possibility of the error.
```

#### ↳ Re: Structure me this. . .

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fmacu$ct5$1@nnrp1.deja.com>`
- **References:** `<8fknt0$nu4$1@slb6.atl.mindspring.net>`

```


> >
> > PROCEDURE DIVISION.
…[17 more quoted lines elided]…
> >  *   If you have a compiler with EXIT PARAGRAPH, you could do that
here, if
> > not
> >
…[29 more quoted lines elided]…
> >    ****

Hi Bill:

I note that you said you wouldn't do this this way
and appreciate the example.

This is the sort of thing that I would have
expected as being representative of the
structured approach and, it is what I
was expecting from the original thread.

Are people being trained to do things like
this in the name of GO TO-less programming?

Thanks

TOny Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Structure me this. . .

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39200DE3.F2D38B8C@cusys.edu>`
- **References:** `<8fknt0$nu4$1@slb6.atl.mindspring.net> <8fmacu$ct5$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> Are people being trained to do things like
> this in the name of GO TO-less programming?

I was never trained in GO TO-less programming.  I learned structured
programming the hard way, by maintaining all kinds of code and noticing
which styles took lots of time and effort and which styles made my job
easy.
```

###### ↳ ↳ ↳ Re: Structure me this. . .

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fp9cl$cj9$1@news.igs.net>`
- **References:** `<8fknt0$nu4$1@slb6.atl.mindspring.net> <8fmacu$ct5$1@nnrp1.deja.com> <39200DE3.F2D38B8C@cusys.edu>`

```

Howard Brazee wrote in message <39200DE3.F2D38B8C@cusys.edu>...
>Foodman wrote:
>>
…[6 more quoted lines elided]…
>easy.

Yup.  And probably about five years before anybody ever published a book on
"structure".  About the only thing new I learnt in reading about "structure"
was that it was possible to force a junior programmer to use it by outlawing
"GO TO".

Oh yes, and the formal terminology involved.
```

###### ↳ ↳ ↳ Re: Structure me this. . .

_(reply depth: 4)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93o0is48ohbje01724vcfqnb8kv19dvp6s@4ax.com>`
- **References:** `<8fknt0$nu4$1@slb6.atl.mindspring.net> <8fmacu$ct5$1@nnrp1.deja.com> <39200DE3.F2D38B8C@cusys.edu> <8fp9cl$cj9$1@news.igs.net>`

```
"donald tees" <donald@willmack.com> wrote:

> About the only thing new I learnt in reading about "structure"
>was that it was possible to force a junior programmer to use it by outlawing
>"GO TO".

to me, GOSUB was my first introduction to structure (we are talking
basic on grade school computers). then i went to vb, where you didn't
even need line numbers. after that, the only improvement i can see is
a gui that would work on all computers, and that has yet to happen,
unless you want to re-invent most of your software with java.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Structure me this. . .

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fpt39$lrq$1@news.igs.net>`
- **References:** `<8fknt0$nu4$1@slb6.atl.mindspring.net> <8fmacu$ct5$1@nnrp1.deja.com> <39200DE3.F2D38B8C@cusys.edu> <8fp9cl$cj9$1@news.igs.net> <93o0is48ohbje01724vcfqnb8kv19dvp6s@4ax.com>`

```

G Moore wrote in message <93o0is48ohbje01724vcfqnb8kv19dvp6s@4ax.com>...
>"donald tees" <donald@willmack.com> wrote:
>
>> About the only thing new I learnt in reading about "structure"
>>was that it was possible to force a junior programmer to use it by
outlawing
>>"GO TO".
>
…[5 more quoted lines elided]…
>

Well, for a number of years Cobol screen sections worked on dozens of
platforms.  I still have code running on PC's that the code is twenty years
old.  The screen I-O and the file locking (plus extensions) is the only
change.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
