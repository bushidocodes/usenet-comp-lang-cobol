[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Anybody have alogrithum to caluclate the day of the week given the date

_6 messages · 6 participants · 1997-08_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Anybody have alogrithum to caluclate the day of the week given the date

- **From:** "ram..." <ua-author-16628599@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5s21ia$s6b@newsfep1.sprintmail.com>`

```

I am working on a class assingment at Depaul Univ

I am looking for an algorithim that given the date (i.e. 08/12/1997) will
tell me what day of the week it is. Reason is if the day is a weekend I
do not want to give the user access to certain functions.

Any example of code to determine day of week given date would be greatly
appreciated. I have looked everywhere and have not found an example
```

#### ↳ Re: Anybody have alogrithum to caluclate the day of the week given the date

- **From:** "bill - netcom" <ua-author-17071652@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fece407b3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5s21ia$s6b@newsfep1.sprintmail.com>`
- **References:** `<5s21ia$s6b@newsfep1.sprintmail.com>`

```

Method 1 -
Rough and ready calculation - general formula only, will need
debugging. Its been years since I had to write this code..

1 Jan 1950 = Monday (thank you Quicken) (a better starting point is 1st
Jan 1900, but I couldn't be bothered scrolling that far back in Quickens
calendar - but then I don't need the grades )

1 year = 365 days = 52 weeks + 1 day. so each 'year' January 1st
advances by 1 day

1 Jan 1950 = Monday
1 Jan 1951 = Tuesday etc

leap years have an extra day, so the year after a leap year, January 1st
advances by 2 days

have a look up table of the cumulative number of days from the start of
the year;

January = 31
February = 59 etc

Step1 - determine the day of the week that Jan 1st falls on

= current year - 1950
+ number of leap years between the 2 dates
/ 7 to find the number of days to advance the 1950 start date

- test this by printing out the day of the week for Jan 1st from
1950 onwards..

Step 2 - determine the number of days since Jan 1st

use the look up table to determine the number of days since the
start of the year for any given month


Method 2
- check if your compiler has a 'day of the week' function


Tony wrote:

› I am working on a class assingment at Depaul Univ
› 
…[8 more quoted lines elided]…
›   appreciated.  I have looked everywhere and have not found an example
```

#### ↳ Re: Anybody have alogrithum to caluclate the day of the week given the date

- **From:** "pdubois" <ua-author-15560036@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fece407b3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5s21ia$s6b@newsfep1.sprintmail.com>`
- **References:** `<5s21ia$s6b@newsfep1.sprintmail.com>`

```

Tony,

Why are you taking this course if you can't solve the problem on your
own? There are probably over a 1000 ways to solve this problem, your
assignment is to find one of them, and in the process hopefully learn
something.

Where I work, we would never write this routine from scratch. We
would use code that was already written. The exception to this is if
the previous written code was buggy or inefficient.

I sympathize with your plight, as writing routines that you know 100's
of people have already written is boring. I offer you some words of
advice. I am a programmer and only 20 - 30% of my time is spent
coding. The other time is spent SOLVING PROBLEMS. Try to write the
routine to just get it working. Then try to make it better. Don't
try to write the best code the first time. Just get something going,
and you will then see how to improve it. If you are hopelessly stuck,
I would be willing to help, or you can find a tutor.


Take it easy,

Paul



ram··.@spr··l.com (Tony) wrote:

› I am working on a class assingment at Depaul Univ
›  
…[5 more quoted lines elided]…
›  appreciated.  I have looked everywhere and have not found an example

To reply by email, remove the words NO*SPAM from my
email address. Thanks.
```

#### ↳ Re: Anybody have alogrithum to caluclate the day of the week given the date

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fece407b3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5s21ia$s6b@newsfep1.sprintmail.com>`
- **References:** `<5s21ia$s6b@newsfep1.sprintmail.com>`

```

Tony wrote:
› 
› I am working on a class assingment at Depaul Univ
…[6 more quoted lines elided]…
›   appreciated.  I have looked everywhere and have not found an example

I've had to do this a couple of times in my career. The first time was
my very first professional programming assignment, and I was given the
source code to a 370 Assembler program and asked to implement the
algorithm in ANSI-74 COBOL on an IBM Series/1. I didn't understand why
the mathematical formula worked, but I was able to test if for a wide
enough range of dates for the application.

A year ago I had to do it again in COBOL, so I figured one out. A
general approach is to calculate the number of days from some base date
for which the day of week is known, and then do modulo-7 arithmetic
(DIVIDE GIVING REMAINDER) to obtain a code for the day of week.

It is not trivial to determine the number of days since Monday
01/01/1601, for example, but once you can do that, it is easy to
determine the day-of-week.

Just remember than a standard 400-year epoch (like 01/01/1601 to
12/31/2000) always begins on a Monday and ends on a Sunday. It has
146,107 days and is evenly divisible by 7. A normal century is missing
a leap year for the year ending in 00, so it has 36,524 days. A
four-year period with one leap year has 1461 days.

I think it's actually much more difficult to convert a number of days
from a base date back into a MM/DD/YYYY date.

I've seen assembler programs that figure day-of-week using MM/DD/YY, but
they assume you are starting with Monday, 01/01/1900, and they sometimes
have bugs because 1900 was not a leap year. 1900 is evenly divisible by
100, but not by 400, so it was not a leap year. 2000 is evenly
divisible by 400, so it is a leap year.

Does your instructor want you to develop your own algorithm, or simply
implement someone else's algorithm?

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Anybody have alogrithum to caluclate the day of the week given the date

- **From:** "geo" <ua-author-14677@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fece407b3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5s21ia$s6b@newsfep1.sprintmail.com>`
- **References:** `<5s21ia$s6b@newsfep1.sprintmail.com>`

```

Tony wrote:
›
› I am working on a class assingment at Depaul Univ
Here is a program that I wrote just last week for my Pascal class.
While it is not what you need and I personally know nothing of
COBOL yet (until September at least), perhaps you can glean
an idea here. This program takes the user input in the form
MMM DD, YYYY and converts it the days on the Julian calendar.
It also traps for leap years (although I just learned from
the post of Arnold Trembley that [1900 mod 4 = 0] is not a
leap year!). I used two arrays (is that similar to a lookup
table in COBOL?) to convert to days. The Days array is
somewhat similar to what Bill-Netcom says about accumulating
the days of the year. Remember that if you do have a leap
year, you don't add a day until in the case of my program:
index(of the array) > 2. Meaning you have a date that is
March 1 or 'greater.'

Geo



Program JulianDays;
Uses Crt;
Type
MonthType = Array[1..12] of String; {Setup a couple of arrays to
store}
DayType = Array[1..12] of Integer; {months and corresponding no
of days}
Const {Use constants so you can just
pluck
out a value}
Days : DayType = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273,
304, 334);
Months : MonthType = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec');
Var
Input : String; {User input}
Error : Integer; {use for val error output}
Ch1 : Char; {use with readkey}
Month : String; {these next three vars will temporarily}
Day : Integer; {store values for what they say}
Year : Integer;
JulDays : Integer; {store value for Julian days}
x, Index : Integer; {use x in a for loop, Index as for an array
element}
LeapYear : Integer; {use when determining whether or not leap year}
ErrorCode: Integer; {use in error checking}
Begin
Repeat
ClrScr;
WriteLn('Please enter a date to be converted to a Julian date');
Write('in the following format (MMM DD, YYYY), ex: Jan 1, 1980:
');
ReadLn(Input); {get user input}
WriteLn('You have entered: ', Input,'.'); {tell user what he
entered}

If (Length(Input) = 11) Then
Begin
Month := Copy(Input, 1, 3); {store the first 3 characters
in Month}

Val(Copy(Input, 5, 1), Day, Error);{Check for numeric input
and}
If Error > 0 Then {store the 5th character
as Day}
ErrorCode := 1; {This will be used throughout for bad
input}
Val(Copy(Input, 8, 4), Year, Error);{Check for numeric
input and}
If Error > 0 Then {store last 4 characters as Year}
ErrorCode := 1;
End
Else
If (Length(Input) = 12) Then
Begin
Month := Copy(Input, 1, 3); {store the first 3
characters in Month}
Val(Copy(Input, 5, 2), Day, Error);{Check for numeric
input and}
If Error > 0 Then {store the 5th + 6th characters as
Day}
ErrorCode := 1;
Val(Copy(Input, 9, 4), Year, Error);{Check for numeric
input and}
If Error > 0 Then {store the last 4 characters as
Year}
ErrorCode := 1;
End
Else {input is incorrect}
Begin
ErrorCode := 1
End;

Index := 0; {Initialize this variable}
For x := 1 To 12 do {Use a for loop to get the array index}
Begin {of the Month entered}
If (Month = Months[x]) Then
Begin
Index := x;
End;
End;
If (Index = 0) Then {incorrect input}
Begin
ErrorCode := 1;
End;

JulDays := Days[Index] + Day; {index the Days array for a
numeric value}
If (Year mod 4 = 0) Then {and add the
value of Day}
LeapYear := 1 {If a leap year is entered}
Else
LeapYear := 0;
If (Index > 2) Then {If the date is March 1 or later then 0 is
added for a}
JulDays := JulDays + LeapYear;{non-leap year and 1 added for a
leap year}
If ErrorCode = 1 Then {If any input is incorrect}
Begin
WriteLn('You have a data entry error');
ErrorCode := 0; {Set this to 0 in case input is correct
next time}
WriteLn('Please press the Enter key to continue.');
Ch1 := Readkey;
End
Else {If the input is correct}
Begin
WriteLn('That translates to ', JulDays, ' days on the Julian
Calendar.');
Write('Would you like to try another number (y/n)?');
Ch1 := Readkey;
End;
Until (Ch1 = 'n') or (Ch1 = 'N') {n or N ends the loop}
End.
```

#### ↳ Re: Anybody have alogrithum to caluclate the day of the week given the date

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-08-04T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fece407b3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5s21ia$s6b@newsfep1.sprintmail.com>`
- **References:** `<5s21ia$s6b@newsfep1.sprintmail.com>`

```

ram··.@spr··l.com (Tony) wrote:
› I am working on a class assingment at Depaul Univ
› 
…[5 more quoted lines elided]…
›  appreciated.  I have looked everywhere and have not found an example

Is it possible that the purpose of the assignment was to write your own?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
