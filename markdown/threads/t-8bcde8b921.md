[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus File Name Limitations

_2 messages · 2 participants · 2003-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus File Name Limitations

- **From:** dmckeon@ameritas.com (Dan McKeon)
- **Date:** 2003-09-18T14:28:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61ad99f6.0309181328.5d9b029@posting.google.com>`

```
We have encountered limitations in several MicroFocus Workbench
functions.  I know this product is no longer supported, but we are
unable to get approval to purchase NetExpress.  File handling
functions such as CBL_COPY_FILE, CBL_CHECK_FILE_EXIST, etc. will not
work if the DSN is over 100 bytes or so.  I was able to rewrite those
functions in C++ and call them from COBOL, but there is one more...

The "OPEN" command will fail if the file name is greater than 100
bytes.  This gets a bit trickier.  Has anyone else run into this?  Is
there any sort of compiler directive that can override the inherent
"OPEN" to something home-grown?  I can write C++ functions for these
too, but C++ creates a handle when you open the file and you reference
the handle to write, read, close.  It just gets a bit ugly to try to
keep the association between the file name and the handle.
```

#### ↳ Re: MicroFocus File Name Limitations

- **From:** godch01 <member30532@dbforums.com>
- **Date:** 2003-09-19T09:23:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3390348.1063977792@dbforums.com>`
- **References:** `<61ad99f6.0309181328.5d9b029@posting.google.com>`

```

I assume you're using this in Windows. If you are and can call C and C++
then use the Microsoft system function GetShortPathName to get a
truncated but vaid name. that is less than 65 bytes long.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
