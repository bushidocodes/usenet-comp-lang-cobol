[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# y2k- entire mainframe recompile

_2 messages · 2 participants · 1999-11_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: y2k- entire mainframe recompile

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s3dfr2ph3ef18@corp.supernews.com>`
- **References:** `<r6dc3s8m6fslq1q7gpsuft9c4ata59jqmj@4ax.com>`

```
I claim such massive code changes can be carried out, in practice.

You probably can't avoid recompiling the entire million-line source code
base,
but that might merely be an overnight problem.    The database conversion
you can do incrementally: simply add a parallel relation which records for
every record whether it is expanded or not, initally marking all records as
"unexpanded".
(Many of the Y2K fixes hide this bit in the existing representation of the
year,
such that the current year values essentially indicate "unexpanded").

Then the code needs to read records and consult the "unexpanded" bit
to decide how to complete the read.   On a write, always write the expanded
form and set the bit.   At some point, run a utility to clean up the
unconverted files.

So this is sort of easy.

What's hard is getting the entire source base to change overnight.  You
cannot do
this by hand.    You need a tool that reads the entire source base (between
application programmer revisision, so probably overnight, or at best over a
day or two),
and make consistent code changes to accomplish the above.

See http://www.semdesigns.com/Products/DMSToolkit.htm to see a tool
that could be used for this purpose.

-- IDB

G Moore wrote in message ...
>ok, i have been thinking, and i have come across a theoretical
>problem....
…[7 more quoted lines elided]…
>of code as a copy file or whatever... that would mean that it has alot of
records....
>
>in any case, such a machine *would* require downtime, as one would be
…[3 more quoted lines elided]…
>10% of the problem takes 90% of the time, right?
```

#### ↳ Re: y2k- entire mainframe recompile

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81793p$127$1@nntp6.atl.mindspring.net>`
- **References:** `<r6dc3s8m6fslq1q7gpsuft9c4ata59jqmj@4ax.com> <s3dfr2ph3ef18@corp.supernews.com>`

```
Not sure if this is what was being asked, but - online database
re-engineering can reasonably be accomplished using shadow
databases.

Create a second copy of the DB & make the OS point O/L Apps.
at the shadow, instead of the original. Then use the original (or latest
image copy), to unload/reload with a user exit in the reload to re-engineer,
with the new DBD.

I'm trying to convince my current clients to use switchable DB's
for an application that has 24 hour O/L window, but needs to take
the DB down for update & reorg. Of course this requires more
disk & CPU resources, so they are reticent. But eventually they
will see that this is the optimum solution - I hope!

> G Moore wrote in message ...
> >ok, i have been thinking, and i have come across a theoretical
…[18 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
