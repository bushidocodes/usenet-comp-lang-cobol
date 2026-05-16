[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help: COBOL/CICS Re-useable Working-Storage Problem

_1 message · 1 participant · 1998-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Help: COBOL/CICS Re-useable Working-Storage Problem

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Czd4xQerEldG@Dwight_Miller.iix.com>`
- **References:** `<35F3903B.508D2B41@powernet.co.uk>`

```
On Mon, 7 Sep 1998 07:50:19, Phil Davey <davey@powernet.co.uk> wrote:

> I tested a solution today which I think works,  I put the table into an
> ASM routine and statically linked it into the dynamic routine.
…[18 more quoted lines elided]…
> comments).

Multiple programs updating the same storage location?  Each could be 
addressing simultaneously, and that should be OK .  It bothers me for 
some reason, but I can't find a reason it should not work.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
