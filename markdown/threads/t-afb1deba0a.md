[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# People using Micro Focus

_21 messages · 5 participants · 2010-01 → 2010-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### People using Micro Focus

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-01-16T23:14:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7rdhreFddcU1@mid.individual.net>`

```
Does anybody use Micro Focus COBOL (any version, procedural or OO) to access 
COM or Automation server code, or even to write a COM compliant server 
module? If you do, there is a COBOL sample program below, written in Fujitsu 
OO NetCOBOL that I would be very interested to see "translated" to Micro 
Focus. It is a very small program and shouldn't take anyone too long.

The Component Object Model provides an ideal platform for encapsulating 
functionality and making it available to other languages and platforms. As 
most of Microsoft Office is written as Automation servers, compliant with 
COM, it is also a very useful way to handle ACCESS, EXCEL, WORD and POWER 
POINT from within your own programs. Everything you can do manually with 
these packages can be done under program control, even from COBOL, via the 
COM interface. For example, the sample below is manipulating EXCEL, but it 
could equally well be ANY of the MS Office suite, as well as thousands of 
other COM compliant components.

If you accept this request, and have no objection, I'll place both sets of 
code on the cobol21 web site with suitable background and acknowledgement of 
source. I'll also wrap your code so it can be used with .NET if it isn't 
already a .NET Assembly.

Any takers?

 PROGRAM-ID.  XLTEST.
* written by Pete Dashwood, PRIMA Computing, (NZ) Ltd. January 2010.
* (some parts loosely based on Fujitsu sample code)
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 REPOSITORY.
     Class COM AS "*COM".
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01   ExcelProgID pic x(20) value "Excel.Application.12".

 01   objExcel      OBJECT REFERENCE COM.
 01   objWorkbooks  OBJECT REFERENCE COM.
 01   objWkBk       OBJECT REFERENCE COM.
 01   objWorksheets OBJECT REFERENCE COM.
 01   objCurrSheet  OBJECT REFERENCE COM.
 01   objSelectCell OBJECT REFERENCE COM.
 01   objRangeBegin OBJECT REFERENCE COM.
 01   objRangeEnd   OBJECT REFERENCE COM.
 01   objRange      OBJECT REFERENCE COM.
 01   objCell       OBJECT REFERENCE COM.
 01   objPageSetUp  OBJECT REFERENCE COM.

 01   CellLine         PIC S9(9) COMP-5.
 01   CellCol          PIC S9(9) COMP-5.
 01   COMTrue       PIC 1(1) BIT VALUE B"1".  *> Ugh!!!
 01   Print-Range-String PIC X(20).
 01   numDisplay    PIC 999.

 01 Test-Value         pic x(35) value "Print".
 PROCEDURE DIVISION.
 Main section.
 000.
*======================================================================
*  Activate Excel.
*======================================================================

     invoke COM "CREATE-OBJECT"
                         USING     ExcelProgID
                         RETURNING objExcel
     end-invoke
     invoke objExcel "SET-VISIBLE"
                         USING     COMTrue
     end-invoke
*======================================================================
*  Create a new Workbook
*======================================================================
*
     invoke objExcel "GET-WORKBOOKS"  *> Get the Workbook object.
                            RETURNING objWorkbooks
     end-invoke
     invoke objWorkbooks "Add"
                            RETURNING objWkbk
     end-invoke
     invoke objWkBk "Activate" end-invoke
*======================================================================
*  Create a new sheet in the new workbook and get a reference to it
*======================================================================
     invoke objWkBk "GET-WORKSHEETS"
                        RETURNING objWorksheets
     end-invoke
     invoke objWorksheets "Add"  *> makes the new sheet active also...
     end-invoke
     *> get a reference to the current sheet in the new workbook
     invoke objWkBk "GET-ACTIVESHEET"
            RETURNING objCurrSheet
     end-invoke
*======================================================================
*  Set the value for 1st - 10th Cell (A1 to J1) in the new sheet
*  We will print cells 1 - 7 but not the rest...
*======================================================================
     move 1 to CellLine.
     perform
        varying CellCol
           from 1
             by 1
          until CellCol > 10
            invoke objCurrSheet "GET-CELLS"
                     USING     CellLine CellCol
                     RETURNING objCell
            end-invoke
            move spaces to test-value
            if CellCol > 7
               move "Don't print" to test-value
               move CellCol to numDisplay
               move numDisplay to test-value (13:3)
            else
               move "Print" to test-value
               move CellCol to numDisplay
               move numDisplay to test-value (7:3)
            end-if

            invoke objCell "SET-VALUE"
                          USING     test-value
            end-invoke
     end-perform
*======================================================================
*  Select the 1st - 7th Cell in the 1st line (from A1 to J1).
*======================================================================
     move 1 to CellLine
     move 1 to CellCol               *> Get the beginning position of
     invoke objCurrSheet "GET-CELLS"   *> the Cell object.
                      USING     CellLine CellCol
                      RETURNING objRangeBegin
     end-invoke
     MOVE 1  TO CellLine
     MOVE 7 TO CellCol    *> Get the ending position of the
     invoke objCurrSheet "GET-CELLS"  *> Cell object.
                      USING     CellLine CellCol
                      RETURNING objRangeEnd
    end-invoke
     invoke objCurrSheet "GET-RANGE"
                      USING     objRangeBegin objRangeEnd
                      RETURNING objRange
     end-invoke
*======================================================================
*  Set the visible print area
*
*  This has to be in A1 style address format. Use the "Address"
*  property of the range to get this.
*======================================================================
     invoke objRange "GET-Address"
            returning Print-Range-String
     end-invoke
     *> Get a reference to the sheet's PageSetup
     invoke objCurrSheet "GET-PageSetUp"
            returning objPageSetUp
     end-invoke
     *> Add the visible print area to the sheet's PageSetup
     invoke objPageSetUp "SET-PrintArea"
            using Print-Range-String
     end-invoke
     *> At this point cells 1 - 7 appear on the spread sheet
     *> with a dotted frame around them
*======================================================================
*  Print the Cells...
*  uses the default printer.
*======================================================================
     invoke objCurrSheet "PrintOut"
     end-invoke
     *> ONLY the specified range is printed...

     .
 999.
     exit program
     .
 END PROGRAM XLTEST.


Pete
```

#### ↳ Re: People using Micro Focus

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-01-18T03:50:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net>`

```
On Jan 16, 10:14 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Does anybody use Micro Focus COBOL (any version, procedural or OO) to access
> COM or Automation server code, or even to write a COM compliant server
…[172 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

I tried compiling this. Had to change all of the comments (MF uses *>
for comments) then ran in to the definition of ComTrue as a problem.
MF doesn't recognise the PIC and I could not find anything to match
the Fujitsu definition.
```

##### ↳ ↳ Re: People using Micro Focus

- **From:** "john@wexfordpress.com" <john@wexfordpress.com>
- **Date:** 2010-02-03T06:25:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com>`

```
On Jan 18, 6:50 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> On Jan 16, 10:14 am, "Pete Dashwood"
>
…[182 more quoted lines elided]…
> the Fujitsu definition.

I don't recognize this program as being standard COBOL. If you want to
deal
with such esoterica as COM I would use the language that others use to
deal with
such matters. Specifically I don't find these constructs in any COBOL
document I have.
In general the recent attempts to make COBOL into some kind of object-
oriented language
lead us down the wrong path. I have been programming in COBOL for 42
years and I don't
recognize half the statements in the above code.

That defeats one of the purposes of any High Level Language:
 to be a language where programmer x can read, understand and modify a
program written by
programmer y.


John Culleton, CPP
```

###### ↳ ↳ ↳ Re: People using Micro Focus

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-03T09:39:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com>`

```
On Feb 3, 2:25 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
wrote:
> On Jan 18, 6:50 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>
…[207 more quoted lines elided]…
> - Show quoted text -

The only piece that I do not recognise as being standard cobol is the
COMtrue bit setting. Otherwise it appears to me to be as per the last
standard of Cobol.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-03T20:07:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oRqan.24043$Fe4.54@newsfe21.iad>`
- **In-Reply-To:** `<e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com> <e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com>`

```
Alistair wrote:
> On Feb 3, 2:25 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
> wrote:
…[5 more quoted lines elided]…
>>>> ENVIRONMENT DIVISION etc......
<snip> ....

>>That defeats one of the purposes of any High Level Language:
>> to be a language where programmer x can read, understand and modify a
…[8 more quoted lines elided]…
> standard of Cobol.

 >>>> 01   COMTrue       PIC 1(1) BIT VALUE B"1".  *> Ugh!!!

Well it does look like it might be specific to Fujitsu COBOL.

But what is the BIG DEAL ? I could be using Level 88's or 78's. Only 
last week I spoke to a Brit who has been in Canada since 1974, three 
months before me in 1975. He was using COBOL before he came across, and 
while currently in an analyst role, does program in Micro Focus.

I referred him to 'Level 78's'. He corrected me, "You mean Level 88's 
?". "No", I replied, "Level 78's". He wasn't aware of them - and yes Mr. 
Dinosaur, (programming 42 years), the Level 78 is a Micro Focus 
extension and EXTREMELY useful. I'm damn sure it would have been 
proposed to the Standards Committee by M/F.

Unfortunately their rep was not the sort of personality to push for its 
use. I recall from the only Standards meeting I ever visited, that was 
2000 at M/F's (Newbury, Berkshire, UK) HQ. A Dutch representative, nice 
guy and enthusiastic as hell pushed and pushed for some 30 minutes, 
emphasized by scribbling examples on a white board - I don't recall it 
now, but something about whether or not you could get away with not 
having a space after a literal name - he just kept going on and on until 
the dozen or so around the table gave in. (No it wasn't specifically no 
space after a literal - but something just as daft that he was pushing 
for :-).

Should I not use the following  ?

01 ls-Bool      pic x comp-5.
   88 isTrue	value 1.
   88 isFalse    value 0.

CALL/INVOKE "something" using xxxxx returning ls-Bool

if 	isTrue
	do this .....

else	do something else...
end-if

I don't really care whether or not it is Comp- 0, 1, 2, 3, 4, 5, 6, 
Comp-Sync, Comp5Length2 or Comp5Length6; I'll use what suits the 
occasion. And, I can't be bothered to check, but which of the above is 
so-called COBOL 85 or COBOL 2002 for that matter. I did use comp-3 and 
currently use comp-5 because it works hand in glove with the way Micro 
Focus have written their OO classes. (But OO 'attached' to COBOL - 
that's another topic for the dinosaur to attack).

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-06T01:51:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t2iisFb0mU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com> <e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com> <oRqan.24043$Fe4.54@newsfe21.iad>`

```
James J. Gavan wrote:
> Alistair wrote:
>> On Feb 3, 2:25 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
…[46 more quoted lines elided]…
>

Good story, Jimmy :-)

> Should I not use the following  ?
>
…[11 more quoted lines elided]…
>

That looks fine to me, as far as it goes.

(Personally, I use boolean flags as pic x because on IBM mainframes it 
generates better code (CLI - Compare logical Immediate, where the value it 
is comparing to can be stored in the same instruction, and on the Intel x86 
platform (my favourite) it is again a single compare (COMSB). Comp-5 is 
native architecture and would probably use arithmetic instructions instead. 
(I haven't checked so can't be sure...)

So I would code your example above as:

01 filler pic x.
     88 isTrue    value '1'.
     88 isFalse   value '0'.

... pretty much the same.  (I use filler for flags so I can avoid the urge 
to MOVE something to them; instead the values are set with SET.
     set isTrue to TRUE)

C# does this with a Boolean type which is really cool...

BOOLEAN itWorked = false; //declares the variable and sets it to 'false'

itWorked = true;  //sets the value to 'true'

if (itWorked)
    {
          // hooray! Do the good stuff...
     }
else
    {
         // Bugger! Clean up the mess...
     }

We've had arguments here before about the use of 88 levels; some people love 
'em (self included), some people don't. They're not "wrong"; it is a 
question of preference, that's all.

In this specific instance we are constrained by the requirement of the 
Automation server. It needs a Bit turned on. (specifically to make the new 
Excel Spreadsheet visible). It is tricky to do that in standard COBOL, but 
fortunately, the COM interface comes to our rescue. COM is designed to talk 
across many platforms and languages. One of those is Visual Basic (Hey! it 
WAS designed by Microsoft... you can't blame them favouring their own 
products :-)) Visual Basic has a Boolean type similar to the C# example 
above, but actually implemented as a 16 bit binary field.

Dim itWorked AS Boolean   'declares the variable
itWorked = True                  'sets it to true...

There is a fighting chance that if we offer the COM interface something that 
looks like a VB Boolean type, it will take it and convert to the Boolean bit 
value used by the COM server.

01  COMTrue pic s9(4) comp value -1.

Unfortunately, I am unable to test this hypothesis, not having the MF 
compiler available.


> I don't really care whether or not it is Comp- 0, 1, 2, 3, 4, 5, 6,
> Comp-Sync, Comp5Length2 or Comp5Length6; I'll use what suits the
…[4 more quoted lines elided]…
> that's another topic for the dinosaur to attack).

For the most part, it isn't too important, although sticking to simple forms 
is probably a good idea. I don't know many COBOL programmers who do all 
their internal arithmetic in long floating point (comp-2) for instance. :-)

Pete.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-05T11:33:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FvZan.151531$uH1.31724@newsfe25.iad>`
- **In-Reply-To:** `<7t2iisFb0mU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com> <e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com> <oRqan.24043$Fe4.54@newsfe21.iad> <7t2iisFb0mU1@mid.individual.net>`

```
Pete Dashwood wrote:
> James J. Gavan wrote:
>
<snip>

>>Should I not use the following  ?
>>
…[28 more quoted lines elided]…
> 
Brief response; that's how M/F illustrate it and comp-5 is the backbone 
of their returns from invoking methods in their support classes; the 
most 'common' coming back to you is pic x(4) comp-5. And should you need 
to send 'positioning, i.e. 'x,y,w,h' co-ordinates for GUIs then you are 
into s9(05) comp-5.

> 
> We've had arguments here before about the use of 88 levels; some people love 
> 'em (self included), some people don't. They're not "wrong"; it is a 
> question of preference, that's all.

Not an argument with me - I LUV 'em too. See following which illustrates 
both 88s and that 'dreadful' Level 78 :-

01 ErrorCode                       pic x(4) comp-5.
    88 NoErrors                     value 0.
    88 Error-DateFormat             value 1.
    88 Error-Value1                 value 2.
    88 Error-TwoValues              value 3.
    88 Error-VerifyDates            value 4.
    88 Error-DayName                value 5.
    88 Error-Separator              value 6.
    88 Error-MonthDisplay           value 7.
    88 Error-TimeDisplay            value 8.
    88 Error-MonthRange             value 9.
    88 Error-DaysRange              value 10.
    88 Error-DateLess               value 11.
    88 Error-ISO-8                  value 12.
    88 Error-ISO-6                  value 13.
    88 Error-EU-8                   value 14.
    88 Error-EU-6                   value 15.
    88 Error-NA-8                   value 16.
    88 Error-NA-6                   value 17.
    88 Error-InputValues            value 18.
    88 Error-ValidOutput            value 19.
    88 Error-NumberOfDays           value 20.
    88 Error-NonNumericDate         value 21.
    88 Error-LeapDay                value 22.
    88 Error-LT-1601                value 23.
    88 Error-SlidingYears           value 24.
    88 Error-NonNumericTimes        value 25.
    88 Error-DayOfWeek              value 26.
    88 Error-Years2                 value 27.
    88 Error-Days3                  value 28.
    88 Error-StringingDate          value 29.
    88 Error-OutDateFormat          value 30.
    88 ErrorsFound                  value 1 thru 99.

78 MaxMessages                     value 30.
78 MEL                             value 35.
01 MessageTable-1.
    05 pic x(MEL) value "Error  1 - DateFormat".
    05 pic x(MEL) value "Error  2 - Value1".
    05 pic x(MEL) value "Error  3 - TwoValues".
    05 pic x(MEL) value "Error  4 - VerifyDates".
    05 pic x(MEL) value "Error  5 - DayName".
    05 pic x(MEL) value "Error  6 - Separator".
    05 pic x(MEL) value "Error  7 - MonthDisplay".
    05 pic x(MEL) value "Error  8 - TimeDisplay".
    05 pic x(MEL) value "Error  9 - MonthRange".
    05 pic x(MEL) value "Error 10 - DaysRange".
    05 pic x(MEL) value "Error 11 - DateLess".
    05 pic x(MEL) value "Error 12 - ISO-8".
    05 pic x(MEL) value "Error 13 - ISO-6".
    05 pic x(MEL) value "Error 14 - EU-8".
    05 pic x(MEL) value "Error 15 - EU-6".
    05 pic x(MEL) value "Error 16 - NA-8".
    05 pic x(MEL) value "Error 17 - NA-6".
    05 pic x(MEL) value "Error 18 - InputValues".
    05 pic x(MEL) value "Error 19 - ValidIOutput".
    05 pic x(MEL) value "Error 20 - NumberOfDays".
    05 pic x(MEL) value "Error 21 - NonNumericDate".
    05 pic x(MEL) value "Error 22 - LeapDay".
    05 pic x(MEL) value "Error 23 - Century Date < 1601".
    05 pic X(MEL) VALUE "Error 24 - Sliding Years > 100".
    05 pic X(MEL) VALUE "Error 25 - NonNumericTimes".
    05 pic X(MEL) VALUE "Error 26 - DayOfWeek <> 1 -  7".
    05 pic X(MEL) VALUE "Error 27 - Years 2 = zeroes".
    05 pic X(MEL) VALUE "Error 28 - Days 3 = 0 or > 366".
    05 pic X(MEL) VALUE "Error 29 - StringingDate".
    05 pic x(MEL) VALUE "Error 30 - OutDateFormat".

01 MessageTable-2
    redefines MessageTable-1.
    05 ws-Message pic x(MEL) occurs MaxMessages.

You will no doubt latch onto the above. As I 'fiddle' around with 
coding, I just add to the ErrorCode table and the others, adjusting the 
78s for MaxMessages and MEL.

01 MonthDays-Table-1.
    05  pic 9(02) value 31.
    05  pic 9(02) value 29. *> <---See check for Leap Years
    05  pic 9(02) value 31. *>        in method "ValidateDate"
    05  pic 9(02) value 30.
    05  pic 9(02) value 31.
    05  pic 9(02) value 30.
    05  pic 9(02) value 31.
    05  pic 9(02) value 31.
    05  pic 9(02) value 30.
    05  pic 9(02) value 31.
    05  pic 9(02) value 30.
    05  pic 9(02) value 31.

01 MonthDays-Table-2
    redefines MonthDays-Table-1.
    05 MonthDays-Count occurs 12 pic 9(02).


I've 'thrown' in that reference to Leap Years above. I'd love to see 
what COBOL 85 supporters would offer as a solution. They do the job, but 
there are some really archaic examples on the Web; 'cos he thinks you 
have to be a mathematician to program, you should see Judson's example. 
I have a very elegant way of doing it - just by searching the Web.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-06T00:54:13+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t2f77FnqcU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com> <e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com>`

```
Alistair wrote:
> On Feb 3, 2:25 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
> wrote:
…[191 more quoted lines elided]…
>>> to match the Fujitsu definition.

Thanks for doing that Alistair.

I put the "Ugh!" comment by it because I really don't like it. It is how 
they did it in Fujitsu sample code. I've thought about it since and COBOL 
types are translated to COM types by the *COM Class. (I guess MF have a 
similar facility. Part of this exercise is to investigate that.) There IS a 
COM type of VBOOL so it is possible that using a 16 bit (VB TypeBoolean) 
with all bits set might have the same effect. Could you possibly try it 
replacing the stupid PIC 1 field as: 01 COMTrue pic s9(4) comp value -1. ?

Failing that, it is also possible that the new spreadsheet is set to visible 
by default and this action may not be required anyway...
>>
>> I don't recognize this program as being standard COBOL. If you want
…[22 more quoted lines elided]…
> standard of Cobol.

I already responded to John. :-)

Thanks for your time, Alistair.

Pete.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-05T06:56:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9bab902-68aa-45f0-8a32-188e045f5a20@n33g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com> <e1c8d1e3-af07-4f7a-a69f-6f0020f02241@m31g2000yqb.googlegroups.com> <7t2f77FnqcU1@mid.individual.net>`

```
On Feb 5, 11:54 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Alistair wrote:
> > On Feb 3, 2:25 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
…[239 more quoted lines elided]…
>

OK will try. I had checked to see if I could replace that one bit but
felt that the whizz-kids on this newsgroup would have beaten me to
it.    :-(
```

###### ↳ ↳ ↳ Re: People using Micro Focus

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-06T00:43:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t2eiqFk68U1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <614bf8a8-bc34-4173-a8ed-bf8e5d649a4f@m26g2000yqb.googlegroups.com> <1887f6d9-6bde-43bb-b04f-e0ae52531b93@f5g2000vbm.googlegroups.com>`

```
john@wexfordpress.com wrote:
> On Jan 18, 6:50 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>> On Jan 16, 10:14 am, "Pete Dashwood"
…[187 more quoted lines elided]…
> I don't recognize this program as being standard COBOL.

Well posting it here does reformat it a bit. It looks better in a COBOL 
IDE... :-)


>If you want to
> deal
> with such esoterica as COM I would use the language that others use to
> deal with
> such matters.

Esoterica? COM?  :It is one of the single most used features of the 
Microsoft environment and  there's certianly nothing esoteric about. it. The 
Component Object Model  (COM) evolved from Online Linking and Embedding 
which, in turn, was based on Dynamic Data Exchange (DDE). These things have 
been with us for a couple of decades and, as a developer targeting mainly 
Microsoft platforms, I have used all of these models from COBOL.

I don't know about "others" but I've been dealing with COM objects in COBOL 
for at least 12 years now.

> Specifically I don't find these constructs in any COBOL
> document I have.

Try the documents that AREN'T illuminated on sheepskin... :-)

> In general the recent attempts to make COBOL into some kind of object-
> oriented language
> lead us down the wrong path.

Ah, departure from the One True Faith... I understand.


> I have been programming in COBOL for 42 years
43 for me.

> and I don't
> recognize half the statements in the above code.

Ok, shall I just throw the code away then? :-)

I have been programming in COBOL longer than you have (not that it matters, 
but it apparently does to you)  and I do recognize all of the statements... 
plus a lot more I didn't use...and even more in at least 5 other programming 
languages, plus 7 dialects of COBOL :-) But I don't generally refer to 
myself as a programmer; there are REAL programmers in this forum.


>
> That defeats one of the purposes of any High Level Language:
>  to be a language where programmer x can read, understand and modify a
> program written by
> programmer y.

Oh Dear. And here's me thnking all these years that High Level languages 
were invented so code could be ported. (In low level languages it has to be 
emulated)

But just because there exists some x that cannot "read, understand and 
modify a program written by programmer y" does that mean all x cannot?

Does it mean y's program is useless?

Does it mean that y is "too clever by half"?  Or isn't it possible that 
there could be some x who CALL themselves "programmers" but really are only 
programmers in the very most limited sense of the word?

Are you suggesting that programming should be pitched to the lowest common 
denominator of skills?

Doing that leads to shops which ban use of PERFORM... VARYING, say all IF 
statements must test TRUE, Reference Modification must not be used  (because 
some people have trouble with numbers), and all the other stupid and 
restrictive standards that COBOL shops implement so that no-one has to think 
or learn their craft.

John, I don't want you to take this personally, it isn't meant to wound, but 
why would you post to a thread where I'm trying to get some serious support 
so that something can be learned, just so you can Harrumph and tell us it 
ISN'T COBOL, when it blatantly IS?

It just may not be COBOL as YOU know it.

That doesn't make it worthless.

Pete.
```

#### ↳ Re: People using Micro Focus

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-05T09:20:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net>`

```
On Jan 16, 10:14 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Does anybody use Micro Focus COBOL (any version, procedural or OO) to access
> COM or Automation server code, or even to write a COM compliant server
…[20 more quoted lines elided]…
>

If I knew anything (worth knowing or otherwise) about OO this would
have been a cinch.
Amended code follows. Problems were:

1.  MF v5.1 NET EXPRESS uses *> for comment lines. Code changed
accordingly.

2.  The bit setting of ComTRUE replaced by USING BY VALUE 1 on the
INVOKE.

3.  setting of compiler directive ooctrl required.

4.  Hyphens removed in method (the bit between the quotes on the
INVOKES?)

5.  Addition of CLASS-CONTROL paragraph.

6.  Removal of COM on the OBJECT REFERENCEs.

7.  Object names changed (to protect the guilty?).

8.  Comments removed from some INVOKE statements as these interfered
with the run.

9.  Test - program created spreadsheet with Print00n in cols 1 - 7
where n is the column number and Dont print in cols 8-10. Prinout was
columns 1 - 7 in A4 portrait.


ps you can keep the copyright.

pps The bits I jiggered with have the crap line numbering on the right
so should be easy enough to identify.


      *> This is required for OLE
applications                          00001000
        $set
ooctrl(+P)                                                 00002000
 
00003000
        PROGRAM-ID.
XLTEST.                                            00004000
       *> written by Pete Dashwood, PRIMA Computing, (NZ)
Ltd.          00005000
       *> January
2010.                                                 00006000
       *> (some parts loosely based on Fujitsu sample
code)             00007000
 
00008000
        ENVIRONMENT
DIVISION.                                           00009000
        CONFIGURATION
SECTION.                                          00010000
        class-
control.                                                  00011000
          MSExcel is class "$OLE
$Excel.Application".                    00012000
 
00013000
 
REPOSITORY.
00014000
            Class COM AS
"*COM".                                        00015000
 
00016000
        DATA
DIVISION.                                                  00017000
        WORKING-STORAGE
SECTION.                                        00018000
        01   ExcelProgID pic x(20) value "Excel.Application.
12".        00019000
 
00020000
 
00021000
        01   ExcelObject          OBJECT
REFERENCE.                     00022000000
        01   WorkBooksCollection  OBJECT
REFERENCE.                     000230000023000
        01   WorkBook             OBJECT
REFERENCE.                     000240000
        01   objWorksheets        OBJECT
REFERENCE.                     00025000
        01   objCurrSheet         OBJECT
REFERENCE.                     00026000
        01   objSelectCell        OBJECT
REFERENCE.                     00027000
        01   CellRangeBegin       OBJECT
REFERENCE.                     000280000
        01   CellRangeEnd         OBJECT
REFERENCE.                     000290000
        01   CellRange            OBJECT
REFERENCE.                     000300000
        01   Cell                 OBJECT
REFERENCE.                     00031000
        01   objPageSetUp         OBJECT
REFERENCE.                     00032000
 
00033000
 
00034000
        01   CellLine         PIC S9(9)
COMP-5.                         00035000
        01   CellCol          PIC S9(9)
COMP-5.                         00036000
 
00037000
       *> 01   COMTrue       PIC 1(1) BIT VALUE B"1".  *>
Ugh!!!        00038000
       *>  bit value passed by "  USING BY VALUE 1  " on
INVOKE         00039000
 
00040000
        01   Print-Range-String PIC
X(20).                              00041000
        01   numDisplay    PIC
999.                                     00042000
 
00043000
        01 Test-Value         pic x(35) value
"Print".                  00044000
 
00045000
        PROCEDURE
DIVISION.                                             00046000
        Main
section.                                                   00047000
 
000.
00048000
 
00049000
 
*>
00050000
 
*>==============================================================
00051000
       *>*  Activate
Excel.                                             00052000
 
*>*==============================================================00053000
 
00054000
 
00055000
            invoke MSExcel
"new"                                   00056000000
                                USING
ExcelProgID                   00057000
                                RETURNING
ExcelObject                   00058000000
            end-
invoke                                                  00059000
            invoke ExcelObject
"SETVISIBLE"                            00060000000
                                USING BY VALUE
1                        00061000
            end-
invoke                                                  00062000
 
*>*==============================================================00063000
       *>*  Create a new
Workbook                                       00064000
 
*>*==============================================================00065000
 
*>*
00066000
            invoke ExcelObject
"GETWORKBOOKS"                           00067000000   00066000
                                   RETURNING
WorkBooksCollection        000680000068000
            end-
invoke                                                  00069000
            invoke WorkBooksCollection
"Add"                            000700000070000
                                   RETURNING
WorkBook                   000710000
            end-
invoke                                                  00072000
            invoke WorkBook "Activate" end-
invoke                       000730000
 
*>*==============================================================00074000
       *>*  Create a new sheet in the new workbook and get a reference
t00075000
 
*>*==============================================================00076000
            invoke WorkBook
"GETWORKSHEETS"                             000770000
                               RETURNING
objWorksheets                  00078000
            end-
invoke                                                  00079000
            invoke objWorksheets "Add"  *> makes the new sheet active
al00080000
            end-
invoke                                                  00081000
            *> get a reference to the current sheet in the new
workbook 00082000
            invoke WorkBook
"GETACTIVESHEET"                            000830000
                   RETURNING
objCurrSheet                               00084000
            end-
invoke                                                  00085000
 
*>*==============================================================00086000
       *>*  Set the value for 1st - 10th Cell (A1 to J1) in the new
shee00087000
       *>*  We will print cells 1 - 7 but not the
rest...               00088000
 
*>*==============================================================00089000
            move 1 to
CellLine.                                         00090000
 
perform                                                     00091000
               varying
CellCol                                          00092000
                  from
1                                                00093000
                    by
1                                                00094000
                 until CellCol >
10                                     00095000
                   invoke objCurrSheet
"GETCELLS"                       00096000
                            USING     CellLine
CellCol                  00097000
                            RETURNING
Cell                              00098000
                   end-
invoke                                           00099000
                   move spaces to test-
value                            00100000
                   if CellCol >
7                                       00101000
                      move "Don't print" to test-
value                  00102000
                      move CellCol to
numDisplay                        00103000
                      move numDisplay to test-value
(13:3)              00104000
 
else                                                 00105000
                      move "Print" to test-
value                        00106000
                      move CellCol to
numDisplay                        00107000
                      move numDisplay to test-value
(7:3)               00108000
                   end-
if                                               00109000
 
00110000
 
00111000
                   invoke Cell
"SETVALUE"                               00112000
                                 USING     test-
value                   00113000
                   end-
invoke                                           00114000
            end-
perform                                                 00115000
 
*>*==============================================================00116000
       *>*  Select the 1st - 7th Cell in the 1st line (from A1 to
J1).  00117000
 
*>*==============================================================00118000
            move 1 to
CellLine                                          00119000
            move 1 to CellCol               *> Get the beginning
positio00120000
            invoke objCurrSheet "GETCELLS"   *> the Cell
object.        00121000
                             USING     CellLine
CellCol                 00122000
                             RETURNING
CellRangeBegin                   001230000
            end-
invoke                                                  00124000
            MOVE 1  TO
CellLine                                         00125000
            MOVE 7 TO CellCol    *> Get the ending position of
the      00126000
            invoke objCurrSheet "GETCELLS"  *> Cell
object.             00127000
                             USING     CellLine
CellCol                 00128000
                             RETURNING
CellRangeEnd                     001290000
           end-
invoke                                                   00130000
            invoke objCurrSheet
"GETRANGE"                              00131000
                             USING     CellRangeBegin
CellRangeEnd      0013200000
                             RETURNING
CellRange                        001330000
            end-
invoke                                                  00134000
 
*>*==============================================================00135000
       *>*  Set the visible print
area                                  00136000
 
*>*
00137000
       *>*  This has to be in A1 style address format. Use the
"Address"00138000
       *>*  property of the range to get
this.                          00139000
 
*>*==============================================================00140000
            invoke CellRange
"GETAddress"                               001410000
                   returning Print-Range-
String                         00142000
            end-
invoke                                                  00143000
            *> Get a reference to the sheet's
PageSetup                 00144000
            invoke objCurrSheet
"GETPageSetUp"                          00145000
                   returning
objPageSetUp                               00146000
            end-
invoke                                                  00147000
            *> Add the visible print area to the sheet's
PageSetup      00148000
            invoke objPageSetUp
"SETPrintArea"                          00149000
                   using Print-Range-
String                             00150000
            end-
invoke                                                  00151000
            *> At this point cells 1 - 7 appear on the spread
sheet     00152000
            *> with a dotted frame around
them                          00153000
 
00154000
 
*>*==============================================================00155000
       *>*  Print the
Cells...                                          00156000
       *>*  uses the default
printer.                                   00157000
 
*>*==============================================================00158000
            invoke objCurrSheet
"PrintOut"                              00159000
            end-
invoke                                                  00160000
            *> ONLY the specified range is
printed...                   00161000
 
00162000
 
00163000
            .
00164000
 
999.
00165000
            exit
program                                                00166000
            .
00167000
        END PROGRAM
XLTEST.                                             00168000
 
00169000
 
00170000
```

##### ↳ ↳ Re: People using Micro Focus

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-05T14:06:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gL%an.69168$RS6.57781@newsfe15.iad>`
- **In-Reply-To:** `<9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com>`

```
Alistair wrote:
> On Jan 16, 10:14 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[3 more quoted lines elided]…
> Amended code follows. Problems were:

Not your fault old son, but let's clarify what you are referring to. I 
haven't downloaded V 5.1 for a look see as yet. Tried a while back; M/F 
buzzed away downloading M/F software and then stopped halfy-way saying I 
needed to download some of the Microsoft stuff first ! Oh bugger ! I 
gave up at that stage. (Not very good communication from M/F was it ?).

What were you referring to as your M/F demo, was it the one on their 
site under examples - couldn't be more specific -

Excel.zip which contains one source :-

	Excel.cbl - Tues Feb 19 09:30:58 2002

Again, I say to myself looking at the above date, "Bugger ! Surely 
nobody uses that weird sequence, 'Time' before 'Year' ? Just so happens 
that I'm dabbling with Date and Time at the moment - so I could include 
  that weirdo if it's legitimate that it is commonly used. Well 
obviously they do at the 'glasshouse' in Newbury, Berks :-)

Assuming I've hit the right example, (just out of interest), in W/S 
include :-

	01 charx	pic x.

and in the code add charx as follows :-

*>   Set the chart type to be 3D-Column
      invoke Chart "setType" using by value -4100
      accept charx

then you can take a look see at the Chart - which must be Microsoft 
generated, (into, or already in the Workbook), because I couldn't 
establish where it comes from using a slightly earlier version of the 
program above.

If it IS the above example you are referencing, it will be N/E V 3.1 or 
there abouts. Now on the basis you are using N/E V 5.1 :-


> 1.  MF v5.1 NET EXPRESS uses *> for comment lines. Code changed
> accordingly.
> 
Bit puzzled what is going on; was the original source 'freeformat', so 
that he is starting in Column 1. (N/E you specifically set a DIRECTIVE 
for free format).

> 2.  The bit setting of ComTRUE replaced by USING BY VALUE 1 on the
> INVOKE.
> 
> 3.  setting of compiler directive ooctrl required.

V 5.1 you maybe able to get away without some of the old directives, but 
certainly I needed the $set ooctrl (+P) using V 3.1
> 
> 4.  Hyphens removed in method (the bit between the quotes on the
> INVOKES?)

Don't think so - I've just changed my source to accept the following :-

"GetTime-8" and "GetTime-WithGMT"

(Now of course I've got to take those hyphens out and recompile :-) )

> 
> 5.  Addition of CLASS-CONTROL paragraph.

You were thrown by the example. There is a directive in V 3.1 to include 
  the Repository syntax - but it just doesn't do anything for you. From 
V 4.0 onwards the syntax du jour is REPOSITORY - so change your code to 
Repository and see what happens. (Remember M/F were putting this stuff 
together over a decade before COBOL 2002 happened, whereas F/J were in 
on the act later when references to REPOSITORY were firmed up - so 
that's what they went with from their Day 1).

Can't comment on remainder because I don't want to sidetrack to become 
conversant with OLE - deep into my 'DateAndTime' class. PECD must have a 
'similar' but in the vein of XP = e(X)treme (P)rogramming - check the 
M/F documentation on OLE Exception Errors.

Jimmy, Calgary AB

> 6.  Removal of COM on the OBJECT REFERENCEs.
> 
…[7 more quoted lines elided]…
> columns 1 - 7 in A4 portrait.

 > amended source snipped.......
```

###### ↳ ↳ ↳ Re: People using Micro Focus

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-05T15:29:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e2c6f91-2fd5-43c0-853d-156866b3994d@n7g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <gL%an.69168$RS6.57781@newsfe15.iad>`

```
On Feb 5, 9:06 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Alistair wrote:
> > On Jan 16, 10:14 am, "Pete Dashwood"
…[11 more quoted lines elided]…
>

The version of MF was v5.1 Net Express Personal Edition. The freebie
off of the internet. The Microsoft stuff you might have needed was
probably the MS Visual Studio 2008. There is an option which loads up
a cut down version for you. My fundamentalist friend ran in to this
problem last week.


> What were you referring to as your M/F demo, was it the one on their
> site under examples - couldn't be more specific -
…[4 more quoted lines elided]…
>

That is the one. You may notice that I used the same obj* names
filched from their example.

> Again, I say to myself looking at the above date, "Bugger ! Surely
> nobody uses that weird sequence, 'Time' before 'Year' ? Just so happens
…[3 more quoted lines elided]…
>

Dunno, I never noticed any date problem.

> Assuming I've hit the right example, (just out of interest), in W/S
> include :-
…[22 more quoted lines elided]…
> for free format).

No. My implementation does not accept an asterisk in col 7 as the
start of a comment without the angle brackets.

>
> > 2.  The bit setting of ComTRUE replaced by USING BY VALUE 1 on the
…[6 more quoted lines elided]…
>

There are about 4 default settings available. P worked nicely.

>
>
…[39 more quoted lines elided]…
>  > amended source snipped.......
```

###### ↳ ↳ ↳ Re: People using Micro Focus

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-06T12:48:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t3p23F5hjU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <gL%an.69168$RS6.57781@newsfe15.iad>`

```
James J. Gavan wrote:
> Alistair wrote:
>> On Jan 16, 10:14 am, "Pete Dashwood"
…[99 more quoted lines elided]…
>> amended source snipped.......

Thanks for the comments, Jimmy.

Given that Alistair's code works and achieves the same result as the Fujitsu 
code I put together, I think it is fair to go with that.

However, any enlightment to help with some of the noted problems he 
encountered is very acceptable and thanks for that.

If you could implement the changes you have suggested and get it to work so 
it produces the desired result, I'd be very happy to post your version with 
annotations in source by you, as well.

All of this is really good stuff that can help people using Micro Focus and 
Fujitsu COBOL to interface to MS Automation servers like Excel.

As I noted at the start of the thread, COM is REALLY useful and it is good 
to have a simple example using everyday software that people are familiar 
with.

The general feeling amongst MS developers is that most of the COM 
functionality is now replaced by .NET Classes and facilities. As someone who 
uses both every day, I can only say I see a place for both.

It is the "universal interface" of COM which makes it invaluable and enables 
it to run in any COM aware environment. Obviously, COBOL legacy code can be 
wrapped as COM by adding around half a dozen lines to it, and it is then 
able to go and play nicely on .NET without the need for a .NET COBOL 
compiler. (This is only possible because MS DESIGNED a feature into .NET 
(InterOP Services) to handle legacy code (primarily for old native code 
applications in VB and C, but it works for unmanaged code generally, and it 
works extremely well for anything wrapped as COM, including COBOL).

Although Microsoft are much maligned, sometimes, when they get it right, the 
results are simply outstanding. I LOVE InterOP Services and have used it to 
lever most of my old COBOL components into .NET. (Now, through the PRIMA 
Migration Toolset [ http://primacomputing.co.nz/PRIMAWebSite ] I am 
assisting others to do the same. It is very interesting and the wide range 
of different COBOLs in use by clients means the toolset occupies a fair bit 
of my time.)

Exercises like this one, which show how  currently popular COBOL compilers 
like Fujitsu and Micro Focus can interface to COM objects, pave the way for 
even more important stuff later.

If you enjoy managing things like Excel from your current COBOL code, it 
isn't hard to imagine managing your own applications and components in a 
.NET environment, where you have over 80,000 pre-written, debugged Classes 
to play with, that let you do virtually ANYTHING supported in a Windows 
environment. :-)

InterOP Services in .NET allows "old" (Mainly COBOL, in my case) components 
to run alongside and interact with components utilising .NET Classes and 
facilities (written in C#; you don't need a .NET COBOL compiler... and C# is 
free), completely seamlessly and painlessly. It is an excellent result.

Thanks again for your comments, Jimmy.

Appreciate your interest, and time.

Pete.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-05T21:29:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<je6bn.53912$s%.4439@newsfe18.iad>`
- **In-Reply-To:** `<7t3p23F5hjU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <gL%an.69168$RS6.57781@newsfe15.iad> <7t3p23F5hjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> James J. Gavan wrote:
> 
…[5 more quoted lines elided]…
>>for free format).

Although not shown in the code were you automatically 'free-formating' ?
I haven't tried it - but I kind of think that either in Column 1 or 
Column 7 your asterisks should be accepted. (I'll give that a try sometime).
> 

> Although Microsoft are much maligned, sometimes, when they get it right, the 
> results are simply outstanding. 

I agree with that; they have done an outstanding job with the Office 
suite. But here's the rub. I had MS Word, plus the others on my Win 98 
machine and produced some block diagrams. If I recall I used this 
feature when writing to J4 about Collections, supporting my text with 
diagrams. Now I'm into Win XP and as part of the deal I bought MS Office 
Suite 2003. My block diagrams didn't work - pretty drawing was replaced 
by something called Hyperlink. (A feature BTW that has crept into some 
of the latest J4 write-ups). So now I started searching MS directly for 
Word. I found all sorts of amazing examples, with demos. But the whole 
thing finishes up. "Like what we've shown you. Well why not upgrade to 
MS 2007 ($$$$$$) ?".

So that triggered my looking at Sun's OpenOffice.org 3.0. I had a quick 
dabble at it and reproduced the original block diagrams, with colouring 
as necessary, fairly quickly. The original 'getting into Word' for 
diagramming paid off when using OpenOffice - the macros (dropdown 
menus/keys/mouse/whatever) although perhaps given slightly different 
names, the features were easy to identify. Being a Sun product, if you 
are familiar with Java you can invoke OpenOffice.org from the latter - 
not surprising. I think for non-Java people you use Basic. I have only 
taken a cursory look to-date. Now if you can link to it with COBOL/OO 
COBOL - and thinking of the word 'Open' (means 'FREE' doesn't it ?) - 
why go with an excellent MS product, which although it adds new 
useful/more flexible features, also adds a new price ?

As that Corsican said to his wife, "Not to-night Josephine". But get my 
DateAndTime done - I will take a look at the Excel demo.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-07T14:42:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t6k3qFdlnU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <gL%an.69168$RS6.57781@newsfe15.iad> <7t3p23F5hjU1@mid.individual.net> <je6bn.53912$s%.4439@newsfe18.iad>`

```
James J. Gavan wrote:
> Pete Dashwood wrote:
>> James J. Gavan wrote:
…[13 more quoted lines elided]…
>>

Asterisk in column 7 (as per the ancient COBOL tradition) will definitely 
work.

I like to insert comments in code and don't always want them on a different 
line (I have become used to using // on C# lines)
The COBOL standard now supports "*>"  (at least I think it does...)  and so 
that made sense.

>> Although Microsoft are much maligned, sometimes, when they get it
>> right, the results are simply outstanding.
…[12 more quoted lines elided]…
> upgrade to MS 2007 ($$$$$$) ?".

I use Visio for all my diagrams (including the ones on the cobol21 and PRIMA 
sites). I bought Visio back in the '90s and upgraded to 2003. It didn't cost 
a lot and was worth every penny. I haven't upgraded Visio to Office 2007 
(although I do run that suite) because the version I have does everything I 
want. (Again, it is a COM server and integrates seamlessly with all the 
other Microsoft software). Sometimes, it is necessary to spend a few hundred 
bucks on something that makes life easier. Most "hobbies" require SOME 
investment and I guess "computing" is no exception. If you are writing 
commercial software you can write these purchases off against tax.

Having said that, I agree it is a never ending battle... I had a request 
from a client a few days ago for a 64 bit windows 7 version of the Toolset 
(It is currently 32 bit but will run on any processor (including 64 bit) and 
is targeted for Win XP.)  He runs multiple copies of it for various projects 
and staff, using a virtual machine image for each one. He's very happy with 
it, but thought if he could run 64 bit Win 7 it would be easier for backups 
and management, as well as being even faster, presumably.

I simply don't have that environment in place and won't have until I replace 
my current main notebook. (BIGBLACK) Like you, it is a bit like having your 
nose pressed up against the shop window :-)

I replace my main notebook every 3 - 4 years, but I don't do it unless I am 
absolutely sure the new one will pay for itself. (BIGBLACK has paid for 
itself many times over). I don't own or plan to own a desktop system and 
haven't for about 10 years. The power of modern notebooks renders them 
unnecessary, in my opinion, and the convenience of being able to work at the 
beach is the clincher for me. I run a wireless LAN and have one of the "old" 
notebooks dedicated to managing shared printing and LAN storage for backups. 
Other notebooks join the network as needed, and the MAC addresses of certain 
friends' machines are also programmed into my router so they can log on from 
the comfort of an armchair at my place. BIGBLACK is a dual core 4GB 17" SONY 
Vaio AR250G notebook with a HDMI interface so I can run it in high 
definition through my flat screen TV (very good for doing presentations, and 
viewing internet TV) and was one of the first notebooks in the world to have 
a 200GB hard drive. It is almost obsolete now and the next one will be quad 
with full Win 7 and XP in virtual machine.

I am currently looking at new notebooks and like the latest Sager quads. 
Technically, these are gaming machines but the tech. specs. are simply 
breathtaking. Besides, commercial computing is a game, isn't it? :-)

I can't see me getting anything before April, possibly later.

>
> So that triggered my looking at Sun's OpenOffice.org 3.0. I had a
…[11 more quoted lines elided]…
> useful/more flexible features, also adds a new price ?

The latest release of Office 2010 I understand is going to be a free upgrade 
to people with Office 2007. (This may change before the package is 
officially released.). It is also possible to download the current Beta for 
free, particularly if you are a software developer.

I'll stay with the MS product because that's where my current living is, but 
I have only heard good things about Open Office.

>
> As that Corsican said to his wife, "Not to-night Josephine". But get
> my DateAndTime done - I will take a look at the Excel demo.

Would appreciate it if you could, Jimmy.

Thanks,

Pete.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-06T21:01:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36706c56-19f2-45cf-9161-060f5b948b08@s33g2000prm.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <gL%an.69168$RS6.57781@newsfe15.iad> <7t3p23F5hjU1@mid.individual.net> <je6bn.53912$s%.4439@newsfe18.iad> <7t6k3qFdlnU1@mid.individual.net>`

```
On Feb 7, 2:42 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> James J. Gavan wrote:
> > Pete Dashwood wrote:
…[99 more quoted lines elided]…
> to people with Office 2007.

As I understand what was put on the MS web site and then taken down
again was that people that bought Office 2007 after March <someday I
forget> will get free upgrade to 2010 not everyone with 2010.


> (This may change before the package is
> officially released.). It is also possible to download the current Beta for
…[3 more quoted lines elided]…
> I have only heard good things about Open Office.

Lotus Symphony 3 is based on Open Office plus some extras and will be
released soon. Beta available now.


> > As that Corsican said to his wife, "Not to-night Josephine". But get
> > my DateAndTime done - I will take a look at the Excel demo.
…[7 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: People using Micro Focus

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-06T11:59:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t3m6rFmovU1@mid.individual.net>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com>`

```
Alistair wrote:
> On Jan 16, 10:14 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[407 more quoted lines elided]…
> 00170000

Outstanding!

Thank you SO much, Alistair.

A really good migration job, especially from someone who is, by self 
admission, NOT an OO Programmer. :-)

I REALLY like your solution to setting the Boolean bit to make the 
Spreadsheet visible.

In Fujitsu, because it is using the *COM interface Class, all parameters 
MUST be passed BY REFERENCE, but being able to do it BY VALUE is a cool 
solution.

I'm not claiming any copyrights on this; it would be good if people simply 
find it useful.

As soon as I possibly can I'll get this to the cobol21 web site with 
suitable acknowledgement.

Again, thanks, great job.

Pete.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-05T15:31:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7fac2a6-b7b9-4ed3-b9eb-1763844b344b@r19g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <7t3m6rFmovU1@mid.individual.net>`

```
On Feb 5, 10:59 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Alistair wrote:
> > On Jan 16, 10:14 am, "Pete Dashwood"
…[428 more quoted lines elided]…
>

You are welcome. The "cool" replacement for ComTRUE was something I
stumbled across in either their sample program or in the
documentation.

As an aside, I really am beginning to hate M/F documentation. There
doesn't seem to be any easy way of finding the stuff you really need
to find.
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-05T20:31:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bo5bn.176$JE2.155@newsfe09.iad>`
- **In-Reply-To:** `<d7fac2a6-b7b9-4ed3-b9eb-1763844b344b@r19g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <7t3m6rFmovU1@mid.individual.net> <d7fac2a6-b7b9-4ed3-b9eb-1763844b344b@r19g2000yqb.googlegroups.com>`

```
Alistair wrote:
> 
> As an aside, I really am beginning to hate M/F documentation. There
> doesn't seem to be any easy way of finding the stuff you really need
> to find.

Try this and see if you have any better luck :-

http://supportline.microfocus.com/documentation/books/nx51ws01/nx51indx.htm

There's an overall index for ALL the books, then indices within books.

Now I know there used to be a Personal Edition way back but it was not 
anything like the N/E I use. Are you talking specifically 'Personal 
Edition' or is there another called 'University Edition' - I understood 
the latter to be the full McCoy - just the 22K line limit on source so 
that you can't distribute it.

Where's Michael W. Can you clarify ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: People using Micro Focus

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-02-06T04:48:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36fe67da-d2ef-4fed-a632-08e9a3889062@r19g2000yqb.googlegroups.com>`
- **References:** `<7rdhreFddcU1@mid.individual.net> <9ecd47d6-fff3-4d19-97a8-7a6c4ac2715a@d27g2000yqn.googlegroups.com> <7t3m6rFmovU1@mid.individual.net> <d7fac2a6-b7b9-4ed3-b9eb-1763844b344b@r19g2000yqb.googlegroups.com> <bo5bn.176$JE2.155@newsfe09.iad>`

```
On Feb 6, 3:31 am, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Alistair wrote:
>
…[14 more quoted lines elided]…
> that you can't distribute it.

Definitely MF NET EXPRESS 5.1 Personal Edition (that is what it has on
the start menu).

Thanks for the link.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
