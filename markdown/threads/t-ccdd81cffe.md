[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# lock record problem on fujitsu v 4.2

_2 messages · 2 participants · 2000-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### lock record problem on fujitsu v 4.2

- **From:** "Massimo Morgia" <areasoftware@tiscali.it>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g53a8$thn$1@pegasus.tiscalinet.it>`

```
When I read the same record of the same indexed file from another computer
in the local net (w98) the system not wait but send the message "JPM0320I-I
Input output error" have you a solution ?


Best regards

Massimo Morgia
```

#### ↳ Re: lock record problem on fujitsu v 4.2

- **From:** "Joe Hunter" <pcs@usaor.net>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sicfna3fqod137@corp.supernews.com>`
- **References:** `<8g53a8$thn$1@pegasus.tiscalinet.it>`

```

Massimo Morgia <areasoftware@tiscali.it> wrote in message
news:8g53a8$thn$1@pegasus.tiscalinet.it...
> When I read the same record of the same indexed file from another computer
> in the local net (w98) the system not wait but send the message
"JPM0320I-I
> Input output error" have you a solution ?
>
What is the value of FILE-STATUS?

Try LOCK MODE IS AUTOMATIC.

The above message states "Close error during program termination"  Was there
another error before this.

Joe Hunter
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
