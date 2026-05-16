[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microsoft XML-parser

_7 messages · 4 participants · 2001-08_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Microsoft XML-parser

- **From:** "Tommy Nilsen" <nilse-to@online.no>
- **Date:** 2001-08-05T20:57:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no>`

```
Anyone have any experience in using MSXML3 ??

Tommy Nilsen
```

#### ↳ Re: Microsoft XML-parser

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-08-09T02:43:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ktgnm01ql5@enews1.newsguy.com>`
- **References:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no>`

```
I've used it--but that's about it--what do you want to know?

"Tommy Nilsen" <nilse-to@online.no> wrote in message
news:2Ggb7.4062$e%4.119202@news3.oke.nextra.no...
> Anyone have any experience in using MSXML3 ??
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Microsoft XML-parser

- **From:** "Tommy Nilsen" <nilse-to@online.no>
- **Date:** 2001-08-10T00:02:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BKDc7.829$fT5.13200@news1.oke.nextra.no>`
- **References:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no> <9ktgnm01ql5@enews1.newsguy.com>`

```
I was just wondering if you had any problems when finalizing xml-objects ??

To me it seems that even though I finalize the xml-objects , resources are
not always released.

Have you experienced the same ??

I've written a service that call's a com-object and receives some
xml-objects.

The service makes this call every second, so it is very important that
resources are beeing released...

Tommy


"Grinder" <grinder@no.spam.maam.com> wrote in message
news:9ktgnm01ql5@enews1.newsguy.com...
> I've used it--but that's about it--what do you want to know?
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Microsoft XML-parser

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-08-09T18:47:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9kv7fr063e@enews2.newsguy.com>`
- **References:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no> <9ktgnm01ql5@enews1.newsguy.com> <BKDc7.829$fT5.13200@news1.oke.nextra.no>`

```

"Tommy Nilsen" <nilse-to@online.no> wrote in message
news:BKDc7.829$fT5.13200@news1.oke.nextra.no...
> I was just wondering if you had any problems when finalizing
xml-objects ??
>
> To me it seems that even though I finalize the xml-objects ,
resources are
> not always released.

In what time-frame?  COM does some trash collection, but it
doesn't always come off when you release the object.
```

###### ↳ ↳ ↳ Re: Microsoft XML-parser

_(reply depth: 4)_

- **From:** "Tommy Nilsen" <tommy.nilsen@hands.no>
- **Date:** 2001-08-10T12:55:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l0eju$1u6v$1@news.dataguard.no>`
- **References:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no> <9ktgnm01ql5@enews1.newsguy.com> <BKDc7.829$fT5.13200@news1.oke.nextra.no> <9kv7fr063e@enews2.newsguy.com>`

```
If I let the service run over night, the Memory Usage(reported by Windows
Task Manager) can increase from 4MB to 300 MB , depending on how much data
is transferred !!

I have made a temporarily solution.The service calls a subprogram
(exe-program) that do all the transferring of data.

This seems to work fine...

Tommy

"Grinder" <grinder@no.spam.maam.com> wrote in message
news:9kv7fr063e@enews2.newsguy.com...
>
> "Tommy Nilsen" <nilse-to@online.no> wrote in message
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Microsoft XML-parser

_(reply depth: 5)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-08-10T20:02:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l20a90f3h@enews3.newsguy.com>`
- **References:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no> <9ktgnm01ql5@enews1.newsguy.com> <BKDc7.829$fT5.13200@news1.oke.nextra.no> <9kv7fr063e@enews2.newsguy.com> <9l0eju$1u6v$1@news.dataguard.no>`

```
I'll point out that I'm flailing--I'm not familiar with your
environment.

What objects are you using?  Some things have to be explicitly
cleaned up.  If you've moved it to a subordinate EXE, leaks may
be recovered when the entire process ends--that could explain
the difference you're seeing.

"Tommy Nilsen" <tommy.nilsen@hands.no> wrote in message
news:9l0eju$1u6v$1@news.dataguard.no...
> If I let the service run over night, the Memory Usage(reported
by Windows
> Task Manager) can increase from 4MB to 300 MB , depending on
how much data
> is transferred !!
>
> I have made a temporarily solution.The service calls a
subprogram
> (exe-program) that do all the transferring of data.
>
…[9 more quoted lines elided]…
> > > I was just wondering if you had any problems when
finalizing
> > xml-objects ??
> > >
> > > To me it seems that even though I finalize the xml-objects
,
> > resources are
> > > not always released.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Microsoft XML-parser

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-08-10T01:09:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YuGc7.4641$NJ6.22008@www.newsranger.com>`
- **References:** `<2Ggb7.4062$e%4.119202@news3.oke.nextra.no> <9ktgnm01ql5@enews1.newsguy.com> <BKDc7.829$fT5.13200@news1.oke.nextra.no>`

```
Some COM objects require you to explicitly release the resources.  It appears
you are doing so.  Since this object is almost certainly C++ - there's no
garbage collection to clean up.  I have not looked at this particular com object
in detail -- yet.  It's possible that some resources allocated are reused
instead of being released.  I'm afraid experimentation is the only way to find
out, if it's not documented in the MS documentation.

In article <BKDc7.829$fT5.13200@news1.oke.nextra.no>, Tommy Nilsen says...
>
>I was just wondering if you had any problems when finalizing xml-objects ??
…[30 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
