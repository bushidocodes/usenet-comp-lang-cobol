[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Improved Comb Sort with pre-defined gap table

_1 message · 1 participant · 2001-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Improved Comb Sort with pre-defined gap table

- **From:** jdveale@world.std.com (James D. Veale)
- **Date:** 2001-07-25T08:02:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GH0ro0.Lr2@world.std.com>`

```
The April 1991 edition of Byte Magazine described a "comb sort"
by Stephen Lacey and Richard Box.  The sort described was easy to
code, worked well with random number sequences,  and had an "N log(N)"
growth characteristic with execution times close to that of a heap
sort.

Although the original comb sort generally works well,  it is
vulnerable to seriously degraded performance with certain repetitive
input sequences. The improved comb sort uses a pre-defined gap table
and results in the following:

   - Effectively eliminates turtles for random input sequences.

   - Limits the worst case performance for repetitive input sequences
     to about twice that of normal sequences, as well as substantially
     reducing vulnerability to repetitive input sequences.

   - Slightly worse than N log(N) execution growth with increasing N.

For more details see:

     http://world.std.com/~jdveale/combsort.htm

     Sorry the pseudo-code isn't in a cobol style.  A newsgroup
     and web search produced a number of hits in the cobol community,
     so I thought it might be of interest.

NOTE: This message is a technical note to a technical community
about an algorithm I've found very useful for nearly a decade.
It addresses a recently encountered weakness which is apparently
not well known.
----------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
