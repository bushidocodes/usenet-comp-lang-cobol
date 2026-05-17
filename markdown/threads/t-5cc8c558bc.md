[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL 3.2 using "CHAIN" command

_3 messages · 3 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL 3.2 using "CHAIN" command

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998072019442300.PAA04123@ladder03.news.aol.com>`

```
Good Afternoon,

Could i get some input as to the positive and negative impact of using the
"CHAIN" command to pass control from program to program as opposed to using the
"CALL" command from a central program.

Thanks,

Bob Hennessey
```

#### ↳ Re: MF COBOL 3.2 using "CHAIN" command

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cc8c558bc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998072019442300.PAA04123@ladder03.news.aol.com>`
- **References:** `<1998072019442300.PAA04123@ladder03.news.aol.com>`

```
› "CHAIN" command to pass control from program to program as >opposed to
› using the
› "CALL" command from a central program.

The chain command is really a high level GO TO, while
the call really is a CALL. Does that and the phrase "top down
structured code" clarify matters? ;<)
```

#### ↳ Re: MF COBOL 3.2 using "CHAIN" command

- **From:** "kfl..." <ua-author-17084597@usenetarchives.gap>
- **Date:** 1998-07-22T10:53:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cc8c558bc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1998072019442300.PAA04123@ladder03.news.aol.com>`
- **References:** `<1998072019442300.PAA04123@ladder03.news.aol.com>`

```
I've used the CHAIN a time or two. We had a 'Starter' program that had
initiated a session for System 'A' with an operator. The 'starter' would
then call a System 'A's Driver program. The operator would then converse
back and forth with System A. Many programs would have been called, screens
sent back and forth, etc. Eventually, we'd return back to the original
'starter' program with a request to transfer to System 'B'. So we used a
CHAIN to free up resources that a plain CALL wouldn't. It worked well for
us.

In article <199··.@lad··l.com>,
bob··.@a··.com (Bob7536) wrote:
› Good Afternoon,
› 
…[9 more quoted lines elided]…
› 

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
