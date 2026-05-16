[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Runtime Messages

_3 messages · 3 participants · 2000-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Runtime Messages

- **From:** "Joe Hunter" <pcs@usaor.net>
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<smboh1g1nu7@corp.supernews.com>`

```
How do I suppress the runtime messages in Fujitsu 5.0.  If I received a
FILE-STATUS 46 error,  Fujitsu's runtime message pops up.

I currently have @NoMessage=YES in the runtime environment file.

Thanks in advance.

Joe Hunter
pcs@usaor.net
```

#### ↳ Re: Fujitsu Runtime Messages

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39666304.72688266@207.126.101.100>`
- **References:** `<smboh1g1nu7@corp.supernews.com>`

```
On Fri, 7 Jul 2000 10:03:50 -0400, "Joe Hunter" <pcs@usaor.net> wrote:

>How do I suppress the runtime messages in Fujitsu 5.0.  If I received a
>FILE-STATUS 46 error,  Fujitsu's runtime message pops up.
>
>I currently have @NoMessage=YES in the runtime environment file.
>

@NoMessage=YES works for me.  (Reminds me of the error message: A file
which does not exist was found.).

What I HAVE found is that this suppression does NOT exist if you are
debugging.  I'll have to check further to make sure it really is
working for me, but I'm 99.9% sure it is.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Fujitsu Runtime Messages

- **From:** Hajo Schepker <schepker@fbw.fh-wilhelmshaven.de>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000710.6184593@Wpc8.fbw.fh-wilhelmshaven.de>`
- **References:** `<smboh1g1nu7@corp.supernews.com>`

```
Hi,

you must have a declaratives Section, then the pop-up-windows does not 
appear.

Mit freundlichen Grüßen
H. Schepker 
www.schepker.de


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 07.07.00, 16:03:50, schrieb "Joe Hunter" <pcs@usaor.net> zum Thema 
Fujitsu Runtime Messages:


> How do I suppress the runtime messages in Fujitsu 5.0.  If I received a
> FILE-STATUS 46 error,  Fujitsu's runtime message pops up.

> I currently have @NoMessage=YES in the runtime environment file.

> Thanks in advance.

> Joe Hunter
> pcs@usaor.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
