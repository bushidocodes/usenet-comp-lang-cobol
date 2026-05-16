[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Getting System date in 4 digit year format

_14 messages · 10 participants · 1999-03_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### Getting System date in 4 digit year format

- **From:** "Duane Dobesh" <dobesh@mindspring.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dd81g$dmc$1@camel18.mindspring.com>`

```
Can someone tell me what is the easiest way to get the system date in 4
digit year format.  I use MF COBOL.    ACCEPT ... from date seems to only
provide the year in YY format.

I apologize if this question has been asked and answers probably multiple
times before.

Thanks
```

#### ↳ Re: Getting System date in 4 digit year format

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36FA46AB.4212A77E@ASPMnetdoor.com>`
- **References:** `<7dd81g$dmc$1@camel18.mindspring.com>`

```
In RM-COBOL you can write ACCEPT ... FROM CENTURY-DATE.

Duane Dobesh wrote:

> Can someone tell me what is the easiest way to get the system date in 4
> digit year format.  I use MF COBOL.    ACCEPT ... from date seems to only
> provide the year in YY format.
```

#### ↳ Re: Getting System date in 4 digit year format

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36FA4636.624C8036@NOSPAMhome.com>`
- **References:** `<7dd81g$dmc$1@camel18.mindspring.com>`

```
Duane Dobesh wrote:
> 
> Can someone tell me what is the easiest way to get the system date in 4
…[6 more quoted lines elided]…
> Thanks


If you're only concerned with today's date, you should be able to use a
window effectively:
    if yy=99 then yyyy=9999 else yyyy=yy + 2000

Or wait until January and add 2000 to it!!!

Or get a compiler which handles YYYY format.  Does MF Cobol have date
functions?
```

#### ↳ Re: Getting System date in 4 digit year format

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36fa2690@news3.us.ibm.net>`
- **References:** `<7dd81g$dmc$1@camel18.mindspring.com>`

```

Duane Dobesh <dobesh@mindspring.com> wrote in message
news:7dd81g$dmc$1@camel18.mindspring.com...
> Can someone tell me what is the easiest way to get the system date in 4
> digit year format.  I use MF COBOL.    ACCEPT ... from date seems to only
> provide the year in YY format.

01  system-date  pic 9(8).
01  filler               redefines system-date.
      02  system-date-cc  pic 99.
      02  system-date-yymmdd pic 9(6).
      02  filler         redefines system-date-yymmdd.
            03  system-date-yy pic 99.
            03  system-date-mm pic 99.
            03  system-date-dd pic 99.

accept system-date-yymmdd from date
if system-date-yy = 99
     move 19 to system-date-cc
else
    move 20 to system-date-cc
```

##### ↳ ↳ Re: Getting System date in 4 digit year format

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36FA70A7.4182@zag.si>`
- **References:** `<7dd81g$dmc$1@camel18.mindspring.com> <36fa2690@news3.us.ibm.net>`

```
Leif Svalgaard wrote:
> 
> Duane Dobesh <dobesh@mindspring.com> wrote in message
…[19 more quoted lines elided]…
> .

01 system-date  pic 9(8).

move 19000000 to system-date
accept system-date(3:6) from date
if system-date(3:2) < 50  
   move 20 to system-date(1:2)
end-if
```

#### ↳ Re: Getting System date in 4 digit year format

- **From:** goble@kin.on.net (David. E. Goble)
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36fdbb56.0@duster.adelaide.on.net>`
- **References:** `<7dd81g$dmc$1@camel18.mindspring.com>`

```
"Duane Dobesh" <dobesh@mindspring.com> wrote:
>
>Can someone tell me what is the easiest way to get the system date in 4
…[5 more quoted lines elided]…
>
Hi Duane;

Using Stern & Stern

Although the technique for setting up the system date shown on pages
217-218 is correct it is more efficient to make use of the string
function which appears in chapter 16 pages 662-666. Because of the
problems caused by year 2000 problems, COBOL programs should no longer
use the older:

ACCEPT ws-date  FROM DATE.

statement as this only produces a two digitr date (pages 217-218). In
stead the COBOL-85 function:

MOVE FUNCTION CURRENT-DATE TO ws-date

should be used and a tipical paragraph of code might be:

xxxx-Set-System-Date

	MOVE FUNCTION CURRENT-DATE TO ws-date.
	STRING ws-date-day "/"
                            ws-date-month "/"
                            ws-date-year "/"
             	      DELIMITED BY SIZE INTO ws-report-date
             END-STRING.

Anyway I hope this helps.
	




--Regards :                David. E. Goble
                           goble@kin.on.net
           http://www-mugc.cc.monash.edu.au/~degob1/goble
      Po Box 648 Kingscote Kangaroo Island South Australia 5223
```

##### ↳ ↳ Re: Getting System date in 4 digit year format

- **From:** edwardw355@aol.com (EdwardW355)
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990329003731.22006.00001587@ng-da1.aol.com>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net>`

```
Or in IBM COBOL for OS/390:

01  todays-date.
    03  todays-ccyy             pic  9(04).
    03  todays-mm                pic  9(02).
    03  todays-dd                 pic  9(02).

accept todays-date from date yyyymmdd.
```

###### ↳ ↳ ↳ Re: Getting System date in 4 digit year format

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36FF7F06.B33AD3F7@zip.com.au>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net> <19990329003731.22006.00001587@ng-da1.aol.com>`

```
EdwardW355 wrote:
> 
> Or in IBM COBOL for OS/390:
…[6 more quoted lines elided]…
> accept todays-date from date yyyymmdd.

IF the appropriate patch has been applied to your compiler...
```

###### ↳ ↳ ↳ Re: Getting System date in 4 digit year format

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xv8koDAvn+$2IwB7@rcav8r.demon.co.uk>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net> <19990329003731.22006.00001587@ng-da1.aol.com>`

```
In article <19990329003731.22006.00001587@ng-da1.aol.com>,
EdwardW355 <edwardw355@aol.com> writes
>Or in IBM COBOL for OS/390:
>
…[5 more quoted lines elided]…
>accept todays-date from date yyyymmdd.

Or in Acucobol-GT

ACCEPT TODAYS-DATE FROM CENTURY DATE.

or, compile with -Zy and

ACCEPT TODAYS-DATE FROM DATE.

Best regards

Nigel
```

###### ↳ ↳ ↳ Re: Getting System date in 4 digit year format

_(reply depth: 4)_

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3700DA06.458AB630@ASPMnetdoor.com>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net> <19990329003731.22006.00001587@ng-da1.aol.com> <Xv8koDAvn+$2IwB7@rcav8r.demon.co.uk>`

```
Nigel Eaton wrote:

> In article <19990329003731.22006.00001587@ng-da1.aol.com>,
> EdwardW355 <edwardw355@aol.com> writes
…[12 more quoted lines elided]…
>

Better make that CENTURY-DATE.
```

###### ↳ ↳ ↳ Re: Getting System date in 4 digit year format

_(reply depth: 5)_

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ds57q$ak8$1@holly.prod.itd.earthlink.net>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net> <19990329003731.22006.00001587@ng-da1.aol.com> <Xv8koDAvn+$2IwB7@rcav8r.demon.co.uk> <3700DA06.458AB630@ASPMnetdoor.com>`

```

Warren Porter wrote in message <3700DA06.458AB630@ASPMnetdoor.com>...
>
>Will that be not "not paper and not plastic?"


I guess the opposite of bisacksual is by hand.
```

###### ↳ ↳ ↳ Taglines (Was: Getting System date in 4 digit year format)

_(reply depth: 6)_

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37028061.20EDFEC5@ASPMnetdoor.com>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net> <19990329003731.22006.00001587@ng-da1.aol.com> <Xv8koDAvn+$2IwB7@rcav8r.demon.co.uk> <3700DA06.458AB630@ASPMnetdoor.com> <7ds57q$ak8$1@holly.prod.itd.earthlink.net>`

```
Jerry Peacock wrote:

> Warren Porter wrote in message <3700DA06.458AB630@ASPMnetdoor.com>...
> >
> >Will that be not "not paper and not plastic?"
>
> I guess the opposite of bisacksual is by hand.

In the days of computer bulletin boards, many offline mail readers had
collections of taglines which could be edited or borrowed from the bottom
of other people's messages.  In the transition to direct connection to
usegroups, that feature has kinda gone by the wayside.  Sigh.
```

###### ↳ ↳ ↳ Re: Getting System date in 4 digit year format

_(reply depth: 5)_

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y5vNdDAfCoA3Iw4D@rcav8r.demon.co.uk>`
- **References:** `<36fdbb56.0@duster.adelaide.on.net> <19990329003731.22006.00001587@ng-da1.aol.com> <Xv8koDAvn+$2IwB7@rcav8r.demon.co.uk> <3700DA06.458AB630@ASPMnetdoor.com>`

```
In article <3700DA06.458AB630@ASPMnetdoor.com>, Warren
Porter <warrenp@ASPMnetdoor.com> writes
>>
>
>Better make that CENTURY-DATE.
>--

Only if you want it to compile and run correctly.....   :^)

Thanks for the correction Warren.

Best regards

Nigel
```

#### ↳ Re: Getting System date in 4 digit year format

- **From:** "Duane Dobesh" <dobesh@mindspring.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dqd0u$k9a$1@camel25.mindspring.com>`
- **References:** `<7dd81g$dmc$1@camel18.mindspring.com>`

```
Thanks For the help on this.  The current-date solution works.  MF help says
this only returns 2 digit years unless i read it wrong.  Anyway, thanks
again.


Duane Dobesh wrote in message <7dd81g$dmc$1@camel18.mindspring.com>...
>Can someone tell me what is the easiest way to get the system date in 4
>digit year format.  I use MF COBOL.    ACCEPT ... from date seems to only
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
