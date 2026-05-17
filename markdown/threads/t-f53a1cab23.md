[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read another record based on condition

_3 messages · 3 participants · 1998-02_

---

### Read another record based on condition

- **From:** "sbouc..." <ua-author-16821643@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980213210001.QAA21998@ladder02.news.aol.com>`

```

There are certain records whic have a 'x' in a particlular position defined in
the input record as flag. If an x appears in this position we want to read the
next record. Is this just a simple if statement ?

Input-Rec
Input-fields pic
Flag pic x

Read-it
If Flag equal 'X' perform Read-it
```

#### ↳ Re: Read another record based on condition

- **From:** "don eakin" <ua-author-2567354@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f53a1cab23-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980213210001.QAA21998@ladder02.news.aol.com>`
- **References:** `<19980213210001.QAA21998@ladder02.news.aol.com>`

```

you could also say, if flag is not eual to 'x' perform do-not-read-it.
```

#### ↳ Re: Read another record based on condition

- **From:** "mike salter" <ua-author-17071840@usenetarchives.gap>
- **Date:** 1998-02-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f53a1cab23-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19980213210001.QAA21998@ladder02.news.aol.com>`
- **References:** `<19980213210001.QAA21998@ladder02.news.aol.com>`

```



SBouc16898 wrote in article
<199··.@lad··l.com>...
› There are certain records whic have a 'x' in a particlular position
› defined in
…[10 more quoted lines elided]…
› 

How about something like:

PERFORM READ-IT UNTIL FLAG <> 'X' OR INPUT-AT-END.

READ-IT.
READ INPUT-FILE
AT END
MOVE SPACES TO INPUT-REC
MOVE 'Y' TO INPUT-AT-END-SW
END-READ.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
