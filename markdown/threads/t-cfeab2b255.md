[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DOS Cobol (dongle) under NT

_3 messages · 3 participants · 1995-11 → 1995-12_

---

### DOS Cobol (dongle) under NT

- **From:** "kpr..." <ua-author-17086774@usenetarchives.gap>
- **Date:** 1995-11-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<30be9201.282479@news.solo.pipex.co.za>`

```
Hi

Has anyone tried using Microfocus Cobol 3.2.31 for DOS (dongle
version) under Windows NT.

NT does not like it. How does one get around the problem of NT not
letting software talk directly to the hardware.

Thanx
Keith
```

#### ↳ Re: DOS Cobol (dongle) under NT

- **From:** "dan yates" <ua-author-17086085@usenetarchives.gap>
- **Date:** 1995-12-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfeab2b255-p2@usenetarchives.gap>`
- **In-Reply-To:** `<30be9201.282479@news.solo.pipex.co.za>`
- **References:** `<30be9201.282479@news.solo.pipex.co.za>`

```
NT does not allow software to communicate directly with the
hardware. This is the responsibility of the Hardware
Abstraction Layer (HAL) subsystem. It is this subsystem that
allows NT to run on multiple platforms. It should be the
vendors responsibilty to supply the needed HAL subsystem
software modules needed by their hardware/software.

Dan Yates
MSS III
U of I @ Springfield
```

##### ↳ ↳ Re: DOS Cobol (dongle) under NT

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-12-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfeab2b255-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cfeab2b255-p2@usenetarchives.gap>`
- **References:** `<30be9201.282479@news.solo.pipex.co.za> <gap-cfeab2b255-p2@usenetarchives.gap>`

```
Is the command for HAL "Open the pod bay door HAL?".

Whoops, probably won't work too well...

Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
