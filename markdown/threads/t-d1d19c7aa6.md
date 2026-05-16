[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Non numeric move to comp-3 field does not give a system completion code 0C7

_8 messages · 5 participants · 2005-06 → 2005-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** David Roser <david.roser@iinet.net.au>
- **Date:** 2005-06-06T12:29:19+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`

```
I have a program which allows a non-numeric move
to a comp-3 field without a 0C7 error.
Would anyone know why ?

TIA
David


03 WHJ1-DSPLY-INVC-ARGT-ID        PIC X(10)   VALUE SPACES
10 AAWFQ-INVC-ARGT-ID             PIC S9(10) COMP-3.


DISPLAY 'WHJ1-DSPLY-INVC-ARGT-ID = ' WHJ1-DSPLY-INVC-ARGT-ID
MOVE WHJ1-DSPLY-INVC-ARGT-ID      TO AAWFQ-INVC-ARGT-ID
DISPLAY 'AAWFQ-INVC-ARGT-ID      = ' AAWFQ-INVC-ARGT-ID


  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
    Display  Filter  View  Print  Options  Help
  ------------------------------------------------
  SDSF OUTPUT DISPLAY SFLOINC1 JOB24659  DSID   12
  COMMAND INPUT ===>
WHJ1-DSPLY-INVC-ARGT-ID = 008A500000
ECDF6CEDDE6CDEC6CDCE6CC474FFFCFFFFFF4444444444444
681104273809553019730940E000815000000000000000000
  ------------------------------------------------
AAWFQ-INVC-ARGT-ID      = 0081500000
CCECD6CDEC6CDCE6CC44444474FFFFFFFFFF4444444444444
116680955301973094000000E000815000000000000000000
  ------------------------------------------------
```

#### ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-06-06T03:22:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3kPoe.56932$W62.42120@fe10.news.easynews.com>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`

```
Check out the NUMPROC and ZWB compiler options.  There is NEVER a guarantee that 
"incompatible data" will cause a S0C7 (IBM mainframe ABEND) ... Only that 
"results are unpredictable".
```

#### ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** "Ron" <NoSpam@SpamSucks.Org>
- **Date:** 2005-06-06T22:43:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xK6dnR-4gq1LijjfRVn_vg@giganews.com>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`

```
>I have a program which allows a non-numeric move
> to a comp-3 field without a 0C7 error.
…[4 more quoted lines elided]…
>

Without getting the assembler translation I have to assume COBOL
is just doing a PACK into the field. At the assembler level a PACK
instruction never fails with an S0C7. You can PACK anything.
It's when you try to do arithmetic that you're in trouble. PACK just inserts
the numerics left to right until the low order byte when it swaps the zone
and numeric. So X'40404040' packs X'00040'. Now try to
ADD 1 TO AAWFQ-INVC-ARGT-ID and watch the fireworks.

It looks like DISPLAY did some unpacking for you. UNPK also always
works and your results look like what I would expect.

Aside from that, this is really really bad COBOL code. Given that FIELD1
can be non-numeric you can end up with junk or S0C7 latter on.
I suggest that you redefine FIELD1 to PIC 9(10) to guarantee proper decimal
alignment and then:
If field1-9 is numeric
  move field1-9 to field2
else
  move zeros to field2 <- OR whatever to make sure it is valid.
end-if

I wouldn't screw around with compiler options like ZWB and NUMPROC and stuff.
Having special compile requirements for a program is somebody else's abend
waiting to happen. Code it right in the first place.
```

##### ↳ ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com>
- **Date:** 2005-06-16T14:24:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42B16F6F.3050106@fujitsu-siemens.com>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au> <xK6dnR-4gq1LijjfRVn_vg@giganews.com>`

```


Ron schrieb:
>>I have a program which allows a non-numeric move
>>to a comp-3 field without a 0C7 error.
…[12 more quoted lines elided]…
> and numeric. So X'40404040' packs X'00040'. Now try to

I think that it packs to X'000004'

Rosa
> 
> 
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** David Roser <david.roser@iinet.net.au>
- **Date:** 2005-06-19T13:39:34+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42b4e8f6$0$31333$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`
- **In-Reply-To:** `<xK6dnR-4gq1LijjfRVn_vg@giganews.com>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au> <xK6dnR-4gq1LijjfRVn_vg@giganews.com>`

```
Thanks for that. I checked the compile listing
and there are no assembler instructions in it.
Is there a compile option to show assembler instructions
in the listing ?


Ron wrote:
>>I have a program which allows a non-numeric move
>>to a comp-3 field without a 0C7 error.
…[40 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-06-19T06:26:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Fe8te.336553$cg1.46289@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<42b4e8f6$0$31333$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au> <xK6dnR-4gq1LijjfRVn_vg@giganews.com> <42b4e8f6$0$31333$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`

```


David Roser wrote:
> Thanks for that. I checked the compile listing
> and there are no assembler instructions in it.
> Is there a compile option to show assembler instructions
> in the listing ?

For IBM Mainframe compilers from COBOL II and later, the option is 
LIST.  If your system defaults include OFFSET, you may have to use 
NOOFFSET,LIST.

I hope that helps!
```

###### ↳ ↳ ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

_(reply depth: 4)_

- **From:** David Roser <david.roser@iinet.net.au>
- **Date:** 2005-06-24T03:21:20+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42baef8b$0$27722$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`
- **In-Reply-To:** `<Fe8te.336553$cg1.46289@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au> <xK6dnR-4gq1LijjfRVn_vg@giganews.com> <42b4e8f6$0$31333$5a62ac22@per-qv1-newsreader-01.iinet.net.au> <Fe8te.336553$cg1.46289@bgtnsc04-news.ops.worldnet.att.net>`

```
Thanks for that - I got the assembler listing.
It is a PACK instruction.

Arnold Trembley wrote:

> 
> 
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Non numeric move to comp-3 field does not give a system completion code 0C7

- **From:** David Roser <david.roser@iinet.net.au>
- **Date:** 2005-07-09T15:42:18+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42cf63ab$0$21455$5a62ac22@per-qv1-newsreader-01.iinet.net.au>`
- **In-Reply-To:** `<xK6dnR-4gq1LijjfRVn_vg@giganews.com>`
- **References:** `<42a3b4ff$0$10160$5a62ac22@per-qv1-newsreader-01.iinet.net.au> <xK6dnR-4gq1LijjfRVn_vg@giganews.com>`

```
Adding +1 did not S0C7 either.

Anyway, the code was corrected with...

If field1-9 is numeric
   move field1-9 to field2
else
    error-routine
end-if

Cheers
David


Ron wrote:
>>I have a program which allows a non-numeric move
>>to a comp-3 field without a 0C7 error.
…[40 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
