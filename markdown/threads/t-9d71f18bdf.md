[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using VAX COBOL to create mailbox

_2 messages · 2 participants · 1998-01_

---

### Using VAX COBOL to create mailbox

- **From:** "j.no..." <ua-author-17074115@usenetarchives.gap>
- **Date:** 1998-01-23T12:17:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<885575822.145096712@dejanews.com>`

```

Does anyone have a sample VAX COBOL program pair that does the
following:

MAILBOX WRITER
1. Create a mailbox using SYS$CREMBX
2. Write a message to the mailbox using SYS$QIO(W)

MAILBOX READER
3. Read the mailbox message created above using SYS$QIO(W)

Thanks in advance

John Nogueira
Computer Programmer
The Board of Education for the City of London
London, Ontario, Canada

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Using VAX COBOL to create mailbox

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9d71f18bdf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<885575822.145096712@dejanews.com>`
- **References:** `<885575822.145096712@dejanews.com>`

```

In article <885··.@dej··s.com>,
j.n··.@lbe··n.ca wrote:
› 
› Does anyone have a sample VAX COBOL program pair that does the
…[7 more quoted lines elided]…
› 3.  Read the mailbox message created above using SYS$QIO(W)

I started out to answer this and was trying to explain why it's the
reader that should be creating the mailbox when I realized that it would
take two or three hundred lines, and I'd rather go home.

When someone has a question about how to do X in language Y, it's not
always clear whether it should be posted in newsgroup X or newsgroup Y.
Sometimes people get quite heated about things they consider off-topic,
and sometimes as a result you don't get an answer in either newsgroup.

I don't think you were wrong to ask this question here, but I do think it
would be worth your while to try comp.os.vms. For one thing, there are
lots more people there, so your chances are better. Even if you can only
get an answer in C, it's trivial to translate into CoBOL. I hope your
next question hits me on a better day :)


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
