[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RESPONSE MODE TRANSACTION TERMINATED WITHOUT REPLY.

_2 messages · 2 participants · 2001-08_

---

### RESPONSE MODE TRANSACTION TERMINATED WITHOUT REPLY.

- **From:** kanoako@netnet.net (Kano Ako)
- **Date:** 2001-08-16T08:21:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<677e6c81.0108160721.194739e@posting.google.com>`

```
Greetings,

I apologize if this is 2x posted.  I posted via google and got a
server not found page when I hit the post button.


Anyway we are working on an IMS DC application and get the message in
the subject when the program tries to jump to another screen.  What in
general does this mean?

Thanks
KA
```

#### ↳ Re: RESPONSE MODE TRANSACTION TERMINATED WITHOUT REPLY.

- **From:** "Don Leahy" <dleahy@wave.home.com>
- **Date:** 2001-08-16T12:39:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DSe7.32281$KG2.3211994@news20.bellglobal.com>`
- **References:** `<677e6c81.0108160721.194739e@posting.google.com>`

```
This message occurs when an MPP (message processing program) terminates
without inserting a message to the IOPCB.   Look for a logic error in your
program that is causing it to bypass the message insert.   A very common
cause of this problem is a misbehaving edit routine that upon detecting an
error aborts further processing, including the message insert.

Kano Ako <kanoako@netnet.net> wrote in message
news:677e6c81.0108160721.194739e@posting.google.com...
> Greetings,
>
…[9 more quoted lines elided]…
> KA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
