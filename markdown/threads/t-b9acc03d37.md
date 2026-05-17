[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol and Assembler combination slow (MVS)

_3 messages · 3 participants · 1998-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cobol and Assembler combination slow (MVS)

- **From:** "peter hartman" <ua-author-2159010@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd63d5$24a63c60$8e48e6a1@essdpch>`

```

We have a suite involving COBOL II rel 3 MVS cobol with a small assembler
utility in between. Without the assembler routine the job eats 5 CPU
seconds. With the assembler utility, the job eats 30 CPU seconds.

The assembler module only passes a couple of parameters and I have the
feeling the rununit is re-initialized each and every time. Strobe indicates
the assembler utility is using only 5% CPU so the majority is eaten by the
cobol library routines.

Does anybody have an idea where we could start searching for a solution ?

Thanks,
- Peter -
```

#### ↳ Re: Cobol and Assembler combination slow (MVS)

- **From:** "ken floyd" <ua-author-2409564@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9acc03d37-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd63d5$24a63c60$8e48e6a1@essdpch>`
- **References:** `<01bd63d5$24a63c60$8e48e6a1@essdpch>`

```

Have a look at the RETREUS parameter. I think it might help.

Peter Hartman wrote:

› We have a suite involving COBOL II rel 3 MVS cobol with a small assembler
› utility in between. Without the assembler routine the job eats 5 CPU
…[10 more quoted lines elided]…
›  - Peter -
```

#### ↳ Re: Cobol and Assembler combination slow (MVS)

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9acc03d37-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd63d5$24a63c60$8e48e6a1@essdpch>`
- **References:** `<01bd63d5$24a63c60$8e48e6a1@essdpch>`

```


Peter Hartman wrote in message <01bd63d5$24a63c60$8e48e6a1@essdpch>...
› We have a suite involving COBOL II rel 3 MVS cobol with a small assembler
› utility in between. Without the assembler routine the job eats 5 CPU
…[11 more quoted lines elided]…
› 

Another post mentioned RTEREUS, but what you really need to do is check out
the section on setting up a COBOL run-time environment (from your Assembler
driver). There are a variety of approaches available. I think that using
either ILBOSTP0 or IGZERRE is preferable (in your case) to using RTEREUS.

You said that you are using VS COBOL II (rather than COBOL for OS/390 & VM).
I hope you are looking at upgrading soon, but in case you aren't, the place
you should look is in your Programming Guide. I can't reach the online dox
at the moment, so I suggest you look at your manual and check the index for
"IGZERRE" and that should put you in the right place. Let me know if you
have a problem finding this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
