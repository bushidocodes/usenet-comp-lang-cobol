[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# My lab is DUE!!!

_9 messages · 6 participants · 1996-08_

---

### My lab is DUE!!!

- **From:** "jeffe'" <ua-author-17087334@usenetarchives.gap>
- **Date:** 1996-08-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<320FAAA6.5EB5@instat.com>`

```

Help me please,

My lab is due and I can't get it to work!

Here's the situation:
1. I need to generate a unique ID number for a record.
2. The ID must consist of the following:
A. 7 digit number representing the current date including the
century (YYYYDDD).
B. A two digit counter.

I know how to increment the counter, but, I keep getting an error when
checking that says "Integer Required".

I'm trying to use this syntax:

WORKING-STORAGE SECTION.
01 THIS-DATE.
05 THIS-YR PIC 9(04).
05 THIS-MO PIC 9(02).
05 THIS-DY PIC 9(02).

01 PROJ-ID.
05 JULIAN PIC 9(07).
05 OTHER-PART PIC 9(02).
...
MOVE FUNCTION CURRENT-DATE TO THIS-DATE.
COMPUTE JULIAN =
FUNCTION DAY-OF-INTEGER (FUNCTION INTEGER-OF-DATE
(THIS-DATE)).

This is the same exact syntax that is in my book and I keep getting the
error "Integer Required".

What's wrong?
```

#### ↳ Re: My lab is DUE!!!

- **From:** "guyf..." <ua-author-17071752@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p2@usenetarchives.gap>`
- **In-Reply-To:** `<320FAAA6.5EB5@instat.com>`
- **References:** `<320FAAA6.5EB5@instat.com>`

```

Jeffe' wrote:

› Help me please, 
 
› My lab is due and I can't get it to work!
 
› Here's the situation:
› 1. I need to generate a unique ID number for a record.
…[3 more quoted lines elided]…
› 	B. A two digit counter.
 
› I know how to increment the counter, but, I keep getting an error when
› checking that says "Integer Required".
 
› I'm trying to use this syntax:
› 
…[5 more quoted lines elided]…
› 
 
› 	01  THIS-DATE		PIC 9(8).
 
› 01 PROJ-ID.
› 	05 JULIAN	PIC 9(07).
…[5 more quoted lines elided]…
› 				(THIS-DATE)).
 
› This is the same exact syntax that is in my book and I keep getting the
› error "Integer Required".
 
› What's wrong?


Try using the above change to your working-storage. A group item is
defined as alphanumeric, even if all its' elements are integer. If you
need to reference the year, month or day, you can always use reference
modification.
```

##### ↳ ↳ Re: My lab is DUE!!!

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-08-14T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f04bada629-p2@usenetarchives.gap>`
- **References:** `<320FAAA6.5EB5@instat.com> <gap-f04bada629-p2@usenetarchives.gap>`

```

guy··.@ind··o.ie (Guy C. Fountain) wrote:
› Jeffe'  wrote:
› 
…[44 more quoted lines elided]…
› 

If you had tested this incorrect code before posting it, you would realize
that it places the LOW-order eight characters of the function's return value
in THIS-DATE. These eight characters aren't even all numeric.

The function CURRENT-DATE returns a 21-character STRING value consisting of
1-4 year
5-6 month
7-8 day
9-10 hours past midnight
11-12 minutes
13-14 seconds
15-16 hundredths of seconds
17 relationship to Greenwich Mean Time ( "-" or "+")
18-19 hours ahead/behind GMT
20-21 additional minutes ahead/behind GMT
```

#### ↳ Re: My lab is DUE!!!

- **From:** "lma..." <ua-author-17086820@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p4@usenetarchives.gap>`
- **In-Reply-To:** `<320FAAA6.5EB5@instat.com>`
- **References:** `<320FAAA6.5EB5@instat.com>`

```

Jeffe',

I misled you in my previous reply. The fields do not have to be coded
as COMP to be handled correctly. COBOL handles the data conversion.
The referenced data names have to be numeric, and group levels default
to alpha-numeric fields.

Larry
```

#### ↳ Re: My lab is DUE!!!

- **From:** "lma..." <ua-author-17086820@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p5@usenetarchives.gap>`
- **In-Reply-To:** `<320FAAA6.5EB5@instat.com>`
- **References:** `<320FAAA6.5EB5@instat.com>`

```

In article <320··.@ins··t.com>, From Jeffe' ,
the following was written:
› Help me please, 
› 
…[33 more quoted lines elided]…
› What's wrong?

The basic problem has to with data format. The functions that you are
using in the JULIAN computation must be integers which are defined as
COMP. Also the CURRENT-DATE function returns more than just the date,
so I changed that also. Here is the code that I compiled and ran to get
what I believe you are looking for. Hope this helps.

Larry

IDENTIFICATION DIVISION.
PROGRAM-ID. TESTPGM.
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. IBM-PC.
OBJECT-COMPUTER. IBM-PC.

DATA DIVISION.

WORKING-STORAGE SECTION.

01 CURR-DATE-STUFF.
05 CURR-DATE PIC 9(8).
05 FILLER PIC X(13).

01 THIS-DATE PIC 9(8) COMP.

01 PROJ-ID.
05 JULIAN PIC 9(07) COMP.
05 OTHER-PART PIC 9(02).

PROCEDURE DIVISION.

MOVE FUNCTION CURRENT-DATE TO CURR-DATE-STUFF.
MOVE CURR-DATE TO THIS-DATE.
DISPLAY THIS-DATE.
COMPUTE JULIAN =
FUNCTION DAY-OF-INTEGER (FUNCTION INTEGER-OF-DATE
(THIS-DATE)).
DISPLAY JULIAN.
```

##### ↳ ↳ Re: My lab is DUE!!!

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-08-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f04bada629-p5@usenetarchives.gap>`
- **References:** `<320FAAA6.5EB5@instat.com> <gap-f04bada629-p5@usenetarchives.gap>`

```

lma··.@cr··s.com (Larry Martin) wrote:
› In article <320··.@ins··t.com>, From Jeffe' ,
› the following was written:
…[39 more quoted lines elided]…
› COMP.

This is not completely correct. The fields must be integers, yes, but there
is no requirement that they be USAGE COMP.

› Also the CURRENT-DATE function returns more than just the date,
› so I changed that also. Here is the code that I compiled and ran to get
› what I believe you are looking for. Hope this helps.
›

Actually, he's using this properly, I think -- since he's returning the value
into an alphanumeric data item, it's truncated on the right, which produces
the desired result. His problem is simply that he needs to redefine those
eight bytes as PIC 9(8) before trying to use them as input to the next
function call. There's no need to copy that to a COMP field.

› Larry
› 
…[30 more quoted lines elided]…
›
```

#### ↳ Re: My lab is DUE!!!

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p7@usenetarchives.gap>`
- **In-Reply-To:** `<320FAAA6.5EB5@instat.com>`
- **References:** `<320FAAA6.5EB5@instat.com>`

```

Jeffe' wrote:
+Help me please,
+
+My lab is due and I can't get it to work!
+
+Here's the situation:
+ 1. I need to generate a unique ID number for a record.
+ 2. The ID must consist of the following:
+ A. 7 digit number representing the current date including the
+century (YYYYDDD).
+ B. A two digit counter.
+
+I know how to increment the counter, but, I keep getting an error when
+checking that says "Integer Required".
+
+I'm trying to use this syntax:
+
+WORKING-STORAGE SECTION.
+ 01 THIS-DATE.
+ 05 THIS-YR PIC 9(04).
+ 05 THIS-MO PIC 9(02).
+ 05 THIS-DY PIC 9(02).
*********** add this here
01 this-date-n REDEFINES this-date PIC 9(8).
**************************************************************************
+
+ 01 PROJ-ID.
+ 05 JULIAN PIC 9(07).
+ 05 OTHER-PART PIC 9(02).
+....
+ MOVE FUNCTION CURRENT-DATE TO THIS-DATE.
+ COMPUTE JULIAN =
+ FUNCTION DAY-OF-INTEGER (FUNCTION INTEGER-OF-DATE
**************************************** and change this
+ (THIS-DATE)).
********************************************* to this:
(this-date-n)).


+This is the same exact syntax that is in my book and I keep getting the
+error "Integer Required".
+
+What's wrong?

The book's author didn't test everything he wrote -- a common affliction
even (particularly?) among experienced programmers.
```

#### ↳ Re: My lab is DUE!!!

- **From:** "andy styles" <ua-author-8438810@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p8@usenetarchives.gap>`
- **In-Reply-To:** `<320FAAA6.5EB5@instat.com>`
- **References:** `<320FAAA6.5EB5@instat.com>`

```

Jeffe' wrote:

› WORKING-STORAGE SECTION.
›         01 THIS-DATE.
›                 05 THIS-YR      PIC 9(04).
›                 05 THIS-MO      PIC 9(02).
›                 05 THIS-DY      PIC 9(02).

I think this is where your problem lies. Any GROUP level item (such as
your "01 THIS-DATE" is considered to be a character field. You need to
change it as follows:

01 THIS-DATE-CHAR.
05 THIS-YR PIC 9(04).
05 THIS-MO PIC 9(02).
05 THIS-DY PIC 9(02).
01 THIS-DATE REDEFINES THIS-DATE-CHAR PIC 9(8).

Then it'll work.

You also need to change the MOVE statement to be :

MOVE FUNCTION CURRENT-DATE TO THIS-DATE-CHAR.

Hope this helps!!

Andy Styles. 

     /o/-------------------------------------/o/
    /o/ EMail: usf··.@ibm··l.com (work)  /o/
   /o/       and··.@dir··o.uk  (home)   /o/  
   \o\. . . . . . . . . . . . . . . . . . .\o\
   /o/ My opinions are my own, and do not  /o/
  /o/ reflect those of Ford Motor Company /o/
```

#### ↳ Re: My lab is DUE!!!

- **From:** "je..." <ua-author-17087196@usenetarchives.gap>
- **Date:** 1996-08-13T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f04bada629-p9@usenetarchives.gap>`
- **In-Reply-To:** `<320FAAA6.5EB5@instat.com>`
- **References:** `<320FAAA6.5EB5@instat.com>`

```

Thanks for all your help. I chose to use a REDEFINES clause and it worked.
It is great to see that the Inet can be such a powerful tool!

Jeffe'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
