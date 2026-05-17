[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol 74 help

_3 messages · 3 participants · 1998-04_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Cobol 74 help

- **From:** "grea..." <ua-author-463939@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998040219500200.OAA10097@ladder01.news.aol.com>`

```

I have a question on a program that I am writing on an older version of RM
Cobol 74 off an NCR box.

I am trying to write a file to disk. The file only contains one record, this
record is approx. 1000 characters long. When the program tries to write the
record, I get an "I/O error 97/00" Which translates into invalid record
length.

My question is this, what is the record size limit for writing a record to
disk? I assumed it would be much higher than 1000 characters, but I could be
wrong.

Secondly, are there any suggestions to resolving the problem.

Thank you

Darren O'Neill gre··.@a··.com
```

#### ↳ Re: Cobol 74 help

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc94d6f6e3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998040219500200.OAA10097@ladder01.news.aol.com>`
- **References:** `<1998040219500200.OAA10097@ladder01.news.aol.com>`

```

Great Nitz wrote:
› 
› I have a question on a program that I am writing on an older version
…[11 more quoted lines elided]…
› Secondly, are there any suggestions to resolving the problem.

First, please be aware that this version of RM/COBOL has not been
supported for several years. But in the spirit of "just this once"...

Are you writing a sequential file? If so, any binary data (i.e. not
ASCII text) will cause a 97 error. So, do you have COMP-6, COMP, COMP-1
or COMP-3 data in the file? If so, this is most likely the problem.

Otherwise, please provide the appropriate sections of the program...

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

#### ↳ Re: Cobol 74 help

- **From:** "jcj..." <ua-author-1139539@usenetarchives.gap>
- **Date:** 1998-04-04T10:41:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc94d6f6e3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1998040219500200.OAA10097@ladder01.news.aol.com>`
- **References:** `<1998040219500200.OAA10097@ladder01.news.aol.com>`

```

gre··.@a··.com (Great Nitz) wrote:

› I am trying to write a file to disk.  The file only contains one record, this
› record is approx. 1000 characters long.  When the program tries to write the
› record, I get an "I/O error 97/00"  Which translates into invalid record
› length.
› 

Could the actual record length not agree with your record contains
clause in the FD? My experience with RM Cobol (several years ago)
was that the calculated record length and the record contains clause
had to agree or you got a compile-time error, so I'm probably just
having a senior moment. My concern is that you stated the reclen
is *approx* 1K.
James.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
