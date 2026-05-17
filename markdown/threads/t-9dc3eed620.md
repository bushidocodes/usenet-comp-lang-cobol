[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 24 x 7

_2 messages · 2 participants · 1996-03_

---

### 24 x 7

- **From:** "dbret..." <ua-author-6588809@usenetarchives.gap>
- **Date:** 1996-03-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4i7c3a$m2j@newsbf02.news.aol.com>`

```
I have a question for some of you Hogan programmers that may be out there.
In the course of my work, I have heard that the Hogan deposit system is a
true 24 x 7 system (running 24 hours a day, 7 days a week). I am curious
how this is possible. I know that Hogan has both an online and batch
process, and I was wondering how the batch and online portions of the
system run at the same time, and still maintain data integrity.

Any insight you can give me would be appreciated.

Thanks.

Dave Bretz
```

#### ↳ Re: 24 x 7

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-03-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9dc3eed620-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4i7c3a$m2j@newsbf02.news.aol.com>`
- **References:** `<4i7c3a$m2j@newsbf02.news.aol.com>`

```
dbr··.@a··.com (DBretz0727) wrote:
› I have a question for some of you Hogan programmers that may be out there.
› In the course of my work, I have heard that the Hogan deposit system is a
…[9 more quoted lines elided]…
› Dave Bretz

I have never heard of the Hogan deposit system, but I support a 24 x 7
application on MVS with VSAM files and CICS and batch programming.

Basically, all the application files are mirrored. We have primary files
and secondary files. Normally the primary files are open and
online updates are written to the primary transaction log file.
Periodically during the day, a batch refresh job reads the
primary transaction log file and refreshes those updates to the
secondary application files.

A CICS transaction is used to quiesce the system to prevent
additional online updates. This task then refreshes the most
recent updates from the primary transaction log to the secondary files.
Then the primary files are closed and the secondary files left open.
Batch processing is performed against the primary files.

A batch file refresh is then run to read the secondary transaction log
file and apply updates to the primary application files. A second CICS
file refresh/switch is performed to refresh primaries from the
secondary transaction log, close secondaries, and leave primaries open.
Quiescing the system and switching the files in CICS does cause a service
outage that may last a minute or two. File switches are normally
scheduled between 1:00 AM and 6:00 AM when transaction volume is low.

You could try VSAM shareoptions (4 4), but you probably would not like
the response time. I'm sure this is not the only solution to this
particular problem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
