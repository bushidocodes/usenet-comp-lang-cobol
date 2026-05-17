[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EIBCPOSN in CICS programs

_1 message · 1 participant · 1995-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### EIBCPOSN in CICS programs

- **From:** "7161..." <ua-author-17086122@usenetarchives.gap>
- **Date:** 1995-12-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b9a6j$s7l$1@mhadf.production.compuserve.com>`

```
Sorry I didn't quote the title correctly ... Actually, using the
CURSLOC=YES parameter on the DFHMSD macro when defining your BMS
map tells BMS to set bit two of the field's flag byte on the
inbound map upon execution of the RECEIVE of the map when the
cursor is positioned in that field. All you need to do is
interrogate the flag byte of each cursor sensitive field to
determine the field containing the cursor. This makes the logic
field oriented instead of relative position oriented thereby
making maintenance more logical for a COBOL type although bit
status interrogation is not a commonplace COBOL construct.
One additional caution ... since 3270 applications generally
"auto-skip" between fields on the screen, take care in how you
implement your cursor sensitivity so that the terminal operator
actually gets the result expected on the correct field.
Hope this helps.

Kevin P. Corkery
Independent Consultant
Voorhees, NJ  08043
COR··.@NAS··M.COM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
