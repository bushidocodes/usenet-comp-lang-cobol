[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# printing from version 2.0.02 dos

_3 messages · 3 participants · 1999-02_

---

### printing from version 2.0.02 dos

- **From:** marianne_mayberry@yahoo.com
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ap7nl$vh1$1@nnrp1.dejanews.com>`

```
Could you possibly help me with a problem I've been having with printing from
DOS version 2.0.02?

I'm a new user, so forgive me if this question has been asked.  I've been
creating output reports for printing.  I retrieve them in the COBOL editor and
print from there.  The output appears the way I intend it to, however, when I
print there is a problem. The first page of my report always skips a line
before printing.  The consecutive pages start on the first line of the page as
it should.

Do you know what I could do in order to get the first page to begin printing
on the first line as do all the other pages?  This is a problem even my
profesor cannot solve.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: printing from version 2.0.02 dos

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mrA2.15042$OS5.15015918@news3.mia>`
- **References:** `<7ap7nl$vh1$1@nnrp1.dejanews.com>`

```
View the file in HEX.  There is probably a CR/LF pair (HEX '0D0A')
at the top.  Check the source to see if there is an initial write
or improperly initialised data.

marianne_mayberry@yahoo.com wrote in message
<7ap7nl$vh1$1@nnrp1.dejanews.com>...
>Could you possibly help me with a problem I've been having with printing
from
>DOS version 2.0.02?
>
>I'm a new user, so forgive me if this question has been asked.  I've been
>creating output reports for printing.  I retrieve them in the COBOL editor
and
>print from there.  The output appears the way I intend it to, however, when
I
>print there is a problem. The first page of my report always skips a line
>before printing.  The consecutive pages start on the first line of the page
as
>it should.
>
>Do you know what I could do in order to get the first page to begin
printing
>on the first line as do all the other pages?  This is a problem even my
>profesor cannot solve.
>
>-----------== Posted via Deja News, The Discussion Network ==----------
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: printing from version 2.0.02 dos

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b4oqe$nuh$1@news.igs.net>`
- **References:** `<7ap7nl$vh1$1@nnrp1.dejanews.com>`

```
Are you using a "PRINT AFTER"?

marianne_mayberry@yahoo.com wrote in message
<7ap7nl$vh1$1@nnrp1.dejanews.com>...
>Could you possibly help me with a problem I've been having with printing
from
>DOS version 2.0.02?
>
>I'm a new user, so forgive me if this question has been asked.  I've been
>creating output reports for printing.  I retrieve them in the COBOL editor
and
>print from there.  The output appears the way I intend it to, however, when
I
>print there is a problem. The first page of my report always skips a line
>before printing.  The consecutive pages start on the first line of the page
as
>it should.
>
>Do you know what I could do in order to get the first page to begin
printing
>on the first line as do all the other pages?  This is a problem even my
>profesor cannot solve.
>
>-----------== Posted via Deja News, The Discussion Network ==----------
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
