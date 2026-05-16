[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Another pointer question.

_2 messages · 1 participant · 2001-02_

---

### Another pointer question.

- **From:** "Tom Wright" <twright@@larimore.net>
- **Date:** 2001-02-01T10:48:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rtge6.1283$9r5.206995@news1.primary.net>`

```
In Microfocus cobol how does someone setup a pointer that is return to them
from a C DLL where the pointer points to an array.

Thanks
Tom Wright
```

#### ↳ Re: Another pointer question.

- **From:** "Jacques Vidal" <jvidal@mail.dotcom.fr>
- **Date:** 2001-02-02T19:53:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95evsm$er9$1@wanadoo.fr>`
- **References:** `<rtge6.1283$9r5.206995@news1.primary.net>`

```

Tom Wright <twright@@larimore.net> a �crit dans le message :
rtge6.1283$9r5.206995@news1.primary.net...
> In Microfocus cobol how does someone setup a pointer that is return to
them
> from a C DLL where the pointer points to an array.
>
> Thanks
> Tom Wright

If I understand what you mean correctly, it should look like this:

WORKING-STORAGE SECTION.
    77    MY-DATA-POINTER    USAGE    POINTER.
    ...
LINKAGE SECTION.
    01    MY-DATA-ARRAY.
            02    MY-DATA    <picture clause> <occurs clause>. // to keep it
simple
    ...
PROCEDURE DIVISION.
    ...
    CALL <call convention if needed> "cfunc" USING BY REFERENCE
MY-DATA-POINTER.
    SET ADDRESS OF MY-DATA-ARRAY TO MY-DATA-POINTER.
    ...

From now on,  you can access your array elements with MY-DATA (n). Depending
on what your array contains, you may have to be careful when you define
MY-DATA for alignment reasons. See the  h2cpy utility (it comes packaged
with the mF compiler) if your data is too much complex.

Hope it helps,

Jacques Vidal
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
