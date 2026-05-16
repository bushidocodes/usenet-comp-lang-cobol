[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Caller Line Identification /NetExpress/MF Cobol Under Unix

_3 messages · 3 participants · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Caller Line Identification /NetExpress/MF Cobol Under Unix

- **From:** nick@asheath.demon.co.uk (Nick & Carol Lucas-White)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365c45fd.188713@news.demon.co.uk>`

```
Has anyone any experience of using caller line identification with
NetExpress or Cobol under Unix. This is with an SDX Index phone system
and possibly some software from a compnay  called CT integration.
Basically a 'phone number is going to appear down a serial line and
then somehow we need to pick it up in a cobol program. Any assistance
on how to read a serial line (comm port) using MF cobol would also
help. Thanks in advance for any response.

Nick Lucas
```

#### ↳ Re: Caller Line Identification /NetExpress/MF Cobol Under Unix

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73k46f$n24@hyperion.mfltd.co.uk>`
- **References:** `<365c45fd.188713@news.demon.co.uk>`

```
Nick,

You can access serial ports using normal COBOL file handling syntax, or via
the CBL_OPEN_FILE, CBL_READ_FILE calls.

Nick & Carol Lucas-White wrote in message
<365c45fd.188713@news.demon.co.uk>...
>Has anyone any experience of using caller line identification with
>NetExpress or Cobol under Unix. This is with an SDX Index phone system
…[6 more quoted lines elided]…
>Nick Lucas
```

#### ↳ Re: Caller Line Identification /NetExpress/MF Cobol Under Unix

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981125214306.20914.00000634@ng128.aol.com>`
- **References:** `<365c45fd.188713@news.demon.co.uk>`

```
Hi Nick,

I use API calls to read/write to the com port.  If you would like samples
please let me know.

Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
