[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Syntax errors in ms cobol II

_2 messages · 2 participants · 1998-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Syntax errors in ms cobol II

- **From:** "jay" <ua-author-14326@usenetarchives.gap>
- **Date:** 1998-08-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdc471$cc97f060$50dcf5cf@default>`

```



I need the syntax errors to retrieve from ms cobol II,

please post,Thanking you in advance.
```

#### ↳ Re: Syntax errors in ms cobol II

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-08-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a08fd7ea0f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bdc471$cc97f060$50dcf5cf@default>`
- **References:** `<01bdc471$cc97f060$50dcf5cf@default>`

```
jay wrote:

› I need the syntax errors to retrieve from ms cobol II,

Just compile this and print the listing:
-----start code-----
IDENTIFICATION DIVISION.
PROGRAM-ID. ERRMSG.
PROCEDURE DIVISION.
P. GOBACK.
-----end of code-----
After that you could change the program's name to IEFBR14, compile, link
and save the load module to get some more functionality with less
output. :))

The COBOL Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
