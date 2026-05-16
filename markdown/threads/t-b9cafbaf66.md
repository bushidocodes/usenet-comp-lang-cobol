[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF goes windows from OS/2

_5 messages · 2 participants · 1998-09_

---

### MF goes windows from OS/2

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tcrd0$34q6$1@news-inn.inet.tele.dk>`

```
(MF = Micro Focus).

I've been asking this earlier as a part of a mail. But since noone has
answered, here is the question again:

we have a large COBOL  (Microfocus 4.0.26) application presently running in
OS/2. We'll be using Win95 soon. So I'd really like to know if you know
what's going to happen: We're going to use MF for windows. Will my OS/2
application compile with no problems?

Kennet
```

#### ↳ Re: MF goes windows from OS/2

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298254.72653.13910@kcbbs.gen.nz>`
- **References:** `<6tcrd0$34q6$1@news-inn.inet.tele.dk>`

```
In message <<6tcrd0$34q6$1@news-inn.inet.tele.dk>> "kennet" <kennet@post11.tele.dk> writes:
> 
> I've been asking this earlier as a part of a mail. But since noone has
> answered, here is the question again:

Perhaps no one knew the answer.

> 
> we have a large COBOL  (Microfocus 4.0.26) application presently running in
> OS/2. We'll be using Win95 soon. So I'd really like to know if you know
> what's going to happen: We're going to use MF for windows. Will my OS/2
> application compile with no problems?

That may depend on how you coded the application.  Did you use
OS/2 APIs ?  Or is it just an ADIS program ?
```

##### ↳ ↳ Re: MF goes windows from OS/2

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tg1ok$53ea$1@news-inn.inet.tele.dk>`
- **References:** `<6tcrd0$34q6$1@news-inn.inet.tele.dk> <3298254.72653.13910@kcbbs.gen.nz>`

```
It's strictly ADIS.

Richard Plinston skrev i meddelelsen <3298254.72653.13910@kcbbs.gen.nz>...
>In message <<6tcrd0$34q6$1@news-inn.inet.tele.dk>> "kennet"
<kennet@post11.tele.dk> writes:
>>
>> I've been asking this earlier as a part of a mail. But since noone has
…[5 more quoted lines elided]…
>> we have a large COBOL  (Microfocus 4.0.26) application presently running
in
>> OS/2. We'll be using Win95 soon. So I'd really like to know if you know
>> what's going to happen: We're going to use MF for windows. Will my OS/2
…[4 more quoted lines elided]…
>
```

#### ↳ Re: MF goes windows from OS/2

- **From:** sands@mcmail (David Sands)
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fa32a6.806780@news.mcmail.com>`
- **References:** `<6tcrd0$34q6$1@news-inn.inet.tele.dk>`

```

It all depends on what your applicaiton is doing.

Straight forward COBOL will migrate between environments with no
problems. If your application uses character based ACCEPT/DISPLAY for
it's user interface then again this will move across to Win95 with no
changes.

But...

If your application used low level API calls to OS/2 then you will
have some work to do implementing the equivalent funcitonality on
Win95. If your application uses a GUI then you may have some problems
migrating that to Windows as some PM user interface features are
different in Win95.

You should also consider moving to Net Express which is the latest
Windows COBOL product from MF rather than the classic workbench.

Hope this helps
David.


On Sat, 12 Sep 1998 05:54:24 +0200, "kennet" <kennet@post11.tele.dk>
wrote:

>(MF = Micro Focus).
>
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF goes windows from OS/2

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tdmsu$2n3m$1@news-inn.inet.tele.dk>`
- **References:** `<6tcrd0$34q6$1@news-inn.inet.tele.dk> <35fa32a6.806780@news.mcmail.com>`

```
I only use character based interfaces.
And we do plan to switch to Net Express in a year or so - but I don't really
know this product. Is it simply an update of the workbench?


David Sands skrev i meddelelsen <35fa32a6.806780@news.mcmail.com>...
>
>It all depends on what your applicaiton is doing.
…[29 more quoted lines elided]…
>>we have a large COBOL  (Microfocus 4.0.26) application presently running
in
>>OS/2. We'll be using Win95 soon. So I'd really like to know if you know
>>what's going to happen: We're going to use MF for windows. Will my OS/2
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
