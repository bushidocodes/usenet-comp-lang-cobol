[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DCE/thread support

_2 messages · 2 participants · 1996-09_

---

### DCE/thread support

- **From:** "dan jalbert" <ua-author-17086160@usenetarchives.gap>
- **Date:** 1996-09-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3246FBA3.54F1@uhc.com>`

```

Hi,

We're looking for a Cobol environment supporting the development
of DCE applications. Specifically, we'd like native cobol support
complete with thread safe run-time libraries. Please let us know if you
have any experience/recomendations in this area.

thanks!
Dan

p.s. My email is probably broken, please post replies.
```

#### ↳ Re: DCE/thread support

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-09-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cea972ae68-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3246FBA3.54F1@uhc.com>`
- **References:** `<3246FBA3.54F1@uhc.com>`

```

Dan Jalbert wrote:
› 
› Hi,
…[4 more quoted lines elided]…
› have any experience/recomendations in this area.

Hi Dan.

I`m not sure quite what you`re after (I don`t know enough about DCE, I`m afraid)
but I do know that the Micro Focus Unix product does have a set of DCE_ calls
(like our CBL_ calls) which put a COBOL-like wrapper around the DCE libraries
(by COBOL-like, I mean the interface is defined in terms more natural to a COBOL
program than the C API is. They might also do some nice housekeeping for you
too, though I can`t guarantee that). Having said that, you can, of course, call
the C API directly from any 32-bit Micro Focus product.

Sorry I can`t be of any more use, I guess you should contact the Micro Focus
sales department if you`re interested. They may have some literature for you.

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
