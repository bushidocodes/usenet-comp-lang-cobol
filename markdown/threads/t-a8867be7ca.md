[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Win95 network errors with MF ver2.5

_5 messages · 5 participants · 1998-02_

---

### Win95 network errors with MF ver2.5

- **From:** "kevin karch" <ua-author-17075447@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net>`

```

Does anyone know why I might be getting file status error 209 (Network
communication error) using MF ver 2.5 multi-user DOS app under windows 95??
Sometimes it recognizes the file locks and sometimes I get the 209.
Any help would be appreciated.
```

#### ↳ Re: Win95 network errors with MF ver2.5

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8867be7ca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net>`
- **References:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net>`

```


Kevin Karch wrote in message <01bd30e0$dfccf240$Loc··.@LIH··b.net>...
› Does anyone know why I might be getting file status error 209 (Network
› communication error) using MF ver 2.5 multi-user DOS app under windows 95??
› Sometimes it recognizes the file locks and sometimes I get the 209.
› Any help would be appreciated.

I hope you know how old Version 2.5 is. I am certain that it was never
tested with Windows95. I won't even swear to it being tested with Windows
3.1. This doesn't mean that what you are trying won't work - but I sure
would consider it pure luck if it does.
```

##### ↳ ↳ Re: Win95 network errors with MF ver2.5

- **From:** "edw" <ua-author-7163589@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8867be7ca-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8867be7ca-p2@usenetarchives.gap>`
- **References:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net> <gap-a8867be7ca-p2@usenetarchives.gap>`

```

We get the same problem now and again using version 3.2 on OS/2, NT4 and
95, so I don't think its the age of your compiler, a DOS box is a DOS box,
after all. I think you'll find the 209 is a momentary network glich; I
tell my lovely users to try again and it always goes away. If you are
getting this more often than now and again, I reckon you've got a
distinctly dodgy network.

William M. Klein wrote in article
<6b81d9$3.··.@dfw··m.com>...
› 
› Kevin Karch wrote in message <01bd30e0$dfccf240$Loc··.@LIH··b.net>...
…[14 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Win95 network errors with MF ver2.5

- **From:** "spm-c..." <ua-author-16631837@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8867be7ca-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8867be7ca-p3@usenetarchives.gap>`
- **References:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net> <gap-a8867be7ca-p2@usenetarchives.gap> <gap-a8867be7ca-p3@usenetarchives.gap>`

```

In article <01bd318b$17d78f60$3a4e80c1@loanstt>, "edw" wrote:
› We get the same problem now and again using version 3.2 on OS/2, NT4 and
› 95, so I don't think its the age of your compiler, a DOS box is a DOS box,
…[23 more quoted lines elided]…
›› 
Sorry William, as far I know, you will get error 209's (network error) instead
of the usual error 65 (record locked) on a locked record under Win95 DOS boxes
until you upgrade your compiler to version 3.2.50... If your lovely users are
successful on a later run, I submit that the record in question is no longer
locked when the user re-runs the program.

I had the same problem with the 209 errors when I upgraded some of my users
PC's to Win 95 from Win 3.1. The server, wiring, hubs, NIC's all were
untouched during this time. The 209s starting showing back up as
65's after I upgraded to 3.2.50.

Chuck McGavern
```

#### ↳ Re: Win95 network errors with MF ver2.5

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-02-04T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8867be7ca-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net>`
- **References:** `<01bd30e0$dfccf240$LocalHost@LIHQ.pb.net>`

```

On 3 Feb 1998 20:23:36 GMT, "Kevin Karch"
wrote:

› Does anyone know why I might be getting file status error 209 (Network
› communication error) using MF ver 2.5 multi-user DOS app under windows 95??
› Sometimes it recognizes the file locks and sometimes I get the 209.
› Any help would be appreciated.

Yes!

You are accessing a NOVELL network, using the native Novell drivers
that came with Windows 95. Go to the Novell web site and download the
"Client 32" drivers and your problems will go away.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
