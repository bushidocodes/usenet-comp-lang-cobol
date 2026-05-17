[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Windows 95 Question

_4 messages · 4 participants · 1998-08_

---

### Windows 95 Question

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-08-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`

```
Good Afternoon,

I know this is not the right place to post this question but i am not sure
where to look for the answer.

Is there anyway to disable the [Ctrl] [Esc] key sequence to prevent bringing up
the "Start Menu / Task Bar" ?


Thanks for any help you can offer,

Bob Hennessey
```

#### ↳ Re: Windows 95 Question

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-08-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd083e97cc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`
- **References:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`

```

Bob7536 wrote in message
<199··.@lad··l.com>...
› Is there anyway to disable the [Ctrl] [Esc] key sequence to prevent
› bringing up
› the "Start Menu / Task Bar" ?


You probably only want to do this when you are in a DOS box running a Cobol
program
that use Ctrl+Esc. If so, right-click on the DOS icon to bring up the
property sheet for Dos. In there is a Misc tab, click that, near the bottom
you UNcheck the
Ctrl+Esc combination.
```

#### ↳ Re: Windows 95 Question

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-08-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd083e97cc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`
- **References:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`

```
In message <<199··.@lad··l.com>> bob··.@a··.com writes:
› 
› I know this is not the right place to post this question but i am not sure
…[3 more quoted lines elided]…
› the  "Start Menu / Task Bar" ?

On a shortcut: right-click, 'Properties', 'Misc', unset Ctrl-Esc
(plus any others), 'OK'.
```

#### ↳ Re: Windows 95 Question

- **From:** "pduboisr..." <ua-author-1265004@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd083e97cc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`
- **References:** `<1998081201064200.VAA26447@ladder01.news.aol.com>`

```
Bob,

I did a search on www.dejanews.com for "disable win95" and found the
following info:

int oldValue;
SystemParametersInfo(SPI_SCREENSAVERRUNNING, TRUE, (PVOID)&oldValue,
0);

The code snippet is C, but you could probably do the call in CoBol.
This is a Kernel call.

The link to the article is:

http://x2.dejanews.com/getdoc.xp?AN=375389338&CONTEXT=903029561.1542848728&hitnum=58

There are also some software programs you can buy that will run in the
background and do the same thing.

Paul


on 12 Aug 1998 01:06:42 GMT, bob··.@a··.com (Bob7536) wrote:

› Good Afternoon,
› 
…[9 more quoted lines elided]…
› Bob Hennessey

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
