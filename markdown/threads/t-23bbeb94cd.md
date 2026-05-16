[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trapping errors using CALL

_3 messages · 3 participants · 2001-11_

---

### Trapping errors using CALL

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2001-11-09T05:45:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0111090545.798a8112@posting.google.com>`

```
Hi,

I have a COBOL main program calling a COBOL sub-program using the CALL
statement. My COBOL sub-program has a series of COMPUTE / DIVIDE BY
statements that may result in an error. I do not want to write an ON
SIZE ERROR for each one of them. Can I trap this in the CALL statement
?? The sub-program is not a separate executable, it is compiled and
linked to the main program.

Thanks and Regards,
M Shetty
```

#### ↳ Re: Trapping errors using CALL

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-09T09:28:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pDRG7.33893$bf1.3846287@news20.bellglobal.com>`
- **References:** `<bfbb8fd4.0111090545.798a8112@posting.google.com>`

```
If the compiler is newish, then you can do it in the decalratives.

Donald.

"mshetty" <mshetty@mail.com> wrote in message
news:bfbb8fd4.0111090545.798a8112@posting.google.com...
> Hi,
>
…[8 more quoted lines elided]…
> M Shetty
```

#### ↳ Re: Trapping errors using CALL

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-11-09T14:32:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011109093215.23316.00001682@mb-ck.aol.com>`
- **References:** `<bfbb8fd4.0111090545.798a8112@posting.google.com>`

```
M Shetty writes ...

>Hi,
>
…[7 more quoted lines elided]…
>Thanks and Regards,

You can do this using callable LE services and creating your own condition
handler (which can be written in COBOL).

<ad>
We cover how to use LE services in programs written in Assembler, COBOL, PL/I,
and C in our three-day course "Application Design Using LE Services". For more
information about this course, look at:

http://www.trainersfriend.com/m212descr.htm

</ad>

Hope this helps.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
