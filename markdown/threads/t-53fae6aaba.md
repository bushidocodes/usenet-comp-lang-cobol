[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorting

_2 messages · 2 participants · 1995-09_

---

### Sorting

- **From:** "joe.s..." <ua-author-17088313@usenetarchives.gap>
- **Date:** 1995-09-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8B1527D.0C0000011B.uuout@sinbad.com>`

```
I am currently working on a class assignment. The program is
coded...running and the output is correct as far as what is required.
However I want to go a step futher.

The printed output list sales transactions from a sequentially read input
file. The transaction records listed in the input file are basically
sorted by account number but not by transaction date.

I use the account number as a printing control break so each customer's
bill is printed on a seperate page. However their transactions are not
listed sequentially. Although this is fine for the assignment...it is not
professional looking and would not be acceptable in the real world.

I would like to sort the input-file that contains the sale transactions by
account-number and date. The name of the input-file is Phone-in-File.

I am confused as to what coding is needed in the Input-Outut section of the
program. This is what my Input-Output section reads (I took out anything
thing that deals with sorting since none of them worked)

FILE-CONTROL.
SELECT Cust-In-File
ASSIGN To Disk, "B:\Data\Customer.Dat"
Organization is line sequential.

SELECT Price-In-File
ASSIGN To Disk, "B:\Data\Price.Dat"
Organization is line sequential.

SELECT Phone-In-File
ASSIGN To Disk, "B:\Data\Phonesal.Srt"
Organization is line sequential.

SELECT Sales-Out-File
ASSIGN To Disk, "B:\Sales.Rpt".



The subroutine I wanted to use to perform the sort was:

300 Sort-Phone-In-File
Sort Sort-File
On ascending key S-cust-number
S-trans-sdate
Using Phone-In-File
Giving Phone-Sale-File

What would I need to include in my Input-Output section in order to
accomplish this.

Thanks in advance.

-=>Joe Sweeney-=<
joe··.@sin··d.com











---
* WR 1.31 # 698 *
```

#### ↳ Re: Sorting

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1995-09-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-53fae6aaba-p2@usenetarchives.gap>`
- **In-Reply-To:** `<8B1527D.0C0000011B.uuout@sinbad.com>`
- **References:** `<8B1527D.0C0000011B.uuout@sinbad.com>`

```
684··.@LMS··D.COM wrote:

› In article <8B1··.@sin··d.com>
› joe··.@sin··d.com (JOE SWEENEY) writes:
…[52 more quoted lines elided]…
› LMSC5:  Tons of Beautiful Big Blue Iron...

I would like to add that you will need to add an OPEN INPUT the file
"Phone-Sale-File" used in the SORT GIVING clause after the SORT and
process the report. But since you want to go further, may I suggest
you experment with INPUT / OUTPUT PROCEDURE clauses depending whether
you need to filter the data used in the report. This avoids the
intermediate FD file "Phone-Sale-File" (unless your instructure wants
to see the sorted file, then add a second WRITE statement to send the
raw record to "Phone-Sale-File"). For a greater challange, code the
INPUT / OUTPUT PROCEDURE clauses as a COBOL-74 program (with its
SECTION and GO TO requirements).

Just my two cents (PIC V99) worth,
Boyce Williams
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
