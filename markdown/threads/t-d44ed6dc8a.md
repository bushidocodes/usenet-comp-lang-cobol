[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL- Tables help.

_3 messages · 3 participants · 1998-12_

---

### COBOL- Tables help.

- **From:** "Steve Reid" <asreid@lineone.net>
- **Date:** 1998-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Prd2.2530$Uh5.62@news-reader.bt.net>`

```
I'm a student trying to get my head around writing tables. At present I'm
writing a programme to produce a table of student grades. First in Working
Storage to hold a count of the number of students for each of the four
grades(Distinction, Credit, Pass and Fail) within each exam paper (3). Max
of 99 students.  Then I have to produce a complete Procedure Division to
read each record in turn using Paper and Mark fields from incoming data to
add 1 to the relevant counter in the table.

Any help on this subject would be appreciated.

Steve.
```

#### ↳ Re: COBOL- Tables help.

- **From:** docdwarf@clark.net ()
- **Date:** 1998-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7564lm$3go$1@clarknet.clark.net>`
- **References:** `<0Prd2.2530$Uh5.62@news-reader.bt.net>`

```
In article <0Prd2.2530$Uh5.62@news-reader.bt.net>,
Steve Reid <asreid@lineone.net> wrote:

[snippage of table-handling assignment]

>Any help on this subject would be appreciated.

The help offered will depend on the work already done... please either
post the code to show how far you've already gotten or do your own
homework..

DD
```

#### ↳ Re: COBOL- Tables help.

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1998-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75b5p7$nkr$1@nnrp1.dejanews.com>`
- **References:** `<0Prd2.2530$Uh5.62@news-reader.bt.net>`

```
I won't code your solution, but think about this:

Visualize a spreadsheet, with each row representing an exam and each column a
grade.	Now, when you code your table in working storage, each row is a
single occurance of the group field to which you apply your OCCURS clause. 
Within that group item that OCCURS n times, each column of your spreadsheet
is a field - one field for each possible grade.

In procedure, when you read a record, if the PAPER (exam?) field is numeric,
use that field as the subscript value to point to a row of the table and add
1 to the appropriate field/column.  How you determine the appropriate field
to increment will depend on the nature of the data in your MARK field on the
input file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
