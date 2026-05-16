[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL DATES CALCULATION ROUTINES

_12 messages · 6 participants · 2002-07_

---

### COBOL DATES CALCULATION ROUTINES

- **From:** rig <rig01@yahoo.com>
- **Date:** 2002-07-25T18:19:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com>`

```
Hi Folks :

Ned help please ,  Where Can I get COBOL dates routines to calculate
dates . 
I need one routine to ADD or SUBSTRACT (days,months,years) from a
given Input Date in any format Julian or Gregorian..

Any input is welcome


Thanks
rig012yahoo.com
```

#### ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** docdwarf@panix.com
- **Date:** 2002-07-25T21:35:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahq90n$9t5$1@panix1.panix.com>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com>`

```
In article <23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com>,
rig  <rig01@yahoo.com> wrote:
>Hi Folks :
>
…[5 more quoted lines elided]…
>Any input is welcome

My input is... this smells like homework.  What kind of application are 
you working on?

DD
```

##### ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-07-26T14:28:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahrm9e$1r6$1@peabody.colorado.edu>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <ahq90n$9t5$1@panix1.panix.com>`

```

On 25-Jul-2002, docdwarf@panix.com wrote:

> My input is... this smells like homework.  What kind of application are
> you working on?

Certainly - Date calculations are pretty easy, even without intrinsic
functions.
```

#### ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-07-26T01:47:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D40A550.A7DBC494@shaw.ca>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com>`

```


rig wrote:

> Hi Folks :
>
…[8 more quoted lines elided]…
> rig012yahoo.com

You will find samples at different COBOL sites, but you are lucky - I
remembered  I have the source for all Intrinsic Functions (Dates are  a
sub-set). The program is written by Jerome Garfunkel who spent some time
on the COBOL Standards Committee. Yes I know, you are too young to
remember <G> - but he is the brother of Art Garfunkel from the fabulous
duo 'Simon and Garfunkel'.

Too big to post here - I'll send separately.

Bill - I'm sending you a copy. I think this would be a good one to
include in your FAQ

Jimmy, Calgary AB
```

##### ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** Anonymous <Nobody>
- **Date:** 2002-07-26T16:01:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d40feb3$1_1@anonymous>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <3D40A550.A7DBC494@shaw.ca>`

```
Would you mind sharing this example?

Thanks.

JD
dragonslayer@morelerbe.com

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3D40A550.A7DBC494@shaw.ca...
>
>
…[28 more quoted lines elided]…
>




-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

###### ↳ ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-07-26T20:55:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D41B855.691AC433@shaw.ca>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <3D40A550.A7DBC494@shaw.ca> <3d40feb3$1_1@anonymous>`

```


Anonymous wrote:

> Would you mind sharing this example?
>
…[3 more quoted lines elided]…
> dragonslayer@morelerbe.com

 Bill,

Any chance you could quickly add Jerry's source to COBOL FAQ - would save me
answering individual requests - they could download from cobolreport
automatically.

I await Bill's reply - if in negative I'll send you a copy.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-07-26T17:53:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahskad$qa0$1@slb7.atl.mindspring.net>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <3D40A550.A7DBC494@shaw.ca> <3d40feb3$1_1@anonymous> <3D41B855.691AC433@shaw.ca>`

```
The current FAQ already contains (as mentioned in a previous reply to this
thread) an example of date manipulation via intrinsic functions.  I see
(personally) no need to add additional examples.  If someone sees some
"problem" (or omission) with what is in the FAQ already, please let me know
what and why.
```

###### ↳ ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-07-27T01:07:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D41F2B5.E33536B2@shaw.ca>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <3D40A550.A7DBC494@shaw.ca> <3d40feb3$1_1@anonymous> <3D41B855.691AC433@shaw.ca> <ahskad$qa0$1@slb7.atl.mindspring.net>`

```

"William M. Klein" wrote:

> The current FAQ already contains (as mentioned in a previous reply to this
> thread) an example of date manipulation via intrinsic functions.  I see
…[19 more quoted lines elided]…
> >

OK Anonymous - e-mail me. Previous message, copy to you got returned, "You had
exceeded your quota'. You forgot to put a dime in the parking meter ?

Jimmy, Calgary AB
```

#### ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-26T02:57:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8U209.328434$Im2.16752823@bin2.nnrp.aus1.giganews.com>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com>`

```

"rig" <rig01@yahoo.com> wrote in message
news:23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com...
> Hi Folks :
>
…[5 more quoted lines elided]…
> Any input is welcome

Check the intrinsic functions section of your manual. For example, to find
today minus 1234 days:

Compute TempDate = Function Integer-of-date(TodaysDate) - 1234
Compute NewDate = Function Date-Of-Integer(TempDate)

Or,
Compute NewDate = Function Date-Of-Integer(Function
Integer-of-date(TodaysDate) - 1234)
```

##### ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-07-25T22:15:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahqes0$2lo$1@slb2.atl.mindspring.net>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <8U209.328434$Im2.16752823@bin2.nnrp.aus1.giganews.com>`

```
Alternatively, see the sample code for using intrinsic functions with dates
in the COBOL FAQ at:

 http://cobolreport.com/faqs/cobolfaq.htm#Sample_date_compare
```

#### ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-07-26T14:07:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahrl1l$14b$1@peabody.colorado.edu>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com>`

```

On 25-Jul-2002, rig <rig01@yahoo.com> wrote:

> Ned help please ,  Where Can I get COBOL dates routines to calculate
> dates .
> I need one routine to ADD or SUBSTRACT (days,months,years) from a
> given Input Date in any format Julian or Gregorian..

Is there any reason you can't use its intrinsic functions?   What is your
platform?
```

##### ↳ ↳ Re: COBOL DATES CALCULATION ROUTINES

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-07-26T16:51:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D417F21.4CA18AA5@shaw.ca>`
- **References:** `<23u0kuk2nmmqot662tees7ksplhe5bpekj@4ax.com> <ahrl1l$14b$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> On 25-Jul-2002, rig <rig01@yahoo.com> wrote:
>
…[6 more quoted lines elided]…
> platform?

He's figured out what he wants from Jerome Garfunkel's source. Always happy
to help somebody from the Great White North - la belle provence <G>

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
