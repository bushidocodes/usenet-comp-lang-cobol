[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How change record with no unique fields?

_2 messages · 2 participants · 1997-01_

---

### How change record with no unique fields?

- **From:** "byate..." <ua-author-14787294@usenetarchives.gap>
- **Date:** 1997-01-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970130054500.AAA23195@ladder01.news.aol.com>`

```

Hello,

For a school project, I am trying to give the user the ability
to select and change a record in a file that has no unique fields.

For example, if a user needed to change the second record below
to LD (instead of LE), how might one program that option, since
there are no unique fields to select the correct record?

EMP-ID-NO. TRIP-NO.
123456789 0000000LB
123456789 0000000LE
567890123 0000000LC
567890123 0000000LE

...etc.

BTW, the reason EMP-ID-NO has duplicates is because an employee
may take more than one trip.

Also, TRIP-NO has duplicates because 1 to 20 employees may go on
the same trip together.

One approach I am thinking about is to use the record number
Cobol automatically creates (though I don't know how to access
it). My idea, if I could access that number, is to print the
entire file (after it has been sorted) showing each record
number, and then, after it is printed, the user could enter the
automatic record number at a prompt to bring up the record that
needs to be changed.

Can anyone advise me how to do this, or maybe suggest a better
approach altogether?

I am using RmCobol-85 (student edition).


Sincerely,


B.Yates
```

#### ↳ Re: How change record with no unique fields?

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-01-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9db22dea9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970130054500.AAA23195@ladder01.news.aol.com>`
- **References:** `<19970130054500.AAA23195@ladder01.news.aol.com>`

```

In message <<199··.@lad··l.com>> bya··.@a··.com writes:
› 
› For a school project, I am trying to give the user the ability
…[10 more quoted lines elided]…
›   567890123       0000000LE

Have the key field emcompass both the employee id and the trip-no.

01 Employye-Trip-Record.
03 ET-Key.
05 ET-Employee-ID PIC X(8),
05 ET-Trip-No PIC X(8).

Now think about the procedure that *actually* occurs.
Do Employees 'change' from one trip to another, or do
they cancel being on one trip and attach themselves to a trip.

ie don't treat 'change' as a special case but as cancel and
create, which presumably already exist in the code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
