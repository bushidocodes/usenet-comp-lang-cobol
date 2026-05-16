[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# No More Counting Lines of COBOL Code

_3 messages · 3 participants · 1999-08_

---

### No More Counting Lines of COBOL Code

- **From:** "editor" <editor@aboutlegacycoding.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tjxu3.5$3S5.413@client>`

```
Check out this free utility download for COBOL and cut the hassle of
counting lines of COBOL code.  It's called COBOL Record Sizer.   You copy
any COBOL record layout to the clipboard and this application will calculate
"the size in bytes" of the (largest) record found.

You'll find the down load at www.aboutlegacycoding.com/code1.asp
```

#### ↳ Re: No More Counting Lines of COBOL Code

- **From:** Dave Polzin <dlpolzin@coredcs.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BAB426.4A15@coredcs.com>`
- **References:** `<Tjxu3.5$3S5.413@client>`

```
** editor wrote:
** Check out this free utility download for COBOL and cut the hassle
** of counting lines of COBOL code.  It's called COBOL Record Sizer.  
** You copy any COBOL record layout to the clipboard and this
** application will calculate "the size in bytes" of the (largest)
** record found.

I must be really missing the point here.

First of all, record size has nothing whatsoever to do with lines of
COBOL code - code being defined as that which takes place in the
Procedure Division (or perhaps in the entire program source), not just
source lines in a record definition.

Second, on the right side of my compiles, the record length is already
defined by the compiler.  Including any ODO definitions.

So what do I need this utility for??  Beats me!

================================
Dave Polzin  <dlpolzin@coredcs.com>
================================
```

##### ↳ ↳ Re: No More Counting Lines of COBOL Code

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MOBu3.204$%93.12088@dfiatx1-snr1.gtei.net>`
- **References:** `<Tjxu3.5$3S5.413@client> <37BAB426.4A15@coredcs.com>`

```
Dave Polzin wrote in message <37BAB426.4A15@coredcs.com>...
>Second, on the right side of my compiles, the record length is already
>defined by the compiler.  Including any ODO definitions.
>
>So what do I need this [Progeni record sizing] utility  for??  Beats me!

1. You do not have a compiler listing handy.
2. Your compiler does not (was not directed to) produce a data map.
3. Your compiler is at work, you are at home.
4. You are developing and don't have enough to compile yet.
5. You need to copy the file to another media using some utility which
requires a record length, but you don't have access to a cobol compiler.
6. You are designing a new record type for a fixed-record-length file and
you want to add the correct number of FILLER bytes to the record.

So if *you* don't need it, maybe someone else does. I tried this and it's
pretty cool, although a tad limited.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
