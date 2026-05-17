[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL making program sleep

_7 messages · 7 participants · 1998-05_

---

### COBOL making program sleep

- **From:** "mike krueger" <ua-author-1374644@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<356f2348.0@news1.ibm.net>`

```

Hello
Is there a COBOL verb that causes the program to sleep for a period of time;
i.e.. do something, then stop for a configurable amount of time, do
something then stop for configurable amount of time...
```

#### ↳ Re: COBOL making program sleep

- **From:** "andrew j. jackson" <ua-author-6589078@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afbcefbb63-p2@usenetarchives.gap>`
- **In-Reply-To:** `<356f2348.0@news1.ibm.net>`
- **References:** `<356f2348.0@news1.ibm.net>`

```

Mike Krueger wrote:

› Hello
› Is there a COBOL verb that causes the program to sleep for a period of
› time;
› i.e.. do something, then stop for a configurable amount of time, do
› something then  stop for configurable amount of time...

As far as I know there is none; CICS does have that capability.

Richard Jackson
Houston
```

#### ↳ Re: COBOL making program sleep

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-05-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afbcefbb63-p3@usenetarchives.gap>`
- **In-Reply-To:** `<356f2348.0@news1.ibm.net>`
- **References:** `<356f2348.0@news1.ibm.net>`

```

There is no standard COBOL verb to do this - but many compilers (natively or
via the operating system) provide such a capability.

What compiler are you using on what operating system - and we can reply more
specifically.
```

#### ↳ Re: COBOL making program sleep

- **From:** "albert ratzlaff" <ua-author-6589172@usenetarchives.gap>
- **Date:** 1998-05-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afbcefbb63-p4@usenetarchives.gap>`
- **In-Reply-To:** `<356f2348.0@news1.ibm.net>`
- **References:** `<356f2348.0@news1.ibm.net>`

```



Mike Krueger escribiÃ³:

› Hello
› Is there a COBOL verb that causes the program to sleep for a period of time;
› i.e.. do something, then stop for a configurable amount of time, do
› something then  stop for configurable amount of time...

RM/COBOL 85 (versiones 5.3 and up) has a timeout feature with ACCEPT that could
possibly be used for this.

Regards
Albert Ratzlaff
```

#### ↳ Re: COBOL making program sleep

- **From:** "ginseng jones" <ua-author-6589137@usenetarchives.gap>
- **Date:** 1998-05-29T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afbcefbb63-p5@usenetarchives.gap>`
- **In-Reply-To:** `<356f2348.0@news1.ibm.net>`
- **References:** `<356f2348.0@news1.ibm.net>`

```

If you're running on MVS environment, there should be a utility program you
can call to accomplish this task.

› Hello
› Is there a COBOL verb that causes the program to sleep for a period of
› time;
› i.e.. do something, then stop for a configurable amount of time, do
› something then  stop for configurable amount of time...
```

#### ↳ Re: COBOL making program sleep

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-05-29T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afbcefbb63-p6@usenetarchives.gap>`
- **In-Reply-To:** `<356f2348.0@news1.ibm.net>`
- **References:** `<356f2348.0@news1.ibm.net>`

```

Mike,

Windows 95/NT has an API called SleepEX which allows an EXE to go into sleep
mode for a specified period of time. For more information se the CBLEXEC
sample at:
http://www.adtools.com/support/samples.htm

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


Mike Krueger wrote in message <356··.@new··m.net>...
› Hello
› Is there a COBOL verb that causes the program to sleep for a period of
…[4 more quoted lines elided]…
›
```

##### ↳ ↳ Re: COBOL making program sleep

- **From:** "m.cr..." <ua-author-12785883@usenetarchives.gap>
- **Date:** 1998-05-31T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-afbcefbb63-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-afbcefbb63-p6@usenetarchives.gap>`
- **References:** `<356f2348.0@news1.ibm.net> <gap-afbcefbb63-p6@usenetarchives.gap>`

```

If you're running under unix you can call the kernal system call
sleep.

Something like...

01 sleep-seconds pic 9(9) comp value 10;

* This should sleep for 10 seconds.

call "sleep" using by-value sleep-seconds.



› Mike Krueger wrote in message <356··.@new··m.net>...
›› Hello
…[5 more quoted lines elided]…
››
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
