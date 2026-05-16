[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do you use Cobol to convert a cobol print job onto Wordpad

_2 messages · 2 participants · 1999-06_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Migration and conversion`](../topics.md#migration)

---

### How do you use Cobol to convert a cobol print job onto Wordpad

- **From:** alisonchan@my-deja.com
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kl378$6j0$1@nnrp1.deja.com>`

```
I am a new comer to Cobol and my first assignment is to convert a cobol print
job using cobol on the AS400 system onto Wordpro or any other ASCII file so
that i can use it later and send out by e-mail as an attachment.

Any help will be greatly appreciated.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: How do you use Cobol to convert a cobol print job onto Wordpad

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376E2F68.DAD01187@zip.com.au>`
- **References:** `<7kl378$6j0$1@nnrp1.deja.com>`

```
alisonchan@my-deja.com wrote:
> 
> I am a new comer to Cobol and my first assignment is to convert a
…[4 more quoted lines elided]…
> Any help will be greatly appreciated.

I will assume you have FTP.

Create a job containing 

1. the cobol program output to a sequential file.
2. an FTP step to the PC (lan server whatever)

Voila....

Make sure your output from cobol is simple text, no format
characters or ANSI control characters (does AS400 have these?).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
