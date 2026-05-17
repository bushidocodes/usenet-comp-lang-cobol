[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INITIALIZE and FILLER question

_2 messages · 2 participants · 1995-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### INITIALIZE and FILLER question

- **From:** "wak..." <ua-author-17087769@usenetarchives.gap>
- **Date:** 1995-05-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3pdg1l$9i0@parsifal.nando.net>`

```
When I use INITIALIZE with a group item the area defined by FILLER is
low values when I would expect it to be spaces. Here is how I have it
defined.
01 x05-IO-AREA.
05 X05-RECORD-KEY.
10 X05-VENDOR PIC X(25).
10 FILLER PIC X(10).
Here is how I am using the verb.
INITIALIZE X05-IO-AREA.

Any help would be greatly appreciated.
```

#### ↳ Re: INITIALIZE and FILLER question

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1995-05-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc4af724d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3pdg1l$9i0@parsifal.nando.net>`
- **References:** `<3pdg1l$9i0@parsifal.nando.net>`

```
In message <<3pdg1l$9.··.@par··o.net>> wak··.@na··o.net writes:
› low values when I would expect it to be spaces. Here is how I have it
› defined.
…[7 more quoted lines elided]…
› Any help would be greatly appreciated.

That would appear to be correct behaviour.

Try using:

MOVE SPACES TO X05-IO-Area

If that is what you require.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
