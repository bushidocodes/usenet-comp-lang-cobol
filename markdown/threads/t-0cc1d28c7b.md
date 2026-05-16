[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right Justify Routine

_1 message · 1 participant · 1998-09_

---

### Re: Right Justify Routine

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-dHzW10KtU9zp@Dwight_Miller.iix.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-XiTbHJiS5z0r@Dwight_Miller.iix.com> <o%VH1.3786$gM3.2803875@news4.mia.bellsouth.net> <trYH1.464$I%.1378959@news1.atlantic.net> <HtbI1.5187$eZ3.3317864@news3.mia.bellsouth.net> <BseI1.481$I%.1861130@news1.atlantic.net>`

```
On Sat, 5 Sep 1998 17:26:41, "Rick Smith" <ricksmith@aiservices.com> 
wrote:

> On my machine, with MF 3.2, "Rick" ran in 5.49 seconds, "Judson"
> in 2.86 seconds, and "hand-coded" in 0.38 seconds. The execution
…[6 more quoted lines elided]…
> adding the move statement!

I had to change your program slightly to get it to compile under 
Fujitsu - seems MicroFocus allows you to MOVE the value from a numeric
intrinsic function, where the standard (and thus Fujitsu) only allow 
their use in compute statements.

This is the line I changed: move function length (input-field) to i j

Make it a compute i  = function length (input-field)
                   move i to j

After that it ran.  Similar time differential, but the Judson and the 
Hand coded one were closer in timing.  Turning on Fujitsu optimization
made the Judson routine and the hand coded routine equal, or gave the 
hand coded routine only a very slight edge after repeated executions. 
Very interesting.  I never thought that little code snippet would open
this kind of can of worms!  Great disucssion though.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
