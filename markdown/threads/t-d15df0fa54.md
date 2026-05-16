[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL indexes

_2 messages · 2 participants · 2003-02_

---

### Re: COBOL indexes

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-25T14:44:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3grl5$qce$1@si05.rsvl.unisys.com>`

```
I wrote:

> Indeed, I don't see just a whole bunch of unique functionality associated
> with USAGE INDEX data items offhand; when they are used to reference table
> entries, they function as subscripts, not as indices.

Actually, I'll take that back.  I do see significant functionality.

USAGE INDEX can I think reasonably be assumed to be implemented in a manner
that represents a given implementation's MOST EFFICIENT way of storing and
retrieving an occurrence number, and I'd further expect the implementor's
definition of "most efficient" to be in terms of processor time consumption
during execution.    All that's required of it is that it represent an
occurrence number; the rest is left up to the implementor.

To use a *reductio ad absurdum*:   An implementor COULD choose something
like
    01  USAGE-INDEX-STYLE USAGE DISPLAY PICTURE ***,***,***,*99CR.
as an appropriate model for storing indices.  It's even COBOL85 compatible
because of the de-editing features of COBOL85.  I would, however, contend
that would be a *bad* choice.

In the case of Unisys MCP/AS systems,
    77  USAGE-INDEX-STYLE USAGE BINARY EXTENDED PIC S9(11). *< or even PIC
S9(23)
would be a MUCH BETTER choice, and comes really close to how it's actually
implemented.  But such a declaration would not be portable to, or meaningful
on, anything but another Unisys MCP/AS system.  It'd be worthless on a V
Series, or a 2200, or an IBM system, or a PC, or a Unix box.

If the programmer has coded USAGE INDEX, we are free to use the above
format, IBM is free to use whatever's best for it, and so on.  A
standards-compliant program would be portable -- even in how it uses the
USAGE INDEX item, so long as it's not, say, in a file somewhere -- to any
other machine with a standards-compliant compiler, and be relatively
efficient (in this respect) on any of them.

That doesn't *guarantee* the most efficient implementation, but it does
suggest that a USAGE INDEX item is *most likely* to be more efficient than
"generic numeric", and that any significantly greater efficiency would
require the use of an "implementor extension" USAGE for that purpose.
It's portable because it's required by the standard, and no aspect of its
use places any specific format on it.

    -Chuck Stevens
```

#### ↳ Re: COBOL indexes

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2003-02-26T09:14:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.hax68p0.pminews@News.CIS.DFN.DE>`
- **References:** `<b3grl5$qce$1@si05.rsvl.unisys.com>`

```
On Tue, 25 Feb 2003 14:44:54 -0800, Chuck Stevens wrote:

>I wrote:
>
…[12 more quoted lines elided]…
>

In this discussion I am missing a very important argument in favor of
indexing.
An index belongs to one particular table and the compiler guarantees that it
will not be used for other purposes.
Am I the only one who has tried to find out why  and where a certain
subscript field was changed?

The performance issue is also very clear to me. Indexing will never be slower
than subscripting and takes the same time to code, so  I use indexing.
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
