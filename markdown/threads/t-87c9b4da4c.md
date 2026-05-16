[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Infinite Loops and Explicit Exits

_1 message · 1 participant · 2004-11_

---

### Re: Infinite Loops and Explicit Exits

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-11-01T12:04:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cm64rk$188s$1@si05.rsvl.unisys.com>`

```
As I mentioned peripherally elsewhere, these two documents have now been
posted on the INCITS/J4 website at http://www.cobolportal.com/j4/ :

a.. 04-0194 -- Allow EXIT PERFORM [CYCLE] in Out-of-Line PERFORM
a.. 04-0195 -- Provide Explicit Infinite Loop Capability

They are on the agenda for the next J4 meeting for discussion as candidates
for a future revision of the standard.

    -Chuck Stevens

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message news:...
> For those who have been following the "perform forever" and "exit perform
> [cycle]" threads, I'm just tidying up the first drafts of two proposals
that
> I hope to submit Real Soon Now to INCITS/J4 for evaluation and
consideration
> for a future standard, if nothing else so that they can be added to the
> "candidates list" for future consideration.
>
> One of these proposals relaxes the current restriction that an EXIT
PERFORM
> or EXIT PERFORM CYCLE statement may only appear within a PERFORM ...
> END-PERFORM range.
>
> The other proposal is for PERFORM ... UNTIL FALSE.   I didn't want to add
a
> new reserved word and for that reason rejected PERFORM ... FOREVER.  I was
> concerned about the potential semantic ambiguities that one might
encounter
> in sequences like "PERFORM ... PERFORM ... UNTIL EXIT PERFORM ...
> END-PERFORM ...", which led me away from PERFORM ... UNTIL EXIT.  I don't
> care for PERFORM ... WITH NO TEST because it really doesn't convey the
sense
> of iteration.  I am not wedded to the syntax I chose, but I think the
> technical reasons for avoiding the other three here presented are sound.
>
> Unless WG4 so directs, these capabilities can't be included in the
proposed
> 2008 standard.  But I can envision no technical barrier at all to the
second
> of these, and the only barriers I can envision to the first are
> implementor-specific, WG4 *might* acquiesce so long as the additions do
not
> cause a delay in the production of that next standard.
>
> At the very least this action on my part will ensure that these topics are
> on the standards committees' radar screens, and stimulate the discussion
and
> clarification as to why EXIT PERFORM (with or without CYCLE) was limited
to
> inline PERFORMs in the 2002 standard.
>
>     -Chuck Stevens
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
