[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Function Keys

_7 messages · 7 participants · 1999-11_

---

### Function Keys

- **From:** "Maarten Van der Biest" <van.der.biest@pandora.be>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be>`

```
Can anyone tell me how i have to work with functionkeys? The problem is that
you need to check all times if any key is pressed, and not at a specific
moment...
e.g. F12 calls a new function, but can be pressed during the entire
program...

Thanx in advance
```

#### ↳ Re: Function Keys

- **From:** docdwarf@clark.net ()
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MuhY3.38239$oa2.183930@iad-read.news.verio.net>`
- **References:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be>`

```
In article <2ccY3.301$UW4.10548@afrodite.telenet-ops.be>,
Maarten Van der Biest <van.der.biest@pandora.be> wrote:
>Can anyone tell me how i have to work with functionkeys? The problem is that
>you need to check all times if any key is pressed, and not at a specific
>moment...
>e.g. F12 calls a new function, but can be pressed during the entire
>program...

Please do your own homework.

DD
```

##### ↳ ↳ Re: Function Keys

- **From:** "Peter Demeyer" <peter.demeyer@pandora.be>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZZkY3.571$UW4.16491@afrodite.telenet-ops.be>`
- **References:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be> <MuhY3.38239$oa2.183930@iad-read.news.verio.net>`

```

<docdwarf@clark.net> wrote in message
news:MuhY3.38239$oa2.183930@iad-read.news.verio.net...
> In article <2ccY3.301$UW4.10548@afrodite.telenet-ops.be>,
> Maarten Van der Biest <van.der.biest@pandora.be> wrote:
> >Can anyone tell me how i have to work with functionkeys? The problem is
that
> >you need to check all times if any key is pressed, and not at a specific
> >moment...
…[6 more quoted lines elided]…
>
What's this fucking newsgroup for then?
```

###### ↳ ↳ ↳ Re: Function Keys

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80scd4$1dkg$1@news.hitter.net>`
- **References:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be> <MuhY3.38239$oa2.183930@iad-read.news.verio.net> <ZZkY3.571$UW4.16491@afrodite.telenet-ops.be>`

```

Peter Demeyer wrote in message ...
>
><docdwarf@clark.net> wrote in message
…[15 more quoted lines elided]…
>

The purpose of the newsgroup is stated in the FAQ
< http://www.netcom.com/~wmklein/cobolfaq.htm >.

The FAQ has statements concerning both homework
questions and the type of information to supply when
requesting help.

The original post appears as though it may be a request
for help with homework and lacks the suggested information
needed to provide a good response, specifically; the compiler
and platform.

Peter Demeyer, your question was just plain rude!
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Function Keys

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383247DD.56AC555F@att.net>`
- **References:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be> <MuhY3.38239$oa2.183930@iad-read.news.verio.net> <ZZkY3.571$UW4.16491@afrodite.telenet-ops.be>`

```
Peter Demeyer wrote:
> 
(snip)

> > >you need to check all times if any key is pressed, and not at a specific
> > >moment...
…[7 more quoted lines elided]…
> What's this fucking newsgroup for then?

It's NOT here to do your fucking homework, just so we're clear on that
point.

Bill Lynch
```

#### ↳ Re: Function Keys

- **From:** "Hansjoerg Kaempf" <hjkaempf@wfeca.net>
- **Date:** 1999-11-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s35ecfi1hsq34@corp.supernews.com>`
- **References:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be>`

```
Dear Maarten Van der Biest,

It is no surprise to me, that you don't get an answer from this user group.

1) DD is an asshole, and everybody know it.

2) I tend to agree with Peter Demeyer - except the "fucking".

3) Rick Smith is blaming Peter for being rude - but accepts the rudeness of
DD?

4) Bill Lynch is wrong because nobody was asking for doing his/hers
homework.

Unfortunately dear Maarten, I don't have the answer.

Regards, Hansj�rg
Maarten Van der Biest <van.der.biest@pandora.be> wrote in message
news:2ccY3.301$UW4.10548@afrodite.telenet-ops.be...
> Can anyone tell me how i have to work with functionkeys? The problem is
that
> you need to check all times if any key is pressed, and not at a specific
> moment...
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Function Keys

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8117hu$ad0$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<2ccY3.301$UW4.10548@afrodite.telenet-ops.be>`

```
    Everybody lost track of the original guestion.  This varies from
compiler to compiler and platform to platform,
but basically, you need to check for the presence of a keystroke without
actually accepting it.  the call (CBL_READ_KBD_STATUS on MF) returns at once
even if there is no keystroke waiting, and does not disturb the keystroke.

    If a keystroke exists, read it.  You will need to locate the exact
syntax yourself.  See DD's response.



Maarten Van der Biest <van.der.biest@pandora.be> wrote in message
news:2ccY3.301$UW4.10548@afrodite.telenet-ops.be...
> Can anyone tell me how i have to work with functionkeys? The problem is
that
> you need to check all times if any key is pressed, and not at a specific
> moment...
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
