[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Evaluate

_1 message · 1 participant · 1995-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Evaluate

- **From:** "t..." <ua-author-17087614@usenetarchives.gap>
- **Date:** 1995-05-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3odh65$5dn@news.cerf.net>`

```
This EVALUATE should work too:

77 the-item pic 9.
88 paragraph-1 value 1.
88 paragraph-2 value 2.
.
.
.
88 paragraph-20 value 20

evaluate true
when paragraph-1
when paragraph-2
when paragraph-3
perform something
when paragraph-10
perform something-else
when other
perform default-handling
end-evaluate.

You just have to remember that in a "stacked" WHEN clause, the first WHEN
clause that evaluates true will be the one that transfers control in your
program, so you want to be careful about the order.

Tim McCormley
tim··.@acu··l.com
---------------------------------------------------------------------
"Eat a live bullfrog in the morning and that's the worst thing that
will happen to you all day".
-Country Dick Montana
---------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
