[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXTERNAL DATA

_2 messages · 2 participants · 1995-04_

---

### EXTERNAL DATA

- **From:** "gt..." <ua-author-2476667@usenetarchives.gap>
- **Date:** 1995-04-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3mhik3$lie@newsbf02.news.aol.com>`

```
Could someone explain external data and Global data to me. From the very
little
I know about this it sounds to good to be true, what are the pro's and
con's. Let me know if I am on the right track. By declaring a 01 level
structure EXTERNAL it
can be used by any other linked program without having to pass it in the
Linkage Section. Like using pointers in PL/I without having to pass the
pointer as a parm to the module.
Thanks
```

#### ↳ Re: EXTERNAL DATA

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-04-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4cee6a57b8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3mhik3$lie@newsbf02.news.aol.com>`
- **References:** `<3mhik3$lie@newsbf02.news.aol.com>`

```
In article <3mhik3$l.··.@new··l.com> I used EXTERNAL to use the same file in multiple programs in the same
gt··.@a··.com (GTOME) writes: run unit. In the Past, a programmer would have to keep opening and
closeing the file with some flag passed in the linkage section to
› alert the subroutine to open or close the file. Well, with EXTERNAL,
› little you can define the file in the main program, and then define it external
› structure EXTERNAL it in the subprogram, and be able to read it in the subprogram.

For example:
In the main program:
FD input-file
is external.
01 input-record pic x(80).

procedure division.
a000-patio-furniture.
open input input-file.
call 'subprog'.
close input-file.
stop run.

and in the subroutine...
fd input-file
is external.
01 input-record pic x(80).
procedure division.
read input-record.
display 'I like gerbils, and the record contains = '
input-record.
exit program.
Chris Mason
HCM··.@ix.··m.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
