[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question on Cobol Move statement - mixed move x to zzz9.

_25 messages · 14 participants · 2007-05_

---

### Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Michael Schey <mscheynjSPAMBLOCK@yahoo.com>
- **Date:** 2007-05-21T16:11:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`

```
18 year cobol veteran here.  Stumped trying to come up with a
technical explanation on this one. I know why this is happening but I
can't explain it to the higher ups because I can't explain it to
myself.  

05  WS-PROP-PREMISE                PIC X(04).


05  WS-FORMAT-4                 PIC ZZZ9.


WS-PROP-PREMISE has a value of  3.   That is 3 followed by 3 spaces. 

The code MOVE WS-PROP-PREMISE to WS-FORMAT-4 results in

3000

Why?

When the sending field has 0003 we get 3 in the result.  This is what
we are expecting from the sending system.  Now they are 'sometimes'
sending us a 3 followed by 3 spaces, which gives us the 3000 in the
result field. 

Thanks.

Michael
(http://michaelschey.blogspot.com/)
```

#### ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-05-21T16:19:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net>`
- **In-Reply-To:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`

```
Michael Schey wrote:
> 18 year cobol veteran here.  Stumped trying to come up with a
> technical explanation on this one. I know why this is happening but I
…[25 more quoted lines elided]…
> (http://michaelschey.blogspot.com/)

3<blank><blank><blank> is an edited field. Use

MOVE NUMVAL(WS-PROP-PREMISE) to WS-FORMAT-4.

Donald
```

##### ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Michael Schey <mscheynjSPAMBLOCK@yahoo.com>
- **Date:** 2007-05-21T16:26:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net>`

```
On Mon, 21 May 2007 16:19:09 -0400, donald tees <donald@execulink.com>
wrote:

>Michael Schey wrote:
>> 18 year cobol veteran here.  Stumped trying to come up with a
…[32 more quoted lines elided]…
>Donald


Donald:

Thanks for the info.  I know how to re-code this piece of logic that
has been around for almost 20 years.  What I want to know is WHY the
result is coming out the way it is when we get this new type of value
(which btw....I told the sending system to cease and desist sending it
in that format.  They made a change to their format and didn't think
it would have any effect on downstream systems and not only did not
tell us but did not regression test).
Michael
(http://michaelschey.blogspot.com/)
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-21T14:29:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com>`

```
On Mon, 21 May 2007 16:26:47 -0400, Michael Schey
<mscheynjSPAMBLOCK@yahoo.com> wrote:

>Thanks for the info.  I know how to re-code this piece of logic that
>has been around for almost 20 years.  What I want to know is WHY the
…[4 more quoted lines elided]…
>tell us but did not regression test).

I think he explained why.   Do you still have any questions?
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 4)_

- **From:** Michael Schey <mscheynjSPAMBLOCK@yahoo.com>
- **Date:** 2007-05-21T16:32:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc0453dncj0nrmqstiriaut1ov7dbs3hhc@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com>`

```
On Mon, 21 May 2007 14:29:58 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Mon, 21 May 2007 16:26:47 -0400, Michael Schey
><mscheynjSPAMBLOCK@yahoo.com> wrote:
…[9 more quoted lines elided]…
>I think he explained why.   Do you still have any questions?

Yup.  I'm not stupid and work on many platforms.  Shit, I used to
teach Cobol (a long time ago) and understand how moves work.  The
sending field is moving the data left to right, one byte at a time.  I
just can't explain why the result is coming out the way it is. 
Michael
(http://michaelschey.blogspot.com/)
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 5)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-21T23:41:41-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<prl453t812kh8m5jkvfdag6lsihh5pceef@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com> <bc0453dncj0nrmqstiriaut1ov7dbs3hhc@4ax.com>`

```
On Mon, 21 May 2007 16:32:56 -0400, Michael Schey
<mscheynjSPAMBLOCK@yahoo.com> wrote:

>On Mon, 21 May 2007 14:29:58 -0600, Howard Brazee <howard@brazee.net>
>wrote:
…[18 more quoted lines elided]…
>Michael

Depending on the platform and possible low-order zone, the blanks are
treated as zeros.  I could see this causing a data exception (S0C7) on
an IBM z series unless the PACK was followed by an OR IMMEDIATE on the
sign position because the packed value of the field would be
x'030004'.  Other platforms would have their own peculiarities.
>(http://michaelschey.blogspot.com/)
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-22T11:59:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179860347.012530.24170@h2g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<prl453t812kh8m5jkvfdag6lsihh5pceef@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com> <bc0453dncj0nrmqstiriaut1ov7dbs3hhc@4ax.com> <prl453t812kh8m5jkvfdag6lsihh5pceef@4ax.com>`

```
On 22 May, 03:41, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Mon, 21 May 2007 16:32:56 -0400, Michael Schey
>
…[39 more quoted lines elided]…
> - Show quoted text -

No PACK involved. The move was a simple move. If EBCDIC then
X'F3404040' would result in an S0C7 (I presume) unless only the low-
order nibbles are moved for each character and the X'F' nibble put in
to all high order positions ie X'F3404040' becomes X'F3F0F0F0'. My
money says that as there was no reported abend then it isn't IBM
hardware.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-22T22:21:32-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uj1753hcbo47rhnd8lnfks4gvd8uhr52kd@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com> <bc0453dncj0nrmqstiriaut1ov7dbs3hhc@4ax.com> <prl453t812kh8m5jkvfdag6lsihh5pceef@4ax.com> <1179860347.012530.24170@h2g2000hsg.googlegroups.com>`

```
On 22 May 2007 11:59:07 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 22 May, 03:41, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
>> On Mon, 21 May 2007 16:32:56 -0400, Michael Schey
…[47 more quoted lines elided]…
>hardware.

The original posting stated that when the sending field contained 0003
the receiving field became space space space 3.  The Language
Reference Manual states that a PIC X(4) sending field is treated as if
it is PIC 9(4) when the receiving field is numeric edited thus
conforming to what the original poster stated was happening.  This
implies 
MVC TEMPEDIT,EDITMASK   
PACK  TEMP,WS-PROP-PREMISE  
ED TEMPEDIT,TEMP   
MVC WS-FORMAT-4,TEMPEDIT+1. 
on an IBM z series (or predecessor).   Thus TEMP would become
x'030004' when WS-PROP-PREMISE is packed and since the edit mask would
not contain a sign position based on the picture, the sign position is
probably not used and thus the data exception would not be raised.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 7)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-05-23T08:49:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f30o63$f3v$1@nntp.fujitsu-siemens.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com> <bc0453dncj0nrmqstiriaut1ov7dbs3hhc@4ax.com> <prl453t812kh8m5jkvfdag6lsihh5pceef@4ax.com> <1179860347.012530.24170@h2g2000hsg.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> schrieb im Newsbeitrag
> No PACK involved. The move was a simple move. If EBCDIC then
> X'F3404040' would result in an S0C7 (I presume) unless only the low-
…[3 more quoted lines elided]…
> hardware.

not necessarily - depends on the generate instructions: we also generate 
code for IBM hardware interface, but we include a ZAP which leads to an 
interrupt if the sending field is not numeric though the COBOL standard 
requests it to be. We do this on special customer request, in order to 
'detect' such nonnumeric sending fields.

regards
K. Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-05-24T21:10:49-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kt4c539u98nqmkj3enj4at2gjipnqukrvs@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <i80453t6i0b4o8j95qqm5gkim0in9vuvr7@4ax.com> <bc0453dncj0nrmqstiriaut1ov7dbs3hhc@4ax.com> <prl453t812kh8m5jkvfdag6lsihh5pceef@4ax.com> <1179860347.012530.24170@h2g2000hsg.googlegroups.com>`

```
On 22 May 2007 11:59:07 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>On 22 May, 03:41, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
>> On Mon, 21 May 2007 16:32:56 -0400, Michael Schey
…[47 more quoted lines elided]…
>hardware.


The Language Reference Manual for Enterprise COBOL on the IBM z series
say that if the receiving field is numeric edited which WS-FORMAT-4 is
and the sending field is PIC X(4), the sending field is treated as PIC
9(4) (unsigned integer).  Thus I would expect the following sequence.

  PACK  TEMPNUMERIC,WS-INPUT-FIELD   I forgot the name
  MVC   EDITTEMP,EDITMASK   Editmask probably would be x'402020202021'
  ED    EDITTEMP,TEMPNUMERIC
  MVC   WS-FORMAT-4,EDITTEMP+2  Ignore the fill character and the
*              first byte because the pack would have added a high 
*              order zero.

Since the sign byte will never be examined, the invalid sign won't be
detected (principles of operations for the z series).
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-05-21T16:35:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hZCdncj0qbzsn8_bnZ2dnUVZ_qqrnZ2d@golden.net>`
- **In-Reply-To:** `<q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com>`

```
Michael Schey wrote:
> On Mon, 21 May 2007 16:19:09 -0400, donald tees <donald@execulink.com>
> wrote:
…[47 more quoted lines elided]…
> (http://michaelschey.blogspot.com/)

Well, "3   " and "   3" are two different things. A blank gets read as a 
zero in a numeric read.  It *never* gets read as a shift data, which is 
what you want. The first 3 in the first case is in the thousands digit 
spot, and that is exactly what you get. The datum "3.  " might work, but 
I would not count on it.  I always use numval when importing foreign fields.

Donald
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 4)_

- **From:** Michael Schey <mscheynjSPAMBLOCK@yahoo.com>
- **Date:** 2007-05-21T16:36:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2m04535eqfkvj21lq3mi0657ig7fn3fcrb@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <rv2dnXlPb_EkY8zbnZ2dnUVZ_vfinZ2d@golden.net> <q004531j1b8ql1q31ovm2lar89h55h54k9@4ax.com> <hZCdncj0qbzsn8_bnZ2dnUVZ_qqrnZ2d@golden.net>`

```
On Mon, 21 May 2007 16:35:01 -0400, donald tees <donald@execulink.com>
wrote:

>Michael Schey wrote:
>> On Mon, 21 May 2007 16:19:09 -0400, donald tees <donald@execulink.com>
…[56 more quoted lines elided]…
>Donald


Perfect.  Thankee sai  !!
Michael
(http://michaelschey.blogspot.com/)
```

#### ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-05-21T23:45:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Daq4i.21462$dh5.19823@fe01.news.easynews.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`

```
You don't tell us your platform or compiler and the answer is what you get WILL 
depend upon which compiler you use (and you MIGHT get an error with either " 
3" or "3   " in the input.

The ONLY time that a move from an alphanumeric to a numeric or numeric-edited 
field is DEFINED (by the standard) is if it contains an unsigned integer - and 
that does not mean an "unsigned integer with some spaces".  Therefore, moving
  "0003"
would work for all compilers, but anything else is "results are unpredictable".

In some compilers there are times when a space is treated as a zero, e.g. "   3" 
is treated as "0003" - but that is not universal - and may not even be universal 
for a single compiler that does it sometimes.

If you compiler has an option for showing "assembler" (or other pseudo-object 
code) then you may want to look at what is generated for the specific MOVE 
statement.

Bottom-Line:
  Doing a move from an alphanumeric field to a numeric-field WITHOUT doing an 
"IF NUMERIC" test first, is NOT something that you should rely on working the 
same across compilers  or with future releases of existing compilers.
```

#### ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-05-21T20:27:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1354hnbqkgo115b@news.supernews.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`

```
Michael Schey wrote:
> 18 year cobol veteran here.  Stumped trying to come up with a
> technical explanation on this one. I know why this is happening but I
…[20 more quoted lines elided]…
> result field.

One way to explain it:

In the original (asume ASCII), you have 33303030. The move routine 
(evidently) moves only the right-most nibbles, x3x0x0x0 ==> 3000 and is 
indifferent to the left-most nibbles
```

#### ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-21T19:29:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179800990.129832.240940@y18g2000prd.googlegroups.com>`
- **In-Reply-To:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com>`

```
>
> 05  WS-PROP-PREMISE                PIC X(04).
…[8 more quoted lines elided]…
>
Better yet....

05  WS-PROP-PREMISE        PIC X(04).
05  WS-FORMAT-4  redefines WS-PROP-PREMISE PIC ZZZ9.

Then MOVE 3 TO WS-FORMAT-4 instead.... nobody uses REDEFINES anymore.
Aside from shared memory bits, it works all the time.

It should work the first time.... naahh.
```

##### ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-05-22T09:11:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a02653hpipcejmo3d6dv42cqpg19nlf0ts@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com>`

```
On 21 May 2007 19:29:50 -0700, Rene_Surop <infodynamics_ph@yahoo.com>
wrote:

>nobody uses REDEFINES anymore.

I'm assuming that you're joking here.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-22T11:59:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179860385.365535.26370@q69g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<a02653hpipcejmo3d6dv42cqpg19nlf0ts@4ax.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <a02653hpipcejmo3d6dv42cqpg19nlf0ts@4ax.com>`

```
On 22 May, 16:11, Howard Brazee <how...@brazee.net> wrote:
> On 21 May 2007 19:29:50 -0700, Rene_Surop <infodynamics...@yahoo.com>
> wrote:
…[3 more quoted lines elided]…
> I'm assuming that you're joking here.

This ole Cobol dinosaur still uses REDEFINES.
```

##### ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-05-23T12:20:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bhfn2F2ss955U1@mid.individual.net>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1179800990.129832.240940@y18g2000prd.googlegroups.com...
> >
>> 05  WS-PROP-PREMISE                PIC X(04).
…[18 more quoted lines elided]…
>
REDEFINES is one of the most powerful constructs in COBOL. It can achieve 
things no other combination of verbs can achieve. Why would anyone NOT use 
it?

Pete.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-05-22T19:56:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179888985.898523.38370@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<5bhfn2F2ss955U1@mid.individual.net>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <5bhfn2F2ss955U1@mid.individual.net>`

```
>
> REDEFINES is one of the most powerful constructs in COBOL. It can achieve
…[4 more quoted lines elided]…
>

Yap.. the assumption is correct. I was kidding.

Well, come to think of it... no other language can dup it. (I think?)
It is because I haven't used it Java or C++. The REDEFINES verb is a
head/tail all-in-one.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 4)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-05-22T23:15:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vv-dnRe1PZJBLM7bnZ2dnUVZ_t3inZ2d@golden.net>`
- **In-Reply-To:** `<1179888985.898523.38370@g4g2000hsf.googlegroups.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <5bhfn2F2ss955U1@mid.individual.net> <1179888985.898523.38370@g4g2000hsf.googlegroups.com>`

```
Rene_Surop wrote:
>> REDEFINES is one of the most powerful constructs in COBOL. It can achieve
>> things no other combination of verbs can achieve. Why would anyone NOT use
…[10 more quoted lines elided]…
> 

Overlaying different descriptions of data is common in Assembler.  At 
least the assemblers I have used.

Donald
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-23T23:32:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y945i.12793$Ut6.5948@newsread1.news.pas.earthlink.net>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <5bhfn2F2ss955U1@mid.individual.net> <1179888985.898523.38370@g4g2000hsf.googlegroups.com> <Vv-dnRe1PZJBLM7bnZ2dnUVZ_t3inZ2d@golden.net>`

```

"donald tees" <donald@execulink.com> wrote in message 
news:Vv-dnRe1PZJBLM7bnZ2dnUVZ_t3inZ2d@golden.net...
> Rene_Surop wrote:
>>> REDEFINES is one of the most powerful constructs in COBOL. It can 
…[18 more quoted lines elided]…
> Donald

IBM mainframe assembler uses the assembler directive ORG.

I almost said "mainframe assemble" but then put in the "IBM" because Chuck 
Stevens would complain otherwise.  Has anybody heard anything from him? 
While he and I did not always agree I enjoyed and learned from his posts. 
Perhaps he will return some day.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-05-24T01:21:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yM55i.214174$6m4.36823@pd7urf1no>`
- **In-Reply-To:** `<Y945i.12793$Ut6.5948@newsread1.news.pas.earthlink.net>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <5bhfn2F2ss955U1@mid.individual.net> <1179888985.898523.38370@g4g2000hsf.googlegroups.com> <Vv-dnRe1PZJBLM7bnZ2dnUVZ_t3inZ2d@golden.net> <Y945i.12793$Ut6.5948@newsread1.news.pas.earthlink.net>`

```
Charles Hottel wrote:
> "donald tees" <donald@execulink.com> wrote in message 
> news:Vv-dnRe1PZJBLM7bnZ2dnUVZ_t3inZ2d@golden.net...
…[32 more quoted lines elided]…
> 
Well he is still acting as a backup, (the alternate) for Karlin's Corner 
on the minuscule J4 team, even though now he is in a private capacity. I 
suspect he was greatly disappointed by the layoff from Unisys and 
although he loved his job, probably doesn't have the enthusiasm to 
continue participating. Be nice if he did though !

Jimmy
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-05-24T09:11:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f33ksv$36c$1@reader2.panix.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <Vv-dnRe1PZJBLM7bnZ2dnUVZ_t3inZ2d@golden.net> <Y945i.12793$Ut6.5948@newsread1.news.pas.earthlink.net> <yM55i.214174$6m4.36823@pd7urf1no>`

```
In article <yM55i.214174$6m4.36823@pd7urf1no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:

[snip]

>I 
>suspect he was greatly disappointed by the layoff from Unisys and 
>although he loved his job, probably doesn't have the enthusiasm to 
>continue participating.

I suspect likewise and, further, believe he was treated, based on the 
descriptions posted here, in a shabby, shoddy, cheap and shameful manner.

DD
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-05-23T11:51:17+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f312qp$ir6$03$1@news.t-online.com>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <5bhfn2F2ss955U1@mid.individual.net> <1179888985.898523.38370@g4g2000hsf.googlegroups.com>`

```
"Rene_Surop" <infodynamics_ph@yahoo.com> schrieb im Newsbeitrag 
news:1179888985.898523.38370@g4g2000hsf.googlegroups.com...
> >
>> REDEFINES is one of the most powerful constructs in COBOL. It can achieve
…[12 more quoted lines elided]…
>

Well, C has unions which are essentially the same thing.
```

###### ↳ ↳ ↳ Re: Question on Cobol Move statement - mixed move x to zzz9.

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-05-23T23:28:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W645i.9569$296.2238@newsread4.news.pas.earthlink.net>`
- **References:** `<kqu353tuc6123ou8ikpru9seale4fovsti@4ax.com> <1179800990.129832.240940@y18g2000prd.googlegroups.com> <5bhfn2F2ss955U1@mid.individual.net> <1179888985.898523.38370@g4g2000hsf.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1179888985.898523.38370@g4g2000hsf.googlegroups.com...
> >
>> REDEFINES is one of the most powerful constructs in COBOL. It can achieve
…[12 more quoted lines elided]…
>

For replacing some but not all uses of REDEFINES in COBOL or tagged unions 
in C, you can use a class hierarchy AKA subclassing in Java. If the storage 
reuse is simply for two different looks at the same storage e.g. to at a 
field as an integer and use that to print a hexadecimal value, Java would 
comsider that a violation of type and something to be avoided. There are 
methods in the API to print  hex values but they are platform independent 
because of the JVM.

Here is a sample C program:

/* Discriminated union */
#include "math.h"
typedef enum {RECTANGLE, CIRCLE} shapeType_t;

typedef struct {
    double length;
    double width;
} rectangleDimensions_t;

typedef struct {
    double radius;
} circleDimensions_t;

typedef struct {
    shapeType_t tag;
    union {
        rectangleDimensions_t rectangle;
        circleDimensions_t    circle;
    } dimensions;
} shape_t;

double area(shape_t *shape) {
    switch(shape->tag) {
      case RECTANGLE: {
        double length = shape->dimensions.rectangle.length;
        double width  = shape->dimensions.rectangle.width;
        return length * width;
      }
      case CIRCLE: {
        double r = shape->dimensions.circle.radius;
        return M_PI * (r*r);
      }
      default: return -1.0; /* Invalid tag */
    }
}

int main() {
    shape_t rectangle, circle;
    rectangle.tag = RECTANGLE;
    rectangle.dimensions.rectangle.length = 2.0;
    rectangle.dimensions.rectangle.width = 3.0;
    printf("Rectangle area: %f\n", area(&rectangle));

    circle.tag = CIRCLE;
    circle.dimensions.circle.radius = 1.0;
    printf("Circle area: %f\n", area(&circle));

    return 0;
}


And here is one way to do it in Java:

// Page 101
abstract class Shape {
    abstract double area();
}

class Circle extends Shape {
    final double radius;

    Circle(double radius) { this.radius = radius; }

    double area() { return Math.PI * radius*radius; }
}

class Rectangle extends Shape {
    final double length;
    final double width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width  = width;
    }

    double area() { return length * width; }
}

// Page 102
class Square extends Rectangle {
    Square(double side) {
        super(side, side);
    }

    double side() {
        return length; // or equivalently, width
    }
}


This is fromt the book, Effective Java by Joshua Bloch, item 20.  It 
describes the disadvantages of the C version and the advantages of the Java 
version.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
