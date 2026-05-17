[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# *** NEED HELP WITH MF 3.1.35 - REBUILD FACILITY ***

_1 message · 1 participant · 1996-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### *** NEED HELP WITH MF 3.1.35 - REBUILD FACILITY ***

- **From:** "dt..." <ua-author-7376421@usenetarchives.gap>
- **Date:** 1996-11-22T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<575gd3$n24@camel1.mindspring.com>`

```

Hello all. Here's my situation. I have "old" data files that were
created using MF 2.4.38 (indexed - variable length files). I have
ported the program files over to MF 3.1.35 and re compiled them under
that version. The new program files can read, write, and rewrite to
the "old" data files without a problem (as one of the supplied
documents stated the 3.1.35 EXTFH could do). Now, when I run a
REBUILD on one of those data files, it rebuilds the .IDX just fine,
but now, I can't seem to write to that rebuilt data file! I get a
status 9/ 07 (which is Disk Full - Drive limit exceeded); I have 200
megs free and then some ... so that's not it.

I have tried various combinations of compiler directives (including
the IDXFORMAT"2"), and nothing seems to change this strange error.

Special Notes:
* The problem only occurs if I REBUILD the index. If I reorganize the
data file (using the input-file, output-file), this error goes away.

* I don't have this problem with ALL my indexed variable length data
files. Only one of them seems to get this error (nothing fancy about
the data file either).

* After the rebuild, I can read the data file without a problem

* If I DON'T rebuild the data file, I can Read, Write, Rewrite, and
delete without a problem (think I already said this)

Hope that covers it. If you've run into this before, please let me
know. I'd rather NOT have to reorganize the data files because some
of them exceed 100 megs and using the input-file, output-file requires
the user to have that amount of free space to create the new data
file. (end users, can't live with 'em, can't delete 'em ... oh well).

D.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
