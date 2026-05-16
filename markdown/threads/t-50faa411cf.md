[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem running an ACUBOL v 6.2.0.1 program on AIX 5.2

_3 messages · 3 participants · 2006-08_

---

### Problem running an ACUBOL v 6.2.0.1 program on AIX 5.2

- **From:** "Andres Tarallo" <atarallo@gmail.com>
- **Date:** 2006-08-08T08:30:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1155051019.696304.203390@m79g2000cwm.googlegroups.com>`

```
Hi

I have an application made in  ACUBOL v 6.2.0.1, running on AIX 5.2.
This application takes same files that can be on a local Filesystem or
a remote one, usually exported via NFS or CIFS (Samba on Linux
Servers).

When this application is runned and the files are in a local filesystem
or a filesystem exported via NFS it works fine. However when the files
are in a remopte filesystem exported via CIFS (Samba Server on Linux)
we get an error. We have no problems creating and reading files in the
exported filesystems with shell programs or programs developed by us in
C.

Any idea to debug this problem or solve it is appreciated.

Andres Tarallo
```

#### ↳ Re: Problem running an ACUBOL v 6.2.0.1 program on AIX 5.2

- **From:** sgbojo@gmail.com
- **Date:** 2006-08-08T12:17:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1155064623.268619.164210@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1155051019.696304.203390@m79g2000cwm.googlegroups.com>`
- **References:** `<1155051019.696304.203390@m79g2000cwm.googlegroups.com>`

```
What error are you receiveing and what value have you assigned to the
FILE-PREFIX runtime configuration variable?


Andres Tarallo wrote:
> Hi
>
…[14 more quoted lines elided]…
> Andres Tarallo
```

#### ↳ Re: Problem running an ACUBOL v 6.2.0.1 program on AIX 5.2

- **From:** Lothar Krauss <news5@m2006.lkrauss.de>
- **Date:** 2006-08-09T22:14:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ebdfnk$n83$01$1@news.t-online.com>`
- **References:** `<1155051019.696304.203390@m79g2000cwm.googlegroups.com>`

```
Andres Tarallo wrote:

> Hi
> 
…[14 more quoted lines elided]…
> Andres Tarallo

Are you using sequential files or are you using AcuCobol Vision files? With
Vision files you may have the problem that locking bytes in a file will
produce a problem using the Samba protocol.

Lothar
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
