[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# same field for input output

_1 message · 1 participant · 2002-06_

---

### same field for input output

- **From:** "Joseph Ostreicher" <josephos@hotmail.com>
- **Date:** 2002-06-26T00:42:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d1947c7@news.mhogaming.com>`

```
using the following, how would I code it, to get the input and output on the
same screen item

 working-storage section.
 01  Phone-number           pic 9(14)      value zero.
 01  Formatted-number       pic x(14)      value "(xxx) xxx-xxxx".
 01  Formatted-alt          pic x(8)       value "xxx-xxxx".
 01  The-edited-number      pic z(14)      value space.
 screen section.
 01 pe blank screen.
     03 line 1 column 1 value "Enter Phone Number".
     03 line 1 column 22 pic 9(14) using Phone-number.
/     03 line 1 column 1 value "Edited Phone Number".
/     03 line 1 column 22 pic x(14) from the-edited-number.
 procedure division.
 if-test-start.
     display pe
     accept pe


     if phone-number > 9999999
/ test above 9(7)
     inspect Formatted-number
     replacing First "xxx" by phone-number (1:3)
               First "xxx" by Phone-number (4:3)
               First "xxxx" by phone-number (7:4)
     move formatted-number to phone-number
     else
     inspect formatted-alt
     replacing First "xxx" by phone-number (4:3)
               First "xxxx" by phone-number (7:4)
     move formatted-alt to phone-number
     end-if
     display pe
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
