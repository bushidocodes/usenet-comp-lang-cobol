[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [Q] Anyone using MF CCI modules??

_2 messages · 1 participant · 1995-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### [Q] Anyone using MF CCI modules??

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-06-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3qvp7m$782@news0.cybernetics.net>`

```
Anyone using Micro Focus CCI stuff?
I just finished (I thought) setting up a C/S app, runs great as long as
the client and server are on the same system, craps out with RC=6 or 9
on the InitClient call if client and server are on different systems.
This is (should be) using the CCITCP mods.
:-(
```

#### ↳ Re: [Q] Anyone using MF CCI modules??

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-06-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0a7da9e8c4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3qvp7m$782@news0.cybernetics.net>`
- **References:** `<3qvp7m$782@news0.cybernetics.net>`

```
Greg Granger (ggr··.@cyb··s.net) wrote:
: Anyone using Micro Focus CCI stuff?
: I just finished (I thought) setting up a C/S app, runs great as long as
: the client and server are on the same system, craps out with RC=6 or 9
: on the InitClient call if client and server are on different systems.
: This is (should be) using the CCITCP mods.
: :-(

Well I discovered what my problem was.
I was using CCI across a bridge that filtered broadcasts. Once that was
changed everything worked well.

I'd still be interested in hearing from anyone using CCI (thoughts, comments
war stories, etc...)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
