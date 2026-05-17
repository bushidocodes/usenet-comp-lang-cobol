[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with Micro Focus Sort

_3 messages · 3 participants · 1997-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Help with Micro Focus Sort

- **From:** "john h. howe" <ua-author-36325@usenetarchives.gap>
- **Date:** 1997-06-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33AEFA05.4BB5@worldnet.att.net>`

```

Please help with a MF SORT problem.

A program created in MF Cobol ver. 3.2.46 ,sorts data, then prints a
report. When in the animator everything works fine. Once the program is
compiled and installed in the object subdir is when the problem starts.
When the program is executed, the runtime error LOAD FAILURE (173) ON
FILE _SORT rears its ugly head. I have tried everything I can think
of. Yes I have all of the files that the manual requires in a COBLIB
subdir, I also have an environmental variable COBDIR pointing to the
COBLIB directory.


Any help would be gratefully appreciated.

John H. Howe
Fairfield Communities, Inc.

joh··.@wor··t.net
```

#### ↳ Re: Help with Micro Focus Sort

- **From:** "j.s." <ua-author-88615@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbe53f81d2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33AEFA05.4BB5@worldnet.att.net>`
- **References:** `<33AEFA05.4BB5@worldnet.att.net>`

```

Are you using MFSORT or some other sort program. There are speical
programs the need to be delivered with the .EXE in order for the external
sort to work properly. Check the maunual, or call MF COBOL support(God be
with on this one).
John H. Howe wrote in article <33A··.@wor··t.net>...
› Please help with a MF SORT problem.
› 
…[16 more quoted lines elided]…
›
```

#### ↳ Re: Help with Micro Focus Sort

- **From:** "sa..." <ua-author-17071631@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbe53f81d2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33AEFA05.4BB5@worldnet.att.net>`
- **References:** `<33AEFA05.4BB5@worldnet.att.net>`

```

John,

What platform are you running on ?

We have the "_SORT.DLL" file in the current directory of the
application and have a TMP environment variable pointing to the
location where temporary sort files are held.

If you are using the static runtime then you may need to link in the
relevant OBJ using the linker. Check out the Linking section of the
manual. It gives info on what files need to be linked.

Regards
Dave.


On Mon, 23 Jun 1997 18:34:45 -0400, "John H. Howe"
wrote:

› Please help with a MF SORT problem.
› 
…[15 more quoted lines elided]…
› joh··.@wor··t.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
