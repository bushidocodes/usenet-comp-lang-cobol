[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol RT Error 173

_5 messages · 4 participants · 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol RT Error 173

- **From:** "joe howell" <ua-author-15620784@usenetarchives.gap>
- **Date:** 1997-01-22T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32E8618E.7975@gnt.net>`

```

I have just started getting a 173 at weird times while
testing an app I am developing. Book says that directory/file
does not exist, but it does. I can successfully call it from
other programs. I seem to remember way back that Linkcount
would help this problem.

Here is a sample of what is happening...

Prog A
call "prog B" using xxx

Prog B works fine....

Prog C
call "prog D"
prog D calls Prog E
prog E calls Prog B - fails RT Error 173 - file not found

Any ideas??


 Joe Howell, HIS COmpany                       904-678-3238
 PO Box 73                                     904-678-7378
 Valparaiso ("The Valley Of Paradise"), Florida, USA  32580
```

#### ↳ Re: MF Cobol RT Error 173

- **From:** "joe howell" <ua-author-15620784@usenetarchives.gap>
- **Date:** 1997-01-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f9a7820abe-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32E8618E.7975@gnt.net>`
- **References:** `<32E8618E.7975@gnt.net>`

```

Joe Howell wrote:
›
› I have just started getting a 173 at weird times while
› testing an app I am developing. Book says that directory/file
›

I'm answering my own question, but thought I would post it to
the newsgroup in case someone else has this problem.

I moved my MF Cobol/Dos/Win 3.2.27 to a Win 95 environment. All
worked fine, so I have been developing for a good while before this
problem came up. When my config.sys file was cleaned out, the files
and buffers statements were removed. I added these back, and the 173
problem went away. (the clue was that finally I got a 14 error- too
many files open.

Hope this helps someone else. -:)
 Joe Howell, HIS COmpany                       904-678-3238
 PO Box 73                                     904-678-7378
 Valparaiso ("The Valley Of Paradise"), Florida, USA  32580
```

#### ↳ Re: MF Cobol RT Error 173

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-01-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f9a7820abe-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32E8618E.7975@gnt.net>`
- **References:** `<32E8618E.7975@gnt.net>`

```

In message <<32E··.@g··.net>> Joe Howell writes:

› prog E calls Prog B - fails RT Error 173 - file not found
›
› Any ideas??

Put FILES=100 in CONFIG.SYS.
```

#### ↳ Re: MF Cobol RT Error 173

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-01-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f9a7820abe-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32E8618E.7975@gnt.net>`
- **References:** `<32E8618E.7975@gnt.net>`

```

Joe,

You are likely running out of memory. The MF RTS sometimes reports the 173
(Not found). It is even MORE likely that you have run out of File handles,
which ALWAYS reports back a 173. Increase the FILES= statement in your
CONFIG.SYS.


Joe Howell wrote in article <32E··.@g··.net>...
› I have just started getting a 173 at weird times while 
› testing an app I am developing.  Book says that directory/file
…[23 more quoted lines elided]…
›
```

#### ↳ Re: MF Cobol RT Error 173

- **From:** "fernando kvistgaard" <ua-author-6588930@usenetarchives.gap>
- **Date:** 1997-01-28T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f9a7820abe-p5@usenetarchives.gap>`
- **In-Reply-To:** `<32E8618E.7975@gnt.net>`
- **References:** `<32E8618E.7975@gnt.net>`

```

It seems to be a memory problem.

Have tried "on exception"?


Joe Howell wrote in article <32E··.@g··.net>...
› I have just started getting a 173 at weird times while 
› testing an app I am developing.  Book says that directory/file
› does not exist, but it does.  I can successfully call it from
› other programs.  I seem to remember way back that Linkcount 
› would help this problem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
