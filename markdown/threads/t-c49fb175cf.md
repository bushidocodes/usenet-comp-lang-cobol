[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# REDEFINES STATEMENT (LONGISH)

_4 messages · 4 participants · 1999-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### REDEFINES STATEMENT (LONGISH)

- **From:** "Teresa A. Robinson" <trobinson@wworld.com>
- **Date:** 1999-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d094da@news.wworld.com>`

```
If you are using the following input layout:
Department    xxx
Course            9999
Section            999
with alphanumeric, and numeric as shown, can you do this and will it work?
08   t-course               pic x(10).
                       08   us-string redefines t-course.
                               10  us-dept           pic xxx.
                                10  us-course       pic 9999.
                                 10  us-section      pic 999.
The 3 elements come in separately, must be strung together, loaded into a
variable length table and sorted.  Then they must be compared to another
input file to compare the department numbers for a match.  If they match a
counter must be incremented for 5 class levels (2 dimensional), if not an
error line is to be written with the bad info.  After the file is read and
the table complete, and unstringing the elements again, the table is finally
printed out with control breaks on the department.  I can't get it to work.
I think it is hanging up on the search all module during the process and
never gets to printing the table.  It is printing the data twice in
succession and all the data is coming out as errors.  That is probably why
the table doesn't print, it thinks it is done.  It has no flagged
statements, but is still wrong.  I had the above data as all alphanumeric
but wondered if the above will work.  I don't know how to read the
diagnostics to help locate where it bombed.  If anyone can help I would
certainly appreciate it!  Thanks in advance!
```

#### ↳ Re: REDEFINES STATEMENT (LONGISH)

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37D1093F.BAEF12E@ix.netcom.com>`
- **References:** `<37d094da@news.wworld.com>`

```
Without source code to see, diagnostics is at best difficult. Have you verified
that your table is sorted as specified by the 'ASCENDING'  key clause. This
clause only tells the compiler you expect your data to be in the correct order.
Another possibility is that you have not set  a value for the DEPENDING object.
There are a couple of ways to handle this:

One is to  set the DEPENDING object to the maximum value in the beginning of the
program (or using a value clause in working storage). Then, after the table has
been loaded, move the number of occurrences to the DEPENDING object.

A second method is to initialize  the DEPENDING object to zero  in the beginning
of the program and then increment the DEPENDING object before adding an element
to the table.

A third, (my preference) is to avoid the use of variable tables altogether in
working storage. It only adds to program complexity, execution overhead, and
saves no storage, since the compiler must allocate sufficient storage for the
maximum possible size anyway.

Your code snippet is correct, but here is an alternative which uses a group and
no redefines.  Both are (almost) equivalent (group level vs. alphanumeric).
08   t-course.
      09   us-string.         *> not really necessary, but included to use all
the names.
          10  us-dept           pic xxx.
           10  us-course       pic 9999.
           10  us-section      pic 999.

If you need additional help, pls send/post your source code.

Regards,
John


"Teresa A. Robinson" wrote:

> If you are using the following input layout:
> Department    xxx
…[22 more quoted lines elided]…
> certainly appreciate it!  Thanks in advance!
```

#### ↳ Re: REDEFINES STATEMENT (LONGISH)

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1999-09-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qslrc$2qg_002@news.netdirect.net>`
- **References:** `<37d094da@news.wworld.com>`

```
In article <37d094da@news.wworld.com>,
   "Teresa A. Robinson" <trobinson@wworld.com> wrote:
+If you are using the following input layout:
+Department    xxx
+Course            9999
+Section            999
+with alphanumeric, and numeric as shown, can you do this and will it work?
+08   t-course               pic x(10).
+                       08   us-string redefines t-course.
+                               10  us-dept           pic xxx.
+                                10  us-course       pic 9999.
+                                 10  us-section      pic 999.

The REDEFINES is legal, but completely unnecessary.
08 t-course.
   10 us-dept          pic xxx.
   10 us-course        pic 9999.
   10 us-section       pic 999.
will produce the desired result. By definition, *all* group items (such as
t-course) are treated as alphanumeric; thus, t-course is by default pic x(10).
```

#### ↳ Re: REDEFINES STATEMENT (LONGISH)

- **From:** bpkprsnl@erols.dot.com (Boris)
- **Date:** 1999-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d6ce4a.2161905@news.erols.com>`
- **References:** `<37d094da@news.wworld.com>`

```
Teresa,

Folks here are more than willing to help, but for homework problems most of us
would appreciate it if you identified that its homework in the subject and show
what you have figured out so far on your own.

Good luck.

PS:  All COBOL questions should reference the platform and dialect of COBOL in
use.


On Fri, 3 Sep 1999 22:44:13 -0500, "Teresa A. Robinson" <trobinson@wworld.com>
wrote:

<a homework problem>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
