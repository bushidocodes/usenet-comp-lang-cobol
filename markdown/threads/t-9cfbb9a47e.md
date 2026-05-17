[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Illegal character in numeric field.

_6 messages · 6 participants · 1998-02_

---

### Illegal character in numeric field.

- **From:** "craig nass" <ua-author-17074983@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34e3f3e8.0@news3.ibm.net>`

```

I'm working in Win 95 with MF Personal COBOL.
Not Cobol, I'm told.

I can read in the following data fields and display them with no problem.


01 PhoneData.
05 FIRSTNAME PIC X(20).
05 ADDRESS-IN PIC X(20).
05 PAST-KILO-USAGE PIC 99999.
05 PIC X(5).
05 CURRENT PIC 99999.
05 PIC X(7).
05 CHARGE PIC V99.

01 temp-inv-out PIC 99999 VALUE 0.

I need to perform a calculation with CURRENT.

COMPUTE TEMP-INV-OUT = 2 + CURRENT

But I then get the illegal character message.

This is a sample of the data. I've checked and I am not reading out of the
range of the data.
So, what is the illegal character?


BART SIMPSON 1423 FRANGO ST. 69440 70000 08
HENRY HIGGINS 783 ASH ST. 68403 70893
07
JANE WYMAN 1202 CHERRY ST. 98000 05400 08
FRED MACMURRAY 1818 MOLTON AVE. 30303 30600 08
JAYNE MANSFIELD 234 GREEN ST. 50004 51000 08
FRED MERTZ 4040 ELM ST. 99200 00600
07
HERMAN MUNSTER 8010 SCARY AVE. 80403 81224 08
SARAH LAWRENCE 2242 WHIP LANE 00800 02000 07
RICKY NELSON 505 MEIGS ST. 95000 00000
07
JIM BACKUS 1234 EASTERN AVE 67884 67999 08
MYRNA LOY 080 HOTSHOT LANE 78003 79200 08


I cannot move any of the numeric fields either- unless I reset the source
and destination to PIC X.

Thanks

Craig.
```

#### ↳ Re: Illegal character in numeric field.

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cfbb9a47e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34e3f3e8.0@news3.ibm.net>`
- **References:** `<34e3f3e8.0@news3.ibm.net>`

```

Hi Craig,

Craig Nass wrote:
› I can read in the following data fields and display them with no problem.
› 
…[5 more quoted lines elided]…
›            05 CURRENT                     PIC 99999.
Insert the following here:
05 CURRENT-X REDEFINES CURRENT PIC XXXXX.
›            05                                     PIC X(7).
›            05 CHARGE                      PIC V99.
…[10 more quoted lines elided]…
› range of the data.
 
› Which of the samples produces the error ?
 
› So, what is the illegal character?

Make the above change, then put a "DISPLAY CURRENT-X" before the
compute.
What does it display ?

Cheers,
Kev.
```

#### ↳ Re: Illegal character in numeric field.

- **From:** "bbell..." <ua-author-1898047@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cfbb9a47e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34e3f3e8.0@news3.ibm.net>`
- **References:** `<34e3f3e8.0@news3.ibm.net>`

```

Craig wrote....
› I'm working in Win 95 with MF Personal COBOL.
› Not Cobol,  I'm told.
…[49 more quoted lines elided]…
› 

Which editor did you use to create this file? You might want to use
"ORGANIZATION IS LINE SEQUENTIAL" In your select statement.

Good luck

Bosun

BBe··.@a··.com
http://members.aol.com/bbello5778/bosun.htm
Programmer/Analyst. Bloomington, IL
```

#### ↳ Re: Illegal character in numeric field.

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cfbb9a47e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34e3f3e8.0@news3.ibm.net>`
- **References:** `<34e3f3e8.0@news3.ibm.net>`

```

Craig
"Run Time System Message 163 : Illegal character in numeric field.
By default the value which you enter into a numeric or numeric-edited field
is checked to ensure that it is numeric. You have entered either nonnumeric
characters or uninitialized numerics into numeric or numeric-edited fields:
these are automaticcllly space filles and are thus classified as nonnumeric
items." Probably you haven't Initialized your fields.
i.e.: Initialize Current.
David

Craig Nass wrote in message <34e··.@new··m.net>...
› I'm working in Win 95 with MF Personal COBOL.
› Not Cobol,  I'm told.
…[20 more quoted lines elided]…
›
```

#### ↳ Re: Illegal character in numeric field.

- **From:** "edw" <ua-author-7163589@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cfbb9a47e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34e3f3e8.0@news3.ibm.net>`
- **References:** `<34e3f3e8.0@news3.ibm.net>`

```

If you query the value of CURRENT in the animator in hex, you will probably
find it contains 20 20 20 20 20h, which is spaces, and that's your illegal
character. You can either give CURRENT a value 0 clause (you see, you were
on the right track with TEMP-INV-OUT), or initialize it or it's group item
PHONEDATA. It's odd that the initial state of a numeric field should be
spaces, but I'm pretty sure it's because ANSI told them to do it that way.

›         01 PhoneData.
›            05 CURRENT                     PIC 99999.
…[8 more quoted lines elided]…
›
```

#### ↳ Re: Illegal character in numeric field.

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-02-20T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9cfbb9a47e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<34e3f3e8.0@news3.ibm.net>`
- **References:** `<34e3f3e8.0@news3.ibm.net>`

```

Craig Nass wrote:
› 
› I need to perform a calculation with CURRENT.
…[15 more quoted lines elided]…
› FRED MERTZ                     4040 ELM ST.              99200     00600

The erratic way this is spaced suggests to me that you have some tabs in
your data where you should have some spaces. Try DISPLAYing the
individual fields before you do math.

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 29th Term Revealed (!?):
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
