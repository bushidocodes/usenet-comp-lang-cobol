[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Random number generator

_1 message · 1 participant · 1995-05_

---

### Random number generator

- **From:** "t..." <ua-author-17087614@usenetarchives.gap>
- **Date:** 1995-05-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o8tn1$h7e@news.cerf.net>`

```

Here's one that was written for Acucobol-85.

Enjoy!

Tim McCormley
t.··.@acu··l.com

identification division.
program-id. rnd is resident program.
********************************************************************
remarks.

Every time you perform "call rnd" you get a new random-number rnd_value
between rnd_from and rnd_to !!!
Based on a publication of Hewlett-Packard for the HP41 calculator.

rnd=rnd*9821+0.211327
rnd=rnd-int(rnd)

***<<< Here is a sample call ***>>>
working-storage section.
01 rnd_value pic 9(12)v9(5) value 0.
01 rnd_from pic 9(3) value 0.
01 rnd_to pic 9(3) value 1.
01 rnd_form pic z(12).z(5).
procedure division.
rnd-start.
perform 24 times
call "rnd" using rnd_value rnd_from rnd_to
move rnd_value to rnd_form
display rnd_form
end-perform.
accept omitted.
***<<< End Sample call ***>>>

environment division.
configuration section.
data division.

********************************************************************
working-storage section.
********************************************************************
01 int1 double value 0.
*01 int1 pic 9(12)v9(5) value 0.
01 int2 pic 9(12).
01 time_i pic 9(8).


linkage section.

01 rnd_value pic 9(12)v9(5).
01 rnd_from pic 9(3).
01 rnd_to pic 9(3).

********************************************************************
procedure division using rnd_value rnd_from rnd_to.
********************************************************************
rnd-start.
if int1 = 0
accept time_i from time
move time_i(7:2) to int1
compute int1 = int1 / 100
if (rnd_from - rnd_to) = 0
move 0 to rnd_from
move 1 to rnd_to
end-if
end-if

compute int1 = int1 * 9821 + 0.211327
move int1 to int2
compute int1 = int1 - int2
move int1 to rnd_value
compute rnd_value = rnd_value * (rnd_from - rnd_to) + rnd_from.

exit program.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
