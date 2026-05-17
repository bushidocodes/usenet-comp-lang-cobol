[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Cobol problem

_3 messages · 3 participants · 1997-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Cobol problem

- **From:** "elo simonsen" <ua-author-17073105@usenetarchives.gap>
- **Date:** 1997-02-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33032922.677A@csc.dk>`

```

After installing the fujitsu's free cobol in my Windows 95 I'm
constantly getting this message-popup when starting windows 95:
REMIND: Invalide schedule file

drive:\fsc\regsoft\remind.sch

It seems being a reminder to register the software, what I've been doing
(or at least tried to) during the installation.
But the file above does'nt exist, so how can I avoid this ?

Elo Simonsen :(
```

#### ↳ Re: Fujitsu Cobol problem

- **From:** "co..." <ua-author-6588778@usenetarchives.gap>
- **Date:** 1997-02-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aebe8cc153-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33032922.677A@csc.dk>`
- **References:** `<33032922.677A@csc.dk>`

```

It is easy to fix this error by editing your win.ini file. Remove the
line that points to this file (REMIND.SCH) and you will have no
further problems. It is usually about the 4th or 5th line in the
program. Whenever you edit your win.ini file, it is always smart to
make a backup first.

If you are using NT take a look at our bulletin board:
http://www.adtools.com/wwwboard/cobol/

Thanks,

Fujitsu Software


Elo Simonsen wrote:

› After installing the fujitsu's free cobol in my Windows 95 I'm
› constantly getting this message-popup when starting windows 95:	
› REMIND: Invalide schedule file
 
› drive:\fsc\regsoft\remind.sch
 
› It seems being a reminder to register the software, what I've been doing
› (or at least tried to) during the installation.
› But the file above does'nt exist, so how can I avoid this ?
 
› Elo Simonsen :(

Fujitsu Software Corporation
http://www.adtools.com
Tel (800) 545-6774
Fax (408) 428-0600
```

#### ↳ Re: Fujitsu Cobol problem

- **From:** "kindrick ownby" <ua-author-1089339@usenetarchives.gap>
- **Date:** 1997-02-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aebe8cc153-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33032922.677A@csc.dk>`
- **References:** `<33032922.677A@csc.dk>`

```

Elo Simonsen wrote:
› 
› After installing the fujitsu's free cobol in my Windows 95 I'm
…[3 more quoted lines elided]…
›         drive:\fsc\regsoft\remind.sch

The following came directly from Fujitsu when I had the same problem:

As for the remind.sch problem, if you look in your WIN.ini file about the
4th line will have a path that points to the REMIND.SCH or REMIND.EXE.
Delete that entire line and you should have no further problems.

Kindrick
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
