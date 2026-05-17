[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Comp-3, who can help me!

_9 messages · 9 participants · 1998-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Cobol Comp-3, who can help me!

- **From:** "torsten..." <ua-author-8001365@usenetarchives.gap>
- **Date:** 1998-06-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

Hallo

I'm not a expert in cobol.
I have to read data-files using COBOL comp-3 format.
Who can send me a describtion or other help!
Please direct to me.

Torsten Herrmann
eMail: Tor··.@t-o··e.de

thanks

-----
This Message was send via Microsoft Mail and News
```

#### ↳ Re: Cobol Comp-3, who can help me!

- **From:** "dave johnson" <ua-author-6589126@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6lrenj$5e$1@news00.btx.dtag.de>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

Torsten Herrmann wrote in message <6lrenj$5e$1.··.@new··g.de>...
› Hallo
› 
…[12 more quoted lines elided]…
› This Message was send via Microsoft Mail and News

a minor addition to the other posts - watch out for COMP-3 fields in Adabas
descriptors as it prefers 'F' as the positive sign instead of (the more
usual) 'C'. (if you don't know what Adabas is, it won't trip you up!).
DaveJ.
```

#### ↳ Re: Cobol Comp-3, who can help me!

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6lrenj$5e$1@news00.btx.dtag.de>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

Torsten Herrmann (Tor··.@t-o··e.de) wrote:
: Hallo
: I'm not a expert in cobol.
: I have to read data-files using COBOL comp-3 format.
: Who can send me a describtion or other help!
: Please direct to me.
: Torsten Herrmann
: eMail: Tor··.@t-o··e.de
: thanks
----------------------------------


Comp-3 contains two digits per byte, except for the rightmost byte,
which contains 1 digit and a sign (each digit is made up of 4 binary
bits).

For instance, if you defined an item as pic S9(5) comp-3, then
the definition would be:

99999S (9's are digit positions and S is the sign).

If you did not specify a sign in the picture, the sign value would
always be positive.

If the definition is pic 9(6) comp-3, then the def. is:

9999999S (notice that the number of digits is always odd, in this
case, one more than in the pic)

One caution: If the data was created by a program compiled by a
different compiler, make sure that the same sign values
are created/recognized by both programs.
```

#### ↳ Re: Cobol Comp-3, who can help me!

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6lrenj$5e$1@news00.btx.dtag.de>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

In article <6lrenj$5e$1.··.@new··g.de>, Tor··.@t-o··e.de
(Torsten Herrmann) writes:

› I have to read data-files using COBOL comp-3 format.
› Who can send me a describtion or other help!

On which platform? "USAGE IS COMPUTATIONAL-3 (usually the whole phrase is
abbreviated down to COMP-3) can vary between platforms.

On an IBM mainframe, COMP-3 is packed decimal, which has two digits per byte of
storage (hex 0 for 0 through hex 9 for 9), except that the low-order 4 bits of
the rightmost byte has a sign code (hex C for positive, hex D for negative, hex
F or all four bits on to represent unsigned but internally will be treated as
positive for purposes of movement or comparison). In hex dumps, packed numbers
are fairly easy to read, e.g., a hex dump value of 0001234C is positive 1234,
but one has to consult the PICTURE clause to see where the implied decimal goes
(e.g., PIC S9(5)V99 COMP-3 would mean the above dump value is positive 12.34).
If an even total number of digits is specified, the number will be extended to
the left by one digit but will be treated as if that extra digit is 0, which is
why many shops recommend that if a number is COMP-3, the total number of digits
should be odd.

COMP-3 fields are probably the second most efficient way of handling numbers
(COMP or binary being the most efficient), but COMP-3 fields have the advantage
that they are in the form that IBM mainframes need for "editing" fields for
display purposes (e.g., suppress leading zeroes, adding punctuation), which, in
addition to ease of reading in dumps, is why COMP-3 is very commonly used on
IBM mainframes. (For "editing" numbers for display purposes, if the number is
not COMP-3, the code on IBM mainframes have to convert it to COMP-3 first and
then it can do its ED or EDMK instruction on it. Likewise, for decimal math,
the work has to be done in either COMP-3 or binary--display fields have to be
packed to COMP-3 before math can be done, and UNPKed to convert back to display
format.)

(The above discussion is ignoring floating point types, which if I recall
correctly, are COMP-1 and COMP-2 on IBM mainframes.)

Mark A. Young
```

#### ↳ Re: Cobol Comp-3, who can help me!

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6lrenj$5e$1@news00.btx.dtag.de>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

Torsten,

As told by Jack Yazel and Mark A. Young, COMP-3 stores 2 bytes per
digit, sign separately in the last half byte. Both gentlemen told about
odd and even numbers of digits.

HOWEVER ...

These stories are perfectly well on IBM mainframe hardware. On OTHER
vendor's hardware it soes not hold.

EXAMPLE:

Bull h/w stores COMP-3 as 2 digits per byte, totally WITHOUT a sign if
no S is in the COBOL picture. These fields should have an EVEN number of
digits to fit in a whole number of bytes. When signed, the COMP-3 fields
are much the same as with IBM.

So, what platform are you on?

(Also COMP-1 and COMP-2 are NOT floating point on Bull)

The Frog
```

#### ↳ Re: Cobol Comp-3, who can help me!

- **From:** "ram..." <ua-author-6589307@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6lrenj$5e$1@news00.btx.dtag.de>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

You need to state platform. The following is for IBM/MVS mainframes.

COMP-3 is a way to store numbers in a smaller amount of space, plus gain
addition speed.

Numbers can be stored in varying formats, all depending on how the pic clause
is used.
A - PIC 999 - stores the number in display format, each digit taking up
one byte of space. IF little math is going to be performed and the number is
going to be printed or displayed on the screen this is the most efficient way
(since before a number can be printed to a report or displayed it has to be
converted to display format). However, the disadvantage is that it takes up
more space and is much slower for math that other storage formats.

To deal with this, IBM developed several alternate formats. There most most
common are
comp-3 (- pic 9999 comp-3 ) (packed decimal) stores two digits per byte plus
one for the sign
comp(Bianry) (- pic 99999 comp ) stores binary representation one byte per
number
plus some other little used formats

The most common usage is comp-3 for several reasons.
Storage:
Numbers take up about 1/2 as much space as comp or display format. So
to figure out the size in display format, double it and add one. So a pic
999 comp-3 will be 3*2 bytes + 1= pic 9999999. Even these days with much
cheaper storage, needing 1/2 as much space is a serious advantage. Also
companies can use the saving to purchase more sophisticated DASD systems.

Speed
While comp(binary) theortically would give the fastest way to handle numbers,
on many IBM CPUS comp-3 can work directly with the math registers without
conversion, thus giving better performance than comp (comp is converted to
comp-3 before being manipulated and then back again). The main usage of comp
has been to obtain higher precision(comp-1 and comp-2 on some systems are for
single and double precision). Since most work on IBM systems is for business,
there is seldom a need to use comp. The possible exception is for subscripts
or indexes. On many systems they will before faster with comp usage.

There is no special technique to handling comp-3 numbers. If you move a
comp-3 to display format or vica versa, as long as each field has enough
space, the conversion is automatic. You can work with comp-3 directly just
like any other pic 9 field.

Tip: if you are in ISPF, edit or browse the dataset with HEX ON, it will
allow you to see how much space is being taken up by the comp-3 field, without
having to do a print dump.





In article <6lrenj$5e$1.··.@new··g.de>, Tor··.@t-o··e.de
(Torsten Herrmann) wrote:
› Hallo
› 
…[9 more quoted lines elided]…
› 

Dan Ramriez


ram··.@mai··e.com
Development Analyst
Information Systems
Commonwealth Edison

The contents of this message express only the sender's opinion. This message does not necessarily reflect the policy or views of my employer, Commonwealth Edison. All responsibility for the statements made in this Usenet posting resides solely and completely with the sender.
```

#### ↳ Re: Cobol Comp-3, who can help me!

- **From:** "co..." <ua-author-17075254@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6lrenj$5e$1@news00.btx.dtag.de>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de>`

```

› 
› I'm not a expert in cobol.
…[3 more quoted lines elided]…
› 

I assume you mean IBM mainframe packed decimal. Packed decimal
is not, is not, is not, is not a COBOL format!!!!

Packed decimal is built into the hardware of IBM mainframe machines.
There are specific machine language instructions to manipulate
packed data. COMP-3 is how COBOL impliments the USE of packed decimal.

1 byte = 2 decimal numbers expect the low order byte which contain 1
decimal number plus the sign. The sign can be x'C' positive, x'D'
negative or x'F' absolute value. Example the number +123 looks like
x'123C'. In cobol this is PIC S9(3) COMP-3. You specify the number of
digits NOT the number of bytes.

If you are referring to something other than an IBM mainframe, all,
some or none of this may apply.
```

##### ↳ ↳ Re: Cobol Comp-3, who can help me!

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cc76af4f65-p7@usenetarchives.gap>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de> <gap-cc76af4f65-p7@usenetarchives.gap>`

```

I agree entirely that what "COMP-3" means is very much implementor specific
however, in reply to,

› Packed decimal
› is not, is not, is not, is not a COBOL format!!!!
›


That is simply more than a decade wrong. "USAGE PACKED-DECIMAL" has been a
part of Standard COBOL since 1985. How (exactly) it is implemented may
still vary from implementation (COBOL compiler, not hardware or software) to
implementation - but any compiler that claims to support ANSI/ISO/FIPS
syntax MUST support it (and must have been supporting it for over a decade).
```

###### ↳ ↳ ↳ Re: Cobol Comp-3, who can help me!

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-06-14T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc76af4f65-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cc76af4f65-p8@usenetarchives.gap>`
- **References:** `<6lrenj$5e$1@news00.btx.dtag.de> <gap-cc76af4f65-p7@usenetarchives.gap> <gap-cc76af4f65-p8@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› I agree entirely that what "COMP-3" means is very much implementor specific
…[10 more quoted lines elided]…
› syntax MUST support it (and must have been supporting it for over a decade).

How it's implemented may be exactly the same as DISPLAY. In fact does
the standard say anything to prevent an implementor from using BINARY to
mean packed decimal or PACKED-DECIMAL to mean binary? This implementor
dependant stuff is inherently quite vague.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net             Bar··.@att··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \          Extremism in the defense of liberty is no vice
e    |\        Moderation in the pursuit of justice is no virtue
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ Secret of the 1,2,3,4,25 Sequence revealed!  And a new puzzle!
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
