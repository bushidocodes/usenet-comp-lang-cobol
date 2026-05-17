[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to find a field in an FD?

_2 messages · 2 participants · 1994-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### How to find a field in an FD?

- **From:** "ab..." <ua-author-1994472@usenetarchives.gap>
- **Date:** 1994-11-23T02:09:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-gtHtewiKQe0@usenetarchives.gap>`

```

I manually calculate the position of a field in an fd (file description).
Is there a routine in COBOL which computes it for me and that handles
'occurs' in the file description.
```

#### ↳ Re: How to find a field in an FD?

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1994-11-23T12:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e0d8b8de17-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-gtHtewiKQe0@usenetarchives.gap>`
- **References:** `<ua-fallback-gtHtewiKQe0@usenetarchives.gap>`

```
In article Abdel-Hadi Bukres,
ab··.@ago··p.com writes:
›
› I manually calculate the position of a field in an fd (file description).
› Is there a routine in COBOL which computes it for me and that handles
› 'occurs' in the file description.
›
You are not clear as to whether you want to do this while the program
is running or have something read the source and tell you the offset.
Every compiler I know of tells you the latter if you request it. For
a dynamic offset, you could use the intrinsic function LENGTH to add
up the stuff in front of what you want. A bit lengthy perhaps. One
function that has been proposed is OFFSET, which will tell you
exactly what you want to know. However, it does not appear that it
will get into the next standard.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
