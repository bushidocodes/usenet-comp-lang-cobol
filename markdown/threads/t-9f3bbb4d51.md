[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# convert packed CHAR to unpacked DIGIT

_12 messages · 10 participants · 2005-04_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### convert packed CHAR to unpacked DIGIT

- **From:** "ssb" <mail_ssb@yahoo.com>
- **Date:** 2005-04-15T19:02:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```
Hi,

Input record has a field of size 5 bytes containing packed numbers. But
this field is defined as CHARACTER.

E.g. WS-A    PIC X(5) '1212343455'

My task is to display '1212343455' on a report. Obviously, it requires
converting packed to unpacked numbers.

I tried doing something like this:

MOVE X(5)        TO 9(9) COMP-3.
REDEFINE 9(9) COMP-3 AS 9(10)

Any suggestions/help..? Thanks.
```

#### ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** Bill TB <thunderbox@hotmail.com>
- **Date:** 2005-04-16T12:49:51+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7%7e.6637$Le2.47154@nasal.pacific.net.au>`
- **In-Reply-To:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```


ssb wrote:
> Hi,
> 
…[14 more quoted lines elided]…
>
```

#### ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-04-15T19:57:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113620221.059864.160730@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```
Try something like this:
(IBM mainframe COBOLII or later)

01  ws-a  pic x(5).

01  ws-b.
    05  ws-a5 pic x(5).
    05  fil   pic x(1) value X'0C'.
01  ws-b-c3   redefines
    ws-b      pic s9(11) comp-3.

01  ws-c-9    pic s9(11).
01  ws-c-x    redefines
    ws-c-9.
    05  ws-c-ans pic x(10).
    05  fil      pic x(1).

   move ws-a to ws-a5
   move ws-b-c3 to ws-c-9
   display 'this s/b the ans ==>' ws-c-ans '<=='

All the usual caveats and copouts apply.


ssb wrote:
> Hi,
>
> Input record has a field of size 5 bytes containing packed numbers.
But
> this field is defined as CHARACTER.
>
> E.g. WS-A    PIC X(5) '1212343455'
>
> My task is to display '1212343455' on a report. Obviously, it
requires
> converting packed to unpacked numbers.
>
…[5 more quoted lines elided]…
> Any suggestions/help..? Thanks.
```

##### ↳ ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-04-16T12:04:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113678274.837564.87300@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1113620221.059864.160730@z14g2000cwz.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com> <1113620221.059864.160730@z14g2000cwz.googlegroups.com>`

```
Hi  ssb,

Didn't realize you wanted the ans as PIC 9.  Just change ws-c-ans to
pic 9(10).

Regards, Jack.
```

#### ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** Louis Krupp <lkrupp@pssw.NOSPAM.com.INVALID>
- **Date:** 2005-04-16T03:05:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161le0fasteuaa@corp.supernews.com>`
- **In-Reply-To:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```
ssb wrote:
> Hi,
> 
…[13 more quoted lines elided]…
> Any suggestions/help..? Thanks.

If your compiler supports reference modification and the ORD intrinsic, 
you could try stepping through the input field one character at a time, 
using ORD to find its binary value, dividing that value by 16, and using 
the dividend and remainder respectively to index into a table of 
hexadecimal characters (0123456789ABCDEF), and moving the results into 
the output record.

Louis
```

#### ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-16T15:11:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113689508.106446.257390@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```
> Input record has a field of size 5 bytes containing packed numbers.
> But this field is defined as CHARACTER.

> E.g. WS-A    PIC X(5) '1212343455'

If it is packed decimal then it should be defined as PIC S9(9) PACKED
or COMP-3 or similar.  This will occupy 5 bytes.

Or redfine it as:

    03  WS-A       PIC X(5).
    03  WS-A-Packed REDEFINES WS-A PIC S9(9) PACKED.

> My task is to display '1212343455' on a report. Obviously, it
requires
> converting packed to unpacked numbers.

    MOVE WS-A-Packed TO WS-A-Edited

where WS-A-Edited is defined as PIC -(9)9  or similar.

> I tried doing something like this:

> MOVE X(5)        TO 9(9) COMP-3.
> REDEFINE 9(9) COMP-3 AS 9(10)

A REDEFINE gives a different definition to the _same_ area.  A PIC X(5)
and S9(9) PACKED (or COMP-3) can redefine each other as they are the
same size.  PIC 9(10) is a different size and so won't map over a PIC
X(5).

MOVEing a PICS9(9) PACKED to S9(10) will do the unpacking.
```

##### ↳ ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-16T23:14:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q%g8e.4579809$Zm5.715769@news.easynews.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com> <1113689508.106446.257390@g14g2000cwa.googlegroups.com>`

```
Just to clarify, there is NOTHING in the '85 (or '02)  ANSI/ISO Standard that 
says you may NOT store 10 (decimal) digits in a 5-byte (character position) 
field - with USAGE Packed-Decimal, i.e.

  Pic 9(10) Packed-Decimal

*may* require only 5 "bytes".  In fact, there ARE implementations where this is 
true.

It is ALSO true that many (possibly MOST) implementations require a nibble 
(half-byte) for a "sign place holder" even for fields defined withOUT an "S" 
that have USAGE PACKED-DECIMAL.

As the original post did not (I don't think) provide any "clue" as to the 
compiler or the operating system,

A) we don't know if 9(10) (requiring 5 or 6) bytes (or even 5 1/2) would be 
required for this poster

B) whether (given one posted solution) a X'0C' - or X'C0" or X"F0" or X"0F" 
hex-something else would help or be required in order to "treat" the input 
information as a "valid" packed field.

   ***

Note:
   For some compilers "COMP-6" is the way to define a packed-decimal field with 
NO sign-nibble. YMMV
```

#### ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2005-04-17T02:42:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113730964.213376.70720@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```

ssb wrote:
> Hi,
>
> Input record has a field of size 5 bytes containing packed numbers.
But
> this field is defined as CHARACTER.
>
> E.g. WS-A    PIC X(5) '1212343455'
>
> My task is to display '1212343455' on a report. Obviously, it
requires
> converting packed to unpacked numbers.
>
…[5 more quoted lines elided]…
> Any suggestions/help..? Thanks.

While what the others have said is useful and appropriate, are you sure
that the size of the input field isn't six bytes instead of five?

Usually and not necessarily always, packed-decimal fields have a sign
in the rightmost half-byte, whether or not the field was defined as
signed.  Consequently, there may also be another digit in the leftmost
half-byte of the rightmost byte, if indeed the real field size is six
bytes.

Robert
```

##### ↳ ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-04-17T12:11:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113765117.660583.96040@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1113730964.213376.70720@o13g2000cwo.googlegroups.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com> <1113730964.213376.70720@o13g2000cwo.googlegroups.com>`

```
For those who haven't noticed, my proposed solution was designed for
compilers on:

 Quote:
(IBM mainframe COBOLII or later)

While any byte value can be used here to provide the missing sign,
prudence dictated the use of X'0C' in the event the field may need
future manipulation.

A divide by 10 would return the packed field to its orig value.
```

##### ↳ ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-04-18T02:15:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1165dec9l9l654f@news.supernews.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com> <1113730964.213376.70720@o13g2000cwo.googlegroups.com>`

```
Robert Jones wrote:
> ssb wrote:
>> Hi,
…[23 more quoted lines elided]…
> bytes.

I think the original creator of the file didn't want to lose a half-byte on 
no stinkin' sign - that is, this is not a "true" packed number. More like a 
home-brew "compressed" number.

I'd do it:

01  FUNNY-NUMBER.
   02  FUNNY-ORIGINAL  PIC X(5).
   02  Filler X Value X'OC'.
01  REAL-NUMBER REDEFINES FUNNY-NUMBER PIC S9(11) COMP-3.

Move ORIGINAL-NUMBER To FUNNY-ORIGINAL.
Compute REALLY-REAL-NUMBER = REAL-NUMBER / 10.
```

#### ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-04-29T23:52:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-D23B26.23525729042005@ispnews.usenetserver.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com>`

```
In article <1113616966.172135.175650@o13g2000cwo.googlegroups.com>,
 "ssb" <mail_ssb@yahoo.com> wrote:

> Hi,
> 
…[13 more quoted lines elided]…
> Any suggestions/help..? Thanks.

77 I        Pic S9(8) comp.
77 X        Pic S9(4) comp.
77 Y        Pic S9(4) comp.
77 Z        Pic S9(4) comp.
77 HEX      Pic X(16) value '0123456789abcdef'.
77 WS-A-OUT Pic X(10).

Perform varying I from 1 by 1
  until I > length of WS-A

  Move 0 to X Y Z  
  Move WS-A (I:1) to X (2:1)
  Divide X by 16 giving Y remainder Z
  Move HEX (Y:1) to WS-A-OUT (I*2:1)
  Move HEX (Z:1) to WS-A-OUT (I*2+1:1)

End-Perform

Happy hacking --- btw, there is one small gotcha left as an exercise for 
the reader...
```

##### ↳ ↳ Re: convert packed CHAR to unpacked DIGIT

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-04-30T17:17:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n4Pce.1178029$6l.1109083@pd7tw2no>`
- **In-Reply-To:** `<joe_zitzelberger-D23B26.23525729042005@ispnews.usenetserver.com>`
- **References:** `<1113616966.172135.175650@o13g2000cwo.googlegroups.com> <joe_zitzelberger-D23B26.23525729042005@ispnews.usenetserver.com>`

```
Joe Zitzelberger wrote:
> In article <1113616966.172135.175650@o13g2000cwo.googlegroups.com>,
>  "ssb" <mail_ssb@yahoo.com> wrote:
…[39 more quoted lines elided]…
> the reader...

Does this help at all ? I suggested following to somebody :-

One immediate possibility is dabble with the intrinsic functions :-
------------------------------------------
Program-id. StringTest.

Working-storage section.
01 ws-50 pic x(50) value "-1234.567".
01 ws-Number pic s9(09)v9(03).

Procedure Division.
compute ws-Number = function numval (ws-50)
display ws-Number.
------------------------------------------

Patrick Magee, (M/F), went even one better :-

The following should work.

working-storage section.
77 wx50 pic x(50).
77 W9S9V3 PIC S9(09)V999 value zero.
procedure division.
MOVE "-2,345.67" TO WX50
move function numval(wx50) to W9S9V3
stop run.
-----------------------------------------

The only thing to watch out for in the above is that if your sending 
field contains any alpha, then the function will return a result of zero.

Jimmy Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
