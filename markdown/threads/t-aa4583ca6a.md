[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right Justify Routine

_1 message · 1 participant · 1998-09_

---

### Right Justify Routine

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-XiTbHJiS5z0r@Dwight_Miller.iix.com>`

```
Here's a little ditty some of you might be able to use.  Also, I am 
sure someone can post an improvement!

 Identification Division.
 Program-Id.  Test3.
* right justify
 Environment Division.
 Configuration Section.
 Source-Computer.  IBM-PC.
 Object-Computer.  IBM-PC.
 Data Division.
 Working-Storage Section.
 01  input-field    pic x(30)        value spaces.
 01  output-field   pic x(30)        value spaces.
 01  counter        pic 9(9) comp    value zeros.
 Procedure Division.
 test3-start.
     display "Enter field: "
     accept input-field
     if input-field > spaces
        perform varying counter from 1 by 1
                until function reverse (input-field) (counter:1) > 
space
          continue
        end-perform
        move function reverse (input-field) (counter:) to output-field
        move function reverse (output-field) to input-field
     end-if
     display "*" input-field "*"
     Stop Run
     .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
