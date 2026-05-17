[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL TRACE

_2 messages · 2 participants · 1997-10_

---

### COBOL TRACE

- **From:** "ru..." <ua-author-13489737@usenetarchives.gap>
- **Date:** 1997-10-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62gon6$lho$1@news.utdallas.edu>`

```

Hi,
Im using Micro Focus COBOL for UNIX V3.2 revision 031 on HP-UX B.10.01 A 9000/829.
I'm using the TRACE option - adding "READY TRACE" at the beginning of the program
and compiling with flag TRACE - so when the program runs it prints each label it reaches.

I don't want to have the printing of the display all the time, so can I have an environemtn variable
that will do it for me - i.e. compile ot once , and changing the environment variable to print
or not to print the labels.

Thanks , Doron (dv8··.@sbm··c.com)
```

#### ↳ Re: COBOL TRACE

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-10-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d77c6fa2a0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<62gon6$lho$1@news.utdallas.edu>`
- **References:** `<62gon6$lho$1@news.utdallas.edu>`

```

ru··.@utd··s.edu wrote:
› 
› Hi,
…[6 more quoted lines elided]…
› or not to print the labels.

Hi.

Of course you can. The "READY TRACE" is what actually switches the
label printing on ("RESET TRACE" switches it off again). Therefore,
get the value of the environment variable ("DISPLAY UPON
ENVIRONMENT-NAME", "ACCEPT FROM ENVIRONMENT-VALUE" syntax) and
put your "READY TRACE" in a condition.

Alternatively, use the COBOL switch mechanism (See the SPECIAL-NAMES
paragraph documentation in your Language Reference guide) and do a
similar condition.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
