[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM - solution from 2006

_1 message · 1 participant · 2008-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM - solution from 2006

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-11-26T17:04:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<492D8194.6F0F.0085.0@efirstbank.com>`

```
Hi Andreas,

I asked a similar question on the ibm-main listserv just the other day.  A
reply I got seems quite similar to your idea:

"This can be solved by writing a COBOL routine named DSNHLI that does 
nothing but call DSNHLI dynamically. Link this routine statically into all
of your 
application programs. At runtime, the //STEPLIB needs to concatenate the 
library containing the stub of the corresponding environment. 
A similar approach should work for EZASOKET."

I don't actually have DB2 for z/OS yet (we are considering migrating from
VSE to z/OS, but we haven't purchased DB2 for z/OS yet), so I can't test it.
 Are saying that you have in fact tested it and it in fact does work?  If
so, that is good news indeed.

Still I have to wonder why IBM doesn't address this issue directly.  It
seems to me that, even if you stick with static calls of the DSN stub in the
Cobol program, that stub should simple dynamically call the correct module. 
Which is exactly what this workaround seems to be doing.

In any case, I look forward to trying this solution when the time comes.

Frank


n 11/26/2008 at 1:37 PM, in message
<14102947-7263-4caf-bf63-e155606d804b@y18g2000yqn.googlegroups.com>,
<plastiksprengstoff@googlemail.com> wrote:
> in 2006 i post this question - i dont beleve that see also
> http://groups.google.de/group/comp.lang.cobol/browse_thread/thread/46b66 
…[79 more quoted lines elided]…
> Andreas Lerch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
