[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# indexed file

_3 messages · 3 participants · 2002-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### indexed file

- **From:** "GG" <ggazzola@inwind.it>
- **Date:** 2002-07-13T13:21:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7PVX8.32903$7N3.749695@twister2.libero.it>`

```
How can I create an indexed file, to execute a batch cobol
program in the PC environment?


            thanks
            Giorgio.
```

#### ↳ Re: indexed file

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-07-13T13:37:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j2WX8.89293$eF5.2671220@twister.austin.rr.com>`
- **References:** `<7PVX8.32903$7N3.749695@twister2.libero.it>`

```
HUH?

To execute a 'batch' file in the PC environment you need either one of two things;

(1) A program which would read a data file and execute each command in it (which if you want
      and Indexed Data File for some reason, could be a COBOL program)   OR

(2) A text file that ends with a .BAT or .CMD extension that contains the list of commands you want
      to execute. This is NOT an indexed file.

Perhaps it is just too early on Saturday morning for me to correctly interpret what you asked. :)

-Paul


"GG" <ggazzola@inwind.it> wrote in message news:7PVX8.32903$7N3.749695@twister2.libero.it...
> How can I create an indexed file, to execute a batch cobol
> program in the PC environment?
…[5 more quoted lines elided]…
>
```

#### ↳ Re: indexed file

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-07-13T09:41:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J3WX8.1226$WF6.311065@news20.bellglobal.com>`
- **References:** `<7PVX8.32903$7N3.749695@twister2.libero.it>`

```
OPEN OUTPUT FILENAME.

Donald

"GG" <ggazzola@inwind.it> wrote in message
news:7PVX8.32903$7N3.749695@twister2.libero.it...
> How can I create an indexed file, to execute a batch cobol
> program in the PC environment?
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
