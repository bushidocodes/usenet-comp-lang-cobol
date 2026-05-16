[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Beginner Problems Acucobol

_2 messages · 2 participants · 2001-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Beginner Problems Acucobol

- **From:** "Stephan Wiesner" <stephan@stephanwiesner.de>
- **Date:** 2001-08-11T09:53:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l2o98$t8d$05$1@news.t-online.com>`

```
Hi, I'm studying computerscience and have to do a homework in Cobol.
My prof. just threw Acucobol 5.1 at us. No handbook, just some very basic
lessons.

Now I'm stuck.
How can I read what a user wrote into a Entry Field?

Is there a handbook or a userguide or something out there I can use with
Acucobol?

Stephan
```

#### ↳ Re: Beginner Problems Acucobol

- **From:** "Acucorp News" <shaun_gough@hotmail.com>
- **Date:** 2001-08-13T16:07:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1451C740A890D411B65C00104B95B1C03147BB@ras.acucorp.com>`
- **References:** `<9l2o98$t8d$05$1@news.t-online.com>`

```
Dear Stephan.

You can verify the contents of the data entered into an ENTRY-FIELD by
checking the contents of the WORKING-STORAGE item that you defines for the
ENTRY-FIELD.

For example, your program should look like the following:

 WORKING-STORAGE SECTION.
 01 entry-field-data       PIC X(10).

 SCREEN SECTION.
 01 user-screen.
    03 ENTRY-FIELD  USING entry-field-data, SIZE 10, LINE 5 COLUMN 10.

 PROCEDURE DIVISION.
 Main Section.
   DISPLAY user-screen.
   ACCEPT user-screen.

You can verify the contents of the ENTRY-FIELD by checking the contents of
the WORKING-STORAGE item entry-field-data in this example.

Thanks
Shaun Gough
ACUCORP Inc.
"Stephan Wiesner" <stephan@stephanwiesner.de> wrote in message
news:9l2o98$t8d$05$1@news.t-online.com...
> Hi, I'm studying computerscience and have to do a homework in Cobol.
> My prof. just threw Acucobol 5.1 at us. No handbook, just some very basic
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
