[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling win32 API CreateDirectoryA from Realia cobol program

_2 messages · 2 participants · 2001-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Calling win32 API CreateDirectoryA from Realia cobol program

- **From:** daniel_email2000@yahoo.com (Daniel)
- **Date:** 2001-08-22T17:41:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8e3e9cd.0108221641.15340973@posting.google.com>`

```
I am trying to call the Win32 API routine CreateDirectoryA from a
Realia Cobol program but the linking step is display the following
error:

Error LNK2001: unresolved external symbol  _CreateDirectoryA@8

This problem is probably because a library is missing.

This is my test program to call the WIN32 API routine

       PROGRAM-ID. TESTAPI.
       01  filename-str        PIC X(80).
       01  isec                PIC S9(9) BINARY.
       01  iresult             PIC S9(9) BINARY.
       PROCEDURE DIVISION.
       0000-MAIN-LOGIC.
           STRING 'APITMP'   DELIMITED BY SIZE
                 X'00'       DELIMITED BY SIZE
                      INTO            filename-str.
           CALL 'S_CreateDirectoryA'
                   USING BY REFERENCE  filename-str
                         BY REFERENCE  isec
                   GIVING              iresult.
           STOP RUN.

To compile and link I a type:

Cobol  testapi
Linkcob testapi

My questions are how do I link my object? What library do I need?
Where can I get the library?
```

#### ↳ Re: Calling win32 API CreateDirectoryA from Realia cobol program

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-08-23T02:19:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2LZg7.5990$n75.1122287@news4.rdc1.on.home.com>`
- **References:** `<a8e3e9cd.0108221641.15340973@posting.google.com>`

```
Use kernel32.lib.

"Daniel" <daniel_email2000@yahoo.com> wrote in message news:a8e3e9cd.0108221641.15340973@posting.google.com...
> I am trying to call the Win32 API routine CreateDirectoryA from a
> Realia Cobol program but the linking step is display the following
…[29 more quoted lines elided]…
> Where can I get the library?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
