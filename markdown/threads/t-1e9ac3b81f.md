[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Style (was: Sets and subsets

_1 message · 1 participant · 2003-04_

---

### Re: Style (was: Sets and subsets

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-28T12:58:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8jq3q$9bt$1@slb1.atl.mindspring.net>`
- **References:** `<b7tepn$9tb$1@slb9.atl.mindspring.net> <3EA55E79.6090702@newsguy.com> <3ea5ed65.19257366@news.optonline.net> <3EA69C04.7090208@newsguy.com> <3ea88130.21326254@news.optonline.net> <b8ab71$1dv$1@aklobs.kc.net.nz> <3eaaa1e8.160795747@news.optonline.net> <b8h8s8$c6r$1@slb9.atl.mindspring.net> <3eac5f18.274780521@news.optonline.net> <217e491a.0304272216.24c66f64@posting.google.com> <3ead12ba.320773761@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ead12ba.320773761@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
> >robert@wagner.net (Robert Wagner) wrote
> >
<snip>.
>
> >Arguing for DISPLAY format in Cobol indexed files misses the point
> >entirely.
>
> Actually, I thought we were talking about sequential files. WMK called
them
> "output files", which usually means sequential.
>

Please be aware that when I use the term "output file" - I mean *any* COBOL
file that was created (or updated) via an
   OPEN OUTPUT
        or even
   OPEN I-O

statement - so it may be sequential (line or record where such things are
available), indexed or relative.  I wouldn't have thought that this would
have been an "ambiguous" term in a COBOL context, but if it is, then please
accept this clarification.

Furthermore, OPEN I-O files are rarely (but not quite never) ORGANIZATION
SEQUENTIAL; OPEN OUTPUT files are often - but I would hesitate to state (as
above) "usually" ORGANIZATION <line/record> SEQUENTIAL.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
