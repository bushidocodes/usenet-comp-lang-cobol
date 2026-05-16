[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Any need for PIC A ?

_4 messages · 4 participants · 1998-09_

---

### Re: Any need for PIC A ?

- **From:** dbryant@netcom.com (David K. Bryant)
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dbryantEz8MH7.9Dz@netcom.com>`
- **References:** `<68n$1@nnrp1.dejanews.com> <C9NK19410@news4.mia.bellsouth.net>`

```
"Judson McClendon" <judmc123@bellsouth.net> writes:

>beelerj@my-dejanews.com wrote:
>>Does anyone know of a circumstance when PIC A would be prefereable to PIC X?
>>My COBOL instructor (a real-world programmer) couldn't think of any, and I
>>was just curious.


>That's a good question.  I've been programming COBOL for 30 years, and have
>never seen a need for it.  I would like to know if anybody else has seen one.


You've probably never seen a PIC A used because you've 
never worked with programmers who have actually opened
the manual to see what nice features Cobol actually has.
Instead they rely on what they learned in two semesters
of academic settings.

Instead of letting the system enforce data integrity thru
the use of PIC 9 or PIC A acceptance fields, they would 
rather code everything as PIC X and handle data integrity 
thru range selections.  If you're lucky.

I spend a part of my week troubleshooting problems that often  
turn out to be related to dirty data.... uninitialized
Working Storage, input into PIC X when the only valid values
are numeric, etc.


Typical:  Need to input all-numeric Social Security Numbers,
telephone numbers, or ZIP (postal) codes.  Sure, we'll just
input into a PIC X and then write a look to scan and check
each digit for 0-9 content....  but they get lazy and leave
out the part following "and then".
```

#### ↳ Re: Any need for PIC A ?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6th7j8$m13@sjx-ixn10.ix.netcom.com>`
- **References:** `<68n$1@nnrp1.dejanews.com> <C9NK19410@news4.mia.bellsouth.net> <dbryantEz8MH7.9Dz@netcom.com>`

```

David K. Bryant wrote in message ...
>"Judson McClendon" <judmc123@bellsouth.net> writes:
>
>>beelerj@my-dejanews.com wrote:
>>>Does anyone know of a circumstance when PIC A would be prefereable to PIC
X?
>>>My COBOL instructor (a real-world programmer) couldn't think of any, and
I
>>>was just curious.
>
>
>>That's a good question.  I've been programming COBOL for 30 years, and
have
>>never seen a need for it.  I would like to know if anybody else has seen
one.
>
>
…[22 more quoted lines elided]…
>

Do you know of a SINGLE COBOL compiler and run-time that gives any error or
problem if you try and put a numeric into a PIC A field?  I don't!

Furthermore, although there are several types of "terminals" (dumb, smart,
and PC) that will reject an attempt to enter a letter into a PIC 9 "input
field", I don't know of a single one that will "reject" an attempt to put a
number into a PIC A field.  I have tried this on all the IBM 327x terminals,
several PCs (with different operating systems and compilers).  There may be
one out there that actually does the edit for you - but I haven't
experienced it.  (and of course it will become "non-standard" to make such a
distinction in the next Standard).

Just to be clear, there are LOTS of good reasons to use a PIC 9 (numeric or
numeric-edited) field rather than a PIC X field.  However, I have yet to see
a time when using a PIC A field instead of a PIC X field has provided any
advantage.  Such a case may exist - but I haven't found it yet.
```

#### ↳ Re: Any need for PIC A ?

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tjab8$14q$1@callisto.clark.net>`
- **References:** `<68n$1@nnrp1.dejanews.com> <C9NK19410@news4.mia.bellsouth.net> <dbryantEz8MH7.9Dz@netcom.com>`

```
In article <dbryantEz8MH7.9Dz@netcom.com>,
David K. Bryant <dbryant@netcom.com> wrote:
>"Judson McClendon" <judmc123@bellsouth.net> writes:
>
…[12 more quoted lines elided]…
>the manual to see what nice features Cobol actually has.

... or maybe he has worked with programmers who know their codes well
enough to write:

88  VALID-ALPHA VALUES 'A' THRU 'H', 'I' THRU 'R', 'S' THRU 'Z'.

... and rely on a sensible 88 rather than a 2-yr maintenance coder's being
familiar with Pic A?

DD
```

#### ↳ Re: Any need for PIC A ?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<956L1.1742$te.2584561@news2.mia.bellsouth.net>`
- **References:** `<68n$1@nnrp1.dejanews.com> <C9NK19410@news4.mia.bellsouth.net> <dbryantEz8MH7.9Dz@netcom.com>`

```
David K. Bryant wrote in message ...
>"Judson McClendon" <judmc123@bellsouth.net> writes:
>
…[8 more quoted lines elided]…
>of academic settings.

Having only read through various COBOL manuals cover to cover several
dozen times myself, in addition to thousands of hours of study, and
having taught dozens of programmers, that is an interesting statement
to read.  Perhaps you never considered that it is one thing to know
about an option, and how it works, and quite another to actually see
a need for it.

>Instead of letting the system enforce data integrity thru
>the use of PIC 9 or PIC A acceptance fields, they would
>rather code everything as PIC X and handle data integrity
>thru range selections.  If you're lucky.


How many situations can you enumerate where 'dirty data' would cause
a problem, but strictly garbage data, though alphanumeric, would work
correctly?  Non initialized data is, by definition, random, and can be
alphabetic, or numeric by chance.  The answer is to validate all input
data, not just for alpha or numeric, but with appropriate range and
specific value tests as well.  Declaring a field with PIC A is no
substitute for that.  The time to validate the data is when it is being
entered, while the user is looking at it, and has the source document
in front of them.  Not when a batch program is being run at 2AM the next
morning.  And not by bombing a program.  You bomb a program because of
internal data corruption, not invalid input data.

Even if the compiler did test for alphabetic, why would you want the
compiler to generate an alphabetic test for every single move you did
to a PIC A item?  Why would you want to bomb your program, rather than
print an error message?  Because you were too lazy to write code to
validate the data, or just don't know better?  Looks like you never
worked with programmers with enough experience to know how it should
be done, outside of what their professors told them.  Most professors
have zip real world experience.

>I spend a part of my week troubleshooting problems that often
>turn out to be related to dirty data.... uninitialized
>Working Storage, input into PIC X when the only valid values
>are numeric, etc.


Any *you* talk about being around programmers who know what their
doing?

>Typical:  Need to input all-numeric Social Security Numbers,
>telephone numbers, or ZIP (postal) codes.  Sure, we'll just
>input into a PIC X and then write a look to scan and check
>each digit for 0-9 content....  but they get lazy and leave
>out the part following "and then".


You think it is better to input the data directly into PIC 9 fields
and bomb the program, than input it into PIC X fields and validate
it?  Anyway, who said anything about numeric data?  The discussion
is about PIC A.  There are many reasons to use PIC 9.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
