[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing a file - PC_WIN_PRINT_FILE_EXT

_2 messages · 2 participants · 1996-05_

---

### Printing a file - PC_WIN_PRINT_FILE_EXT

- **From:** "jhost..." <ua-author-16629294@usenetarchives.gap>
- **Date:** 1996-05-15T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4nfe67$mpt@lily.redrose.net>`

```

To print a report from within my COBOL program, I create a file that
contains the report. I then use the library routine PC_WIN_PRINT_FILE_EXT,
giving it the file name that contains the report. This successfully prints my
report from Windows for Workgroups!

Now, the problem: When I run this application under Windows NT, everything
works great, except the printing. Nothing gets sent to the printer, whether
it is local or on the network. It appears to work successfully, but nothing
gets printed. We think we have narrowed it down to this PC_WIN_PRINT_FILE_EXT
function. Any help or suggestions would be greatly appreciated.

Thank you!

****************************
Jay Hostetter
D&E Tel. & Tel. Co.
Ephrata, Pa. U.S.A
jho··.@da··e.com
****************************
```

#### ↳ Re: Printing a file - PC_WIN_PRINT_FILE_EXT

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1996-05-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fbcb84854e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4nfe67$mpt@lily.redrose.net>`
- **References:** `<4nfe67$mpt@lily.redrose.net>`

```

Hi Jay!

You might want to look at using COBOL WinPrint. Because you're already
using COBOL spII for your screen handling, COBOL WinPrint would be a snap to
implement. Are you running a 16 bit Windows application under Windows NT or
is it a 32 bit application?

Take a look at our home page and follow the link for Using the Windows Print
Manager in COBOL. Our URL is:

http://www.flexus.com

Call me if you have questions on the product.

Bob Wolfe
flexus
rtw··.@fle··s.com

In article <4nfe67$m.··.@lil··e.net>, jho··.@da··e.com says...
› 
›   To print a report from within my COBOL program, I create a file that 
…[16 more quoted lines elided]…
› function.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
