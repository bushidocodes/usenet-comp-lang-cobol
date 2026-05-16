[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Print screen under w98

_2 messages · 2 participants · 2000-02_

---

### Print screen under w98

- **From:** "Massimo Morgia" <areasoftware@tiscali.it>
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<880i0v$enl$1@pegasus.tiscalinet.it>`

```
I must print the screen (Microfocus cobol caracter pgm)
under w98 how to do ?

Best regards
```

#### ↳ Re: Print screen under w98

- **From:** mrtonyr@my-deja.com
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8817d3$9ie$1@nnrp1.deja.com>`
- **References:** `<880i0v$enl$1@pegasus.tiscalinet.it>`

```
In article <880i0v$enl$1@pegasus.tiscalinet.it>,
  "Massimo Morgia" <areasoftware@tiscali.it> wrote:
> I must print the screen (Microfocus cobol caracter pgm)
> under w98 how to do ?
…[3 more quoted lines elided]…
>

In Micro-focus you can use the cobol function "CBL_READ_SCR_CHATTRS"
to read the screen into a buffer and then just write the buffer to the
printer one line at a time. Micro Focus manual should tell you how to
call the function and the working storage requirements.

Tony


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
