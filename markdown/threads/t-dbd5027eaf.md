[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Implied decimal in amount field

_12 messages · 6 participants · 1998-10_

---

### Implied decimal in amount field

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3626F132.286F@bellsouth.net>`

```
My program reads a file with an amount field of PIC 9(8)V99 in the
record.  I list any records with amounts over $9,999.99.  

I changed the input field to PIC 9(10) and if the input amount was
greater than 999999, I moved it to the edited report line, which was
WRONG.  Then I set up a working-storge field, WS-AMT  PIC 9(8)V99, moved
the INPUT-AMT  PIC 9(10) to WS-AMT, and moved that to the edited field,
which was WRONG.  (Is it even legal to move to a field with an implied
decimal??)

I'm wondering about a redefines on the input amount field,

05  INPUT-AMT      PIC 9(10).
05  INPUT-AMT-R REDEFINES INPUT-AMT
                   PIC 9(8)V99.

05  EDITED-AMT     PIC ZZ,ZZZ,ZZ9.99.

IF INPUT-AMT GREATER THAN 999999
    MOVE INPUT-AMT-R TO  EDITED-AMT.

- OR - Could I do this:

05  INPUT-AMT      PIC 9(8)V99.
05  INPUT-AMT-X REDEFINES INPUT-AMT
                   PIC X(10).

IF INPUT-AMT-X GREATER THAN '999999'
    MOVE INPUT-AMT TO EDITED-AMT.

- OR - what??

kitty
```

#### ↳ Re: Implied decimal in amount field

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gGV1.26087$lp3.2402368@news2.mia.bellsouth.net>`
- **References:** `<3626F132.286F@bellsouth.net>`

```
Kitty Carr wrote:
>My program reads a file with an amount field of PIC 9(8)V99 in the
>record.  I list any records with amounts over $9,999.99.

Kitty, you answered your own question right there.  If the input data
is formatted as 9(8)V99, then use that for the PICTURE.  Then compare
it to numeric literal 9999.99.

   05  INPUT-AMT      PIC 9(8)V99.

   05  EDITED-AMT     PIC ZZ,ZZZ,ZZ9.99.

   IF INPUT-AMT GREATER THAN 9999.99
       MOVE INPUT-AMT TO  EDITED-AMT.

Sure, you can move to fields with assumed decimal points.  If you
couldn't, we would all be a lot of trouble. :-)

P.S. -I know you have ordered it already, but for your info, the
      Books-A-Million at Eastwood Mall has "COBOL Unleashed".
```

##### ↳ ↳ Re: Implied decimal in amount field

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36276CB7.68F5@bellsouth.net>`
- **References:** `<3626F132.286F@bellsouth.net> <8gGV1.26087$lp3.2402368@news2.mia.bellsouth.net>`

```
Judson McClendon wrote:
> 
> Kitty Carr wrote:
…[12 more quoted lines elided]…
>        MOVE INPUT-AMT TO  EDITED-AMT.

This is the one way I DIDN'T try.  I said greater than 999999 (without
the decimal point); I thought if I wrote greater than 9999.99, I'd get
an error when it hit the period, thinking (thinking?) it was the end of
the statement.  I mean, unless it was in quotes.  And that's what I get
for thinking . . .

Thanks.
```

#### ↳ Re: Implied decimal in amount field

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36275897.75BD6ECD@home.com>`
- **References:** `<3626F132.286F@bellsouth.net>`

```
Just curious, why do any redefines at all for this problem?  The
compiler knows about the inplied decimal.  Just compare your amount to
9999.99!

Kitty Carr wrote:
> 
> My program reads a file with an amount field of PIC 9(8)V99 in the
…[7 more quoted lines elided]…
> decimal??)
```

#### ↳ Re: Implied decimal in amount field

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com>`
- **References:** `<3626F132.286F@bellsouth.net>`

```
On Fri, 16 Oct 1998 05:15:16, Kitty Carr <kcarr1@bellsouth.net> wrote:

> My program reads a file with an amount field of PIC 9(8)V99 in the
> record.  I list any records with amounts over $9,999.99.  
…[18 more quoted lines elided]…
> 

Let's look at this a second.  If the actual value of input-amt is 
888,888.99

It is NOT greater than 999999 but you will still move it because 
Input-Amt will equal 88888899.  Instead:

If Input-Amt-R > 999999 
   Move Input-Amt-R to Edited-Amt.

Should work fine.
```

##### ↳ ↳ Re: Implied decimal in amount field

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3627AC43.5054@bellsouth.net>`
- **References:** `<3626F132.286F@bellsouth.net> <Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
> On Fri, 16 Oct 1998 05:15:16, Kitty Carr <kcarr1@bellsouth.net> wrote:
…[32 more quoted lines elided]…
> Should work fine.


That's the first thing I did before I changed pic 9(8)v99 to pic 9(10). 
But when I tried:


INPUT-AMT    PIC 9(8)V99.

EDITED-AMT   PIC ZZ,ZZZ,ZZ9.99.

IF INPUT-AMT GREATER THAN 999999
    MOVE INPUT-AMT TO EDITED-AMT,

then the edited field (using your example of 888,888.99) looked like
this 88,888,899.00.  Oh, wait - sorry, that's what you just said! 
  
But if you say IF INPUT-AMT-R GREATER THAN 999999
                   MOVE INPUT-AMT-R TO EDITED-AMT,

isn't that saying the same thing, since INPUT-AMT-R is PIC 9(8)V99? I'm
having a mental block about these implied decimal points.  Well, I can't
do anything until Monday, anyway.
```

###### ↳ ↳ ↳ Re: Implied decimal in amount field

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-wod1mJM40lKd@Dwight_Miller.iix.com>`
- **References:** `<3626F132.286F@bellsouth.net> <Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com> <3627AC43.5054@bellsouth.net>`

```
On Fri, 16 Oct 1998 18:33:25, Kitty Carr <kcarr1@bellsouth.net> wrote:

>> That's the first thing I did before I changed pic 9(8)v99 to pic 
9(10). 
> But when I tried:
> 
…[7 more quoted lines elided]…
> 

This should have worked fine! IIt will align the implied decimal with 
the actual decimal.  Check how the value got moved into Input-Amt. - 
There is nothing wrong with what you have here.
```

###### ↳ ↳ ↳ Re: Implied decimal in amount field

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HP_V1.26829$lp3.2960865@news2.mia.bellsouth.net>`
- **References:** `<3626F132.286F@bellsouth.net> <Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com> <3627AC43.5054@bellsouth.net> <Jl0PnHJ5PvPd-pn2-wod1mJM40lKd@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
>Kitty Carr wrote:
>
…[12 more quoted lines elided]…
>There is nothing wrong with what you have here.


The original post is mostly gone by now, but the problem is because
Kitty needed to test for > 9999.99, not > 999999.  I believe she was
concerned that the actual decimal point in the literal would not compare
properly with the assumed decimal point in the PIC, and that is why
she was trying those other forms.
```

###### ↳ ↳ ↳ Re: Implied decimal in amount field

_(reply depth: 5)_

- **From:** ShatTCat@ymg.SPAM.urban.ME.ne.NOT.jp (Shat T Cat)
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3635eeab.8607093@nntp.urban.ne.jp>`
- **References:** `<3626F132.286F@bellsouth.net> <Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com> <3627AC43.5054@bellsouth.net> <Jl0PnHJ5PvPd-pn2-wod1mJM40lKd@Dwight_Miller.iix.com> <HP_V1.26829$lp3.2960865@news2.mia.bellsouth.net>`

```
On Sat, 17 Oct 1998 11:03:03 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

:Thane Hubbell wrote:
:>Kitty Carr wrote:
:>
:>>> That's the first thing I did before I changed pic 9(8)v99 to pic 9(10).
:>> But when I tried:
:>>
:>> INPUT-AMT    PIC 9(8)V99.
:>>
:>> EDITED-AMT   PIC ZZ,ZZZ,ZZ9.99.
:>>
:>> IF INPUT-AMT GREATER THAN 999999
:>>     MOVE INPUT-AMT TO EDITED-AMT,

:>This should have worked fine! IIt will align the implied decimal with
:>the actual decimal.  Check how the value got moved into Input-Amt. -
:>There is nothing wrong with what you have here.

:The original post is mostly gone by now, but the problem is because
:Kitty needed to test for > 9999.99, not > 999999.  I believe she was
:concerned that the actual decimal point in the literal would not compare
:properly with the assumed decimal point in the PIC, and that is why
:she was trying those other forms.

     Personally, I would put a variable within the Working Storage
section to hold that value.  It would then eliminate the problem at
hand and make it easier to find if the value were to change in the
future.
```

###### ↳ ↳ ↳ Re: Implied decimal in amount field

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y0oX1.725$Se2.1325573@news4.mia.bellsouth.net>`
- **References:** `<3626F132.286F@bellsouth.net> <Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com> <3627AC43.5054@bellsouth.net> <Jl0PnHJ5PvPd-pn2-wod1mJM40lKd@Dwight_Miller.iix.com> <HP_V1.26829$lp3.2960865@news2.mia.bellsouth.net> <3635eeab.8607093@nntp.urban.ne.jp>`

```
Shat T Cat wrote:
>Judson McClendon wrote:
>:Thane Hubbell wrote:
…[25 more quoted lines elided]…
>future.

I agree.  Even better, use a constant if your compiler supports them.
```

###### ↳ ↳ ↳ Re: Implied decimal in amount field

_(reply depth: 7)_

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363BA33A.68F8@bellsouth.net>`
- **References:** `<3626F132.286F@bellsouth.net> <Jl0PnHJ5PvPd-pn2-Ldi0vQHgrKXr@Dwight_Miller.iix.com> <3627AC43.5054@bellsouth.net> <Jl0PnHJ5PvPd-pn2-wod1mJM40lKd@Dwight_Miller.iix.com> <HP_V1.26829$lp3.2960865@news2.mia.bellsouth.net> <3635eeab.8607093@nntp.urban.ne.jp> <Y0oX1.725$Se2.1325573@news4.mia.bellsouth.net>`

```
Judson McClendon wrote:
> 
> Shat T Cat wrote:
…[22 more quoted lines elided]…
> >:she was trying those other forms.

I had it in my mind that if I coded: 
    If input-amt greater than 9999.99
        move input-amt to edited-amt, the compiler would get an error at
the period like it was the period at the end of a statement.  Yep. 
That's what I thought.  And when I got to work I asked two others what
they thought.  They thought the same thing.  Hello!  This is YOUR tax
money at work!

> >
> >     Personally, I would put a variable within the Working Storage
…[4 more quoted lines elided]…
> I agree.  Even better, use a constant if your compiler supports them.

I would normally have defined it in Working-Storage, but this was one of
those We Just Need to Run This ONE Time, never again, which means, being
interpreted, We just need to run this once until the next time.   
> --
> Judson McClendon      judmc123@bellsouth.net  (remove numbers)
> Sun Valley Systems    http://personal.bhm.bellsouth.net/~judmc
> "For God so loved the world that He gave His only begotten Son, that
> whoever believes in Him should not perish but have everlasting life."

Thank you all for your help.
```

#### ↳ Re: Implied decimal in amount field

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1998-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<709v0o$fg_001@news.netdirect.net>`
- **References:** `<3626F132.286F@bellsouth.net>`

```
In article <3626F132.286F@bellsouth.net>,
   Kitty Carr <kcarr1@bellsouth.net> wrote:
+My program reads a file with an amount field of PIC 9(8)V99 in the
+record.  I list any records with amounts over $9,999.99.  
+
There have already been several very good responses to your question,
so I'll omit duplicating the effort here. But there was something else
that I felt should be pointed out.
[snip]
+
+- OR - Could I do this:
+
+05  INPUT-AMT      PIC 9(8)V99.
+05  INPUT-AMT-X REDEFINES INPUT-AMT
+                   PIC X(10).
+
+IF INPUT-AMT-X GREATER THAN '999999'
+    MOVE INPUT-AMT TO EDITED-AMT.
+
This will certainly _not_ work. An alphanumeric comparison between two 
operands of different lengths proceeds as if the shorter one is padded on the 
right with spaces to make it the same length as the longer one. Hence, the IF 
statement you propose is equivalent to
	IF INPUT-AMT-X GREATER THAN '999999~~~~' (~ = space)
If the numeric value of INPUT-AMT is, say, 10000.00, this will result in
comparing "0001000000" with "999999~~~~" and the program will conclude that
the second operand is greater than the first -- clearly not what you want.

IF INPUT-AMT-X GREATER THAN '0000999999' would produce the desired result.
But IF INPUT-AMT GREATER THAN 9999.99 is more clear and hence preferable.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
