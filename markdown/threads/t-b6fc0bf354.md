[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# API GetFullPAthName

_10 messages · 5 participants · 2003-03_

---

### API GetFullPAthName

- **From:** "James" <james@wasystems.co.nz>
- **Date:** 2003-03-21T10:14:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<V4rea.23790$jE3.559280@news.xtra.co.nz>`

```
Fujitsu Power Cobol 6. I can seem to get this to work. It say unresolved
external linkage. I have the kernel32.lib file included in the module. Any
ideas ?
```

#### ↳ Re: API GetFullPAthName

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-20T19:16:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LrydnXlxmJuP9OejXTWckw@giganews.com>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz>`

```

"James" <james@wasystems.co.nz> wrote in message
news:V4rea.23790$jE3.559280@news.xtra.co.nz...
> Fujitsu Power Cobol 6. I can seem to get this to work. It say unresolved
> external linkage. I have the kernel32.lib file included in the module. Any
> ideas ?


Make sure Script/Properties/Options includes:

ALPHAL(WORD)

Without this, Fujitsu folds called module names to upper-case.
```

##### ↳ ↳ Re: API GetFullPAthName

- **From:** "James" <james@wasystems.co.nz>
- **Date:** 2003-03-21T13:37:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3uea.24035$jE3.563178@news.xtra.co.nz>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz> <LrydnXlxmJuP9OejXTWckw@giganews.com>`

```
Now it cant find some other functions....



"JerryMouse" <nospam@bisusa.com> wrote in message
news:LrydnXlxmJuP9OejXTWckw@giganews.com...
>
> "James" <james@wasystems.co.nz> wrote in message
> news:V4rea.23790$jE3.559280@news.xtra.co.nz...
> > Fujitsu Power Cobol 6. I can seem to get this to work. It say unresolved
> > external linkage. I have the kernel32.lib file included in the module.
Any
> > ideas ?
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: API GetFullPAthName

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-21T03:05:23
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7a8176_1@text-west.newsgroups.com>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz>`

```
You need "user32.lib"

Pete.

"James" <james@wasystems.co.nz> wrote in message
news:V4rea.23790$jE3.559280@news.xtra.co.nz...
> Fujitsu Power Cobol 6. I can seem to get this to work. It say unresolved
> external linkage. I have the kernel32.lib file included in the module. Any
> ideas ?
>
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

##### ↳ ↳ Re: API GetFullPAthName

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-22T10:37:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303221037.11d40436@posting.google.com>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz> <3e7a8176_1@text-west.newsgroups.com>`

```
Pete - according to this:

http://msdn.microsoft.com/library/en-us/fileio/base/getfullpathname.asp

It's Kernel32.lib.  It's also why I suggested checking parm signature
and using GetFullPathNameA.


"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:<3e7a8176_1@text-west.newsgroups.com>...
> You need "user32.lib"
> 
…[15 more quoted lines elided]…
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: API GetFullPAthName

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-23T00:55:21
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7d0603_2@text-west.newsgroups.com>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz> <3e7a8176_1@text-west.newsgroups.com> <bfdfc3e8.0303221037.11d40436@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0303221037.11d40436@posting.google.com...
> Pete - according to this:
>
…[4 more quoted lines elided]…
>
Yes, I agree it SHOULD be Kernel32.lib. But he tried that and it didn't
work... Using the alias GetFullPathNameA is also a useful trick that has
worked for me on a few occasions.

However, I almost always include User32.lib in the project when I am using
the API and since I've been doing that I've had fewer problems...

I was trying to help <G>. As such, I suggested doing what I would do when
faced with the same problem. If it still doesn't work he is no worse off and
he has eliminated one more possibility...

Pete.






----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: API GetFullPAthName

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-20T21:03:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303202103.624f90b9@posting.google.com>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz>`

```
Try GetFullPathNameA

That fails - check the parms, the signature of parm lengths must match.

"James" <james@wasystems.co.nz> wrote in message news:<V4rea.23790$jE3.559280@news.xtra.co.nz>...
> Fujitsu Power Cobol 6. I can seem to get this to work. It say unresolved
> external linkage. I have the kernel32.lib file included in the module. Any
> ideas ?
```

#### ↳ Re: API GetFullPAthName

- **From:** "R. Hendriks" <R.Hendriks_1@uvt.nl>
- **Date:** 2003-03-21T13:06:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5ev31$ktg$1@mailnews.kub.nl>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz>`

```
post the code of the API call and I'll be glad to look at it.

"James" <james@wasystems.co.nz> wrote in message
news:V4rea.23790$jE3.559280@news.xtra.co.nz...
> Fujitsu Power Cobol 6. I can seem to get this to work. It say unresolved
> external linkage. I have the kernel32.lib file included in the module. Any
> ideas ?
>
>
```

##### ↳ ↳ Re: API GetFullPAthName

- **From:** "James" <james@wasystems.co.nz>
- **Date:** 2003-03-24T08:43:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71pfa.29021$jE3.657664@news.xtra.co.nz>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz> <b5ev31$ktg$1@mailnews.kub.nl>`

```
 ENVIRONMENT     DIVISION.
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01 lpFileName       pic x(256).
 01 nBufferLength    pic s9(6) comp-5.
 01 lpBuffer         pic x(256).
 01 lpFilePart       pic x(256) value spaces.
 01 return-value     pic s9(6) comp-5.
 PROCEDURE       DIVISION.
     move "main.exe" to lpBuffer.
     move 256 to nBufferLength.
     call "GetFullPathNameA" with STDCALL using
                by reference lpFileName,
                by value nBufferLength,
                by reference lpBuffer,
                by reference lpFilePart
          returning return-value.



"R. Hendriks" <R.Hendriks_1@uvt.nl> wrote in message
news:b5ev31$ktg$1@mailnews.kub.nl...
> post the code of the API call and I'll be glad to look at it.
>
…[3 more quoted lines elided]…
> > external linkage. I have the kernel32.lib file included in the module.
Any
> > ideas ?
> >
> >
>
>
```

###### ↳ ↳ ↳ Re: API GetFullPAthName

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-23T21:52:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303232152.4de0bbc7@posting.google.com>`
- **References:** `<V4rea.23790$jE3.559280@news.xtra.co.nz> <b5ev31$ktg$1@mailnews.kub.nl> <71pfa.29021$jE3.657664@news.xtra.co.nz>`

```
Are you using Binary(Byte) as a compiler directive?

If so - the Pic S9(6) COMP-5's will be 3 bytes (not good).

The MS docs indicate the following:

DWORD GetFullPathName(
  LPCTSTR lpFileName,  // file name
  DWORD nBufferLength, // size of path buffer
  LPTSTR lpBuffer,     // path buffer
  LPTSTR *lpFilePart   // address of file name in path
);


I didn't test this but try:

  01 lpFileName       pic x(256).
  01 nBufferLength    pic s9(9) comp-5.
  01 lpBuffer         pic x(256).
  01 lpFilePart       POINTER.
  01 return-value     pic S9(9) comp-5.
  PROCEDURE       DIVISION.
      move "main.exe" to lpBuffer.
      move 256 to nBufferLength.
      call "GetFullPathNameA" with STDCALL using
                 by reference lpFileName,
                 by value nBufferLength,
                 by reference lpBuffer,
                 by reference lpFilePart
           returning return-value.

I changed lpfilepart to Pointer because the docs say:

lpFilePart 
[out] Pointer to a buffer that receives the address (in lpBuffer) of
the final file name component in the path.

Since the buffer is receiving the address, it's a pointer.  Now, I
expect that you can't pass this pointer by reference - I think the
compiler will compain.

So change it to pic s9(9) comp-5 and redefine it with usage pointer. 
You'll have to use that pointer to get the path portion.


"James" <james@wasystems.co.nz> wrote in message news:<71pfa.29021$jE3.657664@news.xtra.co.nz>...
> ENVIRONMENT     DIVISION.
>  DATA            DIVISION.
…[31 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
