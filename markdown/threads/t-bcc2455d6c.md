[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL ISAM / vs. Database

_1 message · 1 participant · 1997-12_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`VSAM, files, sorting`](../topics.md#files)

---

### COBOL ISAM / vs. Database

- **From:** "pa..." <ua-author-6589140@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<677c12$eg2@lotho.delphi.com>`

```

I have a nice little project here that I want to develop. Since
if it takes off (as I hope it does) it will be necessary to use the
system as a distributed database with periodic updates, my inclination
is to use a RDBMS (i.e. UDB version 5) to control the data.

I'm much better at SQL than I am at COBOL I'm afraid, but I need
procedural logic in the application(s). (They model workflow.)
Would it make sense to use the database as a transaction store
in this case, or would I be better off using the COBOL ISAM
stuff, and using a socket channel to do updating over the network
when necessary?

I know that I haven't provided near enough information about
this to make any kind of rational decision, but I'm really looking
for experience stories and whateverelse may.be.relevant to this
situation. Are there any really big "gotchas" to watch out for
here?

Thanks
-Paul
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
