[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL (Unix): are there tools to read EBCDIC files, tapes with COMP-3?

_3 messages · 3 participants · 1996-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### MF COBOL (Unix): are there tools to read EBCDIC files, tapes with COMP-3?

- **From:** "spk..." <ua-author-17071408@usenetarchives.gap>
- **Date:** 1996-12-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59fl8g$rbv@bogus.cts.com>`

```

We are doing a COBOL conversion from IBM MVS -to- DEC Alpha Unix
running MF COBOL. For testing, we need to be able to read EBCDIC files
(ftp'd to unix as binary) -- both EBCDIC PIC X fields and COMP-3 fields
occur in the records.
Now we can build COBOL programs that will read these, but in the
best of worlds, we would like a utility that would:
* read and interpret the FD COPY member (copybook)
* read the EBCDIC file
* output an ASCII record with COMP-3 fields converted to
ASCII PIC S9.....

Does MF toolkit (or other utilities) provide this capability, or
anything close to it?
Please post the reply, if possible. If you prefer, just email me.
Thanks!
-steve

Homepage at http://www.users.cts.com/crash/s/spkemp
```

#### ↳ Re: MF COBOL (Unix): are there tools to read EBCDIC files, tapes with COMP-3?

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-12-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d1ea94db-p2@usenetarchives.gap>`
- **In-Reply-To:** `<59fl8g$rbv@bogus.cts.com>`
- **References:** `<59fl8g$rbv@bogus.cts.com>`

```

Steve Kemp wrote:
› 
›         We are doing a COBOL conversion from IBM MVS -to- DEC Alpha Unix
…[11 more quoted lines elided]…
› anything close to it?

Hi Steve.

I don't know off the top of my head about any utilities/tools to do this
automatically, but you can certainly code a simple program to convert an
EBCDIC file to an ASCII one in MF COBOL.

Declare two similar files with the appropriate SELECT clauses ripped out
of
your existing program, and also rip the FD from your existing program
and
include it twice, once for each file.
In the input file (EBCDIC) FD, include the clause CODE-SET IS EBCDIC-CS
(where EBCDIC-CS is declared as an EBCDIC alphabet-name in
SPECIAL-NAMES).
You may or may not need to use the "FOR " clause.
In the ASCII FD, change those COMP-3's to PIC S9.... and simply READ
each
record from the input file, MOVE CORR the EBCDIC FD to the ASCII FD and
then WRITE the ASCII record.
The above assumes you have some sort of Micro Focus documentation and
can
look up the specific details about the stuff I've mentioned
(specifically,
the Language Reference manual - see the "Data Division/File Section"
part).

That'll convert a working file, but if you just want to read an EBCDIC
file
and output a report or something just MOVE the required fields from the
EBCDIC FD to wherever you want after reading each record - the fields
are
converted to ASCII.

Cheers, Kev.
```

#### ↳ Re: MF COBOL (Unix): are there tools to read EBCDIC files, tapes with COMP-3?

- **From:** "casey..." <ua-author-994183@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d1ea94db-p3@usenetarchives.gap>`
- **In-Reply-To:** `<59fl8g$rbv@bogus.cts.com>`
- **References:** `<59fl8g$rbv@bogus.cts.com>`

```

You might want to talk to the people at MSEN, for they have a utility that
converts from ASCII to Unix form. It's called bsd2dos or dos2bsd. Ask
them about it. in··.@ms··n.com is there contact address.
Computer Consultant: FoxPro 2.6 for Windows, MSC++ 7.0a SDK, Visual BASIC, COBOL-85, and others. INET: cas··.@a··.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
