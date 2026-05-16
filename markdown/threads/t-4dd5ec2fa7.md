[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Nice to have" Enhancement in draft/next Standard (was Exit program vs. Goback

_1 message · 1 participant · 1999-03_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Re: "Nice to have" Enhancement in draft/next Standard (was Exit program vs. Goback

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bqueg$84@dfw-ixnews8.ix.netcom.com>`
- **References:** `<japC2.8497$jf2.3109245@hme2.newscontent-01.sprint.ca> <36dae4be.29987780@news.enterprise.net> <36DAEC47.AEC0DEDB@NOSPAMhome.com> <36daff7d.6644584@news3.ibm.net> <36db151e.0@mercury.nildram.co.uk> <36dbc94f.88500967@news.enterprise.net> <7bh9dr$aks@dfw-ixnews6.ix.netcom.com> <36DEB2CF.A11C1B72@ms.com> <7bn4v4$ehd@dfw-ixnews5.ix.netcom.com> <36E04E56.31E459C6@ms.com> <7bpshc$ap5@dfw-ixnews4.ix.netcom.com> <36e09afa.251569626@news1.ibm.net> <7bqeta$lsl@sjx-ixn6.ix.netcom.com>`

```
I checked the rules and my last example is NOT valid.  A "good" (valid)
example of the use would be:

Evaluate A
    When > B
        Perform X
    When < C
        Perform Y
    When Positive
        Perform Z
    When Other
        Display "Here we go again"
End-Evaluate

This is valid because the Selection OBJECT begins with a relational operator
or starts a class test - but the Selection SUBJECT is still an identifier.
(My original error was having the "dangling" relational operator - which I
think at one time was allowed but not by the current draft.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
