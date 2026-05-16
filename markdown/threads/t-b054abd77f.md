[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help with subscripts

_4 messages · 4 participants · 1999-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### help with subscripts

- **From:** wescraven_1@excite.com
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7smq5h$k2t$1@nnrp1.deja.com>`

```
i am trying to use a subscript to go through a table which has a salary
that can occur 3 times but not always and i want it to go through
depending on if there is a salary and if not to stop right there. need
help                              Thank you to anyone who helps

   PERFORM
       VARYING EMP-SUB FROM 1 BY 1
           UNTIL EMP-SALARY (EMP-SUB) > 3
           AND EMP-SALARY (EMP-SUB) NOT = 0


   END-PERFORM.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: help with subscripts

- **From:** bbello5778@aol.com (BBello5778)
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990927071457.28360.00003106@ng-da1.aol.com>`
- **References:** `<7smq5h$k2t$1@nnrp1.deja.com>`

```
>PERFORM
>       VARYING EMP-SUB FROM 1 BY 1
>           UNTIL EMP-SALARY (EMP-SUB) > 3
>           AND EMP-SALARY (EMP-SUB) NOT = 0

try UNTIL EMP-SALARY (EMP-SUB) > 3      OR EMP-SALARY (EMP-SUB) = 0

Good luck
```

#### ↳ Re: help with subscripts

- **From:** Ed Stevens <Ed.Stevens@nmm.nissan-usa.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7snsua$ajs$1@nnrp1.deja.com>`
- **References:** `<7smq5h$k2t$1@nnrp1.deja.com>`

```
I won't do your homework assignment for you, but here's some things to
look at that should lead you to the solution.

Since your control variable is EMP-SUB, and EMP-SUB has a max value 3,
you should be checking for EMP-SUB > 3.  As it is, you're checking for
a particular occurance of EMP-SALARY > 3.  Also, consider the impact of
joining two condition with AND vs. joining two conditions with OR.

Others will disagree for valid reasons, but my personal style is to
have only one condition in the UNTIL clause, and that condition is
checking for the control subscript > its max value. Any other
conditions that could cause an 'early bailout' are checked as part of
the processing of each value of the subscript.

In article <7smq5h$k2t$1@nnrp1.deja.com>,
  wescraven_1@excite.com wrote:
> i am trying to use a subscript to go through a table which has a
salary
> that can occur 3 times but not always and i want it to go through
> depending on if there is a salary and if not to stop right there. need
…[11 more quoted lines elided]…
>
```

#### ↳ Re: help with subscripts

- **From:** john_mindock@my-deja.com
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7snv4j$c99$1@nnrp1.deja.com>`
- **References:** `<7smq5h$k2t$1@nnrp1.deja.com>`

```

>
>    PERFORM
…[5 more quoted lines elided]…
>
There's an obvious mistake in the UNTIL.. line.

Here's a solution (pseudocode).
Set a SALARY-DONE-SW switch to 'N', with an '88' SALARY-DONE VALUE 'Y'.
PERFORM VARYING ... UNTIL EMP-SUB > 3 OR SALARY-DONE.
If you hit EMP-SALARY(x) = 0, MOVE 'Y' TO SALARY-DONE-SW.

John


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
