[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compile error

_1 message · 1 participant · 2004-03_

---

### Re: Compile error

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-03-14T16:39:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_PidnaZWM_OJQsnd4p2dnA@giganews.com>`
- **References:** `<20040313233938.02537.00003479@mb-m23.aol.com> <1MX4c.9$Q16.2532@news20.bellglobal.com> <ofudnXosF7HrAcnd4p2dnA@giganews.com> <qdm950tcmgium27afa1shinsl5216b8hp9@4ax.com>`

```
Volker Bandke wrote:
> On Sun, 14 Mar 2004 11:55:34 -0600, "JerryMouse" <nospam@bisusa.com>
> wrote:
…[29 more quoted lines elided]…
> Which will not work if sal-po-asking = 20000

Good catch! I should have said:

EVALUATE SAL-PO-ASKING
  WHEN 95 THRU 20001 *> or some other arbitrarily large number
      blah
  WHEN 94 THRU 20001
      blah2
  WHEN 92.5 THRU 2001
      blah3
   etc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
