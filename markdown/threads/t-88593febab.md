[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Left Justify Numeric Field- HOW?

_10 messages · 7 participants · 2000-08_

---

### Left Justify Numeric Field- HOW?

- **From:** Larry Venick <lvenick@my-deja.com>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m9rt2$91c$1@nnrp1.deja.com>`

```
This is the layout for my output record which occurs 25 times:
          05 DREY-P-REC.
            10  DREYP-SEQ                PIC 99.
            10  DREYP-DE-1               PIC X(5).
            10  DREYP-DE-1-VAL           PIC X(30).
            10  DREYP-DE-2               PIC X(5).
            10  DREYP-DE-2-VAL           PIC X(30).
            10  F                        PIC X(8)     VALUE SPACES.

The VAL fields are used (on some records) to hold Prices/Amounts.
In Working Storage I have the following defined:

       01 AMT-HOLD                                  PIC 9(9)V99.
       01 DISP-FIELD                                PIC ZZ,ZZZ,Z99.99.
       01 DISP-FIELD-R      REDEFINES  DISP-FIELD   PIC X(13).


My routine is :

       PROCEDURE DIVISION:

           MOVE 20                         TO DREYP-SEQ
           MOVE 'DS228'                    TO DREYP-DE-1
           COMPUTE AMT-HOLD        = (AHDB-ORD-INC-AMT-FED +
                                         AHDB-CAP-GAINS-AMT-FED)
           MOVE AMT-HOLD                   TO DISP-FIELD
           MOVE DISP-FIELD-R               TO DREYP-DE-1-VAL.
           MOVE 'DS229'                    TO DREYP-DE-2
           COMPUTE AMT-HOLD        = (AHDB-ORD-INC-AMT-STATE +
                                         AHDB-CAP-GAINS-AMT-STATE)
           MOVE AMT-HOLD                   TO DISP-FIELD
           MOVE DISP-FIELD-R               TO DREYP-DE-2-VAL.
           WRITE DIST-REC                  FROM DREY-P-REC
           INITIALIZE                      DREY-P-REC.


What I'm getting is:
20DS228            425.33DS229             00.00



What I want to get is :
20DS228425.33            DS22900.00


Nothing seems to work.....Any help would be appreciated.
Thanks

Larry






Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Left Justify Numeric Field- HOW?

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rc6i5.124$l36.78760@nnrp1.sbc.net>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com>`

```
A byte at a time works swell.

There is no single command that does the job.
```

##### ↳ ↳ Re: Left Justify Numeric Field- HOW?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3989a06b.188341343@207.126.101.100>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com> <Rc6i5.124$l36.78760@nnrp1.sbc.net>`

```
On Wed, 2 Aug 2000 23:04:27 -0500, "Jerry P" <jerryp@bisusa.com>
wrote:

>A byte at a time works swell.
>
>There is no single command that does the job.
>

But there could be.  Use OO, or get someone to implement user defined
functions.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Left Justify Numeric Field- HOW?

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MHyi5.680$_%2.139144@nnrp3.sbc.net>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com> <Rc6i5.124$l36.78760@nnrp1.sbc.net> <3989a06b.188341343@207.126.101.100>`

```


> >A byte at a time works swell.
> >
…[3 more quoted lines elided]…
> But there could be.  Use OO, or get someone to implement user
defined
> functions.

We have a single command at our shop already:

CALL 'JUSTL' USING LEN STRING

We also have a command called "JUSTR." It is left to the reader to
deduce it's purpose.
```

###### ↳ ↳ ↳ Re: Left Justify Numeric Field- HOW?

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<398AC76A.C5082168@brazee.net>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com> <Rc6i5.124$l36.78760@nnrp1.sbc.net> <3989a06b.188341343@207.126.101.100> <MHyi5.680$_%2.139144@nnrp3.sbc.net>`

```
Just in time Re-engineering?

Jerry P wrote:
> 
> > >A byte at a time works swell.
…[13 more quoted lines elided]…
> deduce it's purpose.
```

#### ↳ Re: Left Justify Numeric Field- HOW?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ma63h$gtt$1@slb3.atl.mindspring.net>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com>`

```
Check the COBOL FAQ at

  http://cobolreport.com/faqs/cobolfaq.htm

and look for

 "Appendix A.4 - How to "right justify" an alphanumeric field"

NOTE TO OTHER CLC readers:

Isn't the FAQ exactly backwards?
   Shouldn't this be "left-justified" and not "right-justified" ???

(I may be confused, so I won't change the FAQ until someone tells me that I
am correct that the current FAQ is in error.)
```

##### ↳ ↳ Re: Left Justify Numeric Field- HOW?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ma67p$p98$1@slb0.atl.mindspring.net>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com> <8ma63h$gtt$1@slb3.atl.mindspring.net>`

```
Call me confused (and talking to myself) <G>

I just thought about it.  The FAQ example DOES "right justify".

For the person asking this question, they would want to "reverse" the logic
to left-justify.
```

##### ↳ ↳ Re: Left Justify Numeric Field- HOW?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3989a031.188283151@207.126.101.100>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com> <8ma63h$gtt$1@slb3.atl.mindspring.net>`

```
No, we went through a big exercise on right justification - I think
the FAQ is correct - Left Justification is much easier.


On Wed, 2 Aug 2000 17:08:39 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>Check the COBOL FAQ at
>
…[77 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Left Justify Numeric Field- HOW?

- **From:** piasa_bird@my-deja.com
- **Date:** 2000-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8meou0$tgf$1@nnrp1.deja.com>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com>`

```
In article <8m9rt2$91c$1@nnrp1.deja.com>,
  Larry Venick <lvenick@my-deja.com> wrote:

it is questionable what the results would be if you redefine an edited
field.  since an edited field is no longer numeric or alphabetic.

however one could redefine a strictly numeric field to an alpha numeric
field and inspect for leading spaces using tallying and use the counter
to determine the location of the first non-space letter.  i.e. ctr + 1
= first digit you want. Then use move field (ctr + 1:size - ctr) and
move it to a desired field.

Using referrential addressing is a nice thing if you can use it.

"Move field (7:2)" moves 2 digits starting from position 7 of a given
field.  All you have to do is determine what part of the field to move.


> This is the layout for my output record which occurs 25 times:
>           05 DREY-P-REC.
…[45 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Left Justify Numeric Field- HOW?

- **From:** jack <jacksleightNOjaSPAM@hotmail.com.invalid>
- **Date:** 2000-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<150d730f.cda94602@usw-ex0102-016.remarq.com>`
- **References:** `<8m9rt2$91c$1@nnrp1.deja.com> <8meou0$tgf$1@nnrp1.deja.com>`

```
Hi Larry,

You might want to give this a try:

In W/S add ctr pic s9(2) comp.

In P/D, before the start of rtn, add move zeros to ctr.

Change compute amt-fld-hold etc. to compute disp-fld etc.
Replace move amt-fld-hold etc. and move disp-fld-r etc. with:

inspect disp-fld-r tallying ctr for leading spaces
move disp-fld-r(ctr + 1:) to dreyp-de-1

Do the same for fld-2.

Hope this helps, Jack.

P.S.

I was under the impression that JUSTIFY only works when the
sending field is shorter than the receiving field. Am I wrong?
If anybody knows, I'd appreciate a definitive answer.

Tahnx.



-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
