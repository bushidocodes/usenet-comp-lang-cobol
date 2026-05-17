[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

_7 messages · 5 participants · 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "douglas h. troy" <ua-author-17073163@usenetarchives.gap>
- **Date:** 1997-01-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`

```

I think I already know the answer to this one, but I figured that I would
ask anyways. I want to use a "newer" version of the MF compiler (3.1.35)
but without converting any data files (wait, that's not the punch line).
The data files were created under 2.4.38, so I figured, if I setup the new
compiler, but link in the "old" EXTFH.OBJ file to the final executable,
that it just might work. Ok, so there's got to be more to it than that ...
but does anyone have any idea if this is even remotely feasible or not.
(ok, you can start laughing now).

Thanks for your input and for not laughing too hard (I did when I thought
of this, but yeah ... you never know until you try).
D.

dt··.@drs··e.com
```

#### ↳ Re: Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "scott warren" <ua-author-939265@usenetarchives.gap>
- **Date:** 1997-01-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee3fefb918-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`
- **References:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`

```

I don't think linking in the old extfh is a good idea.
What about the Micro Focus rebuild utility for the new compiler.
You can give the rebuild program you key layout and it recreates the idx
file.





Douglas H. Troy wrote:
› 
› I think I already know the answer to this one, but I figured that I would
…[12 more quoted lines elided]…
› dt··.@drs··e.com
```

##### ↳ ↳ Re: Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "javier medina" <ua-author-13463924@usenetarchives.gap>
- **Date:** 1997-01-23T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee3fefb918-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ee3fefb918-p2@usenetarchives.gap>`
- **References:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com> <gap-ee3fefb918-p2@usenetarchives.gap>`

```

do you know where i can get a free or really inexpensive compiler for a
beginner for DOS or Windows? please ask around. thanks.

j.m.
```

#### ↳ Re: Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "jamie burks" <ua-author-6589396@usenetarchives.gap>
- **Date:** 1997-01-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee3fefb918-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`
- **References:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`

```

The file formats are supposed to be compatible so you should be able to
use the 3.1 EXTFH. At least that's what MF says. I have seen instances
where 2.x files are not readable under 3.x. If your files don't use
data or key compression, you should be fine. I would suggest running a
rebuild in them first.

Jamie Burks
Email: jgb··.@fe··x.com
Phone: 901-922-4472
```

##### ↳ ↳ Re: Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "douglas h. troy" <ua-author-17073163@usenetarchives.gap>
- **Date:** 1997-01-22T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee3fefb918-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ee3fefb918-p4@usenetarchives.gap>`
- **References:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com> <gap-ee3fefb918-p4@usenetarchives.gap>`

```

Jamie:

Well, they are supposed to be compatible, but I discovered that after
rebuilding
the index on one of our data files, that I could no longer add data records

(received disk full errors). Now, I didn't run the rebuilds with an
input/output, I
just recreated the index itself. Running the rebuild with the
input/output specified
fixes this record adding problem, but I can't have our clients do this
(many don't
have enough HD space for the output file).

Let me know if you have any other ideas.
Thanks.
D.


Jamie Burks wrote in article
<32E··.@fe··x.com>...
› The file formats are supposed to be compatible so you should be able to
› use the 3.1 EXTFH.  At least that's what MF says.  I have seen instances
…[8 more quoted lines elided]…
›
```

#### ↳ Re: Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "john noland" <ua-author-15410449@usenetarchives.gap>
- **Date:** 1997-01-20T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee3fefb918-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`
- **References:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com>`

```



Douglas H. Troy wrote in article
<01bc0559$13b839c0$527··.@MyC··g.com>...
› I think I already know the answer to this one, but I figured that I would
› ask anyways.  I want to use a "newer" version of the MF compiler (3.1.35)
…[7 more quoted lines elided]…
› (ok, you can start laughing now).

Doug,

I went from Micro Focus Version 1.1.17(Run Time Version 2.1) of the
compiler to version 3.1.31 with no difficulty. I had to rebuild the
occasional index, but that was about it. The only reason I even had to do
that was because the new version catches some problems that the old system
ignored. I was able to maintain my data files as they were with no
conversion whatsoever. You should be in even better shape coming from
Version 2.4.28. No need to waste your time and try to fix a problem that
doesn't exist! Although you can if you want, especially considering you're
e-mail address indicates you work for one of my competitors.:-)

John
```

##### ↳ ↳ Re: Micro Focus 2.4.38 EXTFH and Micro Focus 3.1.35 compiler

- **From:** "douglas h. troy" <ua-author-17073163@usenetarchives.gap>
- **Date:** 1997-01-22T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ee3fefb918-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ee3fefb918-p6@usenetarchives.gap>`
- **References:** `<01bc0559$13b839c0$527679a8@MyComputer.mindspring.com> <gap-ee3fefb918-p6@usenetarchives.gap>`

```

John:

Well, I already tried the "simple" recompile all the source under 3.1.35
and rebuild the data files.
No problems there ... UNTIL you try to add another record to one of the
indexed data files that was
rebuilt. The compiler returns a disk full error. Unfortunately, this
seems to only happen
on SOME of the indexed files, but not all. No data compression is being
used, it's not a duplicate key
issue, and if I run the rebuilds with a input file/output file, it corrects
the problem. I can't ask our client's
to do this, however, because (1) it would be a support nightmare (over 2000
clients) and (2) many of
these doctor's are still using 80286 computers (as if they couldn't afford
to buy new ones) with a 100 meg
Hard disk and a 60+ meg charge file (no room for the output file...).

So, that's why I can't use the MF 3.1.35 EXTFH. God I love programming.

D.

P.S.
What company do you work for?


John Noland wrote in article
<01bc0744$6aecb6c0$394e9ecf@default>...
› 
› 
…[31 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
