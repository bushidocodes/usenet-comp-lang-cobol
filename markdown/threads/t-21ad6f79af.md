[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Status number 39 on opening file

_3 messages · 3 participants · 2000-11_

---

### Status number 39 on opening file

- **From:** "Daniel Ratt���" <dratte@mediom.qc.ca>
- **Date:** 2000-11-04T01:26:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SXNM5.3713$vr5.138222@wagner.videotron.net>`

```
Hello,

I have to read data from an input file organized sequentially.  I use a flag
to monitor the status of the file on opening, and when running the code with
the debugger I see that the status number is 39.  This is not among the
status numbers I was told about, and I wonder if someone could tell me what
it means.

Also, the records in this file are each supposed to have one 20-character
field, followed by 12 binary numeric fields for 4-digit integer values
(thus, 2 bytes each).  This makes records of 44 bytes each.  Now, when I
read this input file with a low-level text editor like Notepad or Textpad,
the records look like they are supposed to: 20 alphanumeric characters
followed by 24 characters of any nature, representing the bytes for the
binary integers.  However, when I look at this file with a binary editor,
these same records show that the binary-integer fields contain more than 24
chars in some cases, and this way the records are not of constant length.
What is this due to, and how can I read this data as 12 binary integers?  (I
am a student in a university Cobol course, and I have not yet seen how to
access files randomly with Cobol, nor am I allowed to for this project...).

Thank you!
```

#### ↳ Re: Status number 39 on opening file

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tVTM5.2401$2Y1.215875@nnrp1.sbc.net>`
- **References:** `<SXNM5.3713$vr5.138222@wagner.videotron.net>`

```
Be careful, too, on the organization. If you're trying to read binary
data with a, for example, LINE SEQUENTIAL organization some binary
data may confuse the program into thinking that a carriage return has
been detected. Conversely, when you issue a read, the program may
slurp up the whole file  as one record, looking for a non-existent
carriage return.

On the other matter, trust the display from the binary editor. Again,
as above, text editors make the presumption that you are reading
non-binary text and will treat binary data, sometimes, as control
information (such as line-feed, or end-of-file).


"Daniel Ratt�" <dratte@mediom.qc.ca> wrote in message
news:SXNM5.3713$vr5.138222@wagner.videotron.net...
> Hello,
>
> I have to read data from an input file organized sequentially.  I
use a flag
> to monitor the status of the file on opening, and when running the
code with
> the debugger I see that the status number is 39.  This is not among
the
> status numbers I was told about, and I wonder if someone could tell
me what
> it means.
>
> Also, the records in this file are each supposed to have one
20-character
> field, followed by 12 binary numeric fields for 4-digit integer
values
> (thus, 2 bytes each).  This makes records of 44 bytes each.  Now,
when I
> read this input file with a low-level text editor like Notepad or
Textpad,
> the records look like they are supposed to: 20 alphanumeric
characters
> followed by 24 characters of any nature, representing the bytes for
the
> binary integers.  However, when I look at this file with a binary
editor,
> these same records show that the binary-integer fields contain more
than 24
> chars in some cases, and this way the records are not of constant
length.
> What is this due to, and how can I read this data as 12 binary
integers?  (I
> am a student in a university Cobol course, and I have not yet seen
how to
> access files randomly with Cobol, nor am I allowed to for this
project...).
>
> Thank you!
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Status number 39 on opening file

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-11-04T00:43:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8u0b7p$bg0$1@newssvr04-int.news.prodigy.com>`
- **References:** `<SXNM5.3713$vr5.138222@wagner.videotron.net>`

```

39: The OPEN statement was unsuccessful because a conflict was detected
between the fixed file attributes and the attributes specified for that file
in the program.  These attributes include the organization of the file
(sequential, relative, or indexed), the prime record key, the alternate
record keys, the code set, the maximum record size, and record type (fixed
or variable).
    Most often, this happens when your program indicates a record size
different than that of the file's Data Control Block.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
