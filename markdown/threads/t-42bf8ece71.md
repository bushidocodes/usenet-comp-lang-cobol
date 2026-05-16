[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Bit mnipulation

_22 messages · 10 participants · 2003-10_

---

### Bit mnipulation

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-10-23T08:11:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.  In
Aseries Cobol there is an extension to the MOVE verb to allow bit
manipulation.

IE.

MOVE SRC TO TGT [A:B:C]

Would move C bits from bit no A from SRC to TGT starting at bit B. Bits are
number 47 to 0 from left to right.

So in my particular case

     MOVE WS01-COLUMN             TO WS01-INDEX [ 15 : 7 : 8 ].

This would move WS01-COLUMN bits 7 to 15 to WS01-INDEX bits 0 to 7 (and
leave the other bits alone).

Is there any way I can do this in Microfocus Cobol?

TIA
```

#### ↳ Re: Bit mnipulation

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-10-23T08:55:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn8tlq$1fr6$1@si05.rsvl.unisys.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```

"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message
news:bn82g5$1em$1@hercules.btinternet.com...
> I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.  In
> Aseries Cobol there is an extension to the MOVE verb to allow bit
…[6 more quoted lines elided]…
> Would move C bits from bit no A from SRC to TGT starting at bit B. Bits
are
> number 47 to 0 from left to right.
>
…[12 more quoted lines elided]…
> Steve

First off, we need to know more about the declarations of WS01-COLUMN and
WS01-INDEX.  I am going to presume herein that they're USAGE BINARY items
with no scale factor.  That's an A Series word-oriented integer; the topmost
bit's not used; the sign's in the next bit; the next 7 bits should be zero;
and the integer value is maintained in the remaining low-order 38 bits.

I'd expect the following to be equivalent on any sort of binary usage on
just about any system I can think of, so long as that usage covers at least
sixteen bits for both fields:
    IF WS01-INDEX IS GREATER THAN ZERO
        COMPUTE WS01-INDEX = 256 * FUNCTION INTEGER (WS01-INDEX / 256) +
                FUNCTION MOD (FUNCTION INTEGER (WS01-COLUMN / 256), 256)
     ELSE
        COMPUTE WS01-INDEX = 256 * FUNCTION INTEGER (WS01-INDEX / 256) -
                 FUNCTION MOD (FUNCTION INTEGER (WS01-COLUMN / 256), 256).

You might be able to make this a little clearer using a user field as a
temporary!

Obviously this bit transfer isn't going to be as efficient as the original
object code, which was only two instructions (ignoring the retrieval of the
words onto the stack and the storing of the destination):  ISOL (15:8) and
INSR (7:8).  That's a lot quicker than all the COMPUTE gyrations.

You'd probably be better off figuring out exactly what the code was *really*
trying to do with these word-oriented fields, and re-engineer it to use
something more generic, perhaps using *character-oriented* MOVEs.

Also, if you KNOW that WS01-INDEX is zero immediately before the MOVE, then
you don't need to worry about saving off the high-order (n - 8) bits of the
word before putting the information from WS01-COLUMN into it.

      -Chuck Stevens
```

##### ↳ ↳ Re: Bit mnipulation

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-10-23T17:10:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn921k$job$1@sparta.btinternet.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <bn8tlq$1fr6$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:bn8tlq$1fr6$1@si05.rsvl.unisys.com...
>
> "Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message
> news:bn82g5$1em$1@hercules.btinternet.com...
> > I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.
In
> > Aseries Cobol there is an extension to the MOVE verb to allow bit
> > manipulation.
…[25 more quoted lines elided]…
> with no scale factor.  That's an A Series word-oriented integer; the
topmost
> bit's not used; the sign's in the next bit; the next 7 bits should be
zero;
> and the integer value is maintained in the remaining low-order 38 bits.
>
> I'd expect the following to be equivalent on any sort of binary usage on
> just about any system I can think of, so long as that usage covers at
least
> sixteen bits for both fields:
>     IF WS01-INDEX IS GREATER THAN ZERO
…[10 more quoted lines elided]…
> object code, which was only two instructions (ignoring the retrieval of
the
> words onto the stack and the storing of the destination):  ISOL (15:8) and
> INSR (7:8).  That's a lot quicker than all the COMPUTE gyrations.
>
> You'd probably be better off figuring out exactly what the code was
*really*
> trying to do with these word-oriented fields, and re-engineer it to use
> something more generic, perhaps using *character-oriented* MOVEs.
>
> Also, if you KNOW that WS01-INDEX is zero immediately before the MOVE,
then
> you don't need to worry about saving off the high-order (n - 8) bits of
the
> word before putting the information from WS01-COLUMN into it.
>
>       -Chuck Stevens
>
>

Chuck,

Thanks for your help you are of course correct the data items are USAGE
BINARY.

I'll have to think about whether the rest solves this problem but I really
need to generic solution which will work with any start position length etc.
There may not be one of course but the thought of having to work out what
every one of these is actually doing does my head in.

Once again thanks for you efforts.

Steve
```

###### ↳ ↳ ↳ Re: Bit mnipulation

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-10-23T10:26:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn92vu$1k50$1@si05.rsvl.unisys.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <bn8tlq$1fr6$1@si05.rsvl.unisys.com> <bn921k$job$1@sparta.btinternet.com>`

```
Part of the problem is what happens *on A Series* if you store something
above bit 38 in the destination word where previously there were zeroes -- 
USAGE BINARY is, in hardware, an INTEGER, not a REAL.  Bits 45:7 reflect the
EXPONENT, bit 46 the mantissa sign, and diddling with either of these won't
have the same impact on the NUMERIC value of the destination on any other
architecture.

Within limits, yes, you can come up with generic solutions -- source bit no
higher than #38, destination bit no higher than #38 -- you can probably come
up with a similar formula.

Beyond that, the code's into deliberate side-effects -- the COBOL program
could be constructing a floating-point value into a fixed-point space, with
results meaningful only on A Series, or in any other architecture or USAGE
that exactly and accurately reflects the A Series 48-bit single-precision
word format (BINARY or REAL).

    -Chuck Stevens
```

#### ↳ Re: Bit mnipulation

- **From:** "lkrupp@pssw.NOSPAM.com.INVALID" <"lkrupp@pssw.NOSPAM.com.INVALID">
- **Date:** 2003-10-23T10:01:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vpfuv1p09r6l42@corp.supernews.com>`
- **In-Reply-To:** `<bn82g5$1em$1@hercules.btinternet.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
Steve Rainbird wrote:

> I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.  In
> Aseries Cobol there is an extension to the MOVE verb to allow bit
…[16 more quoted lines elided]…
> Is there any way I can do this in Microfocus Cobol?

If you can get Microfocus COBOL to do bit-wise logical operations, you
could do your own masking and shifting (you could use division by powers
of two for shifting).  You probably knew that.

If you have to, you could call C routines (if you have a C compiler) to
do the bit twiddling.  That would be awkward and possibly slow.  You
probably knew that, too.

If the line you quoted is the only place anything is moved to
WS01-INDEX, the original author may have been using a clever way of
doing something like this:

DIVIDE WS01-COLUMN BY 256 GIVING TEMP1
DIVIDE TEMP1 BY 256 GIVING TEMP2 REMAINDER WS01-INDEX

If WS01-COLUMN never has anything in bits 16 and up, you could try:

DIVIDE WS01-COLUMN BY 256 GIVING WS01-INDEX

... or is it more complicated than that?

Louis Krupp
```

##### ↳ ↳ Re: Bit mnipulation

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-10-23T17:12:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn9260$5o$1@hercules.btinternet.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <vpfuv1p09r6l42@corp.supernews.com>`

```

"lkrupp@pssw.NOSPAM.com.INVALID" <"lkrupp@pssw.NOSPAM.com.INVALID"> wrote in
message news:vpfuv1p09r6l42@corp.supernews.com...
> Steve Rainbird wrote:
>
> > I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.
In
> > Aseries Cobol there is an extension to the MOVE verb to allow bit
> > manipulation.
…[5 more quoted lines elided]…
> > Would move C bits from bit no A from SRC to TGT starting at bit B. Bits
are
> > number 47 to 0 from left to right.
> >
…[31 more quoted lines elided]…
>

Louis

Yes I think its more complicated that that.  I really need a generic
solution not just one for this case.

The C routine bit seems my only solution at the moment but I'm still hopeful
someone here will come up with a brilliant idea.

Regards

Steve
```

#### ↳ Re: Bit mnipulation

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-10-23T17:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F981306.70AB04BB@shaw.ca>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```


Steve Rainbird wrote:

> I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.  In
> Aseries Cobol there is an extension to the MOVE verb to allow bit
> manipulation.

Steve,

I don't use bit manipulation - but have you checked the on-line help to see if
the bit manipulation routines there will work for you ?

Jimmy, Calgary AB
```

#### ↳ Re: Bit mnipulation

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-23T11:03:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310231003.530027f2@posting.google.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote 

> So in my particular case
> 
…[5 more quoted lines elided]…
> Is there any way I can do this in Microfocus Cobol?

There are probably several ways, but I suspect that you want an easy
way.  There is no easy way.

It may be possible to use the CALL x"F5" Unpack byte and CALL x"F4"
Pack byte in a routine that will emulate the MOVE.
```

#### ↳ Re: Bit mnipulation

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-10-23T16:27:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oJWdnQoOdJtF2gWiU-KYiw@giganews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
Steve Rainbird wrote:

This might get you started on a generic solution:

 IDENTIFICATION DIVISION.
 PROGRAM-ID.  BITBYTE.
*=================================================================
*    NAME: BITBYTE
*
*    PURPOSE: Convert 8 bytes of flags to single byte and
*        vice-versa
*
*    INVOCATION:
*
*        CALL 'BIT-BYTE' USING SINGLE-BYTE EIGHT-BYTES
*        CALL 'BYTE-BIT' USING EIGHT-BYTES SINGLE-BYTE
*
*    DATE WRITTEN:
*
*    SIZE: CODE
*          DATA
*          TOTAL
*
*    REVISIONS:
*
*=================================================================
 COPY BIS.
 DATA DIVISION.
 FILE SECTION.
 WORKING-STORAGE SECTION.

 01  I                           PIC S9(2) COMP-5.
 01  J                           PIC S9(2) COMP-5.
 01  TEST2                       PIC S9(4) COMP-4.
 01  FILLER REDEFINES TEST2.
     02  TEST-L                  PIC X.
     02  TEST-R                  PIC X.

 LINKAGE SECTION.

 01  SINGLE-BYTE                 PIC X.
 01  EIGHT-BYTES                 PIC X(8).

 PROCEDURE DIVISION.
     GO TO QUIT.
 MAIN.
     ENTRY 'BIT-BYTE' USING SINGLE-BYTE EIGHT-BYTES.

     MOVE 0 TO TEST2.
     MOVE SINGLE-BYTE TO TEST-R.
     PERFORM VARYING I FROM 1 BY 1 UNTIL I > 8
         COMPUTE TEST2 = TEST2 * 2
         IF TEST-L NOT = LOW-VALUES
             MOVE '1' TO EIGHT-BYTES(I:1)
             MOVE LOW-VALUES TO TEST-L
         ELSE
             MOVE '0' TO EIGHT-BYTES(I:1)
             END-IF
         END-PERFORM.
     GO TO QUIT.

 OTHER-MAING.
     ENTRY 'BYTE-BIT' USING EIGHT-BYTES SINGLE-BYTE.
     MOVE 0 TO TEST2.
     PERFORM VARYING I FROM 1 BY 1 UNTIL I > 8
         IF EIGHT-BYTES(I:1) NOT = '0'
             COMPUTE J = 8 - I
             COMPUTE TEST2 = TEST2 + 2 ** J
             END-IF
         END-PERFORM.
     MOVE TEST-R TO SINGLE-BYTE.
     GO TO QUIT.
 QUIT.
     GOBACK
```

##### ↳ ↳ Re: Bit mnipulation

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-24T11:03:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f985056_5@news.athenanews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com>`

```
Sorry to be "picky" Jerry...

This routine has no initial value on TEST-L.

When using the 'BIT-BYTE' entry it ASSUMES this field has low values in it,
and then clears it only after it has "used" it in the first iteration.

On some platforms this is an invalid assumption...

(Seeing this code brought back some memories... we wrote a very similar
routine for System 360 in the late 60s <G>)

Pete.

"JerryMouse" <nospam@bisusa.com> wrote in message
news:oJWdnQoOdJtF2gWiU-KYiw@giganews.com...
> Steve Rainbird wrote:
>
…[73 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Bit mnipulation

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-10-24T21:30:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eOSdnYdiOPzTfQSiU-KYvA@giganews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com> <3f985056_5@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
> Sorry to be "picky" Jerry...
>
…[11 more quoted lines elided]…
> Pete.

See:
   MOVE 0 TO TEST2
as first executable statement.

Regards,
Jerry

>
> "JerryMouse" <nospam@bisusa.com> wrote in message
…[74 more quoted lines elided]…
>>      GOBACK
```

###### ↳ ↳ ↳ Re: Bit mnipulation

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-25T19:43:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f9a1d6e_3@news.athenanews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com> <3f985056_5@news.athenanews.com> <eOSdnYdiOPzTfQSiU-KYvA@giganews.com>`

```
Ah, tricked by the old REDEFINES... <G>

Thanks for pointing that out and apologies. <Blushes with embarrassment...>

As I have been "investigating" bit manipulation in Fujitsu COBOL in
connection with other requirements, I came across the following surprising
(well to me at least) facts:

1. If you define a field as Pic 1(?) the representation of it depends on the
USAGE clause.

    So, if you say:   01 my-field pic 1(8)  DISPLAY value 11010011.

    The field is held as 8 BYTES containing 0x3131303130303131.
     (This appears to provide the same functionality as the Bit2Byte
routine, but without any computational overhead. The compiler absorbs it
all...)

    On the other hand...
     if you say:       01 my-field pic 1(8)  BIT value 11010011.

     The field is held as 8 BITS with a value of  0xD3.

      Given that you can MOVE one to the other, it appears to remove the
need for the routine you posted. (It also explains why there is no Fujitsu
equivalent routines to the MicroFocus routines that do this...)

2.  You can define bit arrays using the BIT usage.

      01   twelve-bits pic 1(12) usage BIT.
      01   bit-array REDEFINES twelve-bits  pic 1(1) BIT occurs 12

indexed by  ba-x1.

      This allows access to the twelve bits individually or as a group.

This is because Fujitsu consider pic 1 items to be BOOLEANs. I was pretty
impressed by this as I had never explored it and was used to applying
Logical operations and masks to perform bit manipulation in COBOL.  My
beloved CBL_AND, CBL_OR, CBL_IMP, CBL_EQU and CBL_XOR are now on the back
burner while I check this out, and may be rendered virtually redundant by
this functionality.

Given the above facilities, I can't see any need to do bit manipulation in
other languages. (I was going to do it in Assembler as a last resort - no
need now...)

If anyone has made use of these facilities and found them useful, I'd be
interested to hear what it was used for.

Pete.

<snipped Jerry's interesting code>
```

###### ↳ ↳ ↳ Re: Bit mnipulation

_(reply depth: 5)_

- **From:** Donald Tees <Donald_Tees@sympatico.ca>
- **Date:** 2003-10-25T17:51:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jiCmb.11641$VQ3.681370@news20.bellglobal.com>`
- **In-Reply-To:** `<3f9a1d6e_3@news.athenanews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com> <3f985056_5@news.athenanews.com> <eOSdnYdiOPzTfQSiU-KYvA@giganews.com> <3f9a1d6e_3@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
> Ah, tricked by the old REDEFINES... <G>
> 
…[52 more quoted lines elided]…
> 

I am using them to mask out mouse bits received from intrerupts. What is 
really neat is that they work with the display statements for debugging. 
   The intrinsic logic functions are worth looking at as well.

Donald
```

###### ↳ ↳ ↳ Re: Bit mnipulation

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-25T23:17:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fwDmb.2334$Px2.2079@newsread4.news.pas.earthlink.net>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com> <3f985056_5@news.athenanews.com> <eOSdnYdiOPzTfQSiU-KYvA@giganews.com> <3f9a1d6e_3@news.athenanews.com>`

```
Pete,
  I know this will depress you <G> but what you describe below is straight
out of the ISO 2002 COBOL Standard.  If Fujitsu has implemented the "full"
Standard, you might want to also look for INTEGER-of-Boolean and
Boolean-of-Integer intrinsic functions.
```

###### ↳ ↳ ↳ Re: Bit mnipulation

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-26T21:57:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f9b8c8a_6@news.athenanews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com> <3f985056_5@news.athenanews.com> <eOSdnYdiOPzTfQSiU-KYvA@giganews.com> <3f9a1d6e_3@news.athenanews.com> <fwDmb.2334$Px2.2079@newsread4.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:fwDmb.2334$Px2.2079@newsread4.news.pas.earthlink.net...
> Pete,
>   I know this will depress you <G>
> but what you describe below is straight
> out of the ISO 2002 COBOL Standard.

No Bill, I am NEVER depressed by good news <G>.

It isn't about who's right, it's about what's right. If the Standards
committee got this right (and it looks as if they did), then I give them
full credit and congratulations (exactly as I would accord them the opposite
when they get it wrong...).

I'll certainly check out the functions you mention.

Thanks for the "heads up".

Pete.


> If Fujitsu has implemented the "full"
> Standard, you might want to also look for INTEGER-of-Boolean and
…[3 more quoted lines elided]…
> Bill Klein
<snipped>
```

###### ↳ ↳ ↳ Re: Bit mnipulation

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-26T21:57:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f9b8cc0_3@news.athenanews.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com> <3f985056_5@news.athenanews.com> <eOSdnYdiOPzTfQSiU-KYvA@giganews.com> <3f9a1d6e_3@news.athenanews.com> <fwDmb.2334$Px2.2079@newsread4.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:fwDmb.2334$Px2.2079@newsread4.news.pas.earthlink.net...
> Pete,
>   I know this will depress you <G>
> but what you describe below is straight
> out of the ISO 2002 COBOL Standard.

No Bill, I am NEVER depressed by good news <G>.

It isn't about who's right, it's about what's right. If the Standards
committee got this right (and it looks as if they did), then I give them
full credit and congratulations (exactly as I would accord them the opposite
when they get it wrong...).

I'll certainly check out the functions you mention.

Thanks for the "heads up".

Pete.


> If Fujitsu has implemented the "full"
> Standard, you might want to also look for INTEGER-of-Boolean and
…[3 more quoted lines elided]…
> Bill Klein
<snipped>
```

##### ↳ ↳ Re: Bit mnipulation

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-10-24T07:59:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bnam4v$gb$1@sparta.btinternet.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <oJWdnQoOdJtF2gWiU-KYiw@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:oJWdnQoOdJtF2gWiU-KYiw@giganews.com...
> Steve Rainbird wrote:
>
…[73 more quoted lines elided]…
>

Thanks Jerry
```

#### ↳ Re: Bit mnipulation

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2003-10-23T16:25:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0310231525.3261f7b1@posting.google.com>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message news:<bn82g5$1em$1@hercules.btinternet.com>...
> I am migrating a Cobol source from Unisys Aseries Cobol to Microfocus.  In
> Aseries Cobol there is an extension to the MOVE verb to allow bit
> manipulation.
> 

Steve,

if, like me, you are averse to re-inventing the wheel, I can offer you
a component that does exactly what you are looking for.

I understand that MicroFocus COBOL supports COM components so it
should be very simple to use.

I am currently working on some bit manipulation for XORed LRC check
digit computation and checking, for use in writing magnetic key cards
used by hotels, and it is very easy to extend this to do what you
want.

The component will install itself and a runtime and register itself on
your system.

You must instantiate it ONCE using the method prescribed by MF. 

(In Fujitsu it is as follows:

invoke COMClass "CREATE-OBJECT" using      ProgIDString
                                returning  BitMoveObj
end-invoke

...where "COMClass" is a name that has been equated to the COM Class
via the Repository (this will be different on MF and I have no idea or
documentation on how you achieve it in that environment. You would
need to check the MF docs on COM support...), "ProgIDString" is a
dataname with a value of "BitMove.BitMove.1" (which is the name the
component registers under on your system), and BitMoveObj is an Object
Reference of Class COMClass.)

Once installed and instantiated, it can be invoked as follows:

invoke BitMoveObj "BitMove" using SourceData
                                  TargetData
                                  SourceOffset
                                  TargetOffset
                                  NumberOfBits
end-invoke

(It is also possible to simply SET the properties then invoke the
Method with no parameters, but the above is more familiar for COBOL
programmers.)

If you want to, you can check the special register "PROGRAM-STATUS"
which will be non-zero if a problem was encountered. (I don't use
RETURNING unless I have to, and I understand it is not available on
UNIX systems anyway...)

Note that SourceData and TargetData must both be 48 bits and the
Offsets are calculated as 0 - 47 from right to left, as you described.
NumberOfBits is s9(4) comp-5.

If you are not ready for the 21st Century yet <G> I MIGHT be persuaded
to let you have the Source code so you can compile it on MF as a
CALLable subroutine instead of a component.... (it uses the CBL bit
manipulation functions which, if memory serves, are certainly
available in the MicroFocus environment.)

Mail me privately if interested.

Pete.
```

#### ↳ Re: Bit mnipulation

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-23T23:45:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AKZlb.3468$wc3.1790@newsread3.news.pas.earthlink.net>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
Interestingly enough, I can find the documentation in the Server Express -
but not in the Net Express online dox.  However, what I would suggest that
you do is go to:


http://supportline.microfocus.com/supportline/documentation/books/sx22sp1/sx22indx.htm

and look for:
  "3.5 Manipulating Bits Using Logic (Boolean) Operators"
```

##### ↳ ↳ Re: Bit mnipulation

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-10-24T17:07:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F995DA1.F9947C37@shaw.ca>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <AKZlb.3468$wc3.1790@newsread3.news.pas.earthlink.net>`

```


"William M. Klein" wrote:

> Interestingly enough, I can find the documentation in the Server Express -
> but not in the Net Express online dox.  However, what I would suggest that
…[6 more quoted lines elided]…
>

My reference to bit manipulation was the Windows on-line help format. If he uses the
search key 'bit manipulation' then it takes him on to an old DOS program LOGPER.cbl which
does bit manipulation for Screen Section, and then you go on from there to CBL_AND, CBL_OR
etc......

Anybody new to M/F would be well advised to randomly go through the on-line help -
particularly looking at the CBL_routines which cover many facets. (Plus for printing,
PC_PRINT_routines).

As regards the M/F on-line manuals - they get better and better, incorporating much that
is in the on-line help. (The latest on Character/Screen usage includes some of the old DOS
demo programs - would be useful to Floyd's student if he *was* using an M/F compiler).).

I dislike the Windows 'help' approach intensely. It is so fragmented, and you find
yourself jumping all over the place. Nothing like a good 'read' from a book where the
topic is dealt with in logical order.

Jimmy, Calgary AB
```

#### ↳ Re: Bit mnipulation

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-10-24T17:48:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bnbolu$5f4$1@peabody.colorado.edu>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com>`

```
There are clumsy ways of doing bit manipulation using CoBOL.   If you redefine
your field as binary you can copy that binary field to a work field and do left
and right shift by multiplying and dividing by 2.  (or 4 or 8 or 16 etc).

There are some other tricks available as well like this.   Or you can call
assembler routines.
```

##### ↳ ↳ Re: Bit mnipulation

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-24T18:05:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GRdmb.662$RQ1.429@newsread3.news.pas.earthlink.net>`
- **References:** `<bn82g5$1em$1@hercules.btinternet.com> <bnbolu$5f4$1@peabody.colorado.edu>`

```
In an LE (z/OS) environment (not that from the original question), check
out:

 "4.0 Bit manipulation routines"

at:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3130/4.0
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
