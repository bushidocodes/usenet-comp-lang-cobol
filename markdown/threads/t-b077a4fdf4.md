[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ANSI COBOL and DELETE FILE

_7 messages · 5 participants · 2004-05_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### ANSI COBOL and DELETE FILE

- **From:** marvbudd@cs.com (Marvin E Budd)
- **Date:** 2004-05-04T15:21:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a66855f8.0405041421.f040d69@posting.google.com>`

```
We would like to know if the standards for COBOL include DELETE FILE
filename. In our code we want to delete a file on disk and have seen
this statement on some quick references. But it is apparently not
available in the Fujitsu NetCOBOL for Windows implementation which we
are using although they have two other extensions that can accomplish
the same thing. We are puzzled why they would implement extensions for
this when others have implemented the DELETE FILE statement.

Thanks for any help.

Marvin Budd
```

#### ↳ Re: ANSI COBOL and DELETE FILE

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-05-04T15:53:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c796st$2ccc$1@si05.rsvl.unisys.com>`
- **References:** `<a66855f8.0405041421.f040d69@posting.google.com>`

```
No, the COBOL standards do not include a DELETE FILE statement.  There have
been proposals submitted to INCITS/J4 to include such a feature, but ISO/IEC
JTC1/SC22/WG4 did not include it in its list of approved enhancements for
the proposed 2008 standard currently in preparation.

My personal opinion is that it means to "delete a file on disk" differs from
implementation to implementation and from device to device, and rightly
belongs in the implementation-dependent category.   In the Unisys MCP
environment, an extension to CLOSE, specifically "CLOSE <filename> WITH
PURGE", (applicable to other devices as well, such as magnetic tape, and
device-independent at the syntactic level) has provided this functionality
through three decades and more of implementations of COBOL, and I'm not sure
I see the fundamental semantic advantage of the DELETE FILE syntax over
enhancements to CLOSE (standard or otherwise).

    -Chuck Stevens

"Marvin E Budd" <marvbudd@cs.com> wrote in message
news:a66855f8.0405041421.f040d69@posting.google.com...
> We would like to know if the standards for COBOL include DELETE FILE
> filename. In our code we want to delete a file on disk and have seen
…[8 more quoted lines elided]…
> Marvin Budd
```

#### ↳ Re: ANSI COBOL and DELETE FILE

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-05-04T17:53:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_LednaYBHcVhgwXdRVn-vg@giganews.com>`
- **References:** `<a66855f8.0405041421.f040d69@posting.google.com>`

```
Marvin E Budd wrote:
> We would like to know if the standards for COBOL include DELETE FILE
> filename. In our code we want to delete a file on disk and have seen
…[4 more quoted lines elided]…
> this when others have implemented the DELETE FILE statement.

You might ask the developers at Fujitsu. But I'm pretty sure:

A. Deleting a file is not part of any COBOL standard,
B. Nobody ever asked Fujitsu to implement such a thing as an extension to
the language.
```

#### ↳ Re: ANSI COBOL and DELETE FILE

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-04T20:16:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405041916.37f20e17@posting.google.com>`
- **References:** `<a66855f8.0405041421.f040d69@posting.google.com>`

```
marvbudd@cs.com (Marvin E Budd) wrote 

> We are puzzled why they would implement extensions for
> this when others have implemented the DELETE FILE statement.

You could ask why others would implement a 'DELETE FILE' statement
when other extensions, such as 'CBL_DELETE_FILE', are available.

Partly the answer would lie in the way that indexed files are
implemented.  With, say, Microfocus, an indexed file is implemented as
a data file plus a separate index file with a type .idx.  If the
CBL_DELETE_FILE were used with the name of the file then only the data
file would be deleted and the index file may remain and cause problem
if the file were recreated.  The 'DELETE FILE' overcomes this issue by
deleting both parts, and can do so because it has the correct
semantics.

Fujitsu doesn't need this, its indexed files are a single file so any
simple delete, eg: CALL SYSTEM("rm filename"), will work correctly.
```

##### ↳ ↳ Re: ANSI COBOL and DELETE FILE

- **From:** marvbudd@cs.com (Marvin E Budd)
- **Date:** 2004-05-05T08:07:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a66855f8.0405050707.706d7208@posting.google.com>`
- **References:** `<a66855f8.0405041421.f040d69@posting.google.com> <217e491a.0405041916.37f20e17@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0405041916.37f20e17@posting.google.com>...

> Fujitsu doesn't need this, its indexed files are a single file so any
> simple delete, eg: CALL SYSTEM("rm filename"), will work correctly.

Many thanks to all who have graciously responded to my question.

Richard, the CALL SYSTEM() construct is unfamiliar to me. Have you
used this in Fujitsu NetCOBOL for Windows, or was this hypothetical
code for communicating your excellent point? Attempting to compile
this statement fails for me in a default configuration.
```

###### ↳ ↳ ↳ Re: ANSI COBOL and DELETE FILE

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-05T16:47:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405051547.337311aa@posting.google.com>`
- **References:** `<a66855f8.0405041421.f040d69@posting.google.com> <217e491a.0405041916.37f20e17@posting.google.com> <a66855f8.0405050707.706d7208@posting.google.com>`

```
marvbudd@cs.com (Marvin E Budd) wrote 

> > Fujitsu doesn't need this, its indexed files are a single file so any
> > simple delete, eg: CALL SYSTEM("rm filename"), will work correctly.
…[6 more quoted lines elided]…
> this statement fails for me in a default configuration.

Oops, wrong syntax, I have been writing too much Python (yay) and Perl
(yuk) recently.

    Try CALL "system" USING "rm filename" & x"00"

But then this is a Unix/Linux thing, so you have to use "del
filename", or even "COMMAND /C del filename" & x"00".
```

###### ↳ ↳ ↳ Re: ANSI COBOL and DELETE FILE

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-06T21:56:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<409ab422.301593576@news.optonline.net>`
- **References:** `<a66855f8.0405041421.f040d69@posting.google.com> <217e491a.0405041916.37f20e17@posting.google.com> <a66855f8.0405050707.706d7208@posting.google.com> <217e491a.0405051547.337311aa@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>marvbudd@cs.com (Marvin E Budd) wrote 
>
…[16 more quoted lines elided]…
>filename", or even "COMMAND /C del filename" & x"00".

If the compiler had been Micro Focus, an undocumented(?) extension lets one
write:

call 'SYSTEM' using z'rm filename'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
