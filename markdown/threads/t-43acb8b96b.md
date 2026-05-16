[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Index corruption in Microfocus

_1 message · 1 participant · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Index corruption in Microfocus

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81jv7c$gpt$4@aklobs.kc.net.nz>`
- **References:** `<81hr36$dl7$1@ssauraab-i-1.production.compuserve.com> <vh7p3sob1piae3kdd79vid47ib6k58n8g0@4ax.com>`

```

:>We've found that parts of the file can be read with 
:>the index but not others. I had hoped to drop the index (by 
:>erasing the idx file) and rebuild it, on the suspicion that the 
:>data in the dat file is okay. However the utilities seems not to 
:>be able to read the file at all once the index is erased. 

The .IDX file contains information on the key sizes and positions.
The REBUILD utility should work with a corrupted index (which
is what it is for actually), but may fail if the key information
is corrupt.  There are command line options for specifying the
record size, key size and position, and that the data file
should be copied to create a new file.

I have used this to recreate a file and index some time ago.

It may depend on the file format thugh as MF can create and use
several different indexed formats: Level II, BTrieve, C2.
Some combinations of format and other parameters seem not
to work.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
