[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM-Cobol & CD-Rom

_2 messages · 2 participants · 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM-Cobol & CD-Rom

- **From:** "leo.v..." <ua-author-17071581@usenetarchives.gap>
- **Date:** 1997-01-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32e510d4.942485@news.tip.nl>`

```


I have put some RM-Cobol data file on a CD-ROM. When I try to access
those files I get an error-code 3022.
What I've found out is that RM-COBOL (in a multiuser system) tries to
update the header of the file you are trying to access.
I've tried everything I could think of: different ACCESS modes,
EXCLUSIVE OPENS etc.

If somebody knows of an answer (a patch/or runtime command parameter)
please let me know!

The system is an IBM-RS6000-AIX system, the RM-COBOL version is
V6.00.
```

#### ↳ Re: RM-Cobol & CD-Rom

- **From:** "uwe baemayr" <ua-author-6588910@usenetarchives.gap>
- **Date:** 1997-01-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b28ba7cb72-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32e510d4.942485@news.tip.nl>`
- **References:** `<32e510d4.942485@news.tip.nl>`

```

Leo Veenstra wrote:

› I have put some RM-Cobol data file on a CD-ROM. When I try to access
› those files I get an error-code 3022.
…[3 more quoted lines elided]…
› EXCLUSIVE OPENS etc.

This is a known problem, and is scheduled to be fixed in the upcoming
6.5 release.

-----------------------------------------------------------------------------
| Uwe Baemayr | u.··.@li··t.com / jea··.@ccw··s.edu |
| Ryan McFarland Corporation | http://www.liant.com |
| a division of Liant Software | Compuserve: 74774,47 / GO LIANT |
-----------------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
