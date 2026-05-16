[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe Question

_8 messages · 6 participants · 2006-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Mainframe Question

- **From:** "Lee" <flu8349nospam@nospam.yahoo.com>
- **Date:** 2006-02-02T07:17:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com>`

```
Fujitsu claims their (incorrect) result is the same as that produced by IBM 
COBOL on MVS or whatever they run nowadays.  Can someone please confirm 
this?  TIA



      01 W-Depr-Rem               Pic S9(15)V9(2) Comp Value +0.
       01 W-Est-Life-Y             Pic S9(11)V9(6) Comp Value +5.
       01 W-Depr-Mhs               Pic S9(7)       Comp Value +2.
       01 W-Value                  Pic S9(11)V9(6) Comp Value +14800.
       01 W-Depr-Tot               Pic S9(11)V9(6) Comp Value +0.
       01 W-Depr                   Pic S9(11)V9(6) Comp Value +0.

       PROCEDURE DIVISION.

           Compute W-Depr = (2 / W-Est-Life-Y) * (W-Value - W-Depr-Tot) * 
(W-Depr-Mhs /12).



      *The result of the above calculation using Fujitsu is 
+00000000986.662720
      *The same calculation in Microfocus is  +00000000986.666666
```

#### ↳ Re: Mainframe Question

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-02T12:47:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drsv1e$t5o$1@reader2.panix.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com>`

```
In article <vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com>,
Lee <flu8349nospam@nospam.yahoo.com> wrote:
>Fujitsu claims their (incorrect) result is the same as that produced by IBM 
>COBOL on MVS or whatever they run nowadays.  Can someone please confirm 
…[20 more quoted lines elided]…
>      *The same calculation in Microfocus is  +00000000986.666666

Using IBM Enterprise COBOL for z/OS and OS/390 3.2.0 and the same code as 
above but including:

01 W-DEPR-DISP              PIC  Z(11).9(6)+  VALUE ZEROES.

...

MOVE W-DEPR  TO  W-DEPR-DISP.        
DISPLAY ' DEPR DISP = ', W-DEPR-DISP.

...

... the compile generates a return-code of 4 (IGYPS0001-W   A blank was 
missing before character "1" in column 42.  A blank was assumed.) and 
throws out the following in the JESlog:

DEPR DISP =         986.662720+

DD
```

#### ↳ Re: Mainframe Question

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-02-02T14:07:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jmoEf.16049$_S7.13172@newssvr14.news.prodigy.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com>`

```
"Lee" <flu8349nospam@nospam.yahoo.com> wrote in message
news:vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com...
> Fujitsu claims their (incorrect) result is the same as that produced by
IBM
> COBOL on MVS or whatever they run nowadays.  Can someone please confirm
> this?  TIA
>       *The result of the above calculation using Fujitsu is
> +00000000986.662720
>       *The same calculation in Microfocus is  +00000000986.666666

That 'same as' claim should probably be qualified, since you can get
different results on IBM depending on compile-time options;e.g., the TRUNC
and FLOAT options come to mind for arithmetic.

Besides, in the example you have here, this code is not written correctly if
you want that many digits of precision in the answer. Your intermediate
values are almost certainly getting rounded 'somewhere' and depending on
where that occurs it will affect the final result to varying degrees.  You
need to control the rounding yourself and/or COMPUTE the intermediate values
yourself to WS variables of sufficient precision.

MCM
```

#### ↳ Re: Mainframe Question

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2006-02-02T09:07:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enoEf.60$0D6.168088@news.sisna.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com>`

```
That's the question which result is incorrect.
I don't know Cobol that well but as I can recall 70-s, for PL/I there was an 
IBM document describing exactly how FIXED operations performing.
What I mean is what's the TYPE of the (intermidiate) result of (W-Depr-Mhs 
/12).
Because it's just "12", the result type of this operation should be the type 
of W-Depr-Mhs, i.e. S9(11)V9(6)
In this case IBM result is correct and Microfocus (as well as OpenCobol) are 
wrong !
If you change "12" by "12.000000000000" you'll get Microfocus result.

BTW, AS/400 is giving the same result as 390.

Regards,
Sergey.

"Lee" <flu8349nospam@nospam.yahoo.com> wrote in message 
news:vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com...
> Fujitsu claims their (incorrect) result is the same as that produced by 
> IBM COBOL on MVS or whatever they run nowadays.  Can someone please 
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Mainframe Question

- **From:** "Lee" <flu8349nospam@nospam.yahoo.com>
- **Date:** 2006-02-04T03:05:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fSUEf.29726$H71.15481@newssvr13.news.prodigy.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com> <enoEf.60$0D6.168088@news.sisna.com>`

```
Thanks for the answers everyone.

BTW the answer in Fujitsu is the same even when all operands are (11)v(7).
You can achieve the (correct) result by re-ording the operations so that 
division is done last.

Lee
```

#### ↳ Re: Mainframe Question

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-02-02T10:26:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11u49a7op2fho6a@corp.supernews.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com>`

```

"Lee" <flu8349nospam@nospam.yahoo.com> wrote in message
news:vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com...
> Fujitsu claims their (incorrect) result is the same as that produced by
IBM
> COBOL on MVS or whatever they run nowadays.  Can someone please confirm
> this?  TIA
…[19 more quoted lines elided]…
>       *The same calculation in Microfocus is  +00000000986.666666

Using the directive ARITHMETIC"VSC2"
with Micro Focus 3.2.24 gives +00000000986.662720.
Without the directive the result is +00000000986.666666.
```

##### ↳ ↳ Re: Mainframe Question

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-02T17:05:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<drte5n$993$1@reader2.panix.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com> <11u49a7op2fho6a@corp.supernews.com>`

```
In article <11u49a7op2fho6a@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
>"Lee" <flu8349nospam@nospam.yahoo.com> wrote in message
…[3 more quoted lines elided]…
>> this?  TIA

[snip]

>>       *The result of the above calculation using Fujitsu is
>> +00000000986.662720
…[4 more quoted lines elided]…
>Without the directive the result is +00000000986.666666.

Gotta love this Web-thingie... from 
http://docs.hp.com/cgi-bin/doc3k/BB243390006.13011/20 :

--begin quoted text:

*   You can now give a compiler directive (ARITHMETIC"VSC2" or
    ARITHMETIC"OSVS") which ensures the program will give results
    compatible with IBM mainframes in arithmetic statements.  Up until
    now arithmetic statements have used Micro Focus's algorithms for
    the accuracy of results (generally determined by the way
    intermediate results in arithmetic statements are stored).  With
    this release the algorithms used are selectable at compile time.
    A simple example of where behavior can be different is:

         01  work-index     pic 9
              ...
             compute work-index = ( 7 / 4 ) * 4.

    The mainframe compilers will return the result 4; Micro Focus has
    always returned the result 7.  This is because on the mainframe
    the intermediate result of the division (1.75) is stored in a PIC
    9 field so it becomes 1.

    Results in Micro Focus COBOL may still differ from results on the
    mainframe, if the intermediate result requires more than 20 digits
    before, or more than 20 digits after, the decimal point,

--end quoted text.

DD
```

###### ↳ ↳ ↳ Re: Mainframe Question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-02T19:40:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ietEf.27387$Dc2.25811@fe05.news.easynews.com>`
- **References:** `<vmiEf.40880$dW3.22826@newssvr21.news.prodigy.com> <11u49a7op2fho6a@corp.supernews.com> <drte5n$993$1@reader2.panix.com>`

```
That "arith" directive is FAR from new.  In fact, I remember when I was still 
working (for Micro Focus) and wrote those exact words that DD quoted for the 
"Mainframe compatibility Guide" - and I went on disability in 1996).

FYI,
  For anyone wanting to know HOW IBM (currently supported compilers) determines 
intermediate results, see:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg30/APPENDIX1.1

as far as the rules of COBOL go (before the '02 Standard introduced "ARITHMETIC 
IS STANDARD") the implementor was free to do WHATEVER they wanted with such 
cases.  Even with the "new" ARITHMETIC clause, many calculations are still 
implementor defined.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
