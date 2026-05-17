[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Difference between I-O and EXTEND clause in the OPEN statement

_3 messages · 3 participants · 1998-04 → 1998-05_

---

### Difference between I-O and EXTEND clause in the OPEN statement

- **From:** "as..." <ua-author-567058@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6id889$s9n@freenet-news.carleton.ca>`

```


What is the difference between the two statements in COBOL?

OPEN EXTEND INVENTORY-FILE

and

OPEN I-O INVENTORY-FILE

>From my understanding, both allow you to read and write to the same file.

Thanks
```

#### ↳ Re: Difference between I-O and EXTEND clause in the OPEN statement

- **From:** "jcj..." <ua-author-1139539@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-94c4fde8e7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6id889$s9n@freenet-news.carleton.ca>`
- **References:** `<6id889$s9n@freenet-news.carleton.ca>`

```

› What is the difference between the two statements in COBOL?
› 
…[7 more quoted lines elided]…
› 
Not so. A file opened for EXTEND means you are adding records to
a file that already exists. That file must be ACCESS IS SEQUENTIAL.

A file opened for I-O must be ACCESS IS DYNAMIC or ACCESS IS
RANDOM. I-O mode allows you to write, rewrite, and delete records.

James.
```

#### ↳ Re: Difference between I-O and EXTEND clause in the OPEN statement

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-05-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-94c4fde8e7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6id889$s9n@freenet-news.carleton.ca>`
- **References:** `<6id889$s9n@freenet-news.carleton.ca>`

```

In article <6id889$s.··.@fre··n.ca>,
Sean Smith wrote:
› 
› What is the difference between the two statements in COBOL?
…[8 more quoted lines elided]…
› 

Do your own homework, please.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
