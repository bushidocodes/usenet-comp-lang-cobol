[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Student question "evaluate"

_2 messages · 2 participants · 1999-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Student question "evaluate"

- **From:** "Bill" <123vapos123@excite.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7db8ej$qqr@chronicle.concentric.net>`

```
I'm using the "EVALUATE TRUE" statement
When a true condition is hit upon, does the program execute this condition
and jump to the "END-EVALUATE" or does it fall to the next WHEN?

case 1 :  A=2, B=5, C=0;  only 456-WALK will be executed.
case 2 : A=1, B=8, C=9;  will 123-RUN and 789-CRAWL both execute?

EVALUATE TRUE
    WHEN A = 1
      PERFORM 123-RUN THROUGH 123-EXIT
    WHEN B = 5
      PERFORM 456-WALK THROUGH 456-EXIT
    WHEN C = 9
      PERFORM 789-CRAWL THROUGH 789-EXIT
END-EVALUATE

Thanks in advance.
Bill
________________________
remove both "123"s to email me
123vapos123@excite.com
```

#### ↳ Re: Student question "evaluate"

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990324163517.01187.00001000@ng-ch1.aol.com>`
- **References:** `<7db8ej$qqr@chronicle.concentric.net>`

```
when the first true condition is "hit" it executes the statements and then goes
to the end-evaluate statement.

TW
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
