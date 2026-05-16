[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol I/O error ,34,01 on file

_5 messages · 3 participants · 1999-01_

---

### Cobol I/O error ,34,01 on file

- **From:** "stcheong" <stcheong@mbox2.singnet.com.sg>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76hs3p$eu4$1@mawar.singnet.com.sg>`

```
I need some answer for the problems which I encountered.
I am running a called program under unix ATT V5.
My datafile is an ISAM file with more than 1.07GB.
I am running under rmcobol version 5
Everytime I run the program, it stopped at the same point.
I have change my disk block size from 1024 to 4096. It should allow up to a
max. of 2GB.
The error could refer to insufficient disk space which infact, there are
still approx. 900MB of free disk space.
Hope someone out there would be able to help.
Thanks

popsinit@popular.com.sg
```

#### ↳ Re: Cobol I/O error ,34,01 on file

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990101114105.21249.00001605@ngol07.aol.com>`
- **References:** `<76hs3p$eu4$1@mawar.singnet.com.sg>`

```

In article <76hs3p$eu4$1@mawar.singnet.com.sg>, "stcheong"
<stcheong@mbox2.singnet.com.sg> writes:

>Subject:	Cobol I/O error ,34,01 on file
>From:	"stcheong" <stcheong@mbox2.singnet.com.sg>
…[15 more quoted lines elided]…
>

You might want to check with the vendor as to the actual file size limitation
using the default .dll/lib files.  I experienced something similar with
FujiCOBOL.  They indicatedthat I could process up to 2G files, but my programs
repeatedly abended at 1.3G.   Later I found that there was a LARGE file DLL had
to be swapped out for the standard file handling DLL.
```

##### ↳ ↳ Re: Cobol I/O error ,34,01 on file

- **From:** "stcheong" <stcheong@mbox2.singnet.com.sg>
- **Date:** 1999-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76k52r$9lr$1@mawar.singnet.com.sg>`
- **References:** `<76hs3p$eu4$1@mawar.singnet.com.sg> <19990101114105.21249.00001605@ngol07.aol.com>`

```
System DLL or Cobol DLL  ?
Thanks
popsinit@popular.com.sg


Sff5ky wrote in message <19990101114105.21249.00001605@ngol07.aol.com>...
>
>
>You might want to check with the vendor as to the actual file size
limitation
>using the default .dll/lib files.  I experienced something similar with
>FujiCOBOL.  They indicatedthat I could process up to 2G files, but my
programs
>repeatedly abended at 1.3G.   Later I found that there was a LARGE file DLL
had
>to be swapped out for the standard file handling DLL.
>
>
```

###### ↳ ↳ ↳ Re: Cobol I/O error ,34,01 on file

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990102122928.25338.00001920@ngol02.aol.com>`
- **References:** `<76k52r$9lr$1@mawar.singnet.com.sg>`

```

In article <76k52r$9lr$1@mawar.singnet.com.sg>, "stcheong"
<stcheong@mbox2.singnet.com.sg> writes:

>
>System DLL or Cobol DLL  ?
…[3 more quoted lines elided]…
>

This replacement DLL was a COBOL DLL
```

#### ↳ Re: Cobol I/O error ,34,01 on file

- **From:** "Robert Heady" <rheady1@flash.net>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ghzj2.786$fR1.945@news.flash.net>`
- **References:** `<76hs3p$eu4$1@mawar.singnet.com.sg>`

```
I suspect that maybe you are running into the ulimit.  The ulimit is defined
in the UNIX kernel and sets the maximun
file size for a user.  Type ulimit at a UNIX prompt, the number returned is
a maximum number of 512? blocks allowed.  See
your system documentation for extending the ulimit.

For indexed files the maximum file size depends on the block size used for
the file.
 (MAX_LOCK_BYTE / (BlockSize + 256) ) * BlockSize

The larger the block size, the closer the FILE_LIMIT will approach the
MAX_LOCK_BYTE.
Examples:

 BlockSize = 512
                       (2147478525 / ( 512 + 256)) * 512    =
1,431,652,350  bytes   (1.33 GB)

 BlockSize =  4096
                       (2147478525 / ( 4096 + 256)) * 4096 =   2,021,156,258
bytes  (1.88 GB)

stcheong wrote in message <76hs3p$eu4$1@mawar.singnet.com.sg>...
>I need some answer for the problems which I encountered.
>I am running a called program under unix ATT V5.
…[13 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
