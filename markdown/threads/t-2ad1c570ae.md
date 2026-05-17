[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF duplicates barrier.

_6 messages · 5 participants · 1998-05_

---

### MF duplicates barrier.

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-05-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jeqpf$oon$1@fep5.clear.net.nz>`

```

Windows Compiler Experts,
Ms COBOL vs5.0 (MF COBOL vs3.0.60) has a limit on duplicate keys of 64,000.
But I need say 512,000 to safely allow say 400,000 records in a file (say
180Mb on a Server).
I have to quote capability to clients considering purchase.
[I have been advised that MF COBOL 3.2.50 is the reliable 16bit Compiler for
win.]
Can anybody quote me an MF COBOL version that could handle this?
Thankyou in advance.
```

#### ↳ Re: MF duplicates barrier.

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ad1c570ae-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6jeqpf$oon$1@fep5.clear.net.nz>`
- **References:** `<6jeqpf$oon$1@fep5.clear.net.nz>`

```

David,

Fujitsu COBOL provides full support for MS COBOL V5 and has no real
restriction on the number of duplicate keys. You can still get the FREE
unrestricted Fujitsu COBOL Starter Set at www.adtools.com

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


David Mowat wrote in message <6jeqpf$oon$1.··.@fep··t.nz>...
› Windows Compiler Experts,
› Ms COBOL vs5.0 (MF COBOL vs3.0.60) has a limit on duplicate keys of 64,000.
…[18 more quoted lines elided]…
›
```

#### ↳ Re: MF duplicates barrier.

- **From:** "kenmu..." <ua-author-17072514@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ad1c570ae-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6jeqpf$oon$1@fep5.clear.net.nz>`
- **References:** `<6jeqpf$oon$1@fep5.clear.net.nz>`

```

› Subject: MF duplicates
› barrier.
…[26 more quoted lines elided]…
› 

My NetExpress help file indicates that there can be 4,294,967,297 duplicate
keys if you use the IdxFormat "4" (compiler directive)...It also states that
this format is for better processing of duplicate keys...

Ken Mullins
Atlanta, GA
```

#### ↳ Re: MF duplicates barrier.

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ad1c570ae-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6jeqpf$oon$1@fep5.clear.net.nz>`
- **References:** `<6jeqpf$oon$1@fep5.clear.net.nz>`

```

In message <<6jeqpf$oon$1.··.@fep··t.nz>> "David Mowat" writes:
› Ms COBOL vs5.0 (MF COBOL vs3.0.60) has a limit on duplicate keys of 64,000.
› But I need say 512,000 to safely allow say 400,000 records in a file (say
…[3 more quoted lines elided]…
› win.]

Why on earth would you ever want duplicate alternate keys in any
case. If all your records had the same key value then there
would be no point at all in having the key at all. It would
be easy enough to add some distinct value to avoid duplication
at all, and this may be beneficial in any case. For example
adding a date/time value will ensure all records with the same
leading part to the key are ordered. Often a descending
date/time may be useful as it obtains the latest record
first.

Now there is a case that says that records may have an
empty field used as alternate where a value here indicates
something interesting, and most records are not interesting.
But it is only necessary to arange a different set of values
(such as numeric date/time) to indicate uninteresting and
alphabetic to indicate interesting (such as requiring
some form of processing).
```

#### ↳ Re: MF duplicates barrier.

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ad1c570ae-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6jeqpf$oon$1@fep5.clear.net.nz>`
- **References:** `<6jeqpf$oon$1@fep5.clear.net.nz>`

```

David,

You are correct when you say that the default limit for duplicate keys
in our 16 bit product is 64,000. However, you can define the file with
an IDXFORMAT"4" which allows you to go beyond this limit.

I cannot confirm that this feature is in MS COBOL 5.0 (I do not have
access to any documentation). However, if you look for the IDXFORMAT
compiler directive in your manuals this should confirm its presence.

As for later 16 bit compilers. The 3.2 product is no longer available and
has been replaced by version 3.4.23.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

David Mowat wrote in message <6jeqpf$oon$1.··.@fep··t.nz>...
› Windows Compiler Experts,
› Ms COBOL vs5.0 (MF COBOL vs3.0.60) has a limit on duplicate keys of 64,000.
…[18 more quoted lines elided]…
›
```

#### ↳ Re: MF duplicates barrier.

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ad1c570ae-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6jeqpf$oon$1@fep5.clear.net.nz>`
- **References:** `<6jeqpf$oon$1@fep5.clear.net.nz>`

```

David,

You are correct when you say that the default limit for duplicate keys
in our 16 bit product is 64,000. However, you can define the file with
an IDXFORMAT"4" which allows you to go beyond this limit.

I cannot confirm that this feature is in MS COBOL 5.0 (I do not have
access to any documentation). However, if you look for the IDXFORMAT
compiler directive in your manuals this should confirm its presence.

As for later 16 bit compilers. The 3.2 product is no longer available and
has been replaced by version 3.4.23.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

David Mowat wrote in message <6jeqpf$oon$1.··.@fep··t.nz>...
› Windows Compiler Experts,
› Ms COBOL vs5.0 (MF COBOL vs3.0.60) has a limit on duplicate keys of 64,000.
…[18 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
