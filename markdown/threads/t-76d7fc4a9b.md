[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help reading ".TXT" into MF cob program

_2 messages · 2 participants · 1997-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help reading ".TXT" into MF cob program

- **From:** "dba" <ua-author-534259@usenetarchives.gap>
- **Date:** 1997-11-28T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcfc8e$03a609e0$2c645ecf@dba.ix.netcom.com>`

```

I'm trying to read a ".TXT" file into my Cobol program. The book (which is
for a 2x version) tells me that I need to declare it as variable, but then
goes into a Header definition. In one section is says that the "FILE" has a
header while in another it states that each record has a header ??? Could
someone shed some light on this issues and if possible a small example?

Thanks...
```

#### ↳ Re: Help reading ".TXT" into MF cob program

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-76d7fc4a9b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcfc8e$03a609e0$2c645ecf@dba.ix.netcom.com>`
- **References:** `<01bcfc8e$03a609e0$2c645ecf@dba.ix.netcom.com>`

```

You don't say which computer, operating system or compiler you're using. But
".TXT" sounds like it might be DOS or Windows. In the DOS/Windows world,
text files are delimited by a carriage return and a line feed (0DH,0AH). In
Micro Focus COBOL (yours may be slightly different) you would use a text file
like this:

SELECT SAMPLE-FILE ASSIGN TO DISK
ORGANIZATION IS LINE SEQUENTIAL.

FD SAMPLE-FILE
VALUE OF FILE-ID IS "SAMPLE.TXT".
01 SAMPLE-RECORD ...

Input:
OPEN INPUT SAMPLE-FILE.

READ SAMPLE-FILE
AT END
...

CLOSE SAMPLE-FILE.

Output:
OPEN OUTPUT SAMPLE-FILE.

WRITE SAMPLE-RECORD.

CLOSE SAMPLE-FILE.

It is likely that the 'header' reference means a record placed at the front
or end of the file by your program, to store totals or control information.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

dba  wrote:
> I'm trying to read a ".TXT" file into my Cobol program.  The book (which is
> for a 2x version) tells me that I need to declare it as variable, but then
> goes into a Header definition. In one section is says that the "FILE" has a
> header while in another it states that each record has a header ??? Could
> someone shed some light on this issues and if possible a small example?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
