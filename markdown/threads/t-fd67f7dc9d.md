[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Merge statement

_2 messages · 2 participants · 1997-05_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Merge statement

- **From:** "james o. hart" <ua-author-13465525@usenetarchives.gap>
- **Date:** 1997-05-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc5cf2$03c4c740$74146bce@hartj>`

```

Hello, I'm a student at Oregon Institute of Technology and Currently taking
the PLI
class. I'm working on the last program and must use a MERGE statement to
merge and sort two files. The book we're using basically says the
statement is the same as the sort but must have two files in the using
portion.

My code is attached.

Any suggestions or maybe a good explanation of how the merge statement
works would be appreciated.

I'm using MicroFocus compiler.

Thanx in advance.
[uuencoded file 'Lab1.cbl' removed: 0.1 KB]
```

#### ↳ Re: Merge statement

- **From:** "stu9..." <ua-author-584048@usenetarchives.gap>
- **Date:** 1997-05-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd67f7dc9d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5cf2$03c4c740$74146bce@hartj>`
- **References:** `<01bc5cf2$03c4c740$74146bce@hartj>`

```

In article <01bc5cf2$03c4c740$74146bce@hartj>, "James O. Hart" wrote:
› Hello, I'm a student at Oregon Institute of Technology and Currently taking
› the PLI
…[12 more quoted lines elided]…
› Thanx in advance.
I am a student at Grove City College and I just finished the COBOL class here.
I think I can help but I can not guarantee that this will be perfect. Well,
here goes.............

This is your MERGE STATEMENT

MERGE UNSORTED-FILE1
ASCENDING KEY SR-LAST-NAME1
ASCENDING KEY SR-FIRST-NAME1
ASCENDING KEY SR-MI1
USING UNSORTED-FILE2
GIVING EMPLOYEE-FILE

I think that your code should appear more like this...
MERGE SOME-NEW-FILE
ASCENDING KEY SR-LAST-NAME1
ASCENDING KEY SR-FIRST-NAME1
ASCENDING KEY SR-MI1
USING SORTED-FILE1
SORTED-FILE2
GIVING EMPLOYEE-FILE.

First of all SOME-NEW-WORK file must be defined as an SD entry. Both
the SORTED-FILE1 and SORTED-FILE2 are FD enrties and appear in a SELECT
statement and MUST be sorted already and have identical record layouts.
Also, none of the files specified can be open at the time of the MERGE.
The MERGE statement will open and close all the files needed.

Basically a merge is the same as a sort only that a merge goes on
assumption that the files being merged are in order already.

Please write me back and tell me how it went. I hope what I told you is
useful.

Chad
stu··.@g··.edu
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
