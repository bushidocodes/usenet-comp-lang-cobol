[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with accumulating

_6 messages · 5 participants · 2002-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help with accumulating

- **From:** JennCordell <member@dbforums.com>
- **Date:** 2002-11-12T17:43:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2038211.1037122998@dbforums.com>`

```

My professor handed out this assignment and I'm nearly clueless -
control break processing.  I can't figure out a way to accumulate the
department, division and company hourly rates and weekly salary
averages.  Here's what I have so far:

Procedure Division.
*>
100-Main-Module.
  Perform 150-Sort.
  Perform 200-Initialize.
  Perform 300-Process until Done.
  Perform 400-Total-Line.
  Perform 900-Close.
  Stop Run.
*>
150-Sort.
  Sort Work-File on ascending key
    Division-Key
    Department-Key
      Using Employee-Data
        Giving Sorted-Employees.
*>
200-Initialize.
  Perform 210-Open-Files.
  Perform 220-Read-Detail.
  Call "Dates" using Current-Date.
  Perform 230-Set-Values.
*>
210-Open-Files.
  Open Input Sorted-Employees
      Output Division-Report.
*>
220-Read-Detail.
  Read Sorted-Employees at end move "no" to Are-There-More-Records.
*>
230-Set-Values.
  Move Current-Date to Date-Out.
  Move Department-In to Department-Ws.
  Move Division-In to Division-Ws.
*>
300-Process.
  Evaluate True
    When Division-In not equal to Division-Ws
      Perform 310-Division-Change
      Perform 362-Division-Heading
      Perform 363-Department-Heading
    When Department-In not equal to Department-Ws
      Perform 320-Department-Change
      Perform 363-Department-Heading
  End-Evaluate.
    Perform 330-Calculate.
    Perform 340-Accumulate.
    Perform 350-Format.
    Perform 360-Write.
    Perform 220-Read-Detail.
*>
310-Division-Change.
  Perform 320-Department-Change.
  Perform 311-Accumulate-Division.
  Perform 312-Format.
  Perform 313-Write-Division.
  Perform 314-Reset-Values.
*>
311-Accumulate-Division.
 Add 1 to No-Of-Employees-Div.
 Add Hourly-Rate-In to Hourly-Rate-Div.
 Add Weekly-Salary-Ws to Weekly-Salary-Div.
*>
312-Format.
  Move Division-Ws to Division-Out.
*>
313-Write-Division.
  Add 1 to Line-Count.
*>
314-Reset-Values.
  Move Division-Out to Division-Out-Total.
*>
320-Department-Change.
  Perform 321-Accumulate-Department.
  Perform 322-Format.
  Perform 323-Write.
  Perform 324-Reset-Values.
*>
321-Accumulate-Department.
  Add 1 to No-Of-Employees-Dept.
  Add Hourly-Rate-In to Hourly-Rate-Dept.
  Add Weekly-Salary-Ws to Weekly-Salary-Dept.
*>
322-Format.
   Divide Hourly-Rate-Dept by No-Of-Employees-Dept giving
    Hourly-Rate-Dept-Avg rounded.
  Divide Weekly-Salary-Dept by No-Of-Employees-Dept giving
    Weekly-Salary-Dept-Avg rounded.
*>
323-Write.
  Add 1 to Line-Count.
  Write Report-Record from Department-Heading after advancing 1 line.
  Write Report-Record from Department-Total-Line after advancing 2
  lines.
*>
324-Reset-Values.
  Move Department-Out to Department-Out-Total.
  Move Department-In to Department-Ws.
  Move zero to Accumulators.
*>
330-Calculate.
  Multiply Hours-Worked-In by Hourly-Rate-In giving Weekly-Salary-Ws.
*>
340-Accumulate.
  Add 1 to No-Of-Employees-Co.
  Add Hourly-Rate-In to Hourly-Rate-Co.
  Add Weekly-Salary-Ws to Weekly-Salary-Co.
*>
350-Format.
  Move Division-Ws to Division-Out.
  Move Department-Ws to Department-Out.
  Move Employee-Name-In to Employee-Name-Out.
  Move Hourly-Rate-In to Hourly-Rate-Out.
  Move Weekly-Salary-Ws to Weekly-Salary-Out.
*>
360-Write.
  If Line-Count > 22 then
    Perform 361-Page-Heading
    Perform 362-Division-Heading
    Perform 363-Department-Heading
  End-If.
  Perform 364-Data.
*>
361-Page-Heading.
  Add 1 to Page-Count.
  Move Page-Count to Page-Out.
  Move zero to Line-Count.
  Write Report-Record from Report-Heading after advancing page.
  Move all "-" to Report-Record.
  Write Report-Record after advancing 1 line.
*>
362-Division-Heading.
  Add 1 to Line-Count.
  Move Division-Ws to Division-Out.
  Write Report-Record from Division-Heading after advancing 2 lines.
*>
363-Department-Heading.
  Write Report-Record from Department-Heading after advancing 1 line.
  Write Report-Record from Column-Heading after advancing 2 lines.
  Write Report-Record from Under-Line after advancing zero lines.
*>
364-Data.
  Write Report-Record from Data-Line after advancing 2 lines.
*>
400-Total-Line.
  Perform 410-Build-Total-Line.
  Perform 420-Write-Total-Line.
*>
410-Build-Total-Line.
*>
420-Write-Total-Line.
  Write Report-Record from Company-Total-Line after advancing 3 lines.
*>
900-Close.
  Close Sorted-Employees
        Division-Report.

I get the actual layout of the report, just nothing for the averages.
Any help is greatly appreciated!  Thank you!

Jennifer
```

#### ↳ Re: Help with accumulating

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-11-12T19:18:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqrk6g$o8b$1@peabody.colorado.edu>`
- **References:** `<2038211.1037122998@dbforums.com>`

```

On 12-Nov-2002, JennCordell <member@dbforums.com> wrote:

> My professor handed out this assignment and I'm nearly clueless -
> control break processing.  I can't figure out a way to accumulate the
> department, division and company hourly rates and weekly salary
> averages.  Here's what I have so far:

Not a bad start - make sure you write yourself a test plan that includes such
things as divisions changing, but departments remaining the same (two divisions
have the same department name).

I prefer paragraph names that are more clear - you have 314-Reset-Values and
324-Reset-values.  To tell the truth, I don't put these in a paragraph at all.
But figure what your teacher wants.

I think what you're missing is how to calculate the weekly salary average.   To
do this, you need some intermediate values:


add salary to department-total-salary, division-total-salary,
company-total-salary.
add 1        to department-total-count, division-total-count,
company-total-count.

On your department break, COMPUTE DEPARTMENT-AVERAGE = DEPARTMENT-TOTAL-SALARY /
DEPARTMENT-TOTAL/COUNT
and reset these totals.
```

#### ↳ Re: Help with accumulating

- **From:** JennCordell <member@dbforums.com>
- **Date:** 2002-11-12T22:07:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2039472.1037138820@dbforums.com>`
- **References:** `<2038211.1037122998@dbforums.com>`

```

I understand what you're saying...I'm just not sure how to force the
wage rate and weekly salary into their respective places and how to get
the program to count how many employees are in the department/division.
```

#### ↳ Re: Help with accumulating

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-11-13T03:02:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021112220257.24187.00004418@mb-mw.aol.com>`
- **References:** `<2038211.1037122998@dbforums.com>`

```
>Subject: Help with accumulating
>From: JennCordell member@dbforums.com 
>Date: 11/12/02 12:43 PM Eastern Standard Time

>My professor handed out this assignment and I'm nearly clueless -
>control break processing.  I can't figure out a way to accumulate the
>department, division and company hourly rates and weekly salary
>averages.

You're on to a good start but you're missing one vital piece of processing -
detail process, that is the processing of each individual record.

Right now your program only accumulates on a control break, which means you are
only accumulating the record that causes the break and not those inbetween.

The cycle goes something like this:
(note - this is my personal preference - there are those that do it a bit
differently)

1)  Prime read
     a)  set up control break holding fields

2)  Check for break
      a)  yes - do break
      b)  no - accumulate necessary fields to accumulator of lowest control
break
3)   Read another record

You do have the 'rolling totals' concept coded where the higher control break
calls the lower one.  In the lower control break the totals are rolled to the
next higher so at Department break the department totals are added to Division
totals and are then cleared.  At the Division break those are added to the next
higher and so on.

If the Company total is the final total that is done at end of file.

Eileen
```

#### ↳ Re: Help with accumulating

- **From:** "monkeycat" <mensa@iname.com>
- **Date:** 2002-11-20T03:27:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wiDC9.86318$hR3.68928@news2.central.cox.net>`
- **References:** `<2038211.1037122998@dbforums.com>`

```
I won't comment suggest actual changes to your coding - it's more important
that you have the right model in your mind.
.
Keep the following thought in mind - violating it is the most common logic
mistake of beginning programmers:
Once you have determined there is a control break, the control break
routines themselves should not do anything with the current record.  Control
break routines are dealing with totals of records you have ALREADY read.

Here's your safest sequence:

Check for control breaks and do them.
Process the current record, adding its numbers to the LOWEST control break
accumulators
Read the next record
.
.
In the LOWEST control break routine, before you zero out the LOWEST
accumulators, add them to the accumulators of the next higher control break
In the next highest control break, do the same for its next higher control
break. Etc. Etc.
.
.
.
Don't forget that end of file ALWAYS implies a control break of the highest
order.

Good Luck!

"JennCordell" <member@dbforums.com> wrote in message
news:2038211.1037122998@dbforums.com...
>
> My professor handed out this assignment and I'm nearly clueless -
…[167 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Help with accumulating

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-20T00:02:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<arf8hs$1ml$1@slb6.atl.mindspring.net>`
- **References:** `<2038211.1037122998@dbforums.com> <wiDC9.86318$hR3.68928@news2.central.cox.net>`

```
Or use Report Writer - where all of this is done FOR YOU <G>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
