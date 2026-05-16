[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for simpler algorithm

_1 message · 1 participant · 2000-01_

---

### Re: Looking for simpler algorithm

- **From:** "Glenn Gordon" <ggordon@dimensional.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Eddh4.446$x3.730@wormhole.dimensional.com>`
- **References:** `<388752b8.9703165@news.supernews.com>`

```
"zennmaster" <zenn@master.net> wrote in message
news:388752b8.9703165@news.supernews.com...
> I have various date conversion programs except (of course) the one I
> need most - a julian to gregorian conversion program that includes
…[3 more quoted lines elided]…
> for this subprogram?

Use the built-in functions to make it a breeze.  Untested typed from memory
use at own risk working storage left as an exercize only looks like COBOL
pseudo-code:

To Julian:

move Greg-yyyy to Greg-Base-yyyy
                             Juli-yyyy
compute Juli-ddd = function integer-of-date(Greg-Date) -
                             function integer-of-date(Greg-Date-Base) + 1
end-compute

where Greg-Date-Base is Greg-Base-yyyy with 0101 for month and day.


From Julian:

move Juli-yyyy to Greg-Base-yyyy
compute Greg-Date = function date-of-integer(
                                     integer-of-date(Greg-Date-Base) +
Juli-ddd -1)
end-compute

where Greg-Date-Base is Greg-Base-yyyy with 0101 for month and day.



>
> thanks!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
