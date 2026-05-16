[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# moving a alpha numeric field to a numeric field

_8 messages · 6 participants · 1999-10_

---

### moving a alpha numeric field to a numeric field

- **From:** "Sinead Moore" <smoore@idb.ie>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u4opj$gbs$1@ezekiel.eunet.ie>`

```
if i moved a field with of 3 alphanumerics to a 2 digit numeric field
what happens and why?
```

#### ↳ Re: moving a alpha numeric field to a numeric field

- **From:** docdwarf@clark.net ()
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XFlN3.1013$9%5.21223@dfw-read.news.verio.net>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie>`

```
In article <7u4opj$gbs$1@ezekiel.eunet.ie>, Sinead Moore <smoore@idb.ie> wrote:
>if i moved a field with of 3 alphanumerics to a 2 digit numeric field
>what happens and why?

Please do your own homework

DD
```

#### ↳ Re: moving a alpha numeric field to a numeric field

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AamN3.43009$Ev4.37260@news3.mia>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie>`

```
Sinead Moore wrote:
>if i moved a field with of 3 alphanumerics to a 2 digit numeric field
>what happens and why?

You could have simply tried it and learned the answer faster than you
can post a message and wait for a response. ;-)
```

##### ↳ ↳ Re: moving a alpha numeric field to a numeric field

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aimN3.43018$Ev4.37498@news3.mia>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie> <AamN3.43009$Ev4.37260@news3.mia>`

```
Judson McClendon wrote:
>Sinead Moore wrote:
>>if i moved a field with of 3 alphanumerics to a 2 digit numeric field
…[3 more quoted lines elided]…
>can post a message and wait for a response. ;-)

A move to a numeric field is right-justified (or decimal aligned, if
appropriate), and truncated or zero-filled to the left, as applicable.
A move to an alpha (PIC A) or alphanumeric (PIC X) field is left-
justified and space filled or truncated to the right as applicable.

In answer to your question:
  1. The contents of the sending field must be numeric (only 0-9).
  2. The data will be right-justified in the 2 digit numeric field,
     and the leftmost position will be truncated to 2 digits.
```

###### ↳ ↳ ↳ Re: moving a alpha numeric field to a numeric field

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u51qf$lqn@dfw-ixnews16.ix.netcom.com>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie> <AamN3.43009$Ev4.37260@news3.mia> <aimN3.43018$Ev4.37498@news3.mia>`

```
Judson McClendon <judmc123@bellsouth.net> wrote in message
news:aimN3.43018$Ev4.37498@news3.mia...
> Judson McClendon wrote:
> >Sinead Moore wrote:
…[11 more quoted lines elided]…
>

Judson,
  I think (but haven't checked it out) that a MOVE from a PIC A (not PIC X)
field to a PIC 9 field is "illegal".  It's results are certainly UNDEFINED -
because the former can't include 0-9 and the latter must.
```

###### ↳ ↳ ↳ Re: moving a alpha numeric field to a numeric field

_(reply depth: 4)_

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JWsN3.144$Nw2.4786@cac1.rdr.news.psi.ca>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie> <AamN3.43009$Ev4.37260@news3.mia> <aimN3.43018$Ev4.37498@news3.mia> <7u51qf$lqn@dfw-ixnews16.ix.netcom.com>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7u51qf$lqn@dfw-ixnews16.ix.netcom.com...
> Judson McClendon <judmc123@bellsouth.net> wrote in message
> news:aimN3.43018$Ev4.37498@news3.mia...
…[16 more quoted lines elided]…
>   I think (but haven't checked it out) that a MOVE from a PIC A (not PIC
X)
> field to a PIC 9 field is "illegal".  It's results are certainly
UNDEFINED -
> because the former can't include 0-9 and the latter must.
>
…[4 more quoted lines elided]…
>

and the computer police will surround the computer...
```

###### ↳ ↳ ↳ Re: moving a alpha numeric field to a numeric field

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u704a$g86$1@news.igs.net>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie> <AamN3.43009$Ev4.37260@news3.mia> <aimN3.43018$Ev4.37498@news3.mia> <7u51qf$lqn@dfw-ixnews16.ix.netcom.com>`

```

William M. Klein wrote in message <7u51qf$lqn@dfw-ixnews16.ix.netcom.com>...
>Judson McClendon <judmc123@bellsouth.net> wrote in message
>news:aimN3.43018$Ev4.37498@news3.mia...
…[17 more quoted lines elided]…
>field to a PIC 9 field is "illegal".  It's results are certainly
UNDEFINED -
>because the former can't include 0-9 and the latter must.
>
picky, picky.
```

###### ↳ ↳ ↳ Re: moving a alpha numeric field to a numeric field

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lwoN3.43205$Ev4.39517@news3.mia>`
- **References:** `<7u4opj$gbs$1@ezekiel.eunet.ie> <AamN3.43009$Ev4.37260@news3.mia> <aimN3.43018$Ev4.37498@news3.mia> <7u51qf$lqn@dfw-ixnews16.ix.netcom.com>`

```
William M. Klein wrote:
>Judson McClendon wrote:
>> Judson McClendon wrote:
…[12 more quoted lines elided]…
>because the former can't include 0-9 and the latter must.

You are correct.  I was simply making a general statement about PIC A
being left justified, not that it could be used in this example. :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
