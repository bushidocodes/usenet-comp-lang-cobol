[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress 2.0 and Dialog System 3.0

_2 messages · 2 participants · 1998-03_

---

### NetExpress 2.0 and Dialog System 3.0

- **From:** "tommy nilsen" <ua-author-17072129@usenetarchives.gap>
- **Date:** 1998-03-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34FD6A72.789D155A@yahoo.com>`

```

Hi.

I'm using Dialog System 3.0 in NetExpress 2.0

Can I post a user-event from one object to another (not window) ??

I've tried it, but I can't get it working..

Am I doing something wrong or what.... ???

Tommy Nilsen
tom··.@ya··o.com
```

#### ↳ Re: NetExpress 2.0 and Dialog System 3.0

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b833b8aef0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34FD6A72.789D155A@yahoo.com>`
- **References:** `<34FD6A72.789D155A@yahoo.com>`

```

tommy nilsen wrote:
› 
› Hi.
…[8 more quoted lines elided]…
› 

I'm an expert with Dialog, but I don't understand your terminology.
What are you trying to accomplish exactly?

Dialog has events occuring at different levels.

For example - a GAINED-FOCUS event. You can code it on an individual
object - say an entry field. If you don't code it there, the Dialog
runtime will look for a coded GAINED-FOCUS even in the Window Dialog of
the window you placed the entry field on. If it does not find it there,
it looks in the GLOBAL DIALOG for the event. So if you have envent you
want to capture across all objects in a particular window, code it in
the window dialog. If you want to capture the event across the entire
screen set, code it in the Global Dialog.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
