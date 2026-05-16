[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# file size

_3 messages · 3 participants · 1999-06_

---

### file size

- **From:** theisb@21st.dk
- **Date:** 1999-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jgcvk$m2k$1@nnrp1.deja.com>`

```
Hi There.

I've got a variable with a size of 2000 bytes I'd like to write to a
file, but when I write the file it's 2002 bytes long???

Where does the 2 bytes come from, and how do I get rid of them?

Regards Theis (Denmark)


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: file size

- **From:** Ed Stevens <Ed.Stevens@nmm.nissan-usa.com>
- **Date:** 1999-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jgfaf$mqc$1@nnrp1.deja.com>`
- **References:** `<7jgcvk$m2k$1@nnrp1.deja.com>`

```
In article <7jgcvk$m2k$1@nnrp1.deja.com>,
  theisb@21st.dk wrote:
> Hi There.
>
…[9 more quoted lines elided]…
>

What COBOL are you using?  If Micro Focus and your file is ORGANIZATION
LINE SEQUENTIAL, the extra two bytes are the CR-LF pair.  If it is
RECORD SEQUENTIAL, with a variable record length, it is the record
length descriptor.
```

#### ↳ Re: file size

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Oj_63.1615$1Z6.240577@typhoon01.swbell.net>`
- **References:** `<7jgcvk$m2k$1@nnrp1.deja.com>`

```

<theisb@21st.dk> wrote in message news:7jgcvk$m2k$1@nnrp1.deja.com...
> Hi There.
>
…[4 more quoted lines elided]…
>
And if it's the FJ compiler, the compiler adds two bytes to the FRONT
of the record. The two bytes contain the record size.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
