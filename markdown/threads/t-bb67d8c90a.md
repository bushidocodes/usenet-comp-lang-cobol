[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with Packed fileds

_1 message · 1 participant · 2006-05_

---

### Problem with Packed fileds

- **From:** "Jyothy" <jyothy.annem@cognizant.com>
- **Date:** 2006-05-23T19:51:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148439076.758144.228860@j33g2000cwa.googlegroups.com>`

```
Hi All,

This is Jyothy.I am working on Migration Project.source is Main Frame
and Target is Teradata.I am extracting data through Power Exchange.In
My copybook , The field is defined as DATE PIC S9(7) COMP-3. when
Importing to Power Exchange I am getting the field data type as DATE
PACKED(7,0).When doing the row test I am getting the data as '61011'.
It is displaying as DATE DECIMAL(7,0) in INFORMATICA.Because of decimal
,leading zeros are getting truncated.Becomming invalidate for
DATE.Could you pls provide solution to unpack the data in the Power
Excahnge Itself? Or we have to do padding in the INFA?

Thanks
Jyothy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
