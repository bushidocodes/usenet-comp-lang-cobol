[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to get address of Cobol variable?

_3 messages · 3 participants · 1998-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: How to get address of Cobol variable?

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1998-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a4f6e0.18100807@news.enter.net>`
- **References:** `<6n8a1q$o98$1@news5.ispnews.com> <3598987D.8CE0AD60@IMN.nl> <359A25FC.12B5@ibm.net> <359B9FD9.C7236A0@IMN.nl>`

```
"Cobol Frog (Huib Klink)" <H.Klink@IMN.nl> wrote:

>/SERIOUS on
>To add: neither variable need to be in linkage section, but may be anywhere in
…[17 more quoted lines elided]…
>

Froggy:

I always thought you had to have a terminating /SERIOUS off command.
Are you telling me that a /JOKE off command automatically sets
/SERIOUS on?


Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: How to get address of Cobol variable?

- **From:** "COBOLFrog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AB109B.636D113B@IMN.nl>`
- **References:** `<6n8a1q$o98$1@news5.ispnews.com> <3598987D.8CE0AD60@IMN.nl> <359A25FC.12B5@ibm.net> <359B9FD9.C7236A0@IMN.nl> <35a4f6e0.18100807@news.enter.net>`

```
Bob Wolfe wrote:

> "Cobol Frog (Huib Klink)" <H.Klink@IMN.nl> wrote:
>
> >/SERIOUS on

8<

> >/JOKE on

8<

> >/JOKE off (to get SERIOUS default)

8<

> Froggy:
>
> I always thought you had to have a terminating /SERIOUS off command.
> Are you telling me that a /JOKE off command automatically sets
> /SERIOUS on?

/JOKE offBob,

Both /serious and /joke work on the same serious bit: 0 = fun, 1 = not
rem /SERIOUS on sets 1
rem /SERIOUS off sets 0
rem /JOKE on sets 0
rem /JOKE off sets 1
The rems are to keep it on!

The Frog
```

##### ↳ ↳ Re: How to get address of Cobol variable?

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oh5li$23s@bgtnsc03.worldnet.att.net>`
- **References:** `<6n8a1q$o98$1@news5.ispnews.com> <3598987D.8CE0AD60@IMN.nl> <359A25FC.12B5@ibm.net> <359B9FD9.C7236A0@IMN.nl> <35a4f6e0.18100807@news.enter.net> <35AB109B.636D113B@IMN.nl>`

```
COBOLFrog (Huib Klink) wrote:
> 
(snip)

> Vandaag is de eerste dag van de rest van je leven! Maak er wat van!
> Today is de first day of the rest of your life!

True, but so is tomorrow!

Bill Lynch :-)

> Use it!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
