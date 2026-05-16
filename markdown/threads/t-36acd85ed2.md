[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# internal v. external sort-> which do you like?

_1 message · 1 participant · 1999-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### RE: internal v. external sort-> which do you like?

- **From:** Peter van Zeeland <peter.van.zeeland@cmg.nl>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6DE2D20B5851D2119BB300A0C9DAF69851314E@NL-AMB-MAIL01>`

```
I second the idea of using index files. I use it a lot. When using the
logic:

form the key
read temporary file
invalid
   create record for this key
not invalid
   add current value to it
    rewrite record for this key
end read

it dismisses you from writing at least the lowest level in the level breaks
for the output processing.
It may not be as efficient, but there are two huge advantages:
(1) it is extremely easy to write
(2) you yourself are in control. Not some implementation/environment-defined
behind-the-screens probably-optimized misterious routine that is called
'internal sort' or 'external sort'. Especially the latter gives you no
indication of progress whatsoever.


> -----Original Message-----
> From:	James J. Gavan [SMTP:jjgavan@home.com]
…[52 more quoted lines elided]…
>  http://www.deja.com/thread/%3C37F048E4.F2D31CDF%40home.com%3E


 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
