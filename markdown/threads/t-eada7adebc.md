[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM Cobol resolution 80x24->132x65

_2 messages · 2 participants · 2004-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM Cobol resolution 80x24->132x65

- **From:** jchipocov@yahoo.com.ar (Juan)
- **Date:** 2004-04-15T19:20:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8a559b.0404151820.3154eb0c@posting.google.com>`

```
Hi friends

I have following problem:
My rm Cobol application is in 80x24 format and I would wish that some
reports appears in a 132x65 format. When I tried :#xterm -geometry 132x65 I
got my xterm terminal resize to that resolution but my cobol
application keeps with 80x24 format, Where should I do the changes in
order to resize my application size???

Thanks in advance

Juan
```

#### ↳ Re: RM Cobol resolution 80x24->132x65

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-04-16T08:16:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v1v7091anag4fnrh3qm67sv7rsnnn03nu@4ax.com>`
- **References:** `<bf8a559b.0404151820.3154eb0c@posting.google.com>`

```
On 15 Apr 2004 19:20:23 -0700, jchipocov@yahoo.com.ar (Juan) wrote:

>Hi friends
>
…[9 more quoted lines elided]…
>Juan

Look at your runtime users manual and search for
SCREEN-COLUMNS = screen-width  (page 8-18)
and
RMTERM132 environment variable

You may need to mess with the terminfo again for this to work.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
