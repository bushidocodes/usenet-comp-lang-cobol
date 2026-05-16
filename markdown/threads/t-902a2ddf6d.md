[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is the equivalent function in Cobol

_4 messages · 4 participants · 1999-01_

---

### What is the equivalent function in Cobol

- **From:** "Pedro Tavares" <pedrotavares@cmvm.pt>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77kvs4$m8u$1@duke.telepac.pt>`

```
What's the equivalent  C function - fflush() in Cobol?
Thanks

Pedro Tavares
Lisbon, Portugal
```

#### ↳ Re: What is the equivalent function in Cobol

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369e1087.100818809@news.freeserve.net>`
- **References:** `<77kvs4$m8u$1@duke.telepac.pt>`

```
On Thu, 14 Jan 1999 14:49:14 -0000, "Pedro Tavares"
<pedrotavares@cmvm.pt> wrote:

>What's the equivalent  C function - fflush() in Cobol?

There isn't one. You don't need one. WRITE is all you need unless you
are doing something with a peculier compilers byte-stream I/O
functions perhaps.

What are you doing that you think you need to be sure that data has
been flushed from the buffers?
```

##### ↳ ↳ Re: What is the equivalent function in Cobol

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990125172955.21395.00002781@ng133.aol.com>`
- **References:** `<369e1087.100818809@news.freeserve.net>`

```
Actually 

   CLOSE filename.

should flush the buffers. And the syntax

    CLOSE ALL.

is available on most compilers.


In online environments you need to trigger a syncpoint to get the data
management subroutines to flush buffers (that will commit all i/o not just DASD
related).

Best Wishes

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: What is the equivalent function in Cobol

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ad508d.84935965@netnews>`
- **References:** `<369e1087.100818809@news.freeserve.net> <19990125172955.21395.00002781@ng133.aol.com>`

```
'Twas 25 Jan 1999 22:29:55 GMT, when rkrayhawk@aol.com (RKRayhawk)
illuminated comp.lang.cobol thusly:

>    CLOSE ALL.
>
>is available on most compilers.

It is?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
