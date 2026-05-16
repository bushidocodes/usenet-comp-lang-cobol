[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OOP's - questions and answers

_4 messages · 2 participants · 2000-03_

---

### OOP's - questions and answers

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a9lid$685$1@news.igs.net>`

```
Can someone please explain FACTORY objects?  As I understand it, I create an
object, invoke methods, etc., then destroy it when done.  A FACTORY, as I
understand it, is an over-ride on the "new" method ... in effect, the object
has a specialized method that is applied when an object is created.

Questions --- How do I code one?  Given the following:

       CLASS-ID. SCRNOBJ INHERITS CBLSCRN.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       REPOSITORY.
           CLASS CBLSCRN.
       OBJECT.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       DATA DIVISION.
      FILE SECTION.
       WORKING-STORAGE SECTION.
       01 OBJECT-ATTRIBUTES.
           02 OBJECT-LENGTH        PICTURE 99 VALUE ZERO.
etc.
       PROCEDURE DIVISION.

*******************************************************************
       METHOD-ID. SET PROPERTY OBJECT-TYPE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       LINKAGE SECTION.
       01 TEMP                     PICTURE 99.
       PROCEDURE DIVISION USING TEMP.
       MAIN-LINE.
           MOVE TEMP TO OBJECT-LENGTH.
           EXIT METHOD.
       END METHOD.
       END OBJECT.
       END CLASS SCRNOBJ.

1. How do I insert a factory method into the code?
2. Can my factory method require arguements?
3. Can I code my own destructor?  If so, where does it go?
It obviously cannot go into the object ... there would be nothing to return
from ... or is it defered until after I exit the method?
```

#### ↳ Re: OOP's - questions and answers

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C94D17.6AAAC9B1@home.com>`
- **References:** `<8a9lid$685$1@news.igs.net>`

```


donald tees wrote:
> 
> Can someone please explain FACTORY objects?  As I understand it, I create an
…[4 more quoted lines elided]…
> Questions --- How do I code one?  Given the following:

Don, I've read and re-read. I know from previous correspondence, sort
of, where your mind is going on this one. But can't quite figure it out.
Do you want to send me some of yur code privately, relating to specific
screen objects. For example you might have something as simple as "Enter
Account # and it Displays Name", and where such an example fits into
your overall thi8nking. Then I can post here publicly if I figure it
out.

I haven't got into ActiveX yet - but the little I've gleaned, (primarily
comments from Pete Dashwood), would I be correct in assuming that what
you are getting at is something in COBOL which is very close to ActiveX.
No magic to the latter - using another language, somebody has sat down
and written pre-packaged modules.

I have one little bitch. I find it difficult to see the wood for the
tress with all that extraneous stuff ENVIRONMENT-DIVISION, DATA DIVISION
etc. when there aren't any contents. (Just my preference).

Jimmy

> 
>        CLASS-ID. SCRNOBJ INHERITS CBLSCRN.
…[33 more quoted lines elided]…
> from ... or is it defered until after I exit the method?
```

##### ↳ ↳ Re: OOP's - questions and answers

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8abs2n$dbv$1@news.igs.net>`
- **References:** `<8a9lid$685$1@news.igs.net> <38C94D17.6AAAC9B1@home.com>`

```

James J. Gavan wrote in message <38C94D17.6AAAC9B1@home.com>...
>
>
>donald tees wrote:
>>
>> Can someone please explain FACTORY objects?  As I understand it, I create
an
>> object, invoke methods, etc., then destroy it when done.  A FACTORY, as I
>> understand it, is an over-ride on the "new" method ... in effect, the
object
>> has a specialized method that is applied when an object is created.
>>
…[9 more quoted lines elided]…
>

Thanks Jim, but Thane has sent me some documentation, and I am going to read
it and try to code the damned thing.  Then I'll send it to you working, with
any luck.  It will probably be next week ... I have a hot date for the
weekend<G>.  BTW, do you have Fujitsu installed?  Can I send you DLL's to
take a look at?  You would need their runtime, but it does not require a
license for runtime only.
```

###### ↳ ↳ ↳ Re: OOP's - questions and answers

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C98230.CDC62939@home.com>`
- **References:** `<8a9lid$685$1@news.igs.net> <38C94D17.6AAAC9B1@home.com> <8abs2n$dbv$1@news.igs.net>`

```


donald tees wrote:
> 
> James J. Gavan wrote in message <38C94D17.6AAAC9B1@home.com>...
…[27 more quoted lines elided]…
> license for runtime only.

Sorry don't have Fujitsu - money, money. That's why I don't have ABC, C,
C++, PL/1, VB, or God knows what else. Now like you - if I had the money
then I could pay some serfs to do it for me, just like Pierre Berton
used all those keen young graduates to assemble the facts for his books,
donned his dickie-bow and posed for pictures to go on the cover :-)  

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
