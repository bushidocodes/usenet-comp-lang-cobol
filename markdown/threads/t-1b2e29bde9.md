[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Create a data file

_2 messages · 2 participants · 1996-06_

---

### Create a data file

- **From:** "9384..." <ua-author-795181@usenetarchives.gap>
- **Date:** 1996-06-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4qe1vf$kpi@ctylnk.cityu.edu.hk>`

```

Dear all,
I am writing a simple cobol program but I don't know
how to create the data file. Some books list example using
an existing file to create a new file. What I want is to
create a data file from the user (just key in data from key-
broad). I am using cobol in UNIX environment. Please give me
advice.

Thank in advance.
```

#### ↳ Re: Create a data file

- **From:** "hhof..." <ua-author-17086193@usenetarchives.gap>
- **Date:** 1996-06-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b2e29bde9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4qe1vf$kpi@ctylnk.cityu.edu.hk>`
- **References:** `<4qe1vf$kpi@ctylnk.cityu.edu.hk>`

```

938··.@cpc··u.hk (patrick) wrote:

› Dear all,
› I am writing a simple cobol program but I don't know 
…[4 more quoted lines elided]…
› advice.
 
› Thank in advance.

For simple sequential files, (printfiles, workfiles) it is sufficient
to just OPEN the file for OUTPUT. If you don't want to lose the
contents of the file you want to create then OPEN the file for EXTEND.

For Indexed files things could be a but more complicated and could
depend on the COBOL implementation you are using. Some COBOL versions
allow the same method. Just opening the Indexed file for OUTPUT will
create the physical file. Some other COBOL versions depend on the
database tools provided to create and design your ISAM files.

So look at your COBOL manual for more details on how to create your
index files, with your sequential files you should have no problems.

Good luck
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
