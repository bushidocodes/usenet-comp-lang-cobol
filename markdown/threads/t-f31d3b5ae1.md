[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A question for OO people

_5 messages · 3 participants · 2000-05_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### A question for OO people

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8emncb$pls$1@newssrv.otenet.gr>`

```
Hi to all,

About 2 weeks ago i posted a question with that title. My intention was NOT
to learn about new tools such as SP2. The initial question was .....

Is there a way to  keep 'alive' my objects (using oocobol) between
different invocations of the server-side program ? A clever approach, posted
by Frog, is to built the program as ISAPI or NSAPI - wich means .DLL - so
the working-storage will not be initialized every time the client sends a
request to the server. I am still working on it.

I am using NetExpress.

Thanx for your ideas
```

#### ↳ Re: A question for OO people

- **From:** "The COBOL Frog" <H.Klink@IMN.NotThisPart.nl>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fe8ql$3uv$1@porthos.nl.uu.net>`
- **References:** `<8emncb$pls$1@newssrv.otenet.gr>`

```
After you have re-asked this question twice now, it seems that only The Grog had a reasonable solution? :))
```

##### ↳ ↳ Re: A question for OO people

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fej38$21h$1@newssrv.otenet.gr>`
- **References:** `<8emncb$pls$1@newssrv.otenet.gr> <8fe8ql$3uv$1@porthos.nl.uu.net>`

```

Unforunately i had no other feedback. But more unfortunately the results
from my experiments are not so good. When the client posted the request for
the first time everything was fine. Then the client sent the second request
and - to my surprise - the objects i created from the first run, were still
there and active ! Then i thought 'Grog is #1'. I was preparing to send you
a present :) But... after some repeated calls, the behavior of the server
program is unpredictable. It produces RT errors, it goes directly to the
last section etc. I tried only with ISAPI. I 'll make a last effort with
NSAPI and then... well, i have no idea ....

Thanks again
Costas


The COBOL Frog <H.Klink@IMN.NotThisPart.nl> wrote in message
news:8fe8ql$3uv$1@porthos.nl.uu.net...
After you have re-asked this question twice now, it seems that only The Grog
had a reasonable solution? :))


Costas Giannoulis <diavasi@otenet.gr> wrote in message
news:8emncb$pls$1@newssrv.otenet.gr...
> Hi to all,
>
> About 2 weeks ago i posted a question with that title. My intention was
NOT
> to learn about new tools such as SP2. The initial question was .....
>
> Is there a way to  keep 'alive' my objects (using oocobol) between
> different invocations of the server-side program ? A clever approach,
posted
> by Frog, is to built the program as ISAPI or NSAPI - wich means .DLL - so
> the working-storage will not be initialized every time the client sends a
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A question for OO people

- **From:** "The COBOL Frog" <H.Klink@IMN.NotThisPart.nl>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fgrci$gsm$1@porthos.nl.uu.net>`
- **References:** `<8emncb$pls$1@newssrv.otenet.gr> <8fe8ql$3uv$1@porthos.nl.uu.net> <8fej38$21h$1@newssrv.otenet.gr>`

```
Ai ai Ai.

It seems that I was ... a bit groggy calling myself grog i.s.o. FFFFFFFrog.

My observation: It's a pity, bu I think that under ISAPI or NSAPI the DLL's are loaded and stay in memory for a while. At some point the delay between two requests is just too long or the server reclaims memory for some other reason and the DLL, including allocated objects, is freed from memory. Upon the next request the DLL is reloaded, thinking the objects still exist, but ... booooooom.

This is probably your scenario now.

I now get convinced that you need to write your objects to persistent media (file, MF_STATE routine etc.) and re-instantiate them upon re-activation. Some more work for you, but it can be done.

Perhaps some quicker solution can be reached. Just check out the URL that, if my memory serves me well, Thane sent me:
<QUOTE> Frog, check out the LRWP protocol for Xitami at http://imatix.com/html/xitami/index12.htm </QUOTE>

Good luck,

The Frog (not grog) :)

"Costas Giannoulis" <diavasi@otenet.gr> wrote in message news:8fej38$21h$1@newssrv.otenet.gr...
> 
> Unforunately i had no other feedback. But more unfortunately the results
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A question for OO people

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391c730b.65223698@news.cox-internet.com>`
- **References:** `<8emncb$pls$1@newssrv.otenet.gr> <8fe8ql$3uv$1@porthos.nl.uu.net> <8fej38$21h$1@newssrv.otenet.gr> <8fgrci$gsm$1@porthos.nl.uu.net>`

```
On Fri, 12 May 2000 13:50:13 +0200, "The COBOL Frog"
<H.Klink@IMN.NotThisPart.nl> wrote:

>Perhaps some quicker solution can be reached. Just check out the URL =
>that, if my memory serves me well, Thane sent me:
><QUOTE> Frog, check out the LRWP protocol for Xitami at =
>http://imatix.com/html/xitami/index12.htm </QUOTE>
>

Not me, but thanks for thinking of me anyway <G>.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
