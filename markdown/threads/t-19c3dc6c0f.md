[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right Justify Routine

_1 message · 1 participant · 1998-09_

---

### Re: Right Justify Routine

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xA%I1.758$I%.3124690@news1.atlantic.net>`
- **References:** `<Jl0PnHJ5PvPd-pn2-XiTbHJiS5z0r@Dwight_Miller.iix.com> <o%VH1.3786$gM3.2803875@news4.mia.bellsouth.net> <trYH1.464$I%.1378959@news1.atlantic.net> <HtbI1.5187$eZ3.3317864@news3.mia.bellsouth.net> <BseI1.481$I%.1861130@news1.atlantic.net> <uCwI1.5340$gM3.3883152@news4.mia.bellsouth.net>`

```
These routines need additional code where indicated.

Judson McClendon wrote in message ...
>Since we're starting to really get into the optimization thing, let's
[...]
>
>       test3-start-Judson.
…[6 more quoted lines elided]…
>                   into output-field with pointer counter
==>      else
==>          move spaces to output-field
>           end-if
>           .
>
[...]
>       test3-start-jud-coded.
>           move "abcdefghijklm" to input-field
…[10 more quoted lines elided]…
>               end-if
==>      else
==>          move spaces to output-field
>           end-if
>           .

There is no difference in performance.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
