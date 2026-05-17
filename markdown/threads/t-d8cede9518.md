[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with protected mode

_3 messages · 2 participants · 1997-06_

---

### Problems with protected mode

- **From:** "andreas leber" <ua-author-17073237@usenetarchives.gap>
- **Date:** 1997-06-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc7773$e14a0440$ae50a2c2@heyne.plannet.de>`

```

Hello, dear collegues!

We are using micro focus visual cobol under DOS. We have changed our system
from real over to protected mode, and from CALL CHAIN to dynamic CALL. We
have testet the result for many weeks, it was all ok. Now, on just some
machines, we get memory problems. We can't yet find any systematics in
these problems; they seem to appear with different memory sizes,
DOS-versions, inside Win95-DOS-boxes, under DOS alone and so on.

Does anybody have experience with converting a system to protected mode?
Any hint, in what direction to search a solution?

We have no tool which could show us the complete usage of memory of our
programs. MEM of DOS shows only, how much the first started program uses,
and only conventional and upper memory, but not XMS. The following, called
programs don't appear in the listings of MEM.

Any hints about how to follow the requesting and releasing of memory
through our programs?

Secondly, we have the problem, that we can't call more than about 10
programs with dynamic CALL at the same time. Then again memory is finished.
How does the reservation of memory work with dynamically called programs?

I'd be very thankful for your help!

Andreas Leber
Programmer
Karlsruhe / Germany
```

#### ↳ Re: Problems with protected mode

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-06-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d8cede9518-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc7773$e14a0440$ae50a2c2@heyne.plannet.de>`
- **References:** `<01bc7773$e14a0440$ae50a2c2@heyne.plannet.de>`

```

In message <<01bc7773$e14a0440$ae5··.@hey··t.de>> "Andreas Leber" writes:
› 
› We are using micro focus visual cobol under DOS. We have changed our system
…[4 more quoted lines elided]…
› DOS-versions, inside Win95-DOS-boxes, under DOS alone and so on.

With Dynamic CALL you should CANCEL after the program is finished
with. Also, while the CALL is by file name the CANCEL is by
PROGRAM-ID. If the PROGRAM-ID does not match the file name (or
specifically the name used in the CANCEL) then the program will
lodge in memory.

It may be not so much running out of memory, but running into
some other limit, such as the CALLed name table.
```

##### ↳ ↳ Re: Problems with protected mode

- **From:** "andreas leber" <ua-author-17073237@usenetarchives.gap>
- **Date:** 1997-06-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d8cede9518-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d8cede9518-p2@usenetarchives.gap>`
- **References:** `<01bc7773$e14a0440$ae50a2c2@heyne.plannet.de> <gap-d8cede9518-p2@usenetarchives.gap>`

```



Richard Plinston schrieb im Beitrag
<329··.@kcb··n.nz>...
› In message <<01bc7773$e14a0440$ae5··.@hey··t.de>> "Andreas
› Leber"  writes:
…[19 more quoted lines elided]…
› 

Thanks a lot for your reply!
It's so difficult to control the memory consumption in protected mode
without good tools. In the moment I'm fighting more with some protection
faults which appear after a CHAINR-call to COMMAND.COM. I can't reconstruct
the former memory problems anymore.
Your hint about Cancel is very interesting. Nobody here has thought about
that. Just by
accident our Compile-and-Link-Batches handle such mistakes in a good way,
we would find
them at compile time. But interesting anyway.

Greetings,
- Andreas Leber
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
