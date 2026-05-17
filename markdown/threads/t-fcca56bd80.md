[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Split keys using non-contiguous fields in VMS Cobol - David Early

_2 messages · 2 participants · 1996-07_

---

### Split keys using non-contiguous fields in VMS Cobol - David Early

- **From:** "earlyd" <ua-author-17086419@usenetarchives.gap>
- **Date:** 1996-07-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4t6d6k$4jj@niamh.indigo.ie>`

```

Does anyone have the correct syntax for defining a key for an RMS file
which has several fields not contiguous. The online help suggests that
this is possible but the apparent syntax is incorrect.

I can get around it by using convert/fdl but doing this to multi-gigabyte
files is very time-consuming. Any help?

David Early - T.L.A. Computing
```

#### ↳ Re: Split keys using non-contiguous fields in VMS Cobol - David Early

- **From:** "fal..." <ua-author-15896936@usenetarchives.gap>
- **Date:** 1996-07-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fcca56bd80-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4t6d6k$4jj@niamh.indigo.ie>`
- **References:** `<4t6d6k$4jj@niamh.indigo.ie>`

```

earlyd wrote:

› Does anyone have the correct syntax for defining a key for an RMS file
› which has several fields not contiguous.

Here's the syntax.

identification division.
program-id. split.
environment division.
input-output section.
file-control.
select testfile assign "testfile.dat"
organization indexed access dynamic
record key mainkey = nname ddate.
data division.
file section.
fd testfile.
1 mainrec.
3 custno pic x(6).
3 nname pic x(25).
3 amtowed pic s9(7)v99.
3 ddate pic x(8).
procedure division.
begin.
open input testfile
move "George" to nname
move "19960701" to ddate
read testfile key is mainkey invalid key
display "Don't know about that one!"
end-read
close testfile
stop run.

Notes:
- The split key could be a secondary key.
- The "key is" clause in the read statement is not needed in this
example.
- Split keys are a Digital extension.
- This example is in terminal format.

George Trudeau, Systems Analyst, Town of Falmouth

"E-Mail so interesting, it doesn't need a tag line."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
