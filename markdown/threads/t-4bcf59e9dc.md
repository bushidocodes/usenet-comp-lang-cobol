[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [kernel32] could not find the calling program

_3 messages · 2 participants · 2002-06_

---

### [kernel32] could not find the calling program

- **From:** "R. Hendriks" <R.Hendriks_1@kub.nl>
- **Date:** 2002-06-25T16:15:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af9trp$jjc$1@mailnews.kub.nl>`

```
I'm (still) trying to make a working api call. The compiler and linker make
the files required without any error, but when running the .dll file that is
made the kernel32.dll report [could not find the calling program]. Where
should I look for an answer/solution to the message?

Rik Hendriks
```

#### ↳ Re: [kernel32] could not find the calling program

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-06-25T21:19:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s75S8.437940$Oa1.30879489@bin8.nnrp.aus1.giganews.com>`
- **References:** `<af9trp$jjc$1@mailnews.kub.nl>`

```

"R. Hendriks" <R.Hendriks_1@kub.nl> wrote in message
news:af9trp$jjc$1@mailnews.kub.nl...
> I'm (still) trying to make a working api call. The compiler and linker
make
> the files required without any error, but when running the .dll file that
is
> made the kernel32.dll report [could not find the calling program]. Where
> should I look for an answer/solution to the message?
>
> Rik Hendriks

Look here by posting the code.

The most common error is that API calls are case sensitive. If you're not
careful, COBOL will fold lower case to upper before calling.
```

##### ↳ ↳ Re: [kernel32] could not find the calling program

- **From:** "R. Hendriks" <R.Hendriks_1@kub.nl>
- **Date:** 2002-06-26T11:01:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afbvr8$co5$1@mailnews.kub.nl>`
- **References:** `<af9trp$jjc$1@mailnews.kub.nl> <s75S8.437940$Oa1.30879489@bin8.nnrp.aus1.giganews.com>`

```
Jerry,

I've already fixed it, but thanx for the reply.

Rik Hendriks

"JerryMouse" <nospam@bisusa.com> wrote in message
news:s75S8.437940$Oa1.30879489@bin8.nnrp.aus1.giganews.com...
>
> "R. Hendriks" <R.Hendriks_1@kub.nl> wrote in message
…[3 more quoted lines elided]…
> > the files required without any error, but when running the .dll file
that
> is
> > made the kernel32.dll report [could not find the calling program]. Where
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
