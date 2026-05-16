[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Writing Output to Multiple Files

_4 messages · 3 participants · 2001-03_

---

### Re: Writing Output to Multiple Files

- **From:** "L. Bertolini" <bertolini.1@osu.edu>
- **Date:** 2001-03-19T08:21:21-05:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<3AB607D1.A8BF65E0@osu.edu>`
- **References:** `<TTCs6.2983$Im6.408807@newsread1.prod.itd.earthlink.net>`

```
Could you... set up one file in your COBOL program,
and write JCL to it, in "IEBUPDTE" format, i.e.:

./ ADD NAME=MEMBER1
//jobname JOB (acct),'blah blah blah',...
//
./ ADD NAME=MEMBER2
//jobname JOB (acct),'blah blah blah',...
//
./ ENDUP

Then run IEBUPDTE in a subsequent step.

"GER:-)" wrote:
> 
> No, I am not in school anymore...this is a real life problem and because we
…[28 more quoted lines elided]…
> very much...
```

#### ↳ Re: Writing Output to Multiple Files

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-03-19T18:44:43+00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<vsst6.1472$94.2014@www.newsranger.com>`
- **References:** `<TTCs6.2983$Im6.408807@newsread1.prod.itd.earthlink.net> <3AB607D1.A8BF65E0@osu.edu>`

```
Larry,

Looks like you win the prize. That's the easiest way to do it. I should
have thought of that myself, but I haven't used IEBUPDTE in years.

Thanx, Jack.


In article <3AB607D1.A8BF65E0@osu.edu>, L. Bertolini says...
>
>Could you... set up one file in your COBOL program,
…[50 more quoted lines elided]…
>away from the five guys who are undecided." - Casey Stengel
```

##### ↳ ↳ Re: Writing Output to Multiple Files

- **From:** JD <pb@dazoo.com>
- **Date:** 2001-03-19T18:18:52-05:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<3AB693DC.298BE0D5@dazoo.com>`
- **References:** `<TTCs6.2983$Im6.408807@newsread1.prod.itd.earthlink.net> <3AB607D1.A8BF65E0@osu.edu> <vsst6.1472$94.2014@www.newsranger.com>`

```
Seems kind of excessive to me.  What's wrong with using the capabilities of the
COBOL compiler and simply open and close the FD as often as you need to with the
name in the environment variable changed so that COBOL dynamically allocates each
of them?

John H Sleight Jr wrote:

> Larry,
>
…[58 more quoted lines elided]…
> >away from the five guys who are undecided." - Casey Stengel
```

###### ↳ ↳ ↳ Re: Writing Output to Multiple Files

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-03-20T00:05:00+00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<M8xt6.1618$94.2144@www.newsranger.com>`
- **References:** `<TTCs6.2983$Im6.408807@newsread1.prod.itd.earthlink.net> <3AB607D1.A8BF65E0@osu.edu> <vsst6.1472$94.2014@www.newsranger.com> <3AB693DC.298BE0D5@dazoo.com>`

```
JD,

There's nothing wrong with your solution, AAMOF, if you read thru the thread
you'll notice it was already offered as a possible solution. But Lenny,s can be
used with any Cobol compiler.

JS  


In article <3AB693DC.298BE0D5@dazoo.com>, JD says...
>
>Seems kind of excessive to me.  What's wrong with using the capabilities of the
…[67 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
