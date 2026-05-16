[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# post-y2k code expansion

_1 message · 1 participant · 1999-10_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### post-y2k code expansion

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a+UZOL9yldjUgs+KK0RpbBIjpOTl@4ax.com>`

```
let's say after jan 1,2000 your company wants to get rid of all
data expansion instances, and replace it with yyyymmdd file expansion
instances

thus, we might create from a

sub-mmddyy-from-mmddyy-giving-days.

function

other functions like

sub-mmddyy-from-mmddccyy-giving-days.
sub-mmddccyy-from-mmddyy-giving-days.

sub-mmddccyy-from-mmddccyy-giving-days.
	*mainly using integer of date functions

or functions like

move-mmddyy-to-mmddccyy.
move-mmddccyy-to-mmddyy.

all with corresponding linkage sections.


newsreader is lagged. please reply via email 
to gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
